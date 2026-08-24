---
name: ref-mcp-hardening
description: Use as a reference guide for hardening the Model Context Protocol (MCP) layer of a legal AI deployment — covering OAuth scope minimization, write-action approval gates, per-tool capability scopes, audit logging, rate limiting, and tenant isolation. Applies to any deployment of Louis or similar legal AI where MCP tools connect the AI to external systems (document management, calendaring, CRM, court filing systems). Critical for firms handling privileged and confidential information.
license: MIT
metadata: " id: ref.mcp-hardening category: ref priority: P1 intent: [__ref__, mcp, security, hardening, legal-ai-ops] related: - ref-privilege-layers - ref-anti-patterns - ref-setup-checklist - ref-skill-authoring source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'ref'.
Registered as a flat plugin skill.
-->


# Reference — MCP Hardening for Legal AI

## Scope

The Model Context Protocol (MCP) is the protocol layer that allows a legal AI assistant to connect to external tools and data sources — document management systems (NetDocuments, iManage), calendaring, conflict-check databases, court filing systems, CRM, billing platforms, and custom firm APIs. In a legal context, MCP tools handle privileged, confidential, and often regulated data. The MCP layer must be hardened to prevent unauthorized access, accidental data leakage, and privilege waiver.

This reference covers the six key hardening areas for MCP in a legal AI deployment.

---

## 1. OAuth grants — narrow and auditable

**Principle:** Every MCP tool that requires OAuth authorization must be granted the minimum scope necessary to perform its function. Broad "read/write all" OAuth grants are incompatible with legal AI deployments.

**Implementation:**
- Define scope per tool, not per user or per session: a "calendar lookup" tool gets `calendar:read`; a "document create" tool gets `documents:write` for a specific workspace only
- OAuth grants must be logged: every grant, revocation, and scope change is recorded with timestamp, user, and justification
- OAuth tokens must have expiry: no permanent tokens; enforce refresh cycles (maximum 24 hours for write-capable tokens; 7 days for read-only)
- Scope review: quarterly audit of all active OAuth grants; revoke unused grants

**Legal-specific requirement:** Tools accessing privileged communications (attorney-client, work product) must be separately scoped and access-controlled, separate from tools accessing non-privileged content.

---

## 2. Write actions — default to "requires approval"

**Principle:** Any MCP tool action that modifies data, sends communications, files documents, or creates records must be set to "requires approval" by default. Write actions are one-way; mistakes can be extremely difficult or impossible to reverse (particularly for court filings).

**Implementation:**
- All MCP tool actions are classified as `READ` or `WRITE` at tool registration time
- WRITE actions are blocked by default; the AI must request approval from an authorized user before executing
- Approval must be explicit (a positive action, not just absence of objection): click a "Confirm" button; type "approve"; use a second-factor confirmation for high-stakes actions
- List of always-blocked WRITE actions (no approval can unlock these):
  - Sending emails to parties not listed in the active matter
  - Filing court documents (must be done by a human lawyer)
  - Deleting or overwriting original documents
  - Creating payments or billing entries above a set threshold

**Exception:** Routine low-risk writes (saving a draft internally, creating a calendar reminder for the authorized user) may have a lower approval threshold; define these in the firm's MCP policy.

---

## 3. Per-tool capability scopes

**Principle:** Each MCP tool has an explicit capability scope defined at registration — a list of exactly what the tool can and cannot do. The AI model does not have the ability to expand a tool's scope at runtime.

**Implementation:**
| Tool | Permitted capabilities | Blocked capabilities |
|---|---|---|
| `document_search` | Search by keyword, date, matter; return document list | Open, edit, or delete documents |
| `document_read` | Read document content for authorized matters | Access documents outside the authorized matter list |
| `calendar_lookup` | Read availability and scheduled events | Create, modify, or cancel events |
| `conflict_check` | Query conflict database | Modify conflict records |
| `matter_notes` | Create and read notes on an authorized matter | Modify or delete notes authored by others |
| `billing_lookup` | Read current billing entries for a matter | Create, edit, or write off billing entries |

- Capability scope is defined in the tool registration manifest (JSON)
- Any attempt by the AI to use a tool in a way not covered by its registered scope is rejected at the MCP layer with an error log entry
- Scope changes require approval from the firm's CISO and General Counsel

---

## 4. Audit logs for all MCP actions

**Principle:** Every MCP tool call — successful or not — is logged with sufficient detail to reconstruct what happened and who caused it.

**Required log fields per MCP action:**
- Timestamp (ISO 8601)
- User or session ID
- Tool name and version
- Action type (READ / WRITE)
- Input parameters (redacted for any PII / privileged content — log metadata, not content)
- Output status (success / error / approval pending)
- Approval record (if a WRITE action: who approved, when)
- Matter reference (if the action was matter-specific)

**Retention:** Audit logs retained for [7 years] or the applicable limitation period for professional liability claims (longer of the two).

**Review:** Automated anomaly detection on audit logs; human review of anomalies within 24 hours; quarterly audit log review by CISO.

**Privilege:** Audit logs may themselves be subject to privilege or professional confidentiality obligations; store them in the same privileged infrastructure as client data.

---

## 5. Rate limiting per tool

**Principle:** Each MCP tool must have a rate limit that prevents both accidental loops and deliberate abuse.

**Default rate limits:**
| Tool category | Rate limit (requests per minute) | Hard ceiling (requests per hour) |
|---|---|---|
| Document search | 30 | 300 |
| Document read | 20 | 200 |
| Conflict check | 10 | 100 |
| Calendar lookup | 15 | 150 |
| Any WRITE action | 5 | 20 |

- Rate limit breaches are logged and alert the CISO
- Rate limits can be adjusted per firm policy; they should be set as low as the typical workflow requires, not as high as the system technically allows
- Hard ceilings (hourly) prevent runaway agent loops from consuming all available API credits or overwhelming connected systems

---

## 6. Tenant isolation at the MCP layer

**Principle:** In a multi-tenant legal AI deployment, each firm (tenant) can only access its own data, tools, and configurations. Cross-tenant access is architecturally impossible, not merely policy-prohibited.

**Implementation:**
- Tenant ID is injected at the MCP gateway level and cannot be overridden by the AI model or by user input
- All database queries are scoped to the tenant's namespace before execution
- MCP tools are registered per tenant; a tool registered for Firm A cannot be invoked by Firm B's session even if the tool name is the same
- Document storage is segregated: Firm A cannot access Firm B's document namespace
- Secrets (API keys, OAuth tokens) are stored in a per-tenant secrets vault; cross-tenant secret access is blocked at the vault level

**Testing:** Annual penetration test specifically targeting tenant isolation; any finding of cross-tenant data access is treated as a critical security incident requiring immediate disclosure to affected tenants and (where required) regulatory notification.

---

## Quick reference — MCP hardening checklist

Before deploying a legal AI with MCP tool access:

- [ ] All MCP tools have explicit capability scope definitions (READ vs WRITE)
- [ ] WRITE actions default to "requires approval"
- [ ] OAuth grants are scoped to minimum necessary permissions
- [ ] OAuth tokens have expiry enforced
- [ ] Audit logging is enabled for all tool calls
- [ ] Rate limits are configured per tool
- [ ] Tenant isolation is implemented and tested
- [ ] Privileged-content tools are separately scoped and access-controlled
- [ ] List of always-blocked actions is defined and enforced
- [ ] Quarterly audit log review is scheduled

---

## Related skills

- [[ref-privilege-layers]]
- [[ref-anti-patterns]]
- [[ref-setup-checklist]]
- [[ref-skill-authoring]]
