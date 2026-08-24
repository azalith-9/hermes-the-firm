---
name: import-assignation-refere-recouvrement-creance
description: Use when migrating a French-law assignation en référé pour recouvrement de créance (emergency summons for debt recovery) from a legacy data source into the Louis platform data model. Handles parsing of the debt-recovery summons structure, field mapping to the Louis matter and document schema, creditor/debtor party mapping, debt amount normalization, and dry-run preview before commit. Applies to French procedure and Lebanese commercial procedure which mirrors it.
license: MIT
metadata: " id: import.assignation-refere-recouvrement-creance category: import jurisdictions: [FR, LB] priority: P3 intent: [__import__, migration, French-procedure, référé, debt-recovery] related: [import-assignation-refere-communication-associe, import-compliance-anthropic, import-canned-responses-anthropic] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'import'.
Registered as a flat plugin skill.
-->


# Import — Assignation en Référé: Recouvrement de Créance

## What it does

This import skill ingests a legacy document of the type *assignation en référé pour recouvrement de créance* — an emergency summons filed in French-procedure référé proceedings to recover a debt that is certain (*certaine*), liquidated (*liquide*), and due (*exigible*). It maps the document into the Louis matter and document schema for tracking, review, and continuation within the platform.

## Legal context

### Recouvrement de créance en référé

In French civil procedure and Lebanese commercial procedure, a creditor holding a certain, liquidated, and due debt may seek judicial recovery without waiting for ordinary civil proceedings. Two main procedural routes exist:

1. **Injonction de payer (payment order)**: a non-adversarial, ex parte application for a payment order. Faster and cheaper; limited to undisputed debts.
2. **Assignation en référé provision**: a contested summary proceeding where the creditor can obtain a provisional order for payment of an undisputed amount, even where some dispute exists, if the obligation is not "seriously contestable."

The *assignation en référé pour recouvrement de créance* is the formal summons initiating the second route. It is used where the debtor disputes the claim but the creditor believes the amount (or a significant portion) is not seriously contestable.

### Applicable law (Lebanon)

In Lebanon:
- The Code de Procédure Civile Libanais (CPCL) governs référé proceedings.
- The Code des Obligations et Contrats (COC) governs the underlying debt claims.
- The Commercial Code governs commercial debts (negotiable instruments, commercial contracts).

The référé judge (President of the First Instance Court or Commercial Court, depending on the nature of the debt) can award a provisional sum, order attachment of assets, or take other urgent measures.

## Import configuration

### Source document fields

| Source field | Louis target field | Notes |
|---|---|---|
| Créancier (creditor) | `matter.party[role=claimant]` | Full legal name + entity type |
| Débiteur (debtor) | `matter.party[role=respondent]` | Full legal name + entity type |
| Juridiction | `matter.court` | Court name + jurisdiction |
| Montant de la créance | `matter.claim_amount` | Amount + currency; normalize to ISO currency code |
| Fondement de la créance | `matter.claim_basis` | Contract, invoice, loan, etc. |
| Documents supports | `matter.evidence_documents` | List of invoices, contracts, etc. referred to in the summons |
| Date d'assignation | `matter.filing_date` | Service date of the summons |
| Fondement légal | `matter.legal_basis` | Article references (CPCL, COC, etc.) |
| Audience prévue | `matter.next_hearing_date` | Référé hearing date |
| Mesures conservatoires | `matter.interim_measures` | Any attachment or preservation order sought |

### Debt amount normalization

The debt amount extracted from the source document must be:
- Expressed in both figures and words in the source: verify they match.
- Tagged with the correct currency (LBP, USD, EUR). Note: in Lebanon post-2019, dual-currency clauses (LBP + USD) are common. Extract both amounts if present.
- Normalized to the Louis amount schema: `{ amount: 50000, currency: "USD", amount_words: "Fifty thousand US dollars" }`.

If the source contains a claim expressed in Lebanese pounds at an old exchange rate, flag this for manual review — Lebanese pound denominated debts have significant valuation complexity post-2019 banking crisis.

### Dry-run preview

Before committing the import, Louis generates a preview showing:
- Parsed creditor and debtor names, with a duplicate detection check.
- The claim amount with currency, and a flag if the currency parsing is uncertain.
- The proposed matter type (`litigation/référé/recouvrement`) and jurisdiction tags.
- Any fields that could not be parsed (flagged for manual completion).
- A warning if the debt amount appears to exceed a threshold (e.g., > USD 1,000,000) warranting additional review.

### Post-import actions

After a successful import, Louis auto-creates:
- A matter entry of type `litigation/référé/debt-recovery`.
- A document entry with the original summons uploaded.
- A task: "Verify debt calculation and accrued interest" — because interest accrual from the accrual date to the hearing date may need to be updated.
- A limitation check: flags if the filing date is approaching the applicable limitation period (see [[heuristic-statute-of-limitations-flag]]).
- A next-hearing-date reminder.

## Failure modes

- **Non-machine-readable source**: trigger OCR; flag low-confidence extractions for manual review.
- **Lebanese pound amounts**: if the claim is in LBP, flag for manual review of exchange rate assumptions and current equivalent value.
- **Multiple debtors or creditors**: parse each party separately; create multiple party entries.
- **Missing claim foundation**: if the underlying contract or invoice reference is not present in the source document, flag a task to attach the supporting documents.

## Related skills

- [[import-assignation-refere-communication-associe]]
- [[import-compliance-anthropic]]
- [[import-canned-responses-anthropic]]
- [[heuristic-statute-of-limitations-flag]]
