---
name: ops-feature-request-collector
description: Use when a user in a legal AI chat session expresses a desire for a new feature, capability, or improvement. Guides the assistant through detecting feature-request language, gathering structured context, tagging by category and persona, submitting to the product backlog (Linear), and aggregating requests for weekly prioritization — distinct from bug reports which go to the bug collector.
license: MIT
metadata: " id: ops.feature-request-collector category: ops priority: P1 intent: [ops, feature-request, product-backlog, linear, roadmap] related: [ops-bug-report-collector, ops-linear-triage-from-chat-bug-report, ops-nps-collector-in-chat, ops-feature-flag-experiment-launcher] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'ops'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Ops — Feature Request Collector

## When to use this

Activate when a user's message contains any of the following patterns (or close semantic equivalents):

- "I wish Louis could…"
- "Can you add…"
- "It would be great if…"
- "Why doesn't Louis have…"
- "Other tools do X, why can't you?"
- "Is there a way to…" (when the answer is no, and the user seems to expect yes)
- "Will you support…"

Do not activate for existing feature questions ("how do I use X?") or for bug reports ("X isn't working"). Route those to [[ops-bug-report-collector]] if applicable.

## Collection flow

### 1. In-chat acknowledgement

At the next natural turn break, confirm you heard the request and ask permission to log it:

> That sounds like a useful feature. Mind if I log it for the product team?
>
> [**Yes, log it**]  [**No thanks**]

If the user says yes, proceed. If no, thank them and move on — do not pressure or re-ask in the same session.

### 2. Context gathering

Ask up to four clarifying questions, keeping the interaction brief:

1. "What specifically would you like the feature to do?"
2. "How often would you use it?" (daily / weekly / occasionally)
3. "How would you use it — in what kind of work?" (drafting / review / research / client communication / etc.)
4. "Any examples from other tools you've seen?"

Capture the user's own words. Do not paraphrase or reframe in legal jargon.

### 3. Auto-tagging

Tag the feature request automatically:

| Tag dimension | Values |
|--------------|--------|
| Category | `UI` / `drafting` / `review` / `research` / `integration` / `collaboration` / `export` / `analytics` / `settings` |
| Persona | `lawyer` / `in-house` / `consumer` / `student` / `enterprise-admin` |
| Tier | `free` / `starter` / `pro` / `business` / `enterprise` |
| Jurisdiction | Infer from user context if available |
| Effort estimate | `small` (UI tweak) / `medium` (feature) / `large` (platform change) — rough auto-estimate only |

Persona and tier are inferred from the user's account profile, not asked.

### 4. Linear submission

Create a Linear issue in the `LOUIS-FEATURES` project:

- **Title**: Short feature name in the form "User can [do X]" (e.g., "User can export draft to Google Docs")
- **Description**: User's exact words + context tags + source ("collected in-chat by feature-request-collector skill")
- **Labels**: category tag + persona tag + tier
- **Priority**: set to P3 by default; the product team triages to P2/P1/P0 based on aggregation
- **Linked to user profile**: so the team can follow up and also count how many users have requested this feature

### 5. User confirmation

After submission:

> Logged it. We'll evaluate it for the roadmap. Would you like us to let you know if it gets added?
>
> [**Yes please**]  [**No thanks**]

If they opt in, store the notification preference against the Linear issue.

## Aggregation

The feature request log is reviewed weekly by the product team. The aggregation process:

1. **Cluster similar requests**: group Linear issues by semantic similarity (e.g., multiple users asking for Google Docs integration).
2. **Count unique requesters**: a feature requested by 10 users outweighs the same feature requested once, even if the wording differs.
3. **Surface trending requests**: requests that received 3+ new instances in the last 7 days are surfaced in the Linear weekly digest.
4. **Cross-reference with NPS feedback**: detractors requesting missing features signal high-priority gaps.

## Prioritization signals (for the product team)

When the product team triages the collected requests, they use:

| Signal | Weight |
|--------|--------|
| Number of unique requesters | High |
| Requesters on paid tiers (Pro/Business/Enterprise) | High — their retention has higher revenue impact |
| Strategic fit with roadmap | High |
| Estimated engineering cost | Medium |
| Competitive differentiation | Medium |
| Requests from NPS detractors | High — these are features whose absence is causing dissatisfaction |

## Privacy

- Store only the feature description and metadata, not the full conversation context.
- User IDs stored against requests are anonymized tenant-scoped identifiers.
- Users who opt out of data collection can still submit requests — just without the follow-up notification.

## Related skills

- [[ops-bug-report-collector]] — the parallel flow for issues (not features)
- [[ops-linear-triage-from-chat-bug-report]] — downstream triage workflow
- [[ops-nps-collector-in-chat]] — NPS detractor feedback often surfaces feature gaps
- [[ops-feature-flag-experiment-launcher]] — high-priority feature requests often become experiments
