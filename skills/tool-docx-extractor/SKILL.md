---
name: tool-docx-extractor
description: Use when parsing a Microsoft Word (.docx) file to extract text and structure for downstream AI analysis — contract review, redline comparison, summarisation, or data extraction. Supports four extraction modes (plain text, structured Markdown, HTML, tracked-changes). Preserves tracked changes, comments, footnotes, and tables separately. Built on the mammoth library with fallback docx parsing. Critical for contract review and document-workspace pipelines.
license: MIT
metadata: " id: tool.docx-extractor category: tool priority: P0 intent: [docx extract, parse docx] related: [tool-e-signature-orchestrator, review-contract-risk, pa-workflow-due-diligence, multimodal-document-ingestion] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'tool'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Tool — DOCX Extractor

## What it does

Extracts text and document structure from Microsoft Word (.docx) files for use in Louis's AI analysis pipelines. Handles the full complexity of legal documents — tracked changes (redlines), comments, footnotes, embedded tables, and complex numbering — without losing information that matters for legal review.

## Setup / auth

No external auth required. The extractor runs server-side using the `mammoth` Node.js library as the primary engine, with a fallback `docx` library for edge cases.

**Library stack:**
- **Primary:** `mammoth` — chosen for its robust handling of complex DOCX structure, tracked changes, and clean Markdown output
- **Fallback:** `docx` library for structural edge cases or when mammoth output requires supplementation
- Both libraries run in the Louis backend; no client-side processing of sensitive documents

## Extraction modes

| Mode | Output | When to use |
|---|---|---|
| **Plain text** | Raw text string, no formatting | Fastest; for feeding into LLM prompt context where structure is not critical |
| **Structured Markdown** | Headings, bold/italic, bullet lists, tables as Markdown | Primary mode for contract analysis; preserves clause hierarchy |
| **HTML** | Full HTML for browser rendering | For document workspace UI display |
| **Tracked changes** | Accept/reject view + change history with author and date | Essential for redline workflows; negotiation review |

## Extraction components

### Core text extraction

- Headings mapped to `#`, `##`, `###` (Markdown mode) — preserves clause numbering where styled
- Bold / italic / underline preserved in Markdown
- Lists (ordered and unordered) maintained
- Tables extracted as Markdown tables

### Tracked changes

Tracked changes in DOCX format (`.docx` revision marks) are extracted as:
```
{type: "insertion", author: "Partner A", date: "2026-04-10", text: "...inserted text..."}
{type: "deletion", author: "Associate B", date: "2026-04-11", text: "...deleted text..."}
```

**Critical:** Do not discard tracked changes. Legal redline workflows depend on being able to see what changed, who changed it, and when. Losing tracked changes is the primary anti-pattern for this tool.

### Comments

Comments (annotations) are extracted separately from the main text body:
```
{commentId: "c1", author: "GC", date: "2026-04-12", anchorText: "...quoted text...", commentBody: "Reject this clause"}
```

Comments are passed to the AI review pipeline as a separate annotation stream — they should not be treated as inline text.

### Footnotes and endnotes

Extracted and numbered; linked to their anchor position in the main text. Important for agreements where definitions, governing law, or exclusions appear in footnotes.

### Tables

Tables are extracted in structured form (row-column arrays) and rendered as Markdown tables. For tables embedded in schedules (e.g., pricing schedules, IP licence scope tables), the table structure is preserved rather than flattened to text.

### Embedded images

- Alt text extracted if present
- Images stored as separate binary blobs referenced by their anchor in the text
- OCR of images not performed by default; flag if image contains legally material text

## API integration

The extractor is used by:
- **Doc workspace `/content` endpoint:** `GET /api/doc-workspace/:docId/content?mode=markdown`
- **Chat tool `read_document`:** Fetches document content for LLM context
- **Contract review pipeline:** Structured mode feeds clause-by-clause analysis

## Output schema

```json
{
  "mode": "structured",
  "metadata": {
    "wordCount": 4521,
    "pageCount": 18,
    "author": "Baker & Partners LLP",
    "lastModified": "2026-04-15T14:30:00Z",
    "hasTrackedChanges": true,
    "commentCount": 7
  },
  "body": "# Share Purchase Agreement\n\n## 1. Definitions\n\n**\"Completion Date\"** means...",
  "trackedChanges": [...],
  "comments": [...],
  "footnotes": [...],
  "tables": [...]
}
```

## Anti-patterns — what not to do

- **Losing tracked-change history:** Always extract tracked changes; never silently accept or reject them before analysis.
- **Treating comments as inline text:** Comments are annotations, not part of the agreement text. Mixing them confuses the AI analysis.
- **Flattening tables:** Tables in schedules contain structured data; flatten only as a last resort.
- **Ignoring footnotes:** Governing law clauses, warranties, and material exclusions appear in footnotes in many MENA and UK agreements.
- **Processing in browser:** Do not expose DOCX parsing to the client side; sensitive document content must stay server-side.

## Failure modes

| Failure | Response |
|---|---|
| Password-protected DOCX | Return error with instruction to remove password protection |
| Corrupted DOCX | Attempt fallback library; if still failing, return partial extraction with explicit warning |
| Unsupported content (macros, embedded OLE) | Extract text content only; flag that embedded objects were skipped |
| Very large file (>50MB) | Chunk extraction; process in sections to avoid memory limits |
| Arabic RTL text | mammoth handles RTL; verify Unicode direction markers are preserved |

## Related skills

- [[tool-e-signature-orchestrator]]
- [[review-contract-risk]]
- [[pa-workflow-due-diligence]]
- [[multimodal-document-ingestion]]
