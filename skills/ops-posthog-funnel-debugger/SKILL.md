---
name: ops-posthog-funnel-debugger
description: Use when analysing conversion drop-off in a defined product funnel (signup → first chat → first draft → first save → upgrade) using PostHog. Produces step-by-step conversion percentages, median time-to-step, cohort-segmented drop-off reasons, path analysis between steps, and three ranked hypotheses for the biggest leak — each paired with an actionable experiment recommendation.
license: MIT
metadata: " id: ops.posthog-funnel-debugger category: ops jurisdictions: [__multi__] priority: P2 intent: [posthog, ops, funnel, conversion, drop-off] related: [ops-feature-flag-experiment-launcher, ops-posthog-cohort-builder, ops-churn-risk-detector] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'ops'.
Registered as a flat plugin skill.
-->


# Ops — PostHog Funnel Debugger

## Purpose

A funnel analysis tells you where users are dropping off. A funnel *debugger* tells you *why*, and what to do about it. This skill wraps PostHog funnel analysis with a structured diagnostic methodology — segmenting drop-off by cohort, exploring user paths between steps, and generating concrete experiment hypotheses ranked by expected impact.

## When to use this

Use this skill when:
- Conversion rate at a key funnel step has declined ≥10% week-over-week or month-over-month.
- A new feature was released and you want to understand its impact on the conversion funnel.
- You are preparing an experiment hypothesis and need data to confirm the problem exists.
- A stakeholder asks "where are users getting stuck?"

## Canonical legal AI funnel

The default funnel for a legal AI product:

```
Step 1: Signup (account created)
Step 2: First substantive prompt sent
Step 3: First draft saved (or first document analysis completed)
Step 4: Matter created (user organizes work into a matter)
Step 5: Upgrade to paid plan
```

Adjust steps based on the specific product flow — this is a starting template.

## Analysis steps

### 1. Run the funnel in PostHog

Configure the PostHog funnel with:
- **Conversion window**: 14 days (allow enough time for deliberate users)
- **Counting method**: unique users (not events)
- **Date range**: last 30 days (or align with the change you're investigating)
- **Breakdown**: by the relevant cohort dimension (persona, tier, acquisition channel)

### 2. Extract step-by-step conversion

For each step transition, record:
- Conversion rate (% of users who proceeded from step N to step N+1)
- Absolute number of users (don't let a high % mask a small absolute number)
- Median time from step N to step N+1

This produces a table like:

| Transition | Conversion | Median time to step |
|------------|-----------|---------------------|
| Signup → First prompt | 68% | 2 hours |
| First prompt → First draft saved | 41% | 1 day |
| First draft → Matter created | 52% | 3 days |
| Matter created → Upgrade | 18% | 12 days |

### 3. Segment drop-off

For the step with the worst conversion rate, compare cohorts:
- Lawyer vs consumer — does one persona drop off more?
- Acquisition channel — do users from LinkedIn convert differently than organic?
- Plan tier — do trial users behave differently than free direct signups?
- Time of signup — did a recent cohort perform worse (suggesting a product change broke something)?

### 4. Path analysis between steps

For users who dropped off at the worst step, use PostHog's path analysis to see what they did instead of proceeding:
- Did they navigate to the settings page? (confusion about the product)
- Did they trigger an error event? (bug preventing conversion)
- Did they come back the next day and convert? (delay, not abandonment)
- Did they exit the app immediately? (activation failure)

### 5. Generate three hypotheses

Based on the conversion data, segmentation, and path analysis, generate exactly three ranked hypotheses for the largest drop-off point:

Format each hypothesis as:
- **Problem**: What behaviour is causing the drop-off?
- **Evidence**: What data supports this?
- **Experiment**: What would we change to test this?
- **Expected impact**: How much could conversion improve?

Example:
> **Hypothesis 1 — Friction at the first draft step**
> **Problem**: Users are typing long prompts but abandoning before saving a draft.
> **Evidence**: Median time at step 3 is 3 hours; path analysis shows 40% of dropoffs go to the error page.
> **Experiment**: Fix the PDF upload error affecting users who try to draft from an uploaded document.
> **Expected impact**: +8–12% conversion at step 3.

### 6. Recommend experiments

For the top hypothesis, link to [[ops-feature-flag-experiment-launcher]] with:
- A drafted hypothesis statement
- The primary metric (conversion rate at the drop-off step)
- Two guardrail metrics
- The cohort to test on

## Output format

Deliver the funnel debug as a brief structured report:
1. Funnel table (step-by-step conversion + median time)
2. Worst-performing step identified
3. Segmentation breakdown for that step
4. Path analysis summary (top 3 paths for dropoffs)
5. Three hypotheses (ranked by expected impact)
6. Recommended experiment for the top hypothesis

## Related skills

- [[ops-feature-flag-experiment-launcher]] — execute the experiment recommended by this analysis
- [[ops-posthog-cohort-builder]] — build the cohort breakdowns used in the funnel segmentation
- [[ops-churn-risk-detector]] — funnel dropoffs at the upgrade step feed the churn risk model
