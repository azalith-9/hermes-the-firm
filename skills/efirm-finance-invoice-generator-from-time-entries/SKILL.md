---
name: efirm-finance-invoice-generator-from-time-entries
description: Use when a law firm needs to assemble and format a client invoice from cleaned time entries and categorized disbursements. Supports detailed (line-item by timekeeper and date), summary (by phase), LEDES electronic billing, and block-billing summary formats. Applies VAT/GST rates by jurisdiction (KSA 15%, UAE 5%, Egypt 14%, EU varies) and generates the invoice document plus an accounting-system export and a cover email to the client. Upstream dependencies are billing-narrative-cleanup and expense-categorizer.
license: MIT
metadata: " id: efirm-finance.invoice-generator-from-time-entries category: efirm-finance jurisdictions: [UAE, KSA, EG, EU, UK, US, GCC] priority: P1 intent: [invoice, billing, invoice generation, legal invoice, ledes, time billing, disbursements] related: [efirm-finance-billing-narrative-cleanup, efirm-finance-expense-categorizer, efirm-finance-budget-vs-actual-matter, efirm-finance-collection-rate-tracker, efirm-finance-ewallet-balance-checker] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'efirm-finance'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Invoice Generator — From Time Entries

The invoice is the point where the firm's work is translated into a request for payment. An invoice that is clearly structured, correctly formatted for the client's billing guidelines, and accurately reflects the work done reduces disputes, accelerates payment, and demonstrates professionalism. This skill builds the invoice from cleaned time entries and categorized disbursements, applies the correct tax, and generates the output documents.

## When to use this

- Monthly billing cycle: generating invoices for all active matters
- Matter-close billing: final invoice at engagement conclusion
- AFA milestone billing: invoicing when a milestone is achieved
- Interim billing for long-running matters
- Generating LEDES-format files for in-house counsel electronic billing systems

## Upstream Dependencies

This skill operates at the end of a three-skill pipeline:

```
1. [[efirm-finance-billing-narrative-cleanup]]
   ↓
2. [[efirm-finance-expense-categorizer]]
   ↓
3. [[efirm-finance-invoice-generator-from-time-entries]] (this skill)
```

Pass the outputs of steps 1 and 2 as input. If the upstream skills have not been run, the invoice will contain unclean narratives and uncategorized disbursements — run the upstream skills first.

## Required inputs

| Input | Notes |
|---|---|
| Cleaned time entries | From billing-narrative-cleanup; by timekeeper, date, description, hours |
| Categorized disbursements | From expense-categorizer; matter-matched client costs |
| Billing rates | By timekeeper; per engagement letter |
| Client billing guidelines | If the client has specific format or content requirements |
| Discount / write-down instructions | Any fee reduction authorized by the billing partner |
| Invoice period | Start and end date of the billing period |
| Tax rate | By jurisdiction (see table below) |
| Invoice format requested | Detailed / summary / LEDES / block-billing |

## Tax Rates by Jurisdiction

| Jurisdiction | Tax | Rate | Notes |
|---|---|---|---|
| UAE | VAT | 5% | Federal Decree-Law 8/2017; applies to legal services; TRN (Tax Registration Number) must appear on invoice |
| KSA | VAT | 15% | Increased from 5% to 15% in July 2020; ZATCA-compliant e-invoicing (Fatoorah) required from Phase 2 rollout |
| Egypt | VAT | 14% | Egyptian Tax Authority; applies to professional services |
| Lebanon | No VAT on legal services | 0% (no VAT) | No VAT on professional services in Lebanon currently; note: other taxes apply at the entity level |
| EU (general) | VAT | 19–25% (varies by state) | B2B reverse charge mechanism applies for cross-border EU services (client pays VAT to their tax authority) |
| UK | VAT | 20% | UK HMRC; VAT registration number required on invoice |
| US | Generally no federal sales tax on legal services | 0% (federal) | Some states impose sales tax on certain professional services; check state rules |
| Bahrain | VAT | 10% | |
| Oman | VAT | 5% | |
| Qatar | No VAT currently | 0% | |
| Kuwait | No VAT currently | 0% | |

## Invoice Format Options

### Format A: Detailed (Line-Item)

Every time entry appears as a separate line:

```
[LAW FIRM NAME]
Invoice No: [INV-YYYY-NNN]
Date: [Date]
Client: [Full Legal Name]
Matter: [Matter Name / Number]
Billing Period: [Start] to [End]

PROFESSIONAL FEES

Date        Timekeeper         Description                        Hours    Rate    Amount
──────────  ─────────────────  ─────────────────────────────────  ─────    ─────   ──────
[Date]      [Name], Partner    [Cleaned narrative from Step 1]    [X.X]    [Rate]  [Amt]
[Date]      [Name], Sr Assoc   [Cleaned narrative from Step 1]    [X.X]    [Rate]  [Amt]
[Date]      [Name], Associate  [Cleaned narrative from Step 1]    [X.X]    [Rate]  [Amt]

                                                     Subtotal:            [Amount]
                                                     Discount:  ([Amount])
                                                     Net Fees:            [Amount]

DISBURSEMENTS

Date        Description                                                    Amount
──────────  ─────────────────────────────────────────────────────────────  ──────
[Date]      [Description from expense-categorizer]                         [Amt]
[Date]      [Description]                                                  [Amt]

                                                     Total Disbursements: [Amount]

                                                     Subtotal Fees + Disb:[Amount]
                                                     VAT [X]%:            [Amount]
                                                     TOTAL DUE:           [Amount]

Payment terms: Net [30] days from invoice date
Bank details: [Account name, IBAN, BIC, Bank name, Reference]
```

### Format B: Summary (By Phase)

Aggregated fees by phase or work category — appropriate when the client prefers a summary view or where detailed narratives are not required:

```
PROFESSIONAL FEES — SUMMARY

Phase / Activity                       Hours     Amount
─────────────────────────────────────  ──────    ──────
Phase 1: Due Diligence                 [X] hrs   [Amt]
Phase 2: Documentation                 [X] hrs   [Amt]
Phase 3: Negotiation                   [X] hrs   [Amt]
─────────────────────────────────────────────────────
Total Professional Fees                [X] hrs   [Amt]
Disbursements                                    [Amt]
─────────────────────────────────────────────────────
Subtotal                                         [Amt]
VAT [X]%                                         [Amt]
TOTAL DUE                                        [Amt]
```

### Format C: LEDES (Electronic Billing)

LEDES (Legal Electronic Data Exchange Standard) format is required by many in-house legal departments. Current standard: LEDES98B or LEDES XML.

LEDES98B format: pipe-delimited flat file with specified fields:
```
LEDES98B[]
INVOICE_DATE|INVOICE_NUMBER|CLIENT_ID|LAW_FIRM_MATTER_ID|BILLING_START_DATE|BILLING_END_DATE|INVOICE_TOTAL|BILLING_START_DATE|...
[Date]|[Inv#]|[ClientID]|[MatterID]|[Start]|[End]|[Total]|...
```

Key LEDES fields:
- TASK_CODE: ABA task codes (A101–Z999) for legal work categories
- ACTIVITY_CODE: ABA activity codes (A101–A115) for specific activities
- EXPENSE_CODE: ABA expense codes (E101–E125) for disbursement types
- TIMEKEEPER_CLASSIFICATION: partner / associate / paralegal

If the client requires LEDES, also request the ABA task code list applicable to the matter.

### Format D: Block-Billing Summary (If Permitted)

Only use if the client's billing guidelines explicitly permit block billing:

```
PROFESSIONAL FEES

[Date range]  [Brief summary of work performed during the period]  [Total hrs]  [Amt]
```

This format is increasingly disfavored; use only when the client engagement letter explicitly permits it.

## Discount and Write-Down Application

Before finalizing the invoice:
1. Partner confirms any discount or write-down
2. State the discount on the invoice: "Volume discount: (Amount)" or "Professional courtesy adjustment: (Amount)"
3. Do not simply reduce the hours or rates silently — the client cannot see the value delivered if the reduction is hidden
4. For AFA matters: if the matter has come in under a fixed fee (because the work was more efficient), the fixed fee is still invoiced (the saving is the firm's); do not reduce the invoice to cost

## Retainer / E-Wallet Application

If the client has an advance retainer on file:
1. Check [[efirm-finance-ewallet-balance-checker]] for available balance
2. Apply the retainer to the invoice and note it:
   ```
   TOTAL DUE:               [Amount]
   Less: retainer applied:  ([Amount])
   NET AMOUNT PAYABLE:      [Amount]
   Remaining retainer:      [Amount]
   ```
3. If the retainer does not fully cover the invoice, request a top-up simultaneously with sending the invoice

## Cover Email to Client

```
Subject: Invoice [Number] — [Matter Name] — [Period]

Dear [Client Name],

Please find attached Invoice [Number] for professional services rendered in 
connection with [Matter Name] for the period [Start] to [End].

Summary:
  Professional fees:    [Amount]
  Disbursements:        [Amount]
  VAT ([X]%):           [Amount]
  Total due:            [Amount]
  [Retainer applied:   ([Amount])]
  [Net payable:         [Amount]]

Payment is due within [30] days of the invoice date. Please remit to:
  [Bank details]

If you have any questions regarding this invoice, please do not hesitate 
to contact [billing partner / finance team].

[Attach: PDF invoice; LEDES file if required]
```

## Accounting System Export

Generate a structured export for the firm's accounting system:

```
ACCOUNTING EXPORT — Invoice [Number]
Date: [Date]    Client: [ID]    Matter: [ID]    Amount: [Total]

GL entries:
  DR  Accounts Receivable — [Client]                [Total invoiced]
  CR  Professional Fees Revenue — [Practice Area]   [Fees]
  CR  Disbursements Revenue / Client Cost Recovery  [Disbursements]
  CR  VAT Payable                                   [VAT amount]
```

## Related skills

- [[efirm-finance-billing-narrative-cleanup]]
- [[efirm-finance-expense-categorizer]]
- [[efirm-finance-budget-vs-actual-matter]]
- [[efirm-finance-collection-rate-tracker]]
- [[efirm-finance-ewallet-balance-checker]]
