---
name: report-jurisdiction-coverage-matrix
description: "Use when the product or content team needs a structured view of how thoroughly the AI assistant covers each combination of practice area and jurisdiction — including depth of knowledge, recency of last update, and quality-evaluation scores. This internal report drives the content roadmap: which jurisdiction-practice-area cells to prioritize next. Trigger on the monthly content-planning cycle or when a new jurisdiction or practice area is under consideration."
license: MIT
metadata: " id: report.jurisdiction-coverage-matrix category: report jurisdictions: [__multi__] priority: P3 intent: [__internal__, coverage, content-roadmap, jurisdiction-matrix, practice-area] related: [report-skill-adoption-by-tier, report-weekly-ai-quality-trend, report-hallucination-rate-tracker, ref-jurisdiction-index] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'report'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Jurisdiction Coverage Matrix — Report

Internal content-strategy report mapping the intersection of practice areas (rows) and jurisdictions (columns) to coverage depth, recency, and evaluated quality. The matrix is the canonical document driving what KB, skill, and eval work to prioritize next.

## Purpose

The matrix answers: **where are we deep, where are we thin, and where should we invest?**

Without this, content investment happens ad hoc. With it, the team can see at a glance that, say, "KSA employment law" is a P1 gap generating user drop-off, while "EU securities" can wait another quarter because no paying users are asking about it.

## Matrix structure

### Axes

**Rows** — Practice areas (standard list; add rows when a new area is formally scoped):
- Corporate / M&A
- Employment & Labor
- Data Privacy & Cybersecurity
- Banking & Finance
- Capital Markets / Securities
- Real Estate & Construction
- Intellectual Property
- Dispute Resolution / Litigation
- Trade, Customs & Sanctions
- Tax
- Regulatory & Licensing
- Family & Personal Status (Islamic-law relevant)
- Criminal / Compliance

**Columns** — Jurisdictions (current primary scope):
- LB (Lebanon)
- KSA (Saudi Arabia)
- UAE Onshore (Federal + Dubai/Abu Dhabi emirate-level)
- DIFC
- ADGM
- QFC (Qatar Financial Centre)
- EG (Egypt)
- FR (France)
- EU (pan-EU instruments)
- UK
- US (general / Delaware)
- OHADA (West Africa)
- GCC (GCC-level instruments)

### Cell schema

Each cell captures four values:

| Field | Description | Values |
|-------|-------------|--------|
| `depth` | How thorough is the KB + skill coverage for this cell? | `deep` / `partial` / `thin` / `none` |
| `last_update` | When was the KB / skill for this cell last substantively updated? | ISO date string |
| `eval_score` | Average score on the benchmark eval suite for prompts targeting this cell (0–100). | Numeric |
| `priority` | Content roadmap priority for improving this cell. | `P0` / `P1` / `P2` / `P3` / `hold` |

### Depth definitions

| Level | Meaning |
|-------|---------|
| `deep` | Full KB article, verified against primary sources, passing eval score ≥ 80, updated within 6 months |
| `partial` | Some content exists; major gaps identified; eval score 50–79 or updated > 6 months ago |
| `thin` | Minimal content; the model may produce plausible but unverified output; eval score < 50 |
| `none` | No dedicated KB or skill; model relies entirely on training data; hallucination risk high |

## How to populate the matrix

### Data sources

1. **Skill inventory**: Count skills and KB articles per practice-area × jurisdiction combination.
2. **Eval scores**: Pull from the weekly eval suite — filter by jurisdiction + practice-area tag.
3. **Last-update dates**: From the skill version history / last commit date on KB files.
4. **User demand signals**: From analytics — query volume, drop-off rate, negative feedback — per cell.

### Update cadence
- Full matrix refresh: monthly (first Monday of each month)
- Spot updates: whenever a KB article is updated or a new skill ships for a specific cell
- Priority column: reviewed at quarterly content planning meeting

## Output format

### Summary heatmap (executive view)

A color-coded table:
- Dark green = `deep` + eval ≥ 80
- Light green = `partial` + improving
- Yellow = `thin` + P1 priority
- Red = `none` + known user demand
- Grey = `none` + no current demand

### Full matrix (working view)

Full spreadsheet with all four cell fields visible, sortable by `priority` and `eval_score`.

### Top gaps report (narrative)

Each month: the top 5 cells with the worst combination of user demand and coverage depth. For each cell:
- Current depth + eval score
- Estimated user queries/week hitting this gap
- Content investment required (small: 1-2 days; medium: 1-2 weeks; large: 1+ month)
- Proposed owner + target date

### Coverage progress (trend)

Track week-over-week:
- Number of cells at `deep` (target: grow)
- Number of cells at `none` with demand > threshold (target: shrink)
- Average eval score across all cells (target: ≥ 80)

## Prioritization rules

A cell is P0 if:
- User demand is high (top quartile by query volume) AND coverage is `thin` or `none`
- A regulatory change has made existing content stale in a jurisdiction that is a core product market

A cell is P1 if:
- User demand is medium AND coverage is `thin` or `none`
- Competitive analysis shows a competitor is deeper in a cell where we claim market leadership

A cell is P3 or `hold` if:
- No user demand in the past 90 days AND no planned market expansion to that jurisdiction

## Action items from the matrix

Every monthly refresh produces:
- A list of KB articles to write or update (assigned to content leads)
- A list of skills to update or create (assigned to skill owners)
- A list of eval prompts to add for newly populated cells
- A roadmap item if a new jurisdiction column should be added

## Related skills

- [[report-skill-adoption-by-tier]]
- [[report-weekly-ai-quality-trend]]
- [[report-hallucination-rate-tracker]]
- [[ref-jurisdiction-index]]
- [[report-competitor-output-comparison-weekly]]
