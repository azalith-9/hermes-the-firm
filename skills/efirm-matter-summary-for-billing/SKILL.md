---
name: efirm-matter-summary-for-billing
description: Use when a lawyer or billing coordinator needs to produce a structured matter summary to accompany or support a client invoice — covering work performed, time entries by timekeeper, expenses, total fees, and narrative description of value delivered. Ensures invoices are clear, defensible, and compliant with any billing-guideline requirements. Part of the eFirm firm-management product suite.
license: MIT
metadata: " id: efirm.matter-summary-for-billing category: efirm jurisdictions: [__multi__] priority: P2 intent: [billing, invoice, matter-summary, narrative, time-entries] related: - efirm-finance-wip-aging-report - efirm-finance-realization-rate-tracker - efirm-client-update-email-draft - efirm-matter-creation-flow source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'efirm'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Matter Summary for Billing

## When to use this

Use this skill when:
- A billing period has closed and an invoice needs to be prepared for a client.
- A client requests a detailed breakdown of fees for a completed phase of work.
- A dispute has arisen over an invoice and a clear narrative of work performed is needed.
- A pre-billing review is underway to identify time entries that should be revised or written down before the invoice is sent.
- A supervising partner needs to review and approve draft invoices from team members.

## Purpose

An invoice without a clear narrative is a billing dispute waiting to happen. Clients — especially sophisticated corporate clients — want to understand what they paid for. A well-structured matter summary serves three functions:
1. **Transparency**: client sees the work performed and can verify value.
2. **Defensibility**: if the invoice is disputed, the summary is the primary evidence.
3. **Relationship maintenance**: a clear, well-organized invoice is a client service touchpoint.

## Required inputs

| Input | Source |
|---|---|
| Matter ID + client name | eFirm matter record |
| Billing period | Finance/billing system |
| Time entries for the period (all timekeepers) | Billing system WIP extract |
| Expense entries for the period | Billing system expense ledger |
| Applicable rate card | Engagement letter |
| Any pre-billing write-down instructions | Partner review notes |
| Prior invoice date and amount (for running total) | Billing system |

## Pre-billing review

Before generating the invoice, the responsible partner should review all time entries for the period and:

1. **Narrative quality**: each time entry must have a clear, non-generic description. Bad: "Reviewing documents." Good: "Reviewing due diligence materials (share register, corporate resolutions, property title deeds) and drafting summary memorandum for client."
2. **Time reasonableness**: flag any entry that appears disproportionate to the task described.
3. **Write-down candidates**: entries for internal meetings, training, or administrative tasks that clients typically object to.
4. **Expense verification**: confirm all expenses have receipts and are within the engagement scope.
5. **Duplicate detection**: flag any time entries that appear to duplicate other entries.

The pre-billing review is the last gate before write-downs are permanent.

## Matter summary structure

### Cover page

```
MATTER SUMMARY AND INVOICE

To:          [Client Legal Name]
From:        [Firm Name]
Date:        [Invoice Date]
Matter:      [Matter Number] — [Matter Title]
Period:      [From Date] to [To Date]
Invoice No.: [Invoice Number]
```

### Executive summary (1 paragraph)

Plain-language description of the work performed in the billing period. Written for a non-lawyer reader. Focus on outcomes and progress, not legal procedure.

Example:
> During [Month], we completed the share purchase agreement and all ancillary documents for the acquisition of [Target] by [Acquirer]. We negotiated the indemnity provisions with counterparty counsel over three sessions, resolved the regulatory pre-approval requirement with the relevant authority, and supported your team in preparing the management accounts required for the conditions precedent to be satisfied. The transaction is on track for execution in [Month].

### Time summary by timekeeper

```
PROFESSIONAL FEES

Timekeeper          | Level          | Hours | Rate ($/hr) | Amount
─────────────────────────────────────────────────────────────────────
[Name 1]            | Partner        | X.X   | $Y          | $Z
[Name 2]            | Senior Assoc.  | X.X   | $Y          | $Z
[Name 3]            | Associate      | X.X   | $Y          | $Z
─────────────────────────────────────────────────────────────────────
TOTAL FEES                          | X.X   |             | $T
Less: write-down    |               |       |             | ($W)
─────────────────────────────────────────────────────────────────────
NET FEES                                                   | $N
```

### Detailed time entries (if client billing guidelines require)

Listed chronologically per timekeeper, with:
- Date
- Timekeeper name
- Description of work
- Hours
- Amount

Clients with billing guidelines (common for large corporate and PE clients) may specify that all entries must meet minimum description standards. Build those requirements into the time-entry narration process upstream.

### Expense summary

```
DISBURSEMENTS

Description                     | Amount
────────────────────────────────────────
Court filing fees                | $X
Translation services             | $Y
Travel — [trip description]      | $Z
────────────────────────────────────────
TOTAL DISBURSEMENTS              | $D
```

### Invoice total

```
INVOICE SUMMARY

Professional fees (net):    $N
Disbursements:              $D
Sub-total:                  $S
VAT ([rate]%):              $V
────────────────────────────────
TOTAL DUE:                  $T

Payment terms:  Net [30] days
Payment to:     [Bank details]
```

### Running totals (optional but recommended)

```
CUMULATIVE FEES — [Matter] — [Date]

Fees invoiced to date (prior periods):  $X
This invoice:                           $Y
Total invoiced to date:                 $Z
Estimated remaining to completion:      $A–$B
```

Clients appreciate seeing the running total — it confirms budget tracking and avoids surprise at final invoice.

## Billing guideline compliance

Many institutional clients impose billing guidelines that govern:
- Minimum description standard per time entry
- Maximum number of timekeepers on certain tasks
- No charges for administrative tasks (filing, scheduling)
- Travel time billed at 50% or not at all
- No charges for multiple lawyers attending the same meeting unless pre-approved

If the client has billing guidelines, the pre-billing review must check each entry against them. Non-compliant entries should be adjusted before invoicing — clients who receive non-compliant invoices will deduct automatically or require a revised invoice.

## Common mistakes

- **Generic descriptions**: "Legal research" and "telephone call" are insufficient in most billing cultures. Describe the substance.
- **Block billing**: combining multiple tasks in one time entry with a single time value is prohibited by many billing guidelines.
- **Rounding up**: minor rounding is acceptable (to nearest 0.1 hr); systematic rounding up is an ethics issue.
- **Late billing**: invoicing work from 3+ months ago without explanation raises client suspicion.
- **No write-down on over-staffed matters**: if the matter was over-staffed (3 timekeepers where 1 was needed), do not pass the inefficiency to the client.

## Related skills

- [[efirm-finance-wip-aging-report]]
- [[efirm-finance-realization-rate-tracker]]
- [[efirm-client-update-email-draft]]
- [[efirm-matter-creation-flow]]
- [[efirm-finance-trust-account-reconciliation]]
