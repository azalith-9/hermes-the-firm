---
name: safety-bar-rules-confidentiality
description: Use as the architecture overview for how professional bar-rules confidentiality obligations are implemented across the legal AI platform. Covers cross-tenant isolation (absolute rule), cross-matter isolation within a tenant, the privilege status of AI conversations (Heppner, Feb 2026), PII redaction defaults, and log scoping. Intended for platform configuration reviews, eFirm onboarding, and lawyer users who ask how confidentiality is protected system-wide.
license: MIT
metadata: " id: safety.bar-rules-confidentiality category: safety jurisdictions: [US, UK, LB, KSA, UAE, DIFC, ADGM, GCC, EU] priority: P0 intent: [safety, confidentiality, bar-rules, architecture, professional-responsibility] related: - safety-client-confidentiality-cross-tenant - safety-bar-rule-1-6-confidentiality-ai - safety-ai-not-privileged-disclaimer-us-heppner - safety-pii-redaction-before-rag - safety-attorney-work-product-ai-handling source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'safety'.
Registered as a flat plugin skill.
-->


# Bar Rules — Confidentiality Architecture

## When to use this

This skill is the **system-level overview** of how lawyer confidentiality obligations map to platform architecture. Use it:
- When onboarding an eFirm tenant and explaining how data isolation works.
- When a lawyer user asks "how do you keep my client data safe?"
- When a compliance team audits the platform against bar-rules confidentiality requirements.
- As the routing parent for the more specific sub-skills on privilege, PII, and tenant isolation.

## The core principle

Lawyers' confidentiality duties under their bar codes are **stricter than general privacy law**. They apply to everything "relating to the representation of a client" — not just personal data, but strategy, litigation analysis, deal terms, and internal communications. The platform is built around this stricter standard.

## Layer 1 — Cross-tenant isolation (absolute)

**Rule**: Data, embeddings, RAG chunks, and learned patterns from Tenant A (Firm A) are **never accessible** to Tenant B (Firm B), under any circumstances.

**Implementation**:
- Vector store partitioned by `tenant_id`; retrieval queries enforce the filter at the storage layer, not the application layer (cannot be bypassed by a misconfigured query).
- Database access is row-level secured by `tenant_id` — [[safety-client-confidentiality-cross-tenant]].
- Tenant-trained few-shot examples and firm-specific playbooks load only when the authenticated tenant matches.

**Operational rule**: if a query contains a reference to another tenant ("how did Firm B handle this?"), the system returns only the public/general answer — Firm B's specific data is never surfaced.

**Audit**: cross-tenant administrative operations (e.g., platform admin acting across tenants) are logged with tenant ID, user ID, action, and timestamp. See [[eng-audit-log-schema]].

## Layer 2 — Cross-matter isolation within a tenant

**Rule**: Within a single eFirm tenant, matter-level isolation is **default-on**. Matter A's documents and context are not available to Matter B queries unless an explicit share action has been taken.

**Mechanics**:
- Each matter has a `matter_id`; RAG retrieval is scoped to the requesting matter by default.
- Sharing context across matters requires an explicit "share with [matter]" action by a lawyer with appropriate permissions, or a firm-wide knowledge base setting.
- This mirrors how a well-run law firm operates: a conflict-wall between matters serves confidentiality obligations to both clients.

**Why it matters**: a lawyer handling an acquisition for Company A must not inadvertently pull in a document from a different client's matter when using the AI for a research query. The default prevents accidental cross-contamination.

## Layer 3 — AI conversation privilege status

**Rule**: AI conversations are **not privileged** in the US per the *Heppner* ruling (Feb 2026) and are unsettled elsewhere.

**Implementation**:
- Surface the Heppner disclaimer to lawyer users when they paste client communications or reference active matters — [[safety-ai-not-privileged-disclaimer-us-heppner]].
- Best practice: keep client-identifying details out of AI prompts wherever possible. Use anonymization or refer to [[safety-pii-redaction-before-rag]] for systematic redaction.

**Work product**: whether AI-assisted work product retains its protection depends on the AI vendor's DPA and confidentiality controls — [[safety-attorney-work-product-ai-handling]].

## Layer 4 — PII redaction before external LLM calls

**Rule**: Before indexing documents to the vector store or sending content to a third-party LLM endpoint, PII redaction runs by default unless the tenant has explicitly opted out for a specific matter.

**Redacts**: names → `[PERSON_N]`, national IDs → `[NAT_ID]`, accounts → `[ACCOUNT]`, phones → `[PHONE]`, emails → `[EMAIL]`, addresses → `[ADDRESS]`, health data → `[HEALTH]`.

**Reverse map**: kept in tenant-scoped encrypted storage; placeholders rehydrated only when sending the final response to the originating user.

**Override**: eFirm lawyers may opt out per-matter when substance review requires real identifiers (e.g., conflict check). Opt-out is logged. See [[safety-pii-redaction-before-rag]].

## Layer 5 — Log scoping and data residency

**Rule**: Access logs are tenant-scoped and do not leave the tenant's designated region.

**Preferred regions**:
- MENA clients: EU-West or ME-South where available, to minimize cross-border transfer obligations under KSA PDPL, UAE PDPL, and GDPR.
- EU clients: EU-West (Frankfurt, Paris, Amsterdam) for GDPR compliance.
- Lawyer can request explicit region assignment at tenant onboarding.

**What logs capture**: who accessed which matter, when, what action was taken, and whether any PII was sent unredacted.

## Confidentiality obligations by jurisdiction

| Jurisdiction | Primary rule | Key AI implication |
|-------------|-------------|-------------------|
| US | ABA Model Rule 1.6 | DPA required; Heppner warning for lawyer users |
| UK | SRA Code Principle 6 + GDPR | DPA required; LPP risk for AI conversations |
| LB | Bar Code of Conduct (sirr al-mihna) | No formal AI guidance; professional secrecy applies |
| KSA | Code of Law Practice M/38 + PDPL Art. 29 | Cross-border transfer requires SDAIA safeguards |
| UAE | Federal Law on Legal Profession + PDPL Art. 22 | Contractual safeguards required; DIFC/ADGM have own DP laws |
| France | RIN + secret professionnel (Art. 226-13 CP) | Strongest privilege in Europe; AI tools must be tightly controlled |
| EU | GDPR Art. 28 + national bar codes | DPA mandatory; cross-border SCCs for non-EU vendors |

## Related skills

- [[safety-client-confidentiality-cross-tenant]] — cross-tenant isolation details
- [[safety-bar-rule-1-6-confidentiality-ai]] — Rule 1.6 and AI tool selection
- [[safety-ai-not-privileged-disclaimer-us-heppner]] — Heppner privilege disclaimer
- [[safety-pii-redaction-before-rag]] — PII redaction before external calls
- [[safety-attorney-work-product-ai-handling]] — work-product doctrine for AI-assisted materials
