---
name: eng-langfuse-trace-inspector
description: Use when investigating the behavior of a legal AI skill by inspecting its LLM traces in Langfuse — understanding which prompts were sent, what the model returned, how long each span took, what scores were assigned, and how to diagnose regressions or quality issues. Engineering and QA skill for legal AI observability and debugging.
license: MIT
metadata: " id: eng.langfuse-trace-inspector category: eng jurisdictions: [__multi__] priority: P2 intent: [langfuse, tracing, observability, debugging, quality, spans] related: - eng-langfuse-eval-runner - eng-audit-log-schema - eng-latency-slo-by-skill - eng-cost-per-message-tracker source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'eng'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Langfuse Trace Inspector

## What it does

Langfuse is an open-source LLM observability platform. Every LLM request in the legal AI product emits a trace to Langfuse, capturing the full prompt, the model's response, token counts, latency, scores, and metadata. The trace inspector is the procedure and tooling for using Langfuse traces to:

- Debug why a skill produced an unexpected or incorrect output.
- Understand the prompt that was sent to the model (including assembled system prompt, skill content, and matter context).
- Measure skill-level latency and identify bottlenecks.
- Review human or automated quality scores against individual traces.
- Correlate traces with audit log events for compliance investigations.

## Trace structure

In the legal AI product, each request produces a Langfuse trace with this span hierarchy:

```
Trace: [request_id]
  ├── span: router.skill-selection
  │     input: user_message, session_context
  │     output: selected_skill_id, confidence
  │     latency: Xms
  │
  ├── span: context.assembly
  │     input: skill_id, matter_id, user_id
  │     output: assembled_prompt_token_count
  │     metadata: cache_hit_l1, cache_hit_l2, cache_hit_l3
  │     latency: Xms
  │
  ├── generation: llm.invoke
  │     model: claude-sonnet-4-6
  │     input: full prompt (system + skill + matter + user)
  │     output: model response
  │     usage: {input_tokens, output_tokens, cached_tokens}
  │     latency: {ttfb, total}
  │     cost: {usd}
  │
  ├── span: output.formatter
  │     input: raw model response
  │     output: formatted response for UI
  │     latency: Xms
  │
  └── scores: [quality_score, accuracy_score, user_feedback]
```

## Key metadata to emit per trace

At the trace level, always include:

```python
langfuse.trace(
    name=f"skill.{skill_id}",
    user_id=user_id,
    session_id=session_id,
    metadata={
        "org_id": org_id,
        "matter_id": matter_id,
        "skill_id": skill_id,
        "skill_version": skill_version,
        "model_id": model_id,
        "cache_hit_l1": bool,
        "cache_hit_l2": bool,
        "cache_hit_l3": bool,
        "fallback_used": bool,
        "fallback_reason": str | None
    },
    tags=[skill_id, org_id, matter_type, "production"]
)
```

Tags enable filtering in the Langfuse UI without querying metadata.

## Inspection workflow

### Step 1: Locate the trace

Filter by one or more of:
- `session_id` (from user complaint or incident report)
- `user_id` (user-specific investigation)
- `org_id` + date range (org-level quality review)
- `skill_id` + score < threshold (quality regression hunt)
- `tag: production` + `model_id` + date (model behavior after upgrade)

### Step 2: Inspect the generation span

The generation span reveals exactly what was sent to the model and what the model returned. Key things to check:

- **System prompt**: was the correct system prompt version loaded?
- **Skill content**: is the correct skill version present in the context?
- **Matter context**: was the matter-specific context correctly assembled?
- **User message**: was the user input correctly parsed and forwarded?
- **Model output**: does the raw output match the formatted output? Any post-processing issues?

In a legal product, the full prompt can be large (100K+ tokens with matter context). Use Langfuse's diff view to compare prompt versions across two traces to identify what changed between a good and bad output.

### Step 3: Review scores

Four types of scores may be attached to a trace:

| Score type | Source | Range |
|---|---|---|
| `quality` | Judge model (automated eval) | 0–1 |
| `accuracy` | Legal accuracy check (automated or human) | 0–1 |
| `user_feedback` | Thumbs up/down from the UI | -1, 0, 1 |
| `latency_slo` | Pass/fail against SLO | 0, 1 |

Cross-reference: low quality + low accuracy score on the same trace = likely content issue. Low quality + high accuracy + negative user_feedback = likely formatting or communication issue.

### Step 4: Identify the root cause

Common root causes in legal AI products:

| Symptom | Likely cause | Investigation |
|---|---|---|
| Wrong conflict check result | Incorrect matter context; stale KB data | Check `matter_id` in trace; verify matter context assembly |
| Engagement letter with wrong jurisdiction | Wrong template loaded | Check skill content in generation span; verify template selection logic |
| Slow response on a specific skill | Context too large; cache miss | Check `context.assembly` latency; `cache_hit_l3` flag |
| Hallucinated statute number | Model inference error; no relevant KB doc retrieved | Check retrieval results in context; add a KB document covering that statute |
| Fallback model used unexpectedly | Primary model overloaded | Check `fallback_used` flag; correlate with provider status page |

## Sampling and retention

Tracing every production request at full detail is expensive. Use a sampling strategy:

| Traffic segment | Sampling rate | Full prompt stored? |
|---|---|---|
| P0 skills (conflict, engagement) | 100% | Yes |
| P1 skills | 20% | Yes |
| P2 skills | 5% | Metadata only |
| Failed requests | 100% | Yes |
| Low-score requests (score < 0.7) | 100% | Yes |

Langfuse traces containing full prompts include user-inputted content (potentially privileged). Apply the same data-retention and access-control policies as the audit log: org-scoped, role-restricted, minimum 1 year for P0 traces.

## Privacy and privilege considerations

Langfuse traces contain:
- User messages (which may include client-identifying details)
- Matter context (potentially privileged)
- Model responses (potentially privileged attorney work product)

Configure Langfuse in your own infrastructure (self-hosted) for any firm that requires data residency or has restrictions on third-party data processors. Do not use the Langfuse cloud service for a firm with strict data governance requirements without a signed DPA and data residency confirmation.

## Related skills

- [[eng-langfuse-eval-runner]]
- [[eng-audit-log-schema]]
- [[eng-latency-slo-by-skill]]
- [[eng-cost-per-message-tracker]]
