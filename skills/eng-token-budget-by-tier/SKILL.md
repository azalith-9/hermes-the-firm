---
name: eng-token-budget-by-tier
description: Use when implementing or configuring the per-tier token budget system that limits LLM usage by subscription plan. Defines the monthly token allowances per tier, enforcement logic, overage handling, BYO-key bypass rules, and the Edge Function middleware that gates requests before they reach the LLM.
license: MIT
metadata: " id: eng.token-budget-by-tier category: eng jurisdictions: [__multi__] priority: P2 intent: [__eng__, billing, token-budget, rate-limiting, tier] related: [eng-supabase-edge-functions-patterns, eng-streaming-response-rules-mobile, eng-posthog-event-naming-convention] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'eng'.
Registered as a flat plugin skill.
-->


# Token Budget by Tier

## What it does

Every LLM call costs tokens; token costs must be controlled per subscription tier. The token budget system tracks monthly token consumption per user/workspace, enforces hard limits before requests reach the LLM API, and provides the data the frontend needs to display usage warnings. It also handles the BYO-key (Bring Your Own Key) path, where the user's own Anthropic API key is used and platform token limits do not apply.

## Setup / auth

Supabase schema:
```sql
CREATE TABLE token_usage (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES auth.users(id),
  workspace_id UUID NOT NULL REFERENCES workspaces(id),
  period TEXT NOT NULL,        -- "2026-05" (YYYY-MM)
  tokens_input INT NOT NULL DEFAULT 0,
  tokens_output INT NOT NULL DEFAULT 0,
  tokens_total INT GENERATED ALWAYS AS (tokens_input + tokens_output) STORED,
  last_updated TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  UNIQUE(user_id, workspace_id, period)
);

-- RLS: users see only their own usage
ALTER TABLE token_usage ENABLE ROW LEVEL SECURITY;
CREATE POLICY "own usage" ON token_usage FOR SELECT
  USING (user_id = auth.uid());
```

## Capabilities

### Tier definitions

| Tier | Monthly token budget | Model access | Notes |
|---|---|---|---|
| `free` | 20,000 tokens | claude-haiku only | Resets on 1st of month |
| `pro` | 500,000 tokens | claude-sonnet | Resets on billing anchor date |
| `business` | 3,000,000 tokens | claude-sonnet + opus on request | Workspace-level pool |
| `byo` | Unlimited (user's own key) | Any model | Platform does not count tokens |
| `internal` | Unlimited | Any model | Dev/test accounts |

Token counts are **input + output combined** (total tokens billed). Cache reads count at 10% weight (Anthropic prompt caching discount).

### Budget check middleware

```typescript
async function checkTokenBudget(userId: string, tier: Tier, estimatedTokens: number): Promise<BudgetResult> {
  if (tier === "byo" || tier === "internal") return { allowed: true, remaining: Infinity };

  const period = getCurrentPeriod();  // "2026-05"
  const budget = TIER_BUDGETS[tier];

  const { data } = await supabase
    .from("token_usage")
    .select("tokens_total")
    .eq("user_id", userId)
    .eq("period", period)
    .single();

  const used = data?.tokens_total ?? 0;
  const remaining = budget - used;

  if (remaining <= 0) return { allowed: false, remaining: 0, reason: "budget_exhausted" };
  if (estimatedTokens > remaining) return { allowed: false, remaining, reason: "request_too_large" };

  return { allowed: true, remaining };
}
```

### Token recording (post-call)

After every successful LLM response, upsert the usage record:

```typescript
async function recordTokenUsage(userId: string, workspaceId: string, usage: { input: number; output: number }) {
  const period = getCurrentPeriod();
  await supabase.rpc("increment_token_usage", {
    p_user_id: userId,
    p_workspace_id: workspaceId,
    p_period: period,
    p_input: usage.input,
    p_output: usage.output,
  });
}
```

SQL function (atomic upsert):
```sql
CREATE FUNCTION increment_token_usage(
  p_user_id UUID, p_workspace_id UUID, p_period TEXT,
  p_input INT, p_output INT
) RETURNS VOID LANGUAGE SQL AS $$
  INSERT INTO token_usage(user_id, workspace_id, period, tokens_input, tokens_output)
  VALUES (p_user_id, p_workspace_id, p_period, p_input, p_output)
  ON CONFLICT (user_id, workspace_id, period)
  DO UPDATE SET
    tokens_input = token_usage.tokens_input + EXCLUDED.tokens_input,
    tokens_output = token_usage.tokens_output + EXCLUDED.tokens_output,
    last_updated = NOW();
$$;
```

### BYO-key path

When a user has configured a BYO Anthropic key:
1. The Edge Function decrypts the stored key from Supabase Vault.
2. The key is used in the Anthropic API call instead of the platform key.
3. `checkTokenBudget` returns `{ allowed: true, remaining: Infinity }` immediately.
4. Token usage is still recorded locally (for analytics) but not enforced as a limit.
5. The PostHog event `chat_response_completed` includes `tier: "byo"`.

### Usage API endpoint

```typescript
GET /api/usage
→ {
    tier: "pro",
    period: "2026-05",
    tokensUsed: 123456,
    tokensBudget: 500000,
    tokensRemaining: 376544,
    percentUsed: 24.7,
    resetDate: "2026-06-01"
  }
```

This feeds the frontend usage display and [[eng-streaming-response-rules-mobile]] token pill.

## Permissions & safety

- Budget enforcement must happen **server-side** in the Edge Function, before any LLM call. Client-side budget checks are for UX only, never for enforcement.
- The `tokens_total` column is a generated column — it cannot be manipulated by application code.
- Do not expose the raw `token_usage` table via the public REST API. Use a dedicated `/api/usage` endpoint that returns only the user's own data.
- Overage: if `checkTokenBudget` returns `allowed: false`, return HTTP 402 with `{ error: "token_budget_exhausted", upgradeUrl: "/billing/upgrade" }`.

## Failure modes

| Failure | Impact | Mitigation |
|---|---|---|
| Token recording fails (DB error) | Usage under-counted; budget not enforced | Log failure; retry async; set usage = budget as conservative fallback |
| Budget check skipped for BYO tier | Fine by design; but must verify tier correctly | Always resolve tier from DB, not from JWT claim which could be stale |
| Period boundary race condition | User gets double budget on month boundary | Upsert with `ON CONFLICT` handles this; period key is YYYY-MM |
| Estimated tokens wildly wrong | Request allowed but exceeds budget | Estimate conservatively (2× average); record actual after call |

## Related skills

- [[eng-supabase-edge-functions-patterns]] — the Edge Function that runs the budget check
- [[eng-streaming-response-rules-mobile]] — displays remaining budget in the chat UI
- [[eng-posthog-event-naming-convention]] — `token_budget_exhausted` event definition
