---
name: prompt-pack-legal-budget-forecast
description: Use when a legal department or law firm needs to build a quarterly or annual legal budget forecast. Produces a template with categories for external counsel fees, litigation costs, compliance, technology, staffing, and contingency, with variance tracking and year-over-year comparison columns. Applicable to in-house legal teams managing budgets across MENA, EU, and global operations.
license: MIT
metadata: " id: prompt-pack.legal-budget-forecast category: prompt-pack practice_area: legal-ops-billing priority: P2 intent: [operations, legal-budget-forecast] related: - prompt-pack-matter-budget-template - prompt-pack-legal-department-kpi-dashboard - prompt-pack-legal-department-annual-report - prompt-pack-outside-counsel-guidelines - prompt-pack-legal-invoice-review-checklist source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'prompt-pack'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Legal Budget Forecast

## When to use this

Use this skill when a General Counsel, Chief Legal Officer, or legal operations manager needs to build or update a budget forecast for the legal function. The output is a structured template that can be populated in Excel, Google Sheets, or a matter management system.

Triggers:
- Annual planning cycle: "Build a legal budget for next fiscal year."
- Quarterly reforecast: "Update the Q3 legal forecast with actuals from Q1–Q2."
- Board/CFO reporting: "Summarize the legal department's expected spend for the year."
- New department setup: "We're building an in-house legal team from scratch — what should we budget for?"

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| Department or firm name | Personalizes the template | "Legal Department" |
| Fiscal year / period covered | Scopes the forecast (quarterly breakdown required for variance tracking) | Current year |
| Forecast period | Quarterly or monthly breakdown | Quarterly |
| Prior-year actuals (if available) | Enables year-over-year comparison | Marked as "N/A – first year" |
| Headcount | Drives staffing cost category | Ask user |
| Known major matters / litigation | Enables realistic litigation reserve | Ask user |

## Optional inputs

- Currency (USD, EUR, AED, SAR, LBP, EGP) — important for MENA multi-currency departments
- E-billing system in use (e.g., eBillingHub, Mitratech, Legal Tracker) — affects line-item granularity
- Whether to include a contingency / reserve line
- Approval workflow (who approves budget reforecasts)

## Budget template structure

### Section 1: External Counsel Fees
| Sub-category | Q1 Budget | Q1 Actual | Q1 Variance | Q2–Q4 (repeat) | FY Total | Prior-Year Actual | YoY % Change |
|---|---|---|---|---|---|---|---|
| Transactions (M&A, JV, commercial) | | | | | | | |
| Litigation and arbitration | | | | | | | |
| Regulatory / compliance | | | | | | | |
| Employment | | | | | | | |
| IP / patents / trade marks | | | | | | | |
| Real estate | | | | | | | |
| Other (specify) | | | | | | | |

### Section 2: Litigation Reserves and Contingencies
| Matter | Estimated exposure | Probability | Expected value | Status |
|---|---|---|---|---|
| [Matter 1] | | | | |
| Unallocated reserve | | | | |

### Section 3: Compliance Expenditure
- Regulatory filings and license fees
- Compliance training programs
- Regulatory change management (outside counsel or consultant fees)
- Audit / inspection support

### Section 4: Legal Technology and Tools
- Matter management system (annual licence)
- Contract lifecycle management (CLM)
- E-billing platform
- Legal research subscriptions (Lexis, Westlaw, regional databases)
- Document management / e-discovery tools
- AI legal tools

### Section 5: Staffing (Internal Legal Team)
| Role | Headcount | Salary + benefits | Q1–Q4 allocation |
|---|---|---|---|
| General Counsel | | | |
| Senior Counsel | | | |
| Counsel | | | |
| Paralegal / Legal Ops | | | |
| Legal Secretary / Support | | | |

### Section 6: Other Operating Costs
- Training and professional development (CLE, bar memberships)
- Travel and entertainment (client/court appearances)
- Office / facilities allocation
- Insurance (professional indemnity, D&O contribution)

### Section 7: Contingency Reserve
- Recommended: 5–15% of total external counsel budget to cover unanticipated matters
- Document assumptions and release process

### Section 8: Summary Dashboard
| Category | FY Budget | FY Forecast | FY Actual (as incurred) | Variance | Variance % |
|---|---|---|---|---|---|
| External Counsel | | | | | |
| Litigation Reserve | | | | | |
| Compliance | | | | | |
| Technology | | | | | |
| Staffing | | | | | |
| Other | | | | | |
| Contingency | | | | | |
| **Total** | | | | | |

## Operational guidance

**Variance tracking**: Flag any line item where actual exceeds budget by more than 10% or USD 50,000 (adjust threshold by department size) — these require a brief written explanation to the CFO.

**Matter-level forecasting**: For significant litigation or transactions, link each matter to a matter budget (see [[prompt-pack-matter-budget-template]]) so that the aggregate external counsel line item is built up from per-matter estimates.

**Quarterly reforecasting**: At the end of each quarter, update the forecast with actuals and revise forward-looking periods based on changed assumptions. Document changes to assumptions.

**MENA-specific considerations**:
- Multi-currency departments (e.g., LBP-denominated costs vs USD-billed external counsel) require currency translation and FX risk disclosure.
- KSA and UAE government-linked entities may require budget approval at board level before incurring external counsel fees above defined thresholds.
- Lebanon-based entities should build in an escalation buffer given economic volatility.

## Common mistakes

- **Not separating litigation reserves from recurring external counsel budgets**: Contingent liabilities inflate the recurring forecast and make year-over-year comparison meaningless.
- **Ignoring technology costs**: Legal tech spend has grown substantially; failing to budget for CLM/AI tools leads to mid-year overruns.
- **Under-budgeting compliance in regulated sectors**: FinTech, banking, healthcare, and energy companies face increasing regulatory filing burdens; compliance spend should be estimated per known regulatory calendar.
- **No approval workflow**: Budgets without sign-off from CFO or board create governance issues — include the approval chain in the template.

## Related skills

- [[prompt-pack-matter-budget-template]]
- [[prompt-pack-legal-department-kpi-dashboard]]
- [[prompt-pack-legal-department-annual-report]]
- [[prompt-pack-outside-counsel-guidelines]]
- [[prompt-pack-legal-invoice-review-checklist]]
