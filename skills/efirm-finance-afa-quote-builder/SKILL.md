---
name: efirm-finance-afa-quote-builder
description: Use when a law firm needs to prepare a fee proposal using Alternative Fee Arrangements (AFAs) — generating quote variations across fixed fee, capped hourly, blended rate, success fee, retainer-credit, subscription, and volume-discount structures. Produces three quote variations with range estimates per phase, a sensitivity analysis, risk-sharing framing, and a comparison against the hourly baseline. Applies to any matter type and jurisdiction; the AFA structure is practice-area-agnostic.
license: MIT
metadata: " id: efirm-finance.AFA-quote-builder category: efirm-finance jurisdictions: [__multi__] priority: P1 intent: [pricing, afa, alternative fee arrangement, fixed fee, blended rate, success fee, legal pricing] related: [efirm-finance-billing-narrative-cleanup, efirm-finance-budget-vs-actual-matter, efirm-finance-contingency-fee-calculator, efirm-finance-invoice-generator-from-time-entries] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'efirm-finance'.
Namespaced as louis-<category>-<skill> on registration.
-->


# AFA Quote Builder

An Alternative Fee Arrangement (AFA) is any pricing structure other than pure hourly billing. The shift to AFAs is driven by in-house counsel demanding budget predictability, competitive pressure between firms, and the efficiency gains that legal AI makes visible. This skill generates structured AFA proposals for any matter, with the decision data the partner needs to price intelligently.

## When to use this

- A client has asked for a fixed-price or budget-capped engagement letter
- The firm is pitching for a panel appointment and needs a model fee schedule
- The relationship partner wants to present pricing options (not just an hourly engagement letter)
- The billing partner wants to assess whether an existing matter should be converted to an AFA
- As a tool to reverse-engineer: given the client's budget, what can the firm commit to?

## Inputs

| Input | Notes |
|---|---|
| Matter type | M&A transaction, litigation, employment dispute, regulatory filing, real estate, etc. |
| Matter complexity | Low / medium / high / bet-the-company |
| Urgency | Standard timeline vs compressed |
| Jurisdiction | Affects rate expectations and local market comparables |
| Team composition | Senior partner, partner, senior associate, associate, paralegal — and anticipated mix |
| Phase breakdown | List the phases of the matter (e.g., due diligence, documentation, negotiation, closing) |
| Comparable historic matters | If available from matter management system |
| Client type | Panel relationship / new client / one-off |
| Outcome sensitivity | Is there a measurable outcome the client cares about (deal close, regulatory approval, settlement amount)? |

## AFA Structures

### 1. Fixed Fee (Phase-by-Phase)
A flat fee is charged for each defined phase of the matter. Phase completion triggers the invoice.

**Best for**: transactions with predictable scope (standard NDA, routine lease, formation documents); litigation phases with defined procedural steps.

**Pricing discipline**: break the matter into phases; estimate hours per phase at each seniority level; apply rates; add a risk margin (typically 10–20% for scope uncertainty). Phase-level fixed fees are easier to price and easier for the client to understand than a single lump sum.

**Output format:**
```
Phase          Scope                               Fixed Fee
─────────      ────────────────────────────────    ─────────
Phase 1        Initial review + legal opinion      [Amount]
Phase 2        First draft documents               [Amount]
Phase 3        Negotiation and iterations          [Amount]
Phase 4        Signing + closing                   [Amount]
─────────      ────────────────────────────────    ─────────
Total                                              [Amount]
```

### 2. Capped Fee (Hourly with Hard Cap)
Hourly billing up to a guaranteed maximum (the cap). If the team exceeds the cap, the over-run is absorbed by the firm.

**Best for**: matters where scope is broadly defined but might compress; clients who want both rate transparency and a budget ceiling.

**Risk allocation**: the cap transfers the risk of scope overrun to the firm. Price the cap at approximately the 75th percentile of estimated hours, not the median — otherwise you absorb normal variance.

**Clause**: "Fees will be billed on a time-and-materials basis at the hourly rates listed below. Total fees for this engagement will not exceed [cap amount] without your prior written authorization."

### 3. Blended Rate
A single hourly rate applied to all time entries, regardless of the timekeeper's seniority. The blended rate is the weighted average of the team's actual rates, adjusted for the anticipated mix.

**Formula:**
```
Blended rate = (Partner hrs × Partner rate + Sr Assoc hrs × Sr Assoc rate + 
                Assoc hrs × Assoc rate + Paralegal hrs × Paralegal rate)
                ÷ Total anticipated hours
```

**Best for**: clients who find rate-by-timekeeper invoices administratively burdensome; in-house legal teams that want a simple billing relationship.

**Risk**: if the actual team mix is more senior than anticipated, the firm loses margin. If less senior, the firm gains. Recalibrate the blended rate if the matter shifts substantially.

### 4. Success / Contingency Fee
A percentage of the outcome, payable on achieving a defined result. May be combined with a reduced base fee (hybrid).

**Best for**: litigation recovery, debt collection, M&A deal close where the outcome is binary, regulatory approval campaigns.

**Jurisdiction restrictions**: see [[efirm-finance-contingency-fee-calculator]] for jurisdiction-specific rules (Lebanon: contingency as sole fee not permitted for lawyers; France: pacte de quota litis prohibited; UAE/KSA: permitted subject to reasonableness).

**Pricing output:**
```
Outcome scenario    Probability    Recovery    Fee (X%)    Expected value
──────────────────  ───────────    ────────    ────────    ──────────────
Favorable judgment  40%            [Amount]    [Amount]    [Amount]
Settlement          45%            [Amount]    [Amount]    [Amount]
Adverse             15%            0           0           0
──────────────────  ───────────    ────────    ────────    ──────────────
Expected fee                                              [Amount]
Hourly baseline estimate                                  [Amount]
AFA premium / discount vs hourly                          [Amount (%)]
```

### 5. Monthly Retainer + Retainer Credit
A fixed monthly retainer provides a defined scope of services. Hours billed against the retainer; excess hours charged at agreed rates; under-utilized retainer may be carried forward or forfeited (depending on agreement).

**Best for**: in-house counsel who need a legal resource available without a transactional relationship; recurring compliance, employment, or commercial queries.

**Retainer structure:**
```
Monthly retainer:    [Amount]
Included hours:      [X hours per month] at [blended rate]
Excess hours:        [Rate per hour]
Unused hours:        [Carry forward / forfeit / credit to next month]
Retainer review:     [Quarterly / annually based on actual consumption]
```

### 6. Subscription (All-You-Can-Eat)
A flat monthly or annual subscription covers unlimited access to defined legal services (or a defined category). Used by in-house teams for high-volume routine work.

**Best for**: multinational in-house teams that need high-volume routine services (NDA review, commercial contract review, employment queries, regulatory filings below a threshold of complexity).

**Scope discipline**: define what is included (e.g., "standard commercial contract review up to 30 pages, maximum 5 contracts per week") and what falls outside (litigation, acquisition, bespoke advice on novel points of law). Without scope limits, the subscription is priced incorrectly.

### 7. Volume Discount Tiers
Standard rates apply; discount increases with volume of work placed.

**Best for**: panel relationships where the client places multiple matters per year and wants volume recognition.

**Tier example:**
```
Annual fees billed    Discount on standard rates
──────────────────    ─────────────────────────
< [Amount]            0% (rack rates)
[Amount] – [Amount]   5%
[Amount] – [Amount]   8%
> [Amount]            12%
```

## Output — Three Quote Variations

For each matter, generate three alternatives:

**Variation A — Firm predictability (fixed fee / capped)**
Maximizes budget certainty for the client; firm absorbs scope risk. Appropriate for established client relationship with good scope definition.

**Variation B — Shared risk (blended rate / hybrid)**
Hourly transparency with rate simplicity or a base fee plus success component. Appropriate for uncertain-scope matters or outcome-sensitive engagements.

**Variation C — Retainer / subscription**
For recurring work or long-term relationship clients. Appropriate when the client has ongoing legal needs and wants a relationship, not transactional billing.

### For each variation, provide:
- Total fee estimate (range: low / mid / high)
- Phase breakdown
- Sensitivity: what increases the fee (scope creep, extended timeline, new regulatory requirement)
- Comparison to estimated hourly billing (AFA represents X% discount or premium)
- Risk allocation statement: who bears cost overruns?

## Sensitivity Analysis

| Variable | Impact on fee | Fee change |
|---|---|---|
| Due diligence findings requiring 2 additional expert reviews | Phase 1 expands | +[Amount] |
| Counterparty requests 3 additional negotiation rounds | Phase 3 extends | +[Amount] |
| Regulatory approval delay by 60 days | Timeline extends | +[Amount] (or 0 if fixed fee structure) |
| Matter settles 60% through Phase 3 | Phase 3 incomplete | Credit/return of [Amount] per agreed terms |

## Comparison vs Hourly Baseline

```
Hourly baseline estimate:
  Partner:        [X] hours × [Rate]  = [Amount]
  Sr Associate:   [X] hours × [Rate]  = [Amount]
  Associate:      [X] hours × [Rate]  = [Amount]
  Paralegal:      [X] hours × [Rate]  = [Amount]
  ──────────────────────────────────────────────
  Total hourly:                         [Amount]

AFA Variation A (fixed fee):            [Amount]  ([+/-X]% vs hourly)
AFA Variation B (blended rate capped):  [Amount]  ([+/-X]% vs hourly)
AFA Variation C (retainer/month):       [Amount/month estimate]
```

If the AFA is priced above the hourly baseline, explain the value: "The fixed fee includes risk premium for scope uncertainty; based on this matter type, historic scope overruns average 20–30% above initial estimate."

## Failure Modes and Mitigations

| Risk | Mitigation |
|---|---|
| Scope creep beyond what the fixed fee covers | Define scope precisely; include a change-order process |
| Underestimation of hours | Price at 75th percentile of range, not median |
| Client requests additional jurisdictions mid-matter | Specify that fee covers [named jurisdictions] only |
| Success fee trigger disputed (what counts as "success"?) | Define trigger with objective, measurable criteria |
| Retainer unused — client feels they're paying for nothing | Quarterly utilization reports; proactive outreach |

## Related skills

- [[efirm-finance-billing-narrative-cleanup]]
- [[efirm-finance-budget-vs-actual-matter]]
- [[efirm-finance-contingency-fee-calculator]]
- [[efirm-finance-invoice-generator-from-time-entries]]
