---
name: eval-rubric-format-structure
description: Use when scoring AI legal output on formatting and structural quality — whether the output is organized appropriately for its type, uses correct heading hierarchy, presents tables and lists where they add value, and meets the formatting conventions expected in MENA legal practice. A 0–5 rubric focused on presentation quality independent of legal accuracy.
license: MIT
metadata: " id: eval.rubric.format-structure category: eval jurisdictions: [__multi__] priority: P2 intent: [__eval__, formatting, structure, rubric, presentation] related: [eval-rubric-completeness, eval-rubric-legal-soundness, eval-llm-as-judge-system-prompt, eval-benchmark-runner] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'eval'.
Registered as a flat plugin skill.
-->


# Eval Rubric — Format and Structure

## When to use this

Apply when the format and presentation of a legal AI output needs to be assessed independently of its legal accuracy. A well-structured contract draft makes review faster; a poorly structured one wastes a lawyer's time. Format quality is a secondary rubric — it rarely changes whether a deployment is blocked, but it tracks the product's output polish over time.

Run in the [[eval-llm-as-judge-system-prompt]] ensemble as an optional rubric (weight it lower than legal soundness and citation quality).

## Scoring (0–5)

| Score | Label | Criteria |
|---|---|---|
| **5** | Excellent | Output type perfectly matched to the request; correct heading hierarchy (numbered clauses for contracts, `##`/`###` for analysis); tables used where appropriate (comparison, calculations); lists used for enumerable items; no unnecessary boilerplate; RTL/LTR correct for language; professional legal register throughout |
| **4** | Good | Well-structured with minor issues (e.g., inconsistent heading numbering, a table that could be a list) |
| **3** | Acceptable | Reasonably structured but with clear formatting gaps (heading levels mixed up; a comparison given as prose instead of a table; a contract clause not numbered) |
| **2** | Poor | Significant structural problems (no headings at all in a 2,000-word draft; a calculation result buried in prose; comparison jumbled) |
| **1** | Very poor | Nearly unstructured; would require complete reformatting to be usable |
| **0** | Fail | Completely inappropriate format for the request type (e.g., a JSON object returned for a contract draft request) |

## Sub-criteria by output type

### Contract drafts

| Criteria | Expected |
|---|---|
| Heading structure | Numbered clauses (1., 2., 2.1, 2.2…) or named articles (Article 1 — Definitions) |
| Definitions section | Appears first (or second, after recitals); terms listed alphabetically or in order of first use |
| Signature block | Present at the end; parties, date, witness/notary block if required by jurisdiction |
| Page numbering reference | Footer formula ("Page X of Y") in the template instruction |
| Arabic contracts | Right-to-left; clause numbers on the right margin |

### Legal analysis / advisory responses

| Criteria | Expected |
|---|---|
| IRAC structure | Issue → Rule → Application → Conclusion clearly delineated |
| Summary box | For long analyses: a 3–5 bullet summary at the top |
| Jurisdiction flags | Each jurisdiction's analysis clearly labeled |
| Risk ratings | For review outputs: High/Medium/Low risk labels on identified issues |

### Comparison tables

For multi-jurisdiction or multi-option comparisons:
- A table beats prose every time. If the output has 3+ jurisdictions or options to compare, a markdown table is the expected format.
- Table columns: jurisdiction | rule | practical effect | risk flag
- Missing table in a comparison context = score ≤ 3.

### Calculation outputs

For EOSG/EOSA or tax calculations:
- Show the formula used, then the substituted values, then the result.
- Break multi-step calculations into numbered steps.
- State the legal authority for the formula.
- Calculations shown as prose without a structured formula are ≤ 2.

### Bilingual (AR/EN) outputs

- Side-by-side or alternating sections; never interleaved paragraph by paragraph.
- Each language version clearly labeled: "**Arabic Version / النسخة العربية**" and "**English Version**".
- Controlling language statement at the top (before both versions).
- Arabic text must be in a RTL paragraph block (not artificially left-aligned).

## What format structure does not measure

- Legal accuracy (see [[eval-rubric-legal-soundness]])
- Whether all required clauses are present (see [[eval-rubric-completeness]])
- Whether sources are accurate (see [[eval-rubric-citation-quality]])

Format structure only measures: is the output presented in a way that makes it easy to use, review, and understand?

## Common failure modes

| Failure | Typical score |
|---|---|
| 20-clause NDA with no heading structure | 1 |
| Comparison of 4 jurisdictions in prose paragraphs (no table) | 2 |
| EOSG calculation as a single number with no formula shown | 2 |
| Arabic text in a left-aligned block | 2 |
| Analysis with IRAC in the correct order but unlabeled | 3 |

## Related skills

- [[eval-rubric-completeness]] — structural completeness (required clauses); format is how they're presented
- [[eval-rubric-legal-soundness]] — legal accuracy of the content within the structure
- [[eval-llm-as-judge-system-prompt]] — applies this rubric in the automated scoring pipeline
- [[eval-benchmark-runner]] — orchestrates scoring across all output types
