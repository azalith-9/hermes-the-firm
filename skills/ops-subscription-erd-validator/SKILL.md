---
name: ops-subscription-erd-validator
description: Use when validating the consistency of the subscription data model in a legal AI SaaS product — specifically the relationships between Stripe customers, users, tenants, subscriptions, plans, feature flags, invoices, and usage records. Flags orphaned records, duplicate active subscriptions, plan/feature-flag mismatches, and proration inconsistencies, and routes findings to the appropriate billing or database owner.
license: MIT
metadata: " id: ops.subscription-erd-validator category: ops jurisdictions: [__multi__] priority: P2 intent: [subscription, ops, billing, data-integrity, stripe] related: [ops-error-classifier, ops-hubspot-property-mapper-stripe-sync, ops-credit-burn-rate-watcher] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'ops'.
Registered as a flat plugin skill.
-->


# Ops — Subscription ERD Validator

## Purpose

The subscription data model is the financial backbone of a SaaS legal AI product. When it has inconsistencies — an orphaned Stripe customer, a user with two active subscriptions, a plan whose feature flags don't match the billing record — the consequences range from free users accessing paid features to paying users being locked out of what they paid for. This skill defines the validation rules and the process for surfacing and resolving inconsistencies.

## Data model overview

The valid subscription ERD (entity-relationship diagram) has these required constraints:

```
Stripe Customer ←→ User: must be 1-to-1 (one Stripe customer per platform user)
Subscription ←→ Tenant: must be 1-to-1 (one active subscription per tenant at a time)
Plan ←→ Feature flags: rules defined in plan config must be consistently applied
Invoice ←→ Usage record: metered usage invoices must match usage logs
```

## Validation checks

The validator runs the following checks:

### 1. Stripe customer ↔ User cardinality

**Check**: Is there exactly one Stripe customer per platform user?

| Violation | Description | Severity |
|-----------|-------------|----------|
| Orphan Stripe customer | A Stripe customer exists with no matching platform user (no `stripe_customer_id` in the users table) | P2 — revenue leak or data residue from deleted account |
| User with no Stripe customer | A user has no Stripe customer record (may be intentional for BYO-key users; verify) | P2 if user should be on managed billing |
| User with multiple Stripe customers | A user has two or more Stripe customer IDs (usually from account merges or import errors) | P1 — billing may be split across records |

### 2. Subscription ↔ Tenant cardinality

**Check**: Does each tenant have exactly one active subscription at any time?

| Violation | Description | Severity |
|-----------|-------------|----------|
| Tenant with multiple active subscriptions | Two or more Stripe subscriptions in `active` status for the same tenant | P1 — double billing; affects feature access logic |
| Active subscription without active tenant | A Stripe subscription is `active` but the platform tenant account is deactivated or deleted | P1 — continued billing with no service delivery |
| Subscription status mismatch | Stripe subscription is `canceled` but platform feature flags still indicate paid access | P1 — free access after cancellation |

### 3. Plan ↔ Feature flag consistency

**Check**: Does the user's plan entitlement match their feature flags in the platform?

- Pull the user's current Stripe plan (`subscription.items.data[0].plan.nickname`).
- Look up the plan definition in the platform config to get the expected feature set.
- Compare to the user's current feature flags in the feature-flag system (PostHog, LaunchDarkly, etc.).

| Violation | Description | Severity |
|-----------|-------------|----------|
| Feature enabled beyond plan | User has a feature flag enabled that their plan does not include | P1 — unintended free access to paid features |
| Feature disabled below plan | User's plan includes a feature but the flag is off | P2 — paying user not getting what they paid for |

### 4. Invoice ↔ Usage consistency

**Check**: For metered billing plans, do the invoice amounts match the usage logs?

- Pull the Stripe invoice for the last billing period.
- Pull the usage records from the platform's usage log for the same period.
- Compare total metered units: does the invoice quantity match the logged usage?

| Violation | Description | Severity |
|-----------|-------------|----------|
| Invoice quantity exceeds logged usage | Stripe is billing for more than the platform logged | P0 — overcharging a customer |
| Invoice quantity below logged usage | Stripe is billing for less than the platform logged | P1 — under-billing (revenue leak) |
| Missing usage records for billed period | Invoice exists but no usage records found | P1 — data integrity issue; cannot verify billing |

### 5. Plan downgrade proration

**Check**: When a user downgrades mid-cycle, is the proration correctly applied?

- Stripe should create a credit note for the unused portion of the higher-tier plan.
- The next invoice should reflect the prorated amount, not the full lower-tier price.
- Verify that the `balance` on the Stripe customer after downgrade matches the expected proration.

## Validation run schedule

- **Daily**: Checks 1 (Stripe customer cardinality) and 2 (subscription cardinality). These are the most likely to catch immediate issues.
- **Weekly**: Check 3 (plan/feature flag consistency). Feature flag drift tends to accumulate slowly.
- **Per billing cycle**: Check 4 (invoice/usage). Run immediately after each billing cycle closes.
- **On-demand**: Triggered by [[ops-error-classifier]] when a schema-integrity error is classified.

## Output

For each violation found, the validator produces:

```json
{
  "violationType": "<string from the check names above>",
  "severity": "P0 | P1 | P2",
  "entityIds": {
    "userId": "<anonymized>",
    "tenantId": "<UUID>",
    "stripeCustomerId": "<Stripe ID>",
    "subscriptionId": "<Stripe sub ID>"
  },
  "description": "<plain-language description of the violation>",
  "suggestedFix": "<string>",
  "autoFixable": true | false
}
```

Auto-fixable violations (e.g., a disabled feature flag for a paying user) can be resolved without manual intervention. Non-auto-fixable violations (e.g., a user with two Stripe customer IDs) require a human decision.

## Related skills

- [[ops-error-classifier]] — triggers this validator when billing-related schema errors are classified
- [[ops-hubspot-property-mapper-stripe-sync]] — the sync layer that can introduce some of these inconsistencies if a webhook is missed
- [[ops-credit-burn-rate-watcher]] — tracks consumption that feeds the usage/invoice validation
