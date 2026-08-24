---
name: efirm-finance-trust-account-reconciliation
description: Use when a law firm accountant or compliance officer needs to perform or verify the three-way reconciliation of client trust/escrow accounts. This is a P0 compliance skill — failure exposes the firm to bar discipline, regulatory sanction, and civil liability. Covers IOLTA (US), SRA Accounts Rules (UK), DFSA client-money rules (DIFC), FSRA client-asset rules (ADGM), and KSA/UAE bar segregation requirements. Produces a reconciliation report, exception list, and remediation actions.
license: MIT
metadata: " id: efirm-finance.trust-account-reconciliation category: efirm-finance jurisdictions: [US, UK, DIFC, ADGM, KSA, UAE, LB] priority: P0 intent: [trust, compliance, IOLTA, client-money, reconciliation, segregation] related: - efirm-finance-realization-rate-tracker - efirm-finance-wip-aging-report - efirm-engagement-letter-draft - efirm-conflict-check source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'efirm-finance'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Trust Account Reconciliation

## When to use this

This is a **mandatory compliance procedure**, not an optional financial report. Use it:
- Monthly (minimum), as required by most bar/regulatory rules.
- Whenever a discrepancy is suspected (negative balance, client complaint, staff departure).
- Before any bar audit or regulatory inspection.
- On firm merger, acquisition, or dissolution — every open balance must be resolved.
- When onboarding a new matter that involves client funds (retainer, escrow, settlement proceeds).

**Critical**: Never treat trust account work as routine bookkeeping. Commingling, overdrafts, or unexplained shortfalls can result in disbarment, criminal prosecution for misappropriation, and civil liability to clients.

## Regulatory framework by jurisdiction

| Jurisdiction | Regime | Key rules | Frequency |
|---|---|---|---|
| US | IOLTA (Interest on Lawyers' Trust Accounts) | State bar rules implementing ABA Model Rules 1.15; IOLTA interest goes to legal aid | Monthly three-way reconciliation |
| UK | SRA Accounts Rules 2019 | Designated client accounts; client money must not be mixed with office money | Reconcile promptly; formal review at least every 5 weeks |
| DIFC | DFSA Client Money Rules | General client account; fiduciary duties under DIFC Trust Law | Monthly |
| ADGM | FSRA Client Asset Rules | Similar to DFSA but under ADGM regulatory framework | Monthly |
| UAE onshore | UAE Federal Law on Legal Profession + Bar rules | Segregation required; enforcement inconsistent but trend toward stricter rules | As per firm policy; recommend monthly |
| KSA | Saudi Bar Association rules | Client funds segregation required; Sharia-compliant accounts (no interest-bearing accounts) | As per bar guidance |
| Lebanon | Beirut Bar Association rules | Segregation expected; regulatory framework less formalized | As per firm policy; recommend monthly |

**Note on Sharia compliance (KSA / GCC)**: Interest-bearing IOLTA-style accounts are not permissible. Use non-interest-bearing client accounts. In the UAE and KSA, consult whether any interest accrued must be returned to the client or donated to charity.

## The three-way reconciliation

All three balances must agree within penny-tolerance at month-end. Any difference is an exception requiring immediate investigation.

```
┌─────────────────────────────────────────────────┐
│  LEG 1: Bank Statement Balance                  │
│  Ending balance per bank statement as of        │
│  reconciliation date                            │
│  +/- Timing items (outstanding checks,          │
│       deposits in transit)                      │
│  = Adjusted bank balance                        │
└──────────────────┬──────────────────────────────┘
                   │ must equal
┌──────────────────▼──────────────────────────────┐
│  LEG 2: Trust Ledger Balance                    │
│  Running balance in firm's accounting system    │
│  for the trust account                          │
└──────────────────┬──────────────────────────────┘
                   │ must equal
┌──────────────────▼──────────────────────────────┐
│  LEG 3: Sum of Individual Client Ledger Balances│
│  Each active client/matter has a sub-ledger     │
│  All sub-ledger balances must sum to trust      │
│  ledger total                                   │
└─────────────────────────────────────────────────┘
```

If Leg 1 ≠ Leg 2: bank recording error or timing item error.
If Leg 2 ≠ Leg 3: a client ledger entry is missing, duplicated, or misposted.
If any leg shows a negative balance: **immediate escalation required**.

## Step-by-step procedure

1. **Pull bank statement** for the trust account as of the reconciliation date.
2. **Identify outstanding items**: checks written but not yet cleared; deposits received by firm not yet credited by bank.
3. **Compute adjusted bank balance**: bank ending balance + deposits in transit − outstanding checks.
4. **Pull trust ledger** from accounting system; confirm ending balance matches adjusted bank balance.
5. **Pull all client sub-ledger balances** as of the same date; sum them.
6. **Compare sum of sub-ledgers to trust ledger**; they must be equal.
7. **Document all timing items** with dates and descriptions.
8. **Sign off** (authorized signatory — typically managing partner or CFO) with date.
9. **File** the completed reconciliation with supporting documents per jurisdiction retention rules.

## Inputs required

| Input | Source |
|---|---|
| Bank statement (monthly) | Bank portal or paper statement |
| Trust ledger / general ledger extract | Accounting system (Clio, Elite, SAP, etc.) |
| Client sub-ledger listing | Accounting system |
| Prior month's reconciliation | Firm records |
| List of outstanding items from prior period | Prior reconciliation file |

## Flags and exception handling

| Exception | Severity | Action |
|---|---|---|
| Negative client balance (any sub-ledger) | CRITICAL | Immediate escalation to managing partner; investigate and cure within 24 hours; may require bar notification |
| Three-way imbalance | HIGH | Trace every transaction since last clean reconciliation; do not release funds until resolved |
| Stale balance (>6 months with no activity) | MEDIUM | Return to client or follow unclaimed property / dormant funds rules by jurisdiction |
| Missing payee identification | MEDIUM | Obtain documentation before disbursement |
| Interest credited to trust (non-Sharia markets) | MEDIUM | Confirm it is being swept to IOLTA fund or returned to client per agreement |
| Commingling: firm funds in trust account | CRITICAL | Regulatory violation; cure immediately; assess reporting obligation |
| Disbursement without sufficient client funds | CRITICAL | Potential misappropriation; legal counsel required |

## Output format

```
TRUST ACCOUNT RECONCILIATION — [Account Name/Number] — [Date]

LEG 1: Bank Statement
  Bank statement ending balance:    $X
  + Deposits in transit:            $A
  − Outstanding checks:             $B
  Adjusted bank balance:            $C

LEG 2: Trust Ledger
  Trust ledger balance per system:  $C  [must equal Leg 1]

LEG 3: Client Sub-Ledgers
  [Client/Matter 001]               $D1
  [Client/Matter 002]               $D2
  ...
  Sum of sub-ledgers:               $C  [must equal Leg 2]

RECONCILIATION STATUS: ✓ BALANCED / ✗ EXCEPTION

EXCEPTIONS (if any):
  [Exception description, amount, action required, owner, deadline]

PREPARED BY: [Name]        DATE: [Date]
REVIEWED BY: [Name]        DATE: [Date]
```

## Retention and access

- Reconciliation records: retain minimum 7 years (matches typical bar retention rules; some jurisdictions require longer).
- Access: restrict to finance staff and partners; attorney-client privilege may attach to trust balances.
- Audit trail: all adjusting entries must be logged with user, timestamp, and reason.

## Limits and escalation

- This skill generates the report and flags exceptions. Detected violations (commingling, shortfall) must be escalated immediately to the managing partner and firm counsel — they may trigger mandatory bar reporting obligations.
- Do not attempt to "cure" a shortfall by moving office funds into trust without partner authorization and documentation — that action itself may require disclosure.

## Related skills

- [[efirm-finance-realization-rate-tracker]]
- [[efirm-finance-wip-aging-report]]
- [[efirm-engagement-letter-draft]]
- [[efirm-conflict-check]]
- [[efirm-matter-creation-flow]]
