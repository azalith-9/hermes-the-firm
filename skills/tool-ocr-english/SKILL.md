---
name: tool-ocr-english
description: Use when a user uploads a scanned English-language PDF or contract image where the text layer is absent or empty. Converts image-based pages to searchable text, preserving clause numbering, section hierarchy, and page anchors for citation. Also detects signature blocks and handwritten initials. Triggers automatically when PDF text extraction returns empty, or when the user uploads a photo of a contract from WhatsApp or email.
license: MIT
metadata: " id: tool.OCR-english category: tool jurisdictions: [__multi__] priority: P1 intent: [ocr, scan, document-extraction, contract-image] related: [tool-ocr-arabic, tool-pdf-extractor, multimodal-scanned-pdf-handler, safety-pii-redaction-before-rag] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'tool'.
Registered as a flat plugin skill.
-->


# OCR — English

## What it does

This tool converts image-based PDFs and contract photographs into machine-readable text. It is invoked when the primary PDF text extraction ([[tool-pdf-extractor]]) returns empty text — indicating the document is a scan — or when the user provides a document as a photograph rather than a native digital file.

The English OCR pipeline is optimized for legal documents: it preserves clause numbering, section hierarchy, and page anchors so that downstream analysis can cite specific provisions as "page 4, clause 7.2" rather than losing positional context.

## When to use this

- User uploads a PDF and text extraction returns empty or near-empty (< 50 characters per page)
- User sends a photo of a contract, lease, or certificate via chat (common for WhatsApp-sourced documents in MENA)
- User explicitly requests "OCR this" or "extract text from this scan"
- Re-running OCR after an initial low-confidence pass to attempt improvement
- Bilingual document where English pages need separate processing from Arabic pages

**Do not invoke** when the PDF has a selectable text layer — use [[tool-pdf-extractor]] directly, which is faster and more accurate.

## Pipeline

### Step 1: Pre-processing
Before OCR, apply image enhancement:
- **Deskew**: correct rotation from scanner placement
- **Binarization**: convert to black-and-white at optimal threshold
- **Denoise**: remove speckle and scan artifacts
- **Resolution check**: if DPI < 300, upscale using bicubic interpolation to 300 DPI minimum; 600 DPI preferred for small print

### Step 2: Engine selection

| Engine | Best for | Data residency |
|--------|----------|---------------|
| **Tesseract (eng)** | Standard print quality; on-premise deployable | Local — no data egress |
| **Google Cloud Vision** | High accuracy on mixed-quality scans; handwriting | Data sent to Google |
| **AWS Textract** | Tables, forms, checkboxes; structured legal documents | Data sent to AWS |
| **Microsoft Azure AI Document Intelligence** | Complex layouts; mixed typefaces | Data sent to Azure |

Default to Tesseract for confidential documents. Use cloud engines only with user consent and appropriate data processing agreements.

### Step 3: Layout analysis
Before OCR character recognition, analyze the page layout to identify:
- **Multi-column layouts** (common in statutes and gazette reprints)
- **Header / footer regions** (exclude page numbers from body text)
- **Margin annotations** (flag separately as "marginal note")
- **Tables** (route to table extractor for separate handling)
- **Signature block regions** (apply signature detection — see Step 5)

### Step 4: OCR and character recognition
Run with English language model. For documents with a small proportion of French or Arabic text, consider multilingual mode (`eng+fra` or `eng+ara`).

Post-processing:
- **Hyphenation correction**: re-join words split across line breaks in justified text
- **Smart quote normalization**: convert smart quotes to straight quotes for downstream text processing
- **Number formatting**: preserve amounts (USD 1,000,000) and dates (01/01/2026)
- **Clause number preservation**: `7.2`, `7.2.1`, `(a)`, `(i)` — critical for legal citation

### Step 5: Signature and initials detection
Legal document processing has specific needs around signatures:
- **Signature blocks**: detect regions that contain signature lines (`___________`) — flag the block as "signature block found, page X"
- **Executed vs blank**: attempt to determine whether a signature line is filled in (ink present) or blank
- **Handwritten initials on pages**: detect but note they are present rather than transcribing them (initials are too variable to reliably OCR)
- **Stamps and seals**: detect the presence of stamps (circular, rectangular) and note their page location; do not attempt to transcribe stamp text unless quality is high

**Output**: `detectedSignatures: [{ page, blockType: "signature_line" | "executed_signature" | "initial", filled: bool }]`

### Step 6: Page anchoring
Each page's text is tagged with its page number. Clause and section numbers detected in the text are indexed to their page. This allows downstream skills (review, analysis) to cite: "Clause 14.2 (page 8): …"

### Step 7: Confidence scoring
Return per-page and per-block confidence scores. Blocks below 80% confidence are flagged for human review. Overall document quality rating: `excellent` (>90%), `good` (80–90%), `marginal` (70–80%), `poor` (<70%).

## Output schema

```json
{
  "fullText": "MASTER SERVICES AGREEMENT\n\nThis Agreement is entered into...",
  "language": "en",
  "pages": [
    {
      "pageNum": 1,
      "text": "...",
      "confidence": 0.94,
      "marginNotes": [],
      "tables": [...]
    }
  ],
  "structure": {
    "headings": [{ "text": "RECITALS", "page": 1, "level": 1 }],
    "clauses": [{ "number": "1.1", "text": "...", "page": 2 }],
    "definitionBlocks": [...],
    "signatureBlocks": [{ "page": 12, "filled": true }]
  },
  "detectedSignatures": [
    { "page": 12, "blockType": "executed_signature", "filled": true },
    { "page": 12, "blockType": "initial", "filled": true }
  ],
  "qualityRating": "good",
  "warnings": ["Marginal annotations detected on pages 3, 7 — not included in main text"],
  "engine": "google-cloud-vision",
  "processingDate": "2026-05-14T10:00:00Z"
}
```

## Limits

- **Language**: English only. For Arabic, use [[tool-ocr-arabic]]; for French, use a French-configured instance of this pipeline or the multilingual mode.
- **Handwriting in margins**: detect and flag; do not attempt to transcribe — accuracy is too low to be reliable.
- **Stamps and seals**: note presence on which page; do not transcribe unless quality is high.
- **Multi-language documents**: if significant non-English content is detected, switch to the appropriate language-specific OCR tool or bilingual mode.
- **Very large files**: documents over 200 pages are chunked into 20-page batches for processing; results are then reassembled.
- **Password-protected PDFs**: cannot be OCR'd. Request user to unlock the PDF first.

## Common legal document types handled

| Document type | Notes |
|---------------|-------|
| Scanned contracts | Core use case; preserve clause numbers |
| Court judgments | Multi-column possible; header/footer exclusion important |
| Corporate certificates | Short documents; certificate of incorporation, CR excerpts |
| Land/property deeds | Older documents may have typewriter text |
| Notarized translations | Bilingual documents common |
| Insurance policies | Tables, schedules important |
| Bank guarantee letters | Structured templates |
| WhatsApp/email photographs | Variable quality; pre-processing critical |

## Failure modes

| Failure | Symptom | Resolution |
|---------|---------|------------|
| Very poor scan | Confidence < 65% | Request better scan; report quality rating to user |
| Encrypted PDF | Cannot extract pages | Ask user to remove password |
| Non-English text dominant | Low confidence + garbled output | Switch to appropriate language OCR |
| Cloud engine timeout | Timeout on large file | Split into batches; retry |
| Layout detection failure | Merged columns or garbled order | Try alternative engine |

## Related skills

- [[tool-ocr-arabic]] — Arabic OCR pipeline; invoke when Arabic content detected
- [[tool-pdf-extractor]] — always try this first; only fall back to OCR when text layer is absent
- [[multimodal-scanned-pdf-handler]] — orchestrator that selects between PDF extraction and OCR
- [[safety-pii-redaction-before-rag]] — apply PII redaction before sending OCR output to RAG or LLM
