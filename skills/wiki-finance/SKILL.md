---
name: wiki-finance
description: Use when discussing law firm financial management, legal-practice economics, or the billing and revenue metrics of a legal-AI product. Covers work in progress (WIP), accounts receivable aging, realization rates, utilization, partner compensation structures, and how these metrics translate into the efirm finance skill suite. Reach for this skill when the user asks about law firm finances, billing efficiency, partner economics, or practice management metrics.
license: MIT
metadata: " id: wiki.finance category: wiki jurisdictions: [__multi__] priority: P3 intent: [__wiki__, law-firm-finance, WIP, realization, billing-metrics] related: [wiki-legal, wiki-product, wiki-haqq-product, wiki-pricing] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'wiki'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Law Firm Financial Management

## Scope

This pack covers the financial mechanics of a law firm as a business: how time and money flow from matter inception through to partner distributions, and the key metrics that signal whether a practice is healthy or troubled. It also covers how these concepts map to features and metrics in a legal-AI product (the efirm finance skill suite), and the MENA-specific variations that affect law firm economics in the region.

---

## Core financial concepts

### Work in Progress (WIP)

WIP is the value of billable time and disbursements that have been recorded but not yet billed to the client. It is the firm's most liquid asset after cash.

Key WIP risks:
- **WIP aging** — the older the WIP, the lower the probability of collection. Firms should bill regularly (monthly in most practices) rather than accumulating WIP.
- **Write-downs at billing** — when the partner decides to bill less than the recorded WIP (e.g. the matter took longer than expected but the client won't pay for the excess), the write-down reduces realization.
- **WIP lock-up** — the number of days of average revenue tied up in WIP; a key efficiency metric.

### Accounts Receivable (AR) Aging

AR aging tracks unpaid invoices by how long they have been outstanding:

| Bucket | Signal |
|---|---|
| 0–30 days | Normal |
| 31–60 days | Monitor; follow up |
| 61–90 days | At risk; escalate collection |
| 90+ days | Likely write-off; provision required |

In MENA markets, payment terms are longer than in the US/UK. Government clients in KSA and UAE regularly pay in 60–90+ days. Managing partners must adjust their AR aging benchmarks accordingly and not mistake slow-pay government work for bad debt.

### Realization Rate

Realization measures how much of the time recorded actually translates into cash collected:

```
Billing Realization = Billed / Recorded WIP
Collection Realization = Collected / Billed
Overall Realization = Collected / Recorded WIP
```

Healthy realization rates vary by firm type and market, but most well-run firms target overall realization above 80%. A firm consistently realizing below 70% has either a pricing, scope, or quality problem.

### Utilization Rate

```
Utilization = Billable Hours / Available Hours
```

Available hours is typically 1,700–2,000 per year per timekeeper (depending on the firm's expectations). Target utilization varies:
- Large international firms: 1,600–1,800 billable hours per associate per year
- Boutique MENA firms: often lower (1,200–1,500) due to different market norms
- Partners: typically lower utilization than associates (business development, management time)

Utilization is a lagging indicator. High utilization with low realization signals a pricing or scoping problem. Low utilization signals either under-staffing on business development or over-staffing on matters.

### Leverage

Leverage is the ratio of non-partner timekeepers to partners. Higher leverage amplifies partner earnings but requires strong supervision infrastructure. A practice with 5 associates per partner can generate far more revenue per partner than a 1:1 ratio, but only if the work is delegatable and the supervision is effective.

### Partner Compensation

MENA law firm partnership models vary:

| Model | Characteristics | Common in |
|---|---|---|
| Lockstep | Compensation tied to seniority/years, not individual origination | UK magic circle offices in MENA |
| Eat-what-you-kill | Origination-heavy; compensation tied to clients brought in | Independent MENA firms |
| Modified lockstep | Base seniority comp + origination bonus | Hybrid / regional firms |

Key compensation metrics tracked per partner: origination credit, billing credit, collection credit, management hours, pro bono contribution.

---

## Key financial metrics for a legal-AI product

When building analytics features or financial dashboards within a legal-AI platform, these are the metrics that matter to law firm clients:

| Metric | Formula | Why it matters |
|---|---|---|
| WIP lock-up days | WIP ÷ (Annual Revenue / 365) | Cash flow efficiency |
| AR lock-up days | AR ÷ (Annual Revenue / 365) | Collection efficiency |
| Overall realization | Cash collected / WIP recorded | Billing + collection health |
| Average hourly rate | Fees billed / hours billed | Pricing power trend |
| Utilization by timekeeper | Billable hrs / available hrs | Staffing efficiency |
| Profit per partner | Net profit ÷ equity partner count | Partner economics |
| Matter profitability | Matter revenue - matter cost | Pricing vs scope alignment |

---

## MENA-specific financial considerations

### VAT and billing

- UAE introduced 5% VAT in 2018; applies to legal services. Invoices must comply with Federal Tax Authority requirements (TRN, invoice format).
- KSA introduced VAT in 2018 at 5%, raised to 15% in 2020; ZATCA compliance required.
- Lebanon: no VAT on most legal services under the current regime, but verify current position.
- DIFC/ADGM firms billing onshore UAE clients: check the VAT treatment for cross-zone billing (typically standard-rated).

### Foreign currency billing

Many MENA firms bill in USD or EUR for international matters while incurring costs in local currency. FX risk management and invoice currency alignment are practice management issues; the legal-AI product should allow invoice currency to be set per matter.

### Retainers and advance payments

Retainer arrangements are common in MENA for both transactional and litigation work. The financial treatment differs:
- **True retainer** (availability fee): recognized as income immediately
- **Advance against fees** (security deposit): held in trust/client account until earned; not income until billed

Distinguishing these correctly is important for both financial reporting and professional ethics compliance.

---

## How this connects to the efirm finance skills

The `efirm-finance.*` skill suite (see `[[efirm-finance-wip]]`, `[[efirm-finance-billing]]`, `[[efirm-finance-reports]]`) operationalises these concepts as AI-assisted tasks: generating WIP reports, drafting billing narratives, analyzing AR aging, and summarizing matter profitability. The foundational concepts in this wiki pack are the domain knowledge those skills draw on.

---

## Caveats & currency

VAT rates and compliance requirements in MENA change frequently (the KSA rate tripled in 2020). Always verify current rates and invoice formatting requirements with the relevant tax authority before advising clients on billing compliance. Partner compensation and practice management norms vary significantly by firm size, jurisdiction, and ownership structure.

---

## Related skills

- [[wiki-legal]]
- [[wiki-product]]
- [[wiki-haqq-product]]
- [[wiki-pricing]]
- [[wiki-real-estate]]
