---
name: ops-hubspot-property-mapper-stripe-sync
description: Use when synchronizing Stripe billing data into HubSpot CRM contacts and deals. Defines the canonical field mapping from Stripe customer, subscription, and invoice objects to HubSpot contact and deal properties — ensuring AEs and CSMs always see current MRR, plan, renewal date, and payment health without manual data entry.
license: MIT
metadata: " id: ops.hubspot-property-mapper-stripe-sync category: ops jurisdictions: [__multi__] priority: P2 intent: [hubspot, stripe, crm-sync, billing, mrr] related: [ops-hubspot-deal-stage-router, ops-subscription-erd-validator, ops-churn-risk-detector] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'ops'.
Registered as a flat plugin skill.
-->


# Ops — HubSpot Property Mapper (Stripe Sync)

## Purpose

Stripe is the source of truth for billing; HubSpot is the source of truth for sales and customer relationships. Without an automated sync, these systems drift apart — AEs quote the wrong renewal date, CSMs don't know a payment failed, and finance can't reconcile ARR against CRM data. This skill defines the exact field mapping and sync rules between the two systems.

## Architecture

**Direction**: Stripe → HubSpot. Stripe is always authoritative for billing data. HubSpot data is updated from Stripe; never the reverse (to avoid billing data corruption).

**Sync trigger**: Stripe webhooks. Every relevant Stripe event fires a sync to HubSpot. Additionally, a daily reconciliation job sweeps for any missed events.

**Relevant Stripe webhook events**:
- `customer.created`, `customer.updated`
- `customer.subscription.created`, `customer.subscription.updated`, `customer.subscription.deleted`
- `invoice.paid`, `invoice.payment_failed`
- `customer.subscription.trial_will_end`

## Field mapping

### Contact-level fields (Stripe Customer → HubSpot Contact)

| Stripe field | HubSpot property name | Type | Notes |
|--------------|----------------------|------|-------|
| `customer.id` | `stripe_customer_id` | Text | Immutable; set once |
| `customer.email` | Standard email field | Email | Used for deduplication |
| `customer.created` | `stripe_customer_since` | Date | When they first became a Stripe customer |

### Deal-level fields (Stripe Subscription → HubSpot Deal)

| Stripe field | HubSpot property name | Type | Notes |
|--------------|----------------------|------|-------|
| `subscription.status` | `subscription_status` | Dropdown | `trialing / active / past_due / canceled / unpaid` |
| `subscription.plan.nickname` | `product` | Text | Plan name (e.g., "Pro Monthly", "Business Annual") |
| `subscription.items.data[0].price.unit_amount / 100` | `mrr` | Currency | Monthly recurring revenue; annualize for annual plans |
| `subscription.current_period_end` | `renewal_date` | Date | When the current subscription period ends |
| `subscription.cancel_at_period_end` | `cancel_at_renewal` | Checkbox | True if user has requested cancellation effective at renewal |
| Latest `invoice.payment_failed` event | `at_risk` | Checkbox | Set to true on payment failure; cleared on successful payment |
| `subscription.trial_end` | `trial_end_date` | Date | When the trial expires; triggers trial-end workflow |

### Invoice-level properties (Stripe Invoice → HubSpot Activity)

- On `invoice.paid`: log a note on the deal with invoice amount, date, and Stripe invoice ID.
- On `invoice.payment_failed`: set `at_risk: true` on the deal and create a HubSpot task: "Follow up on failed payment within 24 hours."

## MRR calculation

- **Monthly plan**: `unit_amount / 100` directly.
- **Annual plan**: `unit_amount / (100 * 12)` for the monthly equivalent.
- **Multi-seat plans**: `unit_amount * quantity / 100` (monthly equivalent).

Store MRR as a USD amount in HubSpot regardless of the customer's billing currency. Currency conversion uses the Stripe invoice's exchange rate at the time of payment.

## Deduplication

Match Stripe customers to HubSpot contacts by email address (primary key). If a match is found, update the existing contact. If no match is found, create a new contact with the Stripe customer data and flag it for AE review (the customer may have signed up through a back-channel not tracked in HubSpot).

## Failure handling

- If a HubSpot API call fails during a sync, log the failure and enqueue for retry.
- After 3 retries, escalate to the ops Slack channel `#crm-sync-alerts`.
- The daily reconciliation job is the backstop — it resolves any events that were missed by failed webhook deliveries.

## Pair with

[[ops-hubspot-deal-stage-router]] updates deal stages based on product events; this skill keeps the financial properties of those deals current. The two skills together give AEs and CSMs a complete picture: where the customer is in their lifecycle (stage router) and what they are worth and whether they are at risk (property mapper).

## Related skills

- [[ops-hubspot-deal-stage-router]] — deal stage transitions that run alongside this property sync
- [[ops-subscription-erd-validator]] — validates the underlying data model for consistency
- [[ops-churn-risk-detector]] — uses `at_risk` and `subscription_status` as churn signals
