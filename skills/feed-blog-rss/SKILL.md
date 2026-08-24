---
name: feed-blog-rss
description: Use when the platform needs to surface a personalized blog and content RSS feed for a Louis user. Aggregates legal blog posts, thought-leadership articles, and practice-relevant content from selected MENA and global legal publishers, filtered by user role, practice area, and jurisdiction preferences. Pairs with churn-risk signals to prioritize re-engagement content.
license: MIT
metadata: " id: feed.blog-RSS category: feed jurisdictions: [__multi__] priority: P3 intent: [__feed__, content-aggregation, personalization, re-engagement] related: [feed-legal-news-mena, feed-case-law-new-publications, ops-churn-risk-detector, feed-changelog-watcher] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'feed'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Blog RSS Feed Surface

## Purpose

The blog RSS surface delivers curated long-form legal content — articles, commentaries, practice guides, and law-firm client alerts — to users within the Louis feed panel. The goal is to keep legal professionals informed about developments in their practice area without requiring them to maintain their own RSS subscriptions.

This surface is **awareness-oriented**, not action-oriented. It does not surface deadlines or matter notifications (those belong to the gazettes and regulator-bulletins feeds). It surfaces thinking material: new court commentary, law firm alerts on regulatory change, academic short-pieces, and how-to guides relevant to the user's jurisdiction and practice.

## Inputs / signals

| Signal | Source | Usage |
|---|---|---|
| `user.practice_area` | User profile | Filters feed categories |
| `user.jurisdictions` | User profile | Filters by geographic relevance |
| `user.role` | User profile (`lawyer`, `in-house`, `consumer`) | Adjusts content register and depth |
| `churn_risk_score` | [[ops-churn-risk-detector]] | High-risk users get more engaging/re-activation content |
| `matter_context` | Active matters | Surfaces articles contextually matching open matters |
| `explicit_feed_prefs` | User feed settings | Hard include/exclude for specific publishers |

## Feed sources

Categorized by type and jurisdiction coverage:

### MENA-focused publishers
- **Al Tamimi & Company** client alerts (UAE, KSA, DIFC/ADGM)
- **Hadef & Partners** publications (UAE)
- **BSA Ahmad Bin Hezeem** client alerts (UAE)
- **Badri and Salim El Meouchi** (LB)
- **Azhari Law Firm** (LB)
- **ACWA** and regional regulatory commentary (KSA, Gulf)
- **Lexology** MENA filter
- **Mondaq** MENA legal filter

### International / cross-border
- **Thomson Reuters Legal** (Westlaw feeds — where API licensed)
- **Lexology** global
- **Law360** international
- **Practical Law** client alerts (UK, EU)
- **Harvard Law Today** (general)

### Free/open legal blogs
- **Conflicts of Laws .net** (private international law — relevant for cross-border MENA)
- **Oxford Business Law Blog** (commercial law, M&A)
- Open legal commentary from government-affiliated law schools in MENA region

## Personalization logic

1. **Base pool**: pull all items published in the past 7 days from subscribed feeds.
2. **Jurisdiction filter**: retain only items tagged or inferred to match the user's active jurisdiction(s). Cross-jurisdictional content (e.g., "GCC-wide" or "OHADA") is included if user has any matching jurisdiction.
3. **Practice-area score**: weight items by cosine similarity between article metadata/keywords and user's primary practice area.
4. **Role register filter**: for `consumer` role, exclude pure technical bar-association commentary; for `lawyer` role, de-prioritize lay-explanation articles.
5. **Churn-risk boost**: if `churn_risk_score > 0.7`, prioritize high-engagement titles (shorter reads, practical how-to framing) over deep commentary.
6. **Recency decay**: items older than 14 days receive a freshness penalty.
7. **Deduplication**: collapse near-identical articles from multiple syndicating publishers.

## Output spec

Each feed item rendered in the UI:

```json
{
  "id": "feed-item-uuid",
  "source_feed": "al-tamimi-alerts",
  "title": "UAE Amends Commercial Companies Law: Key Changes for 2025",
  "summary": "...", // 2-3 sentence AI-generated summary
  "url": "https://...",
  "published_at": "2025-05-12T08:00:00Z",
  "jurisdictions": ["UAE", "DIFC"],
  "practice_areas": ["corporate", "commercial"],
  "read_time_minutes": 5,
  "relevance_score": 0.87,
  "is_bookmarked": false
}
```

## Quality bar

- Items must be from recognized legal or law-firm publishers — no news aggregators without legal editorial oversight.
- AI-generated summaries must accurately represent the article; do not editorialize or reinterpret legal positions.
- Never surface items that contain a specific legal claim unless that claim is attributable to the original publisher.

## Failure modes

- **Feed source goes offline**: cache last 30 days of items; surface a "publisher unavailable" label; don't show stale items beyond 30 days without a freshness flag.
- **Over-personalization**: if the filtered result set is < 3 items, widen jurisdiction filter to region level (e.g., GCC instead of UAE-only).
- **Publisher paywall**: surface the item with a paywall indicator; do not attempt to fetch or summarize paywalled content beyond the lede.

## Related skills

- [[feed-legal-news-mena]]
- [[feed-case-law-new-publications]]
- [[feed-regulator-bulletins-mena]]
- [[ops-churn-risk-detector]]
- [[feed-changelog-watcher]]
