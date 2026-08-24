---
name: outreach-userflow-analyzer
description: Use when the legal AI product team needs to analyse user flows within the product to identify drop-off points, conversion blockers, or opportunities for product-led growth. Maps the journey from first visit through onboarding to retained usage, with specific attention to the conversion steps critical for a legal professional audience. Triggers on requests to improve user activation, reduce churn, or understand user behaviour.
license: MIT
metadata: " id: outreach.userflow-analyzer category: outreach intent: ['__outreach__', 'userflow', 'product analytics', 'conversion', 'onboarding'] related: - outreach-growth-agent-runner - outreach-inbox-scan - outreach-haqq-ai-viz priority: P3 source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'outreach'.
Registered as a flat plugin skill.
-->


# Userflow Analyzer

Understanding where legal professionals drop off in the product journey is essential for growth: a legal AI product that loses users at the onboarding step is a product that will not grow through word-of-mouth referrals. This skill maps and analyses the critical user flows, identifies blockers specific to a legal professional audience, and recommends interventions.

## Purpose

Analyse the user journey for a legal AI product to:
1. Identify the highest-drop-off stages in the acquisition → activation → retention funnel
2. Understand the specific friction points for legal professionals (trust, accuracy concerns, workflow integration)
3. Produce a prioritised list of product and messaging interventions
4. Design A/B test hypotheses for the highest-impact improvements

## Inputs

| Input | Description | Required |
|---|---|---|
| Analytics data | Funnel data from PostHog, Mixpanel, GA4, or equivalent | Yes |
| User feedback | Support tickets, interviews, survey responses | Yes |
| Product flows | Screen recordings or user session replays | Helpful |
| Conversion targets | What is the primary activation event? (first legal query answered, first document drafted, first team member invited) | Yes |

## The legal professional user journey

Legal professionals have specific trust and adoption barriers that differ from general SaaS users:

| Stage | What happens | Legal-specific friction |
|---|---|---|
| Acquisition | User discovers product via PR, SEO, referral, or conference | Trust: "Is this built for my jurisdiction?" |
| Landing page | User reads about product | Credibility: no logos/testimonials from known law firms = high bounce |
| Sign-up | Email registration or SSO | Privacy: "Where does my data go?" (client confidentiality concern) |
| Onboarding | First interaction with the product | Competence anxiety: "If AI gives wrong advice, I'm liable" |
| First activation | User asks first legal question or uploads first document | Accuracy check: first output quality determines retention |
| Retained usage | User returns and integrates into workflow | Workflow fit: does it reduce effort or add a step? |
| Advocacy | User refers colleagues or leaves a review | Professional risk: lawyers are cautious about recommending tools |

## Analysis framework

### Step 1 — Map the funnel

Build a quantified funnel:

```
Visitors → Signups → Onboarding completed → First legal query → Return visit → Weekly active → Monthly active
[N]       [N] (X%)  [N] (X%)               [N] (X%)           [N] (X%)      [N] (X%)        [N] (X%)
```

Identify the step with the largest proportional drop-off. This is the highest-priority fix.

### Step 2 — Segment by user type

Legal users are not homogeneous:

| Segment | Typical conversion pattern | Key blocker |
|---|---|---|
| Solo practitioner | High motivation, low tech confidence | Complexity of setup |
| In-house GC team | Approval required before team adoption | Security/data governance concern |
| Law firm associate | Can try independently; needs firm approval for full use | Billability of AI-assisted work |
| Legal operations | Power user; evaluates rigorously | Integration with existing workflows (DocuSign, iManage, etc.) |

Segment conversion metrics separately — aggregate metrics hide the pattern.

### Step 3 — Identify friction by stage

**Acquisition:** are the right users landing? Bounce rate by source, time on page for key pages.

**Sign-up:** form abandonment? Email-only sign-up converts better for legal professionals than social login (Google/LinkedIn can feel non-anonymous for sensitive work).

**Onboarding:** time to first activation event. If > 10 minutes, the onboarding is too long. Legal professionals have no patience for feature tours when they have a document to review.

**First activation:** was the first output accurate? This is the make-or-break moment. Monitor first-query topics and check output quality for the most common first questions.

**Retention:** do users return? Daily/weekly/monthly return rates by cohort. "Sticky" features for legal professionals: multi-jurisdiction comparison, clause library, template generation.

### Step 4 — Prioritise interventions

Score each identified friction point by:
- Impact (number of users affected × severity of drop-off)
- Effort (engineering time to fix)
- Confidence (how certain are we this is the cause?)

Top 3 interventions for most legal AI products at early stage:
1. **Trust signals on landing page**: add firm logos, lawyer testimonials, data privacy statement
2. **Shorter onboarding**: reduce time to first legal answer to < 3 minutes
3. **First-query quality**: ensure the most common first queries (non-compete, NDA, employment) produce excellent output — these are the product's auditions

## Output format

Produce a one-page funnel analysis:

```
## Funnel Summary
[Quantified funnel table]

## Highest Drop-Off: [Stage]
Cause hypothesis: [1–2 sentences]
Evidence: [data + user quotes]
Recommended fix: [concrete product or messaging change]
Expected impact: [% improvement estimate]

## Top 3 Interventions (ranked)
1. [Intervention] — Impact: H/M/L, Effort: H/M/L
2. [Intervention] — Impact: H/M/L, Effort: H/M/L
3. [Intervention] — Impact: H/M/L, Effort: H/M/L

## A/B Test Hypotheses
[2–3 specific tests to run next]
```

## Related skills

- [[outreach-growth-agent-runner]]
- [[outreach-inbox-scan]]
- [[outreach-haqq-ai-viz]]
