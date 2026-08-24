---
name: docs-roi-calculator
description: Use when a prospective customer or sales team member asks about the financial return of deploying a legal AI assistant, or when handling a cost-based sales objection. Generates a quantified monthly savings estimate and payback period from three simple inputs — contracts reviewed per week, average review time, and billable hourly rate — mapped against Louis's time-saving benchmark. Applicable across all jurisdictions and firm sizes.
license: MIT
metadata: " id: docs.ROI-calculator category: docs jurisdictions: [__multi__] priority: P2 intent: [roi, cost savings, sales objection, payback period, pricing justification] related: [docs-whitepaper-general, docs-security-overview, docs-terms-of-service-summary] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'docs'.
Namespaced as louis-<category>-<skill> on registration.
-->


# ROI Calculator — Legal AI Time & Cost Savings

## Purpose

This skill computes a concrete return-on-investment estimate for a law firm, legal department, or solo practitioner evaluating Louis. It is designed for sales conversations, procurement evaluations, and budget-justification memos — transforming abstract "AI saves time" claims into verifiable, prospect-specific numbers.

## Inputs

| Input | Description | Typical Range | Default if not provided |
|---|---|---|---|
| `contracts_per_week` | Number of contracts or documents reviewed weekly by the target user or team | 2 – 200 | Ask the user |
| `avg_review_hours` | Average time (in hours) to review one contract manually, from open to close | 0.5 – 8 hrs | 2.0 hrs |
| `billable_rate` | Hourly billable rate (or effective cost rate for in-house teams) in USD or local currency | $50 – $800/hr | $300/hr |
| `time_saving_pct` | Louis's estimated time reduction per review. Default benchmark: 40%. Can be adjusted up (80% for routine contracts) or down (20% for bespoke M&A work). | 20% – 80% | 40% |
| `subscription_cost` | Monthly cost of Louis subscription for the user's tier | Varies by plan | Ask or use published pricing |

## Calculation logic

```
hours_saved_per_week  = contracts_per_week × avg_review_hours × time_saving_pct
hours_saved_per_month = hours_saved_per_week × 4.33
monthly_value_saved   = hours_saved_per_month × billable_rate
payback_months        = subscription_cost ÷ monthly_value_saved   (if < 1, express as days)
annual_roi_pct        = ((monthly_value_saved × 12) - (subscription_cost × 12))
                        ÷ (subscription_cost × 12) × 100
```

## Output format

Present results in a clean summary block:

```
─────────────────────────────────────
  Louis ROI Estimate — [Firm/User Name]
─────────────────────────────────────
  Weekly contracts reviewed:      [X]
  Avg. review time:               [X hrs]
  Billable / cost rate:           [$ / hr]
  Time saved per review (40%):    [X hrs]

  Hours saved / month:            [X hrs]
  Monthly value of time saved:    $[X]
  Monthly subscription cost:      $[X]
  Net monthly benefit:            $[X]

  Payback period:                 [X weeks / days]
  12-month ROI:                   [X %]
─────────────────────────────────────
```

Follow the table with a one-paragraph narrative for copy-paste into a business case email.

## Worked example

Inputs: 20 contracts/week · 2 hrs avg · $350/hr · 40% saving · $500/mo subscription.

- Hours saved/month: 20 × 2 × 0.40 × 4.33 = **69.3 hrs**
- Monthly value: 69.3 × $350 = **$24,255**
- Net benefit: $24,255 − $500 = **$23,755/mo**
- Payback: 0.6 days
- 12-month ROI: **4,651%**

## Sensitivities to mention

- **High-volume, routine contracts** (NDAs, employment offers, standard service agreements): time-saving is often 60–80%. The default 40% is conservative.
- **Complex bespoke deals** (M&A, project finance, ISDA): saving is 20–30% and value comes from completeness and consistency, not raw speed.
- **In-house teams** (GC/legal ops): use fully-loaded cost per hour (salary + benefits + overhead ÷ 2,080) rather than billable rate.
- **Currency**: quote in the prospect's local currency (AED, SAR, LBP, EGP, EUR, GBP) for MENA markets.

## Caveats

- These are illustrative estimates, not guarantees. Actual savings depend on task mix, user adoption, document complexity, and integration depth.
- Time savings do not automatically translate to billable revenue for law firms unless the freed capacity is re-billed; frame as "capacity freed for higher-value work" in firm contexts.
- For in-house teams, anchor to headcount avoidance or contract cycle-time reduction as a secondary metric.

## Related skills

- [[docs-whitepaper-general]]
- [[docs-security-overview]]
- [[docs-terms-of-service-summary]]
- [[docs-word-plugin-setup]]
