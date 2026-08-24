---
name: ops-ad-budget-vs-bug-rate-circuit-breaker
description: Use when paid acquisition spend needs to be automatically paused because product quality metrics have degraded beyond acceptable thresholds. Monitors bug rate, hallucination rate, open P0/P1 incidents, churn spikes, and rolling NPS to trigger an ad spend freeze across Google, Meta, LinkedIn, Twitter/X, and Reddit — preventing marketing dollars from being burned while the product is in a quality crisis.
license: MIT
metadata: " id: ops.ad-budget-vs-bug-rate-circuit-breaker category: ops jurisdictions: [__multi__] priority: P2 intent: [ops, growth, ad-budget, circuit-breaker, quality-gate] related: [ops-churn-risk-detector, ops-bug-report-collector, ops-nps-collector-in-chat, ops-credit-burn-rate-watcher] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'ops'.
Registered as a flat plugin skill.
-->


# Ad Budget vs Bug-Rate Circuit Breaker

## Purpose

Paid user acquisition is only valuable if the users acquired have a good first experience. When the product is experiencing elevated bug rates, open incidents, churn spikes, or declining satisfaction, spending money to bring in new users accelerates damage rather than growth.

This skill defines a circuit breaker: an automated system that pauses all paid acquisition channels when quality signals drop below defined thresholds, and requires manual re-enable after an explicit quality sign-off.

## Trigger conditions

The circuit breaker trips when **any one** of the following conditions is met:

| Signal | Threshold | Notes |
|--------|-----------|-------|
| Bug rate / hallucination rate | Above defined baseline for >2h | As measured in production, not just lab eval |
| Open P0 or P1 incident | Unresolved for >24 hours | P0 = outage or data loss; P1 = major feature broken |
| Churn spike | >2 standard deviations above rolling baseline | 7-day rolling window |
| NPS rolling average | Drops >10 points vs prior 7-day average | Calculated from in-chat NPS collector |
| Error rate spike | >3× baseline for >30 minutes | Server 5xx or LLM provider failures |

These are OR conditions — any single trigger is sufficient to pause spend. The system should not wait for multiple signals to align.

## Channels covered

The circuit breaker pauses spend across all active paid acquisition channels:

- Google Ads (Search campaigns + Display/Retargeting)
- Meta Ads (Facebook + Instagram)
- LinkedIn Campaign Manager
- Twitter/X Promoted
- Reddit Promoted Posts

For each channel, the pause action is:
1. Set campaign status to "Paused" via the channel's API.
2. Log the pause event with: timestamp, trigger signal, signal value, campaign IDs paused.
3. Post a notification to the `#growth-ops` Slack channel with a brief summary.

## Re-enable process

Re-enabling spend is **manual and gated**. The system does not auto-resume.

Required before re-enabling:
1. **Incident closed**: the triggering P0/P1 incident must be marked resolved in Linear with an owner-confirmed resolution.
2. **Post-incident summary**: a brief write-up (what failed, what fixed, what prevented recurrence) must be linked in the re-enable approval.
3. **Quality signal recovery**: the triggering metric must have returned to within 1 standard deviation of baseline for at least 2 hours.
4. **Manual approval**: the growth lead (or a designated deputy) must explicitly approve re-enable in the ops dashboard.

Do not re-enable spend until all four conditions are satisfied.

## What this prevents

HAQQ's beta experience demonstrated that running paid acquisition during a product quality crisis has compounding costs:
- New users acquired during a bug period have materially higher early churn.
- Negative first impressions are disproportionately shared (review sites, social media).
- Customer success and support load spikes exactly when engineering is already stretched.
- Marketing spend is wasted because conversion funnel metrics from a crisis period corrupt attribution models.

The circuit breaker prevents all of these by making the cost of quality failures immediately visible to the growth team, not just the engineering team.

## Integration points

- **Trigger feeds from**: [[ops-bug-report-collector]] (bug rate), [[ops-nps-collector-in-chat]] (NPS), [[ops-churn-risk-detector]] (churn signal), and the backend error monitoring system.
- **Pause actions go to**: each channel's API (Google Ads API, Meta Marketing API, LinkedIn API, etc.).
- **Notifications go to**: Slack `#growth-ops` + email to growth lead.
- **Re-enable approval lives in**: ops dashboard (Linear ticket or dedicated ops UI).

## Configuration

The thresholds above are defaults; they should be tuned per product maturity stage:
- Early beta: tighter thresholds (any P0 trips the breaker immediately; churn threshold is 1.5σ).
- Growth stage: defaults as above.
- Mature product with strong baselines: thresholds can be relaxed for well-understood transient events (e.g., a known third-party API degradation with active mitigation).

## Related skills

- [[ops-churn-risk-detector]] — provides the churn signal that feeds this breaker
- [[ops-bug-report-collector]] — collects and classifies bugs that raise the bug-rate signal
- [[ops-nps-collector-in-chat]] — provides the NPS signal
- [[ops-credit-burn-rate-watcher]] — related ops monitoring skill
