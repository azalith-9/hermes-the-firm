---
name: feed-changelog-watcher
description: Use when the platform needs to surface Louis product changelog entries to users as in-app feed items. Monitors the Louis changelog source (release notes, sprint summaries, feature announcements) and delivers structured notifications to users, prioritized by relevance to their role and plan tier. Helps users discover new skills, updated workflows, and resolved issues without requiring them to check external release notes.
license: MIT
metadata: " id: feed.changelog-watcher category: feed jurisdictions: [__multi__] priority: P3 intent: [__feed__, product-updates, feature-discovery, changelog] related: [feed-status-incident-watcher, feed-blog-rss, ops-churn-risk-detector, growth-email-onboarding-sequence] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'feed'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Changelog Watcher Feed Surface

## Purpose

The changelog watcher surfaces Louis platform updates — new skills, improved workflows, resolved bugs, and pricing/plan changes — directly in the user's feed. The goal is feature discovery and trust-building: users who know the product is actively improving are more likely to re-engage and expand usage.

This feed is distinct from [[feed-status-incident-watcher]], which covers outages and degradations. This feed is positive and forward-looking.

## Inputs / signals

| Signal | Source | Usage |
|---|---|---|
| `changelog_source` | Internal release pipeline (GitHub releases / Notion / Linear changelog) | Primary content source |
| `user.plan_tier` | User account | Filter plan-gated features |
| `user.role` | User profile | Surface role-relevant changes first |
| `user.active_skills` | Usage data | Prioritize changes to skills the user has actually used |
| `churn_risk_score` | [[ops-churn-risk-detector]] | High-risk users: surface compelling new feature highlights |
| `last_login` | Session data | Users returning after absence get "what's new since you left" digest |

## Changelog entry categories

| Category | Display label | Priority |
|---|---|---|
| New skill or skill update | "New skill" / "Updated skill" | High if user-relevant |
| New feature (UI/UX) | "New feature" | High |
| Performance improvement | "Faster" | Medium |
| Bug fix (user-facing) | "Fixed" | Medium if affects user |
| API / integration update | "API update" | High for developer accounts |
| Plan/pricing change | "Plan update" | High always |
| Security update | "Security" | High always |
| Infrastructure (user-invisible) | Omit from user feed | N/A — internal only |

## Personalization logic

1. **Role filter**: a `consumer` user does not need API changelog items; a developer does. Filter by `user.role`.
2. **Plan-tier filter**: don't surface features exclusive to a higher plan without an upgrade CTA. For lower-tier users: show the feature with "Available on Pro" framing.
3. **Skill-usage boost**: if the changelog item relates to a skill in `user.active_skills`, boost its feed score.
4. **Returning-user digest**: if the user's last login was > 14 days ago, prepend a "Here's what's new since [date]" digest item summarizing the top 5 changes. This is the single highest-value use of this feed.
5. **Frequency cap**: maximum 1 changelog digest per day per user; individual items can stack but collapse into a digest view when > 3 in a day.

## Output spec

```json
{
  "id": "changelog-uuid",
  "entry_type": "new-skill",
  "title": "New: draft.shareholders-agreement for UAE and KSA",
  "summary": "Draft multi-party shareholders agreements for UAE onshore and KSA entities. Covers board composition, transfer restrictions, drag-along, and tag-along rights.",
  "published_at": "2025-05-01T10:00:00Z",
  "plan_required": "pro",
  "skill_id": "draft-shareholders-agreement",
  "jurisdictions": ["UAE", "KSA"],
  "cta": {
    "label": "Try it now",
    "action": "open_skill",
    "skill_id": "draft-shareholders-agreement"
  },
  "relevance_score": 0.82
}
```

## What makes a good changelog entry

- **Specific and concrete**: "New skill: review.employment-contract for DIFC and UAE federal" is better than "Added new legal review feature."
- **User-value framing**: "saves you 20 minutes on NDA review" is better than "optimized NDA review pipeline."
- **Actionable CTA**: every item should have a one-click action — "Try it," "See what changed," or "Upgrade to access."
- **Short**: changelog items in-feed should be 2-4 sentences maximum. Link to a full release note for detail.

## Failure modes

- **No new entries**: show the last 3 changelog items with a "Last updated [date]" note. Don't show an empty feed section.
- **Changelog source unavailable**: cache last known state. Do not surface an error to the user — simply omit new items until source recovers.
- **Feature flag mismatch**: if a changelog item references a feature not yet rolled out to the user's account, suppress the item until rollout applies.

## Related skills

- [[feed-status-incident-watcher]]
- [[feed-blog-rss]]
- [[ops-churn-risk-detector]]
- [[growth-email-onboarding-sequence]]
- [[growth-push-notif-templates]]
