---
name: connector-stripe
description: Use when the legal-AI platform needs to manage billing, subscriptions, invoices, or payment lifecycle events — including plan upgrades from the UI, in-chat upsell flows, invoice generation with VAT compliance for UAE and KSA, failed payment recovery, and trial conversion. P0 connector for platform revenue. Covers all subscription tiers (Free through Enterprise) and the add-on credit model. Triggers on any billing, payment, upgrade, refund, or subscription state change request.
license: MIT
metadata: " id: connector.stripe category: connector priority: P0 intent: [__connector__] related: [connector-hubspot-crm, connector-posthog, connector-linear] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'connector'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Connector — Stripe

## What it does

Stripe is the billing and payment infrastructure for the legal-AI platform. The Stripe connector is the integration layer between the platform and Stripe, managing the full subscription lifecycle from signup through cancellation, including VAT compliance for the platform's key markets.

This is a **P0 connector** — it is on the critical path for platform revenue and must never be unavailable for more than 15 minutes without an incident escalation.

## Setup / auth

### API keys

- **Secret key** (`sk_live_...`): used for server-side operations — creating customers, managing subscriptions, processing refunds. Never expose to the client side.
- **Publishable key** (`pk_live_...`): used client-side for Stripe.js payment element embedding only.
- **Webhook signing secret**: used to verify webhook event payloads. Mandatory — never process webhook events without signature verification.

All keys stored in the platform's secrets manager per-environment (production vs staging). Separate keys for each environment — never use production keys in staging.

### Tenant isolation

Each legal-AI tenant has their own Stripe customer object:
- `customer.id` is the primary cross-system identifier.
- No cross-tenant billing data access.
- All platform-side queries are scoped to the tenant's customer ID.

## Subscription model

| Plan | Price | Credits/month | Key features |
|---|---|---|---|
| Free | $0 | Limited trial credits | Core skills; BYO-key only |
| Starter | $9/mo | 10,000 credits | All core skills; standard support |
| Pro | $49/mo | 50,000 credits | All skills; priority support; eFirm doc gen |
| Business | $199/mo | Unlimited (fair use) | eFirm features; team seats; custom integrations |
| Enterprise | Custom | Custom | SLA; private deployment; legal opinion workflows |

### Add-ons

- Extra credit packs (10k, 50k, 100k units) — one-time purchase, applied to current period.
- Onboarding service: a fixed-fee item added to the first invoice.
- Custom integration development: custom Stripe product with milestone invoicing.

## Capabilities

### Subscription management

- Create a new subscription on plan selection.
- Upgrade a subscription (proration calculated by Stripe; surface the prorated amount to the user before confirming).
- Downgrade a subscription at period end (no immediate proration; user retains current plan until next billing date).
- Cancel a subscription (with retention flow — offer a pause option before cancel).
- Reactivate a canceled subscription.

### Invoice management

- Generate on-demand invoices for custom/enterprise agreements.
- Retrieve invoice history for a customer.
- Allow invoice PDF download from the customer portal.
- Apply coupons or credits to invoices.
- Issue a credit note (partial or full refund).

### Payment method management

- Embed Stripe's Payment Element for card entry (PCI-compliant; card data never touches platform servers).
- Update payment method without re-entering card for existing customers.
- Support SEPA Direct Debit for EU customers (relevant for French and EU-based law firms).
- ACH Debit for US-based firms (available on Business and Enterprise plans).

### Refund processing

- Process full or partial refunds with a reason code.
- Requires `billing:refund` platform permission — only users with elevated access.
- All refunds logged with reason, amount, actor, and timestamp.

### Customer portal

- Embed Stripe's hosted Customer Portal for self-service billing management.
- Users can update payment method, download invoices, and cancel subscription without contacting support.
- The portal is accessible from `/settings → Billing` in the platform UI.

### Trial conversion

- Trial periods: 14 days on Starter; 7 days on Pro (configurable).
- Trial-end reminder sequence:
  - Day 7 (of 14-day trial): in-chat prompt + email ("You have 7 days left — here's what you'd lose on Free").
  - Day 12: stronger prompt + link to `/settings → Billing`.
  - Day 14: trial ends; plan downgrades to Free automatically; email confirmation.
- Stripe's `trial_end` webhook triggers the downgrade event.

## Tax and VAT compliance

| Market | Tax | Rate | Mechanism |
|---|---|---|---|
| UAE | VAT | 5% | Stripe Tax with UAE business registration |
| KSA | VAT | 15% | Stripe Tax; KSA ZATCA-compliant invoices |
| EU (B2B) | VAT (reverse charge) | 0% (buyer accounts) | Validate VAT number via Stripe; apply reverse charge |
| EU (B2C) | VAT | Local rate (varies) | Stripe Tax determines rate by customer location |
| UK | VAT | 20% | Stripe Tax with UK VAT registration |
| Lebanon | No VAT on digital services | 0% | No Stripe Tax configuration needed |

**Stripe Tax** handles automatic calculation. The platform must ensure the customer's country and tax ID are captured at signup to avoid incorrect tax application.

All invoices issued under UAE and KSA VAT must include:
- Seller TRN (Tax Registration Number).
- Customer TRN (if provided, for B2B).
- Tax amount clearly itemized.
- ZATCA-compliant format for KSA B2B invoices.

## Webhooks

Stripe webhooks are the primary mechanism for keeping platform state in sync with billing state. Required subscriptions:

| Webhook event | Platform action |
|---|---|
| `customer.subscription.created` | Provision plan; update user tier in platform DB |
| `customer.subscription.updated` | Update plan tier; recalculate credit balance |
| `customer.subscription.deleted` | Downgrade to Free; archive eFirm data per retention policy |
| `invoice.paid` | Confirm payment; update last payment date in HubSpot |
| `invoice.payment_failed` | Trigger dunning email; flag account as payment-failed |
| `customer.subscription.trial_will_end` | Send trial-end reminder (3 days before) |
| `payment_method.attached` | Confirm payment method on file |
| `charge.dispute.created` | Alert finance team; pause account pending resolution |

All webhook events must be verified using the Stripe webhook signing secret before processing.

Implement a **dead-letter queue** for failed webhook deliveries — missed events can cause billing state desync (e.g., a user staying on Free after paying).

## Failed payment recovery (dunning)

1. **Day 0** (payment fails): automated email + in-platform banner.
2. **Day 3**: second email with direct link to update payment method.
3. **Day 7**: third email; plan access restricted (read-only).
4. **Day 14**: subscription canceled; account downgraded to Free.

Stripe's Smart Retries (configured in the Stripe Dashboard) automatically retry failed charges on an optimized schedule before the dunning sequence triggers.

## Critical security requirements

- **PCI compliance:** Stripe handles card data; the platform never receives or stores card numbers. Do not add any logging that could capture payment element inputs.
- **Idempotency keys:** All POST requests to Stripe must use idempotency keys to prevent duplicate charges from network retries.
- **Multi-currency:** where possible, charge in the customer's local currency (AED for UAE, SAR for KSA, EUR for EU, GBP for UK). Currency selection at checkout; no silent currency conversion.

## Failure modes

| Failure | Cause | Resolution |
|---|---|---|
| `card_declined` | Card declined by issuing bank | Surface decline reason code to user; provide link to update payment method |
| Webhook signature mismatch | Wrong signing secret or payload tampered | Reject event; alert security team |
| Subscription state desync | Webhook missed; dead-letter queue not processed | Run reconciliation job; check Stripe Dashboard directly |
| Tax miscalculation | Customer country not set | Require country at signup; backfill via bulk update |
| Dispute filed | Chargeback from customer | Alert finance immediately; gather evidence; respond within Stripe's dispute window |

## Related skills

- [[connector-hubspot-crm]]
- [[connector-posthog]]
- [[connector-linear]]
