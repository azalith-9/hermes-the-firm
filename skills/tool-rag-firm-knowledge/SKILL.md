---
name: tool-rag-firm-knowledge
description: Use when drafting or reviewing a document and the firm's own precedents, playbooks, or prior work product should inform the output. Retrieves semantically similar passages from the e-firm tenant's internal knowledge base — NDA templates, MSA playbooks, prior transaction documents, and firm-specific positions — with hard tenant isolation. Invoked explicitly ("use our NDA template") or implicitly when drafting work exists in the firm's KB. The firm KB is always preferred over public templates or model defaults.
license: MIT
metadata: " id: tool.RAG-firm-knowledge category: tool priority: P0 intent: [firm-kb, internal-precedent, playbook, rag-retrieval] related: [tool-rag-personal-knowledge, tool-rag-public-legal-corpus, tool-pdf-extractor, safety-client-confidentiality-cross-tenant] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'tool'.
Namespaced as louis-<category>-<skill> on registration.
-->


# RAG — Firm Knowledge Base

## What it does

This tool performs retrieval-augmented generation (RAG) against the e-firm tenant's internal knowledge base — the collection of precedents, playbooks, templates, model clauses, and prior work product that the firm has uploaded and indexed. When this tool returns results, they are always preferred over generic model knowledge or public legal corpus results, because firm-specific precedent reflects the firm's negotiated positions, house style, and jurisdiction-specific experience.

## When to invoke

### Explicit signals
- "Use our NDA template"
- "Follow the firm's MSA playbook"
- "How did we handle the indemnity clause in the Acme deal?"
- "What's our standard position on governing law?"
- "Draft like our last 3 SPAs"

### Implicit signals
- Any drafting task where the document type (NDA, MSA, SHA, SPA, Facility Agreement) is likely to have firm precedent
- Review tasks where the reviewer asks whether the counterparty's draft deviates from "our standard"
- Research tasks where the question is about the firm's internal policy or past advice

### Do not invoke
- For pure legal research questions (use [[tool-rag-public-legal-corpus]] or premium databases)
- For general legal concepts where no firm-specific nuance is expected
- When the user explicitly asks for a "generic" or "market standard" document

## Retrieval methodology

### Tenant isolation
Every retrieval is scoped to the `tenant_id` of the current session. Cross-tenant access is architecturally prohibited — see [[safety-client-confidentiality-cross-tenant]]. This is a hard constraint, not a soft preference. The embedding store is partitioned by tenant at the storage level.

### Filter sequence
```
1. tenant_id = current tenant (mandatory, non-negotiable)
2. document_type = [NDA | MSA | SPA | SHA | ...] (if known from context)
3. matter_id = current matter (if matter-isolation mode is on)
4. client = counterparty name (fuzzy)
5. jurisdiction = [KSA | UAE | LB | DIFC | ADGM | ...]
```

Filters are applied in order. Documents passing all applicable filters enter the similarity search pool.

### Embedding-based similarity
- Model: tenant-specific embedding (default: `text-embedding-3-large` or equivalent)
- Top-K: return top 5 most similar passages (configurable per tenant: 3–10)
- Relevance threshold: minimum cosine similarity of 0.75 (passages below this score are not returned)
- Re-ranking: after initial top-K retrieval, re-rank by:
  1. Recency (newer documents preferred — captures firm's evolving position)
  2. Matter similarity (same industry sector, same jurisdiction)
  3. Document type match

### Matter isolation configuration
By default:
- **Firm-level precedents and playbooks** are shared across all matters within the tenant (the firm curates these as authoritative templates)
- **Raw matter files** (drafts, correspondence, executed agreements) are isolated to the matter they belong to

A tenant can override this default to enforce stricter matter-level isolation (e.g., for Chinese walls between transaction teams).

## Citations

All retrieved passages must be cited in the output:
- Format: `[Firm KB: <document-name> §<section>]`
- Example: `[Firm KB: NDA-template-v3 §4.2 (Confidentiality Obligations)]`
- Do not quote verbatim passages longer than ~50 words — paraphrase and cite
- If a playbook clause is used verbatim in a draft, note it as "per Firm KB"

This citation discipline:
1. Allows users to verify the firm KB source directly
2. Creates an audit trail for risk management purposes
3. Surfaces when the firm KB is out of date (user can then update it)

## Update mechanism

New documents enter the firm KB through the ingest pipeline:
- **Source**: [[connector-supabase-index-knowledge]] (Supabase vector store ingest)
- **Metadata tracked per document**: document name, document type, version, created by, created date, last updated, matter/client tags, jurisdiction tags
- **Re-indexing**: when a document is updated, the old version is retained with a version tag; the new version becomes the default retrieval target unless a historical version is explicitly requested
- **Versioning**: `NDA-template-v1`, `NDA-template-v2`, etc. — the latest version is always the default

## Cross-matter restrictions (detailed)

| Configuration | Behavior |
|---|---|
| Default | Precedents: firm-shared. Raw matter files: matter-isolated |
| Strict isolation | All documents: matter-isolated. Team must explicitly tag for firm-wide sharing |
| Open sharing | All documents: firm-shared. Use with caution — conflicts-of-interest risk |

For ethical wall / Chinese wall compliance, strict isolation mode must be engaged for the relevant matters, and the wall must be documented in the matter management system.

## Quality and staleness flags

The tool flags retrieved documents when:
- Document was last updated more than 2 years ago → `[WARNING: Firm KB — this template is 2+ years old; verify currency]`
- Document jurisdiction does not match the current task's jurisdiction → `[NOTE: Firm KB — this precedent is for [X] law; current task is [Y] law]`
- Document type is a near-match but not exact → `[NOTE: Firm KB — closest match is [X]; no exact precedent found for [Y]]`

## Output schema

```json
{
  "results": [
    {
      "documentName": "NDA-template-v3",
      "documentType": "NDA",
      "section": "4.2",
      "heading": "Confidentiality Obligations",
      "text": "...",
      "similarity": 0.91,
      "lastUpdated": "2024-11-15",
      "jurisdiction": "DIFC",
      "matterId": null,
      "version": "v3",
      "citation": "[Firm KB: NDA-template-v3 §4.2]"
    }
  ],
  "totalResults": 3,
  "tenantId": "tenant-xyz",
  "queryTimestamp": "2026-05-14T10:00:00Z",
  "matterId": "matter-001"
}
```

## Related skills

- [[tool-rag-personal-knowledge]] — individual user's personal knowledge base (lower precedence than firm KB)
- [[tool-rag-public-legal-corpus]] — public legal corpus RAG for statute and case reference (always lower precedence than firm KB)
- [[tool-pdf-extractor]] — extracts text from PDFs before they are indexed into the firm KB
- [[safety-client-confidentiality-cross-tenant]] — the cross-tenant isolation policy this tool enforces
