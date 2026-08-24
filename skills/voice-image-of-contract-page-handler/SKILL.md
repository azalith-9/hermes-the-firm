---
name: voice-image-of-contract-page-handler
description: Use when a user uploads a photograph or image of a physical contract page — taken with a phone camera, flatbed scanner, or screen capture — rather than a native digital document. This skill governs the OCR extraction, image quality assessment, text flow reconstruction, and integration into the document workspace for downstream legal analysis or drafting assistance.
license: MIT
metadata: " id: voice.image-of-contract-page-handler category: voice jurisdictions: [__multi__] priority: P2 intent: [__voice__, ocr, multimodal, photo-upload, contract-image] related: - voice-multimodal-scanned-pdf-handler - voice-multimodal-signature-page-detector - voice-scanned-pdf-handler source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'voice'.
Registered as a flat plugin skill.
-->


# Image of Contract Page Handler

## What it does

Users often photograph physical contracts with their phones — a page on a desk, a document at a notary's office, a clause they want to query right now. This skill handles the full pipeline from image upload to usable legal text: quality assessment, OCR extraction, text flow reconstruction, and routing into the document workspace.

It is the mobile-first complement to [[voice-multimodal-scanned-pdf-handler]], optimized for single-page or few-page photos rather than full multi-page scan batches.

## Trigger conditions

Invoke this skill when:
- The user uploads an image file (JPEG, PNG, HEIC, WEBP) in a legal context.
- The user's message suggests they are photographing a physical document: "Take a photo of this page", "Here's a picture of the clause", "I just photographed the contract".
- The image content (detected by visual analysis) shows text on paper with document formatting.

Do not invoke this skill for non-document images (photographs of people, logos, product photos). Route those to general multimodal handling.

## Image quality assessment

Before attempting OCR, assess the image quality and flag issues to the user:

| Issue | Detection | Response |
|-------|-----------|---------|
| Blur / camera shake | High-frequency noise analysis | "The image is blurry — can you retake it with the camera steady?" |
| Low light | Brightness histogram below threshold | "The image is too dark to read reliably. Try in better light or increase your screen brightness." |
| Extreme angle / perspective distortion | Keystone effect detection | "The page is at an angle. For best results, photograph straight-on from above." |
| Partial page | Text appears cut off on one or more edges | "Part of the page appears to be outside the frame. Would you like to try again?" |
| Glare / reflection | Specular highlight detection | "There is glare on the page that may affect text extraction." |

For mild quality issues, proceed with OCR but flag the specific sections likely affected. For severe issues (illegible image), ask the user to retake before proceeding.

## OCR extraction

Apply the same language detection and OCR pipeline as [[voice-multimodal-scanned-pdf-handler]]:
1. Detect language(s): Arabic, English, French, or mixed.
2. Apply perspective correction (deskew, straighten).
3. Run OCR with per-word confidence scoring.
4. Reconstruct paragraph flow and reading order (especially important for Arabic right-to-left text).

### Mobile photo specific considerations
- Phone photos of paper often include the hand holding the document, a desk surface, or a shadow — crop or mask these before OCR.
- HEIC format (Apple default) must be converted to JPEG or PNG before processing.
- High-resolution phone photos (12–48MP) should be downsampled to 300 DPI equivalent for OCR — no benefit above this resolution for text, and processing cost increases.

## Text flow reconstruction

A single photograph of a contract page may contain:
- Multi-column layout (common in older MENA contract formats)
- Tables (financial terms, payment schedules)
- Marginalia or handwritten annotations
- Signature lines or official stamps

Handle each distinctly:
- Multi-column: detect column separators and reconstruct correct left-right reading order (or right-left for Arabic).
- Tables: reconstruct as a markdown table or structured JSON, not a linear text dump.
- Handwritten annotations: flag as "handwritten note detected — transcription may be inaccurate."
- Signature lines: flag and route to [[voice-multimodal-signature-page-detector]].

## Integration into document workspace

After extraction:
1. Display the extracted text to the user for confirmation ("Here is what I extracted — does this look correct?").
2. If confirmed, add the page to the active matter's document workspace.
3. Enable downstream skills: the page becomes queryable for clause analysis, summarization, or drafting assistance.
4. Preserve page-number metadata if the user indicates which page of a larger document this is.

## Voice extension

When operating in voice mode, this skill integrates with the camera capability:

> User: "Take a photo of this page and tell me what it says."

In this flow:
1. The system prompts the camera interface.
2. The user photographs the page.
3. This skill runs OCR.
4. The [[voice-short-spoken-output]] skill formats the result for spoken delivery: not the full OCR text, but a summary of the key content detected.

The voice output should lead with: "I found [page type] — it appears to be a [contract type/clause type]. The key terms I can see are..." and then speak the substance.

## Related skills

- [[voice-multimodal-scanned-pdf-handler]]
- [[voice-multimodal-signature-page-detector]]
- [[voice-scanned-pdf-handler]]
- [[voice-short-spoken-output]]
