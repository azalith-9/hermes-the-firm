---
name: efirm-knowledge-base-curation
description: Use when a law firm needs to build, maintain, or govern its internal knowledge base — the structured repository of precedents, standard clauses, legal opinions, regulatory guidance notes, and firm policies that lawyers draw on for client work. Covers content types, tagging schema, curation workflow, quality control, access tiers, and the connection between the KB and AI-assisted drafting skills. Part of the eFirm firm-management product suite.
license: MIT
metadata: " id: efirm.knowledge-base-curation category: efirm jurisdictions: [__multi__] priority: P2 intent: [knowledge-management, KM, precedent, templates, curation, taxonomy] related: - efirm-precedent-finder-internal - efirm-template-library-firm-branded - efirm-document-versioning-rule - efirm-matter-creation-flow source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'efirm'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Knowledge Base Curation

## When to use this

Use this skill to:
- Define the structure and taxonomy for a new or rebuilt firm knowledge base.
- Ingest a completed matter's documents into the KB as precedents after deal close.
- Review and approve a precedent submitted by an associate for inclusion in the KB.
- Determine access tiers for sensitive knowledge assets (e.g., opinion letters, confidential strategies).
- Connect the KB to AI-assisted drafting workflows so skills like [[efirm-template-library-firm-branded]] can retrieve the correct baseline document.

## What belongs in the knowledge base

### Tier 1: Firm-wide precedents

Documents approved for use as baselines by any lawyer on any matter:
- Standard NDA (unilateral; mutual; tri-party variants)
- Standard employment agreement by jurisdiction
- Company formation documents by jurisdiction
- Standard terms and conditions (B2B; B2C)
- Engagement letter templates
- Fee schedule templates

### Tier 2: Practice-area precedents

Documents curated by and for a specific practice group:
- Corporate/M&A: SPA; SHA; Term Sheet; LOI; Management Agreement
- Dispute resolution: Statement of Claim templates; Memorial templates; Arbitration Notices
- Real estate: Sale and Purchase Agreement; Lease template; MoU
- IP: IP Assignment; IP License; FRAND terms
- Employment: TUPE letters (UK); redundancy notices; settlement agreements
- Regulatory: Application templates per authority and jurisdiction

### Tier 3: Precedent opinions and memos

Legal opinions and analysis notes from prior matters — the highest-value and most sensitive KB content:
- Due diligence reports (redacted of client-specific data)
- Regulatory opinions on specific legal questions
- Analysis memos on recurring legal issues

Access: restricted to partner level or specific practice group. These must be reviewed and approved before each reuse — they are not drop-in documents.

### Tier 4: Firm policies and procedures

- Fee schedule
- Data protection / GDPR / PDPL compliance policies
- Conflict-check protocol
- AML policy
- Document retention and destruction policy
- Client communication standards

## Tagging schema

Every KB document must be tagged on ingestion with:

| Tag dimension | Values (examples) |
|---|---|
| Document type | NDA / SPA / Opinion / Policy / Brief / Template |
| Practice area | Corporate / Dispute / Employment / IP / Regulatory / Real Estate |
| Jurisdiction(s) | LB / KSA / UAE / DIFC / ADGM / UK / US / FR / OHADA / GCC |
| Governing law | UAE / DIFC / KSA / English / French / US-NY / other |
| Language | Arabic / English / French / Bilingual-AR-EN |
| Status | Active / Superseded / Under review |
| Access tier | Firm-wide / Practice / Partner-only |
| Matter type | Transaction / Litigation / Advisory / Regulatory |
| Last reviewed | Date |
| Approved by | Responsible partner ID |

Tags must be searchable. The [[efirm-precedent-finder-internal]] skill uses these tags to retrieve relevant documents.

## Curation workflow

### Step 1: Source identification

After each matter closes (or at defined milestones for long-running matters), the responsible associate and partner review the matter documents for KB-worthy content.

Criteria for KB inclusion:
- Document contains a clause, structure, or position not already in the KB.
- Document reflects a new jurisdiction, regulatory environment, or legal development.
- Document was particularly well-received by the client or counterparty (quality signal).
- Document contains a hard-won negotiation position worth preserving.

### Step 2: Redaction and anonymisation

Before any precedent is stored in the firm-wide or practice-area tiers, **client-identifying information must be removed**:
- Party names → generic placeholders (e.g., "Company A", "the Seller")
- Dates → approximate period (e.g., "Q4 2024")
- Transaction-specific financial figures → [AMOUNT] placeholders
- Any information that would identify the underlying matter

Opinion letters and memos require more careful review — even the legal issue described may identify the client in a small market.

### Step 3: Review and approval

All KB submissions require:
1. Associate prepares redacted document + cover note (why it should be added; what it adds beyond existing precedents).
2. Practice group partner or Knowledge Management partner reviews.
3. Approved → tagged and ingested.
4. Declined → feedback provided; document stored in personal matter records only.

### Step 4: Maintenance and currency review

The KB is a living resource that degrades without active maintenance:
- **Annual review**: each practice group partner reviews all active documents in their tier. Superseded law → document flagged for update or retirement.
- **Triggered review**: if a relevant new statute, regulation, or court ruling is published, the KM partner triggers an immediate review of affected documents.
- **Version control**: updated documents follow [[efirm-document-versioning-rule]]; old version is archived as "Superseded" with a note pointing to the new version.

## Quality control standards

- No document enters the KB without partner approval.
- Every KB document must have a clear "last reviewed" date visible in the metadata.
- Documents not reviewed in the last 24 months are automatically flagged for review or retirement.
- Bilingual documents (Arabic/English) must be certified as consistent — a mistranslation in the KB propagates to every matter using that document.

## Access control

| Tier | Access |
|---|---|
| Firm-wide precedents | All attorneys and paralegals |
| Practice-area precedents | Practice group members + partners with cross-practice access |
| Precedent opinions | Partners only; specific practice group |
| Firm policies | All staff (certain policies: all; sensitive: attorneys only) |

Access is provisioned per role in the DMS; changes require KM partner authorization.

## Connection to AI-assisted drafting

When AI skills draft or review a document (e.g., [[efirm-template-library-firm-branded]]; [[efirm-engagement-letter-draft]]), they should:
1. Query the KB for the most recent approved baseline for that document type and jurisdiction.
2. Use the approved baseline as the starting point — never from scratch.
3. Log which KB document version was used as the baseline (audit trail).
4. Surface any KB documents flagged "Under review" so the lawyer knows the baseline may be stale.

## Related skills

- [[efirm-precedent-finder-internal]]
- [[efirm-template-library-firm-branded]]
- [[efirm-document-versioning-rule]]
- [[efirm-matter-creation-flow]]
- [[efirm-engagement-letter-draft]]
