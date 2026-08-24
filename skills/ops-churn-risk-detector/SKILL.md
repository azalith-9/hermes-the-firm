---
name: ops-churn-risk-detector
description: Use when evaluating whether a specific user or account is at elevated risk of cancelling or downgrading. Combines login frequency, session depth, feature breadth, support ticket volume, NPS score, plan history, and explicit churn-signal events into a 0–100 risk score with tiered response triggers (CSM outreach at 70, discount offer at 90, cancel-prevention flow at 95).
license: MIT
metadata: " id: ops.churn-risk-detector category: ops jurisdictions: [__multi__] priority: P1 intent: [churn, ops, retention, csm, predictive] related: [ops-nps-collector-in-chat, ops-credit-burn-rate-watcher, onboarding-upgrade-prompt-when-credits-low] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'ops'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Ops — Churn Risk Detector

## Purpose

Early identification of at-risk accounts gives the customer success team time to intervene before a cancellation decision is made. Churn in B2B legal AI is expensive to reverse — once a firm has moved their matters to a competitor, switching costs are high. This skill defines the predictive model inputs, the risk scoring logic, and the graduated response playbook.

## Input signals

The model draws on the following signals, evaluated per user (for consumer/SMB) or per tenant/account (for firm/enterprise):

| Signal | Weight | Churn indicator |
|--------|--------|-----------------|
| Login frequency trend (last 30d vs prior 30d) | High | Declining login frequency |
| Messages-per-session trend (last 30d vs prior 30d) | High | Declining depth per session |
| Feature breadth (number of distinct features used) | Medium | Drift to single feature (over-reliance = fragility) |
| Support ticket volume (last 30d) | Medium | Rising ticket volume without resolution |
| NPS score (most recent) | High | Score ≤ 6 (detractor) |
| Plan downgrade history | High | Any downgrade in last 90 days |
| Time since last success event | High | >14 days since a completed draft, research, or matter milestone |
| Explicit churn-signal events | Critical | See table below |

### Explicit churn-signal events (highest weight)

These events are strong leading indicators and should immediately spike the risk score:

| Event | Risk bump |
|-------|-----------|
| User exports all their data ("Export all") | +25 points |
| User submits a delete-account inquiry | +30 points |
| User raises a billing dispute or chargeback | +20 points |
| User explicitly mentions a competitor by name | +15 points |
| User cancels a renewal reminder | +10 points |

## Risk score output

The model outputs:

```json
{
  "userId": "<string>",
  "tenantId": "<string>",
  "riskScore": <0–100>,
  "topSignals": ["<signal description>", "..."],
  "suggestedAction": "<string>",
  "evaluatedAt": "<ISO timestamp>"
}
```

`riskScore` is a 0–100 integer where 0 = no risk and 100 = cancellation imminent.

`topSignals` lists the top 3 contributing signals in descending weight order.

`suggestedAction` is derived from the tiered playbook below.

## Response playbook

| Risk score | Action |
|------------|--------|
| 0–50 | No action. Monitor passively. |
| 51–69 | Flag in CSM dashboard. CSM may reach out at discretion. |
| 70–89 | **CSM outreach required.** Assign to account CSM; outreach within 48 hours. Goal: understand friction and remove blockers. |
| 90–94 | **Discount or incentive offer.** CSM calls with a concrete retention offer (discount, feature unlock, dedicated onboarding session). |
| 95–100 | **Cancel-prevention flow.** Escalate to senior CSM or account manager. Offer exit interview. Last-resort save: pause subscription instead of cancel. |

## Integration

- Scores are recalculated daily per user/tenant.
- Scores are surfaced in the ops dashboard under "At-Risk Accounts."
- Score changes of ±10 or more in a 24-hour window trigger a Slack notification to `#csm-alerts`.
- Pairs with [[ops-nps-collector-in-chat]]: a detractor NPS score (≤6) triggers an immediate score recomputation.
- Pairs with [[ops-credit-burn-rate-watcher]]: an account approaching credit exhaustion without upgrading is a moderate churn signal.

## Model calibration

The risk model should be recalibrated quarterly against actual churn outcomes:
- Compare predicted scores (30 days prior to churn) against accounts that actually cancelled.
- Adjust signal weights based on which signals were most predictive.
- Track false positive rate (high-risk accounts that did not churn) to avoid over-triggering CSM workload.

## Related skills

- [[ops-nps-collector-in-chat]] — provides the NPS detractor signal
- [[ops-credit-burn-rate-watcher]] — provides credit exhaustion signals
- [[onboarding-upgrade-prompt-when-credits-low]] — the in-product retention touchpoint for credit-low users
