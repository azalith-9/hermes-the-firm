---
name: outreach-payment-recovery-flow
description: Use when a legal AI product or its law firm users need to run a structured payment recovery sequence — drafting demand letters, escalation notices, and coordinating legal action for unpaid invoices or outstanding receivables. Provides a jurisdiction-aware escalation ladder from polite reminder through formal demand to court filing. Triggers on requests to recover unpaid fees, draft demand letters, or manage debtors.
license: MIT
metadata: " id: outreach.payment-recovery-flow category: outreach intent: ['__outreach__', 'payment recovery', 'demand letter', 'debt collection', 'receivables'] related: - outreach-inbox-scan - draft-demand-letter - kb-commercial-law-uae priority: P3 source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'outreach'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Payment Recovery Flow

Unpaid invoices are a significant operational problem for law firms and legal AI products. The payment recovery flow provides a structured, jurisdiction-aware escalation ladder — from polite reminder to formal demand letter to court action — calibrated so that each step maximises recovery probability while managing relationship cost.

## Purpose

Execute a complete payment recovery sequence:
1. Initial reminder — maintain relationship, prompt payment
2. Formal reminder — signal seriousness, preserve legal position
3. Formal demand letter — create a record, trigger limitation clock if disputed
4. Pre-litigation notice — mandatory in some jurisdictions before filing
5. Court filing / arbitration referral — last resort

## Inputs

| Input | Why it matters | Required |
|---|---|---|
| Outstanding amount | Determines proportionality of recovery steps | Yes |
| Days overdue | Determines starting point on the escalation ladder | Yes |
| Governing law / jurisdiction | Controls which demand letter format and court is appropriate | Yes |
| Contract terms | Payment terms, interest rate, dispute resolution clause | Yes |
| Prior communications | Has the debtor responded? Disputed? Promised to pay? | Yes |
| Relationship status | Is this an ongoing relationship worth preserving? | Informs tone |

## Escalation ladder

### Step 1 — Friendly reminder (Day 7–14 overdue)

Tone: collegial. Assume oversight, not intent. No legal language.

```
Subject: Invoice [Number] — Quick follow-up

Hi [Name],

I wanted to follow up on Invoice [Number] for [Amount], which was due on [Date].
Could you confirm this has been processed? If there's any issue on your end, I'm happy to help sort it out.

Best,
[Name]
```

### Step 2 — Formal reminder (Day 21–30 overdue)

Tone: professional, firm. Note the overdue status. Request payment by a specific date.

```
Subject: Invoice [Number] — Payment Overdue

Dear [Name],

Invoice [Number] for [Amount], due [Date], remains outstanding. I kindly request payment by [date 7 days out].

If you have any queries about this invoice, please contact me directly.

Regards,
[Name]
```

### Step 3 — Formal demand letter (Day 45–60 overdue)

Jurisdiction-specific format. This letter creates a formal record and in many jurisdictions is a prerequisite before court action.

Key elements:
- Full party names and addresses
- Amount owed, invoice reference(s), due date(s)
- Interest accrued (if contract provides for it)
- Specific deadline for payment (typically 7–14 days)
- Statement that legal proceedings will commence if payment is not received
- No threats beyond the legal remedies available

Jurisdiction notes:

| Jurisdiction | Specific requirements |
|---|---|
| UAE | A formal demand (إنذار رسمي / Inzar Rasmi) may be required before filing at UAE courts; notarised via a Notary Public for maximum effect |
| KSA | Formal demand through official channels recommended before HRSD or court filing; notarisation adds evidentiary weight |
| Lebanon | Mise en demeure (formal notice) is a prerequisite under the Code of Obligations and Contracts for some claims |
| DIFC | No mandatory pre-action notice requirement but good practice; DIFC Small Claims Tribunal applies for claims under USD 200,000 |
| ADGM | No mandatory pre-action notice but the ADGM Courts' Practice Direction encourages pre-action correspondence |
| UK | Pre-action Protocol for Debt Claims must be followed before issuing proceedings in England and Wales |
| France | Lettre de mise en demeure — required in most contract claims before filing; may be sent by registered post or bailiff |

### Step 4 — Escalation to legal proceedings

If the formal demand produces no response:
1. File at the appropriate court or tribunal
2. For DIFC/ADGM: consider the Small Claims Tribunal for amounts under the threshold — faster and cheaper
3. For UAE onshore: Dubai Courts or Abu Dhabi Courts; Arabic filings required; translation costs apply
4. For arbitration: check the contract's dispute resolution clause — DIAC, ICC, LCIA, or bespoke

## Interest on late payment

| Jurisdiction | Applicable rate |
|---|---|
| UAE | Contract rate if specified; UAE Civil Code art 226 cap at 12% p.a. (commercial); courts have discretion |
| DIFC | Contract rate; or statutory interest per DIFC Courts rules |
| KSA | Islamic finance principles — interest (riba) is prohibited; late payment penalties must be structured as agreed damages, not interest |
| Lebanon | Legal rate; courts have discretion |
| France | Statutory rate (taux d'intérêt légal) published annually by the Ministry of Finance |
| UK | Late Payment of Commercial Debts Act 1998 — statutory rate of 8% above Bank of England base rate |

**Note for KSA:** structure any late payment provision as a "liquidated damages" or "agreed compensation" clause rather than an interest clause, to be consistent with Sharia principles.

## Quality bar

- Demand letters must not overstate the legal position or threaten remedies that are not actually available.
- Every demand letter should be reviewed by a qualified lawyer before sending, especially for amounts above USD 10,000 or where the jurisdiction requires a specific format.
- Maintain a log of all payment recovery communications — dates, content, and responses — as this becomes evidence if proceedings follow.

## Related skills

- [[outreach-inbox-scan]]
- [[draft-demand-letter]]
- [[kb-commercial-law-uae]]
- [[output-partner-memo-style]]
