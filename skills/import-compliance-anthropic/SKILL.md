---
name: import-compliance-anthropic
description: Use when migrating Anthropic-format compliance configuration data — safety rules, content policy rules, capability limits, behavioral guardrails, and usage policy settings — from an Anthropic API or the agent Console source into the Louis platform's compliance and safety configuration schema. Maps the source compliance shape to Louis's safety-compliance layer, with dry-run preview, conflict detection, and a mandatory human-review gate before any compliance rule is activated in production.
license: MIT
metadata: " id: import.compliance-anthropic category: import jurisdictions: [__multi__] priority: P3 intent: [__import__, migration, compliance, safety-rules, AI-policy] related: [import-canned-responses-anthropic, import-assignation-refere-communication-associe, import-assignation-refere-recouvrement-creance] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'import'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Import — Compliance Configuration (Anthropic Format)

## What it does

This import skill migrates compliance configuration data from an Anthropic-format source into the Louis platform's safety and compliance layer. "Compliance configuration" in this context refers to the structured set of behavioral rules, content-policy settings, capability constraints, and safety guardrails that govern how Louis responds to user inputs — what it will and will not do, and under what conditions.

This migration may be needed when:
- Updating from one Anthropic API version to another with a different compliance schema.
- Moving from a custom the agent API integration to the Louis-native skill framework.
- Consolidating compliance rules that were managed externally into Louis's internal compliance registry.

## What compliance configuration contains

Anthropic-format compliance data typically includes:

| Configuration type | Description |
|---|---|
| System prompt safety rules | Instructions embedded in system prompts about topics to avoid, required disclaimers, escalation behaviors |
| Content policy overrides | Topic-level permissions or restrictions (e.g., "allow detailed legal advice", "require jurisdiction disclaimer") |
| Capability limits | Restrictions on specific skills or output types (e.g., "do not generate actual legal opinions — only analysis") |
| Refusal patterns | Specific input patterns that should trigger refusal or re-routing |
| Disclaimer rules | Required disclaimers that must appear on specific output types |
| Jurisdiction-specific rules | Rules that apply only when a specific jurisdiction is active |
| User-tier rules | Rules that differ by user plan tier (consumer vs lawyer vs enterprise) |

## Data shape

### Source format (Anthropic-style)

```json
{
  "rule_id": "comp-uuid",
  "rule_type": "content_policy",
  "name": "Require jurisdiction disclaimer on legal advice",
  "trigger": {
    "output_type": "legal_advice",
    "jurisdictions": ["__all__"]
  },
  "action": {
    "type": "append_disclaimer",
    "disclaimer_text": "This analysis is for informational purposes and does not constitute legal advice. Consult a qualified lawyer for advice specific to your situation."
  },
  "priority": 100,
  "enabled": true,
  "version": "1.0"
}
```

### Target format (Louis compliance schema)

```json
{
  "id": "lc-uuid",
  "source_id": "comp-uuid",
  "type": "compliance-rule",
  "rule_type": "content_policy",
  "name": "Require jurisdiction disclaimer on legal advice",
  "trigger": {
    "output_type": "legal_advice",
    "jurisdictions": ["__all__"]
  },
  "action": {
    "type": "append_disclaimer",
    "disclaimer_text": "..."
  },
  "priority": 100,
  "status": "draft",
  "imported_at": "[timestamp]",
  "source_system": "anthropic-compliance",
  "review_required": true,
  "reviewed_by": null,
  "reviewed_at": null
}
```

## Import configuration

### Mapping rules

| Source field | Louis target field | Notes |
|---|---|---|
| `rule_id` | `source_id` | Preserve as provenance |
| `rule_type` | `rule_type` | Map to Louis rule type vocabulary |
| `name` | `name` | Copy verbatim |
| `trigger` | `trigger` | Map; verify trigger field names match Louis schema |
| `action` | `action` | Map; verify action types are supported in Louis |
| `priority` | `priority` | Copy verbatim; check for conflicts with existing Louis rules at same priority |
| `enabled` | `status` | Map: `enabled=true` → `status=draft` (not `active` — human review required) |
| `version` | `version` | Copy verbatim |

**Critical**: `enabled=true` in the source maps to `status=draft` in Louis — never to `status=active`. No compliance rule imported from an external system should be activated without explicit human review.

### Conflict detection

1. **Priority conflict**: if an imported rule has the same priority as an existing active Louis compliance rule, flag: "Priority conflict with [existing-rule-name]. Review before activating."
2. **Action type not supported**: if an action type in the source is not supported in the Louis compliance engine, flag: "Unsupported action type — manual implementation required."
3. **Trigger overlap**: if the imported rule's trigger overlaps with an existing rule, surface both rules for comparison to prevent contradictory compliance behavior.

### Dry-run preview

```
Compliance Import Dry Run — [timestamp]
Total rules in source: 12
Rules with no conflicts: 9
Rules with conflicts: 2
Rules with unsupported action types: 1

Details:
[1] "Require jurisdiction disclaimer" — No conflict → Will import as DRAFT
[2] "Restrict output to legal professionals" — Priority conflict with existing rule 'user-tier-gate' → Flag for review
[3] "Webhook on refusal" — Unsupported action type → Manual implementation required
...
```

## Post-import requirements

### Mandatory human-review gate

All imported compliance rules are created in `status=draft`. Before any imported compliance rule can be activated in production:

1. A qualified reviewer (Louis product team or compliance lead) must review the rule.
2. The reviewer must confirm: (a) the rule is consistent with Louis's current compliance policy, (b) the trigger conditions are correct, (c) the action is as intended, and (d) there are no unintended side effects.
3. The review must be recorded: `reviewed_by`, `reviewed_at`, `review_notes`.
4. Only after approval can the status change from `draft` to `active`.

**There is no automated path from import to production for compliance rules.**

### Testing in staging

Before activating any imported compliance rule in production, test it against the Louis golden test set in the staging environment. Compliance rule changes can have broad behavioral effects.

## Failure modes

- **Malformed source JSON**: log per-rule; skip malformed rules; continue; report in import summary.
- **Unknown rule type**: flag for manual classification; import with `rule_type = "unknown"` and `status = "review"`.
- **Missing required fields**: flag per rule; import as draft with missing fields noted for manual completion.
- **Duplicate import**: detect by `source_id`; skip already-imported rules; report skip count.

## Related skills

- [[import-canned-responses-anthropic]]
- [[import-assignation-refere-communication-associe]]
- [[import-assignation-refere-recouvrement-creance]]
