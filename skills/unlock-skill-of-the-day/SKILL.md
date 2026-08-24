---
name: unlock-skill-of-the-day
description: Use when generating or surfacing a daily featured skill recommendation for active platform users. This skill governs the selection algorithm, persona matching, content format, distribution channels, and quality gates for the "Skill of the Day" feature, which surfaces one skill from the library each weekday morning matched to the user's practice area and current activity.
license: MIT
metadata: " id: unlock.skill-of-the-day category: unlock priority: P1 intent: [__unlock__, skill-discovery, engagement, daily-habit] related: - unlock-feature-discovery-by-persona - unlock-first-week-progressive-tour - unlock-template-of-the-week source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'unlock'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Skill of the Day

## Purpose

With nearly a thousand skills in the library, most users encounter only a small fraction through organic use. The Skill of the Day feature creates a daily discovery touchpoint that introduces users to capabilities they have not tried, matched to their persona and current work context.

The goal is habit formation through genuine value delivery — not notification noise. Each featured skill must be something the user can realistically use today.

## Selection algorithm

The selection pipeline runs each weekday morning per user.

### Step 1 — Filter by persona
- **Partner / senior lawyer**: restrict to `draft`, `review`, `intel`, `research`, `efirm` categories.
- **Associate / mid-level lawyer**: all `draft`, `review`, `kb`, `research` skills.
- **In-house counsel**: `draft`, `review`, `research`, `compliance`, `intel`.
- **Law student (Justinian)**: `justinian`, `casesim`, `academy`, `kb`.
- **Consumer (Louis Twin)**: `conversation`, `safety`, `kb` (consumer-appropriate only).

### Step 2 — Filter to production-quality skills only
- Skill `status` must be `drafted` or higher.
- Skill body must exceed 200 characters (stub skills are excluded).
- Skills flagged as `internal-only` or `admin` are excluded.

### Step 3 — Avoid recent exposure
- Exclude any skill featured in the last 7 days for this user.
- Exclude any skill the user has already invoked in the last 30 days.

### Step 4 — Weighted scoring
Score each remaining candidate:

| Factor | Weight |
|--------|--------|
| Trending (high platform-wide usage in past 7 days) | 30% |
| Contextual relevance (matches user's active matter type or recent query topics) | 40% |
| Diversity (not from same sub-category as yesterday's skill) | 20% |
| Recency (newer skills get a small boost) | 10% |

Select the highest-scoring candidate.

## Surfacing format

Each Skill of the Day card contains:

1. **Skill name** — human-readable, not the technical ID.
2. **One-sentence value proposition** — what the user can do with it today.
3. **Concrete example** — a mini-scenario showing the skill in action.
4. **Actions** — three CTAs: [Try it] [Read the skill] [Save for later].

### Example card

> **Skill of the Day: Shareholders' Agreement (SHA)**
>
> Build a full SHA for your next startup matter — equity split, reserved matters, drag/tag rights, and vesting schedule.
>
> *Example: a founder asks you to document a 60/40 split with four-year vesting and a 12-month cliff. This skill drafts the full SHA, flags the valuation and dilution mechanics, and includes DIFC/ADGM-compatible boilerplate.*
>
> [Try it] [Read the skill] [Save for later]

## Distribution channels

| Channel | Opt-in required | Timing |
|---------|----------------|--------|
| In-app notification (bell icon) | No (on by default) | 9:00 AM user's timezone |
| Email digest (weekly summary of 5 skills) | Yes | Monday 9:00 AM |
| Mobile push notification | Yes | 9:00 AM user's timezone |

Weekly email digest batches Monday–Friday selections into a single send, reducing email volume for users who prefer lower-frequency communication.

## Engagement tracking

For each Skill of the Day impression, record:

| Event | Meaning |
|-------|---------|
| `sotd.shown` | Card was displayed |
| `sotd.clicked_try` | User clicked "Try it" |
| `sotd.clicked_read` | User clicked "Read the skill" |
| `sotd.saved` | User saved for later |
| `sotd.dismissed` | User explicitly dismissed |
| `sotd.used_within_7d` | User invoked this skill within 7 days of seeing the card |

The most actionable metric is `sotd.used_within_7d` — this is the true success signal, not click-through rate.

## Quality gates — what not to surface

- **Never surface a stub.** A skill with only a one-line description teaches nothing and wastes the user's trust.
- **Never repeat.** The same skill appearing twice in a week signals a broken algorithm. Monitor for this.
- **Never ignore context.** A corporate M&A skill surfaced to a student doing bar prep is irrelevant. Persona + context filtering is non-negotiable.
- **Easy dismissal.** If the user dismisses three consecutive Skill of the Day cards, reduce frequency to every other day and flag for algorithm review.

## Relationship to Template of the Week

[[unlock-template-of-the-week]] operates on a weekly editorial calendar and features curated document templates. Skill of the Day is algorithmic and daily. They may feature the same underlying skill, but the editorial calendar takes precedence — do not let the algorithm feature a skill already highlighted in that week's Template of the Week.

## Related skills

- [[unlock-feature-discovery-by-persona]]
- [[unlock-first-week-progressive-tour]]
- [[unlock-template-of-the-week]]
- [[unlock-power-user-shortcuts]]
