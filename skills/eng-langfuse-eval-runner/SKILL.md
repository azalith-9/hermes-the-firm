---
name: eng-langfuse-eval-runner
description: Use when setting up or operating automated quality evaluation of legal AI skill outputs using Langfuse. Covers the evaluation dataset structure for legal domains, judge-model configuration, scoring rubrics specific to legal drafting and analysis, how to run batch evals across skill versions, and how to connect eval results to feature-flag promotion decisions. Engineering skill for legal AI quality assurance.
license: MIT
metadata: " id: eng.langfuse-eval-runner category: eng jurisdictions: [__multi__] priority: P2 intent: [eval, quality-assurance, langfuse, scoring, testing, LLM-evaluation] related: - eng-langfuse-trace-inspector - eng-feature-flag-rollout-skills - eng-latency-slo-by-skill - eng-cost-per-message-tracker source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'eng'.
Registered as a flat plugin skill.
-->


# Langfuse Eval Runner

## What it does

The eval runner executes systematic quality evaluations of skill outputs, using Langfuse as the orchestration layer. For each skill under test, it:

1. Takes a dataset of reference input/output pairs (golden set).
2. Runs the current skill version against the inputs.
3. Scores the outputs against the golden outputs using a judge model or custom rubric.
4. Writes scores back to Langfuse traces.
5. Computes aggregated pass rates and quality metrics.
6. Feeds results into the feature-flag promotion decision ([[eng-feature-flag-rollout-skills]]).

In a legal AI product, where the cost of a wrong output is potential malpractice exposure, systematic evaluation is non-optional for any skill that produces client-facing legal content.

## Evaluation dataset structure

A Langfuse dataset item for a legal skill:

```json
{
  "dataset_id": "efirm-conflict-check-eval-v1",
  "item_id": "ulid",
  "input": {
    "skill_id": "efirm-conflict-check",
    "context": {
      "new_client": "Al Baraka Holdings Ltd",
      "counterparties": ["Noor Capital SAOC", "Ali Hassan (individual)"],
      "matter_description": "Acquisition of minority stake in a KSA-incorporated company"
    },
    "user_message": "Run a conflict check for this new matter."
  },
  "expected_output": {
    "result": "CONCERN",
    "dimension_flagged": "former_client_check",
    "description": "Noor Capital SAOC was represented by the firm in matter 2023-UAE-0081 which may be substantially related"
  },
  "metadata": {
    "skill_version": "1.0",
    "practice_area": "corporate",
    "jurisdiction": "KSA",
    "difficulty": "medium",
    "created_by": "legal-qa-team",
    "reviewed_by": "partner-id"
  }
}
```

## Rubrics by skill category

### Conflict check rubrics

| Dimension | Scoring criterion | Weight |
|---|---|---|
| Correct result classification | CLEAN / CONCERN / CONFLICT matches expected | 40% |
| Correct dimension identification | Right conflict dimension flagged | 25% |
| No false negatives | Did not miss a flagged party | 25% |
| Description quality | Actionable, precise description | 10% |

### Drafting skill rubrics (engagement letter, NDA, fee quote)

| Dimension | Scoring criterion | Weight |
|---|---|---|
| Completeness | All required sections present | 25% |
| Accuracy | No fabricated statute numbers, incorrect jurisdiction references | 25% |
| Auto-population | All available fields correctly populated | 20% |
| Plain language | Jargon explained; sentence length within standard | 15% |
| Format compliance | Correct headings, numbering, version stamp | 15% |

### Advisory / analysis skill rubrics

| Dimension | Scoring criterion | Weight |
|---|---|---|
| Issue identification | Key legal issues identified | 30% |
| Legal accuracy | No invented legal rules; correct jurisdiction reference | 35% |
| Actionability | Concrete recommendations, not hedged generalities | 20% |
| Appropriate scope | Does not exceed what can be reliably stated | 15% |

## Judge model configuration

For automated scoring (as opposed to human review), the judge model evaluates each output:

```yaml
judge_config:
  model: claude-sonnet-4-6
  system_prompt: |
    You are a senior legal quality reviewer. Evaluate the AI output against the 
    reference output and the rubric. Score each dimension 0–1 (continuous). 
    Return JSON: {dimension: score, overall: float, pass: bool, notes: string}.
    
    Legal accuracy is paramount. A single fabricated statute number or incorrect 
    jurisdiction claim is an automatic fail regardless of other scores.
    
  pass_threshold: 0.75        # overall score ≥ 0.75 = pass
  legal_accuracy_hard_fail: true   # any legal_accuracy < 0.9 = fail regardless
```

The judge model should never be the same model as the model being evaluated — use a different model or a more capable model as judge.

## Running an eval

### Single skill, current version

```python
langfuse.run_eval(
    dataset_name="efirm-conflict-check-eval-v1",
    skill_id="efirm-conflict-check",
    skill_version="current",
    judge_config="legal-qa-rubric",
    run_name="conflict-check-v1-2025-05-14"
)
```

### A/B comparison (two skill versions)

```python
langfuse.run_eval(
    dataset_name="efirm-engagement-letter-eval-v2",
    experiments=[
        {"skill_version": "1.0", "name": "control"},
        {"skill_version": "1.1-test", "name": "treatment"}
    ],
    judge_config="drafting-rubric",
    significance_threshold=0.05
)
```

## Eval result schema (written back to Langfuse)

```json
{
  "run_id": "run_xxx",
  "skill_id": "efirm-conflict-check",
  "skill_version": "1.0",
  "dataset_id": "efirm-conflict-check-eval-v1",
  "n_items": 50,
  "pass_rate": 0.88,
  "avg_score": 0.83,
  "scores_by_dimension": {
    "result_classification": 0.92,
    "dimension_identification": 0.86,
    "no_false_negatives": 0.84,
    "description_quality": 0.79
  },
  "failures": [
    {"item_id": "xxx", "score": 0.61, "notes": "Missed corporate group adversity"}
  ],
  "promotion_recommendation": "PASS — meets 0.75 threshold",
  "run_timestamp": "ISO-8601"
}
```

## Promotion gate

Integrate with [[eng-feature-flag-rollout-skills]]:
- If `pass_rate ≥ 0.85` AND `avg_score ≥ 0.80`: auto-promote to next rollout stage.
- If `pass_rate < 0.75` OR any legal-accuracy hard fail: block promotion; alert product team.
- Between 0.75 and 0.85: manual review by legal QA partner before promotion.

## Golden set maintenance

- Golden sets must be reviewed and updated by a legal practitioner (not just engineering) at least every 6 months.
- When new legal developments occur (new legislation, regulatory guidance), update affected golden items.
- Target: minimum 30 items per skill for statistically meaningful results; 50–100 items for P0 skills.

## Related skills

- [[eng-langfuse-trace-inspector]]
- [[eng-feature-flag-rollout-skills]]
- [[eng-latency-slo-by-skill]]
- [[eng-cost-per-message-tracker]]
