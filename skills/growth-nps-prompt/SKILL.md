---
name: growth-nps-prompt
description: Use when the platform needs to survey users with a Net Promoter Score question to measure satisfaction, segment users by likelihood to refer, and route detractors to customer success. Defines trigger timing, survey format, scoring methodology, segmentation rules, and downstream actions for promoters (case study ask, referral prompt) and detractors (CS follow-up). Pairs with the in-chat NPS collector for inline implementation.
license: MIT
metadata: " id: growth.NPS-prompt category: growth priority: P1 intent: [__growth__, NPS, satisfaction, survey, retention, referral] related: [growth-case-study-asker, growth-referral-prompt, growth-win-back-inactive, growth-email-onboarding-sequence, ops-nps-collector-in-chat] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'growth'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Growth — NPS Prompt

## Purpose

Net Promoter Score (NPS) is the single most actionable aggregate satisfaction metric for a legal AI product. Beyond the score itself, the NPS workflow is the gateway to: identifying promoters for case studies and referrals, surfacing detractors to CS before they churn, and collecting qualitative feedback that drives product prioritization.

This skill defines when to ask, how to ask, how to score, and what to do with the result.

## When to ask

NPS surveys should feel contextually earned — asked after a real positive or meaningful experience, not on a mechanical timer.

| Trigger | Condition |
|---|---|
| Time-based — new user | 30 days after sign-up (sufficient time to form an opinion) |
| Task-based | After 5 successful task completions |
| Retention-based | Quarterly for users with > 90 days of activity |
| Release-based | After a major product release (optional, keep to once per quarter) |

**Minimum gap rule**: never ask the same user more than once per 90 days regardless of trigger.

## Survey format

### Primary question
> *"On a scale of 0–10, how likely are you to recommend Louis to a colleague or fellow practitioner?"*

0 = Not at all likely | 10 = Extremely likely

### Follow-up (always ask, one short text field)
> *"What's the main reason for your score?"*

This qualitative field is where the real insight lives. Do not make it optional — but keep it low-friction (no word minimum, no formatting required).

### Optional permission
> *"May we follow up with a quick conversation about your experience?"*
> [ Yes, happy to chat ] [ No thanks ]

Users who say yes are routed to [[growth-case-study-asker]] (for promoters) or CS calendar (for detractors).

## Scoring

### Segment classification
| Score | Segment | Definition |
|---|---|---|
| 9–10 | Promoter | Happy, likely to refer; high retention probability |
| 7–8 | Passive | Satisfied but not enthusiastic; vulnerable to churn or switching |
| 0–6 | Detractor | At risk; may actively discourage others |

### NPS calculation
```
NPS = (% Promoters) − (% Detractors)
```
Passives are excluded from the calculation.

### Benchmarks
- SaaS industry average: 30–50
- World-class SaaS: 70+
- Legal AI is a new category; target > 50 in early phases; > 60 at maturity.

## Downstream actions by segment

### Promoters (9–10)
1. Thank them immediately in-app ("Thank you! We're delighted you're finding value.").
2. Queue for [[growth-referral-prompt]] (24–48 hours later, separate touch).
3. Queue for [[growth-case-study-asker]] (48–72 hours later, if no prior case study).
4. Tag in CRM as "Promoter — [date]" for sales outreach if eFirm upgrade candidate.

### Passives (7–8)
1. Thank them.
2. Route qualitative feedback to product team.
3. Investigate the gap: which feature or friction point is keeping them from being a promoter?
4. Follow up with targeted feature discovery email within 14 days.
5. Do not rush to upsell — passives need value deepening first.

### Detractors (0–6)
1. Thank them sincerely and acknowledge the score.
2. Immediate routing to CS for human follow-up within 24 hours.
3. Do **not** send marketing or upsell emails to a detractor until CS has resolved the issue.
4. Log churn-risk signal to [[ops-churn-risk-detector]].
5. If CS resolves the issue, re-survey after 60 days.

## Segmentation and analysis

Beyond the aggregate NPS, segment the results to drive product decisions:

- **By persona**: is the NPS for `lawyer` users vs `consumer` users different? If so, which product experience is failing?
- **By feature usage**: are heavy document-workspace users more satisfied than casual users? If so, what does this tell you about the core value driver?
- **By jurisdiction**: are MENA users rating differently from EU users? Could indicate localization gaps.
- **By tenure**: are 30-day users rating higher than 180-day users (engagement decay)? Or lower (they haven't found value yet)?
- **By plan tier**: are Pro users more satisfied? If so, is it the features or the mindset of paid users?

## Anti-patterns

| Anti-pattern | Why it fails |
|---|---|
| Ask too often | Survey fatigue; users start ignoring or giving noise scores |
| No follow-through on detractor feedback | Destroys trust; the worst outcome is asking and doing nothing |
| Use NPS as the sole quality metric | NPS is a lagging indicator; combine with CSAT, churn rate, feature adoption |
| Punish detractors with more nags | Give detractors a clear path to resolution, not more automation |
| Ask immediately after sign-up | No opinion formed yet; score is random noise |
| Make the follow-up mandatory | Blocks completion; qualitative question should be open but not required |

## Presentation in-app

The in-chat NPS is implemented via [[ops-nps-collector-in-chat]]. It appears as a simple 0–10 slider with a submit button, rendered inline in the chat interface after a triggering event. Do not open a new page or modal — keep it frictionless.

For email NPS, use a 1-click score link in the email body (clicking the number opens a web form pre-filled with the score, showing only the follow-up question).

## Related skills

- [[growth-case-study-asker]]
- [[growth-referral-prompt]]
- [[growth-win-back-inactive]]
- [[growth-email-onboarding-sequence]]
- [[ops-nps-collector-in-chat]]
