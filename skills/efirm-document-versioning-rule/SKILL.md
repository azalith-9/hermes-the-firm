---
name: efirm-document-versioning-rule
description: Use when a law firm needs to define, enforce, or explain its document versioning policy — covering naming conventions, version-number schemes, checkout/check-in controls, comparison workflows, privileged-document protections, and audit-trail requirements. Applies to all document types produced in eFirm (contracts, court filings, legal opinions, correspondence). Part of the eFirm firm-management product suite.
license: MIT
metadata: " id: efirm.document-versioning-rule category: efirm jurisdictions: [__multi__] priority: P2 intent: [versioning, document-management, DMS, audit-trail, collaboration] related: - efirm-matter-creation-flow - efirm-template-library-firm-branded - efirm-knowledge-base-curation - efirm-team-handoff-summary - efirm-precedent-finder-internal source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'efirm'.
Registered as a flat plugin skill.
-->


# Document Versioning Rule

## When to use this

Use this skill to:
- Define and document the firm's versioning policy for a new document management system (DMS) deployment.
- Enforce versioning rules when AI-assisted drafting produces a new document version.
- Train team members on the firm's naming and version-control conventions.
- Recover or reconstruct a document history after an incident.
- Audit whether a document used in a filing, opinion, or transaction was the authorised final version.

In legal practice, document version confusion is a source of costly errors: sending the wrong draft to a counterparty, using a superseded clause in a transaction, filing an unapproved version in court. A clear versioning rule eliminates ambiguity.

## Naming convention

### Standard format

```
[MatterID]_[DocType]_[ShortDescription]_v[Major].[Minor]_[YYYYMMDD]
```

| Component | Description | Example |
|---|---|---|
| MatterID | Firm matter number | `2025-LB-0042` |
| DocType | Document type code (see below) | `NDA` / `SPA` / `BRIEF` |
| ShortDescription | 2–5 word descriptor | `DraftMasterAgreement` |
| v[Major].[Minor] | Version number | `v1.0` / `v2.3` |
| YYYYMMDD | Date of this version | `20250514` |

**Example**: `2025-LB-0042_SPA_SharePurchaseAgreement_v3.1_20250514.docx`

### Document type codes (standard set)

| Code | Document type |
|---|---|
| NDA | Non-disclosure agreement |
| SPA | Share purchase agreement |
| SHA | Shareholders agreement |
| EL | Engagement letter |
| BRIEF | Court brief / memorial |
| MOT | Motion / application |
| OPN | Legal opinion |
| LTR | Correspondence / letter |
| MEMO | Internal legal memo |
| CONT | Contract (generic) |
| REG | Regulatory filing |

Firms should publish a complete code table in their DMS and in the Knowledge Base ([[efirm-knowledge-base-curation]]).

## Version-number scheme

| Version state | Number | When to increment |
|---|---|---|
| First draft | v0.1 | Document first created and saved |
| Substantive draft revisions | v0.2, v0.3 … | Each material revision before partner sign-off |
| Partner-reviewed draft | v1.0 | Partner has reviewed and approved for external transmission |
| External revision received | v1.1, v1.2 … | Each round of counterparty or client comments |
| Agreed / execution version | v[Final] | Parties have agreed; document is ready for execution |
| Post-execution amendment | v2.0 | First amendment to an executed document |

**Rule**: Only a "v[X].0" document may be transmitted to a counterparty or filed with a court. Odd sub-versions (v0.x, v1.1) are internal working drafts.

## Checkout / check-in controls

To prevent simultaneous editing conflicts:

1. **Checkout**: a user locks the document for editing. Others see it as read-only during checkout.
2. **Mandatory comment on check-in**: user describes changes made (e.g., "Revised indemnity clause per partner comments; updated definition of Affiliate per KSA Law").
3. **Auto-unlock**: if checked out for >48 hours without activity, DMS sends a reminder; after 72 hours, an administrator can force-unlock.
4. **Concurrent editing** (if DMS supports): track changes visible to all; merge conflicts reviewed before final save.

## Comparison workflow

When a new version is produced:
1. Generate a tracked-changes comparison between the new version and the immediately prior version.
2. Attach the comparison document as a companion file (same name + `_REDLINE`).
3. For external transmission: send both the clean version and the redline unless the counterparty requests clean-only.

**Naming redline**: `2025-LB-0042_SPA_SharePurchaseAgreement_v3.1_REDLINE_20250514.docx`

## Privileged document protections

- Documents marked **Legally Privileged** must be stored in the privileged sub-folder of the matter.
- Privileged documents must never be transmitted via auto-share or DMS external portal without explicit partner authorization.
- Version history of privileged documents is itself privileged; access is restricted to the matter team.
- Metadata stripping: before external transmission of any Word document, run a metadata clean to remove tracked changes, comments, and author/company fields. Failure to strip metadata has resulted in inadvertent waiver of privilege in reported cases.

## Audit trail requirements

The DMS must record for every version save:
- User ID
- Timestamp (UTC + local timezone)
- Action (created / checked out / checked in / transmitted / archived)
- Document hash (SHA-256 or equivalent) for integrity verification
- Matter ID linkage

Audit logs must be immutable — no user should be able to delete or alter a version history entry. Retention: minimum 7 years (matching typical bar file retention requirements; some jurisdictions require longer for certain matter types).

## Final / executed documents

- The executed (signed) version is designated `vFINAL` or `vEXEC`.
- It must be stored in the signed-documents sub-folder.
- A PDF scan or e-signature platform export is the authoritative copy; the Word source version is retained for reference.
- No further edits to a vFINAL document; any change requires a formal amendment document with a new matter sub-file.

## Common mistakes

- **Email-based versioning** ("Draft v3 FINAL FINAL2 revised.docx"): prohibited. All documents go through the DMS.
- **Personal desktop saves**: documents saved only to a local machine are outside the audit trail and backup system — not permitted.
- **Transmitting a v0.x draft**: internal working drafts must not leave the firm. Only v[X].0 or vFINAL documents are transmitted externally.
- **Metadata in transmitted documents**: always strip before sending; metadata reveals tracked changes, prior authors, internal comments.

## Related skills

- [[efirm-matter-creation-flow]]
- [[efirm-template-library-firm-branded]]
- [[efirm-knowledge-base-curation]]
- [[efirm-team-handoff-summary]]
- [[efirm-precedent-finder-internal]]
