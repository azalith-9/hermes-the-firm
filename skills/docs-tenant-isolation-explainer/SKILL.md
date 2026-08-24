---
name: docs-tenant-isolation-explainer
description: "Use when a customer's security team, DPO, or IT architect asks how Louis prevents one law firm's data from being accessible to another, or how the platform enforces data separation at the infrastructure level. Explains the multi-tenant architecture: per-tenant Postgres row-level security, dedicated KMS keys, no cross-tenant queries, and dual-control on admin tooling. Critical for enterprise procurement and regulated-sector deployments."
license: MIT
metadata: " id: docs.tenant-isolation-explainer category: docs jurisdictions: [__multi__] priority: P2 intent: [tenant isolation, data separation, multi-tenant, security architecture, RLS] related: [docs-security-overview, docs-team-roles-permissions, docs-sso-saml-setup] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'docs'.
Registered as a flat plugin skill.
-->


# Tenant Isolation Architecture

## Why this matters for legal AI

Legal documents contain some of the most sensitive data in existence: M&A strategies, litigation positions, client secrets, regulatory filings. A multi-tenant legal AI platform must provide ironclad guarantees that a leak across tenants — even through a software bug, misconfiguration, or insider threat — is architecturally prevented, not just policy-prevented.

Louis's tenant isolation is defense-in-depth: multiple independent technical controls must all fail simultaneously for cross-tenant access to occur.

## Layer 1 — Logical database isolation via Row-Level Security (RLS)

Every table in the Louis Postgres database that holds tenant data carries a `tenant_id` column. PostgreSQL Row-Level Security (RLS) policies are attached to every such table:

```sql
-- Example RLS policy (illustrative)
CREATE POLICY tenant_isolation ON documents
  USING (tenant_id = current_setting('app.current_tenant_id')::uuid);
```

This means:
- Every database connection operates within a tenant context (set at session start).
- A `SELECT * FROM documents` query, even if executed by a bug in the application, **physically cannot return rows from another tenant** — the database engine filters them out before returning results.
- RLS policies are enforced by the database, not by application code, so they cannot be bypassed by application-layer flaws.

Periodic automated tests verify that cross-tenant queries return zero rows.

## Layer 2 — Dedicated KMS encryption keys per tenant

Each tenant is provisioned with its own encryption key in the Key Management Service (KMS):

- Documents at rest are encrypted with the tenant's key.
- Backups are encrypted with the tenant's key.
- Even if an attacker obtained the raw database bytes for another tenant's rows, decryption would require that tenant's key — which is cryptographically isolated.
- Key rotation can be performed per tenant without affecting others.
- On Enterprise tier, **Bring Your Own Key (BYOK)** is available: the tenant holds the master key in their own KMS (AWS KMS, Azure Key Vault, or GCP Cloud KMS), and Louis never has access to it.

## Layer 3 — Application-layer tenant context enforcement

The application sets tenant context at the start of every request:

1. JWT/session token is validated.
2. The `tenant_id` embedded in the token is extracted.
3. The database session variable `app.current_tenant_id` is set to that value.
4. All queries for the request duration are scoped to that tenant.

Tenant context is never passed as a user-supplied parameter — it comes only from the validated token.

## Layer 4 — No cross-tenant admin operations without dual control

Administrative operations that could potentially access multiple tenants (e.g., a bulk data export, a support engineer reviewing logs) require:

1. A request logged in the admin audit system with stated justification.
2. Approval from a second authorized administrator (dual-control).
3. All actions taken in the admin context are logged immutably with actor, timestamp, tenant accessed, and operation performed.

Support engineers never have standing access to tenant data. Access is granted on a time-limited, purpose-bound basis with full audit trail.

## Layer 5 — AI model isolation

- Prompts and documents submitted to the AI model are processed in isolated request contexts.
- No document content from one tenant is ever included in the context window of a request from another tenant.
- Model fine-tuning or learning from tenant data does not occur by default (no-training policy — see [[docs-security-overview]]).
- If a tenant uses a custom model fine-tuned on their own data, that model is not shared with any other tenant.

## What "logically isolated" means (and doesn't mean)

**Logical isolation** means tenants share the same underlying database infrastructure and servers, but technical controls ensure their data is completely separated. This is the industry-standard approach for SaaS at scale and is equivalent to the isolation provided by AWS RDS, Google Cloud SQL multi-tenancy, and similar managed services.

**Physical isolation** (dedicated servers, dedicated database instances) is available on Enterprise tier upon request. This provides the strongest possible guarantee and may be required by certain regulated entities (DFSA-regulated firms, Saudi SAMA-supervised institutions, etc.).

## Compliance alignment

| Requirement | How tenant isolation addresses it |
|---|---|
| GDPR Art. 25 (data protection by design) | RLS + KMS ensures data minimization at the technical layer |
| UAE PDPL data security obligations | Encryption + access control + audit logs |
| DFSA / ADGM operational resilience | Logical isolation + backup + incident response |
| Professional secrecy (LB Bar, UAE Bar) | No cross-tenant access means client data never mingles |

## Related skills

- [[docs-security-overview]]
- [[docs-team-roles-permissions]]
- [[docs-sso-saml-setup]]
