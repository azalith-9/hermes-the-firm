---
name: docs-enterprise-deployment
description: Use when an enterprise prospect or IT administrator asks about deploying the platform at scale — tenant isolation, SSO, audit logs, custom data residency, SLA, implementation timeline, and dedicated support. This is a platform documentation skill covering the enterprise deployment model, implementation phases, security architecture, and customization options for law firm and corporate legal department deployments.
license: MIT
metadata: " id: docs.enterprise-deployment category: docs jurisdictions: [__multi__] priority: P2 intent: [__docs__, enterprise, sso, tenant isolation, implementation, dedicated support] related: [docs-audit-log-export, docs-data-residency-mena, docs-billing-and-credits, docs-dev-hub-api-reference] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'docs'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Enterprise Deployment

## Overview

The enterprise deployment tier is designed for law firms with 20+ users, corporate legal departments, and any organization that requires:

- Tenant isolation (dedicated infrastructure or logical separation).
- Single Sign-On (SSO) integrated with the organization's identity provider.
- Full audit log access and SIEM integration.
- Custom data residency (MENA/GCC, EU, or US hosting per compliance requirement).
- Enterprise SLA with dedicated support and a named customer success engineer.
- Custom branding and workspace configuration.

The typical implementation timeline is **4–6 weeks** from contract signature to full production deployment. A **pilot phase** (2–4 weeks, limited user group) is strongly recommended before full firm rollout.

## Security architecture

### Tenant isolation

Enterprise customers receive logical tenant isolation: all data, configuration, and audit trails are scoped to the organization's workspace and are inaccessible to other tenants. Dedicated infrastructure (single-tenant deployment) is available on request and negotiated as part of the enterprise agreement.

Key isolation boundaries:
- Database: per-tenant schemas with row-level security.
- Storage: per-tenant encrypted S3-equivalent buckets.
- AI model calls: workspace context is scoped; no cross-tenant context leakage.
- API keys: workspace-scoped; cannot access other workspaces.

### Encryption

- Data at rest: AES-256 encryption.
- Data in transit: TLS 1.2+ (TLS 1.3 where supported by the client).
- Encryption key management: AWS KMS (default) or customer-managed keys (CMK) on request.
- Customer-managed keys (BYOK): available for organizations that require key custody. Contact the sales team.

### Penetration testing and certifications

- SOC 2 Type II attestation: available on request under NDA.
- ISO 27001: certification in progress (verify current status).
- Penetration test reports: annual third-party pen tests; reports available under NDA for enterprise customers.

## Single Sign-On (SSO)

Enterprise customers can integrate with their organization's Identity Provider (IdP) using SAML 2.0 or OIDC:

- Supported IdPs: Okta, Microsoft Azure Active Directory (Entra ID), Google Workspace, PingIdentity, Auth0.
- SCIM 2.0 for automated user provisioning and deprovisioning.
- MFA: platform-level MFA available as a fallback; most enterprise customers use IdP-enforced MFA.
- Session management: configurable session timeout (default 8 hours; configurable 1–24 hours).

SSO configuration is completed during the implementation phase. The IT administrator requires access to the IdP to create the SAML/OIDC application configuration and to provide the platform with the metadata URL or certificate.

## Audit logs and compliance

Enterprise customers receive full audit log access, SIEM streaming, and configurable retention up to 7 years. See [[docs-audit-log-export]] for full detail.

Compliance artifacts available on request:
- Data Processing Agreement (DPA) — GDPR-compliant; also covers UAE PDPL and KSA PDPL.
- Sub-processor list.
- Records of processing activities (RoPA) template.
- Business Associate Agreement (BAA) — for US healthcare-adjacent matters (HIPAA).

## Custom data residency

Enterprise customers can select their data residency region at contract stage:
- **EU Frankfurt** (default).
- **MENA / GCC** (Bahrain region) — for GCC-regulated entities.
- **Saudi Arabia** (roadmap 2026 Q2) — for KSA PDPL and SAMA-regulated entities.
- **US East** — for US-incorporated entities.

See [[docs-data-residency-mena]] for full detail on regulatory drivers and migration process.

## Custom branding and workspace configuration

Enterprise workspaces can be configured with:
- Custom logo and color scheme in the platform UI.
- Custom subdomain (e.g., `legal.acmefirm.com` pointing to the platform).
- Custom email templates for user invitations and notifications.
- Default jurisdiction and language settings per workspace.
- Skill library restriction: administrators can restrict which skills are visible to their users (e.g., hide consumer-facing skills for a professional-only workspace).

## Implementation phases

| Phase | Duration | Activities |
|---|---|---|
| **1. Discovery** | Week 1 | Requirements gathering; IT/security review; data residency selection; SSO IdP details; user count and role mapping |
| **2. Configuration** | Weeks 2–3 | Tenant provisioning; SSO setup and testing; SIEM integration; custom branding; skill library configuration; audit log verification |
| **3. Pilot** | Weeks 3–4 | 5–15 pilot users (mix of power users and average users); use-case validation; feedback collection; training sessions |
| **4. Full rollout** | Week 5–6 | All-user provisioning (via SCIM or bulk import); firm-wide communication; optional live training sessions; CSM handover |

## Dedicated support

Enterprise customers receive:
- **Named Customer Success Manager (CSM)**: single point of contact for strategic questions, roadmap discussions, and escalation.
- **Named Technical Account Manager (TAM)**: for integration support, API questions, and incident escalation.
- **Enterprise SLA**: 99.9% uptime SLA; P1 incidents (platform down) resolved within 4 hours; P2 incidents (significant feature degradation) resolved within 24 hours.
- **Priority support queue**: tickets from enterprise customers are triaged and responded to within 4 business hours.
- **Executive business reviews (EBRs)**: quarterly reviews to discuss usage, ROI, and roadmap alignment.

## Pricing

Enterprise pricing is custom and negotiated based on:
- Number of seats.
- Usage credit bundle.
- Data residency region.
- Support level.
- Contract term (annual with multi-year discount available).

Self-serve pricing is listed on the pricing page. Enterprise pricing requires a sales conversation. See [[docs-billing-and-credits]] for plan tier context.

## How to use this doc

Direct IT administrators, legal operations directors, and enterprise procurement teams here when they ask:
- "What does your enterprise deployment look like?"
- "Do you support SSO with Okta/Azure AD?"
- "What is your SLA?"
- "Can we host our data in Saudi Arabia?"
- "How long does implementation take?"

For security questionnaires and RFPs, the sales team can provide a dedicated security questionnaire response document.

## Related skills

- [[docs-audit-log-export]]
- [[docs-data-residency-mena]]
- [[docs-billing-and-credits]]
- [[docs-dev-hub-api-reference]]
