---
name: import-vscode-extension-builder-lawvable
description: Use when ingesting legal content, skills, or document templates originally authored inside the Lawvable VS Code extension into the Louis/mini-hermes-the-firm data model. Handles mapping of Lawvable's proprietary document-builder schema into standard SKILL.md and draft formats, with config-driven field mapping and a mandatory dry-run preview before any write. Relevant any time a legal practitioner wishes to migrate Lawvable-built clause libraries, templates, or playbooks into the open-source skill ecosystem.
license: MIT
metadata: " id: import.vscode-extension-builder-lawvable category: import jurisdictions: [__multi__] priority: P3 intent: [__import__, migration, vscode, lawvable, template-ingestion] related: [import-xlsx-processing-anthropic, connector-vscode-extension, draft-nda-unilateral] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'import'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Import — VS Code Extension Builder (Lawvable)

## What it does

This import connector translates content produced by the **Lawvable VS Code extension** — a legal document builder that lets lawyers assemble clause libraries and templates directly inside VS Code — into the standard data model used by Louis and `mini-hermes-the-firm`.

The connector performs schema mapping (Lawvable's JSON/XML shapes → SKILL.md frontmatter + body), field normalization, and writes enriched skill files to the target directory. Every import runs in two phases: **config validation + dry-run preview**, then an optional **confirmed write**.

---

## When to use this

- A law firm or legal-tech team has built a clause library in the Lawvable extension and wants to make those clauses available as first-class Louis skills.
- A practitioner is migrating from Lawvable to the open-source mini-hermes-the-firm ecosystem.
- Bulk onboarding of existing Lawvable templates during platform integration.
- Periodic sync of updated Lawvable templates back into the skills store.

---

## Setup / auth

| Requirement | Detail |
|---|---|
| Lawvable extension installed | VS Code 1.82+ with Lawvable extension active |
| Export format | Lawvable export bundle (`.lawvable.zip` or folder) |
| Target directory | Writable path within `skills/` hierarchy |
| Louis API key (optional) | Required only if writing directly to hosted Louis instance |

No OAuth is needed for local file-based imports. For hosted deployments, use a scoped import API key — never a full admin credential.

---

## Capabilities

- Parse Lawvable's document-builder JSON schema (`clauses[]`, `variables[]`, `metadata{}`)
- Map Lawvable clause types to Louis skill categories (e.g., Lawvable `ClauseType.NDA` → category `draft`)
- Extract frontmatter fields: `name`, `jurisdictions`, `practice_area`, `intent` tags
- Normalize variable placeholders (`{{variable}}` → Louis input schema)
- Preserve clause commentary and drafting notes as `## Drafting standards` body sections
- Generate dry-run diff showing: new skills to be created, existing skills to be updated, conflicts requiring manual resolution

---

## Usage patterns

### Basic dry-run

```
import source="lawvable" path="/exports/firm-clause-library" dry_run=true
```

Output: table of detected skills, proposed target paths, field-mapping warnings.

### Confirmed import

```
import source="lawvable" path="/exports/firm-clause-library" dry_run=false overwrite=false
```

`overwrite=false` (default): skip any target file that already exists — safe for incremental syncs.  
`overwrite=true`: replace existing skills — use only after reviewing dry-run output.

### Selective import (single template)

```
import source="lawvable" file="NDA-standard-KSA.json" target="skills/draft/draft-nda-ksa/"
```

---

## Field mapping reference

| Lawvable field | Louis SKILL.md field | Notes |
|---|---|---|
| `metadata.title` | `name` | Lowercased, hyphenated |
| `metadata.jurisdiction[]` | `jurisdictions` | ISO codes normalized |
| `metadata.practiceArea` | `practice_area` | Mapped to Louis taxonomy |
| `metadata.tags[]` | `intent` | Preserved as-is; `__import__` always appended |
| `clauses[].body` | SKILL.md body sections | Mapped by clause type |
| `variables[].name` | `## Required inputs` entries | Type + default extracted |
| `metadata.version` | `version` | Preserved verbatim |

---

## Permissions & safety

- **Dry-run is mandatory** before any write operation. The system will refuse a confirmed write if dry-run has not been executed in the same session.
- **Never overwrite** production skills without explicit `overwrite=true` and dry-run review.
- **PII scrubbing**: if any Lawvable template contains example client data (names, addresses, matter numbers), the importer flags and strips these before writing.
- **No network calls** during import unless explicitly configured for hosted-Louis sync.
- Import runs under the calling user's file-system permissions — do not run as root.

---

## Failure modes

| Failure | Cause | Resolution |
|---|---|---|
| `schema_parse_error` | Lawvable export format changed | Update schema adapter; check Lawvable release notes |
| `jurisdiction_unmapped` | Lawvable uses non-standard jurisdiction code | Add manual mapping in import config |
| `duplicate_skill_conflict` | Target path already exists | Use dry-run to review, then set `overwrite=true` if intentional |
| `variable_type_unknown` | Lawvable variable type not in Louis taxonomy | Defaults to `string`; add to type registry if recurring |
| `body_too_short` | Lawvable clause has no body text | Skill is flagged as stub; manual enrichment required |

---

## Related skills

- [[import-xlsx-processing-anthropic]]
- [[connector-vscode-extension]]
- [[draft-nda-unilateral]]
- [[draft-employment-contract]]
