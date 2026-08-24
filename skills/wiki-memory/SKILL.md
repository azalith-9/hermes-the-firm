---
name: wiki-memory
description: Use when designing, building, or discussing the memory architecture for a legal-AI agent — including user memory (persistent preferences and context), agent memory (matter-level state, cross-session recall), embedding stores for RAG, recall and forget controls, and the privacy obligations that govern what may be retained. Reach for this skill when the user asks about AI agent memory, persistent context, embedding-based recall, or user data retention design for a legal-AI product.
license: MIT
metadata: " id: wiki.memory category: wiki jurisdictions: [UAE, KSA, DIFC, ADGM, __multi__] priority: P3 intent: [__wiki__, agent-memory, user-memory, embedding-store, RAG, recall, privacy] related: [wiki-data, wiki-engineering, wiki-haqq-product, wiki-frontend] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'wiki'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Agent Memory Architecture for Legal-AI

## Scope

This pack covers the memory design for a legal-AI agent: how the agent retains and recalls context about the user, the matter, and previous interactions; how embedding-based retrieval augments generation; and how recall and forget controls are implemented to meet both usability and privacy requirements. This is a design reference for engineers and product managers building persistent-context AI features.

---

## Memory types

A legal-AI agent needs at least three distinct memory layers:

### 1. In-context memory (conversation window)

The current conversation's messages sent to the LLM in the prompt. This is ephemeral — it exists only for the current session. The LLM has access to everything in the context window.

**Limits**: Context windows are finite (even 200 k-token contexts fill up for long document review sessions). Content must be managed: summarise earlier turns, drop low-value history, or chunk and retrieve.

**Legal-AI consideration**: Privilege and confidentiality attach to in-context content. The context window that includes client communications should never be logged in a form accessible to the AI vendor outside the contracted data processing agreement.

### 2. User memory (persistent preferences and profile)

Facts about the user that should persist across sessions, without needing to be re-provided:
- Default jurisdiction(s)
- Preferred language (Arabic/English)
- Practice area(s)
- Firm name and role
- Frequently used skill types
- Preferred output format (summary first vs full draft first)

**Storage**: A structured record in the operational database, updated when the user explicitly sets a preference or when the agent infers a stable preference with high confidence.

**Privacy note**: User memory is personal data under MENA data protection frameworks. Users must be able to view and delete their profile at any time. See [[wiki-data]] for the database design and [[wiki-geopolitics]] for jurisdiction-specific requirements.

### 3. Matter memory (per-matter persistent state)

State that persists across sessions for a specific legal matter:
- Parties, key dates, governing law
- Documents uploaded and their extracted metadata (parties, clause types, risk flags)
- Conversation history for the matter (summarised as the matter progresses)
- Pending action items and flags raised by the agent

**Storage**: A per-matter record and a vector store (see below) for document embeddings.

**Legal-AI consideration**: Matter memory is professional work product. The user should be able to export it (for portability), delete it (for matter closure), and restrict access to it (for conflict screening — a colleague at the same firm should not automatically see another lawyer's matter memory).

---

## Embedding stores and RAG

Retrieval-Augmented Generation (RAG) uses a vector store to retrieve relevant document chunks at query time and inject them into the LLM's context. This is the primary mechanism for a legal-AI agent to "know" the contents of documents larger than the context window.

### Design decisions

**Chunking strategy**: Legal documents have natural structural units (clauses, articles, sections). Prefer semantic chunking (by clause boundaries) over fixed-size chunking for legal text. Fixed-size chunks split clauses in the middle and destroy the meaning of cross-reference ("as defined in Clause 5.2...").

**Embedding model**: Use a model with strong multilingual (EN/AR) performance. OpenAI `text-embedding-3-small` or Cohere `embed-multilingual-v3.0` are reasonable choices as of 2026; verify current benchmarks.

**Metadata on each embedding**: `document_id`, `chunk_index`, `section_label`, `jurisdiction`, `matter_id`, `workspace_id`, `created_at`, `model_version`. All retrieval queries must filter on `workspace_id` — cross-workspace contamination is a critical failure mode.

**Re-embedding on model change**: when the embedding model is updated, all stored embeddings must be regenerated. Schedule this as a background job and do not query the store during migration.

### Retrieval patterns

- **Semantic search**: find chunks most semantically similar to the query (cosine similarity on embeddings)
- **Hybrid search**: combine semantic similarity with keyword/BM25 match; effective for exact clause references ("article 12.3")
- **Filtered retrieval**: semantic search within a filtered subset (e.g. only documents in a specific matter, or only documents with `jurisdiction = DIFC`)

---

## Recall and forget controls

### Recall controls

Users should be able to:
- View their user memory profile (what the agent knows about them)
- Edit any field in their profile
- Export all matter memory for a given matter
- Search their conversation history across matters

### Forget controls

Users should be able to:
- Delete a specific memory item ("forget that I prefer formal tone")
- Clear all memory for a closed matter
- Delete their account (which triggers deletion of all associated memory, documents, and embeddings)

**Retention policy**: define per-workspace and per-plan. Legal-grade accounts may need to retain matter records for a minimum period (bar association rules in some jurisdictions require retention of client files for a defined period after matter close — typically 5–10 years). The system should enforce this minimum and prevent premature deletion of regulated records.

### Forget propagation

When a user deletes a document or matter:
1. Mark the operational record as deleted (soft delete)
2. Enqueue a background job to delete the associated embedding vectors from the vector store
3. Delete the associated encrypted blob from object storage
4. Log the deletion event in the audit log (the audit log record itself is retained per the audit log retention policy)

---

## Privacy and data minimisation

Memory systems are a privacy risk surface. Apply data minimisation:
- Do not infer and store facts about the user that were not explicitly provided or highly confidently observed ("user mentioned they are a DIFC lawyer" should be stored; "user seems to be a senior partner" should not unless confirmed)
- Do not store raw conversation text in user memory — store structured facts extracted from it
- Apply the principle of least privilege: the agent reads user memory at session start; it does not have unrestricted access to all stored facts at all times

Under UAE PDPL, KSA PDPL, and DIFC/ADGM data protection frameworks, users have a right of access (to see what data is held) and a right to erasure (subject to any applicable retention obligations). The memory system must be able to respond to these requests within the regulatory timeframe.

---

## Caveats & currency

Vector store technology and embedding models are evolving rapidly. The chunking, embedding, and retrieval patterns described here represent good practice as of early 2026; the field is moving. Privacy law requirements for AI-derived user profiles (including memory derived from usage behaviour) are not yet settled in MENA jurisdictions; verify with current legal counsel before storing inferred user attributes.

---

## Related skills

- [[wiki-data]]
- [[wiki-engineering]]
- [[wiki-haqq-product]]
- [[wiki-frontend]]
