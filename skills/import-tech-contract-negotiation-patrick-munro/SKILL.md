---
name: import-tech-contract-negotiation-patrick-munro
description: "Use when migrating the Patrick Munro technology contract negotiation methodology into the mini-hermes-the-firm format. This adapter maps structured tech-deal negotiation logic — SaaS/cloud agreement playbooks, data-processing addenda, IP ownership splits, limitation-of-liability battles, and market-standard position matrices — into the standard skill model. Primary contexts: DIFC, ADGM, UAE, UK, and cross-border technology transactions with MENA parties."
license: MIT
metadata: " id: import.tech-contract-negotiation-patrick-munro category: import jurisdictions: [DIFC, ADGM, UAE, UK, __multi__] priority: P3 intent: [__import__, tech-contract, negotiation, saas, migration, commercial-law] related: [import-legal-simulation-patrick-munro, import-vendor-due-diligence-patrick-munro, import-nda-review-jamie-tso, import-red-team-verifier-patrick-munro, review-contract-generic] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'import'.
Registered as a flat plugin skill.
-->


# Import: Tech Contract Negotiation (Patrick Munro)

## What it does

This import adapter migrates a **technology contract negotiation skill modelled on the Patrick Munro methodology** into the `mini-hermes-the-firm` standard format. The Munro tech-negotiation approach is a structured playbook for commercial technology deals: it identifies the key battlegrounds in a typical tech contract, maps each party's market-standard opening position, and gives the negotiator a principled framework for deciding where to push, where to concede, and where to walk away.

Technology contracts — SaaS agreements, cloud services terms, software licences, API access agreements, data-processing addenda (DPAs) — have become among the most common commercial documents in any legal practice. MENA jurisdictions are experiencing rapid technology adoption; standard US/UK template agreements frequently contain provisions that do not translate cleanly to civil-law or Islamic-finance contexts.

## Import config

| Field | Source mapping | Default if absent |
|---|---|---|
| `contract_type` | Legacy `type` | `saas_agreement` |
| `client_side` | Legacy `role` | `customer` (buyer's perspective) |
| `governing_law` | Legacy `governing_law` | `DIFC` |
| `playbook_depth` | Legacy `depth` | `full` (all battleground clauses) |
| `market_standard` | Legacy `market_ref` | `DIFC / UK market standard` |
| `output_format` | Legacy `format` | `negotiation_playbook` |
| `redline_output` | Legacy `produce_redline` boolean | `false` (analysis only; redlines via separate skill) |

## Dry-run preview

```
IMPORT PREVIEW — tech-contract-negotiation-patrick-munro
Source shape    : Tech negotiation playbook (Munro methodology)
Contract type   : SaaS agreement
Perspective     : customer (buyer)
Governing law   : DIFC
Depth           : full
Market standard : DIFC / UK
Output          : negotiation_playbook
Redline         : disabled (analysis only)
```

## Key battleground clauses

The Munro methodology identifies these as the primary negotiation battlegrounds in a technology contract:

### 1. Liability and limitation of liability
- **Mutual cap**: customer wants the supplier's liability cap to equal 12 months' fees (or higher); supplier starts at 100% of fees paid in prior 12 months
- **Exceptions to cap**: fraud, wilful misconduct, death/personal injury, and indemnities for IP infringement typically uncapped — flag if supplier seeks to cap these
- **Consequential loss exclusion**: supplier always seeks to exclude all indirect/consequential loss; customer should carve out: data breach damages, regulatory fines, and loss of data

### 2. Data processing and GDPR/PDPL compliance
- DPA (Data Processing Agreement / Addendum) must be attached for personal data processing
- Data residency: where is data stored? Is it compatible with GDPR Art 46 / UAE PDPL cross-border transfer rules?
- Sub-processors: right to object to new sub-processors; processor must notify before adding
- Data security: must meet ISO 27001 or equivalent standard; breach notification within contractually specified hours (72h for GDPR compliance)
- Return/deletion of data on termination: specific timeline and format

### 3. IP ownership and licence scope
- **Work product ownership**: for bespoke development, who owns deliverables? Customer should seek ownership; supplier will push for licence-back
- **Pre-existing IP**: supplier always owns its pre-existing IP; ensure licence is broad enough for customer's intended use
- **AI-generated output**: ownership of outputs from AI-powered tools is unsettled; negotiate express language
- **Improvements and feedback**: supplier often claims ownership of improvements derived from customer data — push back

### 4. Service levels and remedies
- **SLA**: uptime (99.9% vs 99.99%); measurement window (monthly vs annual); exclusions (maintenance windows, force majeure, customer-caused)
- **Credits**: meaningful? Must credits be requested? Are they the exclusive remedy (problematic)?
- **Termination right for persistent SLA failure**: essential; define trigger (e.g. SLA breach in 3 consecutive months)

### 5. Termination and exit
- **Convenience termination**: does customer have a right to terminate for convenience? Minimum notice period?
- **Termination for cause**: what triggers it? Material breach + cure period (30 days standard)
- **Data export on termination**: guaranteed format; migration assistance; minimum transition period
- **Price lock**: does the customer have pricing certainty for the full term? Or can supplier increase?

### 6. Governing law and dispute resolution
- DIFC or ADGM governing law preferred for UAE-based deals — provides certainty and common-law enforceability
- For KSA: Saudi law + SCCA (Saudi Center for Commercial Arbitration) or ICC arbitration
- Avoid US state law for MENA parties unless counterparty insists and strong commercial reasons exist

## Market-standard position matrix

| Issue | Customer position | Supplier position | Market standard (DIFC/UK) |
|---|---|---|---|
| Liability cap | 24 months' fees | 12 months' fees | 12 months' fees |
| Consequential loss | Carve-out data breach + regulatory fines | Full exclusion | Carve-out for breach of data obligations |
| DPA | ISO 27001 + 72h notification | Best endeavours | ISO 27001 + 72h notification |
| IP ownership | Customer owns work product | Supplier owns; grants licence | Licence-back model |
| SLA credits | Up to 30% monthly fee | Up to 10% | 10–15% |
| Termination for convenience | 30 days' notice | No right / 12 months | 3–6 months |

## MENA-specific negotiation notes

- **Arabic governing law**: if UAE government entity, expect Arabic language and UAE Federal Law governing law — negotiate for DIFC/ADGM as alternative
- **Riba (interest) provisions**: KSA counterparties may require late-payment provisions be restructured as agreed compensation rather than interest
- **Data residency**: UAE healthcare and financial data subject to sector-specific localisation requirements; verify before agreeing to global cloud hosting
- **VAT**: UAE and KSA have VAT; ensure contract is clear on whether fees are VAT-exclusive and which party bears VAT

## Failure modes

| Error | Likely cause | Resolution |
|---|---|---|
| `playbook_one_sided` | Source only addressed supplier perspective | Override `client_side: customer` |
| `governing_law_us` | Source assumed US law | Add DIFC/UK alternative positions |
| `dpa_missing` | Source had no data-processing section | Add DPA battleground as mandatory section |
| `sla_credits_exclusive_remedy` | Credits clause was the only SLA remedy | Flag HIGH risk; add termination right for persistent failure |

## Related skills

- [[import-legal-simulation-patrick-munro]]
- [[import-vendor-due-diligence-patrick-munro]]
- [[import-nda-review-jamie-tso]]
- [[import-red-team-verifier-patrick-munro]]
- [[review-contract-generic]]
