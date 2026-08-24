---
name: efirm-finance-contingency-fee-calculator
description: Use when a law firm or client needs to model and document a contingency or success-fee arrangement. Calculates fee schedules under sliding-scale and flat-percentage structures, produces expected-value tables across outcome scenarios, models the lien on recovery and expense reimbursement, and compares the contingency arrangement against an estimated hourly baseline. Covers jurisdiction-specific rules including Lebanon (success bonus only), France (pacte de quota litis prohibited), UAE/KSA (permitted with reasonableness standard), UK (CFA/DBA), and US (state-by-state).
license: MIT
metadata: " id: efirm-finance.contingency-fee-calculator category: efirm-finance jurisdictions: [UAE, KSA, LB, FR, UK, US, GCC] priority: P1 intent: [contingency, success fee, pricing, contingency fee, cfa, dba, no-win-no-fee] related: [efirm-finance-afa-quote-builder, efirm-finance-invoice-generator-from-time-entries, efirm-finance-budget-vs-actual-matter] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'efirm-finance'.
Registered as a flat plugin skill.
-->


# Contingency Fee Calculator

A contingency fee arrangement aligns the law firm's compensation with the client's outcome — the firm is paid a percentage of the recovery if the case succeeds, and little or nothing if it fails. This skill calculates fee schedules, models expected values across outcome scenarios, and documents the arrangement. Critically, it flags jurisdictional restrictions that may make pure contingency arrangements invalid.

## When to use this

- Litigation matter where the client cannot afford hourly fees and the case has sufficient recovery potential
- Debt collection with percentage-of-recovery pricing
- Settlement negotiation where the firm's fee is tied to the settlement amount
- M&A or transaction advisory where the firm's fee is tied to deal close
- Any engagement where the firm is asked to work "at risk" in exchange for a larger upside

## Required inputs

| Input | Notes |
|---|---|
| Jurisdiction | Determines whether pure contingency is permitted; see table below |
| Matter type | Litigation (civil, commercial, personal injury) / Collection / Transaction advisory |
| Estimated recovery range | Low / mid / high scenarios with probability weights |
| Hourly baseline estimate | For comparison; also the opportunity cost of the contingency arrangement |
| Expense treatment | Off the top of recovery (before percentage) or net (after percentage) |
| Settlement vs judgment | Different percentage may apply at different stages |

## Jurisdiction-Specific Rules

| Jurisdiction | Rule | Permissible structure |
|---|---|---|
| Lebanon | Contingency as the sole fee (pacte de quota litis) is not permitted for lawyers; a success bonus (honoraires de résultat) on top of a base fee is permitted | Base fee (minimum) + success bonus |
| France | Pacte de quota litis prohibited under the decree governing the legal profession (Décret n°91-1197 of November 27, 1991); honoraires de résultat (success fee on top of base) is permitted | Base fee + success bonus on top |
| KSA | Contingency fees for lawyers are permitted; courts retain discretion to adjust if the fee is unreasonable; no statutory cap | Pure contingency or hybrid permitted |
| UAE | Contingency fees are permitted; courts can adjust | Pure contingency or hybrid permitted |
| UK | Conditional Fee Agreements (CFAs): lawyer works for reduced or no fee if case fails; if case succeeds, receives normal fee plus a success uplift of up to 100% of base fee; Damages-Based Agreements (DBAs): percentage of recovery (max 25% of damages for personal injury; 50% for employment tribunal; 50% for other proceedings) | CFA or DBA — regulated forms |
| US | Contingency fees common in personal injury, employment, consumer class actions; state-by-state maximum percentages (typically 33% pre-suit, 40% post-filing, higher on appeal); fee must be in writing; must be reasonable | Sliding scale common; state rules vary |

## Fee Structure Options

### Option 1: Pure Contingency (Flat Percentage)

A single percentage of the gross recovery (or net, after expenses, depending on how "recovery" is defined):

```
Fee = Recovery × Agreed Percentage
```

**Example**: 30% of gross recovery
- If recovery = USD 500,000 → fee = USD 150,000
- If recovery = 0 (case lost) → fee = 0

**Risk**: the firm bears 100% of the cost of performing the work; if the case is lost, the firm receives nothing. This is appropriate only for matters with a reasonable probability of success and a recovery sufficient to justify the risk.

### Option 2: Sliding Scale (Stage-Based)

Different percentages apply at different stages of the matter, reflecting the increased certainty of recovery as the case progresses:

```
Stage                        Percentage of recovery
───────────────────────      ─────────────────────
Settlement pre-filing        25%
Settlement post-filing       33%
After trial has commenced    40%
After appeal                 45%
```

**Rationale**: the firm takes less risk at the pre-suit stage (likely to settle) and more risk at trial (uncertain outcome). The client benefits from a lower percentage if the case settles early.

### Option 3: Hybrid — Base Fee + Success Bonus

Required in Lebanon and France; popular elsewhere as a balanced structure:

```
Base fee:      [Amount or hourly, payable regardless of outcome]
Success bonus: [X]% of recovery above [threshold amount] (or flat amount)
Cap on bonus:  [Amount or X times the base fee]
```

**Example (Lebanon-compliant):**
- Base fee: USD 15,000 (50% of estimated hourly)
- Success bonus: 20% of amounts recovered above USD 100,000
- Cap: USD 80,000 total compensation

### Option 4: Lien on Recovery (Charging Lien)

The firm holds a charging lien on any recovery, settlement proceeds, or judgment amount as security for its fees. This is standard in US contingency practice and increasingly used in other jurisdictions.

**Lien documentation**: the engagement letter must explicitly state the lien; in some jurisdictions (US states), the lien must be filed with the court; in others, it is created automatically by the engagement letter and the firm's involvement in the proceeding.

## Expected Value Analysis

For each fee structure, calculate the expected value across outcome scenarios:

```
EXPECTED VALUE ANALYSIS
Matter: [Name]   Proposed fee: [X]% of gross recovery

Scenario         Probability   Recovery      Fee         Exp. Fee
──────────────   ───────────   ──────────    ──────────  ──────────
Favorable         45%           $800,000      $240,000    $108,000
  judgment
Settlement —      35%           $500,000      $150,000    $ 52,500
  mid-range
Settlement —      10%           $200,000      $ 60,000    $  6,000
  low
Adverse /         10%           $0            $0          $0
  dismissed
──────────────────────────────────────────────────────────────────
Expected fee value:                                       $166,500
Hourly baseline (estimated):                              $110,000
Contingency premium vs hourly:                           +$56,500  (+51%)
Risk-adjusted premium per unit of risk:                   [X]
```

The contingency premium compensates the firm for: (a) the time value of deferred payment; (b) the risk of zero recovery; (c) the opportunity cost of the firm's capacity.

## Expense Treatment

Two standard approaches to expenses (court fees, expert witness fees, travel, filing fees):

**Off the top**: expenses are deducted from the recovery before the percentage fee is calculated.
```
Net recovery for fee calculation = Gross recovery - Expenses incurred
Fee = Net recovery × Contingency %
```

**Net (after percentage)**: the percentage fee is calculated on gross recovery; expenses are then deducted from the client's share.
```
Fee = Gross recovery × Contingency %
Client receives = (Gross recovery - Fee) - Expenses
```

The "off the top" approach is more favorable to the client; the "net" approach is more favorable to the firm. Specify clearly in the engagement letter.

## Settlement vs Judgment Treatment

In many sliding-scale arrangements, a different percentage applies depending on how and when the matter resolves:
- Early settlement (pre-claim): lowest percentage
- Settlement after filing: middle percentage
- Judgment after trial: highest percentage

This must be defined precisely: "settling" on the courthouse steps (after trial commences) triggers the trial rate, not the settlement rate.

## Engagement Letter Provisions for Contingency

The engagement letter must address:
1. Percentage fee (and any sliding scale with trigger events)
2. Definition of "recovery" (gross or net; whether includes costs awards)
3. Expense treatment (off the top or net)
4. What happens if the client settles without the firm's approval (most contingency agreements require the firm's consent to any settlement)
5. What happens if the client terminates the engagement before resolution (quantum meruit claim for work done; lien on recovery)
6. Whether the arrangement complies with applicable professional responsibility rules

## Comparison Output: Contingency vs Hourly

```
PRICING COMPARISON
─────────────────────────────────────────────────────────────────────
Hourly estimate (all scenarios):      [Amount]     (certain cost to client)
Pure contingency (expected value):    [Amount]     (expected cost; 0 if adverse)
Hybrid base + success (expected):     [Amount]     ([Base] certain + [bonus] expected)

From the CLIENT's perspective:
  Contingency advantage: no out-of-pocket fee risk if adverse
  Contingency cost: contingency premium (average higher cost if successful)

From the FIRM's perspective:
  Hourly: certain revenue; firm bears no outcome risk
  Contingency: higher revenue if successful; zero if adverse; capital at risk
─────────────────────────────────────────────────────────────────────
```

## Related skills

- [[efirm-finance-afa-quote-builder]]
- [[efirm-finance-invoice-generator-from-time-entries]]
- [[efirm-finance-budget-vs-actual-matter]]
