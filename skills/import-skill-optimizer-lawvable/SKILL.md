---
name: import-skill-optimizer-lawvable
description: Use when migrating a Lawvable skill-optimizer tool into the mini-hermes-the-firm format. The adapter maps Lawvable's skill-improvement pipeline — prompt quality scoring, output consistency testing, jurisdiction coverage gaps, and iterative refinement recommendations — into the standard skill model. Triggers when importing any Lawvable-native skill quality assurance or optimisation workflow.
license: MIT
metadata: " id: import.skill-optimizer-lawvable category: import jurisdictions: [__multi__] priority: P3 intent: [__import__, skill-optimizer, lawvable, migration, quality-assurance, prompt-engineering] related: [import-skill-creator-anthropic, import-skill-creator-openai, import-tabular-review-lawvable, import-outlook-emails-lawvable] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'import'.
Registered as a flat plugin skill.
-->


# Import: Skill Optimizer (Lawvable)

## What it does

This import adapter migrates a **Lawvable skill-optimizer tool** into the `mini-hermes-the-firm` standard format. Lawvable is a legal AI platform; its skill optimizer is a quality-assurance layer that evaluates existing skills against defined quality criteria and suggests improvements.

In the `mini-hermes-the-firm` context, the skill optimizer serves as a continuous-improvement tool for the skill library: it identifies skills that are too thin, too generic, or missing jurisdictional coverage, and outputs a prioritised improvement plan.

## Import config

| Field | Source mapping | Default if absent |
|---|---|---|
| `optimization_mode` | Legacy `mode` | `full` (coverage + quality + consistency) |
| `quality_dimensions` | Legacy `dimensions` array | 5-dimension model (see below) |
| `jurisdiction_gap_check` | Legacy `check_jurisdictions` boolean | `true` |
| `output_consistency_check` | Legacy `check_output` boolean | `true` |
| `min_body_lines` | Legacy `min_lines` | `120` |
| `max_body_lines` | Legacy `max_lines` | `320` |
| `scoring_method` | Legacy `scoring` | `rubric` (per-dimension score) |
| `output_format` | Legacy `format` | `optimization_report` |

## Dry-run preview

```
IMPORT PREVIEW — skill-optimizer-lawvable
Source shape          : Lawvable skill optimizer config
Mode                  : full (coverage + quality + consistency)
Quality dimensions    : 5 (depth, accuracy, jurisdiction, structure, routing)
Jurisdiction gap check: enabled
Output consistency    : enabled
Body line target      : 120–320 lines
Scoring               : rubric (per-dimension)
Output                : optimization_report
```

## Quality dimensions model (post-import)

### Dimension 1 — Depth
- Is the skill substantively deeper than a generic description?
- Does every section add information a practitioner would act on?
- Score: 1 (stub) → 5 (expert-grade)

### Dimension 2 — Legal accuracy
- Are all statute references verifiable?
- Are jurisdiction attributions correct (common law vs civil law)?
- Score: 1 (unverified/hallucinated) → 5 (fully verified)

### Dimension 3 — Jurisdictional coverage
- Does the skill cover the primary relevant jurisdictions?
- Is there a MENA-aware section where relevant?
- Are common-law vs civil-law differences addressed?
- Score: 1 (single jurisdiction only) → 5 (comprehensive multi-jurisdictional)

### Dimension 4 — Structure
- Does the skill follow the correct category template?
- Are headings consistent with the enrichment guide?
- Is the YAML frontmatter valid and complete?
- Score: 1 (unstructured) → 5 (perfect template adherence)

### Dimension 5 — Routing quality
- Does the description answer "when should the agent reach for this skill?"
- Are intent keywords specific enough to route correctly?
- Is there sufficient discrimination from related skills?
- Score: 1 (too generic to route) → 5 (precisely routable)

## Optimization report output

```
SKILL OPTIMIZATION REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Skill          : [skill name]
Category       : [category]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DIMENSION SCORES
Depth          : [1–5] — [brief finding]
Accuracy       : [1–5] — [brief finding]
Jurisdiction   : [1–5] — [brief finding]
Structure      : [1–5] — [brief finding]
Routing        : [1–5] — [brief finding]
Overall        : [mean score / 5]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
IMPROVEMENT RECOMMENDATIONS (priority order)
1. [specific action] — [expected score impact]
2. ...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRIORITY FOR ENRICHMENT: HIGH / MEDIUM / LOW
```

## Prioritisation logic

Skills are flagged for enrichment priority as follows:

| Condition | Priority |
|---|---|
| Overall score < 2.0 | HIGH — enrich immediately |
| Missing MENA jurisdictional notes for legal skill | HIGH |
| Body < 80 lines | HIGH |
| Jurisdiction score < 2 AND skill is P0/P1 | HIGH |
| Overall score 2.0–3.0 | MEDIUM |
| Body 80–120 lines | MEDIUM |
| Overall score > 3.0 | LOW |

## Failure modes

| Error | Likely cause | Resolution |
|---|---|---|
| `scoring_dimensions_empty` | Legacy had no quality dimensions | Apply default 5-dimension model |
| `min_lines_not_set` | No body-length threshold in source | Apply 120/320 targets |
| `jurisdiction_check_disabled` | Legacy skipped jurisdiction gap analysis | Enable; critical for MENA deployments |
| `output_format_unstructured` | Legacy produced narrative recommendations | Wrap in optimization_report schema |

## Related skills

- [[import-skill-creator-anthropic]]
- [[import-skill-creator-openai]]
- [[import-tabular-review-lawvable]]
- [[import-outlook-emails-lawvable]]
- [[import-legal-risk-assessment-anthropic]]
