---
name: voice-multimodal-scanned-pdf-handler
description: Use when a user uploads a PDF that has no text layer or whose text layer is gibberish — indicating a scanned document that requires OCR processing before any legal analysis can proceed. This skill covers detection, the OCR pipeline (Arabic/English/French), quality confidence scoring, table and signature detection, PII redaction before RAG ingestion, and the critical legal caveat about evidentiary weight of OCR-reconstructed text.
license: MIT
metadata: " id: multimodal.scanned-PDF-handler category: voice priority: P0 intent: [scanned pdf, ocr pdf, ocr, multimodal] related: - voice-multimodal-signature-page-detector - voice-dictation-cleanup - voice-image-of-contract-page-handler - safety-pii-redaction-before-rag source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'voice'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Scanned PDF Handler

## What it does

When a user uploads a PDF, Louis first checks whether the document contains a usable text layer. If it does not — or if the text layer is garbled (a common artifact of some scan-to-PDF pipelines) — the document must be passed through an OCR pipeline before any legal analysis, drafting assistance, or retrieval-augmented generation can begin.

This skill governs that entire pipeline: detection, processing, quality assurance, and the handoff back to the legal analysis layer.

## Detection

A PDF is treated as requiring OCR if any of the following conditions are met:

| Condition | Detection method |
|-----------|-----------------|
| No embedded text layer | PDF.js or equivalent parser returns 0 text tokens from the first page |
| Garbled text (OCR-baked-in artifacts) | Heuristic: high ratio of non-word tokens, unrecognized character sequences, or obvious misrecognition patterns ("rn" for "m", etc.) |
| Mixed content (some pages text, some scanned) | Per-page check; flag scanned pages individually |
| File metadata indicates scan origin | EXIF/PDF metadata shows scanner device, scan date, or scan DPI |
| Image-only PDF | All pages are embedded JPEG/PNG images with no text layer |

Apply per-page detection, not per-document — a 40-page contract may have 38 text pages and 2 scanned signature pages. Handle each appropriately.

## OCR pipeline

### Step 1 — Language detection
Before running OCR, detect the document's language(s):
- Arabic-only: route to Arabic OCR engine (`tool-ocr-arabic`).
- English-only: route to English OCR engine (`tool-ocr-english`).
- Mixed Arabic-English (common in MENA commercial documents): run both engines per paragraph block; use the higher-confidence output per block.
- French or French-Arabic: route accordingly.

MENA legal documents frequently contain mixed-language clauses — a UAE contract may have English body text with Arabic recitals, signature blocks, and Ministry of Labour certification stamps. The pipeline must handle each block independently.

### Step 2 — Page image preprocessing
Before OCR:
- Deskew rotated pages (a common artifact of physical document scanning).
- Binarize for clarity (convert grayscale scans to high-contrast black/white).
- Remove noise from low-quality scans where possible.

### Step 3 — Text extraction
Run OCR engine on each page. Capture:
- Text content (full text, preserving reading order)
- Bounding box coordinates per text block (for page mapping)
- Confidence score per text block (0–100%)

### Step 4 — Paragraph and structure reconstruction
- Reconstruct paragraph breaks from whitespace and layout analysis.
- Detect multi-column layouts (common in court documents and newspapers) and handle column order correctly.
- Detect tables: OCR engines often produce disorganized text from tables — use table-structure detection to reconstruct rows and columns. Flag tables for user review if confidence is below 85%.

### Step 5 — Signature and seal detection
Before returning text, pass each page through the signature detection layer ([[voice-multimodal-signature-page-detector]]):
- Flag signature pages and signature blocks.
- Do not OCR over signature images in a way that loses their original position and nature — the signature location and presence are legally relevant.

## Quality flags and confidence scoring

| Confidence (per block) | Action |
|-----------------------|--------|
| 90–100% | Process normally |
| 80–89% | Include in output; flag block with `[OCR: moderate confidence]` |
| 60–79% | Include but flag prominently: "OCR confidence low for this section — verify against original." |
| Below 60% | Flag to user for manual verification; do not include unreviewed in downstream analysis |

Whole-document confidence is reported as a weighted average. If any critical section (preamble, payment clause, obligations) falls below 80%, surface a banner warning to the user.

## Special handling — MENA document types

| Document type | Special consideration |
|---------------|-----------------------|
| UAE Ministry of Labour / MOHRE stamps | Official stamp text is often partially readable only; flag as "stamp detected, content may be incomplete" |
| KSA notarial seals | Low OCR accuracy; flag and ask user to confirm notarization details manually |
| Lebanese Notaire République seals | French + Arabic mixed; confidence often degrades on embossed stamps |
| Handwritten annotations | Flag as "handwritten annotation detected — manual review required" |
| Arabic text in right-to-left layout | Ensure reading order is RTL; paragraph reconstruction must not reverse sentence order |

## PII redaction before RAG ingestion

Before any OCR output is ingested into a retrieval-augmented generation (RAG) pipeline or vector store, apply the PII redaction layer ([[safety-pii-redaction-before-rag]]):
- National ID numbers (Emirates ID, CNIC, Lebanese NIC, etc.)
- Passport numbers
- Personal financial account numbers
- Personal addresses (unless relevant to a corporate matter)
- Personal phone numbers of individuals named in the document

PII redaction is applied after OCR but before the text is chunked and embedded. The original document (with PII) is stored securely and is never embedded unredacted.

## Legal weight caveat

OCR-reconstructed text is not equivalent to a certified copy of the original document. When the user is relying on OCR output for:
- Evidence in litigation
- Signature verification
- Regulatory filing
- Notarized or apostilled document analysis

Surface this caveat explicitly:

> "This analysis is based on OCR-reconstructed text. For court use, enforcement purposes, or formal regulatory filings, please verify key terms against the original document and obtain a certified copy if required."

## Output to downstream skills

After the OCR pipeline completes, return:
- Full reconstructed text, page-by-page with page-number mapping.
- Per-page confidence scores.
- Flags: signature pages, tables, low-confidence blocks, PII-redacted fields.
- Language detection result per page.

The downstream legal analysis skill (review, extract, draft) receives this output as if it were a native text-layer PDF.

## Related skills

- [[voice-multimodal-signature-page-detector]]
- [[voice-dictation-cleanup]]
- [[voice-image-of-contract-page-handler]]
- [[safety-pii-redaction-before-rag]]
