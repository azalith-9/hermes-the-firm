---
name: voice-signature-page-detector
description: Use when processing a document (via OCR, image, or text) and needing to identify signature pages based on visual and textual features — signature lines, witness blocks, seal placeholders, and execution blocks. This is the lightweight router-level entry point that detects signature-page presence and routes to the full validation skill; it also enforces the critical rule that signature pages must not be paraphrased, redacted, or restructured during document processing.
license: MIT
metadata: " id: voice.signature-page-detector category: voice jurisdictions: [__multi__] priority: P2 intent: [__voice__, ocr, multimodal, signature-detection] related: - voice-multimodal-signature-page-detector - voice-multimodal-scanned-pdf-handler - voice-image-of-contract-page-handler source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'voice'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Signature Page Detector (Router Entry Point)

## What it does

This is the router-level signal that triggers special handling when a page is detected as a signature page. It does not perform the full validation (that is [[voice-multimodal-signature-page-detector]]); its job is to:

1. Detect signature-page indicators during document processing.
2. Flag the page for special handling — preserving it intact during OCR reconstruction and analysis.
3. Route to the full validation skill when complete execution analysis is needed.

## Detection signals

A page is flagged as a signature page when it contains two or more of the following:

### Textual indicators
- Signature line markers: rows of underscores or dotted lines ("____________"), often preceded by "By:", "Signed:", "Signature:" or Arabic equivalents (توقيع، بإمضاء).
- Name and title fields below the signature line.
- Date fields: "Date:", "Dated:", or blank field near a signature line.
- Witness indicators: "Witness:", "Witnessed by:", "In the presence of:", "Notary:".

### Visual indicators (image/OCR context)
- Horizontal rule lines positioned in the lower half of the page (classic signature placement).
- Blank spaces below textual role labels.
- Stamp-shaped circular or rectangular marks with printed text.
- Handwritten strokes that do not correspond to body text (indicating a physical signature was present when the document was scanned).

### Layout indicators
- A page that is predominantly whitespace with only a few labeled fields — the classic signature-page structure.
- A page that follows the last substantive clause page and contains no legal paragraph text.

## Special handling rule

Once a page is flagged as a signature page, enforce these handling constraints throughout all downstream processing:

1. **Do not paraphrase the content of a signature page.** When summarizing a document, exclude the signature page from the summary. Report its existence and status separately.
2. **Do not accidentally redact signature elements.** PII redaction passes that operate on the surrounding document text must be configured to exclude signature blocks — names, titles, and companies in signature lines are legally essential.
3. **Do not restructure the layout.** During text reconstruction from OCR, the signature block's spatial layout (which name is under which signature line) is legally meaningful and must be preserved.
4. **Do not infer content for blank fields.** If a date field or name field on a signature page is blank, flag it as blank — do not infer or fill.

## Output of detection

When a signature page is detected, surface to downstream skills:
```json
{
  "signature_page_detected": true,
  "page_numbers": [10, 11],
  "handling": "preserve-layout",
  "route_to_full_validation": true
}
```

The `route_to_full_validation: true` flag triggers [[voice-multimodal-signature-page-detector]] to run its full execution completeness check.

## User communication

When a signature page is detected and the user has not specifically asked for signature analysis, a brief note is appropriate:
> "I noticed signature pages on pages 10–11. I'll include them in the document but flag them separately. Would you like me to check whether all required signatures are present?"

Do not bury this finding in a long summary output.

## Related skills

- [[voice-multimodal-signature-page-detector]]
- [[voice-multimodal-scanned-pdf-handler]]
- [[voice-image-of-contract-page-handler]]
- [[voice-scanned-pdf-handler]]
