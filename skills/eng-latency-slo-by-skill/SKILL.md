---
name: eng-latency-slo-by-skill
description: Use when defining, measuring, or debugging latency Service Level Objectives (SLOs) for individual legal AI skills. Different skills have different acceptable latency — a conflict check must be fast; a full engagement letter draft can take longer. Covers the SLO definition framework, measurement approach, p50/p95/p99 targets by skill tier, alerting setup, and common latency root causes in legal AI products.
license: MIT
metadata: " id: eng.latency-slo-by-skill category: eng jurisdictions: [__multi__] priority: P2 intent: [SLO, latency, performance, observability, p99, alerting] related: - eng-langfuse-trace-inspector - eng-fallback-model-cascade - eng-cost-per-message-tracker - eng-context-cache-key-design source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'eng'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Latency SLO by Skill

## What it does

A latency SLO (Service Level Objective) defines the acceptable response time for a skill. Without per-skill SLOs, the only latency metric is "it felt slow" — which cannot drive engineering action. With per-skill SLOs:

- Product knows the experience guarantee for each skill.
- Engineering has a measurable target and an alert threshold.
- The [[eng-fallback-model-cascade]] can use SLO breach as a trigger for model switching.
- Users — law firm staff — understand why some skills stream longer than others.

## SLO taxonomy

Latency is measured at the skill level as end-to-end: from the moment the user's message is received by the API gateway to the moment the first response byte is sent (TTFB) and to the moment the full response is complete (total).

| Metric | Definition |
|---|---|
| `p50_ttfb` | Median time to first byte — 50% of requests faster |
| `p95_ttfb` | 95th percentile TTFB — the "most users" experience |
| `p99_ttfb` | 99th percentile TTFB — worst 1% of requests |
| `p95_total` | 95th percentile total response time |
| `error_rate` | % of requests returning an error |

## SLO targets by skill tier

Assign each skill to a latency tier based on expected usage context:

| Tier | Description | p50 TTFB | p95 TTFB | p99 TTFB | p95 total |
|---|---|---|---|---|---|
| Interactive (T-I) | Real-time chat; user is watching | <500ms | <1.5s | <3s | <8s |
| Workflow (T-W) | Triggered by action; user expects slight wait | <1s | <3s | <6s | <20s |
| Document (T-D) | Full document generation; user expects wait; streaming visible | <2s | <5s | <10s | <60s |
| Batch (T-B) | Background job; user not waiting at terminal | <10s | <30s | <60s | <300s |

### Skill-to-tier assignments

| Skill | Tier | Rationale |
|---|---|---|
| `router.*` | T-I | Must not add noticeable latency to user experience |
| `efirm-conflict-check` | T-W | Triggered by matter creation; partner expects fast result |
| `efirm-client-update-email-draft` | T-W | Lawyer requesting a draft; will review before sending |
| `efirm-deadline-tracker` | T-W | Matter dashboard; should load within a workflow step |
| `efirm-engagement-letter-draft` | T-D | Full document; streaming acceptable |
| `efirm-fee-quote-builder` | T-D | Multi-section document output |
| `efirm-matter-creation-flow` | T-W | Orchestration step; sub-skills have own SLOs |
| `efirm-finance-*` (dashboards) | T-D | Report generation |
| Eval runs | T-B | Background quality evaluation |

## Measurement approach

### Instrumentation

At every skill invocation, emit:

```python
langfuse.span(
    name=f"skill.{skill_id}",
    metadata={
        "skill_id": skill_id,
        "tier": skill_tier,
        "model_id": model_id,
        "cache_hit_l1": bool,
        "cache_hit_l2": bool,
        "cache_hit_l3": bool,
        "input_tokens": n,
        "output_tokens": n
    },
    start_time=request_start,
    end_time=response_complete,
    level="DEFAULT" if within_slo else "WARNING"
)

# Also emit a structured metrics event
metrics.histogram(
    "skill.latency.ttfb",
    value=ttfb_ms,
    tags={"skill_id": skill_id, "tier": tier, "model_id": model_id, "cache_hit_l2": str(cache_hit)}
)
```

### Percentile computation

Compute p50/p95/p99 over rolling 1-hour and 24-hour windows per `skill_id`. Use a histogram with power-of-two buckets for efficient percentile estimation.

## SLO alerting

| Alert | Condition | Severity |
|---|---|---|
| TTFB SLO breach (T-I) | p95_ttfb > 1.5s for 5 consecutive minutes | HIGH — wake on-call |
| TTFB SLO breach (T-W/T-D) | p95_ttfb > 3x target for 10 min | MEDIUM — notify eng channel |
| Error rate spike | Error rate > 1% over 5 min | HIGH |
| p99 outlier | p99_ttfb > 4x p50_ttfb | LOW — investigate cache or model issue |
| Total response time exceeded | p95_total > 2x target for 5 min | MEDIUM |

Alerts feed into the [[eng-fallback-model-cascade]] kill-switch: if a skill's p95 TTFB exceeds the T-W threshold and the primary model is at fault, automatically cascade to the secondary model.

## Common latency root causes

| Root cause | Symptom | Resolution |
|---|---|---|
| Cache miss at L2 (skills) | p95 TTFB spike after skill deployment | Warm the cache by sending a low-stakes prefill request after deployment |
| Large matter context (L3) | p95 TTFB proportional to matter age/size | Implement matter-context summarization; truncate least-relevant documents |
| Model overload / 529 | p99 spike; fallback_used rate rises | Cascade to secondary model; alert Anthropic |
| Long output generation | p95_total high despite low TTFB | Expected for T-D skills; verify streaming is enabled so user sees progress |
| Context assembly bottleneck | High latency on `context.assembly` span in Langfuse | Optimize KB retrieval; profile the assembly code |
| Cold start (serverless) | p99 outlier on first request after idle | Keep-alive ping or minimum instance count |

## SLO reporting

Produce a weekly SLO report:

```
SLO REPORT — [Period]

Skill                            | Tier | p50 TTFB | p95 TTFB | SLO Target | Status
─────────────────────────────────────────────────────────────────────────────────
efirm-conflict-check             | T-W  | 820ms    | 2.1s     | 3.0s       | ✓ OK
efirm-engagement-letter-draft    | T-D  | 1.4s     | 4.8s     | 5.0s       | ✓ OK
efirm-fee-quote-builder          | T-D  | 1.9s     | 6.2s     | 5.0s       | ✗ BREACH
router.*                         | T-I  | 210ms    | 480ms    | 1.5s       | ✓ OK

SLO breaches this period: 1 (efirm-fee-quote-builder)
Root cause: Large output + context explosion on complex matters
Remediation: Streaming enabled [date]; p95 expected to improve next period
```

## Related skills

- [[eng-langfuse-trace-inspector]]
- [[eng-fallback-model-cascade]]
- [[eng-cost-per-message-tracker]]
- [[eng-context-cache-key-design]]
