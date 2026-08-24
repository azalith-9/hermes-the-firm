---
name: docs-audit-log-export
description: Use when a user asks how to export, access, or configure audit logs from the legal AI platform, or when a compliance team needs to understand what the audit trail covers for regulatory or forensic purposes. This is a platform documentation skill covering audit log scope, export formats, retention configuration, SCIM compliance, and SIEM integration for enterprise deployments across all jurisdictions.
license: MIT
metadata: " id: docs.audit-log-export category: docs jurisdictions: [__multi__] priority: P2 intent: [__docs__, audit log, compliance, export, SIEM, forensics] related: [docs-enterprise-deployment, docs-data-residency-mena, docs-billing-and-credits] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'docs'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Audit Log Export

## What it does

The audit log export feature provides a timestamped, tamper-resistant record of every significant action taken on the platform. This is required for:

- **Regulatory compliance**: legal professional regulations in many MENA and EU jurisdictions require law firms and legal departments to maintain records of document access, client data handling, and system use.
- **Internal investigations**: if a data incident or unauthorized access event occurs, the audit trail is the starting point.
- **Client billing verification**: billable activity logs support time-entry substantiation and fee audits.
- **IT security and SOC reporting**: SIEM integration allows real-time anomaly detection.

## Scope — what is logged

Every audit entry includes: timestamp (UTC), user identity (email + user ID), action type, resource identifier, IP address, session token, and outcome (success / failure).

| Event category | Specific actions captured |
|---|---|
| Authentication | Login, logout, failed login, MFA challenge, session expiry, API key created/revoked |
| Document access | File opened, file downloaded, file shared, file deleted |
| Drafting and generation | Skill invoked, document generated, document exported |
| Matter management | Matter created, matter assigned, matter closed, client added |
| User management | User created, user role changed, user deactivated, invitation sent |
| Data export | Bulk export initiated, export delivered, export failed |
| Settings changes | Data residency changed, SSO configuration changed, API key permissions changed |
| Billing events | Subscription changed, credit purchased, invoice issued |

## Export formats

| Format | Use case |
|---|---|
| **JSON** | Machine-readable; structured for programmatic processing; suitable for import into SIEM, data warehouse, or custom compliance tooling |
| **CSV** | Human-readable in spreadsheet tools; suitable for manual review, compliance reports, invoice audits |
| **SIEM stream** | Real-time streaming export to SIEM tools (Splunk, Microsoft Sentinel, Elastic Security, Sumo Logic) via webhook or syslog. Configurable per-tenant. Requires enterprise plan. |

## Retention configuration

- **Default retention**: logs are retained for **12 months** on all plans.
- **Extended retention**: configurable up to **7 years** on enterprise plans (recommended for legal professional regulatory compliance in LB, UAE, KSA where client file retention obligations may extend to 7 years or more).
- Retention is configured per-tenant by the workspace administrator. Contact the platform administrator to change the retention period.
- Logs are immutable once written — they cannot be edited, deleted, or overwritten by users, including administrators.

## SCIM compliance

The platform supports **SCIM 2.0** (System for Cross-domain Identity Management) for:
- Automated user provisioning and deprovisioning from an IdP (identity provider: Okta, Azure AD, Google Workspace).
- Audit log events for SCIM-driven provisioning are captured and exported identically to manual provisioning events.
- SCIM integration requires enterprise plan and SSO configuration.

## How to export audit logs

### Admin portal export

1. Navigate to **Settings → Security & Compliance → Audit Logs**.
2. Filter by: date range, user, event category, outcome.
3. Click **Export** → select format (JSON or CSV).
4. Logs are delivered via secure download link valid for 24 hours.

### API export

```
GET /api/v1/audit-logs
Authorization: Bearer {api_key}
Query params: from_date, to_date, user_id, event_type, page, page_size
```

Returns a paginated JSON array. See [[docs-dev-hub-api-reference]] for full schema.

### SIEM streaming setup

1. Navigate to **Settings → Security & Compliance → SIEM Integration**.
2. Configure webhook URL and authentication token.
3. Select event categories to stream.
4. Test the connection.
5. Logs stream in real time with a maximum latency of 60 seconds.

## Permissions and access control

- **Workspace administrators** can export all logs for their workspace.
- **Compliance officers** (if the role is assigned): read-only access to audit logs without admin rights.
- **Regular users**: cannot access audit logs.
- API key used for audit log export should be scoped to read-only and should not be shared with application-level keys.

## Regulatory context

| Jurisdiction | Relevant obligation |
|---|---|
| UAE | Federal Decree-Law No. 45/2021 on Personal Data Protection requires documentation of processing activities; audit logs support Article 30 records-of-processing obligations |
| KSA | PDPL (SDAIA) requires records of data processing activities and security incident logs; 7-year retention recommended for financial/legal matters |
| Lebanon | Banking Secrecy Law (Law 3/1956) and Central Bank circulars require transaction records; applicable to legal matters involving financial institutions |
| EU | GDPR Article 30 (records of processing activities); Article 32 (security measures including logging); audit logs are directly relevant evidence in supervisory authority investigations |
| DIFC | DIFC Data Protection Law 2020, Articles 22–24 (security and records) |

## Related skills

- [[docs-enterprise-deployment]]
- [[docs-data-residency-mena]]
- [[docs-dev-hub-api-reference]]
- [[docs-billing-and-credits]]
