---
name: ops-case-study-asker-after-n-messages
description: Use when a high-value user has crossed a tenure and engagement threshold (50+ turns, 90+ days, NPS promoter) to request a testimonial quote or firm logo feature in the customer wall. Defines the trigger logic, conversation prompt, and downstream handoff to the testimonial collector — with rules about not pressuring users in active legal work and respecting skips gracefully.
license: MIT
metadata: " id: ops.case-study-asker-after-N-messages category: ops jurisdictions: [__multi__] priority: P2 intent: [case-study, ops, testimonial, social-proof, retention] related: [ops-nps-collector-in-chat, outreach-testimonial-collector, ops-churn-risk-detector] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'ops'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Ops — Case Study Asker After N Messages

## Purpose

Social proof is a key driver of B2B legal AI adoption. Law firms and in-house teams are more persuaded by peer testimonials than by vendor claims. This skill handles the in-product moment where an engaged, satisfied user is asked for a testimonial quote or a logo feature — gently, at the right time, and with a dead-simple response flow.

## Trigger conditions

All three conditions must be satisfied before the ask:

| Condition | Threshold | Rationale |
|-----------|-----------|-----------|
| Session depth | 50+ successful turns (cumulative, across all sessions) | User has genuinely used the product, not just explored |
| Tenure | 90+ days since account creation | Enough time to have formed a real view |
| Satisfaction signal | NPS score 9–10 (promoter), OR matter closed-won attributed to the assistant | Only ask satisfied users; detractors are routed to [[ops-churn-risk-detector]] |

Optional additional signal: if the user has explicitly said something positive in chat ("this saved me hours", "really impressed") in the last 30 days, weigh that as a soft positive trigger even if the NPS threshold has not been scored.

## Conversation prompt

Surface the ask at the next natural break after all trigger conditions are met. Use one of two variants based on what the user is most likely to find easy:

### Variant A — Testimonial quote
> Louis has helped you handle [X matters / Y tasks] over the past [Z months]. We'd love to share your experience with other legal teams.
>
> Would you be willing to share a 1–2 sentence quote we could use in our materials?
>
> [**Sure, let me write one**]  [**Maybe later**]  [**No thanks**]

### Variant B — Logo feature (lighter ask)
> You've been with Louis for [Z months] — we'd love to feature [Firm Name] on our customer wall (logo only, no quote).
>
> [**Yes, use our logo**]  [**Maybe later**]  [**No thanks**]

Offer Variant B if the user has previously skipped Variant A, or if the user's firm is large enough that a logo feature has more marketing value than an individual quote.

## Response handling

| User response | Action |
|---------------|--------|
| "Sure" / "Yes" | Open a short in-chat collection flow: ask for the quote text (Variant A) or logo file/permission (Variant B). Hand off to [[outreach-testimonial-collector]]. |
| "Maybe later" | Suppress for 60 days. Re-surface once after 60 days if the user is still active. |
| "No thanks" | Suppress permanently for this user. Never ask again on the same account. |

If the user provides a quote, confirm it back to them before submitting:
> Here's the quote I'll submit: "[their quote]" — does that look right?
>
> [**Yes, submit it**]  [**Let me edit**]

## Timing rules

- Never ask during an active legal task (mid-drafting session, mid-review, mid-research).
- Never ask if the last NPS score was ≤ 6 (detractor/passive) — route those to the churn detector instead.
- Never ask more than once per 60 days on the same account.
- Never ask if the account is in a support ticket backlog or unresolved issue.
- Ask limit: maximum 3 total lifetime asks per user. After 3 declines or skips, stop permanently.

## What to pass to the testimonial collector

On successful collection, pass the following to [[outreach-testimonial-collector]]:

```json
{
  "userId": "<anonymized>",
  "firmName": "<firm if known and consented>",
  "quote": "<their text>",
  "logoConsent": true|false,
  "collectedAt": "<ISO timestamp>",
  "channel": "in-chat",
  "usageMetrics": {
    "turnsCount": <N>,
    "tenureDays": <N>,
    "npsScore": <N>
  }
}
```

The marketing team reviews and approves all testimonials before publication. Do not publish automatically.

## Related skills

- [[ops-nps-collector-in-chat]] — provides the NPS promoter signal that triggers this ask
- [[outreach-testimonial-collector]] — downstream marketing handling of collected testimonials
- [[ops-churn-risk-detector]] — handles detractors who should not receive a testimonial ask
