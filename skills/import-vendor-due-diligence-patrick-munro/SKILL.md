---
name: import-vendor-due-diligence-patrick-munro
description: Use when migrating the Patrick Munro vendor due-diligence methodology into the mini-hermes-the-firm format. This adapter maps structured third-party risk assessment logic — legal, financial, operational, and compliance due-diligence workstreams — into the standard skill model. Relevant for technology vendor selection, supply-chain risk management, M&A target diligence, and regulatory vendor-oversight requirements across MENA (UAE, KSA, LB) and common-law (DIFC, ADGM, UK) jurisdictions.
license: MIT
metadata: " id: import.vendor-due-diligence-patrick-munro category: import jurisdictions: [DIFC, ADGM, UAE, UK, KSA, LB, __multi__] priority: P3 intent: [__import__, vendor-due-diligence, third-party-risk, migration, commercial-law] related: [import-tech-contract-negotiation-patrick-munro, import-legal-simulation-patrick-munro, import-nil-contract-analysis-samir-patel, import-legal-risk-assessment-anthropic] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'import'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Import: Vendor Due Diligence (Patrick Munro)

## What it does

This import adapter migrates a **vendor due-diligence skill modelled on the Patrick Munro methodology** into the `mini-hermes-the-firm` standard format. Vendor due diligence (VDD) is the process of assessing a third party — a supplier, technology vendor, outsourcing partner, or acquisition target — before entering into a material commercial relationship.

The Munro VDD methodology applies a structured, multi-workstream framework that covers legal, financial, operational, compliance, and reputational risk. In MENA, vendor due diligence has heightened importance because of: beneficial-ownership transparency requirements (FATF), sanctions exposure (OFAC, EU, UK), and regulatory vendor-oversight obligations in financial services (DFSA, CBUAE).

## Import config

| Field | Source mapping | Default if absent |
|---|---|---|
| `vdd_type` | Legacy `type` | `commercial_vendor` |
| `workstreams` | Legacy `workstreams` array | Full 5-workstream model |
| `sanctions_check` | Legacy `check_sanctions` boolean | `true` |
| `beneficial_ownership` | Legacy `check_ubo` boolean | `true` |
| `financial_check` | Legacy `check_financials` boolean | `true` |
| `compliance_check` | Legacy `check_compliance` boolean | `true` |
| `reputational_check` | Legacy `check_reputation` boolean | `true` |
| `output_format` | Legacy `format` | `vdd_report` |
| `risk_matrix` | Legacy `matrix` | 3×3 severity × likelihood |

## Dry-run preview

```
IMPORT PREVIEW — vendor-due-diligence-patrick-munro
Source shape       : Vendor DD (Munro methodology)
VDD type           : commercial_vendor
Workstreams        : 5 (legal + financial + operational + compliance + reputational)
Sanctions check    : enabled
Beneficial ownership: enabled
Financials         : enabled
Compliance         : enabled
Reputational       : enabled
Output             : vdd_report
```

## Five-workstream framework (post-import)

### Workstream 1 — Legal
- Corporate existence and good standing: company registration, certificate of incorporation, registered address
- Ownership structure: corporate chart; identify ultimate beneficial owners (UBOs) to required threshold (UAE: 25%; EU/UK: 25%)
- Authorised signatories: verify the individuals who will sign contracts have authority to bind the vendor
- Litigation and disputes: any pending or threatened litigation material to the relationship?
- IP ownership: does the vendor own (or have adequate licences for) the IP embedded in its products/services?
- Contractual restrictions: any exclusivity, change-of-control, or non-compete provisions that affect the proposed relationship?

### Workstream 2 — Financial
- Financial statements: last 2–3 years' audited accounts
- Solvency indicators: debt/equity ratio, current ratio, cash position
- Accounts payable/receivable: are suppliers being paid? Is revenue concentrated in one customer?
- Insurance: professional indemnity, cyber liability, public liability — adequate for the contract risk profile?
- Pricing sustainability: is the vendor's pricing model financially sustainable? (Relevant for critical dependencies)

### Workstream 3 — Operational
- Capacity and scalability: can the vendor meet contract volume requirements?
- Business continuity and disaster recovery: does the vendor have a tested BCP/DR plan?
- Key-person dependency: is performance dependent on specific individuals? What is the retention risk?
- Sub-contractor chain: who does the vendor itself sub-contract to? Does the sub-contractor chain meet the same standards?
- Data security: ISO 27001 certification or equivalent; penetration testing cadence

### Workstream 4 — Compliance
- Sanctions screening: screen vendor name, UBOs, and directors against OFAC SDN list, EU Consolidated list, UK HMT list, and UN sanctions list
- AML/KYC: source of funds verification for financial-services vendors; FATF risk classification
- Bribery and corruption: any adverse press on corruption? FCPA/UK Bribery Act/Sapin II exposure?
- Data protection: GDPR / UAE PDPL compliance for vendors handling personal data; DPA execution required?
- Sector-specific licences: does the vendor hold all required regulatory licences for its activities?

### Workstream 5 — Reputational
- Adverse media screening: systematic search for negative press on vendor, directors, and UBOs
- ESG and human rights: any supply-chain labour or environmental concerns (particularly for MENA manufacturing vendors)?
- Political exposure: are UBOs politically exposed persons (PEPs)?
- Customer references: speak to existing customers; check for patterns in complaints or disputes

## MENA-specific due-diligence notes

- **UAE beneficial ownership**: UAE Federal Decree-Law 32/2021 (Commercial Companies Law) requires UBO registers; DIFC / ADGM have their own UBO registers; check all registers for the target's registered entities
- **KSA**: Saudi Ministry of Commerce company registry searchable online; check Sanadic portal for sanctions
- **Lebanon**: company registry information quality is variable; rely on notarial records and legal counsel confirmation
- **OFAC**: UAE companies with Iranian or Russian beneficial ownership create OFAC exposure; this is a HIGH risk requiring immediate escalation
- **DFSA / CBUAE outsourcing**: regulated firms in DIFC/UAE have mandatory vendor oversight obligations; VDD report is required documentation for material outsourcing arrangements

## VDD report output schema

```
VENDOR DUE DILIGENCE REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Vendor         : [name]
VDD date       : [date]
Prepared by    : [team / counsel]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WORKSTREAM SUMMARY
Legal          : [PASS / ISSUES / FAIL] — [key findings]
Financial      : [PASS / ISSUES / FAIL] — [key findings]
Operational    : [PASS / ISSUES / FAIL] — [key findings]
Compliance     : [PASS / ISSUES / FAIL] — [key findings]
Reputational   : [PASS / ISSUES / FAIL] — [key findings]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OVERALL RISK: LOW / MEDIUM / HIGH / CRITICAL
RECOMMENDATION: Proceed / Proceed with conditions / Do not proceed
CONDITIONS (if applicable): [list of conditions precedent to proceeding]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Failure modes

| Error | Likely cause | Resolution |
|---|---|---|
| `sanctions_check_disabled` | Legacy skipped sanctions workstream | Enable; mandatory for MENA-facing vendors |
| `ubo_not_identified` | Legacy stopped at registered directors | Push to 25% threshold; flag if any UBO is PEP |
| `financial_check_skipped` | Legacy assumed creditworthy | Add minimum: last 2 years' accounts or credit report |
| `sub_contractor_chain_ignored` | Legacy only assessed prime vendor | Extend Workstream 3 to material sub-contractors |
| `ofac_not_checked` | OFAC check absent | Add as mandatory gate; CRITICAL risk if positive hit |

## Related skills

- [[import-tech-contract-negotiation-patrick-munro]]
- [[import-legal-simulation-patrick-munro]]
- [[import-nil-contract-analysis-samir-patel]]
- [[import-legal-risk-assessment-anthropic]]
- [[import-red-team-verifier-patrick-munro]]
