---
name: ops-posthog-cohort-builder
description: Use when building user cohorts in PostHog for segmentation, A/B test targeting, feature rollout audiences, retention analysis, or email campaign segmentation. Defines canonical cohort definitions (activation, retention, persona, tier, feature usage) for a legal AI product, with rules for tenant boundary enforcement and PII handling in cohort queries.
license: MIT
metadata: " id: ops.posthog-cohort-builder category: ops priority: P1 intent: [ops, posthog, cohort, segmentation, analytics] related: [ops-posthog-funnel-debugger, ops-feature-flag-experiment-launcher, ops-churn-risk-detector] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'ops'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Ops — PostHog Cohort Builder

## Purpose

Cohorts are the foundation of product analytics in a legal AI platform. Without well-defined, consistently applied cohorts, A/B test results are unreliable, retention curves are noisy, and feature rollouts reach the wrong users. This skill defines the canonical cohort library and the rules for building, maintaining, and querying them safely.

## Canonical cohort definitions

### Activation cohorts

| Cohort name | Criteria | Use case |
|-------------|----------|---------|
| New users | Account created in last 7 days | Onboarding funnel analysis |
| Activated users | Completed at least 1 substantive prompt (not just signed up and browsed) | Activation rate measurement |
| Power users | 5+ sessions per week for the last 4 weeks | Feature rollout first audience; NPS benchmark |
| Churned-activated | Activated but no session in last 30 days | Win-back targeting |

A "substantive prompt" is defined as a user message that resulted in a draft, a document analysis, or a research response — not a greeting, a settings change, or a navigation event.

### Retention cohorts

| Cohort name | Criteria | Use case |
|-------------|----------|---------|
| Week-1 retained | Signed up >7 days ago; had at least 1 session in last 7 days | Day-7 retention metric |
| Month-1 retained | Signed up >28 days ago; active in last 28 days | Month-1 retention |
| Month-3 retained | Signed up >84 days ago; active in last 30 days | Long-term retention |
| Dormant | No session in last 30 days; was previously active | Re-engagement campaign targeting |
| Resurrected | Dormant for >30 days; then had a session in last 7 days | Resurrection rate metric |

### Persona cohorts

| Cohort name | Criteria | Notes |
|-------------|----------|-------|
| Lawyers (private practice) | Email domain matches known law firm pattern or user declared role | Broadest professional cohort |
| In-house counsel | Corporate domain + role indicator in profile | Often on Business tier |
| Law students | `.edu` domain or declared student role | Typically on Free tier |
| Consumers | Personal email domain (gmail, hotmail, yahoo, etc.) + no professional role indicator | Consumer product experience |
| Enterprise admin | Account has team members + admin role flag | Relevant for team feature rollouts |

Note: persona inference from email domain is approximate. Encourage users to declare their role in onboarding for higher accuracy.

### Tier cohorts

| Cohort name | Criteria |
|-------------|----------|
| Free tier | No active Stripe subscription, or on `free` plan |
| Starter | Active Stripe subscription on `starter` plan |
| Pro | Active Stripe subscription on `pro` plan |
| Business | Active Stripe subscription on `business` plan |
| Enterprise | Active Stripe subscription on `enterprise` plan |
| BYO-key users | Free tier + has configured a custom API key |
| Trial | Active Stripe trial (trial_end is in the future) |

### Feature usage cohorts

| Cohort name | Criteria | Use case |
|-------------|----------|---------|
| Heavy doc workspace users | 5+ document workspace sessions per week | Target for collaboration feature rollout |
| Skills observability users | Has opened the skills observability tab at least once | Target for observability feature announcements |
| Drafting board users | Has had at least 1 drafting board session | Drafting feature experiment audience |
| Multi-jurisdiction users | Has used more than 2 different jurisdiction contexts | Target for jurisdiction-specific feature rollouts |
| Deep-research users | Has triggered deep-research skill at least 3 times | Power users; target for research feature improvements |

## Cohort use cases

- **A/B testing**: use persona + tier cohorts to ensure experiments are measured on the right population.
- **Feature rollouts**: start with power users, then activated, then all.
- **Push / email campaigns**: use dormant or churned-activated for re-engagement; use retained + high-NPS for testimonial asks.
- **Retention analysis**: run retention curves on the Week-1 and Month-1 retained cohorts segmented by persona and tier.
- **Churn deep-dive**: compare feature breadth (from feature usage cohorts) between churned and retained users.

## Building a cohort in PostHog

1. Navigate to **Cohorts** → **New Cohort**.
2. Name the cohort using the canonical name from the table above (consistency is important for cross-team communication).
3. Define the filter criteria using PostHog's behavioral filter builder.
4. Set the cohort to **dynamic** (recalculates daily) unless you need a static snapshot for a specific experiment.
5. Add a description explaining the criteria in plain English (not just the filter expression).
6. Document the version date if the definition has changed — cohort definitions should be version-tracked.

## Critical rules

### Tenant boundaries
Cohort queries must always include a tenant filter if the product is multi-tenant. Never build a cohort that inadvertently mixes users from different tenants — this is both a privacy issue and a data quality issue.

### PII compliance
- PostHog person properties should not store raw PII (full name, email). Use anonymized IDs.
- If email domain is used as a cohort criterion, store only the domain, not the full address.
- Cohort membership lists exported from PostHog must be handled under the same data handling rules as any other personal data export.

### Cohort overlap
When using cohorts for A/B tests, check for overlap between your target cohort and any cohort that is already enrolled in another running experiment. Overlapping experiments produce unreliable results.

### Definition documentation
Every cohort must have a written definition (the criteria in plain English, not just the PostHog filter). Store these definitions in the product wiki alongside the cohort's PostHog URL.

## Related skills

- [[ops-posthog-funnel-debugger]] — use cohorts to segment funnel analysis
- [[ops-feature-flag-experiment-launcher]] — cohorts define the experiment audience
- [[ops-churn-risk-detector]] — churn model is validated against the dormant and churned-activated cohorts
