---
name: eval-regression-detector
description: Use when implementing or triggering the component that compares current benchmark run scores to the previous run and raises alerts when quality drops below threshold. Defines the regression rules, alert thresholds, escalation actions, and investigation flow for quality regressions in the legal AI system.
license: MIT
metadata: " id: eval.regression-detector category: eval priority: P0 intent: [__eval__, regression, quality-gate, alerting, ci] related: [eval-benchmark-runner, eval-llm-as-judge-system-prompt, eval-leaderboard-updater, eval-rubric-legal-soundness, eval-rubric-hallucination-detection] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'eval'.
Registered as a flat plugin skill.
-->


# Regression Detector

## When to use this

The regression detector is called automatically at the end of every [[eval-benchmark-runner]] run, after scores are computed and before [[eval-leaderboard-updater]] records them. It compares current scores to the previous run for the same model and raises alerts if quality has degraded.

It is also the system that **blocks automatic promotion** from staging to production if a blocking-rubric regression is detected.

## Inputs

| Input | Source |
|---|---|
| Current run scores (per-rubric, per-dataset) | eval-benchmark-runner |
| Previous run scores (same model) | eval-leaderboard table |
| `runId`, `model`, `runAt` | eval-benchmark-runner |
| Deployment pipeline hook | CI/CD system |

## Logic

### Regression thresholds

| Metric | Threshold | Severity |
|---|---|---|
| Any rubric score drops > 5% vs previous run | Alert | P1 — investigate before promoting |
| `legal_soundness` score drops > 3% | Alert + block deployment | P0 — hard block |
| `hallucination_rate` increases > 0.5 percentage points | Alert + block deployment | P0 — hard block |
| `citation_quality` score drops > 5% | Alert | P1 |
| `jurisdiction_awareness` score drops > 5% | Alert | P1 |
| Latency p95 increases > 20% vs previous run | Alert | P2 — ops issue |
| Cost-per-message increases > 15% | Alert | P2 — economics issue |

A **hard block** means the CI pipeline returns a non-zero exit code and the deployment is not promoted. It must be manually overridden by a senior engineer with a written justification.

### Regression computation

```typescript
function detectRegressions(current: RunScores, previous: RunScores): RegressionReport {
  const regressions: Regression[] = [];

  for (const rubric of RUBRICS) {
    const currentScore = current.rubrics[rubric];
    const prevScore = previous.rubrics[rubric];
    const delta = currentScore - prevScore;
    const pct = delta / prevScore;

    if (pct < -THRESHOLDS[rubric]) {
      regressions.push({
        rubric,
        currentScore,
        prevScore,
        delta,
        pctChange: pct,
        severity: SEVERITIES[rubric],
        blocking: BLOCKING_RUBRICS.includes(rubric),
      });
    }
  }

  return {
    hasRegressions: regressions.length > 0,
    blockDeployment: regressions.some(r => r.blocking),
    regressions,
  };
}
```

### Outputs

**On regression detected:**
1. **Slack alert** to `#eng-quality` with diff:
   ```
   ⚠️ Quality regression detected — claude-sonnet-4-5
   legal_soundness: 4.2 → 3.9 (-7.1%) [BLOCKING]
   citation_quality: 3.8 → 3.6 (-5.3%)
   Run: 2026-05-14 12:00 UTC
   [View details → Langfuse]
   ```
2. **Linear ticket** auto-created with:
   - Title: "Quality regression — {model} — {rubric} -{pct}%"
   - Description: regression context, top failing prompts, link to run report
   - Assignee: on-call engineer
   - Priority: P0 (for blocking) or P1 (for non-blocking)
3. **Block deployment** if `blockDeployment = true` — CI pipeline exits non-zero.

**On no regression:**
- Update leaderboard silently (no alert needed).
- Post a brief ✓ to `#eng-quality` only on the weekly summary, not every run.

## Investigation flow

When a regression is detected, follow this procedure before manual override:

1. **Identify which prompts regressed** — sort prompts by score delta; focus on the bottom 10%.
2. **Compare current vs previous responses** side-by-side — often a single prompt change reveals the root cause.
3. **Inspect skill routing** — did the router send certain prompts to a different skill? Check `skills_routed` in the run log.
4. **Check for model API changes** — did the underlying model version or API behavior change (e.g., new system-prompt behavior, token limits)?
5. **Check for config drift** — did a system prompt, context window size, or temperature change?
6. **Rollback if P0** — if legal_soundness or hallucination regressed and the cause is not identified within 2 hours, rollback the deployment.

## Observability

Connect to:
- **PostHog**: emit `eval_regression_detected` event with rubric and delta properties.
- **Langfuse**: link regression report to the run trace for full observability.

Both signals feed the weekly engineering review.

## Caveats & currency

- Some score variance between runs is expected (~1–2%) due to LLM judge non-determinism. Only flag regressions that exceed the threshold consistently across 2+ runs before treating them as genuine regressions.
- Recalibrate thresholds annually as the product matures. A threshold that was tight in early development may be too tight once the model quality plateaus at a high level.
- Track *trend* over absolute score — a model running at 4.2 for 3 months is more trustworthy than one that scored 4.5 once and is declining.

## Related skills

- [[eval-benchmark-runner]] — calls this detector after each run
- [[eval-llm-as-judge-system-prompt]] — produces the scores that are compared
- [[eval-leaderboard-updater]] — records results after this detector runs
- [[eval-rubric-legal-soundness]] — primary blocking rubric
- [[eval-rubric-hallucination-detection]] — secondary blocking rubric
