---
name: academy-legal-ai-skills-catalog
description: Use when a user, prospect, or developer wants to browse, filter, or understand the full public catalog of Louis's 982-skill library — filterable by category, jurisdiction, language, and priority. Serves transparency, competitive comparison, and developer/integration discovery purposes. Routes to this skill for "what skills does Louis have?", "do you cover [jurisdiction/practice area]?", or "show me what's available in your skill library" queries.
license: MIT
metadata: " id: academy.legal-ai-skills-catalog category: academy jurisdictions: [__multi__] priority: P3 intent: [__customer-facing__, skills-catalog, transparency, developer-discovery] related: [academy-ai-feature-explainer, academy-feature-explainer, academy-tools-catalog, academy-use-case-explainer] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'academy'.
Registered as a flat plugin skill.
-->


# Legal AI Skills Catalog — Louis's 982-Skill Public Library

## When to use this

Invoke when:
- A user asks "what skills does Louis have?"
- A prospect asks "do you cover KSA employment law?"
- A developer asks for the full skill inventory for integration planning
- A competitor-comparison question requires listing capabilities by category
- A sales conversation requires demonstrating coverage breadth
- A user wants to filter skills by language (Arabic, English, French)

## What the Skills Catalog is

The Louis Skills Catalog is a publicly accessible, filterable inventory of all 982 specialist AI skills in the platform. Its purpose is:

1. **Transparency**: users can see exactly what skills their requests are routed to, reducing black-box anxiety
2. **Discovery**: legal professionals find capabilities they did not know existed
3. **Competitive differentiation**: the breadth and MENA depth of the catalog is a key differentiator versus generic AI tools

## Catalog taxonomy

Skills are organized along five dimensions:

| Dimension | Values |
|---|---|
| Category | draft, review, research, casesim, academy, community, kb, connector, ops, router, justinian, and others |
| Practice area | corporate, employment, real estate, litigation, arbitration, IP, banking & finance, construction, data & privacy, criminal, family, immigration, tax |
| Jurisdiction | LB, UAE-onshore, DIFC, ADGM, QFC, KSA, EG, FR, UK, US, EU, OHADA, GCC |
| Language | Arabic (AR), English (EN), French (FR), bilingual AR-EN |
| Priority | P0 (critical path), P1 (core), P2 (extended), P3 (supplementary) |

## Coverage by category (high level)

### Drafting (draft) — ~180 skills
Contract drafting across all major practice areas and MENA jurisdictions. Each drafting skill includes required inputs, optional inputs, jurisdictional notes, and a document-structure outline. Key skill types:
- NDA / Confidentiality Agreements (unilateral, mutual, tri-party)
- Employment Contracts (UAE, KSA, Lebanon, Egypt; permanent, fixed-term, remote)
- Services Agreements (time-and-materials, fixed-fee, retainer)
- Share Purchase Agreements, Shareholder Agreements, JVAs
- Real Estate (SPA, lease, pre-sale, OQOOD registration)
- Construction (FIDIC-based, EPC, O&M)
- Banking & Finance (facility letters, security documents, guarantees)

### Review / Analysis (review, eval) — ~150 skills
Document review and risk analysis skills. These produce structured risk reports with severity tiers, issue identification, and recommended actions. Coverage mirrors drafting coverage.

### Case Simulation (casesim) — ~40 skills
Litigation training and scenario analysis: client Q&A prep, cross-examination rehearsal, judge-bench perspective, opposing-counsel simulation, outcome probability estimation, and settlement EV calculation.

### Knowledge Packs (kb, ref) — ~200 skills
Reference material organized by jurisdiction and subject: statutory frameworks, compliance thresholds, regulatory procedures, penalties. MENA-primary; GCC, EU, UK, FR, US secondary.

### Education (academy, justinian) — ~60 skills
Bar prep, IRAC coaching, moot court, career development, feature explainers, curriculum guides. See also the Justinian tutor (see [[academy-justinian-tutor]]).

### Connectors and Tools (connector, tool) — ~50 skills
Integrations with document management, e-signature (DocuSign, Tawqi3i), Microsoft 365, Google Workspace, legal databases.

### Research and Intelligence (research, intel) — ~80 skills
Jurisdiction-specific legal research templates, regulatory intelligence, legislative monitoring.

### Router and Orchestration (router, workflow) — ~30 skills
Skills that orchestrate other skills: multi-step legal flows, handoff logic, intake triage.

### Community and Growth (community, growth) — ~50 skills
Partner programs, bar-association engagement, influencer briefs, co-marketing.

### Conversational and Behavioral (conversation, safety, persona) — ~50 skills
Persona definitions, safety guardrails, output standards, on-topic enforcement.

## How to filter the catalog

In the Louis interface:
- Use the catalog search bar with natural-language queries
- Use the filter sidebar: category → jurisdiction → practice area → language → priority
- Use the API (`GET /skills?category=draft&jurisdiction=DIFC&lang=ar`) for developer access

## Transparency features

Each skill in the catalog exposes:
- Skill ID (e.g., `draft.NDA-mutual-UAE`)
- Category and practice area
- Jurisdiction list with coverage level (primary / secondary)
- Languages supported
- Last updated date
- Required and optional inputs
- Output format description

When a skill runs, the response includes a routing trace: which skill was selected, why, and at what confidence level.

## Competitive context

Most legal AI products do not publish their skill inventories. Louis's public catalog is a deliberate transparency choice: it signals that the system is not a black box and that coverage claims can be verified.

## Related skills

- [[academy-ai-feature-explainer]]
- [[academy-feature-explainer]]
- [[academy-tools-catalog]]
- [[academy-use-case-explainer]]
