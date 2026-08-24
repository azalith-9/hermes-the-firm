---
name: academy-clause-library-explainer
description: Use when a user asks what the Clause Library contains, how to find a specific clause, how to compare clause variants across jurisdictions or negotiating positions, or how the clause library differs from the document template library. Covers vetted contractual clauses organized by jurisdiction, language (AR/EN/FR), position (seller/buyer/neutral), and risk tier, with side-by-side comparison and drafting notes. Triggers on queries for standard DIFC/ADGM/KSA/UAE/Lebanese clauses, Arabic-version clause requests, or "show me alternatives" moments.
license: MIT
metadata: " id: academy.clause-library-explainer category: academy jurisdictions: [__multi__] priority: P3 intent: [__customer-facing__, clause-library, drafting, jurisdiction-navigation] related: [academy-legal-document-library-explainer, academy-ai-feature-explainer, academy-feature-explainer, academy-use-case-explainer] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'academy'.
Registered as a flat plugin skill.
-->


# Clause Library Explainer

## When to use this

Invoke when:
- A user asks "show me the standard DIFC governing law clause"
- A user asks "I need an Arabic-version confidentiality clause"
- A user asks "what's the difference between a balanced and seller-favorable limitation of liability?"
- A user is mid-draft and requests alternatives to a clause they have already written
- A prospect asks "do you have clause templates for [jurisdiction]?"
- A user wants to compare how a specific clause type is structured in UAE vs Lebanon vs KSA

## What the Clause Library is

The Louis Clause Library is a curated collection of contractual clauses — not full contracts, but the reusable building blocks that appear across many contract types. Each entry in the library is:

- **Vetted** by jurisdiction-aware review (not AI-generated boilerplate presented as authoritative)
- **Position-aware**: clauses come in variants — seller-favorable, buyer-favorable, and neutral — so the lawyer can select the variant appropriate to their client's negotiating position
- **Multi-lingual**: Arabic, English, and (for applicable jurisdictions) French versions are maintained in parallel. The Arabic versions are drafting-quality, not translations
- **Annotated**: each clause carries drafting notes explaining why specific language was chosen, what risk it addresses, and what to watch for when the counterparty redlines it
- **Cross-referenced**: related clauses link to each other (e.g., a limitation-of-liability clause links to the indemnity clause and the insurance clause)

## How to find a clause

Three access modes:

1. **Natural-language search**: "I need a non-solicitation clause for a UAE employment contract" → the library returns matching clauses ranked by jurisdiction, position match, and recency.
2. **Browse by taxonomy**: Category → Jurisdiction → Position → Language → Risk tier.
3. **In-draft insertion**: while working in the Drafting Board, highlight a clause gap or placeholder and Louis suggests relevant library clauses inline.

## Clause anatomy — what each record contains

| Field | Content |
|---|---|
| Clause name | Standard naming (e.g., "Limitation of Liability — Mutual — UAE onshore") |
| Category | Contract type (NDA, employment, services, SPA, JV, etc.) |
| Jurisdiction | Primary + compatible jurisdictions |
| Language | AR / EN / FR, with bilingual side-by-side where available |
| Position | Seller-favorable / Buyer-favorable / Neutral |
| Risk tier | Standard / Elevated / High-risk |
| Text | The clause text itself |
| Drafting notes | Why this language; what to watch |
| Risk flags | What a court or regulator might challenge |
| Alternates | 1–3 alternate versions with notes on tradeoffs |
| Related clauses | Linked records |
| Last verified | Date of last jurisdiction-law check |

## Jurisdictional notes by clause type

### Governing law and dispute resolution clauses
Civil-law jurisdictions (Lebanon, UAE onshore, KSA, Egypt) do not give the same effect to party choice of foreign law as common-law courts do. DIFC and ADGM courts will generally give effect to the parties' choice. For UAE onshore contracts with mandatory Arabic execution, the Arabic text governs in case of inconsistency — the library flags this where relevant.

### Confidentiality and NDA clauses
KSA: trade secret protection exists under the Anti-Cyber Crime Law and general commercial law principles; a well-drafted NDA clause should reference the applicable regime. UAE: the UAE IP and Trade Secrets framework (Federal Decree-Law No. 36 of 2021 and its implementing regulations) is the primary reference. Lebanon: Code of Obligations and Contracts applies; confidentiality clauses are generally enforceable but remedies for breach may be harder to quantify.

### Limitation of liability clauses
UAE onshore: courts may not give full effect to exclusions of liability for gross negligence or intentional acts. DIFC and ADGM follow English common-law principles more closely (reasonableness test for exclusion clauses). KSA Sharia-influenced approach: courts may reduce damages on fairness grounds; overly punitive LD clauses are disfavored.

### Liquidated damages clauses
US-style "not a penalty" recitals are not necessary in MENA civil-law jurisdictions; courts have their own power to adjust damages that is not waivable by contract. The library flags clauses where US-style language would be surplus or potentially counterproductive.

## The difference between the Clause Library and the Document Library

| Clause Library | Document Library |
|---|---|
| Individual clauses — building blocks | Full document forms |
| Position-aware variants | Template forms (sometimes with position variants) |
| Used mid-draft or in search | Used at draft initiation |
| Reusable across contract types | Contract-type-specific |
| Annotated with risk notes | Annotated with filing / execution notes |

Think of the Clause Library as a well-organized components library; the Document Library is a set of ready-to-instantiate full forms.

## Common mistakes

- **Using an EN clause in an AR-governed contract without checking the Arabic version.** Louis flags this — always confirm the Arabic text aligns with intent.
- **Selecting a "neutral" clause when your client is the stronger party.** The clause library does not enforce this, but the drafting board will ask for confirmation.
- **Accepting the first search result without reading the drafting notes.** The notes often contain the most practically useful information.

## Related skills

- [[academy-legal-document-library-explainer]]
- [[academy-ai-feature-explainer]]
- [[academy-feature-explainer]]
- [[academy-use-case-explainer]]
