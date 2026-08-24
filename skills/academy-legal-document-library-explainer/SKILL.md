---
name: academy-legal-document-library-explainer
description: Use when a user asks about the Louis Document Library — what pre-built document templates are available, how they are organized by jurisdiction and practice area, how to search and instantiate them, and how the Document Library differs from the Clause Library. Triggers on queries for "do you have a template for X?", "show me your NDA template for [jurisdiction]", or "what's the difference between your clause library and document library?".
license: MIT
metadata: " id: academy.legal-document-library-explainer category: academy jurisdictions: [__multi__] priority: P3 intent: [__customer-facing__, document-library, templates, drafting] related: [academy-clause-library-explainer, academy-ai-feature-explainer, academy-feature-explainer, academy-legal-ai-skills-catalog] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'academy'.
Registered as a flat plugin skill.
-->


# Legal Document Library Explainer

## When to use this

Invoke when:
- A user asks "do you have an NDA template for the UAE?"
- A user asks "what contract templates are available?"
- A user wants to start a new document and needs to select a starting point
- A user asks "what's the difference between the clause library and the document library?"
- A developer building an integration needs to understand the document template inventory

## What the Document Library is

The Louis Document Library is a collection of **full-form legal document templates**, organized by jurisdiction, practice area, and drafting position. Each template is:

- **Pre-structured**: the document comes with the correct sections, recitals, body clauses, signature blocks, and schedules for the specified jurisdiction and document type
- **Variable-ready**: placeholders are identified and typed (party name, date, governing law, payment term, etc.) so the Drafting Board can prompt for them intelligently
- **Jurisdiction-calibrated**: mandatory provisions for the relevant jurisdiction are pre-populated (e.g., UAE Labour Law mandatory clauses in employment contracts; Arabic-language execution requirements; DIFC-specific boilerplate for DIFC-governed documents)
- **Versioned**: each template carries a version number and a "last verified" date; the library indicates when jurisdiction law has changed and the template may need review
- **Searchable**: full-text and metadata search across the library

## How the Document Library differs from the Clause Library

This is the single most common confusion point.

| Document Library | Clause Library |
|---|---|
| Full document forms — ready to instantiate | Individual clauses — reusable building blocks |
| Used at the start of a draft | Used mid-draft, when you need a specific provision |
| One document = one template | One clause = one provision type, with variants |
| Jurisdiction + document type determines the template | Jurisdiction + position + risk tier determines the clause variant |
| E.g.: "UAE Fixed-Term Employment Contract" | E.g.: "Non-Compete — UAE — Employee-Favorable" |

Think of the Document Library as the scaffolding; the Clause Library supplies the specific bricks you swap in as you customize.

## Document library taxonomy

### By practice area and document type

**Corporate and Commercial**
- NDA / Confidentiality Agreement (unilateral, mutual, tri-party)
- Services Agreement (time-and-materials, fixed-fee, retainer)
- Agency Agreement
- Distribution Agreement
- Joint Venture Agreement
- Shareholders Agreement
- Share Purchase Agreement
- Memorandum of Understanding / Term Sheet

**Employment**
- Employment Contract (UAE — limited/unlimited term; KSA; Lebanon; Egypt)
- Offer Letter
- Non-Disclosure + Non-Compete (jurisdiction-specific)
- Secondment Agreement
- Contractor / Freelance Agreement

**Real Estate**
- Sale and Purchase Agreement (UAE off-plan; UAE secondary; Lebanon)
- Lease Agreement (commercial; residential; UAE with RERA terms)
- Pre-sale Agreement (Muqawala — Lebanon)

**Banking and Finance**
- Facility Letter (conventional and Islamic finance variants)
- Guarantee / Kafalah
- Security Agreement (pledge, mortgage, charge)

**Construction**
- Construction Contract (FIDIC Yellow Book; FIDIC Red Book adapted)
- Subcontract Agreement
- O&M Agreement

**Corporate Formation**
- Articles of Incorporation (UAE Mainland; DIFC; ADGM; KSA; Lebanon SAL)
- Corporate Resolutions
- Power of Attorney

### By jurisdiction

Each template record is tagged with its primary jurisdiction and lists compatible secondary jurisdictions. A "UAE onshore — Employment Contract" is distinct from a "DIFC — Employment Contract" — the mandatory provisions, governing law clause, and dispute resolution mechanism differ substantially.

## How to use the Document Library

**Step 1 — Search or browse.** Enter the document type you need, or browse by practice area → jurisdiction → document type.

**Step 2 — Select a template.** Review the template summary: what mandatory provisions it includes, what jurisdiction it targets, and what the variable fields are.

**Step 3 — Instantiate in the Drafting Board.** The Drafting Board opens the template, prompts for variable fields, and begins intelligent clause suggestion. If a placeholder is ambiguous, it asks for clarification.

**Step 4 — Customize.** Swap in clauses from the Clause Library, add schedules, and redline. The Drafting Board tracks changes and checks internal consistency.

**Step 5 — Export.** Download as Word (.docx) or PDF, with or without formatting markers.

## Jurisdictional notes for document templates

### UAE mandatory requirements
- Employment contracts must be in Arabic (official version) with English permitted as a parallel text
- Certain document types (real estate SPA for off-plan property) must be registered with RERA / DLD
- Power of attorney: notarization required for registration with UAE authorities; some require Ministry of Foreign Affairs authentication

### Lebanon mandatory requirements
- Real estate transactions must be registered with the Land Registry (Cadastre)
- Commercial contracts often require notarization (Tawqi3i) for enforceability against third parties
- Employment contracts must comply with the Lebanese Labour Code; certain provisions (annual leave, end-of-service indemnity) are mandatory and cannot be contracted out

### DIFC / ADGM
- Documents governed by DIFC law can be in English only
- DIFC Courts-friendly dispute resolution clauses are pre-populated in DIFC-jurisdictions templates
- No notarization requirement for commercial contracts within DIFC/ADGM

### KSA
- Arabic is the official language; English is permitted for commercial contracts but courts apply the Arabic text in case of conflict
- Saudi-specific mandatory provisions in employment contracts (Saudi Labour Law) are pre-populated
- Certain agreements (real estate, certain regulated sectors) require notarization via the Ministry of Justice

## Common mistakes

- Using a template without checking its "last verified" date when there has been a recent law change
- Choosing a UAE-onshore template for a DIFC-incorporated entity — the templates are not interchangeable
- Failing to fill variable fields before sending a draft to a counterparty (Louis will warn about unfilled placeholders on export)

## Related skills

- [[academy-clause-library-explainer]]
- [[academy-ai-feature-explainer]]
- [[academy-feature-explainer]]
- [[academy-legal-ai-skills-catalog]]
