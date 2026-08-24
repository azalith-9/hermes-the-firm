---
name: academy-ai-feature-explainer
description: Use when a prospect or user asks "what can Louis do?" or "how is your AI different from generic AI tools?" Explains the core AI features of the Louis legal AI platform — skill router, clause library, citations engine, risk scanner, document workspace, drafting board, and legal flows — with MENA-first jurisdictional awareness and Arabic-native capability as key differentiators. Routes to this skill for product discovery, competitive positioning, and in-product onboarding moments.
license: MIT
metadata: " id: academy.ai-feature-explainer category: academy jurisdictions: [__multi__] priority: P3 intent: [__customer-facing__, product-discovery, onboarding, competitive-positioning] related: [academy-feature-explainer, academy-use-case-explainer, academy-legal-ai-skills-catalog, academy-clause-library-explainer, academy-legal-document-library-explainer] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'academy'.
Namespaced as louis-<category>-<skill> on registration.
-->


# AI Feature Explainer — What Louis Does and Why It Is Different

## When to use this

Invoke when a user or prospect asks any variant of:
- "What can Louis do?"
- "How is your AI different from ChatGPT / Harvey / Clio / generic AI?"
- "What features does HAQQ offer?"
- "Is this just a chatbot?"
- "Why would I use this instead of [competitor]?"

Also fires during in-product onboarding, on empty-state screens, and in sales-demo contexts where a concise, credible product story is needed quickly.

## Core differentiators — the short version

Louis is **not** a generic large-language model wrapper. Three facts set it apart:

1. **982-skill library with a transparent router.** Every user request is classified by a semantic router and dispatched to one or more specialist skills, each with its own instructions, jurisdiction table, output schema, and quality bar. Users and admins can inspect which skill ran and why.
2. **MENA-first jurisdictional awareness.** Substantive legal knowledge is organized by jurisdiction (Lebanon, UAE onshore, DIFC, ADGM, KSA, Egypt, QFC, OHADA, France, UK, EU) and surfaced automatically. The system does not give UAE answers to a Lebanese user by default.
3. **Arabic-native.** Drafting, review, and output in Arabic are first-class — not post-hoc translation. Bilingual clause comparisons (AR ↔ EN) are built in.

## Feature-by-feature breakdown

### Skill Router
The router reads each user message and selects the most relevant skill(s) from the 982-skill library. It outputs:
- The matched skill ID and confidence
- Required inputs it still needs
- A routing explanation (visible in developer/admin mode)

**Why it matters:** generic AI gives one response from one "mind." Louis gives a specialized response from a purpose-built legal reasoning module, with traceable logic.

### Clause Library
A curated repository of vetted contractual clauses, organized by:
- Jurisdiction (with civil-law vs. common-law variants)
- Language (Arabic, English, French)
- Drafting position (seller-favorable, buyer-favorable, neutral)
- Risk tier (standard, elevated, high-risk)

Each clause includes drafting notes, risk flags, and alternates. Side-by-side comparison across variants is built in.

### Citations Engine
Surfaces relevant statutory provisions, regulations, and (where available) case references keyed to the jurisdiction the user is working in. Citations are formatted for local convention (e.g., UAE Federal Law numbers, Lebanese Code of Obligations, DIFC contract law references). The engine does not fabricate citations — if it cannot verify a reference, it says so.

### Risk Scanner
Automated multi-pass review of uploaded contracts and documents:
- Flags missing standard clauses
- Highlights unfair, one-sided, or jurisdiction-inappropriate language
- Scores overall risk posture (Low / Medium / High / Critical)
- Distinguishes commercial risk from legal enforceability risk

Output is a structured table with clause location, severity, recommended action, and (where applicable) a suggested replacement clause from the Clause Library.

### Document Workspace
A collaborative environment for drafting, reviewing, and versioning legal documents:
- Full document lifecycle (draft → review → redline → sign-off)
- Comment threads with AI-suggested resolutions
- Version diff with change-tagging
- Export to Word / PDF with formatting preservation

### Drafting Board
AI-assisted drafting from templates:
- Starts from the Document Library (pre-built templates per jurisdiction + practice area)
- Fills variable fields intelligently from context
- Suggests clause alternatives when a placeholder is ambiguous
- Detects internal inconsistencies (e.g., defined term used but not defined)

### Legal Flows
Pre-built multi-step AI workflows for recurring legal tasks:
- **NDA Flow:** party identification → scope → term → governing law → output
- **Employment Contract Flow:** jurisdiction → role classification → mandatory provisions → optional clauses → output
- **Entity Formation Flow:** jurisdiction selector → structure → filing checklist → draft articles

Flows enforce jurisdictional mandatory requirements as gates (e.g., required Arabic version in UAE, notarization requirements in Lebanon).

## What Louis does not claim to do

- It does not provide legal advice; it provides legal tools for qualified professionals and informed users.
- It does not guarantee outcome predictions.
- It does not replace a lawyer — it amplifies one.

## Competitive framing

| Dimension | Generic AI (GPT/Gemini) | US Legal AI (Harvey) | Louis |
|---|---|---|---|
| Jurisdiction depth | Global generic | US-primary | MENA-primary, multi-jx |
| Arabic support | Translation-only | Minimal | Native |
| Skill transparency | Black box | Black box | Transparent router |
| Clause library | None | Limited | Vetted, position-aware |
| Risk scanner | Ad hoc | US-contract focused | Multi-jx, civil+common |

## Related skills

- [[academy-feature-explainer]]
- [[academy-use-case-explainer]]
- [[academy-legal-ai-skills-catalog]]
- [[academy-clause-library-explainer]]
- [[academy-legal-document-library-explainer]]
