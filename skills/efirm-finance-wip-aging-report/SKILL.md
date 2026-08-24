---
name: efirm-finance-wip-aging-report
description: Use when a law firm finance team needs to identify and act on unbilled work-in-progress (WIP) that is aging beyond acceptable thresholds. The skill lists all unbilled time and expenses by age bucket, matter, attorney, client, and practice area; highlights write-off candidates and clients requiring interim bills; and produces partner-facing action emails. Relevant to all law-firm jurisdictions.
license: MIT
metadata: " id: efirm-finance.WIP-aging-report category: efirm-finance jurisdictions: [__multi__] priority: P1 intent: [wip, finance, aging, billing, write-off, revenue] related: - efirm-finance-realization-rate-tracker - efirm-finance-utilization-dashboard - efirm-finance-trust-account-reconciliation - efirm-matter-summary-for-billing source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'efirm-finance'.
Registered as a flat plugin skill.
-->


# WIP Aging Report

## When to use this

Use this skill to:
- Run the monthly or weekly WIP review to identify stale unbilled time before it becomes uncollectable.
- Prepare the partner billing meeting — each partner sees their matter list sorted by WIP age.
- Identify matters where an interim bill is overdue (WIP exceeds agreed billing cadence or credit limit).
- Flag likely write-off candidates before year-end so provisions can be made.
- Monitor whether fee-capped matters are approaching their cap (remaining fee capacity vs. remaining WIP).

WIP left unbilled degrades over time: clients forget the work, dispute the descriptions, or face their own budget pressure. The longer WIP ages, the more likely it is to be written down or off.

## Core concepts

### What is WIP?

Work-in-progress (WIP) is time entered and expenses recorded against a matter that has **not yet been invoiced**. It sits on the firm's balance sheet as an asset until billed (when it becomes accounts receivable) or written off (when it becomes a loss).

### Age buckets

| Bucket | Days since entry | Risk level |
|---|---|---|
| Current | 0–30 | Low — normal billing pipeline |
| Aging | 31–60 | Moderate — follow up with billing partner |
| Old | 61–90 | High — requires reason; consider interim bill |
| Stale | 91–180 | Very high — write-off candidate unless justified |
| Critical | 180+ | Near-certain write-off territory; escalate to managing partner |

Firms set their own thresholds; the above are common defaults. Adjust to firm billing policy.

## Required inputs

| Input | Source |
|---|---|
| WIP extract from billing system (all unbilled entries) | Billing system (Clio, Elite, Aderant, etc.) |
| Matter details (client, practice area, responsible partner) | Matter database |
| Billing policy thresholds (WIP credit limit, billing cadence) | Firm policy document |
| Fee-cap / budget amount per matter (if applicable) | Engagement letter or fee quote |
| Prior WIP report (optional, for trend comparison) | Prior period file |

## Report structure

### Summary dashboard

```
WIP AGING REPORT — [Firm] — [Report Date]

AGE BUCKET    | # Matters | WIP $ Value | % of Total WIP
─────────────────────────────────────────────────────────
0–30 days     |           |             |
31–60 days    |           |             |
61–90 days    |           |             |
91–180 days   |           |             |
180+ days     |           |             |
─────────────────────────────────────────────────────────
TOTAL         |           |             | 100%

FLAGS: [count of matters in each flag category — see below]
```

### Detail: by matter (drill-down)

For each matter in the 61+ day buckets:

```
Matter:            [ID / Short Title]
Client:            [Name]
Practice:          [Group]
Responsible:       [Partner]
Total WIP:         $X
  — Time:          $T (Y hrs × avg rate $R)
  — Expenses:      $E
Oldest entry:      [Date] ([N days ago])
Fee cap remaining: $F  (or N/A)
Billing cadence:   [Monthly / Milestone / On demand]
Last invoice:      [Date]
FLAG:              [See flag types below]
```

### By partner

Summarize total WIP by responsible partner, sorted descending, with their oldest WIP date highlighted. This is the input to partner billing meetings.

### By client

Aggregate WIP across matters per client. Flag clients whose aggregate WIP exceeds any agreed credit limit.

## Flags

| Flag | Trigger | Action |
|---|---|---|
| WIP exceeds billing cadence | WIP age > agreed billing cycle (e.g., >30 days for monthly-billing matter) | Generate interim bill |
| WIP > client credit limit | Aggregate client WIP > firm's defined credit limit for client | Hold new work until bill issued + paid; or get partner authorization |
| Stale WIP — write-off candidate | Any WIP entry >90 days (default threshold) | Partner review; write-off or produce explanation + billing plan |
| Fee-cap at risk | WIP + billed fees > 85% of matter cap | Alert responsible partner immediately; scope discussion needed |
| Inactive matter with WIP | No time entries for >60 days but WIP outstanding | Matter may be on hold or closed without billing — investigate |
| Expenses aging | Expense entries >60 days unbilled | Disburse to client ASAP; aging expenses signal billing process failure |

## Partner action email

For each partner with flagged WIP, the skill generates a draft email:

```
Subject: WIP Review Action Required — [Partner Name] — [Month]

Dear [Partner],

Your current WIP summary as of [Date]:

  Total WIP:           $X
  WIP in 60+ buckets:  $Y ([Z]% of your total)
  Matters requiring action:

  1. [Matter 001] — $A WIP — [Flag: Stale / Cap risk / Credit limit]
     Suggested action: [Issue interim invoice / write off $B / partner note required]

  2. [Matter 002] — $B WIP — [Flag]
     Suggested action: [...]

Please confirm actions by [Date]. Finance will process approved write-offs and bills
in the [Month] billing cycle.

[Finance Team]
```

## Year-end considerations

- **WIP provision**: Stale WIP (90+ days) should be provisioned at a discount (commonly 50–100% depending on age and client history) for financial reporting purposes.
- **Revenue recognition** (US GAAP / IFRS 15): Law firms must assess whether WIP is realizable; firms using cash-basis accounting write off WIP when it is determined not collectible.
- **Tax**: Write-offs must be documented with partner sign-off to support tax deduction in most jurisdictions.

## Jurisdictional notes

- **MENA practices**: Year-end timing varies across the GCC (Hijri year vs. Gregorian). Run WIP aging using Gregorian calendar for international billing, but align internal review with firm's fiscal year.
- **Lebanon**: Currency considerations require WIP denominated in USD vs. LBP to be tracked separately; assess collectibility in functional currency.
- **UK SRA**: Firms using the SRA-compliant billing ledger must ensure WIP descriptions are sufficiently detailed to support the invoice narrative requirements.

## Related skills

- [[efirm-finance-realization-rate-tracker]]
- [[efirm-finance-utilization-dashboard]]
- [[efirm-finance-trust-account-reconciliation]]
- [[efirm-matter-summary-for-billing]]
- [[efirm-finance-partner-comp-allocator]]
