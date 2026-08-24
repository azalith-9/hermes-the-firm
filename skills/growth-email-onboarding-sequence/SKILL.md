---
name: growth-email-onboarding-sequence
description: Use when configuring or generating the 7-touch email onboarding sequence for new Louis users. Defines the full 30-day email cadence — timing, subject lines, content goals, personalization rules, and tracking metrics — from welcome email through upgrade nudge. The sequence adapts by user persona (lawyer, SME founder, in-house counsel, consumer) and respects opt-out and emotional-context rules.
license: MIT
metadata: " id: growth.email-onboarding-sequence category: growth priority: P0 intent: [__growth__, email, onboarding, activation, retention] related: [growth-push-notif-templates, growth-nps-prompt, growth-win-back-inactive, growth-case-study-asker, growth-referral-prompt] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'growth'.
Registered as a flat plugin skill.
-->


# Growth — Email Onboarding Sequence

## Purpose

New-user activation is the highest-leverage growth lever for a legal AI platform. Most users who sign up and never use the product are not opposed to it — they just never got far enough to experience real value. The 7-touch email sequence bridges that gap: it moves users from "signed up" to "integrated into workflow" over 30 days through progressively deeper prompts, social proof, and feature discovery.

This sequence is **P0** because early activation directly determines long-term retention. Users who complete their first successful task within 3 days have dramatically higher 30-day retention.

## Sequence overview

| Day | Subject line variant | Primary goal | Content |
|---|---|---|---|
| 0 | "Welcome to Louis" | Confirm + first step | Sign-up confirmation, 1-click first prompt, pricing context |
| 1 | "Pick your first skill" | First task activation | Persona-detected starter prompts, 30-second demo |
| 3 | "Need a hand?" | Re-engage dormant | Offer 1:1 demo; surface value props for non-activators |
| 7 | "Louis can do [X] — try it now" | Feature discovery | Highlight one underused feature matched to persona |
| 14 | "Your week with Louis" | Upgrade nudge | Usage summary + savings estimate; Pro plan benefits |
| 21 | "How [similar user] saves 5 hours/week" | Social proof | Persona-matched case study; soft CTA |
| 30 | "30 days in" | Renewal / survey | Recap progress; upgrade if appropriate; feedback survey if not |

## Email specifications

### Day 0 — Welcome

**Trigger**: immediately on sign-up confirmation.

**Goal**: confirm the user is in the right place and give them one clear next action.

**Content elements**:
- Warm welcome, brief statement of what Louis is (one sentence).
- 1-click CTA: "Start your first task" → opens pre-filled prompt matched to signup questionnaire.
- Brief pricing transparency note ("You're on the free tier — here's what you have").
- Support contact (human-reachable).

**Tone**: warm but professional. Lawyer-register for `lawyer` segment; accessible for `consumer`.

### Day 1 — First skill

**Trigger**: 24 hours after sign-up if user has not completed a task.

**Goal**: drive first task completion.

**Content elements**:
- "Here's what people like you start with" — list 3 persona-matched prompts.
- Embedded or linked short demo: "Watch Louis draft a UAE NDA in 30 seconds."
- Single CTA: "Try it now."

**Persona variants**:
- **Lawyer**: first prompts focus on drafting (NDA, employment clause) or reviewing a document.
- **SME founder**: first prompts focus on contract review, terms of service.
- **In-house**: first prompts focus on policy review, employment agreement.
- **Consumer**: first prompts focus on understanding a contract or lease.

### Day 3 — Re-engagement

**Trigger**: day 3 post-signup if fewer than 2 tasks completed.

**Goal**: identify and overcome barriers to first use.

**Content elements**:
- Acknowledge that getting started is sometimes hard: "Not sure where to begin?"
- Offer: 1:1 product demo (calendar link).
- Surface the top friction point (if known from analytics; otherwise: offer a guided first task).
- CTA options: "Book a demo" or "Try a guided task."

**Do not send if**: user has completed 3+ tasks in the first 3 days — they are activated, don't interrupt with a "beginner" email.

### Day 7 — Feature reveal

**Trigger**: day 7 post-signup.

**Goal**: expand the user's mental model of what Louis can do.

**Content elements**:
- Highlight one specific underused feature matched to the user's role and active skills.
- Examples: "Did you know Louis can summarize a full clause library in one pass?" or "Try the bilingual AR/EN drafting mode."
- Single CTA to the specific feature.

**Personalization**: use `user.active_skills` to identify which features they have NOT used, then pick the highest-value unused feature for their persona.

### Day 14 — Upgrade nudge

**Trigger**: day 14 post-signup.

**Goal**: convert free-tier users who have demonstrated value.

**Content elements**:
- Personal usage summary: "In your first 2 weeks, you completed [N] tasks and saved an estimated [X] minutes."
- Pro plan benefits relevant to their usage pattern (if they've hit free-tier limits, highlight the limit upgrade; if they've used drafting heavily, highlight saved templates).
- Side-by-side comparison of free vs Pro.
- Clear CTA: "Upgrade to Pro" with price.

**Do not send if**: user has already upgraded.

### Day 21 — Case study

**Trigger**: day 21 post-signup.

**Goal**: social proof for users who have not yet upgraded or are showing churn signals.

**Content elements**:
- Open with a practitioner story: "How a corporate associate in Dubai cut NDA turnaround from 2 hours to 20 minutes."
- Story follows the [[growth-case-study-asker]] format: role, use case, outcome, quote.
- Persona-match the story to the user (lawyer story for lawyer users, etc.).
- Soft CTA: "See if Louis fits your workflow too" → links to a specific skill.

### Day 30 — Progress recap

**Trigger**: day 30 post-signup.

**Goal**: consolidate activation, drive upgrade or collect feedback.

**Content elements**:
- "Here's your first month with Louis" recap card (tasks completed, time saved estimate, most-used skills).
- If user is on free tier and has hit value: upgrade CTA with first-month discount.
- If user has low activity: short feedback survey ("What would make Louis more useful for you?").
- If user is already on Pro: appreciation note + invitation to community / advisory program.

## Sequence rules

- **Unsubscribe link**: required in every email. Respect immediately; no re-engagement attempts for 90 days post-unsubscribe.
- **Emotional matter delay**: if user has a matter flagged as distress (divorce, insolvency, urgent litigation), delay all non-essential emails by 24 hours.
- **Personalization per persona**: the copy is different for `lawyer` vs `sme-founder` vs `consumer`. Do not send generic copy — persona detection should gate which sequence variant fires.
- **A/B test subject lines**: run at minimum a 2-variant test on each email subject line. Winning variant is the one with higher open rate at 48h.
- **No duplicate sends**: ensure idempotency — email platform must check "sent" flag before triggering each touch.
- **Respect timezone**: send each email at ~9am local time for the user's detected timezone.

## Tracking metrics

| Metric | Target | Note |
|---|---|---|
| Day 0 open rate | > 70% | High because it's a confirmation email |
| Day 1 open rate | > 45% | |
| Day 1 CTA click rate | > 20% | Activation metric |
| Day 3 re-engagement open rate | > 30% | |
| Day 14 upgrade click rate | > 5% | Revenue metric |
| Day 30 upgrade conversion | > 3% | |
| Unsubscribe rate per email | < 1% | Alert if > 2% |

## Related skills

- [[growth-push-notif-templates]]
- [[growth-nps-prompt]]
- [[growth-win-back-inactive]]
- [[growth-case-study-asker]]
- [[growth-referral-prompt]]
