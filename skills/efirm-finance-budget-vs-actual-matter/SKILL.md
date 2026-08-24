---
name: efirm-finance-budget-vs-actual-matter
description: Use when a law firm needs to track and report on budget versus actual spend for an open matter. Produces a dashboard showing budget by phase, actual hours and fees by phase, variance (absolute and percentage), burn rate, projected-at-completion estimate, and recommended management actions. Triggers automatic alerts when the budget threshold is exceeded or burn rate is off plan. Designed for use by billing partners and matter supervisors to catch overruns before they become client-relationship problems.
license: MIT
metadata: " id: efirm-finance.budget-vs-actual-matter category: efirm-finance jurisdictions: [__multi__] priority: P1 intent: [budget, matter management, fee tracking, variance analysis, burn rate, budget overrun] related: [efirm-finance-afa-quote-builder, efirm-finance-billing-narrative-cleanup, efirm-finance-invoice-generator-from-time-entries, efirm-finance-collection-rate-tracker] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'efirm-finance'.
Registered as a flat plugin skill.
-->


# Budget vs Actual — Matter Dashboard

Budget management is the leading cause of client-firm relationship deterioration. A client who receives an invoice significantly above the budget estimate did not get a surprise — they got a relationship problem. This skill generates a live budget dashboard for each matter with a budget, with automatic alerts and recommended actions when the burn rate or variance cross defined thresholds.

## When to use this

- Monthly matter review for any matter with an approved budget
- Before preparing a client status report (to include financial update)
- Before sending an invoice when the matter is near or over budget
- When the billing partner suspects a phase is running over
- During partner-associate weekly matter reviews

## Required inputs

| Input | Notes |
|---|---|
| Matter identifier | Client/matter number |
| Budget by phase | Approved budget for each phase (dollar amount and/or hours) |
| Actual time entries | All recorded hours and fees to date, by phase |
| Billing rates | By timekeeper and seniority level |
| Phase status | Which phases are complete; which are in progress; which are pending |
| Timeline | Planned start and end date per phase; actual start dates |

## Dashboard Output

### Matter Financial Summary

```
MATTER FINANCIAL DASHBOARD
Matter: [Client / Matter Name]       Date: [Dashboard Date]
Partner: [Name]                      Status: [Active / Phase 2 of 4]
─────────────────────────────────────────────────────────────────────
                          BUDGET     ACTUAL    VARIANCE     VARIANCE%
─────────────────────────────────────────────────────────────────────
Phase 1: Due Diligence    [Amount]   [Amount]  [+/-Amt]     [+/-X%]
Phase 2: Documentation    [Amount]   [Amount]  [+/-Amt]     [+/-X%]
Phase 3: Negotiation      [Amount]   [Amount]  [+/-Amt]     [+/-X%]
Phase 4: Closing          [Amount]   [Amount]  N/A (future) N/A
─────────────────────────────────────────────────────────────────────
TOTAL BUDGET              [Amount]   [Amount]  [+/-Amt]     [+/-X%]
─────────────────────────────────────────────────────────────────────
% of total budget consumed: [X]%
Projected total at completion: [Amount]  ([+/-Y]% vs budget)
```

### Burn Rate Analysis

```
BURN RATE ANALYSIS
─────────────────────────────────────────────────────────────────────
Current phase:             Phase 2 — Documentation
Phase budget:              [Amount]
Phase start date:          [Date]
Phase planned duration:    [X] weeks
Phase elapsed:             [Y] weeks
─────────────────────────────────────────────────────────────────────
Planned burn rate:         [Amount / week]
Actual burn rate:          [Amount / week]
Variance from planned:     [+/-X]% per week
─────────────────────────────────────────────────────────────────────
At current burn rate, phase will complete at: [Projected amount]
vs phase budget:           [+/-Amount]  [OK / ALERT]
```

### Team Utilization by Role

```
TEAM UTILIZATION
─────────────────────────────────────────────────────────────────────
Role           Budget hrs   Actual hrs    Remaining hrs   % Used
─────────────  ──────────   ──────────    ─────────────   ──────
Partner        [X] hrs      [Y] hrs       [Z] hrs         [%]
Sr Associate   [X] hrs      [Y] hrs       [Z] hrs         [%]
Associate      [X] hrs      [Y] hrs       [Z] hrs         [%]
Paralegal      [X] hrs      [Y] hrs       [Z] hrs         [%]
─────────────────────────────────────────────────────────────────────
```

## Alert Thresholds and Triggers

| Alert | Trigger condition | Recommended action |
|---|---|---|
| Budget threshold | >80% of total matter budget consumed | Contact client immediately; provide updated estimate; obtain authorization before incurring further fees above budget |
| Phase overrun | Individual phase exceeds budget by >20% | Investigate cause; discuss with team; assess whether remaining phases are also at risk |
| Burn rate acceleration | Current week's burn rate >125% of planned pace | Review scope; identify if unplanned work is driving the acceleration |
| Phase under-burn | Phase complete but <70% of phase budget used | Carry-forward analysis: can savings be applied to a later phase? Return to client? Credit to a future matter? |
| Matter stalled | No time entries for [X] business days when phase is in progress | Investigate; may indicate team availability issue or waiting on client |

## Recommended Actions by Scenario

### Scenario A: Matter at 85% of budget with Phase 3 still to complete

**Action:**
1. Partner calls or emails client immediately — do not send a surprise invoice
2. Prepare an updated budget estimate for Phase 3 (revised range: low / mid / high)
3. Explain the cause of variance: scope expansion? counterparty-caused extensions? unexpected regulatory requirement?
4. Request client authorization to exceed original budget by [X] — get it in writing (email is sufficient)
5. Consider converting remaining work to a fixed fee for Phase 3 to restore predictability

### Scenario B: Phase overrun due to client-caused delays

**Action:**
1. Document the delay (with dates and emails)
2. Send the client a written scope-variation notice: "The delay in receiving the corporate approvals (notified on [date]) has extended Phase 2 by [X] weeks and resulted in [Y] additional hours of team engagement. This will add approximately [Amount] to the Phase 2 fee."
3. Adjust the budget formally; keep a record
4. Issue a change order or supplemental engagement letter if the amount is material

### Scenario C: Phase under-budget — budget carry-forward opportunity

**Action:**
1. Report the under-spend in the invoice and/or status update
2. Propose carry-forward to a subsequent phase or a corresponding reduction in the fixed fee (demonstrates value and good faith)
3. Alternatively: credit toward the next matter if the client is a relationship client
4. Do not simply pocket the saving without notifying the client — in an AFA context especially, under-spending against a fixed fee is the firm's to keep, but transparency builds trust

### Scenario D: Matter projected to significantly exceed budget at completion

**Action:**
1. Prepare a write-down analysis: what is the firm willing to absorb vs charge?
2. Partner makes the client call: "We are currently tracking above budget. I want to discuss how we handle the balance — here are our options."
3. Options: firm absorbs the overrun (write-down); client authorizes additional fees; scope is reduced to fit within remaining budget; matter is phased to a natural breakpoint
4. Never let the client open the invoice and see a number significantly above budget without prior discussion

## Partner Email Draft (Auto-Generated)

When a threshold alert fires, the dashboard generates a draft email for partner review:

```
Subject: [Matter Name] — Budget Update [Date]

Dear [Client name],

I wanted to update you on the budget position for [Matter Name].

As of [date], we have incurred approximately [Amount] against a budget of 
[Amount], representing [X]% of the approved budget. The matter is currently 
in [Phase X].

[If on track:] We remain within the approved budget and the matter is on track 
to complete within the estimate.

[If approaching threshold:] Based on the remaining work in [Phase X/Y], I 
estimate that the total fees will be in the range of [low] to [high], which 
[exceeds / is at the upper end of] the approved budget of [Amount]. The 
principal driver has been [explanation].

I would welcome a brief call to discuss, or please let me know by email 
whether you wish to [authorize additional fees / adjust the scope / other].

Kind regards,
[Partner Name]
```

## Related skills

- [[efirm-finance-afa-quote-builder]]
- [[efirm-finance-billing-narrative-cleanup]]
- [[efirm-finance-invoice-generator-from-time-entries]]
- [[efirm-finance-collection-rate-tracker]]
