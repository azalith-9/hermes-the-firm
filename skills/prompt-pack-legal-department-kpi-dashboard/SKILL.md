---
name: prompt-pack-legal-department-kpi-dashboard
description: Use when designing a KPI dashboard framework for a legal department. Produces a structured set of metrics covering matter volume, cycle times, spend vs budget, outside counsel utilization, contract turnaround, and client satisfaction. Applicable to in-house legal teams seeking to quantify performance and demonstrate value to leadership.
license: MIT
metadata: " id: prompt-pack.legal-department-kpi-dashboard category: prompt-pack practice_area: legal-ops-billing priority: P2 intent: [operations, legal-department-kpi-dashboard] related: - prompt-pack-legal-department-annual-report - prompt-pack-legal-budget-forecast - prompt-pack-matter-budget-template - prompt-pack-outside-counsel-guidelines - prompt-pack-legal-invoice-review-checklist source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'prompt-pack'.
Registered as a flat plugin skill.
-->


# Legal Department KPI Dashboard

## When to use this

Use this skill to design or populate a performance dashboard for a legal department. The output is a defined KPI framework — each metric with its definition, data source, target, frequency, and owner — that can feed into a PowerBI, Tableau, Excel, or matter management dashboard.

Triggers:
- "Design a KPI dashboard for our legal department."
- "What metrics should a General Counsel report to the board monthly?"
- "We need to show how legal is performing — what should we track?"

## Required inputs

| Input | Why it matters |
|---|---|
| Company / department name | Personalizes the framework |
| Reporting frequency desired | Monthly, quarterly, annual — determines which metrics are practical |
| Scope of legal function | Litigation-heavy vs contracts-heavy vs regulatory-heavy changes metric priorities |
| Available data sources | Determines which metrics can actually be measured (matter management system, e-billing, contract system) |

## Optional inputs

- Current benchmarks (industry peers or prior-year actuals) to set targets
- Whether outside counsel diversity is tracked
- Whether a client satisfaction survey is already in use
- IT/systems constraints (manual vs automated data collection)

## KPI framework

### Tier 1: Financial Metrics (report monthly)

| KPI | Definition | Data source | Target | Owner |
|---|---|---|---|---|
| Total legal spend | Sum of external + internal legal costs | Finance / e-billing | Within X% of budget | GC / Legal Ops |
| External counsel spend | Fees paid to law firms, per matter type | E-billing system | ≤ annual budget line | Legal Ops |
| Spend vs budget variance | Actual vs approved budget, current period and YTD | Finance | < 5% unfavorable variance | GC |
| Cost per matter | Total external spend ÷ matters closed | E-billing + MLMS | Benchmark vs prior year | Legal Ops |
| Blended hourly rate | Weighted average rate across all outside counsel | E-billing | At or below guideline rates | Legal Ops |

### Tier 2: Matter and Workload Metrics (report monthly)

| KPI | Definition | Target |
|---|---|---|
| Matter intake volume | New matters opened in period, by type | Trend-stable or explained growth |
| Matter backlog | Open matters at period end, by status | Below defined threshold |
| Matter cycle time | Average days from matter open to close, by type | Improving quarter-over-quarter |
| Litigation matters: active vs resolved | Count of active litigation and arbitration | Management visibility |
| Contract matters: open vs closed | Contracts in queue vs completed | Backlog ≤ [X] days |

### Tier 3: Contract Performance Metrics (report monthly)

| KPI | Definition | Target |
|---|---|---|
| Contract turnaround time (simple) | Average days to complete a low-risk standard contract | ≤ 5 business days |
| Contract turnaround time (complex) | Average days to complete a negotiated contract | ≤ 20 business days |
| Contracts awaiting business input | Contracts paused due to business-side delay | Track separately (not legal delay) |
| Playbook adherence rate | % of contracts closed using approved standard forms / playbooks | ≥ 80% |
| Contract renewal on time | % of contracts renewed before expiry date | ≥ 90% |

### Tier 4: Outside Counsel Performance (report quarterly)

| KPI | Definition | Target |
|---|---|---|
| Outside counsel utilization | Matters using outside counsel vs handled internally | Track; assess make-vs-buy economics |
| Budget compliance by firm | % of matters where outside counsel stayed within agreed budget | ≥ 85% per firm |
| Invoice compliance | % of outside counsel invoices passing first-pass review without deductions | ≥ 90% |
| Outside counsel diversity spend | % of fees paid to diverse-owned or diverse-staffed firms | Per guidelines target |
| Alternative fee arrangement (AFA) usage | % of matters on fixed fee, capped fee, or other AFA | Trend upward |

### Tier 5: Client Satisfaction (report semi-annually or annually)

| KPI | Definition | Target |
|---|---|---|
| Internal client satisfaction score | Survey result from business unit clients (scale 1–5 or NPS) | ≥ 4.0 / NPS ≥ 30 |
| Responsiveness rating | Specific survey question: "Legal responds in a timely manner" | ≥ 4.2 |
| Business understanding rating | "Legal understands our business objectives" | ≥ 4.0 |

### Tier 6: Risk and Compliance Metrics (report quarterly)

| KPI | Definition | Target |
|---|---|---|
| Regulatory action count | Number of regulatory inquiries, investigations, sanctions in period | Zero sanctionable events |
| Litigation exposure | Aggregate estimated financial exposure across active disputes | Reviewed quarterly by GC |
| Compliance training completion | % of required employees completing assigned compliance training | ≥ 95% |
| Policy updates delivered on time | % of mandatory policy reviews completed per schedule | 100% |

## Dashboard implementation guidance

- **Start with Tier 1 and Tier 2**: financial and workload metrics are the easiest to collect from e-billing and matter management systems and provide immediate value.
- **Add Tier 3 last**: contract cycle time requires tagging in a CLM or contract management system; manual tracking is time-intensive.
- **Set baselines before setting targets**: run the dashboard for one quarter to establish current-state baselines before imposing improvement targets.
- **Use RAG status**: color-code each KPI Red (>10% off target), Amber (5–10% off), Green (within 5%) for executive readability.
- **Automate where possible**: e-billing platforms (Legal Tracker, Mitratech, eBillingHub) export spend data; matter management systems (TeamConnect, Salesforce Legal, ServiceNow) export matter volume data.

## MENA considerations

- GCC in-house legal teams often cover multiple jurisdictions; segment KPIs by country to avoid burying regional performance issues in aggregate numbers.
- Currency-denomination of spend KPIs: use USD as the dashboard base currency for multi-currency teams (AED, SAR, LBP, EGP) with a FX note.
- Contract cycle time benchmarks in MENA markets may be longer than Western markets due to Arabic translation requirements, notarization, and multi-stakeholder approval chains — factor this into targets.

## Common mistakes

- **Too many KPIs**: a dashboard with 40 metrics will not be read. Limit to 12–15 metrics for regular reporting; rotate deeper metrics annually.
- **Measuring activity not outcomes**: "number of contracts reviewed" is activity; "contract turnaround time" and "client satisfaction" are outcomes. Prioritize outcomes.
- **No owner assigned to each KPI**: without a named owner, data collection will not happen.
- **Ignoring data quality**: garbage-in garbage-out. Before publishing a dashboard, verify that underlying data (matter codes, billing codes) are applied consistently.

## Related skills

- [[prompt-pack-legal-department-annual-report]]
- [[prompt-pack-legal-budget-forecast]]
- [[prompt-pack-matter-budget-template]]
- [[prompt-pack-outside-counsel-guidelines]]
- [[prompt-pack-legal-invoice-review-checklist]]
