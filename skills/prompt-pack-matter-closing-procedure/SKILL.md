---
name: prompt-pack-matter-closing-procedure
description: Use when drafting a matter closing procedure for a law firm or legal department covering final billing, client communication, file organization, document retention, conflict system updates, lessons learned, and archiving. Ensures matters are closed in a defensible and organized manner and that institutional knowledge is preserved. Applicable to transactional, litigation, and advisory matters.
license: MIT
metadata: " id: prompt-pack.matter-closing-procedure category: prompt-pack practice_area: legal-ops-billing priority: P2 intent: [operations, matter-closing-procedure] related: - prompt-pack-matter-budget-template - prompt-pack-legal-invoice-review-checklist - prompt-pack-legal-hold-management-procedure - prompt-pack-legal-department-annual-report source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'prompt-pack'.
Registered as a flat plugin skill.
-->


# Matter Closing Procedure

## When to use this

Use this skill to draft or implement a formal matter closing procedure — the organizational process that governs how a matter is brought to a close, ensuring all financial, client, ethical, knowledge-management, and compliance obligations are met before the file is archived.

Triggers:
- "Draft a matter closing procedure for our in-house legal department."
- "We need a standard process for closing matters once a deal or case is finished."
- "Build a matter close checklist for our firm's practices."

## Required inputs

| Input | Why it matters | Default |
|---|---|---|
| Entity type | Law firm vs in-house legal department — procedures differ | Ask user |
| Matter management system | Determines which steps can be automated | None — manual procedure |
| Document retention policy | Specifies how long closed matter files are kept before destruction | Refer to existing policy or local law |
| Jurisdiction(s) | Affects professional conduct rules (file retention, client property) | Ask user |

## Optional inputs

- E-billing platform in use (for automated final invoice processing)
- Knowledge management system (for lessons learned capture)
- Whether the procedure applies to all matter types or only specific categories

## Closing procedure steps

### Step 1: Confirm Matter Is Ready to Close

Before initiating closure, confirm all of the following:
- [ ] The substantive work is complete (transaction closed, litigation concluded, advice delivered, regulatory filing made)
- [ ] All outstanding work streams are finished or formally transferred to another matter
- [ ] No pending appeals, limitation periods, or regulatory follow-up actions
- [ ] Any legal hold issued for the matter has been formally released — see [[prompt-pack-legal-hold-management-procedure]]
- [ ] Client has been notified that the matter is concluding (where applicable)

### Step 2: Final Billing

- [ ] Responsible attorney reviews all unbilled time and disbursements associated with the matter
- [ ] Write down or write off any time not to be billed (with supervisor approval per billing policy)
- [ ] Prepare and issue the final invoice; confirm it complies with OCG requirements or engagement letter terms
- [ ] Confirm all prior invoices have been paid or outstanding balances have been addressed
- [ ] If billing a fixed fee, confirm all milestones and deliverables are complete and accepted before final invoice
- [ ] In e-billing system: mark all open work-in-process as billed or written off; close matter in billing system

### Step 3: Client Communication

- [ ] Send a matter closing letter to the client confirming:
  - The matter has concluded
  - Summary of outcome (as appropriate for the matter type)
  - Status of any ongoing obligations on the client's part (e.g., contractual obligations post-closing, limitation periods for any ancillary claims, registration or filing deadlines arising from the transaction)
  - File retention: how long the firm/department will retain the matter file; procedure for requesting a copy of the file
  - Any original documents held in safekeeping and returned to client
- [ ] Confirm all client-owned documents and originals have been returned or are held per client instructions

### Step 4: File Organization and Documentation

- [ ] Organize the matter file in the document management system:
  - Final executed versions of all key documents (agreements, court filings, regulatory submissions, opinions)
  - Correspondence (chronological order)
  - Research memoranda and advice notes
  - Billing records
- [ ] Confirm all versions and drafts are properly labeled; delete or archive superseded drafts per retention policy
- [ ] Ensure all attorney work product (memos, research) is accessible in the matter management / document management system
- [ ] For transactions: prepare and maintain the final closing set (complete, executed set of transaction documents including conditions precedent documents, opinion letters, corporate approvals)

### Step 5: Conflict System Updates

- [ ] Update the conflict-of-interest system / database with all parties, entities, and matters relevant to the closed matter
- [ ] Add any new confidential information categories that arose during the matter (relevant for future conflict checks)
- [ ] Confirm the matter is flagged as "Closed" in the matter management system so it appears appropriately in future conflict searches

### Step 6: Lessons Learned and Knowledge Capture

- [ ] Responsible attorney completes a brief lessons learned memo (10–20 minutes of reflection is sufficient):
  - What went well
  - What could be improved
  - Novel legal issues or jurisdiction-specific learning
  - Useful precedents or templates developed during the matter
- [ ] Upload any reusable templates, precedents, or research to the firm/department knowledge management library
- [ ] Flag any matters involving new or significant legal developments for inclusion in client alerts or practice group updates

### Step 7: Matter Statistics and Reporting

- [ ] Record final matter statistics in the matter management system:
  - Matter type and sub-type
  - Open date, close date, total duration
  - Total fees billed and collected
  - Timekeeper utilization
  - Outcome (if applicable)
- [ ] Link the matter to the applicable KPI dashboard metrics — see [[prompt-pack-legal-department-kpi-dashboard]]
- [ ] For litigation: record outcome for win/loss reporting

### Step 8: Archiving

- [ ] Mark the matter as "Archived" in the matter management and document management systems
- [ ] Apply the document retention period: per the firm/department policy or applicable law (see below)
- [ ] Physical files: box and label with matter number, close date, scheduled destruction date; transfer to offsite storage
- [ ] Set calendar reminder for destruction date review (do not destroy without a fresh destruction authorization review)

## Document retention guidance

| Matter type | Typical retention period | Notes |
|---|---|---|
| Transactions (M&A, commercial) | 7–10 years from closing | May be longer if matters involve tax, regulatory, or IP issues |
| Litigation / arbitration | 7 years from final resolution | Retain through all appeals + limitation period |
| Real estate | Duration of ownership + [7 years] | Title documents: permanent |
| Employment | 5–7 years from end of employment | MENA: varies by jurisdiction |
| Regulatory filings | 7–10 years from filing | Some jurisdictions require permanent retention |

**Jurisdiction-specific notes**:
- **UAE**: Commercial Companies Law requires companies to retain commercial books and records for 5 years; professional conduct rules for lawyers vary.
- **KSA**: SOCPA accounting standards require 10-year retention of financial records; commercial records generally 10 years.
- **Lebanon**: Commercial code requires commercial document retention for 10 years.
- **GDPR / data protection**: personal data in matter files must be reviewed at retention-period expiry for erasure or justification for continued retention.

## Common mistakes

- **Not confirming legal hold release before closing**: if a hold was issued for the matter, destroying files without formal hold release exposes the company to spoliation claims if related proceedings re-open.
- **Issuing the final invoice without writing off non-billable time**: unbilled time left open in the billing system creates reporting noise and potential errors in future invoices.
- **Skipping the conflict system update**: matters involving adversaries, witnesses, or sensitive commercial information that are not recorded in the conflict system will cause future conflict-check failures.
- **No client closing letter**: the client closing letter documents the formal end of the retainer and protects the firm from arguments that the retainer continued indefinitely.
- **Never doing lessons learned**: systematic avoidance of lessons learned means the firm/department repeats the same mistakes and fails to build institutional knowledge.

## Related skills

- [[prompt-pack-matter-budget-template]]
- [[prompt-pack-legal-invoice-review-checklist]]
- [[prompt-pack-legal-hold-management-procedure]]
- [[prompt-pack-legal-department-annual-report]]
- [[prompt-pack-legal-department-kpi-dashboard]]
