---
name: growth-win-back-inactive
description: Use when the platform needs to re-engage users who have been inactive for 30 or more days. Defines the four-stage win-back sequence (30/60/90/180 days), channel selection, copy approach by inactivity reason, incentive escalation, and stopping criteria. Designed for the MENA legal market where users may go quiet due to seasonal legal calendars, matter closure, or simply not finding their first-use path.
license: MIT
metadata: " id: growth.win-back-inactive category: growth priority: P0 intent: [__growth__, win-back, re-engagement, churn-prevention, retention] related: [growth-email-onboarding-sequence, growth-push-notif-templates, growth-nps-prompt, ops-churn-risk-detector] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'growth'.
Registered as a flat plugin skill.
-->


# Growth — Win-Back Inactive Users

## Purpose

User inactivity is not the same as churn. A lawyer who signed up for Louis, completed a few tasks, and then went quiet may have gone quiet because their deal closed, because they hit a friction point, or simply because they got busy. The win-back sequence diagnoses the reason and makes a targeted, honest offer to return — without harassment.

This skill operates in the 30–180 day window. Users inactive past 180 days who do not respond to the final touch are retired to a suppressed state.

## Inactivity stages

| Stage | Days inactive | Approach | Incentive |
|---|---|---|---|
| Stage 1 | 30 days | Light touch — "just checking in" | None |
| Stage 2 | 60 days | Feature highlight — product has improved | None |
| Stage 3 | 90 days | Incentive offer — free credits or discount | Free credits / 30-day extension |
| Stage 4 | 180 days | Final "last chance" message | Best available incentive + sunset notice |

## Stage 1 — 30-day light touch

**Purpose**: remind the user that Louis exists and that work may be waiting.

**Channels**: email (primary); push notification if app installed and permission granted.

**Copy approach**: matter-contextual where possible. If the user has open matters, reference them ("Your matters have been quiet for a few weeks — anything we can help with?"). If no open matters, use a general prompt based on their role.

**CTA**: "Pick up where you left off" → links to their last active matter or to the skill they used most.

**Do not**: make assumptions about why they left; do not mention "inactivity" explicitly; do not include an incentive at this stage.

## Stage 2 — 60-day feature highlight

**Purpose**: communicate that the product has improved since their last visit, giving them a reason to return beyond obligation.

**Channels**: email (primary); push notification if app installed.

**Copy approach**: "We've made [X] better since you last visited." Identify a specific improvement relevant to their persona:
- For `lawyer`: new skill, improved accuracy on their practice area.
- For `consumer`: simpler interface, new use case.
- For `in-house`: new policy-review or bulk-upload feature.

If no specific improvement is available, use a feature they signed up for but never tried.

**CTA**: "Try [specific feature]" → links directly to the feature, not to the home screen.

**Do not**: send the same feature highlight to every inactive user — it reads as mass marketing. Personalize to the user's persona and usage history.

## Stage 3 — 90-day incentive offer

**Purpose**: remove the barrier of commitment with a risk-free return.

**Channels**: email (primary); SMS if user has opted in; push notification.

**Copy approach**: honest and direct.

> *"It's been a while. We'd like you back — and we're making it easier with [X credits / 30 free days]. No strings. Just come try the thing you signed up for."*

**Incentive options** (select based on plan tier):
- AI tier: +50% credits for 30 days.
- eFirm tier: 30-day extension of current plan.
- Both tiers: offer of a 1:1 demo with the Louis team for hands-on orientation.

**CTA**: "Claim your free credits" or "Book a free demo" — clear, low-pressure.

**Important**: do not make the incentive feel desperate. One offer, clearly stated, with an easy way to accept and a clear expiry date.

## Stage 4 — 180-day final message

**Purpose**: make one final genuine offer; close the loop gracefully.

**Channels**: email only. No push, no SMS — those channels have probably already been dismissed.

**Copy approach**: respectful and final.

> *"This is our last message before we stop reaching out. If Louis isn't right for you, we understand — we'd be grateful if you'd tell us why. If you want to give it one more try, here's our best offer: [incentive]."*

Include a short 1-question exit survey: "What's the main reason you stopped using Louis?" (5 options + "other" text field). This data feeds directly into product prioritization.

**After stage 4 with no response**: mark user as `win-back-suppressed`. No further automated outreach. CS may attempt manual outreach for high-value accounts only.

## Approach by inactivity reason

Where analytics or exit survey data indicates the reason for inactivity, tailor the approach:

### Tried but didn't stick (completed 1–3 tasks, then stopped)
- "We've made [specific friction point] easier — try [improved feature]"
- Offer a 1:1 guided demo to find their workflow fit.
- Free credits for re-activation.

### Signed up but never activated (< 1 task completed)
- Treat as a late-onboarding case, not a win-back.
- "Pick your first skill" prompt (same as Day 1 of [[growth-email-onboarding-sequence]]).
- Sample case study relevant to their persona.
- Free trial extension.

### Was active, then went quiet
- This is the highest-value segment — they found value once.
- Outreach from CS (for accounts > 50 tasks completed) — personal email, not automation.
- "Did we miss something?" with a genuine feedback ask.
- Offer concierge support or a personal onboarding session.

## Channels and delivery rules

| Channel | When to use | Notes |
|---|---|---|
| Email | All stages (primary) | Respect unsubscribe; suppress if opted out |
| Push notification | Stages 1–3 if app installed + permission granted | One push per stage; respect quiet hours |
| SMS | Stage 3 only, if explicitly opted in | Sparingly; high personal intrusion |
| LinkedIn | For B2B / eFirm accounts, stages 2–3 | Treat as personal outreach, not automation |

## Rules and safeguards

- **Respect unsubscribe**: if the user unsubscribed from any Louis email, suppress all non-transactional win-back emails immediately. Do not work around this.
- **One attempt per stage**: if stage 1 email gets no open, do not send a stage 1 follow-up; advance to stage 2 at the next interval.
- **Don't be desperate**: win-back messages should feel like a genuine invitation, not a plea. If your copy sounds needy, rewrite it.
- **Genuine value**: the best win-back is a product improvement the user cares about, not a discount. Always lead with what's new or better.
- **Win-back data**: track who comes back after each stage, which incentive drove return, and what their subsequent retention looks like. This data determines which stage and copy variant to invest in.

## Related skills

- [[growth-email-onboarding-sequence]]
- [[growth-push-notif-templates]]
- [[growth-nps-prompt]]
- [[ops-churn-risk-detector]]
