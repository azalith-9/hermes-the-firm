---
name: eng-supabase-index-knowledge-pipeline
description: Use when building or maintaining the pipeline that ingests legal knowledge (uploaded contracts, legislation, regulatory guidance) into the Supabase pgvector index used by the RAG retrieval system. Covers the full flow from document upload through text extraction, chunking, embedding, and vector storage, with multi-tenant isolation and audit logging.
license: MIT
metadata: " id: eng.supabase-index-knowledge-pipeline category: eng jurisdictions: [__multi__] priority: P2 intent: [__eng__, supabase, vector, rag, knowledge-base, embedding] related: [eng-rag-chunking-rules-legal-docs, eng-pii-redaction-preprocessor, eng-tenant-isolation-row-level-security, eng-supabase-edge-functions-patterns] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'eng'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Supabase Index Knowledge Pipeline

## What it does

The index knowledge pipeline is the end-to-end process that takes a raw document (PDF, DOCX, text) uploaded by a legal user and turns it into searchable vector embeddings stored in Supabase with `pgvector`. When a user asks a question about "our standard supplier NDA" the retrieval system queries these embeddings to find the relevant clauses and passes them to the LLM as context.

The pipeline must be reliable, tenant-isolated, and auditable because it processes client-confidential legal documents.

## Setup / auth

Supabase prerequisites:
```sql
-- Enable pgvector extension
CREATE EXTENSION IF NOT EXISTS vector;

-- Documents table
CREATE TABLE documents (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id UUID NOT NULL REFERENCES workspaces(id),
  uploaded_by UUID NOT NULL REFERENCES auth.users(id),
  filename TEXT NOT NULL,
  doc_type TEXT NOT NULL,    -- 'contract' | 'legislation' | 'judgment' | 'kb'
  language TEXT NOT NULL,
  status TEXT NOT NULL DEFAULT 'pending',   -- 'pending' | 'indexing' | 'ready' | 'error'
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  indexed_at TIMESTAMPTZ
);

-- Chunks table with vector column
CREATE TABLE document_chunks (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  doc_id UUID NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
  tenant_id UUID NOT NULL,
  chunk_index INT NOT NULL,
  chunk_type TEXT,
  heading_text TEXT,
  content TEXT NOT NULL,
  embedding VECTOR(1536),    -- OpenAI text-embedding-3-small dimensions
  metadata JSONB,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Index for fast ANN search
CREATE INDEX ON document_chunks USING ivfflat (embedding vector_cosine_ops)
  WITH (lists = 100);

-- RLS
ALTER TABLE documents ENABLE ROW LEVEL SECURITY;
ALTER TABLE document_chunks ENABLE ROW LEVEL SECURITY;

CREATE POLICY "tenant isolation documents"
  ON documents FOR ALL
  USING (tenant_id = (SELECT workspace_id FROM memberships WHERE user_id = auth.uid()));

CREATE POLICY "tenant isolation chunks"
  ON document_chunks FOR ALL
  USING (tenant_id = (SELECT workspace_id FROM memberships WHERE user_id = auth.uid()));
```

## Capabilities

### Pipeline stages

```
Upload → Extract → Redact → Chunk → Embed → Store → Index-ready
```

1. **Upload** — file lands in Supabase Storage bucket `documents/{tenantId}/{docId}`. File size limit: 20 MB. Accepted types: PDF, DOCX, TXT.
2. **Extract** — trigger: `storage.objects.insert` webhook → Edge Function `process-document`. Extract raw text using `pdf-parse` or `mammoth`.
3. **Redact** — call [[eng-pii-redaction-preprocessor]] with `mode: "hash"`. Store audit log.
4. **Chunk** — apply [[eng-rag-chunking-rules-legal-docs]] rules. Produce `Chunk[]` with metadata.
5. **Embed** — batch-call the embedding API (OpenAI `text-embedding-3-small` or Cohere `embed-multilingual-v3`). Batch size: 100 chunks per call. For Arabic text, prefer Cohere multilingual or a model trained on Arabic data.
6. **Store** — bulk insert into `document_chunks`. Update `documents.status = 'ready'` and `indexed_at`.
7. **Notify** — emit PostHog event `document_indexed`; send in-app notification to uploader.

### Embedding model selection

| Language | Recommended model | Dimension |
|---|---|---|
| English | `text-embedding-3-small` | 1536 |
| Arabic | `embed-multilingual-v3` (Cohere) | 1024 |
| French | `text-embedding-3-small` | 1536 |
| Mixed | `embed-multilingual-v3` (Cohere) | 1024 |

For mixed-language corpora, standardize on the multilingual model across all languages to ensure cosine similarity is comparable across chunks.

### Retrieval query pattern

```typescript
async function retrieveRelevantChunks(
  query: string,
  tenantId: string,
  docIds?: string[],
  topK: number = 5
): Promise<Chunk[]> {
  const embedding = await embed(query);

  const { data } = await supabase.rpc("match_chunks", {
    query_embedding: embedding,
    tenant_id: tenantId,
    doc_ids: docIds ?? null,
    match_count: topK,
  });
  return data;
}
```

SQL function `match_chunks`:
```sql
CREATE FUNCTION match_chunks(
  query_embedding VECTOR(1536),
  tenant_id UUID,
  doc_ids UUID[],
  match_count INT
) RETURNS TABLE(id UUID, content TEXT, heading_text TEXT, metadata JSONB, similarity FLOAT)
LANGUAGE SQL AS $$
  SELECT id, content, heading_text, metadata,
         1 - (embedding <=> query_embedding) AS similarity
  FROM document_chunks
  WHERE document_chunks.tenant_id = match_chunks.tenant_id
    AND (doc_ids IS NULL OR doc_id = ANY(doc_ids))
  ORDER BY embedding <=> query_embedding
  LIMIT match_count;
$$;
```

## Usage patterns

### Triggering reindex

If a document's chunks need to be refreshed (e.g., PII hash key rotated):
```typescript
await supabase.functions.invoke("reindex-document", { body: { docId, tenantId } });
```

This deletes existing chunks (`ON DELETE CASCADE` handles it via the document delete + reinsert) and reruns from the extract step.

### Incremental knowledge base updates (legislation)

For system-wide knowledge (legislation, regulatory guidance) that is not tenant-specific:
- Store in a dedicated `system_chunks` table with `tenant_id = null`.
- Apply a separate RLS policy: `system_chunks` are readable by all authenticated users.
- Update on a weekly cron (see scheduled tasks).

## Permissions & safety

- Raw (pre-redaction) text must never be written to any database table.
- Storage bucket `documents/` must have RLS; only the owning tenant can read their files.
- Embedding API calls must not include document metadata fields that contain PII (filename may contain party names — hash it before logging).
- The `pii_audit_log` entry must be written before the chunk insert, not after. If chunking fails, the audit log still proves redaction ran.

## Failure modes

| Failure | Impact | Mitigation |
|---|---|---|
| PDF text extraction returns empty | Zero chunks indexed; document silently not searchable | Validate extracted text length > 100 chars; set `status = 'error'` and notify user |
| Embedding API rate limit | Batch fails mid-way | Retry with exponential backoff; store last successful chunk index for resumption |
| Vector dimension mismatch | Insert fails | Validate embedding dimension against table definition before insert |
| Large doc > 20 MB | Upload rejected | Enforce client-side size limit; suggest splitting document |
| RLS misconfigured | Cross-tenant chunk retrieval | Integration test: verify that tenant B cannot retrieve tenant A's chunks |

## Related skills

- [[eng-rag-chunking-rules-legal-docs]] — produces the chunks this pipeline stores
- [[eng-pii-redaction-preprocessor]] — runs before chunking in this pipeline
- [[eng-tenant-isolation-row-level-security]] — RLS policies applied to documents and chunks tables
- [[eng-supabase-edge-functions-patterns]] — the Edge Function patterns used by this pipeline
