---
name: eng-rag-chunking-rules-legal-docs
description: Use when implementing the document ingestion pipeline that splits legal texts into retrieval-optimized chunks for embedding and vector storage. Defines chunk-size targets, boundary rules, overlap strategy, and metadata tagging specific to the structure of legal documents (contracts, legislation, court decisions) across English, Arabic, and French.
license: MIT
metadata: " id: eng.RAG-chunking-rules-legal-docs category: eng jurisdictions: [__multi__] priority: P2 intent: [__eng__, rag, chunking, embedding, document-processing] related: [eng-pii-redaction-preprocessor, eng-supabase-index-knowledge-pipeline, eng-supabase-edge-functions-patterns, eng-tenant-isolation-row-level-security] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'eng'.
Registered as a flat plugin skill.
-->


# RAG Chunking Rules — Legal Documents

## What it does

Legal documents have a rigid hierarchical structure (Parts → Articles → Clauses → Sub-clauses) that generic text splitters destroy. Splitting a 200-word Article across two chunks means neither chunk contains the full legal proposition, guaranteeing poor retrieval. This skill defines the chunking strategy for the document ingestion pipeline so that retrieval returns complete, coherent legal units.

## Setup / auth

No separate auth. The chunker runs as part of the document ingestion pipeline, after PII redaction ([[eng-pii-redaction-preprocessor]]) and before embedding/storage ([[eng-supabase-index-knowledge-pipeline]]).

Dependencies: a PDF/DOCX text extractor (e.g., `pdf-parse`, `mammoth`), a boundary-detection function, and a vector DB insert (Supabase `pgvector`).

## Capabilities

### Chunk-size targets

| Document type | Target chunk size | Max | Overlap |
|---|---|---|---|
| Contract clause (short) | 300–500 tokens | 600 | 50 tokens |
| Contract clause (long) | 500–800 tokens | 1000 | 100 tokens |
| Legislative article | 200–600 tokens | 800 | 0 (articles are atomic) |
| Court judgment paragraph | 400–700 tokens | 900 | 80 tokens |
| Recital / preamble | Keep as single chunk | 500 | 0 |
| Definition section | Split by defined term | 200–400 | 0 |

Use token counts (cl100k_base or equivalent), not character counts. Character counts fail badly for Arabic (higher token density).

### Boundary detection rules — in priority order

1. **Article / Clause heading** — any line matching patterns such as `Article \d+`, `المادة \d+`, `Clause \d+`, `Section \d+`, `Article \d+` (French). Always start a new chunk at a heading boundary.
2. **Numbered paragraph** — `(\d+\.\d+)` or `(\d+)\.` at line start within an article. Sub-clauses ≥ 100 tokens get their own chunk; shorter sub-clauses are merged into the parent clause chunk.
3. **Double newline** — blank line between paragraphs in a judgment. Treat as a soft boundary: merge with next paragraph if combined length < target.
4. **Sentence boundary** (fallback only) — split at period + capitalized word only when a chunk would otherwise exceed the hard maximum. Never split within a sentence.

### Metadata to attach to every chunk

```typescript
interface ChunkMetadata {
  docId: string;            // UUID of parent document
  tenantId: string;         // firm/workspace UUID
  chunkIndex: number;       // 0-based sequence within doc
  chunkType: "clause" | "article" | "recital" | "definition" | "judgment_para" | "other";
  headingText?: string;     // nearest parent heading (e.g., "Article 7 — Confidentiality")
  pageNumber?: number;      // from PDF extractor
  language: "ar" | "en" | "fr" | "mixed";
  jurisdiction?: string;    // if detectable from doc metadata
  documentType: "contract" | "legislation" | "judgment" | "regulation" | "unknown";
  charStart: number;        // character offset in original text
  charEnd: number;
}
```

The `headingText` field is the single most important retrieval aid: it tells the LLM "this chunk is from Article 7 — Confidentiality" before the user even asks.

### Arabic-specific rules

- Arabic contracts number articles right-to-left in the source PDF but the text extraction linearizes them left-to-right. Detect Arabic headings with: `/^(المادة|البند|الفقرة)\s+\d+/`.
- Arabic legal text is denser (more information per token) than English. Use the smaller end of the target range.
- Mixed AR/EN contracts (Arabizi headers + English body): detect language per paragraph and tag `language: "mixed"`.
- Diacritics (tashkeel) inflate token counts but add no retrieval value. Strip before embedding; keep in stored raw text.

### Overlap strategy

- Use overlap only for contract clauses and judgment paragraphs — not for legislative articles (which are self-contained by design).
- Overlap is a trailing tail: append the last N tokens of chunk N to the start of chunk N+1. Do **not** repeat the heading — duplicate headings confuse rerankers.
- Never use overlap across article/clause heading boundaries. The heading itself acts as the semantic bridge.

## Usage patterns

### Basic pipeline

```typescript
async function ingestDocument(file: File, tenantId: string): Promise<void> {
  const rawText = await extractText(file);                          // PDF/DOCX → string
  const { redacted } = redactPII(rawText, { mode: "hash" });        // safety gate
  const chunks = chunkLegalDocument(redacted, {
    language: detectLanguage(redacted),
    documentType: classifyDocumentType(redacted),
  });
  const embeddings = await embedBatch(chunks.map(c => c.text));
  await storeChunks(chunks, embeddings, tenantId);
}
```

### `chunkLegalDocument` function contract

```typescript
function chunkLegalDocument(
  text: string,
  options: { language: "ar" | "en" | "fr" | "mixed"; documentType: string }
): Array<{ text: string; metadata: ChunkMetadata }>;
```

### Retrieval hint

When retrieving, always include `headingText` and `documentType` in the returned context so the LLM can attribute the source clause in its response.

## Permissions & safety

- Chunking must occur **after** PII redaction. Never embed PII.
- Each chunk's `tenantId` must be set before database insert; the RLS policy (see [[eng-tenant-isolation-row-level-security]]) enforces that only the owning tenant can retrieve it.
- Chunks of documents the user has not shared with the AI should never be returned by vector search. Apply a `WHERE tenant_id = current_tenant_id() AND doc_id = ANY($sharedDocs)` filter.

## Failure modes

| Failure | Impact | Mitigation |
|---|---|---|
| Over-large chunks | Retrieval returns too much irrelevant context; LLM loses focus | Hard-cap at max token count; recursive split if needed |
| Under-large chunks | Single clause split across multiple chunks; proposition incomplete | Merge short adjacent sub-clauses until target met |
| Missing headingText | LLM can't attribute source | Regex heading detection pass before chunking; fallback to page number |
| Arabic text not detected | Wrong tokenization | Run language detection before choosing chunk-size targets |
| Chunking PII before redaction | PII in vector store | Always run redaction first in pipeline |

## Related skills

- [[eng-pii-redaction-preprocessor]] — must run before chunking
- [[eng-supabase-index-knowledge-pipeline]] — stores the chunks and embeddings
- [[eng-tenant-isolation-row-level-security]] — RLS that scopes chunk retrieval
- [[eng-supabase-edge-functions-patterns]] — deployment pattern for the ingestion worker
