---
name: safety-client-confidentiality-cross-tenant
description: Use when verifying or explaining the cross-tenant data isolation guarantees that prevent one law-firm tenant's client data, documents, embeddings, and learned patterns from leaking to any other tenant. Covers the architectural implementation (storage-layer partitioning, row-level security, query enforcement), the operational rule for queries that reference other tenants, and the audit trail for cross-tenant administrative operations. Core to demonstrating GDPR/PDPL compliance and bar-rules confidentiality in multi-tenant legal AI deployments.
license: MIT
metadata: " id: safety.client-confidentiality-cross-tenant category: safety jurisdictions: [US, UK, LB, KSA, UAE, DIFC, ADGM, GCC, EU] priority: P0 intent: [safety, confidentiality, tenant-isolation, architecture, data-protection] related: - safety-bar-rules-confidentiality - safety-bar-rule-1-6-confidentiality-ai - safety-pii-redaction-before-rag - safety-client-data-retention-mena-rules - eng-tenant-isolation-row-level-security source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'safety'.
Registered as a flat plugin skill.
-->


# Cross-Tenant Confidentiality Isolation

## When to use this

This skill applies in any situation where the multi-tenant nature of the platform is relevant to confidentiality:
- A new tenant (law firm) asks how their data is kept separate from other firms.
- A compliance auditor asks for evidence that the platform prevents cross-tenant data leakage.
- A lawyer asks whether another firm could see their client work.
- An engineer needs to understand the isolation invariants before building a new retrieval feature.
- A data-protection assessment (DPIA) requires documentation of tenant isolation controls.

## The hard rule

**Data, documents, embeddings, citations, session history, and learned patterns from Tenant A must never be accessible to Tenant B, period.** This is not a preference or a best-effort goal — it is a hard architectural invariant whose violation would constitute a breach of multiple bar codes and data-protection laws simultaneously.

This applies even:
- When tenants are in the same geographic region.
- When the same lawyer has accounts under two different firms.
- When an administrative user acts across multiple tenants.
- When two tenants have similar matters or work in the same practice area.

## Architectural implementation

### Vector store (RAG retrieval)
- All document embeddings are stored with a `tenant_id` field.
- Every retrieval query is issued with a mandatory `tenant_id` filter.
- The filter is enforced at the **storage layer** (the vector database engine), not at the application layer. This means a misconfigured application query cannot bypass it — the storage engine rejects or ignores out-of-scope results.
- Tenant-specific few-shot examples and firm playbooks are loaded only when the authenticated session's `tenant_id` matches.

### Relational database (matter data, session history)
- Row-level security (RLS) policies are applied at the database level, keyed on `tenant_id`.
- Application queries that attempt to read rows outside the authenticated tenant's scope are rejected at the database boundary, not filtered after retrieval.
- See [[eng-tenant-isolation-row-level-security]] for the RLS schema and policy definitions.

### LLM context injection
- When constructing the prompt for an AI inference call, context documents are assembled only from the authenticated tenant's retrieval results.
- No cross-tenant document can appear in the context window.

## The operational rule for cross-tenant references

If a user query contains a reference to another tenant's data — e.g., "how did Firm B handle the Al-Rashidi acquisition?" — the system:
1. Does **not** attempt to retrieve Firm B's data.
2. Responds with only publicly available general information relevant to the question.
3. Does **not** confirm or deny whether Firm B is a client of the platform.

Example compliant response:
> I can only access materials from your firm's workspace. For general guidance on acquisition structuring, here's what applies...

## Audit trail for cross-tenant operations

Administrative operations that span tenants (e.g., platform admin acting on behalf of a tenant, support access for troubleshooting) are logged with:
- Acting user ID
- Target tenant ID
- Action type and description
- Timestamp (UTC)
- Business justification (required for access to another tenant's data)

These logs are immutable and exportable for compliance review. See [[eng-audit-log-schema]].

## Compliance mapping

| Obligation | How cross-tenant isolation satisfies it |
|-----------|----------------------------------------|
| ABA Rule 1.6 (US) — client confidentiality | No other firm can access client data; equivalent to a wall between law firms |
| GDPR Art. 25 — data protection by design | Isolation enforced at storage layer before any application logic |
| KSA PDPL — data controller obligations | Organizational and technical measures prevent unauthorized access |
| UAE PDPL — security measures | Encryption + RLS + audit log constitute technical safeguards |
| DIFC Law No. 5/2020 | Equivalent to GDPR data protection by design |
| Bar professional secrecy (LB, FR, etc.) | No other bar member (firm) can access another's client data |

## What cross-tenant isolation does not cover

- **Intra-tenant confidentiality**: isolation between matters within the same firm requires matter-level access controls (see [[safety-bar-rules-confidentiality]] — Layer 2).
- **Insider threats**: a lawyer within Tenant A accessing matters they shouldn't — matter-level RBAC, not cross-tenant isolation, is the appropriate control.
- **AI conversation privilege**: cross-tenant isolation does not make AI conversations privileged under attorney-client doctrine — see [[safety-ai-not-privileged-disclaimer-us-heppner]].

## Related skills

- [[safety-bar-rules-confidentiality]] — full confidentiality architecture overview
- [[safety-bar-rule-1-6-confidentiality-ai]] — Rule 1.6 and AI tool selection
- [[safety-pii-redaction-before-rag]] — PII redaction before external LLM calls
- [[safety-client-data-retention-mena-rules]] — data retention obligations by jurisdiction
- [[eng-tenant-isolation-row-level-security]] — technical implementation of RLS
