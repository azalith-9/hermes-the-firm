---
name: report-weekly-ai-quality-trend
description: Use when the product or engineering team needs a single aggregated weekly view of AI output quality across all tracked dimensions — eval suite scores, user NPS/satisfaction signals, hallucination rate, and bug rate — to spot regressions early, validate improvements, and maintain a historical quality record. This is an internal executive-level quality report. Trigger on the weekly quality-review schedule; escalate to an incident if any metric crosses a red threshold.
license: MIT
metadata: " id: report.weekly-AI-quality-trend category: report jurisdictions: [__multi__] priority: P3 intent: [__internal__, quality-trend, eval, nps, hallucination, weekly-report] related: [report-hallucination-rate-tracker, report-competitor-output-comparison-weekly, report-jurisdiction-coverage-matrix, eval-output-quality] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'report'.
Registered as a flat plugin skill.
-->


# Weekly AI Quality Trend — Report

Internal executive-level quality report aggregating all tracked quality signals for the AI assistant into a single weekly view. The report enables the leadership team to understand whether quality is improving, flat, or regressing — and to act before problems compound.

## Purpose

Quality in a legal AI product has multiple independent signals that can diverge:

- The eval suite can show improvement while user satisfaction drops (the eval is out-of-date with real usage).
- Hallucination rate can spike in a specific jurisdiction while overall eval scores look fine.
- User NPS can lag model regressions by 2–3 weeks because users adapt slowly.

This report forces all signals onto one page weekly, so no single signal goes unnoticed in isolation.

## Input signals

### 1. Eval suite score
**Definition**: Average score across the full benchmark eval suite (correct answers / total, or rubric-weighted score 0–100).

**Sources**: Automated eval run (ideally triggered on each deployment; at minimum weekly).

**Sub-dimensions to track**:
- By skill category (research / review / draft / kb)
- By jurisdiction (LB / KSA / UAE / DIFC / ADGM / EU / UK / US)
- By question type (statute lookup, case law, redline, compliance, licensing)

### 2. User satisfaction rate
**Definition**: Percentage of sessions with a positive feedback signal — thumbs up, 4–5 star rating, or absence of explicit negative feedback (where baseline negative rate is known).

**Sources**: In-product feedback widget; session ratings; conversation-level NPS probes (deployed to a random 10% of sessions).

**Segmentation**:
- By tier (Free / Plus / Pro / Enterprise)
- By skill category
- By jurisdiction

### 3. Hallucination rate
**Definition**: Rate of confirmed factual fabrications per 100 citation-risk assertions. Full methodology in [[report-hallucination-rate-tracker]].

### 4. Bug rate
**Definition**: Count of distinct bugs reported (internally or by users) per week, weighted by severity:
- P0 (data loss, wrong legal advice on high-stakes matter, product down): weight 10
- P1 (skill broken, major output degradation): weight 3
- P2 (minor formatting, UX): weight 1

Weighted bug rate = sum(weight × count) / total sessions × 1000.

## Output format

### Executive summary

```
Week: [ISO week + dates]
Model version: [current production model]
Skills updated this week: [N — list names if > 0]

Eval suite score:    [X/100]  [▲/▼/= vs last week] [▲/▼/= vs 4-wk avg]
User satisfaction:   [X%]     [▲/▼/= vs last week] [▲/▼/= vs 4-wk avg]
Hallucination rate:  [X%]     [▲/▼/= vs last week] [▲/▼/= vs 4-wk avg]
Weighted bug rate:   [X]      [▲/▼/= vs last week] [▲/▼/= vs 4-wk avg]

Overall quality: 🟢 STABLE / 🟡 WATCH / 🔴 DEGRADED
```

### Trend chart (4 weeks rolling)

A simple table showing each metric's weekly value for the past 4 weeks:

| Metric | W-4 | W-3 | W-2 | W-1 (current) | Trend |
|--------|-----|-----|-----|----------------|-------|
| Eval score | | | | | |
| User satisfaction | | | | | |
| Hallucination rate | | | | | |
| Weighted bug rate | | | | | |

### Drill-down by category

| Skill category | Eval score | Satisfaction | Hallucination rate | Notable change |
|----------------|------------|-------------|-------------------|----------------|
| research | | | | |
| review | | | | |
| draft | | | | |
| kb / ref | | | | |

### Drill-down by jurisdiction (top-6 by query volume)

| Jurisdiction | Eval score | Satisfaction | Hallucination rate | Notable change |
|---|---|---|---|---|
| UAE onshore | | | | |
| KSA | | | | |
| DIFC | | | | |
| LB | | | | |
| EU | | | | |
| UK | | | | |

### Notable incidents this week
Any P0 or P1 incidents: description, root cause (if known), status (open / resolved), and link to incident record.

### Actions taken
Changes deployed this week (model update, skill update, KB update, RAG index update) and their measured impact on the metrics above.

### Planned actions next week
Concrete items with owners and expected metric impact.

## Alert thresholds and escalation

| Metric | Yellow (watch) | Red (escalate — same day) |
|--------|----------------|--------------------------|
| Eval score | < 75 or > 5-pt drop week-on-week | < 65 or > 10-pt drop |
| User satisfaction | < 80% or > 5 pp drop | < 70% or > 10 pp drop |
| Hallucination rate | > 3% | > 7% |
| Weighted bug rate | > 20 | > 50 |

Red alert triggers a same-day incident call with product lead, engineering lead, and a legal domain expert.

## Cadence

- **Automated data collection**: continuous (daily cron)
- **Report assembled**: every Monday morning (automated draft + human review)
- **Published**: Monday by 12:00 (team timezone)
- **Archived**: in the quality-reports register with permanent record per week number

## Related skills

- [[report-hallucination-rate-tracker]]
- [[report-competitor-output-comparison-weekly]]
- [[report-jurisdiction-coverage-matrix]]
- [[report-skill-adoption-by-tier]]
- [[eval-output-quality]]
