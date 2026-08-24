---
name: docs-security-overview
description: Use when a prospect, customer, IT/security team, or procurement evaluator asks about Louis's security posture, data handling practices, compliance certifications, or infrastructure protections. Covers encryption standards, tenant isolation, access controls, certification roadmap (SOC 2, ISO 27001), no-training defaults, and zero-trust architecture. Applicable to all enterprise and regulated-sector deployments across all jurisdictions.
license: MIT
metadata: " id: docs.security-overview category: docs jurisdictions: [__multi__] priority: P2 intent: [security, data protection, compliance certifications, encryption, enterprise] related: [docs-tenant-isolation-explainer, docs-sso-saml-setup, docs-team-roles-permissions, docs-terms-of-service-summary] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'docs'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Security Overview — Louis Legal AI Platform

## Purpose

This document answers the security questions that enterprise procurement, IT, and compliance teams ask before deploying a legal AI platform. It is designed to be shared directly with prospects or used as a briefing sheet for sales and customer-success teams.

## Certification roadmap

| Framework | Status | Target |
|---|---|---|
| SOC 2 Type II | In preparation | 2026 |
| ISO 27001 | In preparation | 2026 |
| Penetration testing | Annual third-party pentest | Ongoing |
| GDPR Article 28 DPA | Available on request | Now |
| UAE PDPL compliance | Under review | 2025 |

> Note: Certification timelines are targets and subject to audit completion. Customers requiring current certifications should request the latest status letter from their account manager.

## Data encryption

### At rest
- **AES-256** encryption for all stored data, including documents, conversation history, and generated outputs.
- Encryption keys are managed per-tenant via a Key Management Service (KMS); customer-managed keys (BYOK) available on Enterprise tier.
- Database-level encryption applies to all Postgres-hosted data; backup snapshots are also encrypted.

### In transit
- **TLS 1.3** for all client-server and service-to-service communication.
- Older TLS versions (1.0, 1.1) are disabled. TLS 1.2 retained only where strictly required for legacy IdP compatibility.
- HSTS enforced on all web endpoints; certificate pinning on mobile clients.

## Tenant isolation

Each customer organization is a logically isolated tenant:

- **Row-Level Security (RLS)** applied at the Postgres layer so no query can return rows belonging to another tenant even if application code were to malfunction.
- **Dedicated KMS keys per tenant** — a compromise of one tenant's key does not expose others.
- **No cross-tenant data sharing** — AI models do not see or learn from other tenants' documents.
- Admin tooling requires **dual-control authorization** for any action that crosses tenant boundaries.

See [[docs-tenant-isolation-explainer]] for the technical deep-dive.

## Training data policy — no-training default

By default, **customer documents are never used to train or fine-tune AI models**. This is a contractual commitment, not just a configuration option. Enterprise DPAs include an explicit prohibition on training use. For customers requiring further assurance, a Data Processing Agreement (DPA) is available that codifies this obligation.

## Access controls

### Zero-trust architecture
- No implicit trust based on network location; all requests require authentication and authorization.
- Service-to-service calls use short-lived tokens with least-privilege scopes.
- Administrative access to production infrastructure requires MFA, short-lived credentials, and audit logging of every action.

### User authentication
- Email + password (bcrypt-hashed, salted) as baseline.
- MFA (TOTP / hardware key) available on all plans; required on Enterprise.
- SSO via SAML 2.0 supported — see [[docs-sso-saml-setup]] for setup.

### Role-based access
- Five platform roles: Admin, Billing Admin, Lawyer, Paralegal, Viewer.
- Custom roles on Enterprise tier.
- See [[docs-team-roles-permissions]] for the full permissions matrix.

## Infrastructure security

| Control | Detail |
|---|---|
| Hosting | Managed cloud infrastructure (AWS primary region; region selection available for data-residency requirements) |
| Network | VPC isolation, private subnets for data tier, WAF on public endpoints |
| Secrets management | All credentials and API keys in a secrets manager; never in environment variables or code |
| Logging | Centralized audit log with tamper-resistant storage; customer-accessible activity log in-product |
| Incident response | Documented IR plan; customer notification within 72 hours of confirmed breach (GDPR and UAE PDPL aligned) |
| Vulnerability management | CVE scanning on all dependencies; critical patches within 24 hours; high-severity within 7 days |
| Backup | Daily encrypted backups with point-in-time recovery; tested quarterly |

## Data residency

- Default region: EU (Frankfurt) or UAE (depending on tenant's selected region at onboarding).
- MENA customers may request UAE-only data residency to satisfy UAE Federal Law on Data Protection, Saudi PDPL, or Lebanese preferences.
- Cross-border data transfer: covered by standard contractual clauses (EU SCCs) or equivalent where required.

## Legal-sector specific protections

- Attorney-client privilege considerations: Louis does not index or share contents of uploaded documents with any third party other than the AI model provider under a sub-processor DPA.
- Bar association technology guidelines: customers should independently verify that use of cloud-hosted AI services complies with their jurisdiction's professional responsibility rules (notably Lebanese Bar, DIFC Courts practice direction on AI, UAE Ministry of Justice guidelines).

## Penetration testing and audits

- Annual third-party penetration test by a qualified security firm.
- Summary pen-test reports available to Enterprise customers under NDA.
- Customers with specific compliance requirements (banking, insurance, DFSA-regulated entities) may request custom security assessments.

## How to use this overview

- **Sales calls**: share the encryption and no-training sections first — these answer 80% of initial objections.
- **IT/security review**: provide the full document plus the DPA template.
- **Procurement questionnaires**: map each question to the relevant section; for gaps, escalate to security@haqq.ai.

## Related skills

- [[docs-tenant-isolation-explainer]]
- [[docs-sso-saml-setup]]
- [[docs-team-roles-permissions]]
- [[docs-terms-of-service-summary]]
- [[docs-roi-calculator]]
