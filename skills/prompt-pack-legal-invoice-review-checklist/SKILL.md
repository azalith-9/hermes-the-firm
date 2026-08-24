---
name: prompt-pack-legal-invoice-review-checklist
description: Use when a legal department needs to review outside counsel invoices for compliance with billing guidelines, rate approvals, task coding, block billing, and excessive charges. Produces a structured checklist and review workflow covering first-pass automated checks through manual counsel review and approval. Applicable to any in-house legal team managing outside counsel spend.
license: MIT
metadata: " id: prompt-pack.legal-invoice-review-checklist category: prompt-pack practice_area: legal-ops-billing priority: P2 intent: [review, legal-invoice-review-checklist] related: - prompt-pack-outside-counsel-guidelines - prompt-pack-legal-budget-forecast - prompt-pack-matter-budget-template - prompt-pack-legal-department-kpi-dashboard source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'prompt-pack'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Legal Invoice Review Checklist

## When to use this

Use this skill when a legal operations team or responsible counsel is reviewing invoices submitted by outside counsel. The checklist ensures invoices comply with billing guidelines, identify non-compliant charges, and feeds into the approval workflow before payment is authorized.

Triggers:
- "Review this outside counsel invoice for billing guideline compliance."
- "We're getting invoices with block billing — how do we flag and handle this?"
- "Build an invoice review process for our legal department."

## Required inputs

| Input | Why it matters | Default |
|---|---|---|
| Outside Counsel Guidelines (OCGs) in use | Determines what billing practices are prohibited; rates approved | Company's current OCGs |
| E-billing platform (if any) | Determines which checks are automated vs manual | Manual if none |
| Invoice submitted | The actual invoice to be reviewed | Provided by user |
| Matter budget (if any) | Enables budget-to-actual comparison | None — note if unavailable |
| Approved timekeeper rates | Confirms rate compliance | From OCGs or rate schedule on file |

## Checklist — Phase 1: Administrative Compliance

- [ ] Invoice submitted in the required format (LEDES 1998B, LEDES 2000, PDF per guidelines, or other specified format)
- [ ] Invoice number and date present
- [ ] Matter number / matter name matches the company's matter management system reference
- [ ] Billing period clearly stated (dates from / to)
- [ ] Firm name and billing address match engagement letter
- [ ] Invoice total matches line-item sum (arithmetic check)
- [ ] Currency stated and matches approved billing currency for matter

## Checklist — Phase 2: Timekeeper Rate Compliance

- [ ] Each timekeeper identified by name, title/level (Partner, Senior Associate, Associate, Paralegal, etc.)
- [ ] Each timekeeper's hourly rate matches the approved rate schedule on file
- [ ] Rate increases applied without prior written approval are flagged and reduced to approved rate
- [ ] No rate increases applied retroactively to previously approved invoices
- [ ] Timekeepers not previously approved are flagged (new staffers require pre-approval under most OCGs)

## Checklist — Phase 3: Task Code and Billing Code Compliance

- [ ] All time entries carry UTBMS task codes (Phase, Task, Activity) if required by OCGs
- [ ] Task codes match the work described in the narrative (e.g., L120 Analysis/Strategy should not cover L210 Pleadings work)
- [ ] Expense entries carry appropriate UTBMS expense codes (E101 Copying, E106 Online Research, etc.)
- [ ] No catch-all or generic task codes used as a substitute for proper description

## Checklist — Phase 4: Block Billing Violations

Block billing occurs when a timekeeper records multiple distinct tasks as a single time entry without specifying the time spent on each. This makes it impossible to assess reasonableness.

- [ ] Identify any time entries exceeding [2 hours] that bundle multiple tasks without per-task time breakdown
- [ ] Flag all entries with conjunctions ("and," "reviewed and drafted," "conference and follow-up") that bundle distinct activities
- [ ] For each block billing entry: request a narrative breakdown from the firm or apply a standard reduction (many OCGs specify a 10–25% reduction for block billing entries)
- [ ] Note pattern if block billing is systematic rather than isolated

## Checklist — Phase 5: Excessive and Non-Compliant Charges

**Time-based issues**:
- [ ] Entries exceeding [10 hours] in a single day — flag for reasonableness review
- [ ] Minimum billing increments exceed guideline maximum (e.g., OCG sets 0.1-hour minimum; firm bills in 0.25-hour increments)
- [ ] Administrative tasks billed at attorney rates (filing, scheduling, form completion)
- [ ] Excessive intra-firm conferences or team meetings (multiple timekeepers billing for the same internal discussion)

**Staffing issues**:
- [ ] Overstaffing: multiple senior timekeepers on routine tasks
- [ ] Excessive supervision time billed for supervising junior timekeepers on straightforward work
- [ ] Associate work that should have been handled by a paralegal

**Research issues**:
- [ ] Excessive legal research on settled or basic issues
- [ ] Research billed that should have been covered by the firm's existing knowledge base

**Expense issues**:
- [ ] First-class travel billed (typically prohibited under OCGs; economy class or business for flights over a defined hour threshold)
- [ ] Meals exceeding per diem thresholds
- [ ] Mark-up on photocopying, scanning, or document costs (many OCGs prohibit any mark-up on pass-through costs)
- [ ] Internal firm charges billed as disbursements (internal printing, word processing, secretarial overtime — typically prohibited)
- [ ] Courier / overnight delivery without explanation of urgency

## Checklist — Phase 6: Budget Compliance

- [ ] Invoice total keeps cumulative billings within approved matter budget
- [ ] If cumulative billing approaches or exceeds budget: confirm whether budget increase was pre-approved
- [ ] Budget alert triggered if invoice would bring total spend above [80%] of budget — requires responsible counsel notification

## Checklist — Phase 7: Guideline Compliance — Other Provisions

- [ ] New matter opened by firm only after written authorization received from legal department
- [ ] No work performed before a signed engagement letter or SOW exists for new matters
- [ ] Privilege log entries where time entries describe potentially privileged work protected from disclosure

## Approval Workflow

| Step | Action | Owner | Timing |
|---|---|---|---|
| 1 | Automated first-pass review (if e-billing platform used) | Legal Ops / e-billing system | On submission |
| 2 | Manual review against checklist | Legal Ops or assigned paralegal | Within [5] business days |
| 3 | Flag disputed line items | Legal Ops | Before approval |
| 4 | Responsible attorney review of flagged items | Assigned counsel | Within [3] business days of flag |
| 5 | Communicate adjustment / rejection to firm | Legal Ops | Before final approval |
| 6 | Final approval and payment authorization | GC or delegated approver per authorization matrix | Per payment terms |

## Output format

For each invoice reviewed, produce a review memo with:
1. Invoice reference and billing period
2. Total billed amount
3. Amount approved for payment
4. Amount disputed / reduced
5. Reduction rationale (itemized by category: block billing, rate non-compliance, excessive charges, etc.)
6. Action: Approve / Approve with adjustment / Reject and return to firm

## MENA considerations

- Many MENA-region law firms do not routinely use LEDES billing codes; if the company requires electronic billing, this must be stated in the OCGs and the invoice review process must accommodate non-LEDES invoices from local counsel.
- For KSA and UAE local counsel: Arabic-language invoices should be reviewed with a bilingual reviewer or translated before applying the checklist.
- Local counsel in civil-law markets (LB, EG) may bill on a matter-fee rather than hourly basis; apply a reasonableness standard to fixed fees by reference to matter complexity and outcome.

## Common mistakes

- **Approving invoices without checking approved timekeeper rate schedules**: rate creep is the most common and easiest-to-detect billing abuse.
- **Not tracking block billing reductions**: if the same firm's block billing is reduced invoice after invoice, this should trigger a meeting and OCG compliance letter.
- **No escalation process for budget overruns**: silent overruns that only surface at year-end are a governance failure; the budget alert step is essential.
- **Paying invoices before matter opening authorization**: confirms retroactive engagement practice — OCGs should require pre-approval of all new matters.

## Related skills

- [[prompt-pack-outside-counsel-guidelines]]
- [[prompt-pack-legal-budget-forecast]]
- [[prompt-pack-matter-budget-template]]
- [[prompt-pack-legal-department-kpi-dashboard]]
