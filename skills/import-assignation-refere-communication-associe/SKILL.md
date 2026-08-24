---
name: import-assignation-refere-communication-associe
description: Use when migrating a French-law assignation en référé pour communication d'associé (emergency summons for shareholder communication or document access) from a legacy data source into the Louis platform data model. Handles parsing of the legacy document structure, field mapping to the Louis matter and document schema, and dry-run preview before commit. This import skill is specific to French-procedure corporate dispute documents.
license: MIT
metadata: " id: import.assignation-refere-communication-associe category: import jurisdictions: [FR, LB] priority: P3 intent: [__import__, migration, French-procedure, référé, corporate-dispute] related: [import-assignation-refere-recouvrement-creance, import-compliance-anthropic, import-canned-responses-anthropic] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'import'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Import — Assignation en Référé: Communication d'Associé

## What it does

This import skill ingests a legacy document of the type *assignation en référé pour communication d'associé* — an emergency summons (assignation) filed in référé proceedings (French-procedure summary/expedited proceedings before a President of the Tribunal) to compel a company to communicate documents to a shareholder or partner who has been denied their legal right of information and communication.

The skill maps the legacy data structure of such a document into the Louis matter and document schema, enabling the document to be searched, reviewed, and worked on inside the Louis platform.

## Legal context

### What is an assignation en référé?

In French civil procedure (and in Lebanon, which inherited much of the French procedural framework), a *référé* is an emergency proceeding before the President of the court (or a designated judge). It is used where urgency is required and the rights claimed are not seriously contestable (*pas de contestation sérieuse*) or where interim/preventive measures are needed.

An *assignation* is the formal summons document that initiates proceedings. Filing an *assignation en référé* is the act of formally notifying the opposing party and lodging the matter with the court.

### What is a communication d'associé?

In French company law (and Lebanese commercial law, which parallels it), shareholders and partners have statutory rights to receive certain company documents — annual accounts, management reports, minutes, statutory auditor reports. Where the company refuses or fails to communicate these documents, a shareholder may file for emergency judicial enforcement of this right via référé.

The typical structure of such an assignation:
1. Identification of the parties (associé/demandeur and company/défendeur).
2. Factual background: the documents requested and the company's refusal or silence.
3. Legal basis: the specific provisions of the applicable commercial code (French Code de Commerce, Lebanese Commercial Code) granting the right.
4. Relief sought: order compelling communication of specified documents.
5. Urgency: why the urgency standard is met.

## Import configuration

### Source document fields

| Source field | Louis target field | Notes |
|---|---|---|
| Demandeur (requesting shareholder) | `matter.party[role=claimant]` | Full legal name + entity type |
| Défendeur (company) | `matter.party[role=respondent]` | Full legal name + registration number |
| Juridiction | `matter.court` | Name of court + jurisdiction (Paris, Beirut, etc.) |
| Date d'assignation | `matter.filing_date` | Date the summons was served |
| Documents sollicités | `matter.relief_sought.document_list` | Structured list of documents requested |
| Fondement légal | `matter.legal_basis` | Article references (Code de Commerce, Code de Procedure Civile libanais) |
| Audience prévue | `matter.next_hearing_date` | Date of the référé hearing |
| Urgence | `matter.urgency_basis` | Statement of urgency grounds |

### Dry-run preview

Before committing the import, Louis generates a preview showing:
- The parsed party names and how they map to the matter model.
- Any fields that could not be parsed (flagged for manual completion).
- The proposed matter type, practice area, and jurisdiction tags.
- Duplicate detection: if a matter with the same parties and filing date already exists, surface a warning.

### Post-import actions

After a successful import, Louis auto-creates:
- A matter entry of type `litigation/référé`.
- A document entry with the original uploaded file.
- A task: "Verify legal basis articles against current law" — because article numbers may have been renumbered in the source jurisdiction.
- A next-hearing-date reminder (if the hearing date was successfully parsed).

## Failure modes

- **Unstructured source**: if the source document is an image or non-machine-readable PDF, trigger OCR before import. Flag low-confidence OCR extractions for manual review.
- **Non-standard format**: French référé assignations vary significantly by law firm and jurisdiction (French vs Lebanese procedure). If the document structure does not match expected field positions, fall back to manual field assignment in the import UI.
- **Missing legal basis**: if the specific article numbers are not present in the source, leave `legal_basis` blank and flag for the user to complete.

## Related skills

- [[import-assignation-refere-recouvrement-creance]]
- [[import-compliance-anthropic]]
- [[import-canned-responses-anthropic]]
