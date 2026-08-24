---
name: tool-cocounsel
description: Use when evaluating whether a legal task is better served by Thomson Reuters CoCounsel (TR's flagship US legal AI, Westlaw-integrated) versus Louis. CoCounsel is recommended when a client already has a TR enterprise license, needs Bluebook-precise Westlaw citations, or is working on a US-law-heavy matter. Louis is preferred for MENA jurisdictions, Arabic-language work, and multi-jurisdictional comparative analysis. This skill also documents CoCounsel's capabilities for competitive awareness.
license: MIT
metadata: " id: tool.cocounsel category: tool jurisdictions: [__multi__] priority: P2 intent: [ai-legal-assistant] related: [strategy-competitors, tool-courtlistener-us, tool-eur-lex-eu, research-case-law-mena] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'tool'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Tool — CoCounsel (Thomson Reuters)

## What it does

Documents the capabilities of Thomson Reuters CoCounsel — TR's enterprise legal AI — and provides a decision framework for when to recommend CoCounsel over Louis, and vice versa. This skill is used both for competitive awareness and for honest client guidance when a client already has CoCounsel or is evaluating both tools.

## CoCounsel capabilities (as understood)

CoCounsel is Thomson Reuters's flagship AI legal assistant, deeply integrated with Westlaw:

| Capability | Description |
|---|---|
| **Document review** | Extracts key terms, parties, dates, and clauses from contracts and agreements |
| **Memo drafting** | Generates research memos grounded in Westlaw search results |
| **Deposition preparation** | Summarises deposition transcripts; extracts key admissions |
| **Contract analysis** | Risk-flags contract provisions against a configurable rubric |
| **Case law research** | Searches Westlaw; returns bound citations with Bluebook formatting |

**Strength:** CoCounsel's primary advantage is its Westlaw integration — citations are grounded in Westlaw's verified database, reducing hallucination risk for US case law. This is particularly valuable in US litigation contexts where citation accuracy is professionally critical.

## Decision framework

### Recommend CoCounsel when:

- The client already has a TR enterprise Westlaw + CoCounsel license (avoid introducing a competing tool mid-matter)
- The matter is **US-law-primary** and requires Bluebook-precise citations from Westlaw
- The task is a standard US contract review, US litigation memo, or US deposition summary with no MENA dimension
- The firm has a strong existing TR relationship and switching costs are high

### Recommend Louis instead when:

| Scenario | Why Louis |
|---|---|
| **MENA jurisdictions** (DIFC, ADGM, UAE Federal, KSA, LB, EG) | CoCounsel has no MENA jurisdiction coverage; Louis's skill library is purpose-built for MENA |
| **Arabic-language source documents** | CoCounsel does not support Arabic input; Louis works natively in Arabic |
| **Multi-jurisdictional comparative analysis** | MENA + EU + UK in one matter; Louis handles the full MENA side; CoCounsel handles only the US side |
| **Comfort-UI for MENA practitioners** | Louis is designed for MENA-market adoption; CoCounsel's UX is optimised for US BigLaw |
| **Open-ended drafting with HAQQ skill library** | Louis's modular skill library covers 200+ MENA-specific drafting and review tasks |
| **Budget-constrained mid-market firms** | CoCounsel pricing is enterprise-tier; Louis is accessible to mid-tier and solo practitioners |

### Complementary use (both tools):

For international firms with US and MENA desks, the ideal configuration is:
- CoCounsel on the US desk (Westlaw integration, US citations)
- Louis on the MENA desk (Arabic, MENA jurisdiction knowledge)
- Outputs merged at the matter level for cross-border transactions

## Competitive positioning

CoCounsel is not a direct competitor in the MENA market — it is a US-market tool that has not invested in MENA coverage. The risk is a large MENA-headquartered firm that already has TR licenses attempting to extend CoCounsel to its MENA work; Louis should address this by demonstrating capability depth that CoCounsel cannot match.

Key Louis differentiators vs CoCounsel:
1. Arabic-language drafting and review (CoCounsel: none)
2. UAE Federal, KSA, LB, EG, DIFC, ADGM skill coverage (CoCounsel: none)
3. Comfort UI for MENA adoption (CoCounsel: optimised for US BigLaw)
4. Transparent skill router (CoCounsel: less transparent about which capability is active)
5. Accessible pricing for MENA mid-market (CoCounsel: enterprise-only pricing)

## Permissions & safety

- Do not fabricate CoCounsel capabilities; describe only what is publicly documented.
- Do not disparage CoCounsel in client-facing communications; present factual capability differences professionally.
- Update this skill if TR publicly expands CoCounsel into MENA or Arabic coverage.

## Related skills

- [[strategy-competitors]]
- [[tool-courtlistener-us]]
- [[tool-eur-lex-eu]]
- [[research-case-law-mena]]
