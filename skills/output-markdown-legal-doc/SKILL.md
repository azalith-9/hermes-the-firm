---
name: output-markdown-legal-doc
description: Use when the agent must format a legal document — contract, NDA, policy, opinion, or procedural submission — in clean Markdown that renders correctly and survives conversion to DOCX or PDF. Applies to all jurisdictions and document types. Triggers on any drafting request where the output is a standalone legal document rather than a conversational answer.
license: MIT
metadata: " id: output.markdown-legal-doc category: output intent: ['__format__', 'drafting', 'document', 'markdown', 'export'] related: - output-pdf-export-style - output-irac-structure - output-partner-memo-style - output-inline-citations-with-pinpoints priority: P0 source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'output'.
Registered as a flat plugin skill.
-->


# Markdown Format for Legal Documents

Legal documents must be formatted so they (a) read clearly on-screen, (b) convert faithfully to DOCX and PDF without re-formatting work, and (c) comply with the formal conventions of their jurisdiction and document type. This skill governs the Markdown conventions the agent uses for all legal document output.

## When to use this

Apply this skill whenever the output is a standalone legal document — contracts, NDAs, service agreements, constitutional documents, policies, compliance manuals, opinions, or formal submissions. Do not apply to conversational answers or research notes; those use lighter formatting.

## Document structure

### Top-level heading (H1) — one per document

`# NON-DISCLOSURE AGREEMENT`

The H1 is the document title. Use ALL CAPS for formal contracts (standard in MENA and common-law practice). Use title case for opinions and memos.

### Articles and sections (H2)

`## 1. Definitions`
`## 2. Confidentiality Obligations`
`## 3. Permitted Disclosures`

Number every article from 1. Use decimal numbering (1, 2, 3) for the article level.

### Sub-clauses (H3 or bold inline)

For sub-clauses that are full paragraphs, use H3:
`### 2.1 Scope of Confidential Information`

For short sub-clauses within a paragraph, use bold inline numbering:
`**2.1** For the purposes of this Agreement, "Confidential Information" means...`

Consistency is mandatory within a document — pick one style and stick to it throughout.

### Definitions

Two acceptable formats:

**Table format** (preferred for 5+ definitions):
| Term | Meaning |
|---|---|
| **Confidential Information** | Any information disclosed by the Disclosing Party... |
| **Permitted Purpose** | The evaluation of a potential transaction between the parties. |

**Bullet list** (acceptable for fewer definitions):
- **"Confidential Information"** means any information...
- **"Permitted Purpose"** means...

Alphabetize definitions. Bold the defined term. Use quotation marks around the term in both the definition block and first use in the operative clauses.

## Numbering conventions

**Decimal hierarchy** — use for most MENA and common-law commercial contracts:
```
1.      Article
1.1     Sub-clause
1.1.1   Sub-sub-clause
(a)     List item
(i)     Sub-list item
```

**Lettered paragraphs** — acceptable in short schedules and annexures:
```
(a) first item
(b) second item
```

**Civil-law influence** — Lebanon, France, Egypt: articles may be numbered with "Article" prefix and sub-clauses as (a), (b), (c). Match the convention of the governing law's standard form practice where possible.

## Cross-references

Always spell out cross-references in full:
> "…as set forth in **Section 4.2**…"
> "…subject to the limitations in **Article 7**…"

Do not use relative references ("the previous clause", "the section above") — these break when clauses are renumbered.

Use one consistent reference style throughout the document. Do not mix "Section", "Clause", "Article", and "Paragraph" unless they refer to genuinely different hierarchy levels.

## Standard clause order (commercial contract)

A standard MENA commercial contract typically follows this order:
1. Definitions and Interpretation
2. Scope of Agreement / Engagement
3. Obligations of [Party A]
4. Obligations of [Party B]
5. Payment / Fees (if applicable)
6. Intellectual Property
7. Confidentiality
8. Representations and Warranties
9. Indemnification / Liability
10. Term and Termination
11. Governing Law and Dispute Resolution
12. Miscellaneous (Force Majeure, Notices, Entire Agreement, Severability, Waiver, Assignment)
13. Signature Block
14. Schedules / Annexures

## Signature block

Place at the very end of the document body, before any schedules:

```
IN WITNESS WHEREOF, the parties have executed this Agreement as of the date first written above.

For and on behalf of [Party A]

Name:    ___________________________
Title:   ___________________________
Date:    ___________________________
Signature: _________________________

For and on behalf of [Party B]

Name:    ___________________________
Title:   ___________________________
Date:    ___________________________
Signature: _________________________
```

For UAE/KSA documents requiring notarization (Tawtheeq/Tawqi3i), add a Notarization block:
```
Notarized before:
Notary Public: ____________________
Date:          ____________________
Reference:     ____________________
```

## What to avoid

| Avoid | Because |
|---|---|
| Footnotes (`[^1]`) | Most DOCX converters strip or misplace them; use endnotes or parenthetical citations instead |
| Code blocks for legal text | Renders as monospace — use blockquotes (`>`) for quoted provisions |
| Emoji in body text | Unprofessional and strips on export |
| Tables wider than 5 columns | Break on narrow screens and PDF margins |
| HTML tags (`<br>`, `<div>`) | Survive in some but not all renderers |
| Hard line breaks mid-sentence | Create stray newlines in DOCX |
| `---` dividers mid-document | Render as horizontal rules which look odd in legal text |

## Schedules and annexures

Use a page-break comment before each schedule if the renderer supports it; otherwise use a triple blank line and a bold header:

`**SCHEDULE 1 — SERVICES**`

Number schedules from 1; use capital letters for Annexures (Annexure A, B). Cross-reference in the body: "as set out in **Schedule 1**".

## Language and bilingual documents

For Arabic/English bilingual contracts (common in UAE, KSA, Lebanon):
- Produce the English version first
- Note the governing language in the Governing Law clause
- If Arabic is governing, flag that the English is a courtesy translation only
- UAE: Arabic is mandatory for court proceedings (Federal Decree-Law on Judicial Procedures); an English-only contract is enforceable but the court will require a certified translation

## Export

See [[output-pdf-export-style]] for PDF generation conventions and [[output-irac-structure]] for embedding legal analysis within documents.

## Related skills

- [[output-pdf-export-style]]
- [[output-inline-citations-with-pinpoints]]
- [[output-irac-structure]]
- [[output-partner-memo-style]]
- [[output-source-attribution-block]]
