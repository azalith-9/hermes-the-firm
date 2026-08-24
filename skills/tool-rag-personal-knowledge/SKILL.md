---
name: tool-rag-personal-knowledge
description: Use when retrieving from an individual user's personal knowledge store — documents they have personally uploaded, notes they have taken, or matter-linked files associated with their account. Distinct from the firm-wide knowledge base (which is shared across the tenant) and from the public legal corpus. Invoked when a user refers to something they personally uploaded or when context suggests a personal document is relevant.
license: MIT
metadata: " id: tool.RAG-personal-knowledge category: tool jurisdictions: [__multi__] priority: P2 intent: [personal-kb, uploaded-docs, user-notes, personal-context] related: [tool-rag-firm-knowledge, tool-rag-public-legal-corpus, tool-pdf-extractor, safety-client-confidentiality-cross-tenant] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'tool'.
Namespaced as louis-<category>-<skill> on registration.
-->


# RAG — Personal Knowledge

## What it does

This tool performs retrieval-augmented generation against an individual user's personal knowledge store — a per-user embedding store that holds documents the user has personally uploaded, notes they have taken, and matter-linked files they have associated with their account.

This is distinct from:
- **Firm KB** ([[tool-rag-firm-knowledge]]): shared across the whole tenant, curated as authoritative precedents — higher precedence
- **Public legal corpus** ([[tool-rag-public-legal-corpus]]): indexed public statutes and judgments — lowest precedence

Personal KB is for the user's own working documents: a draft they uploaded for review, a research note they saved from a previous session, a client briefing document they want to refer back to.

## When to invoke

### Explicit signals
- "Earlier I uploaded a document about..."
- "I saved a note on force majeure clauses last week"
- "Use the draft I uploaded"
- "The term sheet I gave you earlier"

### Implicit signals
- User refers to "my document", "my draft", "my notes"
- The query context suggests a personal upload is relevant (user mentioned uploading something during onboarding or in a prior turn)

### Do not invoke
- When the firm-level KB clearly covers the request (firm KB takes precedence)
- For general legal knowledge (no personal context is needed)
- For first-session users who have not uploaded anything

## Storage architecture

- Each user has a dedicated per-user embedding store, isolated from other users in the same tenant
- The user's store is also isolated from the tenant-level firm KB — documents uploaded to personal KB do not automatically become firm KB documents
- **Promotion to firm KB**: a user with the appropriate permission level (partner, knowledge manager) can explicitly promote a personal document to the firm KB, at which point it enters the firm ingest pipeline

## Retrieval rules

### Isolation
Every query is scoped to:
1. `tenant_id` — hard constraint (same as firm KB)
2. `user_id` — hard constraint (personal documents are user-private)

A user cannot retrieve another user's personal documents, even within the same tenant, unless the document has been explicitly shared.

### Filter sequence
```
1. tenant_id + user_id (both mandatory)
2. document_type (if specified)
3. matter_id (if matter context is active)
4. date range (if user specifies "something from last month")
5. Embedding similarity (top-K, threshold 0.72)
```

### Precedence
If both personal KB and firm KB return results for the same query:
1. Firm KB results are presented first (authoritative precedent)
2. Personal KB results are presented as "also in your personal documents"
3. The user decides which to use

## Document lifecycle

| Stage | Action |
|-------|--------|
| Upload | User uploads PDF/DOCX → [[tool-pdf-extractor]] → embedded → stored in personal store |
| Session reference | Tool retrieves relevant passages during active session |
| Retention | Documents retained per tenant data-retention policy (default: 1 year) |
| Deletion | User can delete individual documents from their personal store |
| Promotion | With appropriate permission: promote to firm KB via ingest pipeline |

## Privacy and security

- Personal documents are user-private by default; not accessible to firm administrators without explicit consent except for audit/compliance purposes
- Documents containing PII should be tagged at upload; [[safety-pii-redaction-before-rag]] applies before LLM processing
- For users on shared devices or shared sessions, remind them to log out — personal KB is tied to the session user
- Tenants in regulated industries (banks, law firms subject to attorney-client privilege) should configure the retention and sharing policy to comply with data protection obligations

## Citations

Retrieved personal KB passages are cited as:
- `[Personal KB: <filename> §<section>]`
- Example: `[Personal KB: Acme-draft-MSA-v2.docx §14.2]`

## Output schema

```json
{
  "results": [
    {
      "documentName": "Acme-draft-MSA-v2.docx",
      "documentType": "MSA",
      "section": "14.2",
      "text": "...",
      "similarity": 0.87,
      "uploadedAt": "2026-05-10",
      "userId": "user-xyz",
      "citation": "[Personal KB: Acme-draft-MSA-v2.docx §14.2]"
    }
  ],
  "totalResults": 2,
  "tenantId": "tenant-xyz",
  "userId": "user-xyz",
  "queryTimestamp": "2026-05-14T10:00:00Z"
}
```

## Related skills

- [[tool-rag-firm-knowledge]] — firm-wide knowledge base; higher precedence; shared across tenant
- [[tool-rag-public-legal-corpus]] — public legal corpus; lowest precedence; jurisdictionally indexed
- [[tool-pdf-extractor]] — PDF text extraction that feeds documents into this store
- [[safety-client-confidentiality-cross-tenant]] — cross-tenant isolation policy
