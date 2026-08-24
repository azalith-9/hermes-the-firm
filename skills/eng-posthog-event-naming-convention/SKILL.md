---
name: eng-posthog-event-naming-convention
description: Use when instrumenting user-facing features in the legal AI product with PostHog analytics events. Defines the canonical event taxonomy, naming rules, property schemas, and anti-patterns so that all engineers emit consistent, queryable telemetry that supports product decisions, eval pipelines, and compliance audits.
license: MIT
metadata: " id: eng.posthog-event-naming-convention category: eng jurisdictions: [__multi__] priority: P2 intent: [__eng__, analytics, posthog, telemetry, events] related: [eng-supabase-edge-functions-patterns, eng-token-budget-by-tier, eval-benchmark-runner, eval-leaderboard-updater] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'eng'.
Registered as a flat plugin skill.
-->


# PostHog Event Naming Convention

## What it does

This skill defines the canonical naming convention, property schema, and governance rules for all PostHog analytics events emitted by the legal AI product. Consistent event naming is the prerequisite for building reliable funnels, feature-flag cohorts, and the LLM quality trend dashboard that feeds [[eval-leaderboard-updater]].

## Setup / auth

PostHog project is configured via:
- `POSTHOG_KEY` — public client-side key (safe to expose in frontend)
- `POSTHOG_HOST` — self-hosted or `app.posthog.com`
- `POSTHOG_SERVER_KEY` — server-side key for Edge Function calls (never expose to browser)

All events must include `distinct_id` (the user's UUID, never email/name in the event itself — PII goes through [[eng-pii-redaction-preprocessor]]).

## Capabilities

### Naming structure

```
<noun>_<verb>
```

- **Noun** is the product object: `session`, `skill`, `document`, `chat`, `nda`, `contract`, `user`, `workspace`, `billing`, `eval`.
- **Verb** is the past-tense action: `started`, `completed`, `failed`, `viewed`, `clicked`, `upgraded`, `cancelled`.
- Always lowercase, words joined with `_`.
- No "clicked" or "viewed" as the sole event name — always include a noun: `button_clicked` is useless; `skill_selector_clicked` is queryable.

### Event taxonomy

#### Session & auth

| Event | When |
|---|---|
| `session_started` | User opens the app (not page load) |
| `session_ended` | Tab close or 30-min idle |
| `user_signed_up` | First auth completion |
| `user_signed_in` | Every subsequent auth |
| `user_invited` | Invite link sent |
| `workspace_created` | New workspace provisioned |

#### Chat & skill routing

| Event | When |
|---|---|
| `chat_message_sent` | User sends any message |
| `chat_response_received` | First token streamed back |
| `chat_response_completed` | Stream ends |
| `skill_routed` | Router resolves a skill |
| `skill_fallback_triggered` | No skill matched; fell back to generic |
| `chat_error_occurred` | Any non-2xx from LLM |

#### Document workflow

| Event | When |
|---|---|
| `document_uploaded` | File ingestion starts |
| `document_indexed` | Embedding complete |
| `document_reviewed` | Review skill output delivered |
| `document_drafted` | Draft skill output delivered |
| `document_downloaded` | User exports a document |

#### Billing & tier

| Event | When |
|---|---|
| `upgrade_prompted` | User hits a tier gate |
| `upgrade_completed` | Subscription activated |
| `upgrade_abandoned` | User dismissed upgrade modal |
| `api_key_saved` | BYO-key entered |
| `token_budget_exhausted` | Monthly token limit hit |

#### Eval (server-side only)

| Event | When |
|---|---|
| `eval_run_started` | Benchmark run begins |
| `eval_run_completed` | All rubrics scored |
| `eval_regression_detected` | Any rubric dropped threshold |

### Required properties on every event

```typescript
{
  distinct_id: string;       // user UUID
  tenant_id: string;         // workspace/firm UUID
  session_id: string;        // current session UUID
  platform: "web" | "ios" | "android";
  app_version: string;       // semver
  environment: "production" | "staging" | "local";
}
```

### Per-event additional properties

#### `chat_message_sent`
```typescript
{
  message_length_chars: number;
  language_detected: "ar" | "en" | "fr" | "mixed";
  has_attachment: boolean;
}
```

#### `skill_routed`
```typescript
{
  skill_id: string;          // e.g. "draft-nda-unilateral"
  skill_category: string;    // e.g. "draft"
  confidence: number;        // router confidence 0-1
  latency_ms: number;
}
```

#### `chat_response_completed`
```typescript
{
  skill_id: string;
  tokens_input: number;
  tokens_output: number;
  latency_ms: number;
  tier: "free" | "pro" | "business" | "byo";
  rubric_score?: number;     // if real-time eval enabled
}
```

## Usage patterns

### Frontend (React)

```typescript
import posthog from "posthog-js";

posthog.capture("skill_routed", {
  skill_id: routedSkill.id,
  skill_category: routedSkill.category,
  confidence: routedSkill.confidence,
  latency_ms: Date.now() - startTime,
});
```

### Edge Function (server-side)

```typescript
import { PostHog } from "posthog-node";
const ph = new PostHog(Deno.env.get("POSTHOG_SERVER_KEY")!);

ph.capture({
  distinctId: userId,
  event: "eval_run_completed",
  properties: {
    tenant_id: tenantId,
    run_id: runId,
    aggregate_score: score,
    regression_detected: hasRegression,
    environment: "production",
  },
});
await ph.shutdown();
```

## Permissions & safety

- Never include raw user message content in event properties. Use `message_length_chars` instead.
- Never include full names, email addresses, or phone numbers in event properties. Use UUIDs.
- `environment: "local"` events should not appear in the production PostHog project. Gate on env var.
- Billing events (`upgrade_completed`) must be cross-validated against Stripe webhook receipts.

## Failure modes

| Failure | Impact | Mitigation |
|---|---|---|
| Missing `tenant_id` | Can't segment by firm | Assert required properties at emit site via TypeScript type |
| Duplicate events | Inflated metrics | Deduplicate on `session_id + event + timestamp` in PostHog |
| Events in local env polluting production | Noisy dashboards | Set `environment` filter on all saved insights |
| PII in properties | Privacy violation | Lint rule: reject any property containing `email`, `name`, `phone` |

## Related skills

- [[eng-pii-redaction-preprocessor]] — ensures message content is never passed raw to analytics
- [[eng-token-budget-by-tier]] — tier and budget data feeds `chat_response_completed` properties
- [[eval-benchmark-runner]] — consumes `eval_run_*` events
- [[eval-leaderboard-updater]] — reads PostHog quality-trend data
