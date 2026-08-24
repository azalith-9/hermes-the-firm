---
name: output-source-attribution-block
description: Use when the agent must append a formal sources section to a legal memo, research note, or advice letter. Ensures all legal propositions are traceable to verified primary and secondary authorities. Triggers on any formal legal output that contains citations, and at the end of IRAC analyses, partner memos, and multi-jurisdiction research tasks.
license: MIT
metadata: " id: output.source-attribution-block category: output intent: ['__format__', 'sources', 'citation', 'attribution', 'traceability'] related: - output-inline-citations-with-pinpoints - output-irac-structure - output-partner-memo-style - router-confidence-scorer priority: P1 source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'output'.
Registered as a flat plugin skill.
-->


# Source Attribution Block

A source attribution block is the end-of-document listing of every authority relied upon in a legal memorandum or research note. It does three things: it makes the analysis independently verifiable, it creates an audit trail for professional-responsibility purposes, and it lets the reader immediately see whether the analysis rests on primary law or inference.

## When to use this

Append a Sources block whenever:
- The output is a formal memo, advice note, or legal opinion
- The output contains statute, case, or regulatory citations
- The analysis draws on more than one source
- The output may be forwarded to a client, filed with a regulator, or relied on by a third party

Omit the Sources block for:
- Purely conversational answers with no cited authority
- Quick triage answers where the single source is already stated inline

## Standard pattern

Place the Sources block at the very end of the document, after the Recommendation section, separated by a horizontal rule:

```
---

## Sources

1. UAE Federal Decree-Law 33/2021 (Regulation of Labour Relations) — arts 10, 43, 51
2. Cabinet Decision 1/2022 (Implementing Regulations — Non-Compete)
3. Khoury v. Acme [2024] DIFC CFI 47 at [23]–[31] (non-compete proportionality)
4. SAMA AML Rules 2024 — section 4.2
5. Nayla Comair-Obeid, "Contracts in Arab Countries," Bruylant (2013), p. 214
6. [[kb-employment-law-uae]] — Louis Skills Library (internal reference)
```

## Source categories

Include sources in this order:

### 1. Primary sources — statutes and regulations

One line per instrument. Include:
- Full official name of the statute or regulation
- Jurisdiction
- Specific articles or sections relied on
- If a regulation implements a statute, list the statute first then the regulation

Examples:
- `UAE Federal Decree-Law 33/2021 on the Regulation of Labour Relations — art 10(1), 43`
- `Saudi Labor Law Royal Decree M/51 — arts 80, 83`
- `Lebanese Labor Code (Law of 23 September 1946, as amended) — art 50`
- `DIFC Contract Law (DIFC Law 6/2004) — art 86`
- `Egypt Civil Code (Law 131/1948) — art 147(2)`

### 2. Primary sources — cases

One line per case. Include:
- Full case name
- Citation with court and year
- Pin-cite to the specific paragraph or page
- Brief parenthetical explaining the proposition the case supports

Examples:
- `Khoury v. Acme [2024] DIFC CFI 47 at [23] (proportionality test for non-competes)`
- `Cavendish Square Holding BV v. Makdessi [2015] UKSC 67 at [32] (penalty clause doctrine)`
- `Cass. soc., 10 juill. 2002, n° 99-43.334 (non-compete consideration requirement)`

### 3. Regulatory instruments and official guidance

Circulars, decisions, guidance notes, and enforcement policies:
- `SAMA AML Rules 2024, section 4.2`
- `DFSA Rulebook — COB Module, Rule 7.2.1`
- `UAE Central Bank Circular 2/2023 on BNPL Licensing`

### 4. Secondary sources

Treatises, leading academic commentaries, and top-tier legal publications. Include author, title, publisher, year, and page/section:
- `Nayla Comair-Obeid, "Contracts in Arab Countries," Bruylant (2013), p. 214`
- `Practical Law, "Non-Compete Clauses in UAE Law" (Thomson Reuters 2024)`

Only include secondary sources from recognised authorities. AI-generated text is not a secondary source.

### 5. Internal references

Cross-references to the skills library or internal knowledge base:
- `[[kb-employment-law-uae]] — Louis Skills Library`
- `[Prior Advice Note, Matter Ref. HAQQ-2024-0023, 15 March 2024]`

Use the `[[wikilink]]` notation for internal skill cross-references so they are machine-navigable.

## Verification rules — critical

**Verify every citation before including it.** This means:
- The statute or article number must actually exist and say what you claim it says
- Case citations must be real cases, not hallucinations
- If you cannot verify: write `[citation needed — please verify before relying on this analysis]`
- Mark uncertain sources explicitly: `[unverified — source to be confirmed]`

**Reflective rule:** only include sources that were actually used in the analysis. Do not pad the sources section with related authorities that were not cited.

**No fabricated citations.** A fabricated statute article or invented case name, if discovered by opposing counsel or a regulator, creates professional-responsibility exposure and destroys the credibility of the analysis. See the cite-or-bust rule in [[router-confidence-scorer]].

## Sources vs footnotes

Two acceptable formats depending on the document:

**End-list (preferred for MENA practice):** all sources numbered at the end of the document, cited inline by number `(source 3)` or by parenthetical citation.

**Footnotes (common-law tradition, UK/DIFC):** each citation as a footnote at the bottom of the page. Harder to maintain in Markdown/DOCX; use if the audience expects footnotes.

See [[output-inline-citations-with-pinpoints]] for the inline citation format that pairs with this block.

## Related skills

- [[output-inline-citations-with-pinpoints]]
- [[output-irac-structure]]
- [[output-partner-memo-style]]
- [[router-confidence-scorer]]
