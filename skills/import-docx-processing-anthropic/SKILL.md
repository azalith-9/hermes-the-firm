---
name: import-docx-processing-anthropic
description: Use when importing a DOCX document-processing skill originally authored for the Anthropic the agent API into the mini-hermes-the-firm skill format. The adapter handles extraction of text, tables, tracked changes, and metadata from Word documents, mapping the legacy Anthropic processing configuration to the standard skill model with a dry-run preview before committing.
license: MIT
metadata: " id: import.docx-processing-anthropic category: import jurisdictions: [__multi__] priority: P3 intent: [__import__, docx, document-processing, migration, anthropic] related: [import-pdf-processing-anthropic, import-pptx-processing-anthropic, import-contract-review-anthropic, multimodal-document-ingestion] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'import'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Import: DOCX Processing (Anthropic)

## What it does

This import adapter migrates a **DOCX document-processing skill** originally built for Anthropic's the agent API into the `mini-hermes-the-firm` standard format. Legal teams working with Microsoft Word documents — contracts, briefs, pleadings, board resolutions, regulatory submissions — rely on reliable DOCX ingestion as a prerequisite for all downstream review and analysis skills.

The adapter normalises how the agent reads `.docx` files: extracting body text, table content, header/footer metadata, comments, revision marks (tracked changes), and document properties, then feeding them as structured context into whichever downstream skill (contract review, NDA triage, risk assessment) was originally wired to the Anthropic API.

## Import config

| Field | Source mapping | Default if absent |
|---|---|---|
| `extraction_mode` | Legacy `mode` or `extraction` field | `full_text` |
| `tables` | Legacy `include_tables` boolean | `true` |
| `tracked_changes` | Legacy `track_changes` or `revision_marks` | `accept_all` |
| `metadata_fields` | Legacy `doc_properties` array | `[author, created, modified, title]` |
| `language` | Legacy `lang` | `auto-detect` |
| `output_format` | Legacy `format` | `markdown` |
| `chunk_size` | Legacy `chunk_tokens` | `2000` tokens per chunk |
| `overlap` | Legacy `overlap_tokens` | `200` tokens |

## Dry-run preview

```
IMPORT PREVIEW — docx-processing-anthropic
Source shape : Anthropic DOCX extraction config
Extraction   : full_text + tables
Track changes: accept_all (hidden; use 'show' to surface redlines)
Metadata     : author, created, modified, title
Output       : markdown with table serialisation
Chunk size   : 2000 tokens / 200 overlap
```

Confirm before the adapted skill is written.

## Extraction pipeline (post-import)

Once imported, the skill processes a DOCX file in these steps:

1. **Parse document XML** — unzip the `.docx` container; read `word/document.xml`, `word/styles.xml`, and relationship files.
2. **Body text extraction** — walk paragraph elements, preserving heading hierarchy (H1–H6 → `#`–`######`).
3. **Table serialisation** — convert Word tables to markdown pipe tables; flag merged cells.
4. **Tracked changes** — depending on `tracked_changes` setting: `accept_all` (clean), `reject_all` (original), or `show` (inline `[+added]` / `[-deleted]` markers).
5. **Comments extraction** — append as footnote block with author + timestamp.
6. **Metadata header** — prepend a YAML block with document properties.
7. **Chunking** — split by token count with overlap for large documents before passing to downstream skill.

## Legal document considerations

- **Arabic / bilingual contracts**: DOCX files from MENA jurisdictions often contain right-to-left text (Arabic) alongside left-to-right (English/French). Set `rtl: true` to preserve column order in tables and prevent paragraph reordering.
- **Certified translations**: some UAE Ministry of Justice and Lebanese Notary submissions require the certified translator's stamp metadata to be preserved. Map `doc_properties.custom` fields to retain this.
- **Redlines in M&A**: tracked changes in DOCX are legally significant in negotiated drafts. Default is `accept_all` (clean final read); switch to `show` when the user sends a redlined counterparty markup.
- **Password-protected files**: prompt the user for the document password before extraction; never log it.
- **Macro-enabled files (.docm)**: strip VBA before processing; flag to the user.

## Failure modes

| Error | Likely cause | Resolution |
|---|---|---|
| `corrupt_docx` | File not a valid ZIP/XML structure | Ask user to re-save as `.docx` from Word |
| `encoding_error` | Arabic/Persian characters garbled | Force `encoding: utf-8` and re-extract |
| `table_parse_fail` | Nested or merged cell tables | Fall back to raw cell dump |
| `rtl_paragraph_reversal` | LTR parser reorders RTL paragraphs | Set `rtl: true` |
| `password_protected` | File encrypted | Prompt for password |

## Related skills

- [[import-pdf-processing-anthropic]]
- [[import-pptx-processing-anthropic]]
- [[import-contract-review-anthropic]]
- [[multimodal-document-ingestion]]
- [[review-contract-generic]]
