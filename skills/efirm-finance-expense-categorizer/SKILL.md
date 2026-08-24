---
name: efirm-finance-expense-categorizer
description: Use when a law firm needs to automatically categorize expenses into reimbursable client costs, non-reimbursable overhead, capital expenditure, and tax-deductible vs non-deductible buckets. Matches reimbursable expenses to matters, flags unmatched items, generates journal-entry suggestions for the general ledger, and identifies variances from budget. Designed to feed into the invoice-generator workflow for client disbursement billing and into the firm's financial reporting.
license: MIT
metadata: " id: efirm-finance.expense-categorizer category: efirm-finance jurisdictions: [__multi__] priority: P2 intent: [expense, finance, disbursements, client costs, overhead, expense categorization, gl coding] related: [efirm-finance-invoice-generator-from-time-entries, efirm-finance-budget-vs-actual-matter, efirm-finance-billing-narrative-cleanup] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'efirm-finance'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Expense Categorizer

Every expense incurred by a law firm falls into one of four categories: client-reimbursable costs (billed to clients as disbursements), overhead (firm's own operating cost), capital expenditure (assets), or tax-deductible items. Misclassification results in incorrect invoicing, understated overhead, incorrect tax returns, and failed financial audits. This skill automates the classification workflow.

## When to use this

- Processing expense reports from lawyers and staff
- Month-end close: categorizing all accrued expenses before preparing financial statements
- Pre-invoice review: ensuring all client-reimbursable disbursements are captured and correctly allocated to matters
- Tax preparation: separating deductible from non-deductible expenses
- Budget variance analysis: identifying overhead categories that are running over plan

## Four Expense Categories

### Category 1: Reimbursable Client Costs (Disbursements)

Expenses directly attributable to client matters, which are billed to the client as disbursements:

| Expense type | Examples |
|---|---|
| Court and tribunal filing fees | Filing fees, court expert fees, arbitration fees |
| Process server and bailiff fees | Service of process, execution |
| Expert and consultant fees | Accounting experts, technical experts, medical experts |
| Document production | Printing large volumes for disclosure, binding |
| Travel for client matters | Flights, hotels, ground transport for client-related travel |
| Translation and interpretation | Certified translations of documents; interpreters at hearings |
| Registration and notarial fees | Notary fees for document authentication; registration at land registry |
| Search fees | Company registry searches, land registry searches, IP registry |
| Courier and delivery | Document delivery for client matters |

**Rule**: to be reimbursable, the expense must be: (a) directly caused by the client matter; (b) not already included in the firm's hourly rate; (c) pre-authorized by the client if above an agreed threshold.

### Category 2: Non-Reimbursable Overhead

Firm's own operating costs, not charged to clients:

| Expense type | GL code (typical) |
|---|---|
| Rent and building costs | Occupancy |
| Utilities (electricity, internet, phone) | Occupancy / IT |
| Salaries and employment costs | Personnel |
| Software subscriptions (practice management, research databases) | IT / Professional services |
| Professional development and training | Personnel / Training |
| Marketing and business development | Business development |
| Professional indemnity insurance | Insurance |
| Bar association fees and licenses | Professional |
| Firm-wide courier and postage (not client-specific) | Administrative |

### Category 3: Capital Expenditure (CapEx)

Assets with useful life >1 year:

| Item | Treatment |
|---|---|
| Computers and servers | Capitalize; depreciate over 3–5 years |
| Office furniture and fit-out | Capitalize; depreciate over 5–10 years |
| Leasehold improvements | Capitalize; amortize over lease term |
| Software licenses (perpetual) | Capitalize; amortize over useful life |
| Vehicles | Capitalize; depreciate |

### Category 4: Tax-Deductible vs Non-Deductible

Depends on jurisdiction and the nature of the expense:
- **Generally deductible**: ordinary business expenses (salaries, rent, professional fees, research subscriptions, travel for business)
- **Generally non-deductible / restricted**: entertainment (partially deductible in some jurisdictions; fully non-deductible in others), penalties and fines (never deductible), gifts above threshold amounts, personal expenses inadvertently charged to the firm
- **MENA notes**: UAE corporate tax (9% from June 2023) — deductibility follows accounting treatment with limited specific disallowances (e.g., bribes are non-deductible; charitable contributions in excess of limits are restricted); KSA Zakat and income tax rules apply

## Categorization Workflow

### Step 1: Receive expense items

Accept input in any format: expense report, credit card statement, bank transaction feed, paper receipts (OCR).

Each item should include:
- Date
- Vendor / payee
- Amount and currency
- Description / reference
- Matter reference (if applicable)
- Submitter (employee name)

### Step 2: Auto-classify by pattern matching

Apply classification rules:
```
IF vendor = [court name / filing portal] → Category 1 (Court fee)
IF vendor = [airline / hotel / transport] AND matter_ref present → Category 1 (Travel — reimbursable)
IF vendor = [airline / hotel / transport] AND matter_ref absent → Category 2 (Internal travel — overhead)
IF vendor = [software subscription list] → Category 2 (IT overhead)
IF amount > CapEx threshold (e.g., >$1,000 single item) AND description = equipment → Category 3
IF description = "entertainment" or "meals" → Flag for review (tax treatment varies)
```

### Step 3: Match to matter

For Category 1 items:
- Match the expense to the matter identified in the expense report
- Flag if no matter reference is assigned (requires manual assignment before the expense can be billed to a client)
- Cross-check: is the expense within the client's pre-approved expense cap?

### Step 4: Flag for review

Exceptions that require human review:
- No matter reference on what appears to be a client cost
- Expense above pre-approval threshold (typically > [firm's threshold, e.g., $500])
- Expense in an unusual category or from an unusual vendor
- Duplicate submission (same amount, same vendor, same date, different submitter)
- Personal expenses inadvertently included (e.g., personal groceries on a business card)
- Missing receipt (amounts above a minimum threshold require receipts)

### Step 5: Generate outputs

#### Categorized expense report

```
CATEGORIZED EXPENSE REPORT
Period: [Month]        Date: [Date]
─────────────────────────────────────────────────────────────────────
Date        Vendor              Description           Category     Amount
──────────  ──────────────────  ────────────────────  ──────────   ──────
[Date]      Dubai Courts        Filing fee — Matter X  Reimb/Cat1  [Amt]
[Date]      [Expert Firm]       Expert fee — Matter Y  Reimb/Cat1  [Amt]
[Date]      [Hotel]             Business travel (no matter ref) CAT2-Flag [Amt]
[Date]      [Software vendor]   Legal research sub     Cat2-IT     [Amt]
[Date]      [Furniture store]   Office chairs (6)      Cat3-CapEx  [Amt]
─────────────────────────────────────────────────────────────────────
CATEGORY 1 (Reimbursable):      [Amount]   [X items]
CATEGORY 2 (Overhead):          [Amount]   [X items]
CATEGORY 3 (CapEx):             [Amount]   [X items]
FLAGGED FOR REVIEW:             [Amount]   [X items]
─────────────────────────────────────────────────────────────────────
```

#### Journal entry suggestions

For each categorized expense, suggest the GL entry:

```
Date: [Date]
  DR  Client Disbursements — [Matter ref]   [Amount]
  CR  Accounts Payable / Cash               [Amount]
  Memo: [Expert fee / court fee] for Matter [X]

Date: [Date]
  DR  Office Overhead — IT Subscriptions    [Amount]
  CR  Accounts Payable / Credit Card        [Amount]
  Memo: Monthly [software] subscription — [month]
```

#### Matter disbursement ledger (for billing)

After categorization, generate a per-matter disbursement list for inclusion in the next invoice (via [[efirm-finance-invoice-generator-from-time-entries]]):

```
DISBURSEMENTS — Matter: [Client / Matter Name]
─────────────────────────────────────────────────────────────────────
Date        Description                            Amount
──────────  ────────────────────────────────────   ──────
[Date]      Court filing fee — [proceeding name]   [Amt]
[Date]      Expert fee — [name / firm]             [Amt]
[Date]      Travel — [destination, purpose]        [Amt]
─────────────────────────────────────────────────────────────────────
Total disbursements this period:                   [Amt]
```

## Budget Variance Flagging

For overhead expenses:
- Compare monthly actual vs monthly budget by GL category
- Flag categories where actual > budget by more than [10–15%]
- Produce a one-line summary for partner/finance review: "IT subscriptions are tracking [X]% above budget YTD; driven by [software X] price increase."

## Related skills

- [[efirm-finance-invoice-generator-from-time-entries]]
- [[efirm-finance-budget-vs-actual-matter]]
- [[efirm-finance-billing-narrative-cleanup]]
