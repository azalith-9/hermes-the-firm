---
name: efirm-finance-utilization-dashboard
description: Use when a law firm administrator or practice group leader needs to monitor timekeeper utilization — the ratio of billable hours logged to target hours — across attorneys, practice groups, and time periods. Produces a real-time dashboard with utilization rates, benchmark comparisons, trend lines, and actionable staffing recommendations including burnout risk and under-utilization flags. Benchmarks span US BigLaw, UK City, and MENA practice norms.
license: MIT
metadata: " id: efirm-finance.utilization-dashboard category: efirm-finance jurisdictions: [__multi__] priority: P1 intent: [utilization, efirm, staffing, capacity, billable-hours, burnout] related: - efirm-finance-realization-rate-tracker - efirm-finance-partner-comp-allocator - efirm-finance-wip-aging-report - efirm-deadline-tracker source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'efirm-finance'.
Registered as a flat plugin skill.
-->


# Utilization Dashboard

## When to use this

Use this skill to:
- Monitor whether timekeepers are hitting billable hour targets (weekly, monthly, YTD).
- Identify free capacity for matter staffing — who can absorb new work without burnout risk.
- Spot over-utilization trends early, before associate attrition becomes a problem.
- Prepare data for hiring decisions: sustained over-utilization in a practice group signals a headcount gap.
- Link utilization data to compensation decisions (partners' working credit in [[efirm-finance-partner-comp-allocator]]).
- Track non-billable time allocation (training, BD, pro bono) to ensure firm commitments are met.

## Core metrics

### Utilization rate

```
Utilization Rate = Billable Hours Logged / Target Billable Hours × 100%
```

**Target** is typically set annually by the firm and may vary by level (partner vs. associate vs. paralegal).

### Effective utilization rate

```
Effective Utilization = (Billable Hours × Realization Rate) / Target Hours × 100%
```

Adjusts for write-downs — hours worked but not ultimately billed reduce effective utilization. This is the metric that truly links to revenue.

### Leverage ratio

```
Leverage = Associate Billable Hours / Partner Billable Hours (per matter or practice)
```

A healthy leverage ratio (typically 3:1 to 6:1 in transactional practices) indicates partners are supervising rather than doing associate-level work. Low leverage = partners are billing out at their rate for work that could be done at lower cost.

## Hour-type taxonomy

| Category | Description | Counted in utilization? |
|---|---|---|
| Billable | Client-chargeable hours | Yes |
| Non-billable (training) | CLE, mentoring, skills training | No (tracked separately) |
| Non-billable (BD) | Pitches, proposals, client entertainment | No (tracked separately) |
| Non-billable (admin) | Firm management, committee work | No |
| Pro bono | Charged at $0 to client; may count toward targets | Depends on firm policy |
| Personal / absence | Vacation, sick, personal | No |

Many firms have separate targets for non-billable pro bono and BD hours. Track these dimensions to give a full picture of total time allocation.

## Industry benchmarks

| Tier / Geography | Target billable hours / year | Notes |
|---|---|---|
| US BigLaw — Partner | 1,800–2,000 | Origination time not always counted |
| US BigLaw — Associate (mid-level) | 1,900–2,200 | Bonus thresholds typically at 1,950 |
| US BigLaw — Associate (first year) | 1,800–2,000 | Ramp-up first 6 months |
| UK City — All levels | 1,500–1,800 | Lower than US; 37.5-hr week baseline |
| MENA regional firms | 1,500–1,900 | Varies significantly; Dubai international firms closer to UK norms |
| MENA boutique / local | 1,200–1,600 | Lighter billing culture in some markets |
| In-house counsel | N/A | Utilization tracking not applicable |

**Notes on MENA**: In MENA regional practices, Ramadan productivity drop is real and should be factored into monthly targets. Some firms adjust monthly targets down ~30% during Ramadan month, with compensating targets in other months.

## Dashboard layout

The skill should generate output organized in three views:

### View 1: Firm-wide snapshot (current month + YTD)

```
UTILIZATION DASHBOARD — [Firm] — [Period]

                    | MTD Hrs | MTD Target | MTD Util% | YTD Hrs | YTD Target | YTD Util%
─────────────────────────────────────────────────────────────────────────────────────────
FIRM TOTAL          |         |            |           |         |            |
  Partners          |         |            |           |         |            |
  Associates (Sr)   |         |            |           |         |            |
  Associates (Jr)   |         |            |           |         |            |
  Paralegals        |         |            |           |         |            |
```

### View 2: Individual drill-down

```
[Timekeeper Name] — [Level] — [Practice Group]

  Billable hours this month:     X / Target Y  (Z%)
  Non-billable (training):       A hrs
  Non-billable (BD):             B hrs
  Non-billable (admin):          C hrs
  
  YTD pace vs. target:           [On track / Behind / Ahead]
  
  FLAGS: [see below]
```

### View 3: Trend chart (narrative)

12-month rolling utilization per attorney + practice group, with trend direction noted.

## Flags and recommendations

| Flag | Trigger | Recommended action |
|---|---|---|
| Under-utilization | Utilization <70% for 2+ consecutive months | Check matter pipeline; reassign to available matters; investigate client loss |
| Over-utilization (burnout risk) | Utilization >115% for 2+ consecutive months | Alert practice group leader; prioritize staffing additions; review matter allocation |
| Declining trend | 3-month trend down >10 pp | Investigate: client loss, reduced matter complexity, health issue |
| Rising trend | 3-month trend up >10 pp | Plan hiring; monitor for unsustainable pace |
| Non-billable time spike | Admin/BD >20% of total time | Check for internal projects; ensure client-facing capacity is not being crowded out |
| Leverage imbalance | Partner utilization >90% of associate target | Partners doing associate work; review staffing model |

## Staffing recommendations output

When over/under-utilization is detected, the dashboard should generate a concise recommendation:

```
STAFFING NOTE — [Practice Group] — [Date]

Situation: [Associates in Corporate are running at 130% utilization for Q3 2025]
Implication: [Retention risk; quality risk on matters; client service degradation]
Recommendation: [Hire 1 mid-level corporate associate; interim: engage 2 contract attorneys
                 for Project X; defer non-urgent BD activities for overloaded timekeepers]
Hiring lead time: [~4–6 months for lateral hire; 2–4 weeks for contract resource]
```

## Integration points

- Feeds into [[efirm-finance-partner-comp-allocator]] (working credit calculation).
- Informs [[efirm-finance-wip-aging-report]] (high utilization + high WIP = billing backlog risk).
- Connects to [[efirm-deadline-tracker]] (over-utilized attorneys on deadline-critical matters need escalation).

## Related skills

- [[efirm-finance-realization-rate-tracker]]
- [[efirm-finance-partner-comp-allocator]]
- [[efirm-finance-wip-aging-report]]
- [[efirm-deadline-tracker]]
- [[efirm-matter-creation-flow]]
