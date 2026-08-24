---
name: eng-audit-log-schema
description: Use when designing or reviewing the audit log schema for a legal AI product. Defines the canonical event record structure, required fields for legal-product compliance (attorney-client privilege considerations, regulatory retention rules, tamper-evidence), indexing strategy, retention policies, and the specific event types that must be logged in a law-firm or legal-AI context. Engineering skill — no practice-area jurisdictional notes.
license: MIT
metadata: " id: eng.audit-log-schema category: eng jurisdictions: [__multi__] priority: P2 intent: [audit-log, schema, compliance, tamper-evidence, retention, observability] related: - eng-langfuse-trace-inspector - eng-latency-slo-by-skill - eng-cost-per-message-tracker - eng-mcp-tool-registry source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'eng'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Audit Log Schema

## What it does

The audit log is the system of record for every meaningful event in the legal AI platform. It answers: who did what, to what, when, from where, and with what result. In a legal product, the audit log serves dual purposes: operational observability and legal/regulatory accountability.

Specifically, the audit log must be able to answer:
- "Did the AI access this client's documents before the conflict check was complete?"
- "What version of skill X was used when the AI generated this engagement letter?"
- "Who approved the deletion of matter Y's data, and when?"
- "Was the user's session authenticated before they queried a privileged document?"

## Canonical event record

Every audit log entry is a single JSON object:

```json
{
  "event_id": "ulid or uuid-v7",
  "event_type": "skill.invoked | user.auth | document.accessed | matter.created | ...",
  "timestamp": "2025-05-14T09:31:42.123Z",
  "timestamp_local": "2025-05-14T12:31:42.123+03:00",
  "actor": {
    "user_id": "usr_abc123",
    "role": "associate | partner | admin | system",
    "session_id": "sess_xyz789",
    "ip_address": "203.0.113.42",
    "user_agent": "..."
  },
  "resource": {
    "type": "matter | document | skill | tool | session | user | org",
    "id": "matter_2025-UAE-0147",
    "name": "Al Baraka SPA"
  },
  "action": {
    "name": "read | create | update | delete | invoke | approve | reject | transmit",
    "detail": "Skill efirm-conflict-check invoked for new matter",
    "result": "success | failure | partial",
    "error_code": null,
    "error_message": null
  },
  "context": {
    "skill_id": "efirm-conflict-check",
    "skill_version": "1.0",
    "model_id": "claude-sonnet-4-6",
    "trace_id": "langfuse-trace-id",
    "request_id": "req_abc123"
  },
  "metadata": {
    "org_id": "org_haqq",
    "workspace_id": "ws_default",
    "environment": "production | staging"
  },
  "integrity": {
    "prev_hash": "sha256-of-previous-entry",
    "entry_hash": "sha256-of-this-entry"
  }
}
```

## Required fields (no nullable)

| Field | Type | Purpose |
|---|---|---|
| `event_id` | ULID or UUIDv7 | Monotonic ordering + uniqueness |
| `event_type` | enum string | Fast filtering and alerting |
| `timestamp` | ISO 8601 UTC | Canonical time reference |
| `actor.user_id` | string | Who acted; "system" for automated events |
| `actor.role` | enum | Authorization context |
| `actor.session_id` | string | Links to authentication record |
| `resource.type` | enum | What was acted upon |
| `resource.id` | string | Specific resource identifier |
| `action.name` | enum | What happened |
| `action.result` | enum | Success / failure / partial |
| `context.request_id` | string | Links to request log |

## Event type taxonomy

### Authentication events
- `user.auth.login.success`
- `user.auth.login.failure`
- `user.auth.logout`
- `user.auth.token.refresh`
- `user.auth.mfa.success`
- `user.auth.mfa.failure`

### Matter and document events
- `matter.created`
- `matter.status.changed`
- `matter.accessed`
- `document.created`
- `document.accessed`
- `document.transmitted` (to external party — high importance)
- `document.deleted`
- `document.version.created`

### Skill invocation events
- `skill.invoked`
- `skill.completed`
- `skill.failed`
- `skill.escalated` (skill routed to human review)

### Conflict and compliance events
- `conflict.check.run`
- `conflict.check.result.clean`
- `conflict.check.result.concern`
- `conflict.check.result.conflict`
- `aml.screening.run`
- `aml.flag.raised`

### Data events
- `data.export.requested`
- `data.export.delivered`
- `data.deletion.requested`
- `data.deletion.completed`

### Admin events
- `user.created`
- `user.role.changed`
- `user.access.granted`
- `user.access.revoked`
- `org.settings.changed`

## Tamper-evidence (chained hashes)

For regulatory and malpractice defensibility, the audit log must be tamper-evident:

1. Compute `entry_hash = SHA256(event_id + event_type + timestamp + actor + resource + action + prev_hash)`.
2. Each entry's `prev_hash` is the `entry_hash` of the immediately preceding entry.
3. Any insertion, deletion, or modification breaks the hash chain.
4. Periodically anchor the chain head to an external timestamp authority (e.g., RFC 3161 timestamp token) for legal evidentiary strength.

## Indexing strategy

| Index | Purpose |
|---|---|
| `(org_id, timestamp)` | Org-scoped time-range queries |
| `(actor.user_id, timestamp)` | User activity history |
| `(resource.id, timestamp)` | Resource event history |
| `(event_type, timestamp)` | Alert and monitoring queries |
| `(context.trace_id)` | Cross-service trace correlation |
| `(action.result, event_type, timestamp)` | Failure analysis |

Use a write-optimized append-only store (e.g., ClickHouse, BigQuery, S3+Athena, or a dedicated audit table in PostgreSQL with `UNLOGGED` disabled and row-level security). Do not use the same database table as application data.

## Retention policy

| Event category | Minimum retention | Rationale |
|---|---|---|
| Authentication | 1 year | Security investigation |
| Matter / document access | 7 years | Bar file retention; malpractice | 
| Conflict check | 7 years | Bar discipline defense |
| Skill invocations | 2 years | Operational; AI accountability |
| Financial events (billing, invoices) | 7 years | Tax and audit |
| Data deletion events | Permanent | Proof of compliance |

Retention may be extended by firm policy or jurisdiction-specific requirements.

## Access control

- The audit log is readable by: system admins, managing partner (org-level), compliance officer.
- Individual users can read their own events only.
- No user — including admins — can delete or update audit log entries.
- Write access: system only (no user-facing write endpoint).

## Related skills

- [[eng-langfuse-trace-inspector]]
- [[eng-latency-slo-by-skill]]
- [[eng-cost-per-message-tracker]]
- [[eng-mcp-tool-registry]]
