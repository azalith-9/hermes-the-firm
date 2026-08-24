---
name: efirm-template-library-firm-branded
description: Use when a lawyer needs to retrieve and instantiate a firm-branded document template — populated with firm identity, approved standard clauses, and jurisdiction-specific disclosures — as the starting point for a new draft. The skill connects to the internal KB, applies the firm's visual and language standards, and prevents lawyers from drafting from blank or using unapproved external templates. Part of the eFirm firm-management product suite.
license: MIT
metadata: " id: efirm.template-library-firm-branded category: efirm jurisdictions: [__multi__] priority: P2 intent: [templates, firm-branding, drafting, standardization, knowledge-management] related: - efirm-knowledge-base-curation - efirm-precedent-finder-internal - efirm-document-versioning-rule - efirm-engagement-letter-draft source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'efirm'.
Registered as a flat plugin skill.
-->


# Template Library — Firm Branded

## When to use this

Use this skill when:
- A lawyer is creating a new document and needs the firm's standard starting point for that document type.
- An AI drafting skill needs to retrieve the correct firm-branded baseline before generating or amending a document.
- A new practice group or jurisdiction is being added to the firm and templates need to be created or adapted.
- A template is being updated to reflect a law change and the firm-branded version needs to be refreshed.

The template library enforces three standards that a blank-document approach cannot:
1. **Brand consistency**: letterhead, font, numbering, formatting, and style are uniform across all firm documents.
2. **Legal accuracy**: approved standard clauses are vetted by the responsible partner; unapproved external templates often contain jurisdiction-inappropriate or outdated language.
3. **Audit trail**: every document generated from the library is linked to the approved template version, creating a defensible record.

## Template categories

### Client-facing documents

| Template | Variants | Jurisdiction coverage |
|---|---|---|
| Engagement letter | Standard; short-form; NDA-only; advisory-only | KSA / UAE / DIFC / ADGM / LB / UK / FR / US |
| Fee quote / proposal | Hourly; fixed-fee; hybrid | All |
| Client update letter | Partner-signed; associate-level | All |
| Legal opinion | Formal opinion; reliance letter; addressee instructions | DIFC / ADGM / UK / KSA |
| Disclosure letter | M&A transaction disclosures | UAE / DIFC / UK |
| Termination of engagement | Matter close letter | All |

### Commercial documents (firm-standard positions)

| Template | Variants |
|---|---|
| Non-disclosure agreement | Unilateral; mutual; tri-party |
| Employment agreement | Permanent; fixed-term; contractor |
| Consultancy agreement | Firm as consultant; firm retaining consultant |
| Share purchase agreement | Share-only; asset; hybrid |
| Shareholders agreement | Majority acquisition; JV; minority protection |
| Term sheet / LOI | Binding; non-binding |

### Regulatory and compliance documents

| Template | Notes |
|---|---|
| AML client declaration | Required at intake |
| Source of funds declaration | Per-jurisdiction variants |
| PEP self-declaration | |
| Data protection notice | GDPR / UAE PDPL / KSA PDPL variants |

### Internal firm documents

| Template | Notes |
|---|---|
| Matter file cover sheet | Printed with matter summary |
| Team briefing note | Initial brief for new matter team members |
| Case status memorandum | Internal status report |
| Legal research memo | Structured analysis format |

## Template anatomy

Every firm-branded template contains:

### 1. Header / letterhead block

- Firm logo (high-resolution)
- Firm name and legal entity
- Address, phone, email, website
- Bar registration numbers (per jurisdiction)
- VAT / tax registration number (where applicable)
- "Legally privileged and confidential" notice (where applicable)

### 2. Variable placeholder blocks

Clearly marked fields for matter-specific data:

```
[CLIENT_LEGAL_NAME]
[MATTER_TITLE]
[RESPONSIBLE_PARTNER]
[DATE]
[MATTER_NUMBER]
```

When the template is instantiated, the skill pulls available data from the eFirm matter record to auto-populate these fields. Remaining blanks are highlighted for manual completion.

### 3. Standard clause library

Approved standard clauses are embedded in the template (not referenced externally). Each clause carries:
- Clause identifier (for KB tracking)
- "Approved by" partner and date
- Jurisdiction applicability note

Examples:
- **Limitation of liability clause**: standard version + enhanced version (for high-risk matters)
- **Confidentiality clause**: standard; NDA-level; attorney-client privilege reminder
- **Data protection clause**: GDPR variant; UAE PDPL variant; KSA PDPL variant
- **Governing law and jurisdiction clause**: UAE Civil Code; DIFC; English; French; Saudi law variants

### 4. Jurisdiction-specific appendices

Each template has jurisdiction-specific appendices that are toggled on/off based on the matter jurisdiction:
- UAE appendix: Ministry of Justice registration number; UAE VAT disclosure
- KSA appendix: Saudi Bar number; Saudi VAT; Sharia-compliance note
- DIFC appendix: DIFC registered number; DFSA disclosure if applicable
- LB appendix: Beirut Bar reference
- UK appendix: SRA number; legal ombudsman right; consumer cooling-off right

### 5. Footer

- Page numbering
- Firm name and matter reference on each page
- Version number and date (auto-updated on instantiation)
- "Draft" watermark on all pre-vFINAL versions

## Instantiation workflow

When a lawyer requests a template:

1. **Input**: document type + jurisdiction + governing law + matter ID.
2. **Precedent search**: skill checks [[efirm-precedent-finder-internal]] for any prior precedent that should be used as baseline instead of the generic template.
3. **Template retrieval**: if no precedent, retrieve the current approved template from the library.
4. **Auto-population**: fill variable blocks from matter record data.
5. **Version initialization**: create as v0.1 in DMS per [[efirm-document-versioning-rule]].
6. **Notify lawyer**: document ready in DMS folder; any remaining blanks highlighted.

## Quality control

- All templates must be reviewed and approved by the responsible practice group partner before publication.
- Templates are dated; any template older than 24 months without a review date is flagged for review.
- When a relevant law changes (new statute, regulatory update, court ruling), the KM partner is notified and the affected templates are put "Under review" pending update.
- Lawyers are prohibited from removing or altering standard clauses without partner approval; changes to standard clauses are tracked and reviewed.

## Language standards

- All templates default to the firm's approved writing style: defined terms capitalized; active voice preferred; sentences below 40 words; no unexplained jargon.
- Bilingual templates (Arabic/English) have column-by-column parallel text; the controlling language is stated in the governing-law clause.
- AI-generated text inserted into templates must be reviewed against the firm's style guide before the document is transmitted externally.

## Related skills

- [[efirm-knowledge-base-curation]]
- [[efirm-precedent-finder-internal]]
- [[efirm-document-versioning-rule]]
- [[efirm-engagement-letter-draft]]
- [[efirm-matter-creation-flow]]
