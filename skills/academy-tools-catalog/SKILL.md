---
name: academy-tools-catalog
description: Use when a user asks about the publicly accessible tools available through Louis — both the free public tools (NDA generator, contract summarizer, statute explainer, legal translator AR-EN) and the paid professional tools. Delivers a structured catalog with tool descriptions, access tier, supported jurisdictions, and use cases. Triggers on "what free tools do you have?", "can I try something without signing up?", or tool-discovery queries from visitors not yet committed to a subscription.
license: MIT
metadata: " id: academy.tools-catalog category: academy jurisdictions: [__multi__] priority: P3 intent: [__customer-facing__, tools-catalog, free-tools, discovery] related: [academy-legal-ai-skills-catalog, academy-ai-feature-explainer, academy-feature-explainer, academy-use-case-explainer] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'academy'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Tools Catalog — Free and Paid Louis Tools

## When to use this

Invoke when:
- A visitor or prospect asks "what can I try for free?"
- A user wants to know which tools are available without a subscription
- A marketing context needs a tool inventory (website, ads, social)
- A developer asks about publicly accessible API endpoints
- An enterprise prospect asks for a feature comparison between free and paid tiers

## Tool tier structure

| Tier | Access | Audience |
|---|---|---|
| **Free public tools** | No sign-up required (or basic registration) | Any visitor, prospects, journalists, citizens |
| **Free registered** | Email registration required | Law students, startup program members, occasional users |
| **Professional (paid)** | Subscription | Lawyers, paralegals, in-house teams, law firms |
| **Enterprise** | Contract | Law firms, legal departments, institutions |

---

## Free Public Tools

These tools require no subscription. They demonstrate Louis's core capability and serve as acquisition channels.

### NDA Generator
**What it does:** Generates a simple non-disclosure agreement from a few inputs (parties, scope, term, jurisdiction).
**Jurisdictions:** UAE, Lebanon, KSA, Egypt, DIFC (selectable)
**Language:** English, Arabic (selectable)
**Use case:** Startup founder needs a quick NDA before a meeting; no lawyer available.
**Limitation:** Simple unilateral or mutual NDAs only. Complex or multi-party NDAs require the professional tier.

### Contract Summarizer
**What it does:** Takes an uploaded contract (PDF or Word) and produces a plain-language summary of the key terms: parties, obligations, payment terms, governing law, dispute resolution, termination rights.
**Document limit:** Up to 10 pages on the free tier.
**Language:** Accepts AR/EN/FR contracts; outputs in English by default, Arabic on request.
**Use case:** A manager receives a vendor contract and wants to understand it before sending to legal.

### Statute Explainer
**What it does:** Takes a statutory provision or regulation (by reference or by paste) and explains it in plain language, with practical implications.
**Jurisdictions:** UAE Federal, DIFC, Lebanese, KSA, Egyptian, French (selectable)
**Language:** Output in English or Arabic
**Use case:** An in-house team member encounters a new regulation and wants to understand what it means before escalating to counsel.
**Limitation:** Does not provide legal advice on how the statute applies to a specific situation; explains the text only.

### Legal Translator (Arabic ↔ English)
**What it does:** Translates legal documents between Arabic and English, with legal-terminology awareness (not generic machine translation).
**Supported document types:** Contracts, court orders, regulatory correspondence, corporate documents
**Character limit:** 5,000 characters on the free public tier
**Use case:** A Lebanese company receives a contract from a UAE counterparty in Arabic and needs the English version for internal review.

### Know Your Rights — Quick Reference
**What it does:** Provides a plain-language summary of rights in a specific legal situation for a specific jurisdiction (employment rights, consumer rights, tenant rights, etc.).
**Jurisdictions:** UAE, Lebanon, KSA, Egypt (primary); expanding
**Language:** Arabic and English
**Use case:** An employee in Dubai wants to know their rights regarding end-of-service gratuity.
**Important disclaimer:** This is general legal information, not legal advice. Always consult a qualified lawyer for specific situations.

---

## Free Registered Tools (requires email sign-up)

### Full Contract Summarizer (up to 50 pages)
Extended version of the free contract summarizer with larger document capacity.

### Justinian Study Tools
Free access to Justinian's case brief generator and basic quiz function for verified law students. See [[academy-students-program]].

### Clause Library Browsing (read-only)
Browse and read clauses in the library without the ability to insert or export. Useful for legal research and comparison.

---

## Professional (Paid) Tools — Key Additions

All free tools at full capacity, plus:

### Risk Scanner
Multi-pass contract review with severity scoring and clause-level recommendations. Produces structured risk table output. Full jurisdiction coverage. See [[academy-feature-explainer]] for detail.

### Drafting Board
AI-assisted document drafting from templates. Full clause library integration. Internal consistency checking. Version tracking.

### Document Workspace
Collaborative document lifecycle management. Multi-user review, commenting, redline, and sign-off workflow.

### Full Clause Library (with variants and export)
All clause variants with position-aware filtering, drafting notes, risk flags, and export to Word.

### Skill Router (full 982-skill access)
Direct access to the full specialist skill library for complex legal tasks across all practice areas and jurisdictions.

### Casesim Tools
Litigation simulation tools (judge bench, opposing counsel, client Q&A, settlement EV calculator). See [[academy-litigation-game-coach]].

### Research and Intel Tools
Jurisdiction-specific legal research templates, regulatory monitoring, and comparative analysis.

---

## Developer / API Access

Developers building on top of Louis can access:
- Public tool endpoints (NDA generator, translator, summarizer) via REST API
- Full skill router API (professional/enterprise tier)
- Webhook support for document workflow events

API documentation available at [Louis developer portal].

---

## Related skills

- [[academy-legal-ai-skills-catalog]]
- [[academy-ai-feature-explainer]]
- [[academy-feature-explainer]]
- [[academy-use-case-explainer]]
