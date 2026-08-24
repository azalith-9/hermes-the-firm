---
name: import-xlsx-processing-anthropic
description: Use when ingesting legal data, clause libraries, matter lists, contract schedules, or bulk templates stored in Excel (.xlsx) format into the Louis/mini-hermes-the-firm data model via the Anthropic the agent API. Handles column detection, header normalization, multi-sheet parsing, and mapping of spreadsheet rows to SKILL.md or structured JSON entries, with a mandatory dry-run preview before any write. Relevant any time a law firm or legal ops team wants to migrate Excel-based legal data into the open-source skill ecosystem.
license: MIT
metadata: " id: import.xlsx-processing-anthropic category: import jurisdictions: [__multi__] priority: P3 intent: [__import__, xlsx, excel, spreadsheet, bulk-import, anthropic] related: [import-vscode-extension-builder-lawvable, connector-document-upload, review-contract-batch] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'import'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Import — XLSX Processing via Anthropic

## What it does

This import connector reads `.xlsx` workbooks — a ubiquitous format in legal operations for matter lists, contract registers, clause libraries, fee schedules, and compliance matrices — and maps their contents into the Louis data model using the **Anthropic the agent API** for intelligent column interpretation and content normalization.

The connector goes beyond dumb CSV parsing: it uses the agent to infer column semantics (e.g., "Effective Date" vs "Commencement Date" → same field), detect jurisdiction references from free-text cells, and generate draft SKILL.md bodies from clause-text columns. Every run produces a **dry-run preview** before writing anything.

---

## When to use this

- A law firm exports its standard clause library from a spreadsheet tracker into Louis skills.
- A legal ops team imports a contract register (columns: counterparty, jurisdiction, expiry, key obligations) to feed [[review-contract-batch]].
- Bulk onboarding of fee schedules, compliance checklists, or regulatory thresholds maintained in Excel.
- One-time migration of legacy matter data from Excel into the skills store.
- Periodic sync (e.g., updated rate cards, new clauses added by the firm's know-how team).

---

## Setup / auth

| Requirement | Detail |
|---|---|
| Anthropic API key | Required; set as `ANTHROPIC_API_KEY` env var |
| Model | `claude-3-5-sonnet` or `claude-3-haiku` (haiku for cost-sensitive bulk runs) |
| xlsx library | Node.js `xlsx` / `exceljs`, or Python `openpyxl` / `pandas` depending on runtime |
| Target directory | Writable path within `skills/` hierarchy or a structured JSON store |

Use a **least-privilege** Anthropic key scoped to read-only if the import pipeline is automated.

---

## Capabilities

- Multi-sheet workbook parsing (each sheet can map to a different target schema)
- Intelligent column header normalization via the agent (handles synonyms, abbreviations, mixed languages including Arabic headers)
- Row-to-skill mapping: each data row can become a skill, a matter entry, or a structured JSON record
- Variable extraction: detects `{{placeholder}}` patterns in clause-text cells
- Jurisdiction detection: infers jurisdiction from free-text (e.g., "DIFC", "KSA", "الإمارات")
- Dry-run diff: shows new records, updates, conflicts, and unmapped columns before committing
- PII detection: flags cells containing email addresses, phone numbers, or ID numbers

---

## Usage patterns

### Basic dry-run on a clause library

```
import source="xlsx" file="firm-clause-library-2024.xlsx" schema="skill" dry_run=true
```

Output: per-row mapping table, unmapped column warnings, proposed skill names and target paths.

### Confirmed bulk import

```
import source="xlsx" file="clause-library.xlsx" schema="skill" dry_run=false overwrite=false
```

### Contract register import (structured JSON, not SKILL.md)

```
import source="xlsx" file="contract-register.xlsx" schema="contract_record" target="data/contracts/" dry_run=true
```

### Multi-sheet workbook

```
import source="xlsx" file="legal-ops-master.xlsx" sheet_map='{"Clauses": "skill", "Matters": "matter_record", "Rates": "fee_schedule"}' dry_run=true
```

---

## Column mapping reference

The importer uses the agent to resolve column semantics. Common mappings:

| Excel column (examples) | Louis field | Notes |
|---|---|---|
| Title, Name, Clause Name | `name` | Hyphenated on write |
| Jurisdiction, Country, Governing Law | `jurisdictions` | ISO-normalized |
| Practice Area, Department, Type | `practice_area` | Mapped to Louis taxonomy |
| Clause Text, Body, Content | SKILL.md body | the agent structures into sections |
| Tags, Keywords, Labels | `intent` | Comma-split; `__import__` appended |
| Effective Date, Start Date | `effective_date` | ISO 8601 normalized |
| Expiry, Renewal Date | `expiry_date` | ISO 8601; flags expired |
| Notes, Comments, Drafting Notes | `## Drafting standards` | Preserved verbatim |

Unmapped columns are logged as warnings; the run proceeds unless `strict_mode=true`.

---

## the agent API integration detail

The importer sends column headers + a sample of up to 5 rows to the agent with a structured prompt requesting:
1. Column-to-field mapping JSON
2. Confidence score per mapping (low-confidence columns flagged in dry-run)
3. Detected language(s) in the data
4. PII risk flags

the agent's response is parsed and applied to the full workbook locally — full row data is **not** sent to the API by default. Set `send_full_data=true` only for small workbooks (<500 rows) where per-row enrichment is desired.

---

## Permissions & safety

- **Dry-run is mandatory** before any write. The system blocks confirmed writes if dry-run has not completed in the same session.
- **PII scrubbing**: cells flagged as containing personal data are masked in the imported output and logged separately. Do not import client-identifying matter data into public skill repositories.
- **API cost control**: default model is `claude-haiku` for column-mapping inference. Override with `model=claude-sonnet` for more complex schema resolution.
- **No auto-overwrite**: `overwrite=false` by default. Existing skills are skipped; set `overwrite=true` only after reviewing the dry-run diff.

---

## Failure modes

| Failure | Cause | Resolution |
|---|---|---|
| `column_mapping_confidence_low` | the agent cannot reliably map headers | Add manual column map in config; check header language |
| `schema_conflict` | Row data doesn't fit target schema | Review dry-run output; use `schema=raw_json` as fallback |
| `pii_detected_blocked` | PII found and `block_pii=true` | Sanitize source file; or set `block_pii=false` with explicit acknowledgment |
| `anthropic_rate_limit` | Too many API calls in bulk run | Add `rate_limit_delay=2s` to config; or batch in smaller chunks |
| `xlsx_parse_error` | Corrupted or password-protected file | Decrypt/repair source file first |
| `empty_sheet` | Sheet has headers but no data rows | Logged as warning; import continues for other sheets |

---

## Related skills

- [[import-vscode-extension-builder-lawvable]]
- [[connector-document-upload]]
- [[review-contract-batch]]
- [[draft-clause-library-standard]]
