---
name: ops-nps-collector-in-chat
description: Use when collecting Net Promoter Score (NPS) feedback within a legal AI chat session. Defines the trigger conditions (10th successful turn, major milestone, quarterly heartbeat), the in-chat survey flow (0–10 scale + open-ended follow-up), the output schema, and the downstream routing — detractors to the churn risk detector, promoters to the case-study asker.
license: MIT
metadata: " id: ops.NPS-collector-in-chat category: ops jurisdictions: [__multi__] priority: P2 intent: [nps, ops, retention, satisfaction, feedback] related: [ops-churn-risk-detector, ops-case-study-asker-after-n-messages, ops-feature-request-collector] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'ops'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Ops — NPS Collector In-Chat

## Purpose

NPS collected passively (email surveys, post-session popups) has low response rates from legal professionals who are busy and suspicious of unsolicited outreach. Collecting NPS in-context — immediately after a successful interaction — yields higher response rates and more actionable follow-up because the user's experience is fresh.

## Trigger conditions

The NPS prompt fires on **one** of the following triggers (whichever comes first, with appropriate cool-down):

| Trigger | Condition | Cool-down |
|---------|-----------|-----------|
| Engagement milestone | User completes their 10th successful turn (substantive output delivered) | 90 days before asking again |
| Product milestone | User completes their first full contract draft, saves their first matter, or closes a matter | 90 days |
| Quarterly heartbeat | Last NPS collection was >90 days ago and user is still active | 90 days |

**Never trigger during**:
- An active legal task (mid-drafting, mid-research)
- A conversation that signals distress or urgency
- Within 7 days of a failed turn, error, or support ticket

## In-chat prompt

Surface the prompt as a non-blocking in-line message at the next natural break:

> Quick question — on a scale of 0 to 10, how likely are you to recommend Louis to a colleague?
>
> [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10]  
> [Skip]

The scale must be displayed as tappable/clickable elements (not a text field where the user has to type a number). One tap should submit the score.

## Follow-up questions

Based on the score, surface a single open-ended follow-up:

| Score | Classification | Follow-up prompt |
|-------|---------------|-----------------|
| 9–10 | Promoter | "Glad to hear it! What's been most useful to you?" |
| 7–8 | Passive | "What would make Louis even better for you?" |
| 0–6 | Detractor | "We're sorry to hear that. What's not working well? (We read every response.)" |

The follow-up is optional — make it clearly skippable. One-sentence or keyword answers are fine; do not ask for paragraphs.

## Output schema

```json
{
  "userId": "<anonymized>",
  "tenantId": "<UUID>",
  "score": <0-10>,
  "classification": "promoter | passive | detractor",
  "comment": "<string or null>",
  "context": {
    "trigger": "milestone | heartbeat | engagement",
    "sessionId": "<UUID>",
    "lastActionBefore": "<event name>"
  },
  "collectedAt": "<ISO timestamp>"
}
```

## Downstream routing

| Classification | Action |
|---------------|--------|
| Promoter (9–10) | After 30 days, trigger [[ops-case-study-asker-after-n-messages]] if tenure + turn thresholds are also met. |
| Passive (7–8) | Log for product team review. Surface the comment in the weekly NPS digest. |
| Detractor (0–6) | Immediately recompute the churn risk score via [[ops-churn-risk-detector]]. If the detractor score pushes risk >70, trigger CSM outreach. |

For all scores, the comment (if provided) is logged in the feature request system if it describes a missing capability, or in the bug tracker if it describes a malfunction.

## Aggregate analysis

Weekly NPS digest (posted to `#product-ops` Slack):
- Rolling 7-day NPS score (calculated as % promoters − % detractors)
- Trend vs prior 7 days and prior 30 days
- Top themes from comments (keyword clustering)
- Detractor comments reviewed individually by the product lead

## Privacy

- NPS scores and comments are stored at the user/tenant level.
- Comments may contain sensitive context ("I was handling a client's divorce matter and it got the law wrong"). Treat these as confidential product feedback, not shareable marketing data.
- Users who opt out of feedback collection are excluded from all NPS triggers.

## Related skills

- [[ops-churn-risk-detector]] — receives the detractor signal and computes churn risk
- [[ops-case-study-asker-after-n-messages]] — receives the promoter signal for testimonial collection
- [[ops-feature-request-collector]] — comments from passives and detractors often describe missing features
