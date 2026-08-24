---
name: tool-ocr-arabic
description: Use when a user uploads a scanned PDF or image containing Arabic-language text that is not machine-readable. Invoked automatically when Arabic content is detected in a non-selectable scan, or explicitly when the user requests OCR on an Arabic document. Outputs plain text with confidence scores, RTL-ordered, ready for downstream analysis. Critical for processing Arabic legal documents, court judgments, official gazette pages, and corporate filings in MENA jurisdictions.
license: MIT
metadata: " id: tool.OCR-arabic category: tool priority: P0 intent: [ocr-arabic, scanned-arabic, document-extraction, arabic-text] related: [tool-ocr-english, tool-pdf-extractor, multimodal-scanned-pdf-handler, safety-pii-redaction-before-rag] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'tool'.
Registered as a flat plugin skill.
-->


# Tool — OCR (Arabic)

## What it does

This tool extracts machine-readable text from scanned PDFs and images that contain Arabic-language content. It applies Arabic-tuned OCR with post-processing for RTL text ordering, ligature normalization, and confidence scoring per text block. The output is plain text ready for downstream legal analysis, translation, or RAG indexing.

Arabic OCR is significantly more complex than Latin-script OCR due to:
- Right-to-left (RTL) script direction
- Connected cursive letterforms with context-dependent glyph shapes
- Absence of capital letters (capitalization as a structural signal is absent)
- Mixed Arabic-English documents common in MENA legal practice
- Use of both Eastern Arabic numerals (٠١٢٣٤٥٦٧٨٩) and Western Arabic numerals (0123456789)
- Occasional use of Ottoman/Naskh/Nasta'liq historical scripts in older documents

## When invoked

- User uploads a scanned PDF where `tool-pdf-extractor` returns empty or garbled text
- Arabic character blocks detected in the scan via pre-processing image analysis
- User explicitly says "OCR this", "extract text", or "read this Arabic document"
- Document type suggests Arabic content: court judgment from KSA, UAE, Lebanon, or Egypt; official gazette page; commercial registration excerpt

## Pipeline

### Step 1: Detection
Before invoking the full OCR pipeline, a lightweight detector checks:
- PDF metadata for language tags
- Image character recognition on a sample page (first 200px of page 1)
- Filename or user-provided context

If both Arabic and English are detected (common in bilingual MENA contracts), invoke bilingual OCR mode.

### Step 2: Engine selection

| Engine | Best for | Notes |
|--------|----------|-------|
| **Tesseract (ara traineddata)** | High-quality print; offline; no data residency concern | Weaker on poor scans |
| **Google Cloud Vision** | Mixed-quality scans; high accuracy | Data sent to Google — check residency policy |
| **AWS Textract** | Tables and structured forms (e.g., KSA CR excerpts) | Strong table extraction |
| **Microsoft Azure AI Document Intelligence (Read API)** | Mixed scripts; handwriting | Strongest for handwritten Arabic |

For documents classified as confidential or containing sensitive PII, prefer offline Tesseract or a private endpoint — do not route to third-party cloud services without explicit user consent and data processing agreement.

### Step 3: Pre-processing
- **Deskewing**: correct tilt from scanner placement
- **Binarization**: convert to black-and-white to improve character contrast
- **Noise removal**: despeckle, remove scan artifacts
- **Resolution upscaling**: if DPI < 300, upscale to 300+ DPI before OCR

### Step 4: OCR execution
Run with Arabic language model. For bilingual documents, run with `ara+eng` combined model.

### Step 5: Post-processing
- **Dehyphenation**: Arabic words broken across lines (uncommon but occurs in some print)
- **RTL ordering**: ensure text blocks are ordered right-to-left
- **Ligature normalization**: normalize letter combinations to Unicode canonical forms
- **Hamza/Alef normalization**: treat أ / إ / آ / ا as equivalent for search purposes
- **Tatweel removal**: strip elongation characters (ـ) that appear in some printed documents
- **Numeral normalization**: optionally convert Eastern Arabic numerals to Western for downstream processing

### Step 6: Structure extraction
Where possible, identify:
- **Headings** (larger font, centered, bold)
- **Article/clause numbers**
- **Paragraph boundaries**
- **Tables** (route to table extractor)
- **Signature blocks and stamps** (detect, do not transcribe stamps)

### Step 7: Confidence scoring
Return per-block confidence scores. Flag blocks below 75% confidence for human review.

## Quality considerations

### Handwritten Arabic
Handwritten Arabic is significantly harder than typed. Accuracy drops substantially. Common scenarios:
- Handwritten annotations in contract margins → flag as "handwritten annotation, low confidence"
- Handwritten Arabic signatures → detect presence but do not attempt to read the name
- Handwritten notarial text → accuracy depends heavily on the scribe's handwriting

Always warn the user when handwritten sections are detected:
> "Handwritten Arabic detected on pages X. OCR accuracy for handwritten Arabic is typically 40–70%. Human review recommended."

### Ottoman script
Pre-modern Ottoman Turkish written in Arabic script (used in historical property deeds, older Lebanese legal documents, and Ottoman-era firmans) is not handled by modern Arabic OCR. Flag and escalate.

### Classical Arabic vs Modern Standard Arabic
Classical Quranic Arabic and classical legal texts (fiqh) differ in vocabulary and structure from Modern Standard Arabic. OCR output will be character-accurate but lexical analysis may require specialized tools.

### Mixed Arabic-English documents
Very common in MENA legal practice: English contract body with Arabic-language definitions table, or Arabic court judgment citing English case law. Use bilingual mode and preserve the language switch boundaries in the output.

### Numerical content
Eastern Arabic numerals (٢٠٢٥ = 2025) appear in many official documents. The post-processor can either normalize to Western numerals or preserve both forms. Amounts, dates, and article numbers should be double-checked regardless.

## Privacy and data residency

Arabic legal documents frequently contain:
- National IDs (هوية / رقم الهوية) of parties
- Financial account numbers
- Personal addresses
- Sensitive business information

**Mandatory steps before routing to any cloud OCR engine**:
1. Classify the document sensitivity (public / internal / confidential / secret)
2. Apply PII detection — see [[safety-pii-redaction-before-rag]] for the redaction pipeline
3. For confidential documents: use offline Tesseract or an on-premise private endpoint
4. Maintain an audit log of which documents were processed through which engine

GCC data protection frameworks (UAE Personal Data Protection Law, KSA PDPL, BDL Circular 126) impose restrictions on cross-border personal data transfer. Cloud OCR constitutes processing on a third-party infrastructure outside the jurisdiction — confirm the data processing agreement and adequacy decision before proceeding.

## Output schema

```json
{
  "fullText": "نص المستند الكامل ...",
  "language": "ar",
  "bilingualSections": [
    { "language": "ar", "pages": [1, 2, 3] },
    { "language": "en", "pages": [4] }
  ],
  "pages": [
    {
      "pageNum": 1,
      "text": "...",
      "confidence": 0.91,
      "handwrittenDetected": false,
      "lowConfidenceBlocks": []
    }
  ],
  "structure": {
    "headings": [...],
    "paragraphs": [...],
    "tables": [...],
    "signatureBlocks": [...],
    "stamps": [...],
    "articleNumbers": [...]
  },
  "warnings": ["Handwritten Arabic detected on page 5 — human review recommended"],
  "engine": "aws-textract",
  "processingDate": "2026-05-14T10:00:00Z"
}
```

## Failure modes

| Failure | Symptom | Resolution |
|---------|---------|------------|
| Very poor scan quality | Confidence < 50% across all pages | Request user to provide a better-quality scan |
| Ottoman / historical script | Garbled character output | Flag; escalate to specialist |
| Cloud engine timeout | Timeout on large document | Split into batches of 20 pages |
| Data residency block | User disallows cloud OCR | Switch to offline Tesseract; warn about quality trade-off |
| Encoding error | Reversed RTL rendering | Force UTF-8 + BiDi algorithm post-processing |

## Related skills

- [[tool-ocr-english]] — English OCR pipeline (same architecture, Latin-script tuning)
- [[tool-pdf-extractor]] — always try PDF text-layer extraction first; invoke OCR only as fallback
- [[multimodal-scanned-pdf-handler]] — orchestrator for scanned-only documents that routes to OCR
- [[safety-pii-redaction-before-rag]] — redact PII before sending OCR output downstream
