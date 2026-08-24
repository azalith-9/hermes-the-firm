---
name: efirm-finance-realization-rate-tracker
description: Use when a law firm finance manager or partner needs to compute, monitor, or diagnose realization rates — the ratio of revenue actually billed and collected versus hours worked. Covers billed realization, collected realization, multi-dimensional drill-downs (by attorney, practice, client, matter type), anomaly flagging, and actionable recommendations. Pairs with collection-rate-tracker for a full revenue-cycle picture. Relevant to all law-firm jurisdictions including MENA.
license: MIT
metadata: " id: efirm-finance.realization-rate-tracker category: efirm-finance jurisdictions: [__multi__] priority: P1 intent: [realization, billing, write-down, revenue-cycle, profitability] related: - efirm-finance-collection-rate-tracker - efirm-finance-wip-aging-report - efirm-finance-utilization-dashboard - efirm-finance-partner-comp-allocator source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'efirm-finance'.
Registered as a flat plugin skill.
-->


# Realization Rate Tracker

## When to use this

Use this skill to:
- Calculate current-period realization rates across any billing dimension.
- Diagnose why firm revenue is underperforming relative to recorded hours.
- Flag specific attorneys, clients, or matter types that are consistently written down.
- Prepare materials for partner compensation discussions (write-downs attributable to individual partners).
- Support AFA (Alternative Fee Arrangement) pricing decisions with historical data.

## Concepts and metrics

### Billed realization rate

```
Billed Realization = (Amount Billed) / (Hours Worked × Hourly Rate) × 100%
```

Measures how much of the potential fee the firm actually invoiced. A rate below 100% reflects **write-downs** — hours written off before the invoice is issued, typically due to:
- Over-staffing of the matter.
- Inefficiencies the client should not bear.
- Courtesy reductions.
- Fee cap reach (the firm hit an agreed ceiling).

**Target range**: Healthy firms typically achieve 85–95% billed realization; below 80% is a structural problem.

### Collected realization rate

```
Collected Realization = (Amount Collected) / (Hours Worked × Hourly Rate) × 100%
```

Measures what the firm actually received. The gap between billed and collected realization equals **write-offs** (bad debt, discounts granted post-invoice, disputes).

```
Collected Realization = Billed Realization × Collection Rate
```

A firm billing at 90% but collecting at 80% has a collected realization of 72%.

### Write-down vs write-off distinction

| Term | Timing | Cause |
|---|---|---|
| Write-down | Before invoice | Internal decision; hours removed from bill |
| Write-off | After invoice | Client non-payment or post-billing concession |

Both erode realization. Finance reports should break them out separately.

## Required inputs

| Input | Why it matters |
|---|---|
| Time records (hours + rates) | The denominator of all realization calculations |
| Invoices issued | Numerator for billed realization |
| Payments received (by invoice) | Numerator for collected realization |
| Period | All figures must be period-consistent |
| Dimension key (attorney / practice / client / matter type) | Determines granularity of report |

## Optional inputs

- **Target realization rate** (firm-set benchmark, typically per tier): enables deviation flagging.
- **Matter type codes**: required for matter-type-level analysis.
- **Historical data (prior 4 periods)**: enables trend analysis.
- **AFA flag**: matters under fixed fees should be excluded from hourly realization calculations (or tracked separately as AFA efficiency).

## Analysis dimensions

Run the tracker across each of these dimensions independently:

### By attorney

Identifies individual billing behavior. Flags:
- An attorney whose billed realization is consistently 10+ pp below firm average → training opportunity or rate misalignment.
- High write-down attorneys who are also high utilization → the hours are there but clients won't pay → re-staffing needed.

### By practice area

Identifies systematically thin-margin work:
- Litigation often lower realization due to court-imposed fee constraints or contingency caps.
- Transactional work typically higher if scope is well-defined.
- Regulatory matters in MENA often lower due to relationship-based discounting.

### By client

Most actionable dimension. Flags:
- **Chronic write-down clients**: clients who, over multiple matters and years, generate significant write-downs. The decision is to re-price or decline new matters.
- **Volume clients with low realization**: the total revenue may be large but margin is thin; consider whether the relationship is worth the profitability drag.

### By matter type

Identifies whether pricing models are miscalibrated:
- A matter type with systematically below-average realization may need to be re-priced via fixed fee or AFA.
- Useful for annual rate-card review.

## Output format

```
REALIZATION RATE REPORT — [Dimension] — [Period]

Metric                      | Value     | Prior Period | Δ
─────────────────────────────────────────────────────────
Potential revenue (hrs×rate)| $X        | $Y           | +/-Z%
Billed revenue              | $A        | $B           |
Billed realization rate     | R1%       | R2%          | Δ1 pp
Collected revenue           | $C        | $D           |
Collected realization rate  | R3%       | R4%          | Δ2 pp
Write-downs                 | $W1       |              |
Write-offs                  | $W2       |              |

FLAGS
[List of anomalies — see below]

RECOMMENDATIONS
[Actionable items — see below]
```

## Flags

| Flag | Threshold | Action |
|---|---|---|
| Attorney realization below firm avg | >5 pp below average | Training review / rate discussion |
| Client chronic write-down | >3 consecutive periods | Re-price or terminate relationship |
| Matter type thin margin | <75% collected realization | Re-evaluate AFA vs hourly structure |
| Single-period spike in write-downs | >15% jump vs prior period | Investigate cause (scope creep, staffing error) |
| Write-off without write-down | Bill issued, not collected | Collection action or bad-debt provision |

## Jurisdictional notes

- **MENA firms**: Relationship-based discounting is culturally common in Gulf markets. Track write-downs by "courtesy discount" category separately from efficiency write-downs — the former is a business decision, the latter a workflow problem.
- **KSA**: Some government-linked clients pay on lengthy statutory timescales; factor in when assessing collected realization vs. simple non-payment.
- **DIFC / ADGM**: Common law–style billing norms; detailed time narratives expected; write-downs for poor narration are avoidable.
- **Lebanon**: Currency instability makes USD vs. LBP billing critical; track realization in functional currency.
- **US**: GAAP requires revenue recognized at net realizable value; realization tracking is foundational for proper accounting.

## Limits and escalation

- This skill computes and flags — it does not make the re-pricing or termination decision for a client relationship.
- Partners should review client-level flags before any communication with the client.
- Realization data is confidential firm financial information; output access should be role-restricted.

## Related skills

- [[efirm-finance-collection-rate-tracker]]
- [[efirm-finance-wip-aging-report]]
- [[efirm-finance-utilization-dashboard]]
- [[efirm-finance-partner-comp-allocator]]
- [[efirm-matter-creation-flow]]
