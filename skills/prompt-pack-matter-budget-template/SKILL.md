---
name: prompt-pack-matter-budget-template
description: Use when preparing a per-matter legal budget for a specific litigation, arbitration, transaction, or regulatory matter. Produces a template with phase/task breakdowns, estimated hours by timekeeper level, disbursements, contingency, key assumptions, and alignment with LEDES/UTBMS billing codes. Applicable to outside counsel preparing client budgets and in-house teams evaluating external counsel proposals.
license: MIT
metadata: " id: prompt-pack.matter-budget-template category: prompt-pack practice_area: legal-ops-billing priority: P2 intent: [operations, matter-budget-template] related: - prompt-pack-legal-budget-forecast - prompt-pack-legal-invoice-review-checklist - prompt-pack-outside-counsel-guidelines - prompt-pack-legal-department-kpi-dashboard - prompt-pack-matter-closing-procedure source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'prompt-pack'.
Registered as a flat plugin skill.
-->


# Matter Budget Template

## When to use this

Use this skill when outside counsel needs to provide a client with a matter budget for a specific engagement, or when an in-house team needs to evaluate and document the expected cost of a new matter before instructing external counsel.

Triggers:
- "Prepare a budget estimate for litigating [matter]."
- "Our outside counsel sent a budget — help me review and structure it."
- "I need a matter budget template aligned to UTBMS codes."
- "Draft a transaction budget for the [acquisition] deal."

## Required inputs

| Input | Why it matters | Default |
|---|---|---|
| Matter name and description | Identifies and scopes the budget | Ask user |
| Matter type | Litigation / arbitration / transaction / regulatory / advisory | Ask user |
| Phase/task breakdown | Core structure of the budget | Use standard UTBMS phases for the matter type |
| Timekeeper levels available | Determines which rate tiers appear in the budget | Ask user or use standard tiers |
| Approved rates | Either from OCG rate schedule or quoted rates | Ask user |
| Jurisdiction | Affects expected disbursements (court filing fees, expert rates) | Ask user |

## Optional inputs

- Billing code standard: LEDES 1998B, LEDES 2000, LEDES Timekeeper, or non-LEDES
- Budget format: fixed fee / time-and-materials / phased capped / hybrid
- Alternative fee arrangement (AFA): fixed fee per phase, success fee, blended rate
- Risk adjustment: probability-weighted scenario analysis
- Currency

## Budget template — Litigation / Arbitration

### Matter Information
| Field | Details |
|---|---|
| Matter name | |
| Client | |
| Counsel / Firm | |
| Budget date | |
| Budget period | [Phase 1 only / Through first hearing / Full case] |
| Governing law | |
| Assumed venue | |
| Budget type | Time-and-materials (estimated) / Capped / Fixed fee |

### Phase and Task Budget

For litigation use UTBMS L-codes; for transactions use UTBMS A/P codes.

**Phase L100: Case Assessment, Development, and Administration**

| Task | UTBMS Code | Lead Timekeeper | Hours (est.) | Rate (USD/hr) | Estimated Fee |
|---|---|---|---|---|---|
| Initial case assessment | L110 | Partner | | | |
| Fact investigation | L120 | Sr. Associate | | | |
| Legal research | L120 | Associate | | | |
| Case strategy and planning | L120 | Partner | | | |
| Document management / organization | L140 | Paralegal | | | |
| **Phase L100 subtotal** | | | | | |

**Phase L200: Pleadings**

| Task | UTBMS Code | Lead Timekeeper | Hours (est.) | Rate | Estimated Fee |
|---|---|---|---|---|---|
| Draft complaint / statement of claim | L210 | Partner / Sr. Associate | | | |
| Draft answer / defense | L210 | Sr. Associate | | | |
| Preliminary motions / jurisdictional challenges | L210 | Partner | | | |
| **Phase L200 subtotal** | | | | | |

**Phase L300: Discovery / Disclosure**

| Task | UTBMS Code | Lead Timekeeper | Hours (est.) | Rate | Estimated Fee |
|---|---|---|---|---|---|
| Prepare / respond to document requests | L310 | Associate / Paralegal | | | |
| Document review | L320 | Associate | | | |
| Depositions / witness interviews | L330 | Partner / Sr. Associate | | | |
| Expert reports | L340 | Partner (coordination) | | | |
| **Phase L300 subtotal** | | | | | |

**Phase L400: Trial / Hearing Preparation and Trial**

| Task | UTBMS Code | Lead Timekeeper | Hours (est.) | Rate | Estimated Fee |
|---|---|---|---|---|---|
| Pre-hearing motions / briefs | L420 | Partner | | | |
| Witness preparation | L450 | Partner / Sr. Associate | | | |
| Hearing attendance (days × daily rate) | L450 | Partner + Associate | | | |
| Post-hearing brief | L460 | Partner / Sr. Associate | | | |
| **Phase L400 subtotal** | | | | | |

**Phase L500: Appeal** (if applicable)

| Task | UTBMS Code | Lead Timekeeper | Hours (est.) | Rate | Estimated Fee |
|---|---|---|---|---|---|
| Notice of appeal | L510 | Partner | | | |
| Appellate brief | L510 | Partner / Sr. Associate | | | |
| Oral argument | L520 | Partner | | | |
| **Phase L500 subtotal** | | | | | |

### Disbursements / Expenses

| Expense category | UTBMS Code | Estimated amount | Notes |
|---|---|---|---|
| Court / tribunal filing fees | E112 | | Confirm current fee schedule |
| Expert witness fees | E119 | | Estimate from expert |
| Travel and accommodation | E110 / E111 | | Economy class per OCG |
| Document production / e-discovery platform | E101 / E106 | | Per-GB pricing estimate |
| Interpreters / translation | | | If applicable |
| Process server / enforcement fees | E112 | | |
| Other | | | |
| **Disbursements subtotal** | | | |

### Budget Summary

| Category | Estimated amount | Notes |
|---|---|---|
| Phase L100 | | |
| Phase L200 | | |
| Phase L300 | | |
| Phase L400 | | |
| Phase L500 (if applicable) | | |
| Disbursements | | |
| **Fees + Disbursements subtotal** | | |
| Contingency (typically 10–15%) | | |
| **Total estimated budget** | | |

### Key Assumptions

State all material assumptions on which the budget is based. The budget is only as reliable as these assumptions; if they change, the budget should be revised.

1. This budget covers Phase [X] only / the full case through [award/judgment].
2. No third-party disclosure order is required.
3. Number of witnesses to be deposed/heard: [X].
4. Document volume estimate: [X documents / GB of data].
5. Expert witnesses: [X experts in [X fields]; budget does not include expert fees unless separately stated].
6. Settlement discussions: this budget does not include costs of mediation or settlement negotiation.
7. Regulatory or parallel proceedings: not included unless specified.
8. The other side does not bring a counterclaim of material complexity.
9. Rates are per the approved rate schedule as at [date]; rate adjustments will be addressed by amendment.

### Budget Update Triggers

Outside counsel undertakes to notify the client promptly if:
- Actual costs in any phase approach 80% of the phase budget
- An event occurs that materially changes the scope or complexity of the matter
- The matter proceeds to a phase not originally budgeted

Budget revisions require written agreement from the client before the new budget ceiling is exceeded.

## MENA considerations

- **Expert witnesses in UAE / KSA courts**: court-appointed experts are common and can significantly affect the budget; include a line for responding to court expert reports.
- **Arabic translation costs**: all documents submitted to UAE or KSA courts must be in Arabic or translated with a certified translator; translation costs can be substantial for document-heavy cases.
- **DIAC / ADCCAC arbitration fees**: arbitration institution fees in MENA are calculated as a percentage of the claim amount; include institutional fees as a separate line item.
- **Travel costs for MENA-based hearings**: regional hearings in Dubai, Riyadh, or Beirut involve international travel for international counsel teams; estimate realistically.

## Common mistakes

- **Omitting the assumptions section**: a budget without stated assumptions is meaningless; counsel will always find a reason why costs exceeded budget if assumptions are not pinned down.
- **Not including disbursements**: attorney fees are always presented; disbursements (expert fees, filing fees, translation) can add 20–40% to the total cost.
- **No contingency**: all litigation budgets should carry a contingency; absent one, the first complication produces a budget overrun.
- **Not updating the budget when scope changes**: a budget issued at case inception should be revised at each phase gate; use budget update triggers to formalize this.

## Related skills

- [[prompt-pack-legal-budget-forecast]]
- [[prompt-pack-legal-invoice-review-checklist]]
- [[prompt-pack-outside-counsel-guidelines]]
- [[prompt-pack-legal-department-kpi-dashboard]]
- [[prompt-pack-matter-closing-procedure]]
