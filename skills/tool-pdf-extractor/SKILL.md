---
name: tool-pdf-extractor
description: Use as the first step whenever a user uploads a PDF document that needs text analysis, review, or RAG indexing. Extracts text from PDFs with a selectable text layer using PDF.js (fast, no OCR), preserving page boundaries, paragraph structure, headings, and tables for downstream citation. Falls back to OCR tools for scanned documents. Critical to get right — downstream analysis quality depends entirely on clean text extraction.
license: MIT
metadata: " id: tool.pdf-extractor category: tool priority: P0 intent: [pdf-extract, parse-pdf, document-ingestion] related: [tool-ocr-arabic, tool-ocr-english, multimodal-scanned-pdf-handler, safety-pii-redaction-before-rag, tool-rag-firm-knowledge] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'tool'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Tool — PDF Extractor

## What it does

The PDF Extractor is the entry point for all PDF documents entering the legal AI pipeline. It extracts text content, structure, and metadata from a PDF file, producing a clean, page-anchored text representation suitable for downstream analysis, RAG indexing, drafting reference, or review.

It is invoked automatically whenever a user uploads a PDF and a text-analysis task follows. The extractor decides whether the document has a native text layer (fast extraction) or needs OCR (slower, less accurate). Getting this decision right is critical: OCR on a PDF with a good text layer is wasteful; text extraction on a scanned PDF produces garbage.

## Library stack

| Library | Role | Notes |
|---------|------|-------|
| **pdfjs-dist** (Mozilla PDF.js) | Primary text-layer extraction | Browser + Node; fast; no server-side dependency |
| **pdfminer-six** (Python) | Fallback for complex layouts | Handles rotated pages, ligature correction |
| **Poppler (pdftotext)** | System-level fallback | Fastest for bulk extraction |
| **pdf2json** | JSON-structured extraction | Preserves font metadata for heading detection |

## Extraction modes

### Mode 1: Text-layer extraction (default)
For PDFs with a selectable text layer. This is the fastest path and produces the highest-quality output.

**When to use**: when clicking in the PDF lets you select and copy text — i.e., the PDF was created digitally (from Word, InDesign, etc.) rather than by scanning.

**Process**:
1. Open PDF with PDF.js
2. Extract text content per page with position metadata
3. Reconstruct reading order (left-to-right, top-to-bottom for LTR; right-to-left for RTL)
4. Detect heading candidates (larger font-size, bold, centered)
5. Detect clause/section numbering patterns
6. Detect definition blocks (terms in quotes or bold + definition)
7. Tag page boundaries
8. Return full-text + structure

### Mode 2: OCR fallback
For scanned PDFs where text-layer extraction returns < 50 characters per page.

**Routing**:
- Detect dominant language → route to [[tool-ocr-english]] or [[tool-ocr-arabic]]
- For bilingual documents → run both pipelines and merge by page

**Signal for scanned document**: average characters per page < 50 after text-layer extraction.

### Mode 3: Structured extraction
For documents where clause-level granularity is needed — e.g., a 50-clause MSA where the downstream task is clause-by-clause review.

**Additional steps**:
- Identify clause hierarchy (1, 1.1, 1.1.1; a, b, c; (i), (ii))
- Assign each clause its full hierarchical path
- Return as a nested clause tree

Output shape: `{ clauses: [{ path: "7.2.1", heading: "...", text: "...", page: 8 }] }`

### Mode 4: Table extraction
Tables are common in legal documents: schedules, pricing tables, IP registers, cap tables. PDF tables are structurally challenging — cells may not have borders and rely on spatial positioning.

**Process**:
- Detect table regions using line detection + cell spacing analysis
- Extract cell content row by row
- Return as: `{ tables: [{ page, rows: [[cell,...], ...], headers: [...] }] }`

## Output schema

```json
{
  "metadata": {
    "title": "Master Services Agreement",
    "author": "...",
    "created": "2025-03-01",
    "modified": "2025-03-15",
    "pages": 24,
    "language": "en",
    "encrypted": false,
    "textLayerPresent": true
  },
  "fullText": "MASTER SERVICES AGREEMENT\n\nThis Agreement...",
  "pages": [
    {
      "pageNum": 1,
      "text": "...",
      "headings": [{ "text": "RECITALS", "level": 1 }]
    }
  ],
  "structure": {
    "headings": [...],
    "clauses": [...],
    "definitions": [{ "term": "Confidential Information", "definition": "...", "page": 3 }],
    "tables": [...],
    "schedules": [{ "title": "Schedule 1 — Services", "page": 20 }]
  },
  "extractionMode": "text-layer",
  "qualityRating": "excellent",
  "warnings": []
}
```

## Critical design principles

### PII handling
Before the extracted text is sent to any LLM or RAG system, apply PII detection and — where required by firm policy or user consent settings — redact sensitive personal information. See [[safety-pii-redaction-before-rag]] for the redaction pipeline.

This is mandatory, not optional, for:
- Client-uploaded documents
- Documents containing national IDs, passport numbers, financial account details
- Medical or HR documents

### Page mapping preservation
Every text segment must carry its page number. This allows downstream skills to produce citations like "Clause 14.2 (p. 8)" rather than "somewhere in the document." Loss of page mapping is an anti-pattern — it undermines the tool's core value for legal work.

### Large file handling
Documents over 100 pages should be processed in 25-page batches to avoid memory exhaustion. Re-assemble results after all batches complete.

### Anti-patterns to avoid

| Anti-pattern | Why it's bad |
|---|---|
| Sending raw PDF bytes to LLM | Wastes context window; LLMs are not PDF parsers |
| OCR'ing a PDF that has a text layer | Slower; lower quality than native text |
| Stripping page boundaries | Makes citation impossible downstream |
| Ignoring language detection | Sends Arabic to English OCR → garbled output |
| Merging multi-language pages | Loses RTL/LTR context switching |

## Language detection

Before choosing extraction mode or OCR engine:
1. Extract a sample text block from the first page
2. Run language detection (langdetect or equivalent)
3. If Arabic → flag for RTL handling and OCR routing to [[tool-ocr-arabic]]
4. If French → flag for French-language RAG and analysis downstream
5. If mixed → note which pages are in which language

## Multi-language documents (common in MENA)

Many MENA legal documents are bilingual Arabic/English or Arabic/French. Handling:
- Extract each page separately
- Tag each page with its dominant language
- For interleaved bilingual text: split into language-tagged blocks
- Return a `bilingualSections` field indicating which pages are in which language
- Route each section to the appropriate downstream analysis tool

## Failure modes

| Failure | Symptom | Resolution |
|---------|---------|------------|
| Encrypted / password-protected | Error on open | Ask user to remove password; cannot extract |
| Corrupted PDF | Partial extraction / errors | Try alternative library (pdfminer fallback); warn user |
| Text layer garbage (font encoding error) | Gibberish characters | Try pdfminer with encoding detection; fall back to OCR |
| Scanned document mis-detected as text | Low-quality garbage text | Check chars-per-page threshold; trigger OCR fallback |
| Very large file (>500 pages) | Memory timeout | Chunk into 25-page batches; reassemble |
| Complex XFA forms | No text extracted | XFA requires dedicated form extractor; inform user |

## Related skills

- [[tool-ocr-arabic]] — OCR fallback for Arabic-language scanned pages
- [[tool-ocr-english]] — OCR fallback for English-language scanned pages
- [[multimodal-scanned-pdf-handler]] — higher-level orchestrator that routes scan types
- [[safety-pii-redaction-before-rag]] — apply before any LLM or RAG use of extracted text
- [[tool-rag-firm-knowledge]] — extracted text is indexed here for firm KB
