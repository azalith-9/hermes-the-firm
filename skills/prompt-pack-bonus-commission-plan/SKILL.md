---
name: prompt-pack-bonus-commission-plan
description: Use when drafting a bonus or commission plan for sales, executive, or employee roles covering eligibility, performance metrics, calculation methodology, payment timing, pro-ration, clawback, and discretionary elements. Employment practice area with MENA-specific attention to WPS (Wage Protection System) requirements, gratuity interaction, and Sharia-compliant commission structures in KSA and UAE.
license: MIT
metadata: " id: prompt-pack.bonus-commission-plan category: prompt-pack practice_area: employment priority: P2 intent: [drafting, bonus-commission-plan] related: [prompt-pack-board-resolution, heuristic-always-state-jurisdiction-first, kb-employment-law-mena, prompt-pack-agreement-legal-draft-review, persona-sme-founder] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'prompt-pack'.
Registered as a flat plugin skill.
-->


# Bonus / Commission Plan

## When to use this

Use this skill when drafting:
- A **sales commission plan** for sales representatives, account executives, or distribution staff — specifying how commission accrues on sales performance
- An **annual bonus plan** for executives or employees — specifying the performance targets, calculation, and payment conditions
- A **combined plan** for roles with both a base-plus-commission and a performance-bonus component

These documents can be:
- A standalone plan document (attached to or referenced in the employment contract)
- A section within the employment contract
- A company-wide policy applicable to a defined group of employees

Triggers: new hire package design; annual plan cycle; IPO/equity compensation planning; existing plan review or compliance audit.

---

## Prompt template

> Draft a bonus/commission plan for [sales/executive/employee] roles at [Company]. Include eligibility, performance metrics, calculation methodology, payment timing, pro-ration rules, clawback provisions, and discretionary elements.

Use [[conversation-clarifying-questions]] to elicit `[bracketed]` inputs before drafting.

---

## Required inputs

| Input | Why it matters |
|-------|---------------|
| Company name and jurisdiction | Employment law determines whether bonus/commission is a contractual entitlement or discretionary |
| Role type (sales/executive/employee) | Commission plans differ structurally from bonus plans |
| Performance period | Annual; quarterly; monthly — affects pro-ration and payment timing |
| Target on-target earnings (OTE) | The economic target for the plan |
| Performance metrics | Revenue, margin, units, KPIs — the basis for calculation |
| Discretionary vs. non-discretionary | Critical legal distinction — see below |

---

## Document structure

### 1. Eligibility

Define who is covered:
- Job grades, roles, or individuals by name (for executive plans)
- Commencement of employment: "Employees who join before [date in the plan year] are eligible on a pro-rated basis; employees joining after [date] are not eligible for the current plan year"
- Employment status at payment date: typically, eligibility requires active employment at the payment date; employees who resign before the payment date forfeit the bonus (address this explicitly — see jurisdictional notes)

**MENA trap**: in UAE and KSA, a bonus that has been paid consistently for several years may be treated by labour authorities and courts as a contractual entitlement (part of the basic wage), not a discretionary reward. To preserve discretion:
- State clearly in the plan (and in the employment contract) that the bonus is **discretionary** and does not form part of basic salary
- Add a non-reliance statement: "The payment of a bonus in one period does not create any entitlement to a bonus in any subsequent period"
- Vary the bonus design or amount periodically to prevent crystallization as a custom

### 2. Performance metrics

#### 2.1 Commission plans (sales roles)
Define the commission structure clearly:

**Simple commission**:
- Commission rate: [X%] of net revenue
- "Net revenue" definition: gross sales price minus returns, discounts, taxes, and excluded items (list excluded items — e.g., pass-through expenses, government fees)
- When commission is "earned": on invoice date, on payment by customer, on product delivery — specify; "on payment" is most defensible for businesses with long payment cycles

**Tiered commission**:
| Revenue target | Commission rate |
|---------------|----------------|
| 0 – 100% of quota | [X%] of revenue |
| 101 – 120% of quota | [Y%] of revenue above 100% |
| 121%+ of quota | [Z%] of revenue above 120% |

**Quota definition**: set the individual's quarterly/annual quota and the process for adjusting it (quota relief for territory changes, product changes).

#### 2.2 Bonus plans (executive/employee roles)
Define the performance framework:

**Company-level metrics** (examples):
- Revenue vs. budget: [50% weight]
- EBITDA vs. budget: [30% weight]
- Strategic KPIs (e.g., customer NPS, project completion): [20% weight]

**Individual-level metrics** (examples):
- Individual performance rating (1–5 scale): [50% weight]
- Specific objectives (SMART objectives set at start of year): [50% weight]

**Target bonus**: [X%] of base salary at 100% performance; [Y%] at threshold (minimum payout); [Z%] at stretch (maximum payout). State the threshold below which no bonus is payable.

**Worked example** (include in the plan):
> If target bonus is 20% of base salary (USD 100,000 = USD 20,000 target):
> - 80% achievement → 50% of target bonus = USD 10,000
> - 100% achievement → 100% of target → USD 20,000
> - 120% achievement → 150% of target → USD 30,000 (capped at 150%)

### 3. Calculation methodology

State the formula with no ambiguity:

For commission:
```
Commission = (Actual Sales Revenue × Commission Rate) – Previous Period Commission Paid
```

For bonus:
```
Bonus = Base Salary × Target Bonus % × Performance Multiplier

Where Performance Multiplier = weighted average of company and individual metrics,
as calculated per the schedule
```

Define rounding (to the nearest currency unit; to 2 decimal places for percentages).

Define currency: is the bonus denominated in USD and paid in local currency? At what exchange rate?

### 4. Payment timing

- **Commission**: typically monthly or quarterly; state the payment date (e.g., 15th of the month following the calculation period)
- **Bonus**: typically annually; state the payment date (e.g., by March 31 for the preceding calendar year)
- **Accrual**: state whether bonus/commission accrues during a performance period even if not yet paid

**MENA payroll compliance — UAE WPS (Wage Protection System)**:
- All UAE mainland and most free zone employers must pay salaries via the WPS
- If a bonus forms part of "wage" (basic salary) under UAE Labour Law, it must be paid through WPS
- Discretionary bonuses paid above basic salary: can be paid outside WPS cycle but must be reported
- **Wage Protection Law reminder**: UAE Decree-Law 33/2021 includes "commissions" in the definition of "wage" if they are contractually agreed and recurring; this has implications for gratuity calculation (see below)

### 5. Pro-ration rules

- **New joiners**: pro-rated based on the number of months employed during the plan period; define the start date (first full month vs. actual start date)
- **Leavers during the plan period**: address three scenarios:
  1. Resignation before payment date: typically forfeited; but see jurisdictional notes
  2. Termination without cause before payment date: consider pro-rated entitlement
  3. Termination for cause: forfeited
- **Parental leave and sick leave**: define whether time on leave is included or excluded from pro-ration calculations (employment law may impose a minimum)

**UAE employment law note**: an employee who resigns and has accrued commission on sales made (where commission was earned on the transaction date, not the payment date) may have a legal claim for accrued commission. Define "earned" commission carefully.

### 6. Clawback provisions

A clawback allows the company to recover previously paid bonus/commission if:
- The financial results on which the bonus was based are restated downward
- The recipient is found to have engaged in misconduct contributing to the overstatement
- For sales commission: the customer cancels or returns the goods/services after commission was paid

**Format**:
```
Clawback trigger: [financial restatement within 3 years; misconduct finding; customer cancellation within 90 days]
Clawback amount: [pro-rated reduction in bonus / full repayment / net-of-tax amount]
Recovery mechanism: deduction from future payroll; demand for repayment
Time limit for exercise: [2 years] from original payment
```

**MENA employment law note**: wage deductions in UAE are subject to Article 25 of Decree-Law 33/2021 — deductions are limited to specified purposes and amounts. A clawback that results in deduction from wages must comply with these limits. For material clawback amounts, the employer may need to bring a civil claim rather than deducting unilaterally.

**KSA**: Saudi Labour Law does not readily permit wage deductions; clawback is better implemented as a contractual repayment obligation with a civil remedy than a payroll deduction.

### 7. Gratuity interaction (MENA)

This is a critical MENA-specific issue:

**UAE**: end-of-service gratuity under Decree-Law 33/2021 is calculated on "basic salary" only. Commission and discretionary bonuses are generally excluded from the gratuity calculation base. However, if commission is **contractually promised and recurring**, UAE courts and the Ministry of Human Resources have sometimes included it in the gratuity base.

**Drafting mitigation**: state clearly in the plan and employment contract that commission/bonus is not part of "basic salary" for the purpose of gratuity or end-of-service benefit calculations.

**KSA**: same principle applies under Saudi Labour Law. Severance (end-of-service award) is calculated on the last basic wage; recurring contractual bonuses included in "basic wage" by Saudi courts in some cases.

**Lebanon**: NSSF contributions are based on total remuneration including bonuses; this affects the employer's cost calculation.

### 8. Discretionary elements

State which elements are discretionary (subject to board or management approval) and which are formula-driven:
- "The bonus amount calculated under section [X] is subject to final determination by the Board/Remuneration Committee, which may apply a positive or negative adjustment of up to [X%] based on qualitative factors"
- "The Company reserves the right to modify, suspend, or terminate this plan at any time on [30/60/90] days' notice, without this constituting a breach of any employment obligation"

The notice period for modifying or terminating the plan is important — in UAE and KSA, altering a contractual commission structure unilaterally without notice can trigger a constructive dismissal claim.

### 9. Taxes

- The plan should state that bonus/commission payments are subject to applicable income tax (relevant for EG where income tax applies; LB where income tax applies; and globally for expatriate employees with home-country tax obligations)
- The company is responsible for withholding applicable taxes
- UAE, KSA: no personal income tax on employment income for local nationals and most residents

---

## Jurisdictional notes

### UAE
- WPS compliance: bonuses paid as part of regular payroll must flow through WPS
- Gratuity: Decree-Law 33/2021 — gratuity is 21 days per year of service for the first 5 years; 30 days per year thereafter; based on basic salary only unless commission is recurring/contractual
- Labour Court: if a commission plan is ambiguous, UAE courts tend to interpret in favour of the employee

### KSA
- Saudi Labour Law does not permit pure discretionary bonuses in practice if they have been paid consistently — document the legal basis (performance, not custom)
- Commission plans: state clearly in the employment contract and plan that commission is performance-linked and non-recurring as a right

### Lebanon
- NSSF contributions on all remuneration (including bonuses) at employer rate
- Income tax (impôt sur le revenu) withheld from all employment income

### Egypt
- Income tax applies at progressive rates on employment income including bonuses
- Social insurance contributions on regular bonuses included in the contribution base

---

## Common mistakes

- No definition of when commission is "earned" vs. "paid" — creates disputes on termination
- Clawback mechanism incompatible with local wage-deduction rules
- Plan treated as contractual without the discretionary savings clause
- Gratuity impact not addressed — employer discovers at end-of-service that regular commissions inflate the gratuity base
- No quota/target definition — a commission plan without a defined quota is unworkable

---

## Related skills

- [[kb-employment-law-mena]] — UAE, KSA, LB, EG employment law reference
- [[heuristic-always-state-jurisdiction-first]] — employment law is strictly jurisdiction-specific
- [[persona-sme-founder]] — SME context for designing employee compensation packages
- [[prompt-pack-agreement-legal-draft-review]] — reviewing an employment agreement or existing bonus plan
