---
name: academy-feature-explainer
description: Use when given a specific Louis feature name and asked to produce a clear one-paragraph explanation plus a concrete use case and (optionally) a screenshot reference. This is a generic explainer generator — not a product overview — and fires when users or in-product help systems need on-demand feature documentation for a named capability. Distinct from the AI feature explainer (product overview) and the use-case explainer (user-goal-first).
license: MIT
metadata: " id: academy.feature-explainer category: academy jurisdictions: [__multi__] priority: P3 intent: [__customer-facing__, feature-docs, in-product-help, sales-deck] related: [academy-ai-feature-explainer, academy-use-case-explainer, academy-clause-library-explainer, academy-legal-document-library-explainer, academy-legal-ai-skills-catalog] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'academy'.
Registered as a flat plugin skill.
-->


# Feature Explainer — On-Demand Feature Documentation Generator

## When to use this

Invoke when:
- A user hovers over a feature name and asks "what is this?"
- An in-product help bubble needs to render a feature description dynamically
- A sales deck requires a 1-paragraph feature blurb for a specific capability
- A user asks "explain [feature name] to me"
- A public help center article needs a feature summary

**Key distinction:** this skill starts from a *feature name* (what the product does) and explains it. If a user starts from *what they want to accomplish*, use [[academy-use-case-explainer]] instead.

## Inputs

| Input | Required | Notes |
|---|---|---|
| Feature name | Yes | Exact or approximate — the skill should handle common aliases |
| Audience | Optional | Default: practitioner. Adjust for student / non-lawyer / executive |
| Length | Optional | Default: 1 paragraph + use case. Can expand to full section |
| Screenshot ID | Optional | If a UI screenshot reference is available, include it |

## Output format

A standard feature explainer has three parts:

1. **One-paragraph description** (50–80 words): what the feature is, what problem it solves, how it works at a high level. No jargon beyond what the user already knows.
2. **Use case** (1–3 sentences): a concrete scenario — "Suppose a lawyer at a UAE law firm receives a 60-page services agreement from a Saudi counterparty. The Risk Scanner reads the document in under 30 seconds, flags 7 clauses for review, and ranks them by severity so the lawyer starts with the highest-impact issues."
3. **Screenshot reference** (optional): reference the UI element or screen where the feature lives, using the canonical screenshot ID from the asset library.

## Feature inventory — key features and their one-paragraph stubs

### Skill Router
The Skill Router is the intelligence layer that reads every user request and dispatches it to the most relevant specialist skill in the 982-skill library. Rather than treating all questions the same, the router identifies the practice area, jurisdiction, and task type, then selects the right sub-model of reasoning. Users in developer mode can see which skill was selected and why.

*Use case:* A user types "draft me a non-compete for a UAE employee." The router identifies this as a drafting task, UAE jurisdiction, employment practice area, and routes to the employment contract drafting skill — which then applies UAE Labour Law and Ministry of Human Resources guidelines automatically.

### Risk Scanner
The Risk Scanner performs a multi-pass automated review of any uploaded contract or document. It flags missing standard clauses, one-sided or jurisdiction-inappropriate language, and internal inconsistencies. The output is a prioritized table — Critical / High / Medium / Low — with the clause location, the issue, and a suggested fix.

*Use case:* A procurement officer uploads a vendor services agreement before signature. The Risk Scanner flags a missing liability cap, a payment term longer than 120 days (unusual for the jurisdiction), and a dispute resolution clause that names an arbitral seat not recognized under the UAE Federal Arbitration Law.

### Clause Library
The Clause Library is a curated repository of vetted contractual clauses organized by jurisdiction, language, drafting position, and risk tier. Each clause comes with notes on why the language was chosen, what risks it addresses, and what alternates are available.

*Use case:* A lawyer drafting a joint venture agreement in DIFC needs a deadlock resolution clause. She searches the library for "deadlock — DIFC — neutral" and gets three variants with comparative notes.

### Drafting Board
The Drafting Board is Louis's AI-assisted document editor. It starts from a template in the Document Library, allows the user to fill variable fields, and suggests clause alternatives in real time. It checks for internal consistency (defined terms, cross-references) and can auto-complete based on context.

*Use case:* A startup's in-house counsel opens the NDA template for Lebanon, fills in the party names and scope, and is prompted by Louis when the confidentiality period is left blank — Louis suggests 2 years as the regional default with an option to extend to 5.

### Document Workspace
The Document Workspace is a collaborative environment for the full lifecycle of a legal document — from first draft through review, redlining, and sign-off. It tracks versions, records comment resolutions, and exports to Word or PDF.

*Use case:* Three lawyers in different offices review a draft acquisition SPA. Each leaves comments; Louis summarizes open issues and suggests which are commercially negotiable vs. legally required resolutions.

### Justinian (Legal Education Module)
Justinian is HAQQ's legal-education sub-product, integrated into Louis. It provides bar exam prep, case brief generation, moot court rehearsal, and IRAC-structure coaching. Built for law students and junior lawyers building foundational legal reasoning skills.

*Use case:* A Lebanese law student preparing for the bar uses Justinian to generate case briefs on Lebanese Code of Obligations contract doctrine, then rehearses oral argument with Louis playing the examiner.

## Quality bar for generated explainers

- Concrete use cases, not abstract ones. Name the jurisdiction, role, and document type.
- No filler phrases ("a powerful tool that enables…"). Start with what it does.
- Do not overclaim: "helps you" is fine; "guarantees you will" is not.
- Length: 1 paragraph description + 1 use case as default. Adjust on request.

## Related skills

- [[academy-ai-feature-explainer]]
- [[academy-use-case-explainer]]
- [[academy-clause-library-explainer]]
- [[academy-legal-document-library-explainer]]
- [[academy-legal-ai-skills-catalog]]
