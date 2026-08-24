---
name: docs-billing-and-credits
description: Use when a user asks about pricing, plan tiers, credit consumption, subscription management, or billing configuration for the legal AI platform. This is a platform documentation skill covering the per-seat plus usage-credit billing model, Stripe integration, self-serve top-up, enterprise invoice billing, and credit consumption rates for premium features.
license: MIT
metadata: " id: docs.billing-and-credits category: docs jurisdictions: [__multi__] priority: P2 intent: [__docs__, billing, pricing, credits, subscription, stripe, enterprise] related: [docs-enterprise-deployment, docs-audit-log-export, docs-faq-pack] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'docs'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Billing and Credits

## Overview

The platform uses a two-layer billing model:

1. **Per-seat subscription**: a fixed monthly or annual fee per user on the workspace. Covers core features available on the plan tier.
2. **Usage credits**: a consumed balance for premium features that require significant compute or third-party API cost. Credits are purchased separately or bundled with plan tiers.

## Plan tiers

| Tier | Target user | Seat fee | Credits included | Key features |
|---|---|---|---|---|
| **Free** | Solo practitioners, students, individuals exploring the platform | $0 | 50 credits/month | Chat, basic drafting, NDA and standard templates |
| **Professional** | Individual lawyers and consultants | Per-seat monthly fee (see pricing page for current rates) | 500 credits/month | All drafting skills, document review, multi-doc compare |
| **Team** | Small to mid-size firms (2–20 users) | Per-seat (volume discount) | 1,000 credits/seat/month | Shared matters, team folders, basic eFirm features |
| **Enterprise** | Large firms and legal departments | Custom pricing | Custom credit bundle | All features + SSO, audit logs, custom data residency, dedicated support |

Current pricing is published on the platform pricing page. Prices are listed in USD; invoicing in AED, SAR, or EUR available for enterprise customers.

## Credit consumption — premium features

Credits are consumed per operation. Reference rates (verify in-app for current values):

| Feature | Credit cost per use |
|---|---|
| Deep research (multi-source legal research) | 10–30 credits depending on scope |
| Multi-document compare (redline comparison) | 5 credits per document pair |
| OCR — scanned document ingestion | 2 credits per page |
| Long document analysis (>50 pages) | 10–50 credits depending on length |
| Arabic-English translation (legal documents) | 5 credits per 1,000 words |
| Bulk contract review (10+ documents) | 5 credits per document |

Credits do not expire within the billing cycle on Professional and Team plans. Unused credits do not roll over to the next billing cycle on monthly plans; annual plans include a rollover provision — verify in the subscription settings.

## Payment methods

- **Self-serve**: credit card via Stripe. Visa, Mastercard, Amex accepted. 3D Secure supported. MENA-issued cards are supported on Stripe's regional gateway.
- **Credit top-up**: buy additional credits at any time from **Settings → Billing → Buy Credits**. Available in standard bundles (e.g., 500, 2,000, 5,000 credits).
- **Enterprise invoice billing**: available on Enterprise plan. Net-30 invoicing in USD, AED, SAR, or EUR. Wire transfer, SEPA, or SWIFT. Contact the sales team to set up.

## Stripe integration

The platform uses Stripe as the payment processor. Stripe is PCI DSS Level 1 compliant. Card details are never stored on the platform servers — they are tokenized by Stripe. The platform stores only the last 4 digits and card type for display purposes.

Stripe's EU data processing is governed by a Data Processing Agreement with Stripe. For MENA users, payments may be routed through Stripe's regional processing in accordance with applicable banking regulations.

## Managing the subscription

- **Upgrade / downgrade**: self-serve from **Settings → Billing → Plan**. Changes take effect at the next billing cycle; no prorated charges for downgrades.
- **Cancel**: cancel anytime. Access continues until the end of the current billing period. Data is retained for 90 days post-cancellation, then deleted in accordance with the data retention policy.
- **Admin controls**: workspace administrators can set per-user credit limits to prevent runaway consumption. Configure at **Settings → Billing → Credit Controls**.

## Enterprise billing notes

Enterprise customers receive:
- A named account manager and customer success engineer.
- Custom credit bundle with volume pricing.
- Net-30 invoice billing with purchase-order support.
- SOC 2 Type II attestation report available on request.
- VAT / tax compliance: invoices issued from the relevant entity in the customer's billing jurisdiction (UAE: subject to 5% VAT; KSA: subject to 15% VAT; EU: subject to applicable VAT under reverse-charge or supply-specific rules). Verify current tax treatment with the customer's finance team.

## How to use this doc

Direct users here when they ask:
- "What does it cost to use [feature]?"
- "How do I add more credits?"
- "Can I be invoiced instead of paying by card?"
- "Why was I charged X?"
- "How do I cancel?"

For pricing questions that are time-sensitive or specific (e.g., a proposed enterprise deal), direct to the sales team — pricing in this documentation is indicative and may change.

## Related skills

- [[docs-enterprise-deployment]]
- [[docs-audit-log-export]]
- [[docs-faq-pack]]
