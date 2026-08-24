---
name: connector-hubspot-crm
description: Use when the legal-AI platform needs to read or write CRM data in HubSpot — including logging chat-captured leads, updating deal stages based on subscription lifecycle events, segmenting contacts for marketing campaigns, or triggering sales-to-human handoffs. Covers the full lead-to-deal flow from chat capture through trial conversion and churn monitoring. P0 connector for platform revenue operations. Triggers on any sales, marketing, or customer-success workflow that requires CRM state.
license: MIT
metadata: " id: connector.hubspot-CRM category: connector priority: P0 intent: [__connector__] related: [connector-stripe, connector-linear, connector-gmail, connector-posthog] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'connector'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Connector — HubSpot CRM

## What it does

HubSpot is the CRM platform used for sales pipeline management, marketing automation, and customer-success tracking for the legal-AI product. This connector is the integration layer between the AI assistant, the product's subscription lifecycle, and the sales/marketing team's HubSpot workspace.

The connector serves three user groups:
- **Sales team:** lead capture from chat, deal stage updates, enterprise-inquiry routing.
- **Marketing team:** contact segmentation, campaign list management, email automation triggers.
- **Customer success:** trial conversion monitoring, churn risk alerts, onboarding tracking.

This is a **P0 connector** — it is on the critical path for revenue operations.

## Setup / auth

Each tenant has their own HubSpot organization — **no cross-tenant data sharing**.

Authentication uses **HubSpot Private App tokens** (preferred over legacy API keys):
1. Create a Private App in HubSpot Settings → Integrations → Private Apps.
2. Grant only the required CRM scopes (see below).
3. Store the token in the platform's secrets manager, scoped to the tenant.
4. Rotate tokens annually or upon any personnel change affecting the CRM admin.

### Required scopes

| CRM function | HubSpot scope |
|---|---|
| Read contacts and companies | `crm.objects.contacts.read`, `crm.objects.companies.read` |
| Write contacts and companies | `crm.objects.contacts.write`, `crm.objects.companies.write` |
| Read deals | `crm.objects.deals.read` |
| Write deals | `crm.objects.deals.write` |
| Marketing lists | `crm.lists.read`, `crm.lists.write` |
| Email sends | `marketing-email` |
| Activity logging | `timeline` |

Request only the scopes in use. Do not grant `settings.users.write` or `account-info.security.read` to an automated integration.

## Capabilities

### Contact and company management

- Create or update contact records from chat-captured lead data.
- Sync company records from Stripe customer data (see property mapping below).
- Merge duplicate contacts identified during ingestion.
- Log custom timeline events (e.g., "Trial started via chat," "Upgrade prompted by AI").

### Deal stage management

The platform's deal pipeline mirrors the subscription lifecycle:

| Pipeline stage | Trigger |
|---|---|
| New Lead | Contact captured in chat with email provided |
| Trial Active | Stripe subscription started (free or paid trial) |
| Trial Converting | User visits billing page or asks about paid features |
| Closed Won | Stripe subscription `status: active` (paid) |
| At Risk | PostHog churn score > 70 OR no login in 21 days |
| Churned | Stripe subscription canceled |

Deal stages are updated by webhook (see Webhooks section) — not by polling.

### Property mapping — Stripe → HubSpot sync

| Stripe data | HubSpot property | Object |
|---|---|---|
| `customer.id` | `stripe_customer_id` (custom) | Company |
| `subscription.status` | `deal_stage` | Deal |
| `price.lookup_key` | `plan_tier` (custom) | Company / Contact |
| `subscription.current_period_end` | `subscription_renewal_date` (custom) | Deal |
| `invoice.paid` date | `last_payment_date` (custom) | Company |

Sync runs on each Stripe webhook event. A full reconciliation job runs nightly.

### Marketing automation

- Segment contacts by lifecycle stage, plan tier, practice area (from onboarding survey), and jurisdiction.
- Trigger automated email sequences based on segment membership:
  - Trial welcome sequence (Days 0, 3, 7, 14).
  - Trial-to-paid conversion nudge (Day 12 of trial).
  - Post-upgrade onboarding sequence.
  - Churn-risk re-engagement (triggered by At Risk stage).
- All sequences authored by the marketing team in HubSpot; the connector triggers entry, does not author content.

### Human handoff triggers

When the AI assistant identifies a signal requiring a human response, it creates a HubSpot task or deal note:

| Signal | Handoff destination | HubSpot action |
|---|---|---|
| Enterprise interest ("we have 50 lawyers") | Sales team | Create deal; assign to AE; notify via Slack (via HubSpot workflow) |
| Demo request | Sales team | Create meeting task; assign to AE |
| Partnership inquiry | BD team | Create contact + deal; tag "Partnership" |
| Bug report (billing-level) | Support | Create support ticket in HubSpot Service Hub |
| Churn risk verbal signal | CS team | Update deal stage to "At Risk"; create follow-up task |

## Webhooks

HubSpot webhooks are the primary mechanism for keeping platform state in sync with CRM state. Subscribe to:

- `contact.creation` — new contact created in HubSpot (e.g., by a form or direct sales entry).
- `deal.stageChange` — deal moved between pipeline stages.
- `contact.propertyChange` on `lifecyclestage` — contact promoted through lifecycle.

Stripe webhooks update HubSpot (not the reverse). HubSpot is the system of record for CRM data; Stripe is the system of record for billing.

## Critical security requirements

### Tenant isolation

Each legal-AI tenant connects to their own HubSpot organization:
- No cross-tenant contact or deal records.
- The platform must enforce tenant scoping at the API request level — never derive the HubSpot org ID from user input alone.
- Cross-tenant data leakage is a Category 1 security incident requiring immediate response.

### Audit logs

Every HubSpot write operation (contact creation, deal update, property change) is logged:
- Actor: user ID or service account ID.
- Timestamp (UTC).
- Operation: create / update / delete.
- Object type and ID.
- Before / after values for property changes.

Sales rep access to HubSpot via the platform is logged. Direct HubSpot UI access is subject to HubSpot's own audit logs.

### No PII in custom timeline events

Timeline event descriptions are searchable and may be seen by multiple team members. Do not include client matter details, privileged content, or sensitive PII in timeline event text.

## Failure modes

| Failure | Cause | Resolution |
|---|---|---|
| Duplicate contact | Same email from multiple sources | Implement deduplication check before create; use HubSpot dedup API |
| Deal stage out of sync | Stripe webhook missed | Nightly reconciliation catches gaps; implement dead-letter queue for webhooks |
| Rate limit (100 requests/10s) | Burst of signups | Queue write operations; implement exponential backoff |
| HubSpot API `409 Conflict` | Concurrent writes to the same contact | Last-write wins for non-critical fields; alert for critical fields (plan tier) |

## Related skills

- [[connector-stripe]]
- [[connector-linear]]
- [[connector-gmail]]
- [[connector-posthog]]
