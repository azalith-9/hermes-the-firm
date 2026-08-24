---
name: efirm-finance-ewallet-balance-checker
description: Use when a law firm needs to check and report on client advance retainer or e-wallet balances — displaying the current retainer balance held in trust, recent debits and credits, projected runway at current burn rate, and generating a top-up request email when the balance falls below the replenishment threshold. Must be used with trust-account compliance rules (IOLTA / client money rules); see the related trust-account-reconciliation skill for compliance layer.
license: MIT
metadata: " id: efirm-finance.eWallet-balance-checker category: efirm-finance jurisdictions: [__multi__] priority: P2 intent: [wallet, advance, retainer, client money, trust account, top-up] related: [efirm-finance-collection-rate-tracker, efirm-finance-invoice-generator-from-time-entries, efirm-finance-budget-vs-actual-matter] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'efirm-finance'.
Registered as a flat plugin skill.
-->


# eWallet / Advance Retainer Balance Checker

A client e-wallet or advance retainer is funds held by a law firm on behalf of a client, to be applied against future fees as they accrue. The firm holds these funds in a client trust account (IOLTA in US; client account in UK; separate trust account per most professional conduct rules worldwide). This skill monitors the balance, forecasts runway, and automates top-up requests.

## When to use this

- A client is on a retainer arrangement and the firm needs to monitor available funds
- Before preparing an invoice, to check whether the retainer covers the bill
- When a billing partner wants to see all retainer balances across their portfolio
- Automating a weekly or monthly retainer check as part of the billing pipeline

## Trust Account Compliance — Non-Negotiable Principle

Client retainer funds held in advance are the client's money until earned. They must be:
- Held in a separate client trust account (not commingled with firm operating funds)
- Applied to invoices only when the invoice is approved and sent to the client
- Returned to the client if unearned when the engagement ends

**This skill does not handle the trust account itself** — it reports on balances. For the compliance layer (IOLTA reconciliation, client money regulation), see the related trust-account-reconciliation skill.

## Dashboard Output

### Per-Client Retainer Balance Report

```
CLIENT RETAINER / E-WALLET DASHBOARD
Date: [Date]
─────────────────────────────────────────────────────────────────────
Client          Matter         Opening   Credits   Debits    Balance
─────────────   ────────────   ───────   ───────   ───────   ───────
[Client A]      [Matter 1]     [Amt]     [Amt]     [Amt]     [Amt]
[Client A]      [Matter 2]     [Amt]     [Amt]     [Amt]     [Amt]
[Client B]      [Matter 1]     [Amt]     [Amt]     [Amt]     [Amt]
─────────────────────────────────────────────────────────────────────
[CLIENT A TOTAL]               [Amt]     [Amt]     [Amt]     [Amt]
─────────────────────────────────────────────────────────────────────
```

### Ledger Detail (per client/matter)

```
RETAINER LEDGER — [Client Name] / [Matter Name]
─────────────────────────────────────────────────────────────────────
Date         Transaction               Amount      Running Balance
──────────   ─────────────────────     ──────      ───────────────
[Date]       Opening retainer deposit  +[Amt]      [Amt]
[Date]       Invoice [#] applied       -[Amt]      [Amt]
[Date]       Top-up payment received   +[Amt]      [Amt]
[Date]       Invoice [#] applied       -[Amt]      [Amt]
──────────────────────────────────────────────────────────────────
CURRENT BALANCE:                                   [Amt]
Last top-up date:                                  [Date] ([X] days ago)
Average monthly burn rate:                         [Amt/month]
Projected runway at current burn rate:             [X weeks / months]
Replenishment threshold:                           [Amt]
STATUS:                                            [OK / TOP-UP REQUIRED]
─────────────────────────────────────────────────────────────────────
```

## Alert Thresholds

| Status | Trigger | Action |
|---|---|---|
| OK | Balance > [2 months of average burn] | No action required |
| Monitor | Balance between 1–2 months of average burn | Notify billing partner; include in next status update |
| Top-up required | Balance < 1 month of average burn OR below agreed replenishment threshold | Generate top-up request email; send immediately |
| Critical — below threshold | Balance below next invoice estimate | Do not apply next invoice against retainer; contact client urgently |
| Zero / negative | Retainer fully depleted; outstanding fees | Immediately issue invoice; flag to billing partner; do not advance further work without authorization |

## Top-Up Request Email Draft

```
Subject: Retainer Top-Up Request — [Matter Name] — [Client Name]

Dear [Client Name / Finance Director],

We are writing to request a replenishment of your retainer on file for 
[Matter Name].

Current retainer balance:  [Amount]
Average monthly billing:   [Amount]
Estimated runway:          [X weeks]
Agreed replenishment level: [Amount]

Please arrange a wire transfer of [requested top-up amount] to our 
client trust account:

  Account name: [Firm Client Trust Account]
  Bank: [Bank name]
  IBAN / Account No: [Account number]
  SWIFT / BIC: [Code]
  Reference: [Client / Matter Name / Reference]

Please confirm once payment has been made so we can update our records.

If you have any questions or would like to discuss the retainer arrangement, 
please do not hesitate to contact me.

Kind regards,
[Partner / Finance team]
[Firm Name]
[Contact details]
```

## Runway Analysis

The runway calculation forecasts how long the current balance will last at the current burn rate:

```
Runway (months) = Current balance ÷ Average monthly billing rate

Average monthly billing rate = [Total fees in last 3 months] ÷ 3
```

A projected runway of less than 4 weeks should trigger an immediate top-up request. Runway calculations should account for any pending invoices already prepared but not yet applied.

## Integration with Invoice Pipeline

Before generating and sending an invoice, check the retainer balance:
1. **Balance sufficient**: apply the invoice against the retainer; debit the client's ledger; notify the client of the application and remaining balance in the invoice cover email
2. **Balance partially covers invoice**: apply the available balance; issue the invoice for the difference; request a top-up simultaneously
3. **Balance insufficient**: issue the invoice as normal; send the top-up request; do not hold the invoice pending the top-up (client should receive the invoice promptly)

## Time Since Last Top-Up

Track the time elapsed since the last retainer replenishment. If a client has not topped up in more than [60 days] while the matter is active, this may indicate:
- The client has forgotten (prompt needed)
- The client is experiencing cash flow difficulties (relationship signal; billing partner should call)
- The client is dissatisfied with the billing (billing dispute risk; proactively discuss)

## Related skills

- [[efirm-finance-collection-rate-tracker]]
- [[efirm-finance-invoice-generator-from-time-entries]]
- [[efirm-finance-budget-vs-actual-matter]]
