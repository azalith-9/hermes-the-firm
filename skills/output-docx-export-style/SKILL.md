---
name: output-docx-export-style
description: Use when generating or formatting output as a DOCX file for a legal document. Defines the heading hierarchy (Heading 1 through 3 plus Body Text variants), font and spacing standards (Times New Roman 12pt, 1.5 line spacing), numbering conventions, margin settings, signature block format, and schedule/annex structure — with rules for what to avoid (manual numbering, inconsistent fonts, hand-drawn signature lines).
license: MIT
metadata: " id: output.docx-export-style category: output priority: P1 intent: [docx, export, formatting, document-style, word-processing] related: [output-bilingual-formatting, output-client-letter-style, output-executive-summary-first] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'output'.
Namespaced as louis-<category>-<skill> on registration.
-->


# DOCX Export Style

## When to use this

Apply this style specification whenever generating output that will be exported as a Microsoft Word (.docx) file. This covers:
- Contract drafts and amendments
- Legal memos and opinions
- Client letters formatted for delivery
- Court submissions (where Word format is accepted)
- Term sheets and MOUs

For PDF-only output, these rules still apply — they govern the intermediate Word document before PDF conversion.

## Heading hierarchy

Use named Word styles (not manual bold/font-size formatting — manual formatting breaks on template changes and does not export cleanly):

| Style name | Used for | Example |
|------------|---------|---------|
| Heading 1 | Agreement or document title | NON-DISCLOSURE AGREEMENT |
| Heading 2 | Article (numbered) | ARTICLE 1. DEFINITIONS |
| Heading 3 | Sub-clause heading | 1.1 Confidential Information |
| Body Text | Main clause body | "Confidential Information means..." |
| Body Text Indented | Sub-clauses with one level of indent | "(a) all financial data..." |
| List Paragraph | Bullet or numbered lists within clauses | (i), (ii), (iii) lists |

All heading styles should be defined in the document's built-in style set. Do not override heading styles with manual formatting.

## Font and spacing

| Property | Value | Notes |
|----------|-------|-------|
| Body font | Times New Roman 12pt | Or equivalent serif (Garamond, Palatino) if firm style requires |
| Heading font | Same serif, bold | Heading 1 may be all-caps or small-caps per firm style |
| Line spacing | 1.5 for legal contracts; 1.0 with 6pt paragraph spacing for short memos | 1.5 is the standard for formal contracts |
| Paragraph spacing | 0pt before, 0pt after (for contracts) | Let line spacing create the visual separation |
| First-line indent | 0.5 inch (contracts) | Or paragraph block style with no indent + paragraph spacing |
| Justification | Fully justified for contracts; left-aligned for memos and letters | |

## Margins

| Context | Margins |
|---------|---------|
| US standard | 1 inch all sides |
| EU / MENA standard | 2.5 cm (approx. 1 inch) all sides |
| Filed documents (court) | Follow court's local rules — often larger left margin for binding |

## Page layout

- **Page numbers**: bottom center, starting from page 1 of the agreement body (not the cover page, if any).
- **Header**: agreement short title + version date (optional; depends on firm style). Example: `Non-Disclosure Agreement — Execution Version — May 2026`.
- **Footer**: confidentiality marking — `PRIVILEGED & CONFIDENTIAL` if the document contains legal advice; `CONFIDENTIAL` for commercial contracts between sophisticated parties.

## Numbering

Use **automatic Word numbering** — never manual numbering. Manual numbering (typing "1.", "2." by hand) breaks when clauses are added or removed during negotiation.

Numbering scheme for commercial contracts:
```
ARTICLE 1. DEFINITIONS
  1.1  [Clause body]
  1.2  [Clause body]
    (a)  [Sub-clause]
    (b)  [Sub-clause]
       (i)   [Sub-sub-clause]
       (ii)  [Sub-sub-clause]
```

Cross-references must be implemented using Word's cross-reference fields (Insert → Cross-reference → Heading/Numbered item) — not typed as literal text. Cross-reference fields update automatically when numbering changes.

## Signature block

Place the signature block at the end of the main agreement body, before any schedules:

```
IN WITNESS WHEREOF, the parties have executed this Agreement as of the date first written above.

For [PARTY A NAME]                    For [PARTY B NAME]
By: ___________________________       By: ___________________________
Name:                                 Name:
Title:                                Title:
Date:                                 Date:
```

Rules:
- Two-column layout using a table (no visible borders) — not using tab stops or manual spacing (which breaks on re-pagination).
- Use Word form fields or underline characters for signature lines — not hand-drawn lines.
- Include "By:" to clarify that the signature is that of an authorized representative, not the party entity itself.
- The date line should be left blank in the template for wet-ink or e-signature completion.
- For jurisdictions requiring witnesses (e.g., UAE real estate transactions, Lebanese notarized contracts): add witness blocks below the party signature blocks.

## Schedules and annexes

Each schedule starts on a new page. The cover of each schedule:

```
SCHEDULE [1 / A] — [SCHEDULE TITLE]

(referred to in the Agreement as "Schedule [1/A]")
```

Rules:
- Numbered continuously from the main agreement: Schedules 1, 2, 3 (or Annexes A, B, C — pick one convention and stick to it).
- Cross-references from the main agreement body to schedules use the exact schedule name/number.
- Schedules that are signed separately (e.g., a Statement of Work) need their own signature lines.
- Include the page number in the footer of each schedule page, continuing from the main agreement.

## What to avoid

| Mistake | Why it's a problem | Correct approach |
|---------|-------------------|-----------------|
| Manual numbering | Breaks when clauses are added/removed | Use Word's automatic numbering |
| Inconsistent fonts and sizes | Unprofessional; signals poor quality | Apply styles throughout; never manually override |
| Tab stops for alignment | Breaks on different screens or printers | Use tables (no visible borders) for alignment |
| Hand-drawn signature lines (underscore characters) | Breaks across pagination; hard to clean up | Use Word form fields or a consistent underline style |
| "Track Changes" in the final version | Exposes negotiation history to unauthorized readers | Always accept/reject all changes before sending an execution version |
| Watermarks in the final execution version | Confuses the status of the document | Watermarks are for drafts only; remove before execution |

## Bilingual DOCX

For bilingual Arabic-English documents, see [[output-bilingual-formatting]] for the two-column table layout that pairs with this style specification.

## Related skills

- [[output-bilingual-formatting]] — bilingual layout for Arabic-English DOCX exports
- [[output-client-letter-style]] — client letter formatting that pairs with DOCX export
- [[output-executive-summary-first]] — BLUF structure that may appear at the start of an exported memo
