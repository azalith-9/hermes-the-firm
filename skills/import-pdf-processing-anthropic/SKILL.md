---
name: import-pdf-processing-anthropic
description: Use when migrating a PDF document-processing skill originally built for the Anthropic the agent API into the mini-hermes-the-firm format. The adapter maps legacy PDF extraction configuration — text layer parsing, OCR fallback, table extraction, form field reading, and annotation handling — into the standard skill model. Critical for legal workflows involving court filings, regulatory submissions, notarised documents, and scanned contracts.
license: MIT
metadata: " id: import.pdf-processing-anthropic category: import jurisdictions: [__multi__] priority: P3 intent: [__import__, pdf, document-processing, migration, anthropic] related: [import-docx-processing-anthropic, import-pptx-processing-anthropic, import-contract-review-anthropic, multimodal-document-ingestion] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'import'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Import: PDF Processing (Anthropic)

## What it does

This import adapter migrates a **PDF document-processing skill** originally built for Anthropic's the agent API into the `mini-hermes-the-firm` standard format. PDF is the dominant format for legal documents globally: court filings, notarised instruments, regulatory submissions, signed contracts, government-issued licences, and certified translations all arrive as PDFs.

Unlike DOCX, PDFs may or may not have a selectable text layer. Scanned documents require OCR; encrypted PDFs require a password; form PDFs have interactive fields; certified documents may have a digital signature that must be preserved. The Anthropic-native skill may have used the agent's native PDF vision capability, a dedicated extraction library, or both.

## Import config

| Field | Source mapping | Default if absent |
|---|---|---|
| `extraction_mode` | Legacy `mode` | `text_first_ocr_fallback` |
| `ocr_engine` | Legacy `ocr` | `auto` (system default) |
| `tables` | Legacy `extract_tables` boolean | `true` |
| `form_fields` | Legacy `extract_forms` boolean | `true` |
| `annotations` | Legacy `extract_annotations` boolean | `true` |
| `digital_signature_check` | Legacy `check_signature` boolean | `true` |
| `language` | Legacy `lang` | `auto-detect` |
| `rtl_support` | Legacy `rtl` boolean | `true` (for MENA) |
| `chunk_size` | Legacy `chunk_tokens` | `2000` |
| `overlap` | Legacy `overlap_tokens` | `200` |
| `output_format` | Legacy `format` | `markdown` |

## Dry-run preview

```
IMPORT PREVIEW — pdf-processing-anthropic
Source shape     : Anthropic PDF extraction config
Mode             : text_first_ocr_fallback
OCR              : auto
Tables           : extracted
Form fields      : extracted
Annotations      : extracted
Digital signature: checked (not verified cryptographically — visual only)
RTL              : enabled (Arabic/Hebrew support)
Chunk            : 2000 tokens / 200 overlap
Output           : markdown
```

## Extraction pipeline (post-import)

1. **Detect PDF type**:
   - Native (selectable text) → direct text extraction
   - Scanned image → OCR pipeline
   - Mixed (some pages scanned, some native) → page-by-page detection
   - Encrypted → request password; log attempt; never store password

2. **Page-by-page extraction**: maintain page-number metadata for every extracted element; legal documents frequently reference "page X, clause Y".

3. **Table extraction**: detect table boundaries; serialize to markdown pipe tables; flag tables with merged cells as `[COMPLEX TABLE — manual verification recommended]`.

4. **Form field extraction**: identify interactive PDF form fields; extract field names and values; flag unsigned or blank required fields.

5. **Annotation extraction**: extract highlighted text, comments, and sticky notes; attribute to author if metadata available; append as footnote block.

6. **Digital signature check**: detect presence of digital signature (visual check only — not cryptographic validation); flag signed documents separately.

7. **RTL handling**: detect right-to-left text (Arabic, Hebrew); preserve paragraph ordering; ensure column order in tables reflects RTL layout.

8. **Chunking**: split by token count with overlap; preserve clause boundaries where possible.

## Legal document types and special handling

| Document type | Special requirement |
|---|---|
| Court filing (Lebanon / UAE) | Page/paragraph numbering must be preserved; filing stamps and seals should be flagged |
| Notarised document | Notary signature block and certification text must be extracted intact |
| Certified translation | Translator certification page must be preserved as a separate block |
| Government licence / certificate | Issue date, expiry date, and licence number should be extracted as structured metadata |
| Board resolution / POA | Signatory block and witness/notary endorsement are legally significant |
| Regulatory submission | Submission reference number and date should be extracted as metadata |

## Arabic / bilingual PDF considerations

PDFs from MENA jurisdictions frequently mix Arabic (RTL) and English (LTR) text:
- Set `rtl_support: true` to handle RTL paragraphs
- In bilingual contracts, Arabic is often the prevailing language (UAE and KSA government contracts); flag and note the prevailing language
- OCR quality for Arabic varies by font and scan quality; flag low-confidence passages

## Failure modes

| Error | Likely cause | Resolution |
|---|---|---|
| `no_text_layer` | Scanned PDF without OCR | Switch to OCR mode; warn user of quality risk |
| `password_protected` | Encrypted PDF | Prompt for password; never log |
| `rtl_reversal` | RTL paragraphs extracted as LTR | Ensure `rtl_support: true` |
| `table_parse_fail` | Complex merged-cell tables | Flag for manual review |
| `signature_not_found` | Digital signature present but not detected | Flag as `[SIGNATURE STATUS UNKNOWN]` |
| `arabic_ocr_low_quality` | Poor scan of Arabic text | Warn user; recommend re-scan at 300 DPI minimum |

## Related skills

- [[import-docx-processing-anthropic]]
- [[import-pptx-processing-anthropic]]
- [[import-contract-review-anthropic]]
- [[multimodal-document-ingestion]]
- [[review-contract-generic]]
