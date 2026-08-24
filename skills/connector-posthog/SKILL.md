---
name: connector-posthog
description: Use when the legal-AI product team needs to query product analytics data from PostHog — including usage dashboards, feature adoption metrics, user retention, funnel analysis, and churn risk scoring — to inform product decisions or trigger customer-success workflows. Requires a per-tenant PostHog API key. Triggers on requests for product usage data, churn signals, feature engagement metrics, or any data needed to understand how users interact with the legal-AI platform.
license: MIT
metadata: " id: connector.posthog category: connector jurisdictions: [__multi__] priority: P2 intent: [__connector__] related: [connector-hubspot-crm, connector-stripe, connector-linear, connector-scheduled-tasks] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'connector'.
Registered as a flat plugin skill.
-->


# Connector — PostHog

## What it does

PostHog is the product analytics and session-recording platform used by the legal-AI team. The PostHog connector enables the AI assistant to query analytics data programmatically — surfacing usage metrics, tracking feature adoption, identifying churn signals, and feeding behavioural data into the platform's customer-success and growth workflows.

This is an **internal product-operations tool**. It is not used for legal content generation — it is used to understand how users (lawyers and legal-ops teams) interact with the legal-AI product.

## Setup / auth

Authentication uses a **per-tenant PostHog API key**:

- Project API Key: used for event ingestion (client-side tracking); do NOT use this key for server-side queries.
- Personal API Key: used for server-side data retrieval (Insights API, session recordings); this is what the connector uses.
- Stored in the platform's secrets manager per tenant.
- Rate limit: 240 requests/minute (standard PostHog Cloud plan).

The platform operates in a single PostHog project for HAQQ's own analytics. Tenants do not get their own PostHog projects — usage data is scoped at the user/organization level within the single project.

## Capabilities

| Capability | API | Notes |
|---|---|---|
| Query trends (event counts over time) | `Insights` API | Feature usage, skill invocation counts |
| Funnels (conversion analysis) | `Insights` API | Trial → paid conversion; onboarding completion |
| Retention analysis | `Insights` API | Weekly/monthly active users by cohort |
| Persons (individual user profiles) | `Persons` API | Usage history per user; PII — handle carefully |
| Session recordings | `Session Recordings` API | Qualitative usage signals |
| Feature flags (status) | `Feature Flags` API | Which features are enabled per user/group |
| Cohort definition and query | `Cohorts` API | "Users who invoked NDA skill ≥3 times in 30 days" |
| SQL queries (PostHog ClickHouse SQL) | `Query` API | Flexible ad-hoc analytics |

## Key analytics use cases

### Usage dashboards

Track daily/weekly/monthly active users, segmented by:
- Plan tier (free, starter, pro, business).
- Practice area (as captured in onboarding survey).
- Jurisdiction (where users identified their primary jurisdiction).
- Skill invocation frequency (which skills are used most).

This data informs the product roadmap and skill prioritization.

### Churn risk detection

A user is flagged as churn risk when:
- No login event in the past 21 days (active subscription).
- Skill invocation count dropped >50% week-over-week.
- User raised a support complaint in the last 30 days without a resolution logged.
- Plan tier is Pro or Business (high-value users trigger lower threshold).

Churn risk scores feed into [[connector-hubspot-crm]] to trigger CS team follow-up workflows.

### Feature adoption tracking

For each new skill or feature shipped:
- Define a "first use" event (e.g., `skill_invoked` with `skill_id = "draft-nda-bilateral"`).
- Track adoption rate: what % of active users have used it in the first 30 days.
- Segment by persona and plan tier.

Low adoption in a specific segment suggests a discovery or UX problem — surface to [[connector-linear]] as a product issue.

### Conversion funnel

Key funnel for the business:
1. **Signup** (account created).
2. **Onboarding complete** (first skill invoked).
3. **Engaged** (5+ skill invocations in first 7 days).
4. **Trial converted** (Stripe subscription moved to paid).
5. **Retained** (active at Day 30).

Funnel data is queried weekly and fed into the marketing team's growth reporting.

### Session recording review

For qualitative product research, the PM can review session recordings of users interacting with specific flows (e.g., the NDA generator). PostHog masks PII in session recordings — ensure masking is configured correctly before recordings are reviewed by non-engineering staff.

## Privacy and data handling

- **No legal document content is tracked.** PostHog receives event metadata (skill invoked, UI element clicked, session duration) — never the content of documents generated or reviewed.
- **PII minimization.** User email is stored in PostHog as a person property but should not appear in event properties. Use opaque user IDs in events.
- **Session recording masking.** All form inputs on pages that may contain client information must be masked in PostHog recording configuration.
- **GDPR.** PostHog data for EU users is subject to GDPR. The platform's privacy policy must disclose product analytics and provide an opt-out mechanism.
- **KSA/UAE data residency.** If applicable regulations require data residency in the region, evaluate PostHog EU vs US hosting or a self-hosted deployment.

## Failure modes

| Failure | Cause | Resolution |
|---|---|---|
| `401 Unauthorized` | API key incorrect or expired | Rotate key; update in secrets manager |
| Insight query timeout | Complex query over large dataset | Narrow date range; use sampling; escalate to PostHog support |
| Missing event data | Tracking event not firing (client-side bug) | Check browser console; review PostHog event list; file [[connector-linear]] bug |
| Feature flag stale | Flag not re-evaluated after property change | Trigger flag refresh; check flag evaluation logs |

## Related skills

- [[connector-hubspot-crm]]
- [[connector-stripe]]
- [[connector-linear]]
- [[connector-scheduled-tasks]]
