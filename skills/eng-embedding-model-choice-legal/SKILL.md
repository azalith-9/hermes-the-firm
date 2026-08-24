---
name: eng-embedding-model-choice-legal
description: Use when selecting an embedding model for semantic search, document similarity, or retrieval-augmented generation (RAG) in a legal AI product. Covers the criteria specific to legal text (multilingual Arabic/English, domain vocabulary, long-document chunking), a comparison of leading embedding models, and configuration recommendations for legal retrieval pipelines serving MENA and common-law jurisdictions.
license: MIT
metadata: " id: eng.embedding-model-choice-legal category: eng jurisdictions: [__multi__] priority: P2 intent: [embeddings, RAG, semantic-search, vector-database, multilingual] related: - eng-context-cache-key-design - eng-fallback-model-cascade - eng-langfuse-eval-runner - eng-mcp-tool-registry source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'eng'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Embedding Model Choice — Legal

## What it does

Embedding models convert text into dense vector representations that enable semantic search: "find documents that are conceptually similar to this query, even if they don't share keywords." In legal AI products, embeddings power:
- Precedent retrieval (find the most similar prior NDA to the current draft)
- KB search (retrieve the most relevant knowledge-base document for this user query)
- Conflict-check similarity (find matters involving conceptually similar parties or issues)
- Document classification (identify the document type from its content)

The choice of embedding model has a large impact on retrieval quality. Legal text is domain-specific, often multilingual (Arabic + English in MENA), and involves long documents. Generic models trained on web text perform poorly on legal vocabulary without fine-tuning or careful chunking.

## Key selection criteria for legal text

| Criterion | Why it matters for legal |
|---|---|
| Multilingual quality (AR + EN) | MENA contracts are often bilingual; queries in Arabic must retrieve English documents and vice versa |
| Max input length | Contracts can exceed 10,000 tokens; short-context models require aggressive chunking that loses clause context |
| Domain vocabulary | Legal terms ("indemnification", "escrow", "قضاء", "تعويض") must be represented precisely |
| Embedding dimension | Higher dimensions → more expressive but higher storage/compute cost |
| Cost per token | Embedding all firm documents is a large one-time and recurring cost |
| Latency | Real-time search requires low embedding latency; batch indexing can tolerate higher latency |
| Data privacy | Some models require sending text to a third-party API; sensitive legal documents may require local/self-hosted models |

## Model comparison

| Model | Max tokens | Dimensions | Multilingual AR | Notes |
|---|---|---|---|---|
| `text-embedding-3-large` (OpenAI) | 8191 | 3072 (configurable) | Good | Strong general legal performance; high cost at scale |
| `text-embedding-3-small` (OpenAI) | 8191 | 1536 | Good | Lower cost; slight quality trade-off |
| `voyage-law-2` (Voyage AI) | 16000 | 1024 | Moderate | Specifically trained on legal text; best English legal recall |
| `voyage-multilingual-2` (Voyage AI) | 32000 | 1024 | Strong | Best multilingual option tested on AR-EN legal text |
| `jina-embeddings-v3` (Jina AI) | 8192 | 1024 | Strong | Open-weights available; good AR support; self-hostable |
| `e5-mistral-7b-instruct` (Microsoft) | 4096 | 4096 | Moderate | Open weights; good legal quality if fine-tuned |
| `multilingual-e5-large` | 514 | 1024 | Strong | Short context limit; requires chunking; good AR quality |

**Recommendation for MENA legal AI**:
- Primary: `voyage-multilingual-2` for AR+EN retrieval; or `voyage-law-2` for English-only legal retrieval.
- Privacy-sensitive deployments: `jina-embeddings-v3` (self-hostable) or `multilingual-e5-large` (self-hostable).
- Cost-sensitive: `text-embedding-3-small` with 1536 dimensions reduced to 256–512 (OpenAI supports dimension reduction via MRL training).

## Chunking strategy for legal documents

Legal documents require jurisdiction-aware chunking:

### Fixed-window chunking (simplest, weakest)

Split at N tokens with K-token overlap. Loses clause structure. Use only for short documents.

### Semantic / structure-aware chunking (recommended)

Split at structural boundaries:
1. **Headings**: split at H1/H2/H3 (contract sections, article numbers).
2. **Clause boundaries**: each numbered clause is a chunk candidate.
3. **Paragraph boundaries**: fallback if clause structure is not present.

For contracts with defined-term sections: embed the definitions chunk as a prefix to every subsequent chunk that uses those terms (increases retrieval precision for clause-level queries).

### Hierarchical chunking (best for long contracts)

Embed at two granularities:
- **Document level**: one embedding per document, summarizing the whole.
- **Clause level**: one embedding per clause.

On retrieval: first match at document level (coarse), then re-rank at clause level (fine). This two-stage retrieval is more accurate and cheaper for large corpora.

## Metadata to store alongside embeddings

In the vector database, store these fields alongside each chunk's embedding:

```json
{
  "chunk_id": "ulid",
  "document_id": "doc_xxx",
  "matter_id": "matter_xxx | kb_doc",
  "org_id": "org_xxx",
  "document_type": "NDA | SPA | Opinion | ...",
  "jurisdiction": "UAE | DIFC | KSA | ...",
  "governing_law": "UAE | English | ...",
  "language": "en | ar | bilingual",
  "section_title": "Article 5 — Indemnification",
  "chunk_index": 3,
  "total_chunks": 12,
  "approved_at": "ISO-8601",
  "access_tier": "firm-wide | practice | partner-only"
}
```

Use metadata filters on retrieval to enforce access control — never return a chunk to a user who lacks access to the parent document.

## Access control on retrieval

The embedding search pipeline must enforce tenant and document-access controls:

1. Apply `org_id = current_org` filter to every query — never allow cross-tenant retrieval.
2. Apply `access_tier IN (user's_permitted_tiers)` filter.
3. For matter-specific documents: apply `matter_id = current_matter OR matter_id = 'kb_doc'`.

These filters must be applied at the vector database query layer, not post-retrieval in application code.

## Evaluation

Evaluate embedding model quality on a legal domain test set using:
- **NDCG@10**: ranking quality of retrieved results.
- **Recall@5**: were the 5 most relevant documents retrieved?
- **MRR**: mean reciprocal rank of the first relevant result.

Use Langfuse (see [[eng-langfuse-eval-runner]]) to run systematic retrieval quality evaluations with legal practitioner-curated test cases.

## Related skills

- [[eng-context-cache-key-design]]
- [[eng-fallback-model-cascade]]
- [[eng-langfuse-eval-runner]]
- [[eng-mcp-tool-registry]]
