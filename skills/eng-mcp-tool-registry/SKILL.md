---
name: eng-mcp-tool-registry
description: Use when designing, implementing, or maintaining the MCP (Model Context Protocol) tool registry for a legal AI product. Defines how tools are registered, described, scoped, versioned, and discovered by the skill router; covers the tool schema, permission model, legal-product-specific safety constraints, and failure handling. Engineering skill foundational to all skill-to-tool integrations in the eFirm and other suites.
license: MIT
metadata: " id: eng.MCP-tool-registry category: eng jurisdictions: [__multi__] priority: P2 intent: [MCP, tool-registry, tool-use, function-calling, orchestration] related: - eng-audit-log-schema - eng-feature-flag-rollout-skills - eng-fallback-model-cascade - eng-latency-slo-by-skill source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'eng'.
Namespaced as louis-<category>-<skill> on registration.
-->


# MCP Tool Registry

## What it does

The MCP (Model Context Protocol) tool registry is the catalog of all external tools — APIs, databases, document systems, calendar integrations — that skills can invoke when responding to a user request. The registry:

1. **Defines each tool**: name, description, input/output schema, required permissions, rate limits, latency SLO.
2. **Controls tool discovery**: the router loads only the tools relevant to the active skill, preventing the model from attempting to use unavailable tools.
3. **Enforces permissions**: a skill operating in a user's session cannot invoke tools that exceed the user's authorization level.
4. **Provides a kill-switch**: any tool can be disabled registry-wide without code deployment.
5. **Tracks usage**: tool invocations are logged to the audit log ([[eng-audit-log-schema]]) with the same rigor as LLM calls.

In a legal AI product, tool calls that touch client data, billing systems, or conflict databases have significant consequences — a mis-invoked tool could create an unauthorized record, expose privileged data, or trigger a billing action. The registry is the governance layer that prevents this.

## Tool record schema

```json
{
  "tool_id": "efirm.matter-db.create-matter",
  "name": "create_matter",
  "description": "Create a new matter record in the eFirm database. Only call this after conflict check is CLEAN and engagement letter is drafted. Required fields: client_id, matter_type, responsible_partner_id, fee_structure.",
  "category": "efirm",
  "version": "1.2",
  "enabled": true,
  "kill_switch": false,
  "input_schema": {
    "type": "object",
    "required": ["client_id", "matter_type", "responsible_partner_id", "fee_structure"],
    "properties": {
      "client_id": {"type": "string", "description": "eFirm client UUID"},
      "matter_type": {"type": "string", "enum": ["corporate", "dispute", "ip", "employment", "regulatory", "personal"]},
      "responsible_partner_id": {"type": "string"},
      "fee_structure": {"type": "string", "enum": ["hourly", "fixed", "contingency", "hybrid"]},
      "description": {"type": "string", "maxLength": 500},
      "confidentiality_level": {"type": "string", "enum": ["standard", "enhanced", "privileged-only"], "default": "standard"}
    }
  },
  "output_schema": {
    "type": "object",
    "properties": {
      "matter_id": {"type": "string"},
      "matter_number": {"type": "string"},
      "status": {"type": "string"},
      "created_at": {"type": "string", "format": "date-time"}
    }
  },
  "permissions_required": ["matter:create"],
  "org_scoped": true,
  "rate_limit": {"requests_per_minute": 10},
  "latency_slo_ms": 2000,
  "idempotency_key": "client_id + matter_type + description_hash",
  "side_effects": ["creates database record", "triggers audit log", "sends partner notification"],
  "rollback_support": false,
  "legal_safety_notes": "Verify conflict check is complete before calling. This creates a matter record that triggers billing setup."
}
```

## Tool categories in the legal AI product

| Category prefix | Tools included |
|---|---|
| `efirm.*` | eFirm database operations (create/read/update matter, client, document) |
| `efirm-finance.*` | Billing system reads (WIP, invoices, realization) — read-only by default |
| `calendar.*` | Deadline calendar integrations (Google Calendar, Outlook) |
| `dms.*` | Document management system (create folder, upload, search) |
| `esign.*` | E-signature platforms (DocuSign, Tawqi3i — initiate signature request) |
| `screening.*` | Sanctions and PEP screening APIs |
| `search.*` | Web and legal database search (read-only) |
| `email.*` | Draft and send client communications |
| `comms.*` | Internal team notifications |

## Skill-to-tool binding

Skills declare which tools they are permitted to invoke. The router loads only those tools for the skill's session:

```yaml
skill: efirm-matter-creation-flow
permitted_tools:
  - efirm.client-db.lookup-client
  - efirm.client-db.create-client
  - efirm.conflict-check.run
  - efirm.matter-db.create-matter
  - efirm.engagement-letter.draft
  - screening.sanctions.check
  - calendar.deadline.create
```

A skill not listed as permitted cannot call `efirm.matter-db.delete-matter` even if the model attempts to. The tool registry enforces this at the gateway level, not just at the prompt level.

## Permission model

Tools require permissions that are checked against the session user's role:

| Permission | Minimum role |
|---|---|
| `matter:read` | Associate |
| `matter:create` | Associate (with partner approval gate) |
| `matter:delete` | Partner |
| `client:read` | Associate |
| `client:create` | Associate |
| `billing:read` | Associate |
| `billing:write` | Finance staff, Partner |
| `trust-account:read` | Finance staff, Partner |
| `trust-account:write` | Finance staff with dual-sign |
| `admin:*` | Admin only |

Tools with write-side-effects on client money or matter status require the calling skill to verify that prerequisites are met (e.g., conflict check complete) before the tool call is allowed.

## Safety constraints specific to legal products

The following tool behaviors are **prohibited** by the registry, regardless of model instructions:

1. **No direct client-fund transfers**: the registry contains no tool that moves money between accounts. Fund movements are human-initiated, with multi-party approval.
2. **No deletion of privileged documents without dual approval**: a `dms.document.delete` call requires two separate authorizations (log entries from two different authorized users).
3. **No external transmission of privileged content without explicit user action**: `email.send` and `esign.initiate` are blocked from being invoked autonomously by the model — they require a human-confirmed action event in the session.
4. **No trust-account writes without finance-role session**: the session must have an authenticated finance-role user, not just a general user token.
5. **No screening bypass**: `screening.sanctions.check` is always called before `efirm.client-db.create-client` — the registry enforces this ordering via a prerequisite check.

## Tool failure handling

| Failure type | Behavior |
|---|---|
| Tool unavailable (503) | Return structured error to skill; skill informs user gracefully |
| Tool timeout | Retry once after 2s; if still timeout, return error with `retry_after` hint |
| Permission denied | Return specific permission error; skill explains what the user needs to do |
| Validation error (input) | Return schema validation details; skill prompts user to supply missing fields |
| Rate limit | Return 429 with `retry_after`; skill queues the operation |
| Idempotency replay | Return the original result (do not re-execute) |

The skill must never surface raw tool error codes to the end user. Always translate to professional, context-appropriate language.

## Versioning

Tools are versioned independently of skills:
- Breaking changes to a tool input schema → new `tool_id` version suffix (e.g., `efirm.matter-db.create-matter:v2`).
- Backward-compatible changes → same ID, bump `version` field.
- Deprecated tool IDs remain in the registry with `enabled: false` until all skills referencing them are updated.
- Skills specify the tool ID they depend on; the registry resolves to the latest compatible version.

## Audit logging

Every tool invocation is logged to the audit log ([[eng-audit-log-schema]]) with:
- `event_type: tool.invoked`
- `tool_id` and `tool_version`
- `skill_id` and `skill_version` (the calling skill)
- Input parameters (sanitized — exclude any PII or privileged content from log if configured)
- Output summary
- Result: success / failure / partial
- Latency

## Related skills

- [[eng-audit-log-schema]]
- [[eng-feature-flag-rollout-skills]]
- [[eng-fallback-model-cascade]]
- [[eng-latency-slo-by-skill]]
