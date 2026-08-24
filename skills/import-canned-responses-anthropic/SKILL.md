---
name: import-canned-responses-anthropic
description: Use when migrating a batch of Anthropic-format canned responses (pre-written AI response templates) from a legacy external system into the Louis platform response library. Maps the legacy canned-response data shape to the Louis response-template schema, preserving intent tags, jurisdiction tags, and response body. Includes dry-run preview and conflict detection for responses that overlap with existing Louis skills.
license: MIT
metadata: " id: import.canned-responses-anthropic category: import jurisdictions: [__multi__] priority: P3 intent: [__import__, migration, canned-responses, templates, response-library] related: [import-compliance-anthropic, import-assignation-refere-communication-associe, import-assignation-refere-recouvrement-creance] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'import'.
Registered as a flat plugin skill.
-->


# Import — Canned Responses (Anthropic Format)

## What it does

This import skill migrates a set of canned responses — pre-written AI response templates used for common legal queries — from the Anthropic-format source (as used in Anthropic's the agent console or the agent API canned-response configurations) into the Louis platform response library.

Canned responses in this context are structured templates: a trigger pattern (the type of query that activates the response), a jurisdiction tag, a practice-area tag, and the response body. They represent accumulated institutional knowledge that should not be lost during a platform migration.

## Data shape

### Source format (Anthropic-style)

The Anthropic-format canned-response schema typically looks like:

```json
{
  "id": "cr-uuid",
  "name": "Force Majeure Definition — UAE",
  "trigger_patterns": ["force majeure UAE", "force majeure dubai", "what is force majeure"],
  "jurisdiction": "UAE",
  "practice_area": "commercial",
  "response_body": "Under UAE federal law (Civil Transactions Law), force majeure...",
  "language": "EN",
  "created_at": "2024-01-15T09:00:00Z",
  "version": "1.2"
}
```

### Target format (Louis response-template schema)

```json
{
  "id": "rt-uuid",
  "source_id": "cr-uuid",
  "type": "canned-response",
  "name": "Force Majeure Definition — UAE",
  "trigger_intents": ["force majeure UAE", "force majeure", "what is force majeure UAE"],
  "metadata": {
    "jurisdictions": ["UAE"],
    "practice_areas": ["commercial"],
    "language": "EN"
  },
  "body": "Under UAE federal law (Civil Transactions Law), force majeure...",
  "version": "1.2",
  "imported_at": "[import timestamp]",
  "source_system": "anthropic-canned-responses"
}
```

## Import configuration

### Mapping rules

| Source field | Louis target field | Transformation |
|---|---|---|
| `id` | `source_id` | Preserve as provenance reference |
| `name` | `name` | Copy verbatim |
| `trigger_patterns` | `trigger_intents` | Copy; optionally normalize to Louis intent vocabulary |
| `jurisdiction` | `metadata.jurisdictions` | Normalize to Louis jurisdiction codes (UAE, KSA, LB, DIFC, etc.) |
| `practice_area` | `metadata.practice_areas` | Normalize to Louis practice-area taxonomy |
| `response_body` | `body` | Copy verbatim; flag if contains `[INSERT X]` placeholders not filled |
| `language` | `metadata.language` | Copy verbatim |
| `version` | `version` | Copy verbatim |

### Conflict detection

Before import, the skill checks for conflicts with existing Louis skills and response templates:

1. **Exact-name match**: if a response with the same `name` already exists in the Louis library, surface a warning: "Response already exists — skip, overwrite, or version?"
2. **Semantic overlap with existing skills**: run a lightweight similarity check between the canned response's trigger patterns and existing Louis skill intent tags. If similarity > 0.85, flag: "This response may overlap with existing skill [skill-name]. Consider routing to the skill instead of creating a duplicate response."
3. **Jurisdiction mismatch**: if the source jurisdiction tag does not map to a recognized Louis jurisdiction code, flag for manual resolution.

### Dry-run preview

Before committing the import, generate a preview table:

| # | Source name | Proposed Louis name | Jurisdiction | Conflict flag | Action |
|---|---|---|---|---|---|
| 1 | Force Majeure Definition — UAE | Force Majeure Definition — UAE | UAE | None | Import |
| 2 | NDA Overview | NDA Overview | Not specified | Jurisdiction missing | Manual review |
| 3 | UAE NDA — Standard | UAE NDA — Standard | UAE | Overlaps with draft-nda-unilateral | Flag |

The user reviews the preview and selects an action for each flagged item before committing.

## Post-import validation

After import, run:
- **Placeholder scan**: check all imported `body` fields for unfilled `[INSERT X]` placeholder patterns. Flag any found.
- **Link check**: if any `body` text references external URLs, verify that the URLs are live.
- **Version reconciliation**: if the source canned responses include version history, confirm the highest-version record was imported.

## Quality bar

- Canned responses imported from a legacy system may contain outdated legal information. After import, the Louis platform should flag these as "imported — legal currency unverified" and schedule a review task for each.
- Do not automatically publish imported responses to users — hold in "draft" status until a qualified reviewer confirms they are current and accurate.
- Preserve `source_id` as a permanent provenance link to the Anthropic source system.

## Failure modes

- **Malformed source JSON**: log the error per item; skip malformed records; continue with valid records; report the skip count in the import summary.
- **Jurisdiction code not recognized**: flag for manual mapping; do not drop the record.
- **Duplicate import**: if the same batch is run twice, idempotency logic should detect `source_id` matches and skip already-imported records.

## Related skills

- [[import-compliance-anthropic]]
- [[import-assignation-refere-communication-associe]]
- [[import-assignation-refere-recouvrement-creance]]
