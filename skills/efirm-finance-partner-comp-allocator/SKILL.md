---
name: efirm-finance-partner-comp-allocator
description: Use when a law-firm administrator or managing partner needs to model, allocate, or review partner compensation for a period. Covers the full input set (billable hours, origination credit, working credit, supervision credit, firm contributions), all major allocation models (lockstep, eat-what-you-kill, hybrid), and outputs a structured recommendation with sensitivity analysis and benchmarks. Designed for multi-jurisdiction law firms including MENA practices.
license: MIT
metadata: " id: efirm-finance.partner-comp-allocator category: efirm-finance jurisdictions: [__multi__] priority: P2 intent: [comp, partner, compensation, allocation, PEP, origination] related: - efirm-finance-realization-rate-tracker - efirm-finance-utilization-dashboard - efirm-finance-wip-aging-report - efirm-finance-collection-rate-tracker source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'efirm-finance'.
Registered as a flat plugin skill.
-->


# Partner Compensation Allocator

## When to use this

Use this skill whenever:
- A managing partner or compensation committee is preparing annual or periodic partner draws.
- A firm wants to model compensation under a new allocation policy before implementing it.
- A partner disputes their allocated credit and a structured breakdown is needed.
- The firm is benchmarking total compensation against peer PEP (Profits per Equity Partner) figures.
- A newly promoted partner's first-year comp structure needs to be designed.

Do **not** use this as the sole basis for compensation decisions — it is a structured recommendation tool. Final decisions require human judgment and governance review.

## Required inputs

| Input | Why it matters | Default if missing |
|---|---|---|
| Partner name / ID | Links output to the individual | Required; no default |
| Period (e.g., Q1 2025 or FY 2024) | All metrics must share the same denominator | Current fiscal year |
| Billable hours worked (own) | Direct revenue generation baseline | Pull from time records |
| Standard hourly rate | Converts hours to revenue value | Firm rate card |
| Allocated model | Determines weighting formula | Hybrid 50/30/20 |
| Originating client list | Credits the partner who brought in the client | Matter origination register |
| Working matter list | Credits active management of matters | Matter responsibility register |
| Supervising timekeeper hours | Credits oversight of associates | Time records by supervisor |
| Firm contribution activities | Training, BD, recruiting, committees | Self-report + HR records |

## Optional inputs

- **Collected realization rate per partner** — adjusts comp for write-downs attributable to the partner's billing decisions; pairs with [[efirm-finance-realization-rate-tracker]].
- **WIP at period end** — factor pending billing into projected comp for accrual-basis firms.
- **Peer benchmarks** — external PEP data from surveys (Am Law 100, LACCA, LegalWeek) for context.
- **Lockstep seniority tier** — required if model = lockstep or hybrid.
- **Non-equity partner adjustments** — separate pool and formula for income/salaried partners.

## Allocation models

### 1. Lockstep (seniority-equal)

All equity partners at the same seniority tier receive equal draws from the profit pool. No explicit origination or working credit.

- **Best for**: Long-established firms with deep institutional client relationships, or where teamwork culture is paramount.
- **Risk**: Reduces incentives for business development; younger partners may defect.
- **Calculation**: Total profit pool ÷ total lockstep units × partner's units.

### 2. Eat-What-You-Kill (originator-heavy)

Compensation driven almost entirely by origination credit — the partner who brought in the client keeps the lion's share.

- **Best for**: Lateral-heavy, entrepreneurial practices.
- **Risk**: Hoarding behavior; refusal to collaborate; client ownership disputes on departure.
- **Typical weighting**: 70–90% origination credit, 10–30% working credit, minimal firm contribution credit.

### 3. Hybrid (most common — recommended default)

**Default formula**: 50% originating + 30% working + 20% firm-contributions.

Sub-components:

| Credit type | Calculation |
|---|---|
| Originating credit | Revenue collected on matters the partner originated × 50% weighting |
| Working credit | Revenue worked on matters the partner was responsible attorney × 30% weighting |
| Supervision credit | Associate hours billed under partner supervision × blended rate × supervision factor (typically 0.15–0.25) |
| Firm contribution | Scored on 1–5 scale across: training sessions, BD pitches, recruiting hires, committee participation × 20% weighting |

## Output format

The skill should produce a structured report for each partner covering:

```
PARTNER COMPENSATION RECOMMENDATION — [Partner Name] — [Period]

1. INPUT SUMMARY
   Billable hours (own):          [X hrs at $Y/hr = $Z]
   Originating revenue collected: $A
   Working revenue collected:     $B
   Supervision hours:             C hrs
   Firm contribution score:       D/5

2. ALLOCATION (Hybrid 50/30/20)
   Originating credit:  50% × $A = $A1
   Working credit:      30% × $B = $B1
   Firm contribution:   20% × (D/5) × [pool share] = $C1
   Supervision bonus:   C × rate × factor = $D1
   ─────────────────────────────────────
   TOTAL COMP RECOMMENDATION:     $T

3. BENCHMARKS
   Firm average partner comp (period): $X
   PEP (firm-wide):                    $Y
   External benchmark (survey):        $Z range

4. SENSITIVITY ANALYSIS
   If origination weight ↑ to 60%: comp = $T2
   If working weight ↑ to 40%:     comp = $T3
   If firm contribution dropped:    comp = $T4

5. FLAGS
   [Any anomalies: realization below avg, origination credit dispute, etc.]
```

## Jurisdictional notes

| Jurisdiction | Specific considerations |
|---|---|
| US (Am Law) | PEP is the primary external benchmark. Lockstep largely abandoned at most firms post-1990s. Non-equity partner tier is common; distinguish equity vs. income. |
| UK (Magic/Silver Circle) | Modified lockstep still common; "black box" discretionary element at most firms. Salaried partner tier widely used. |
| MENA (GCC) | Partnership structures vary; some Gulf firms operate as sole practitioner or corporate entities under national law — formal equity partnership may not exist. Track profit distributions per ownership %. KSA firms may operate under a licensed professional company structure. |
| UAE onshore | UAE Federal Law on Commercial Companies governs; professional companies have specific requirements. |
| DIFC / ADGM | Partnerships possible under DIFC/ADGM partnership law; distributions governed by partnership agreement. |
| Lebanon | Bar affiliation required; partnership structures informal. |
| France | SCP/SEP/SELARL structures; remuneration governed partly by partnership deed and partly by CNBF (Caisse nationale des barreaux français) contributions. |

## Common mistakes

- **Double-counting origination and working credit** when one partner does both — set firm policy on split.
- **Ignoring realization** — a partner originating large volumes of uncollected debt should not receive full origination credit.
- **Static benchmarks** — PEP data from prior years is not comparable to current performance; use same-year surveys.
- **No supervision credit formula** — without it, senior partners avoid associate delegation, harming leverage ratio.
- **Failure to document** — comp decisions without a written formula invite disputes and bar complaints (in some jurisdictions, partners are entitled to see the formula under partnership law).

## Related skills

- [[efirm-finance-realization-rate-tracker]]
- [[efirm-finance-utilization-dashboard]]
- [[efirm-finance-wip-aging-report]]
- [[efirm-finance-collection-rate-tracker]]
- [[efirm-matter-creation-flow]]
