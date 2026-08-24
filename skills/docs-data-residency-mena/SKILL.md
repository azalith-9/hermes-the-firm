---
name: docs-data-residency-mena
description: Use when a user asks where their data is hosted, which data residency options are available, or how to configure their workspace for MENA-region data hosting. This is a platform documentation skill covering data residency options (EU Frankfurt default, MENA/GCC on request, Saudi-region roadmap), per-tenant configuration, and the regulatory drivers that make data residency critical for MENA legal professionals.
license: MIT
metadata: " id: docs.data-residency-MENA category: docs jurisdictions: [UAE, KSA, LB, EG, EU, __multi__] priority: P2 intent: [__docs__, data residency, data localization, GCC hosting, cloud compliance] related: [docs-enterprise-deployment, docs-audit-log-export, docs-cookie-policy-summary] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'docs'.
Registered as a flat plugin skill.
-->


# Data Residency — MENA

## Why data residency matters for legal AI

Legal professionals work with highly sensitive client data: M&A deal terms, litigation strategy, personal data of counterparties, financial information. Where this data is hosted — and under which jurisdiction's legal system it falls — is a compliance, professional responsibility, and increasingly a contractual requirement.

Key regulatory drivers in the MENA region:

| Jurisdiction | Data localization requirement |
|---|---|
| **KSA** | Personal Data Protection Law (PDPL, SDAIA): sensitive personal data must be processed within Saudi Arabia. Financial sector: Saudi Central Bank (SAMA) cloud computing framework requires financial data to be hosted in KSA for licensed entities. |
| **UAE** | No general data localization law, but UAE PDPL restricts cross-border transfers of personal data to countries without adequate protections unless safeguards (contractual clauses, consent) are in place. DIFC: DIFC Data Protection Law 2020 restricts transfers to non-adequate destinations. |
| **UAE — financial sector** | Central Bank of the UAE (CBUAE): cloud circulars require financial institutions to maintain data within UAE or to seek regulatory approval for offshore hosting. |
| **Lebanon** | No enacted data protection law as at 2025 (draft law pending — verify current status). No mandatory data localization. |
| **Egypt** | Data Protection Law (Law No. 151/2020): personal data processing must follow principles of adequacy and purpose limitation; cross-border transfers require NCPD approval or adequate safeguards. |
| **EU** | GDPR Chapter V: transfers outside the EEA require adequacy decisions, SCCs, BCRs, or other Article 46 mechanisms. EU standard is the benchmark for "adequate protection" analysis. |

## Available data residency options

### EU — Frankfurt, Germany (default)

- **Default for all plans** unless otherwise configured.
- AWS Frankfurt region (eu-central-1).
- GDPR compliance: standard contractual clauses (SCCs) in place for any processing that involves EU personal data.
- Adequate for most MENA customers whose client data does not include KSA-localized sensitive personal data.
- ISO 27001 certified infrastructure.

### MENA / GCC region hosting

- **Available on request** for customers with MENA data localization requirements.
- Hosted in the AWS Bahrain region (me-south-1) or equivalent GCC-region cloud infrastructure.
- Nearest to UAE, KSA, LB, EG client data.
- Required for: UAE financial institutions subject to CBUAE cloud guidance; KSA entities subject to SAMA cloud framework; customers whose client data consists primarily of GCC-domiciled personal data.
- Setup time: 2–4 weeks from request confirmation. Requires enterprise plan.

### Saudi Arabia region (roadmap)

- **Planned for 2026 Q2** (as at planning date — verify current status with the sales or product team).
- Will be hosted in AWS Riyadh region or equivalent Saudi-region cloud provider.
- Required for entities processing KSA-localized sensitive personal data under the PDPL and SAMA cloud circular.
- Early access program available for KSA enterprise customers — contact the sales team.

### US region

- **Available on enterprise plans** for customers whose investors or parent entities require US-hosted legal data.
- AWS US-East region.
- Appropriate for: US-incorporated entities using the platform for US operations; venture-backed startups with US investor data protection requirements.

## Per-tenant configuration

Data residency is configured per workspace (tenant). The workspace administrator selects or changes the data residency region at **Settings → Security & Compliance → Data Residency**.

Important:
- Changing data residency regions triggers a **data migration** that must be scheduled and confirmed. Data is migrated securely with no downtime for read operations; write operations are paused during the migration window (typically 1–4 hours for workspaces under 50 GB).
- Once migrated, all new data is created in the new region. Historical data is migrated to the new region within the maintenance window.
- A confirmation email is sent to all workspace administrators when a data residency change is initiated and completed.

## What "data residency" covers

The data residency region applies to:

- All legal document content (drafts, templates, clause library customizations).
- All matter metadata (client names, matter descriptions, party information).
- All conversation history (chat transcripts, intake sessions).
- All audit logs (retained in the same region; see [[docs-audit-log-export]]).
- All user-uploaded documents (PDFs, Word documents, scanned contracts).

It does **not** apply to:
- Platform operational logs (anonymized telemetry for platform performance monitoring), which are retained centrally.
- Payment processing data, which is handled by Stripe in accordance with PCI DSS requirements.

## What to tell clients asking about data residency

For a GCC-based law firm evaluating the platform:

1. Default EU hosting meets the adequacy standard for most client data.
2. For clients with KSA-regulated financial data or UAE financial institution requirements, MENA region hosting is the right choice.
3. The Saudi Arabia region option (2026 Q2 roadmap) will be required for full PDPL compliance for KSA-sensitive-data categories.
4. Data residency configuration is per-workspace, not per-user — if the firm has both a Dubai office (EU hosting is fine) and a Riyadh entity (MENA hosting required), they should configure separate workspaces.

## Related skills

- [[docs-enterprise-deployment]]
- [[docs-audit-log-export]]
- [[docs-cookie-policy-summary]]
- [[docs-faq-pack]]
