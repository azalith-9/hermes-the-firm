---
name: eng-supabase-edge-functions-patterns
description: Use when writing, deploying, or debugging Supabase Edge Functions (Deno runtime) for the legal AI backend. Covers authentication patterns, CORS configuration, structured error handling, JWT validation, calling external APIs (Anthropic, PostHog), and patterns specific to multi-tenant legal AI workloads.
license: MIT
metadata: " id: eng.supabase-edge-functions-patterns category: eng jurisdictions: [__multi__] priority: P2 intent: [__eng__, supabase, edge-functions, deno, serverless] related: [eng-tenant-isolation-row-level-security, eng-supabase-index-knowledge-pipeline, eng-streaming-response-rules-mobile, eng-pii-redaction-preprocessor] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'eng'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Supabase Edge Functions Patterns

## What it does

Supabase Edge Functions are Deno-based serverless functions deployed to the global Supabase edge network. In this legal AI product they handle: LLM proxying (streaming chat), document ingestion, PII redaction, billing webhooks, and eval runs. This skill documents the canonical patterns all Edge Functions in the project must follow.

## Setup / auth

```bash
supabase functions new my-function
supabase functions deploy my-function --no-verify-jwt   # only for public webhooks
supabase secrets set ANTHROPIC_API_KEY=sk-ant-...
```

Every function that handles user requests must verify the Supabase JWT:

```typescript
import { createClient } from "https://esm.sh/@supabase/supabase-js@2";

const supabase = createClient(
  Deno.env.get("SUPABASE_URL")!,
  Deno.env.get("SUPABASE_ANON_KEY")!,
  { global: { headers: { Authorization: req.headers.get("Authorization")! } } }
);

const { data: { user }, error } = await supabase.auth.getUser();
if (error || !user) return new Response("Unauthorized", { status: 401 });
```

Do **not** use the service role key for user-facing functions. It bypasses RLS.

## Capabilities

### Standard function skeleton

```typescript
import { corsHeaders } from "../_shared/cors.ts";

Deno.serve(async (req: Request) => {
  // CORS pre-flight
  if (req.method === "OPTIONS") {
    return new Response(null, { headers: corsHeaders });
  }

  try {
    // 1. Auth
    const user = await verifyUser(req);

    // 2. Parse & validate input
    const body = await req.json();
    const parsed = InputSchema.safeParse(body);
    if (!parsed.success) {
      return errorResponse(400, "Invalid input", parsed.error);
    }

    // 3. Business logic
    const result = await doWork(user, parsed.data);

    // 4. Return
    return new Response(JSON.stringify(result), {
      headers: { ...corsHeaders, "Content-Type": "application/json" },
    });
  } catch (err) {
    return errorResponse(500, "Internal error", err);
  }
});
```

### CORS headers (`_shared/cors.ts`)

```typescript
export const corsHeaders = {
  "Access-Control-Allow-Origin": Deno.env.get("ALLOWED_ORIGIN") ?? "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};
```

In production, set `ALLOWED_ORIGIN` to the app's domain. Wildcard `*` is acceptable for staging only.

### Streaming response pattern (LLM proxy)

```typescript
Deno.serve(async (req: Request) => {
  const user = await verifyUser(req);
  const { message } = await req.json();

  const anthropicStream = await fetch("https://api.anthropic.com/v1/messages", {
    method: "POST",
    headers: {
      "x-api-key": Deno.env.get("ANTHROPIC_API_KEY")!,
      "anthropic-version": "2023-06-01",
      "content-type": "application/json",
    },
    body: JSON.stringify({
      model: "claude-sonnet-4-5",
      max_tokens: tokenBudget(user.tier),
      stream: true,
      messages: [{ role: "user", content: message }],
    }),
  });

  return new Response(anthropicStream.body, {
    headers: {
      ...corsHeaders,
      "Content-Type": "text/event-stream",
      "Cache-Control": "no-store",
    },
  });
});
```

### Error response helper

```typescript
function errorResponse(status: number, message: string, detail?: unknown): Response {
  console.error({ status, message, detail });
  return new Response(
    JSON.stringify({ error: message, detail: detail instanceof Error ? detail.message : detail }),
    { status, headers: { ...corsHeaders, "Content-Type": "application/json" } }
  );
}
```

### Environment variable patterns

| Variable | Scope | Notes |
|---|---|---|
| `SUPABASE_URL` | Auto-injected | Do not set manually |
| `SUPABASE_ANON_KEY` | Auto-injected | Use for user-context clients |
| `SUPABASE_SERVICE_ROLE_KEY` | Secret | Use only for admin functions (billing webhooks) |
| `ANTHROPIC_API_KEY` | Secret | Never log |
| `POSTHOG_SERVER_KEY` | Secret | Never log |
| `ALLOWED_ORIGIN` | Secret | Per-env |

## Usage patterns

### Pattern — Calling Anthropic with per-user BYO key

```typescript
const apiKey = user.byoKey
  ? await decryptBYOKey(user.byoKeyEncrypted)
  : Deno.env.get("ANTHROPIC_API_KEY")!;
```

Never store a decrypted BYO key in any log or variable that persists beyond the request lifecycle.

### Pattern — Database insert with RLS context

```typescript
// Using anon key + JWT = RLS enforced automatically
const { error } = await supabase
  .from("chat_messages")
  .insert({ user_id: user.id, content: redactedMessage, created_at: new Date() });
```

### Pattern — Invoking another Edge Function

```typescript
const res = await supabase.functions.invoke("pii-redactor", {
  body: { text: rawMessage },
});
```

## Permissions & safety

- Use `SUPABASE_ANON_KEY` (+ JWT) for all user-facing functions. The JWT propagates to RLS.
- Use `SUPABASE_SERVICE_ROLE_KEY` only for admin/system functions (e.g., billing webhooks from Stripe that don't have a user JWT). Mark these functions `--no-verify-jwt` in deployment.
- Every function must log its `user.id` and `tenantId` at the start of the request for audit purposes. Never log `Authorization` header or API keys.
- Set a hard timeout: Supabase Edge Functions have a 150-second wall-clock limit. For long operations (render, batch embed), use a Postgres job queue (pg_cron + Supabase Queues) instead of synchronous function calls.

## Failure modes

| Failure | Impact | Mitigation |
|---|---|---|
| Missing CORS pre-flight handler | Browser blocks requests | Always handle `OPTIONS` first |
| Service role key in user function | RLS bypassed; tenant leak | Use anon key by default; require code review for service role |
| Unhandled promise rejection | 500 with no context | Wrap all async work in try/catch; use `errorResponse` helper |
| Cold start latency > 2 s | Poor mobile UX | Keep `_shared/` imports minimal; avoid heavy node_modules |
| JWT not re-validated on reconnect | Stale session serves other user | Re-validate on every reconnect for streaming endpoints |

## Related skills

- [[eng-tenant-isolation-row-level-security]] — RLS policies that Edge Functions must respect
- [[eng-supabase-index-knowledge-pipeline]] — document ingestion Edge Function
- [[eng-streaming-response-rules-mobile]] — mobile streaming endpoint pattern
- [[eng-pii-redaction-preprocessor]] — called as an inner Edge Function from the chat handler
