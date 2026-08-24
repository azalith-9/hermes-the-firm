---
name: eng-cost-per-message-tracker
description: Use when building or reviewing the cost accounting layer for a legal AI product — tracking LLM API spend at the granularity of individual requests, skills, matters, users, and tenants. Defines the cost record schema, aggregation dimensions, alerting thresholds, and the connection to the billing model (BYO key vs. platform key). Engineering skill relevant to any the agent-based legal AI deployment.
license: MIT
metadata: " id: eng.cost-per-message-tracker category: eng jurisdictions: [__multi__] priority: P2 intent: [cost, LLM-billing, observability, spend-tracking, token-usage] related: - eng-context-cache-key-design - eng-latency-slo-by-skill - eng-langfuse-trace-inspector - eng-fallback-model-cascade source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'eng'.
Registered as a flat plugin skill.
-->


# Cost per Message Tracker

## What it does

Every LLM API request has a cost: `(input_tokens × input_price) + (output_tokens × output_price)`, adjusted for cached vs. uncached tokens. In a legal AI product serving law firms, cost tracking serves several purposes:

1. **Unit economics**: know the cost per skill invocation to price the product sustainably.
2. **Anomaly detection**: a runaway conversation or a prompt injection that inflates token count must be caught in near-real-time.
3. **Tenant billing**: on BYO-key models, the user pays directly; on platform-key models, the platform must track costs by tenant to apply margin.
4. **Optimization signal**: which skills, matter types, or interaction patterns are most expensive? Where does caching help most?
5. **Budget enforcement**: law firms operate under cost budgets; provide per-matter or per-user cost caps with alerts.

## Cost record schema

Emit one record per LLM API call:

```json
{
  "cost_record_id": "ulid",
  "timestamp": "ISO-8601 UTC",
  "org_id": "org_xxx",
  "user_id": "usr_xxx",
  "session_id": "sess_xxx",
  "matter_id": "matter_xxx | null",
  "skill_id": "efirm-conflict-check | null",
  "skill_version": "1.0",
  "model_id": "claude-sonnet-4-6",
  "model_provider": "anthropic",
  "trace_id": "langfuse-trace-id",
  "request_id": "req_xxx",
  "tokens": {
    "input_total": 14823,
    "input_cached": 12400,
    "input_uncached": 2423,
    "output": 1247,
    "cache_creation": 0
  },
  "cost_usd": {
    "input_uncached": 0.00728,
    "input_cached": 0.00124,
    "output": 0.01871,
    "total": 0.02723
  },
  "latency_ms": {
    "ttfb": 387,
    "total": 4821
  },
  "cache_hit": {
    "l1_system": true,
    "l2_skills": true,
    "l3_matter": false
  }
}
```

## Price table (Anthropic the agent — reference; verify against current pricing)

Prices vary by model and change over time. The tracker should pull from a versioned price table, not hardcode:

```json
{
  "claude-sonnet-4-6": {
    "input_uncached_per_mtok": 3.00,
    "input_cached_per_mtok": 0.30,
    "output_per_mtok": 15.00,
    "cache_write_per_mtok": 3.75
  },
  "claude-haiku-3-5": {
    "input_uncached_per_mtok": 0.80,
    "input_cached_per_mtok": 0.08,
    "output_per_mtok": 4.00,
    "cache_write_per_mtok": 1.00
  }
}
```

Store the price table in configuration, versioned by effective date. Recompute historical costs if Anthropic changes pricing.

## Aggregation dimensions

Query cost records at any granularity:

| Dimension | Use case |
|---|---|
| `org_id` | Tenant-level billing; cost allocation |
| `user_id` | Per-user spend report; anomaly detection |
| `matter_id` | Cost per legal matter; matter profitability analysis |
| `skill_id` | Cost per skill; identify expensive skills for optimization |
| `model_id` | Compare model costs; fallback cascade analysis |
| `session_id` | Session cost; detect runaway sessions |
| `date` | Daily/monthly spend reporting; budget tracking |
| `cache_hit.l2_skills` | Cache efficiency; savings from caching |

## Alerting thresholds

| Alert | Condition | Action |
|---|---|---|
| Single request cost spike | Request cost > $[threshold, e.g., $1.00] | Immediate alert to eng-on-call; review for prompt injection or context explosion |
| Daily org spend > budget | Daily cost > org's configured limit | Alert org admin; optionally suspend new requests |
| Session cost > cap | Accumulated session cost > $[cap] | Warn user; optionally require confirmation to continue |
| Cache hit rate drops | L1 or L2 hit rate < 80% over 1 hour | Investigate cache invalidation or key design issue |
| Model fallback spike | Fallback rate > 20% in 15 min | Investigate primary model availability ([[eng-fallback-model-cascade]]) |

## BYO key vs. platform key implications

| Mode | Cost tracking responsibility | Billing implication |
|---|---|---|
| BYO key (user provides API key) | User pays Anthropic directly; platform tracks for UX/reporting only | No platform cost; track for usage analytics and rate-limit management |
| Platform key (platform absorbs) | Platform pays Anthropic; must track by tenant to recover cost | Cost tracking is financial — must be accurate for margin calculation |

On a BYO-key model (Louis's product decision), the tracker still runs but generates cost visibility reports for the user rather than for internal billing recovery. This transparency is a feature — law firms want to understand their AI spend.

## Matter-level cost reporting

For law firms using the platform, expose a per-matter cost view:

```
MATTER AI COST REPORT — [Matter ID] — [Period]

Total LLM cost:         $X
Cost by skill:
  efirm-conflict-check:        $A
  efirm-engagement-letter-draft: $B
  efirm-deadline-tracker:      $C
  Other:                       $D
  
Avg cost per session:   $Y
Most expensive session: $Z on [Date] — [Skill] — [Brief context]

Cache savings:          $S  (vs. uncached baseline)
```

This view helps partners understand the economic value of the AI system relative to time saved.

## Integration with Langfuse

Cost records should be emitted as custom scores or metadata on Langfuse traces (see [[eng-langfuse-trace-inspector]]). This enables cost analysis alongside quality scores and latency data in a single observability tool.

## Related skills

- [[eng-context-cache-key-design]]
- [[eng-latency-slo-by-skill]]
- [[eng-langfuse-trace-inspector]]
- [[eng-fallback-model-cascade]]
- [[eng-audit-log-schema]]
