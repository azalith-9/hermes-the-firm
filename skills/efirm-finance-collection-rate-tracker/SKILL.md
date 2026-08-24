---
name: efirm-finance-collection-rate-tracker
description: Use when a law firm needs to track and analyze accounts receivable performance — measuring collection rates (billed-to-collected ratio), Days Sales Outstanding (DSO), write-down percentages, and aging buckets across clients, practice areas, attorneys, and time periods. Identifies early-warning signals for clients with deteriorating collection trends, highlights stale AR over 120 days for write-off decision, and generates AR-chase email drafts. Applies to any law firm in any jurisdiction with time-billed matters.
license: MIT
metadata: " id: efirm-finance.collection-rate-tracker category: efirm-finance jurisdictions: [__multi__] priority: P1 intent: [collection, ar, accounts receivable, dso, write-off, billing performance] related: [efirm-finance-invoice-generator-from-time-entries, efirm-finance-budget-vs-actual-matter, efirm-finance-ewallet-balance-checker] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'efirm-finance'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Collection Rate Tracker

Collection rate — the ratio of fees collected to fees billed — is one of the three key financial metrics for any law firm (alongside realization rate and utilization). A firm that bills well but collects poorly is effectively working for free. This skill generates a real-time collection dashboard by client, practice area, attorney, and time period, with early-warning signals and automated AR-chase drafts.

## When to use this

- Monthly financial close: review collection performance across all open matters
- Quarterly partner review: present AR aging and collection trends to the management committee
- Annual client review: identify clients whose payment behavior has deteriorated (a risk signal for the relationship)
- Before taking on a new matter for a client with a history of payment issues
- As part of the billing workflow to identify invoices approaching the 90-day stale threshold

## Metrics Tracked

### 1. Collection Rate (%)
```
Collection rate = Total fees collected ÷ Total fees billed × 100
```
Measured by: client; practice area; attorney; time period (month / quarter / YTD / rolling 12 months).

**Industry benchmarks:**
- Elite law firms: 92–96% collection rate
- Mid-size firms: 85–92%
- Sole practitioners / small firms: 75–88%
- Below 80%: collection problem that needs management attention

### 2. Days Sales Outstanding (DSO)
```
DSO = (Total AR balance ÷ Total fees billed in the period) × Number of days in the period
```

DSO measures how long, on average, it takes to collect a billed dollar.

**Target**: DSO below 60 days is healthy. DSO above 90 days indicates a collection problem.

**Interpretation**: if DSO increases period-over-period, the firm is collecting more slowly — may indicate client financial stress, billing disputes, or inadequate follow-up.

### 3. Write-Down Rate (%)
```
Write-down rate = Total amounts written down ÷ Total amounts billed × 100
```

Write-downs occur when the firm reduces an invoice (before sending) or reduces the outstanding AR (after sending). Persistent write-downs on a specific client or matter type indicate systematic overcharging, scope creep, or inefficient delivery.

### 4. AR Aging Buckets

Standard aging analysis:

| Bucket | Days outstanding | Status |
|---|---|---|
| Current | 0–30 days | Normal |
| Past due — early | 31–60 days | Monitor |
| Past due — medium | 61–90 days | Chase |
| Past due — late | 91–120 days | Escalate; consider interest |
| Stale | >120 days | Write-off assessment; legal action? |

## Dashboard Output

### Collection Rate Dashboard

```
COLLECTION RATE REPORT
Period: [Month/Quarter/YTD]     Date: [Dashboard Date]
─────────────────────────────────────────────────────────────────────
                      BILLED      COLLECTED   COLL%    DSO     W-DOWN%
─────────────────────────────────────────────────────────────────────
BY CLIENT
[Client A]            [Amount]    [Amount]    [X]%     [X]d    [X]%
[Client B]            [Amount]    [Amount]    [X]%     [X]d    [X]%
[Client C]            [Amount]    [Amount]    [X]%     [X]d    [X]%

BY PRACTICE AREA
Corporate             [Amount]    [Amount]    [X]%     [X]d    [X]%
Litigation            [Amount]    [Amount]    [X]%     [X]d    [X]%
Employment            [Amount]    [Amount]    [X]%     [X]d    [X]%

BY ATTORNEY (BILLING PARTNER)
[Partner A]           [Amount]    [Amount]    [X]%     [X]d    [X]%
[Partner B]           [Amount]    [Amount]    [X]%     [X]d    [X]%

FIRM TOTAL            [Amount]    [Amount]    [X]%     [X]d    [X]%
─────────────────────────────────────────────────────────────────────
Prior period TOTAL    [Amount]    [Amount]    [X]%     [X]d    [X]%
YOY change                                   [+/-X]pp [+/-X]d [+/-X]pp
```

### AR Aging Report

```
AR AGING SUMMARY
Date: [Date]
─────────────────────────────────────────────────────────────────────
Client          Invoice#   Inv Date   Amount     Bucket         Status
─────────────   ────────   ────────   ──────     ──────         ──────
[Client A]      [Inv-001]  [Date]     [Amount]   31–60 days     Monitor
[Client B]      [Inv-023]  [Date]     [Amount]   61–90 days     Chase
[Client B]      [Inv-019]  [Date]     [Amount]   91–120 days    Escalate
[Client C]      [Inv-008]  [Date]     [Amount]   >120 days      Write-off?
─────────────────────────────────────────────────────────────────────
TOTAL STALE AR (>120 days):           [Amount]
```

## Early Warning Signals

| Signal | Trigger | Interpretation | Action |
|---|---|---|---|
| Deteriorating collection trend | Client's collection rate drops >10pp quarter-over-quarter | Client may be experiencing financial difficulty; or relationship issue | Billing partner review; proactive call to client |
| Disputed billing | Client pays less than invoiced amount; no formal dispute raised | Client disagrees with the fee; opportunity for early resolution | Contact client; understand the issue; resolve or issue revised invoice |
| Repeated >60-day payment | Client consistently pays at 60–90 days | Cash flow management by client; or low priority on law firm payments | Negotiate payment terms; or require retainer top-up |
| Stale AR >120 days | Invoice not paid or disputed after 120 days | Write-off risk; relationship issue; potential insolvency | Partner assessment: chase, write-off, or instruct collection |
| High write-down on specific matter | Matter write-down >15% | Structural overbilling or scope-definition problem | Partner review of matter economics; pricing adjustment for future work |

## AR Chase Email Drafts (Auto-Generated)

### Gentle reminder (31–60 days)
```
Subject: Invoice [Number] — Gentle Reminder

Dear [Client name / AP contact],

I hope you are well. I wanted to follow up on Invoice [Number] dated [Date] 
for [Amount], which appears to be outstanding.

Please let me know if you have any questions about the invoice or if there 
is anything you need from our side to facilitate payment.

If payment has already been made, please disregard this message.

Kind regards,
[Billing Partner / Finance team]
```

### Formal chase (61–90 days)
```
Subject: Invoice [Number] — Payment Overdue

Dear [Client name / Finance Director],

Our records show that Invoice [Number] dated [Date] for [Amount] remains 
outstanding, now [X] days past our [30-day] payment terms.

We would be grateful for payment by [Date — typically 7 days from this email], 
or please contact me to discuss if there is a query.

Kind regards,
[Partner Name]
```

### Escalation (91–120 days)
```
Subject: Invoice [Number] — Urgent Payment Required

Dear [Client name],

I am writing regarding Invoice [Number] for [Amount], which is now 
[X] days overdue.

We have not received payment or a response to our prior reminders. Please 
contact me directly by [Date] to arrange payment or discuss this outstanding 
balance. Failure to do so may result in [the matter being placed on hold / 
referral to our collections process / accrual of interest at [X]% per annum 
per our engagement letter].

[Partner Name] — Direct: [Phone / Email]
```

### Write-off decision memo (>120 days)
Internal memo for the billing partner / management committee:
```
WRITE-OFF ASSESSMENT MEMO

Client: [Name]   Matter: [Name]   Invoice: [Number]   Amount: [Amount]
Days outstanding: [X]

History: [Summary of chase attempts and responses]

Recommendation: [Write off / Continue chase / Instruct external collection / 
                 Instruct legal proceedings]

Partner approval: ___________________   Date: ____________
```

## Related skills

- [[efirm-finance-invoice-generator-from-time-entries]]
- [[efirm-finance-budget-vs-actual-matter]]
- [[efirm-finance-ewallet-balance-checker]]
