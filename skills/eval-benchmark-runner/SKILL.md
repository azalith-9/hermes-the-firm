---
name: eval-benchmark-runner
description: Use when running the automated daily evaluation suite that measures the legal AI system's output quality across all benchmark datasets. Orchestrates the full eval pipeline — loading datasets, calling the production model, scoring with LLM-as-judge rubrics, detecting regressions, and publishing results to the leaderboard and observability dashboards.
license: MIT
metadata: " id: eval.benchmark-runner category: eval priority: P0 intent: [__eval__, benchmark, quality, regression, ci] related: [eval-llm-as-judge-system-prompt, eval-regression-detector, eval-leaderboard-updater, eval-dataset-nda-prompts-30, eval-dataset-employment-prompts-30, eval-dataset-adversarial-prompts, eval-dataset-multilingual-prompts] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'eval'.
Registered as a flat plugin skill.
-->


# Benchmark Runner

## When to use this

The benchmark runner is the automated quality gate for the legal AI system. It runs:
- **Daily at 12:00 UTC** — tracks quality trend over time.
- **On every staging deployment** — catches regressions before production.
- **On-demand via Slack `/eval-run`** — for ad-hoc quality checks after prompt-engineering changes.

Do not run it on production mid-traffic; use a staging endpoint or a dedicated eval tenant.

## Inputs

| Input | Required | Notes |
|---|---|---|
| `model` | Yes | Production model slug (e.g., `claude-sonnet-4-5`) or experimental |
| `datasets` | Yes | Array of dataset IDs to include; defaults to all |
| `judgeModels` | Yes | Array of judge model slugs for ensemble scoring |
| `costBudget` | Yes | Max USD to spend on this run; aborts if exceeded |
| `runId` | Auto | UUID generated per run |
| `baselineRunId` | Optional | Previous run to compare against for regression detection |

## Review methodology

### Step 1 — Load datasets

Load all configured `eval.dataset.*` files from `eval/datasets/*.jsonl`. Each JSONL file contains records with:
```json
{ "id": "nda-001", "prompt": "...", "category": "draft", "expected_signals": ["mutual", "confidential_info_defined", "governing_law"] }
```

Supported datasets: [[eval-dataset-nda-prompts-30]], [[eval-dataset-employment-prompts-30]], [[eval-dataset-real-estate-prompts-30]], [[eval-dataset-research-prompts-30]], [[eval-dataset-adversarial-prompts]], [[eval-dataset-multilingual-prompts]], [[eval-dataset-competitor-comparison-set]].

### Step 2 — Run prompts against production model

For each prompt:
1. Call the production `/chat` endpoint (not the LLM API directly — test the full stack).
2. Record: `response_text`, `latency_ms`, `tokens_input`, `tokens_output`, `skills_routed`.
3. Enforce a per-prompt timeout of 120 seconds; log any that exceed it.
4. Track cumulative cost; abort if `costBudget` is exceeded.

Run prompts concurrently (max 5 at a time) to keep wall-clock time under 30 minutes.

### Step 3 — Score each response

For each response, invoke the [[eval-llm-as-judge-system-prompt]] with the following rubrics active:
- [[eval-rubric-legal-soundness]] (weight: 0.35)
- [[eval-rubric-citation-quality]] (weight: 0.20)
- [[eval-rubric-jurisdiction-awareness]] (weight: 0.20)
- [[eval-rubric-completeness]] (weight: 0.15)
- [[eval-rubric-hallucination-detection]] (weight: 0.10 — binary, auto-fail)

Use an **ensemble of judges** (e.g., GPT-4o + the agent Sonnet from a different provider + Gemini Pro). Average their scores. Flag any prompt where judge disagreement > 1.5 points for manual review.

**Critical rule**: never use the same model family as both the system under test and the judge. If testing the agent Sonnet, judges must include at least one non-the agent model.

### Step 4 — Compute aggregate scores

Per dataset:
```
dataset_score = Σ(rubric_score × rubric_weight) / n_prompts
```

Global aggregate:
```
aggregate_score = Σ(dataset_score × dataset_weight) / n_datasets
```

Dataset weights (by business priority): adversarial=0.25, NDA=0.20, employment=0.20, multilingual=0.15, real-estate=0.10, research=0.10.

Also compute:
- `hallucination_rate` = count(hallucinated) / total_prompts
- `latency_p50`, `latency_p95`
- `cost_per_message` = total_cost / n_prompts

### Step 5 — Detect regressions

Call [[eval-regression-detector]] with current and previous run scores. Regression triggers:
- Any rubric score drops > 5% vs previous run.
- Hallucination rate increases > 0.5%.
- Latency p95 increases > 20%.
- Cost-per-message increases > 15%.

On regression: Slack alert to `#eng-quality`, auto-create Linear ticket, block deployment promotion if a P0 rubric regressed.

### Step 6 — Publish results

- Update [[eval-leaderboard-updater]] with scores.
- Write structured run report to Langfuse.
- Emit PostHog event `eval_run_completed` with aggregate score and regression flag.

## Output format

```json
{
  "runId": "uuid",
  "model": "claude-sonnet-4-5",
  "runAt": "2026-05-14T12:00:00Z",
  "datasets": {
    "nda-prompts-30": { "score": 4.1, "n": 30, "hallucinations": 0 },
    "adversarial-prompts": { "score": 4.7, "n": 30, "refusal_rate": 0.97 }
  },
  "aggregate_score": 4.2,
  "hallucination_rate": 0.003,
  "latency_p50_ms": 3200,
  "latency_p95_ms": 8100,
  "cost_per_message_usd": 0.0023,
  "regression": false,
  "top_failing_prompts": [
    { "id": "research-027", "score": 1.8, "issue": "fabricated statute number" }
  ]
}
```

## Limits & escalation

- If `hallucination_rate > 1%`, halt deployment automatically regardless of other scores.
- Recalibrate judge prompts against a human gold-standard label set **quarterly**.
- Track *trend* over absolute score — a 4.1 improving steadily from 3.5 is healthier than a 4.5 declining from 4.8.
- Do not over-optimize for benchmark scores — ensure at least 10% of prompts in each dataset are novel and not visible to the model team.

## Related skills

- [[eval-llm-as-judge-system-prompt]] — the system prompt driving rubric scoring
- [[eval-regression-detector]] — detects quality drops across runs
- [[eval-leaderboard-updater]] — records scores to the trend dashboard
- [[eval-dataset-nda-prompts-30]] — NDA benchmark dataset
- [[eval-dataset-adversarial-prompts]] — safety and robustness dataset
