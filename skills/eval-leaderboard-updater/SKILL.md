---
name: eval-leaderboard-updater
description: Use when implementing or operating the component that records benchmark run scores to the internal quality leaderboard and weekly AI quality trend report. Maintains the historical score series, computes week-over-week deltas, and surfaces the trend data to the engineering and product teams.
license: MIT
metadata: " id: eval.leaderboard-updater category: eval jurisdictions: [__multi__] priority: P2 intent: [__eval__, leaderboard, quality-trend, reporting, ci] related: [eval-benchmark-runner, eval-regression-detector, eval-llm-as-judge-system-prompt, eval-rubric-legal-soundness] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'eval'.
Registered as a flat plugin skill.
-->


# Leaderboard Updater

## When to use this

The leaderboard updater runs automatically at the end of every [[eval-benchmark-runner]] run. It is also triggered manually when historical scores need to be backfilled or when the scoring methodology changes and requires recalibration.

## Inputs / signals

| Input | Source | Notes |
|---|---|---|
| `runId` | eval-benchmark-runner | UUID of the completed benchmark run |
| `runAt` | eval-benchmark-runner | ISO 8601 timestamp |
| `model` | eval-benchmark-runner | Model slug under test |
| `scores` | eval-benchmark-runner | Per-dataset and per-rubric scores |
| `aggregateScore` | eval-benchmark-runner | Weighted aggregate |
| `hallucinationRate` | eval-benchmark-runner | Fraction 0–1 |
| `latencyP95Ms` | eval-benchmark-runner | Infrastructure quality signal |
| `costPerMessageUsd` | eval-benchmark-runner | Economics signal |
| `regressionDetected` | eval-regression-detector | Boolean |

## Logic

### Step 1 — Persist to leaderboard table

```sql
INSERT INTO eval_leaderboard (
  run_id, run_at, model, aggregate_score, hallucination_rate,
  latency_p95_ms, cost_per_message_usd, regression_detected,
  dataset_scores, rubric_scores, created_at
) VALUES (...)
ON CONFLICT (run_id) DO NOTHING;
```

The `dataset_scores` and `rubric_scores` columns are JSONB, preserving the full per-dataset breakdown.

### Step 2 — Compute trend deltas

```sql
-- Get the previous run for the same model
SELECT aggregate_score AS prev_score, hallucination_rate AS prev_halluc
FROM eval_leaderboard
WHERE model = $1 AND run_id != $2
ORDER BY run_at DESC LIMIT 1;
```

Compute:
- `score_delta` = current aggregate - previous aggregate
- `hallucination_delta` = current hallucination_rate - previous hallucination_rate
- `trend` = `improving` | `stable` | `declining` (based on 3-run moving average)

### Step 3 — Update the weekly AI quality trend report

Aggregate all runs in the current week and update the `weekly_quality_summary` table:
```json
{
  "week": "2026-W20",
  "avg_aggregate_score": 4.2,
  "best_run_score": 4.4,
  "worst_run_score": 3.9,
  "hallucination_incidents": 0,
  "regressions_detected": 1,
  "regressions_resolved": 1
}
```

This data feeds the internal dashboard and the `report.weekly-AI-quality-trend` report.

### Step 4 — Emit leaderboard update notification

Post to Slack `#eng-quality` with a summary card:
```
Model quality run: claude-sonnet-4-5 @ 2026-05-14 12:00 UTC
Aggregate: 4.2 / 5.0 (+0.1 vs prev) ✓
Hallucinations: 0 ✓
Regression: None ✓
[View full report → Langfuse link]
```

If regression detected, post to both `#eng-quality` and `#eng-on-call`.

## Output

```json
{
  "leaderboardRowId": "uuid",
  "scoreDelta": 0.1,
  "trend": "improving",
  "weekSummaryUpdated": true,
  "slackNotified": true
}
```

## Leaderboard schema

```sql
CREATE TABLE eval_leaderboard (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  run_id UUID UNIQUE NOT NULL,
  run_at TIMESTAMPTZ NOT NULL,
  model TEXT NOT NULL,
  aggregate_score NUMERIC(3,2),
  hallucination_rate NUMERIC(5,4),
  latency_p95_ms INT,
  cost_per_message_usd NUMERIC(8,6),
  regression_detected BOOLEAN NOT NULL DEFAULT FALSE,
  dataset_scores JSONB,
  rubric_scores JSONB,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX ON eval_leaderboard (model, run_at DESC);
```

## Why this matters

A single aggregate score per run is not enough information to improve the product. The leaderboard preserves the full historical series so that:
- Engineers can see whether a prompt-engineering change improved one rubric while degrading another.
- Product can report "model quality improved 12% over the past quarter."
- Teams can detect and reverse regressions promptly rather than discovering them in user complaints.
- The trend (moving average) is more meaningful than any single run's absolute score.

## Caveats & currency

Recalibrate rubric weights in [[eval-benchmark-runner]] when the product's practice area mix changes significantly (e.g., if real-estate usage grows to 40% of queries, its dataset weight should increase). When rubric weights change, historical scores are not directly comparable — mark the change in the leaderboard `notes` column and restart the moving average.

## Related skills

- [[eval-benchmark-runner]] — the upstream process that calls this updater
- [[eval-regression-detector]] — provides the `regressionDetected` signal
- [[eval-llm-as-judge-system-prompt]] — the scoring engine whose output feeds into scores
- [[eval-rubric-legal-soundness]] — primary rubric whose trend is most closely tracked
