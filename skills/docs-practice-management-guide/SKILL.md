---
name: docs-practice-management-guide
description: Use when a user asks about the platform's practice management features — matters, time tracking, billing, conflict checking, and trust accounts — or about integrating with accounting and CRM systems. This is a platform documentation skill covering the practice management feature set and its integration map (HubSpot, Stripe, NetSuite, QuickBooks, Xero).
license: MIT
metadata: " id: docs.practice-management-guide category: docs jurisdictions: [__multi__] priority: P2 intent: [__docs__, practice management, matters, time tracking, billing, conflicts, trust accounts, integrations] related: [docs-legal-ai-workspace-guide, docs-enterprise-deployment, docs-billing-and-credits, docs-audit-log-export] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'docs'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Practice Management Guide

## What practice management features are for

The practice management feature set converts the legal AI workspace from a pure drafting and research tool into a light practice management system: it connects AI-generated legal work product to the matter records, time entries, billing, conflict checks, and trust account management that a law firm needs to run its practice.

For firms that already use a dedicated practice management system (Clio, Leap, PracticePanther), the platform's practice management features are complementary: use the AI workspace for drafting and review, and sync matter and billing data to the existing PMS via API.

For firms without a dedicated PMS, the platform provides a capable subset of practice management functionality without a separate subscription.

## Features

### Matters

The matter record is the organizational unit that links all platform activity to a client engagement.

- **Matter fields**: matter name, client name, matter type (e.g., M&A, Employment, Real Estate), assigned lawyer(s), status (open / on hold / closed), jurisdiction, matter number, date opened, estimated close date.
- **Document linking**: all documents drafted or uploaded within the matter are automatically linked. Documents can also be manually linked from other matters.
- **Timeline view**: chronological audit of all activity on the matter — documents created, review conducted, deadlines added, team assignments changed.
- **Notes**: free-text notes attached to the matter record (can be used for client instructions, negotiating positions, key decision log).
- **Deadline tracking**: matter-level deadlines with configurable reminders (push notification + email). Matter-level statute of limitations deadlines flagged by the [[heuristic-statute-of-limitations-flag]] skill are automatically added here.
- **Matter export**: export full matter file as PDF dossier or ZIP archive for client delivery or firm archive.

### Time tracking

- **Timer**: start a timer on any matter. The timer runs in the background across sessions.
- **Manual time entry**: log time entries after the fact with date, duration (in hours/tenths), description, and billable/non-billable flag.
- **AI-assisted time descriptions**: optionally generate professional time narrative from a brief note ("NDA review — 3h" → "Review and annotation of mutual non-disclosure agreement between Acme Ltd and XYZ Corp (DIFC law); identification of five material risk clauses; preparation of markup for client review").
- **Rate management**: set hourly rates per user and per matter type. Override rates at the matter level.
- **Time reports**: generate time summary by matter, by user, by period. Export as CSV or PDF for billing.

### Billing

- **Invoice generation**: generate professional invoices from time entries and fixed-fee matters. Includes firm letterhead (upload via **Settings → Firm Profile**), matter reference, time entries, disbursements, and tax line (VAT at applicable rate for UAE/KSA/EU).
- **Invoice status tracking**: draft → sent → paid → overdue. Automated overdue reminders at configurable intervals.
- **Credit notes**: issue credit notes for disputed amounts.
- **Trust account integration**: flag billed amounts against trust account balance (see Trust Accounts below).
- **Stripe integration**: if Stripe is connected, clients can pay invoices via a secure payment link (credit card, Apple Pay, Google Pay). Payments are automatically reconciled against outstanding invoices.
- **Currency**: AED, USD, SAR, EUR, GBP, LBP supported. Multi-currency billing: invoice in a different currency than the firm's base currency with configurable exchange rate.

### Conflict checking

The conflict check module prevents a firm from inadvertently representing adverse parties across matters.

- **How it works**: when a new matter is created, the system automatically searches the matter and client database for matches or near-matches to the new client name, counterparty names, and related persons. Flags potential conflicts for partner review.
- **Threshold**: configurable fuzzy-match threshold (exact name match only, or broader "similar name" matching).
- **Result categories**: Clear (no conflict found); Potential conflict (similar name — review); Confirmed conflict (direct adverse representation in active matter).
- **Override**: a confirmed conflict can be overridden with a documented waiver (conflict waiver template available in the clause library); override is logged in the audit trail.
- **Integration with intake**: conflict check is automatically triggered when a new client intake is submitted via the intake skills. If a conflict is flagged, the intake workflow is paused pending partner review.

See [[efirm-conflict-check]] for the detailed conflict check skill.

### Trust accounts

For law firms managing client trust accounts (also known as client funds, escrow, or client ledger accounts).

- **Trust ledger**: per-client trust ledger tracking receipts (funds received), disbursements (payments made on behalf of client), and balance.
- **Three-way reconciliation**: monthly reconciliation of (1) bank statement, (2) trust ledger, (3) client balance listing. Reconciliation report exported as PDF for partner sign-off.
- **Alert on shortfall**: automatic alert if a disbursement would bring a client's trust account below zero or below a minimum holding threshold.
- **Regulatory compliance**: trust account rules vary by jurisdiction. Note:
  - UAE (Dubai): Law Society / DIFC equivalent rules require lawyers to maintain client funds in a separate designated client account. Mixing client funds with firm funds (commingling) is a professional responsibility violation.
  - UK: Solicitors Regulation Authority (SRA) Accounts Rules 2019 — detailed client money handling requirements.
  - Lebanon: Lebanese Bar Association rules require separate client account management.
  - KSA: Saudi Bar Association guidance on client fund management.
- The trust account module assists with record-keeping but does not substitute for jurisdiction-specific bar rules compliance.

## Integration map

| System | Integration type | What syncs |
|---|---|---|
| **HubSpot** | Bidirectional | Client records, matter pipeline, contact information. New matters in the platform create deals in HubSpot; HubSpot contact data populates matter client fields. |
| **Stripe** | Bidirectional | Invoice payment status, credit purchases, subscription management. Payment confirmations sync to invoice records. |
| **NetSuite** | Outbound | Invoice data, time entry data, matter revenue. Platform is the system of record for legal work; NetSuite is the financial system of record. |
| **QuickBooks** | Outbound | Invoice export (as QuickBooks-compatible CSV or direct API sync). Expense tracking integration. |
| **Xero** | Outbound | Invoice export, contact sync, bank reconciliation support. Xero bank feeds can import trust account transactions for reconciliation. |

Integration configuration: **Settings → Integrations → [System name]**. Each integration requires API credentials from the target system (OAuth for HubSpot and Stripe; API key for NetSuite, QuickBooks, Xero). Enterprise customers receive setup assistance from the customer success team.

## Getting started with practice management

1. **Configure firm profile**: **Settings → Firm Profile** — add firm name, logo, address, default billing currency, VAT number. This populates invoice headers.
2. **Create your first matter**: **Matters → New Matter**.
3. **Run a conflict check**: when creating the matter, the conflict check runs automatically. Review any flags before opening the matter.
4. **Log time**: open a matter and click **+ Time Entry** or use the timer button.
5. **Generate an invoice**: **Matters → [Matter name] → Billing → Generate Invoice**. Select the time entries to include, add disbursements, set the tax rate, and generate.
6. **Set up an integration**: **Settings → Integrations → Connect [System]**.

## Related skills

- [[docs-legal-ai-workspace-guide]]
- [[docs-enterprise-deployment]]
- [[docs-billing-and-credits]]
- [[docs-audit-log-export]]
- [[efirm-conflict-check]]
