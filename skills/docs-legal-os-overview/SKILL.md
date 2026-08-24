---
name: docs-legal-os-overview
description: Use when a user wants a high-level explanation of what the platform is and how it is positioned — the "Legal OS" concept that frames the platform as an operating system layer for the legal profession, integrating chat, drafting, review, calculation, compliance, and orchestration into a unified architecture. Covers the five architectural pillars and how they interrelate.
license: MIT
metadata: " id: docs.legal-os-overview category: docs jurisdictions: [__multi__] priority: P2 intent: [__docs__, legal os, platform overview, architecture, positioning] related: [docs-legal-ai-workspace-guide, docs-compare-us, docs-enterprise-deployment, docs-case-study-legal-ontology] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'docs'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Legal OS — Platform Overview

## The "Legal OS" concept

The platform is positioned as a **Legal Operating System** — not a single AI tool, but a layered platform that integrates every core activity in the legal profession into a unified, AI-powered environment. The analogy to an operating system is deliberate:

- Just as macOS or Windows provides a base layer that applications, files, and workflows run on top of, the Legal OS provides a base layer for legal practice: it handles document memory, jurisdictional context, skill invocation, and integration with external systems.
- Legal professionals do not switch between a "drafting tool", a "research tool", and a "matter management tool" — they work in one environment where AI assistance is available throughout.
- The platform is a **developer platform** as well as an end-user product: the skills architecture, API, and webhook system allow firms and legal ops teams to build custom tools on top of the Legal OS foundation.

## Five architectural pillars

### 1. Skills

The skill library is the core of the Legal OS. A skill is a pre-built, tested, jurisdiction-aware legal AI capability: drafting an NDA, reviewing a lease under Dubai law, conducting a statute-of-limitations analysis, running a trademark clearance intake.

Key characteristics:
- Skills are **modular**: they can be invoked individually or chained in automated flows.
- Skills are **jurisdiction-aware**: the same skill produces different outputs depending on the governing law and jurisdiction selected.
- Skills are **open**: the skill library is published as open source, allowing community contributions and custom skill development. See the mini-hermes-the-firm repository on GitHub.
- Skills are **routed**: the router skill analyzes user intent and automatically invokes the most relevant skill for each query.

As at the current version: 200+ skills covering MENA and secondary jurisdictions.

### 2. Clause library

The clause library is a structured, jurisdiction-annotated database of contract clauses, organized by document type, clause type, and governing law.

Key capabilities:
- **Insert clauses into drafts**: when drafting, select from pre-vetted clause variants for each provision.
- **Clause comparison**: compare how the same provision (e.g., limitation of liability) reads across three different jurisdictions.
- **Custom clauses**: firms can add their own standard clauses to the workspace clause library, tagged by matter type and jurisdiction.
- **Version control**: clause history tracks changes to the library over time, important for professional responsibility purposes.

### 3. Calculators

Legal calculators automate routine legal computations that practitioners currently do in spreadsheets:

- **EOSB (End of Service Benefit) calculator**: UAE Federal Decree-Law 33/2021 and older law; KSA Labor Law gratuity; LB indemnity. Inputs: start date, end date, last salary, allowances, termination type (resignation vs termination).
- **Limitation period calculator**: inputs: cause of action type, jurisdiction, date of breach; outputs: expiry date, days remaining, flag if imminent.
- **Rent increase calculator**: Dubai RERA rent increase index — inputs: current rent, market average from index; outputs: maximum permissible increase.
- **Liquidated damages reasonableness check**: tests whether a penalty clause is likely to be upheld or reduced by courts in each jurisdiction.
- **Dilution calculator**: equity/cap-table calculator for option pool sizing, round dilution, liquidation preference waterfall.

### 4. Flows

Flows are automated, multi-step legal workflows that chain skills, calculators, and external integrations together. A flow can:

- Be triggered by an event (new client intake form submitted, contract expiry approaching, email received from a counterparty).
- Execute a sequence of skills and transformations (intake → draft → review → approve → send).
- Route to a human for review or approval at any step.
- Integrate with external systems (HubSpot, DocuSign, Stripe, NetSuite) via the API and webhook system.

Flows make the Legal OS an active orchestration layer, not just a passive tool.

### 5. Integrations

The platform is designed to fit into a firm's existing technology stack, not replace it:

- **CRM**: HubSpot integration for client relationship management and matter origination tracking.
- **Billing**: Stripe integration for client billing and subscription management.
- **Accounting**: NetSuite, QuickBooks, Xero for matter billing and financial reconciliation.
- **Identity**: Okta, Azure AD, Google Workspace for SSO and user management.
- **Document management**: API available for integration with iManage, NetDocuments, or SharePoint.
- **E-signature**: integration with DocuSign and similar providers for contract execution workflows.
- **Communication**: WhatsApp sharing, email integration for document distribution.

## How the pillars work together

**Example workflow** — M&A NDA negotiation:

1. **Router** (skill) identifies the request as an NDA intake.
2. **Intake skill** (skill) collects parties, purpose, term, governing law.
3. **Draft NDA skill** (skill + clause library) generates the draft using the appropriate clause variants for the selected jurisdiction.
4. **Risk review** (skill) flags high-risk deviations from market standard.
5. **Multi-doc compare** (skill) generates a redline when the counterparty sends a markup.
6. **Matter** (platform feature) organizes all versions, correspondence, and decisions.
7. **Flow** (automation) notifies the responsible partner when a new version is received and routes for review.
8. **Clause library** (library) surfaces the firm's preferred language for disputed clauses.
9. **Calculator** (calculator) checks the limitation-of-liability cap against the deal size.
10. **Integration** (DocuSign) sends the final version for execution and records the signed version in the matter.

This is the Legal OS in action: every step is connected, AI-assisted, and jurisdiction-aware.

## Target users

| User type | Primary pillars used |
|---|---|
| **Solo practitioner / boutique firm** | Skills (drafting, review), Clause library, Calculators |
| **Mid-size law firm** | All five pillars; Flows for client intake and document workflows |
| **Corporate legal department** | Skills (contract review, compliance), Flows (contract lifecycle management), Integrations (CRM, accounting) |
| **Legal technology developer** | API, Skill library (as open-source foundation), Webhooks, Calculators |
| **Legal AI researcher** | Legal ontology API, Skill library, Case study documentation |

## Related skills

- [[docs-legal-ai-workspace-guide]]
- [[docs-compare-us]]
- [[docs-enterprise-deployment]]
- [[docs-case-study-legal-ontology]]
