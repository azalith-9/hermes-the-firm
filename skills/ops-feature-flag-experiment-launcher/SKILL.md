---
name: ops-feature-flag-experiment-launcher
description: Use when launching a product experiment in a legal AI platform with a defined hypothesis, metric, and cohort. Guides through defining primary and guardrail metrics, calculating required sample size, creating the feature flag in PostHog or LaunchDarkly, wiring event tracking, and configuring an automatic stop-loss to revert the experiment if guardrail metrics degrade.
license: MIT
metadata: " id: ops.feature-flag-experiment-launcher category: ops jurisdictions: [__multi__] priority: P2 intent: [feature-flag, experiment, a-b-test, posthog, launchdarkly] related: [ops-posthog-funnel-debugger, ops-posthog-cohort-builder, ops-feature-request-collector] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'ops'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Ops — Feature Flag Experiment Launcher

## Purpose

Product experiments in a legal AI platform require more rigour than in a typical consumer app — a bad experiment that changes how legal documents are drafted or reviewed can directly harm professional users. This skill defines the end-to-end process for launching a controlled experiment, from hypothesis to automatic stop-loss, ensuring quality guardrails are in place before any rollout.

## Inputs required

Before launching, the following must be defined:

| Input | Example |
|-------|---------|
| Hypothesis | "Showing a jurisdiction-aware template picker before the user starts drafting will increase first-draft completion rate by 15%." |
| Primary metric | First-draft completion rate (% of sessions where a draft is saved) |
| Guardrail metrics (2) | User satisfaction score (NPS) must not drop; P1 bug rate must not increase |
| Cohort definition | % rollout / specific segment / opt-in |
| Duration | Minimum run time (typically 14 days for legal users; see sample size calculation) |
| Stop-loss threshold | Auto-revert if any guardrail drops >10% relative to control |

## Step-by-step launch process

### 1. Define metrics

**Primary metric**: one metric that directly measures whether the hypothesis is true. It must be:
- Measurable in PostHog or the analytics platform as an existing event.
- Attributable to the experiment (users in the variant, not all users).
- Sensitive enough to detect the expected effect size within the experiment duration.

**Guardrail metrics (exactly 2)**: metrics that should not degrade. Common legal AI guardrails:
- User satisfaction (NPS or in-session thumbs-down rate)
- Error rate or hallucination report rate
- Session abandonment rate
- P0/P1 bug report rate

### 2. Define cohort and rollout

| Cohort type | When to use |
|-------------|-------------|
| Percentage rollout (e.g., 50/50 split) | Default for most experiments |
| Segment-based | When the feature only applies to a user type (e.g., lawyer tier only) |
| Opt-in beta | For high-risk features where voluntary early adopters are preferred |
| Holdout group | When measuring long-term effect across a full billing cycle |

For legal AI experiments, avoid 100% rollout without a holdout — you need a baseline to measure against.

### 3. Calculate sample size

Use a power analysis:
- Desired statistical power: 80% (standard)
- Significance level: α = 0.05
- Expected effect size: from the hypothesis (e.g., +15% on a 40% baseline completion rate)

The required sample size determines the minimum experiment duration. For legal AI user bases (typically smaller than consumer apps), 14–30 days is typical for well-trafficked features.

### 4. Create the flag

In PostHog:
```
Feature flag name: experiment/<hypothesis-slug>  (e.g., experiment/jurisdiction-template-picker)
Rollout: 50% of [cohort]
Variants: control | treatment
```

In LaunchDarkly:
```
Flag key: exp-jurisdiction-template-picker
Targeting: 50% split on user key
Environments: production only (not staging)
```

### 5. Wire tracking

For every flag variant, ensure the following events are tracked:

- `experiment_enrolled`: fired when a user is bucketed into the experiment.
- `[primary_metric_event]`: the existing event that measures the primary metric.
- `[guardrail_metric_events]`: existing events for guardrail metrics.
- `experiment_exposed`: fired when the user actually sees the variant (not just when they are bucketed).

Verify that the `flag_variant` property is set on all relevant events so PostHog can segment by variant.

### 6. Configure stop-loss

Set an automatic revert rule:
- If any guardrail metric drops >10% relative to control for 48 consecutive hours: pause the experiment and revert the flag to control for all users.
- Notify: post to `#experiments` Slack channel with the metric that triggered the stop-loss.
- No automatic re-launch — requires manual review.

## Output

The launcher produces a brief experiment spec document (stored in Linear or Notion) containing:
- Hypothesis and success definition
- Metric definitions with PostHog/LaunchDarkly event names
- Cohort and rollout configuration
- Sample size and duration
- Stop-loss thresholds
- Flag ID(s) for reference

## Related skills

- [[ops-posthog-funnel-debugger]] — use the funnel analysis to find the experiment candidate before launching
- [[ops-posthog-cohort-builder]] — define the experiment cohort in PostHog
- [[ops-feature-request-collector]] — experiments often originate from feature requests
