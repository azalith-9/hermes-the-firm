---
name: ops-hubspot-deal-stage-router
description: Use when mapping in-product user lifecycle events to HubSpot deal stages and triggering downstream CRM workflows. Translates key product milestones (signup, first draft, first matter file, 30-day active, upgrade, cancel) into HubSpot deal stage transitions and fires the corresponding sequences — AE assignment on SQL, onboarding email on Closed-Won, win-back campaign on Closed-Lost.
license: MIT
metadata: " id: ops.hubspot-deal-stage-router category: ops jurisdictions: [__multi__] priority: P2 intent: [hubspot, ops, crm, deal-stage, lifecycle] related: [ops-hubspot-property-mapper-stripe-sync, ops-churn-risk-detector, ops-nps-collector-in-chat] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'ops'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Ops — HubSpot Deal Stage Router

## Purpose

The product generates events that directly map to sales pipeline stages. Without an automated bridge from product events to HubSpot, the CRM lags reality — AEs don't know a user is ready to close, CSMs miss churn signals, and win-back campaigns fire at the wrong time. This skill defines the canonical event → deal stage mapping and the workflows each transition triggers.

## Event-to-stage mapping

| Product event | HubSpot deal stage | Notes |
|---------------|--------------------|-------|
| User creates account | "Trial Start" | All new signups, including BYO-key users |
| First successful contract draft (draft saved or exported) | "Demo Complete" | Confirms the user has experienced the core value prop |
| First matter file uploaded to the workspace | "POC Active" | Signals intent to use for real work, not just exploration |
| Account has 30+ days active with ≥3 sessions/week | "Sales-Qualified Lead (SQL)" | Engagement threshold that signals genuine adoption |
| User upgrades from free/trial to any paid plan | "Closed-Won" | Also fires on first invoice paid, as fallback |
| User cancels subscription or downgrades to free | "Closed-Lost" | Also fires on chargeback or involuntary churn |

**Direction of travel**: stages generally flow forward. A user who goes from Closed-Won back to Closed-Lost (cancels a paid subscription) creates a new deal record rather than updating the original — this preserves win history.

## Workflow triggers per stage transition

### SQL → AE Assignment
When a deal moves to "Sales-Qualified Lead":
- Assign the deal to the account executive (AE) based on the routing rules (geography, firm size, practice area specialization).
- Create a HubSpot task for the AE: "Reach out within 48 hours."
- Send AE a Slack notification: "New SQL: [Firm Name], [Usage stats], [Contact email]."

### Closed-Won → Onboarding Sequence
When a deal moves to "Closed-Won":
- Enroll the contact in the onboarding email sequence (5-email sequence over 14 days).
- Assign a CSM (if Business/Enterprise tier).
- Create a HubSpot task for CSM: "Welcome call within 7 days."

### Closed-Lost → Win-Back Sequence
When a deal moves to "Closed-Lost":
- Wait 90 days.
- Enroll the contact in the win-back sequence (3-email sequence over 14 days).
- Win-back emails should reference what the user accomplished during their time in the product, not generic reactivation copy.
- If the user re-engages (opens emails, clicks), escalate to AE for personal outreach.

## Implementation

Each product event fires a webhook to the HubSpot API:

```json
{
  "event": "first_contract_draft",
  "userId": "<HubSpot contact ID>",
  "timestamp": "<ISO 8601>",
  "metadata": {
    "documentType": "NDA",
    "jurisdiction": "UAE"
  }
}
```

A HubSpot workflow (or a middleware layer) receives the webhook and:
1. Finds or creates the HubSpot deal for the user.
2. Updates the deal stage to the mapped value.
3. Fires the appropriate workflow (email sequence, task creation, Slack notification).

## Edge cases

- **BYO-key users**: they do not have a Stripe subscription. Their deal stages stop at "SQL" until they upgrade to a managed plan. Flag them in HubSpot with a `byo_key: true` property.
- **Enterprise deals (negotiated contracts)**: deal stages are managed manually by the AE; product events are supplementary signals, not authoritative stage drivers.
- **Team accounts**: the deal is linked to the account admin (billing contact), not to individual team members. Individual user events bubble up to the account-level deal.
- **Multiple products or tiers**: if a firm has both a Pro individual and a Business team seat, they may have multiple deals. The router creates separate deals per subscription, not per contact.

## Pair with

[[ops-hubspot-property-mapper-stripe-sync]] ensures that billing data (MRR, renewal date, plan name) is also reflected in HubSpot so AEs and CSMs have a complete picture.

## Related skills

- [[ops-hubspot-property-mapper-stripe-sync]] — keeps billing properties in sync alongside stage transitions
- [[ops-churn-risk-detector]] — provides the churn signal that drives the Closed-Lost transition
- [[ops-nps-collector-in-chat]] — NPS promoters are strong signals for SQL and Closed-Won transitions
