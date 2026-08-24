---
name: voice-scanned-pdf-handler
description: Use when a user uploads a scanned PDF (no text layer) and needs it processed through automatic OCR before any legal analysis, chat, or document workspace ingestion can proceed. This is the lightweight router-level entry point for scanned PDF handling; it detects the absence of a text layer and delegates to the full OCR pipeline, supporting Arabic, English, and French documents with a user-confirmation fallback when confidence is low.
license: MIT
metadata: " id: voice.scanned-PDF-handler category: voice jurisdictions: [__multi__] priority: P2 intent: [__voice__, ocr, multimodal, scanned-pdf] related: - voice-multimodal-scanned-pdf-handler - voice-image-of-contract-page-handler - voice-multimodal-signature-page-detector source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'voice'.
Registered as a flat plugin skill.
-->


# Scanned PDF Handler (Router Entry Point)

## What it does

This is the lightweight, router-level entry point invoked when a user uploads a PDF and the system detects it has no usable text layer. Its job is:
1. Confirm the document is scanned (not native-text).
2. Select the appropriate OCR language mode (English, Arabic, French, or auto-detect).
3. Delegate to the full OCR pipeline ([[voice-multimodal-scanned-pdf-handler]]).
4. Surface a user-confirmation step when overall OCR confidence is low.

Think of this skill as the gatekeeper that ensures no scanned document silently fails into downstream analysis with garbled text.

## Detection logic

A PDF requires scanned handling if:
- Page text token count is zero or near-zero for the first three pages.
- Text extracted is a pattern of gibberish characters consistent with embedded-font issues or pre-baked OCR artifacts.
- The file's creation metadata shows a scanner as the producing application.
- The user explicitly describes the file as scanned ("I scanned this contract", "it's a scan").

If only some pages are scanned and others have native text, process each page type independently and merge the results.

## Language modes

| Mode | When to use |
|------|-------------|
| English | Document is in English only |
| Arabic | Document is in Arabic only |
| French | Document is in French only |
| Auto-detect | Document has mixed language sections (most common for MENA commercial documents) |

Default to auto-detect unless the user specifies a language. Auto-detect applies per-page language identification before routing to the appropriate OCR engine.

## User-confirmation fallback

If the overall OCR confidence score for the document falls below 80%:

Show the user a preview of the extracted text from the first page with this message:
> "I was able to extract text from this scanned document, but the quality is limited. Here is a sample — if it looks correct, I'll proceed. If the text looks wrong, you may get better results by uploading a higher-resolution scan."

[Show first-page extracted text preview]

[Looks good — proceed] [I'll upload a better scan]

This is preferable to silently passing low-quality OCR text into an analysis skill, which would produce unreliable legal output.

## Handoff to full pipeline

Once the scanned-PDF determination is confirmed, delegate entirely to [[voice-multimodal-scanned-pdf-handler]] for:
- Page-by-page processing
- Table detection
- Signature page flagging
- PII redaction before RAG ingestion
- Per-block confidence scoring

This skill does not duplicate that logic — it is the entry point, not the full implementation.

## What to tell the user

When a scanned PDF is detected, acknowledge it proactively:
> "This looks like a scanned document — I'll run OCR to extract the text before we work with it. This may take a moment for longer documents."

Do not silently process. Users need to know why there is a delay and what is happening.

## Related skills

- [[voice-multimodal-scanned-pdf-handler]]
- [[voice-image-of-contract-page-handler]]
- [[voice-multimodal-signature-page-detector]]
- [[voice-dictation-cleanup]]
