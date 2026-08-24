---
name: docs-case-study-legal-ontology
description: "Use when a user asks how the platform structures, classifies, and interrelates legal concepts — or when a developer or legal knowledge engineer wants to understand the underlying legal ontology that powers skill routing, clause libraries, and jurisdictional mapping. This is a platform documentation skill covering the legal ontology architecture: concept nodes, relationship types, jurisdiction overlays, and how the ontology is used in practice."
license: MIT
metadata: " id: docs.case-study.legal-ontology category: docs jurisdictions: [__multi__] priority: P2 intent: [__docs__, legal ontology, knowledge graph, concept mapping, legal AI architecture] related: [docs-legal-os-overview, docs-dev-hub-api-reference, docs-legal-ai-workspace-guide] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'docs'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Case Study: Legal Ontology

## What a legal ontology is

A legal ontology is a structured, machine-readable representation of legal concepts, their relationships, and their jurisdictional applicability. It answers questions like:

- "What is a 'force majeure clause' and how does it relate to 'material adverse change'?"
- "Which skills are relevant when a user mentions 'employment termination' in a KSA context?"
- "What is the relationship between a 'shareholders' agreement' and a 'shareholders' resolution'?"

The platform's legal ontology is the backbone of skill routing (how the router decides which skill to invoke), clause library organization, and jurisdiction-specific guidance surfacing.

## Architecture

The legal ontology is organized as a directed graph with three layers:

### Layer 1: Concept nodes

Every legal concept relevant to the platform's jurisdiction coverage is represented as a node. Nodes fall into categories:

| Node type | Examples |
|---|---|
| **Document types** | NDA, Employment Contract, Shareholders' Agreement, Power of Attorney, Lease, Will |
| **Clauses / provisions** | Force majeure, Limitation of liability, Non-compete, ROFR, Drag-along, Liquidated damages |
| **Legal concepts** | Consideration, Breach, Specific performance, Unjust enrichment, Piercing the corporate veil |
| **Actors** | Employer, Employee, Lessor, Lessee, Grantor, Beneficiary, Director, Shareholder |
| **Events / triggers** | Termination, Default, Change of control, Insolvency, Force majeure event |
| **Jurisdictions** | UAE, KSA, LB, EG, DIFC, ADGM, FR, UK, US |
| **Regulatory bodies** | MOHRE, SAMA, BdL, DIFC Authority, ADGM FSRA, SEC |

### Layer 2: Relationship types

Relationships between nodes are typed:

| Relationship | Example |
|---|---|
| `IS_A` | "Employment Contract IS_A Contract" |
| `HAS_CLAUSE` | "NDA HAS_CLAUSE Confidentiality Period" |
| `GOVERNED_BY` | "DIFC Employment HAS_GOVERNING_LAW DIFC Employment Law No. 2/2019" |
| `REQUIRES` | "Lease in Dubai REQUIRES Ejari Registration" |
| `CONFLICTS_WITH` | "US at-will termination CONFLICTS_WITH UAE mandatory EOSB" |
| `SIMILAR_TO` | "ROFR SIMILAR_TO ROFO" |
| `TRIGGERS` | "Change of Control TRIGGERS Tag-Along Right" |

### Layer 3: Jurisdiction overlays

Each concept node carries jurisdiction-specific metadata:

- Which jurisdictions the concept is recognized in.
- Whether it is mandatory, default, or optional in each jurisdiction.
- Statutory references (where verified at high confidence).
- Common traps or conflicts unique to each jurisdiction.

For example, the "Liquidated Damages" clause node carries:
- **UAE**: enforceable; courts may reduce if grossly disproportionate (Federal Civil Transactions Law).
- **DIFC**: enforceable if a genuine pre-estimate of loss; penalty clauses void (common law rule).
- **KSA**: enforceable but courts apply equity to reduce excessive amounts.
- **France**: judiciary may reduce if manifestly excessive (Code Civil Art. 1231-5).
- **LB**: courts have discretion to reduce (Code of Obligations and Contracts Art. 263).

## How the ontology is used in practice

### Skill routing

When the router receives a user query, it parses the query for concept nodes mentioned (explicitly or implicitly) and uses ontology relationships to identify the most relevant skills. Example:

User: "I need to draft an agreement so my employees don't steal my clients when they leave."

Ontology resolution: "employees" → Employee node; "clients" → Customer/Client node; "leave" → Employment Termination event; "steal my clients" → Non-solicitation clause. Router resolves to [[conversation-intake-employment-contract]] with non-solicitation flag, and optionally [[draft-employment-contract-uae]] if jurisdiction is known.

### Clause library organization

The clause library is organized by ontology nodes. When a user is drafting a contract and needs to insert a "limitation of liability" clause, the clause library queries the ontology for:
- All "Limitation of Liability" clause variants.
- Jurisdiction-specific versions of each.
- Related clauses (consequential damages exclusion, IP indemnity carve-out).

### Jurisdiction conflict detection

The ontology's `CONFLICTS_WITH` relationships power the jurisdiction conflict detector: when a user imports a US-law contract and asks to apply KSA law, the system flags all clauses where the US standard conflicts with KSA requirements (e.g., "at-will termination" clause CONFLICTS_WITH "KSA Labor Law mandatory termination procedures").

## Developer integration

The ontology is accessible via the platform API:

```
GET /api/v1/ontology/concepts?query=force+majeure&jurisdiction=DIFC
GET /api/v1/ontology/relationships?from=NDA&type=HAS_CLAUSE
GET /api/v1/ontology/jurisdictions?concept=liquidated-damages
```

See [[docs-dev-hub-api-reference]] for full schema and authentication requirements.

## How to use this doc

Direct developers and legal knowledge engineers here when they ask:
- "How does the platform organize legal concepts?"
- "Why did the router suggest skill X for my query?"
- "Can I add a custom concept to the ontology?"
- "How do I query the clause library by jurisdiction?"

For end-user questions about what the product does (not how it is structured internally), direct to [[docs-legal-ai-workspace-guide]] or [[docs-legal-os-overview]] instead.

## Caveats and currency

The legal ontology is a working knowledge base, not a definitive legal reference. Concept nodes and relationships are maintained by the platform's legal knowledge team and updated as laws change. Do not rely on ontology metadata as a substitute for jurisdiction-specific legal advice. Statute references in the ontology carry confidence tiers consistent with [[conversation-uncertainty-language]] standards.

## Related skills

- [[docs-legal-os-overview]]
- [[docs-dev-hub-api-reference]]
- [[docs-legal-ai-workspace-guide]]
