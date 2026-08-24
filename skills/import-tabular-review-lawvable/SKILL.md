---
name: import-tabular-review-lawvable
description: Use when migrating a Lawvable tabular-review skill into the mini-hermes-the-firm format. The adapter maps Lawvable's structured table-based legal review output — clause-by-clause issue tables, risk-column scoring, and side-by-side comparison formats — into the standard skill model. Triggers on import of any Lawvable-native tabular review or comparative analysis workflow.
license: MIT
metadata: " id: import.tabular-review-lawvable category: import jurisdictions: [__multi__] priority: P3 intent: [__import__, tabular-review, lawvable, migration, contract-review, structured-output] related: [import-contract-review-anthropic, import-legal-risk-assessment-anthropic, import-nda-triage-anthropic, import-skill-optimizer-lawvable] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'import'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Import: Tabular Review (Lawvable)

## What it does

This import adapter migrates a **Lawvable tabular-review skill** into the `mini-hermes-the-firm` standard format. Lawvable's tabular-review output format is a structured table-based presentation of legal review findings: each clause or provision is a row, with columns for issue description, risk level, page/section reference, and recommended action. This format is highly popular with in-house legal teams and deal teams because it enables rapid prioritisation without reading a narrative memo.

The adapter maps this output format into the mini-hermes-the-firm skill model so that any the agent-powered legal review can produce Lawvable-compatible tabular output.

## Import config

| Field | Source mapping | Default if absent |
|---|---|---|
| `review_type` | Legacy `type` | `contract_review` |
| `table_columns` | Legacy `columns` array | Standard 6-column set (see below) |
| `risk_levels` | Legacy `risk_scale` | HIGH / MEDIUM / LOW / OK |
| `action_column` | Legacy `include_action` boolean | `true` |
| `section_reference` | Legacy `include_section` boolean | `true` |
| `summary_row` | Legacy `include_summary` boolean | `true` |
| `comparison_mode` | Legacy `compare` boolean | `false` (single-document default) |
| `output_format` | Legacy `format` | `markdown_table` |

## Dry-run preview

```
IMPORT PREVIEW — tabular-review-lawvable
Source shape    : Lawvable tabular review config
Review type     : contract_review
Columns         : 6 (section, clause summary, issue, risk, recommendation, action owner)
Risk levels     : HIGH / MEDIUM / LOW / OK
Action column   : enabled
Summary row     : enabled
Comparison mode : disabled (single document)
Output          : markdown_table
```

## Standard 6-column table format

```markdown
| Section | Clause Summary | Issue | Risk | Recommendation | Action Owner |
|---|---|---|---|---|---|
| Clause 1 | [brief summary] | [issue description] | HIGH | [specific fix] | Legal team |
| Clause 2 | [brief summary] | No issue | OK | — | — |
...
| **SUMMARY** | | [count] issues | [overall risk] | [top priority action] | |
```

### Column definitions

| Column | Content | Notes |
|---|---|---|
| **Section** | Clause number or section heading | Enables cross-reference to source document |
| **Clause Summary** | 1-sentence summary of what the clause says | Allows non-lawyers to follow without reading source |
| **Issue** | Description of the problem or risk | Specific, factual — not generic ("unfavourable") |
| **Risk** | HIGH / MEDIUM / LOW / OK | Based on severity × likelihood; OK = no issue |
| **Recommendation** | Specific remediation: suggested re-wording, deletion, or addition | Actionable — not "consider revising" |
| **Action Owner** | Who should action: Legal team / Client / Counterparty / Shared | Enables task assignment |

## Comparison mode (side-by-side)

When `comparison_mode: true`, the table adds two additional columns for comparing two versions of the same document (e.g. sent draft vs returned redline):

```markdown
| Section | Issue | Risk (v1) | Version 1 | Risk (v2) | Version 2 | Change Summary |
|---|---|---|---|---|---|---|
| Clause 3 | Liability cap | HIGH | $1M cap | MEDIUM | $5M cap | Cap increased — acceptable |
```

Use cases:
- Comparing own draft vs counterparty redline
- Comparing NDA received vs firm standard
- Comparing regulatory submission v1 vs regulator's marked-up return

## MENA output considerations

- **Arabic text in table cells**: ensure markdown table renderer supports Arabic RTL in cells; add a note if the document is Arabic-primary.
- **Bilingual clauses**: if a contract has Arabic and English columns, add a "Prevailing language" column.
- **Shariah compliance row**: for KSA/UAE financial contracts, add a dedicated "Shariah compliance" row in the table.
- **Government contracts**: UAE and KSA government contracts may have non-negotiable clauses; mark these as `OK (non-negotiable)` rather than `LOW` to avoid wasted review effort.

## Quality rules for tabular output

- Every HIGH-risk row must have a specific, concrete Recommendation — never "review and revise"
- Issue column must be factual and specific — never "this clause is unfavourable"
- No more than 20 rows without a section break; add headers for major contract parts (Preamble, Commercial Terms, Liability, Governing Law, etc.)
- Summary row must aggregate: total issues, distribution by risk level, top-3 priority actions

## Failure modes

| Error | Likely cause | Resolution |
|---|---|---|
| `generic_issues` | Legacy used "unfavourable" as issue description | Re-run with factual issue-description prompt |
| `no_action_owner` | Legacy omitted action column | Add default `Legal team` owner for all HIGH issues |
| `table_overflow` | >30 rows without structure | Add section headers; split into multiple tables by contract part |
| `comparison_columns_missing` | Comparison mode but only 6 columns | Add v1/v2 columns automatically when two documents provided |

## Related skills

- [[import-contract-review-anthropic]]
- [[import-legal-risk-assessment-anthropic]]
- [[import-nda-triage-anthropic]]
- [[import-skill-optimizer-lawvable]]
- [[review-contract-generic]]
