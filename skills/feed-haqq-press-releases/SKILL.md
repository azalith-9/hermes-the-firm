---
name: feed-haqq-press-releases
description: Use when the platform needs to surface official Louis / HAQQ Legal AI press releases, product announcements, partnership news, and institutional communications as a curated feed for users. This feed maintains brand trust by giving users a single authoritative source for platform-level news, as opposed to third-party coverage or rumor. Relevant to in-house teams, enterprise accounts, and users who need to cite the platform's institutional standing.
license: MIT
metadata: " id: feed.HAQQ-press-releases category: feed jurisdictions: [__multi__] priority: P3 intent: [__feed__, press-release, brand-news, platform-announcements] related: [feed-changelog-watcher, feed-status-incident-watcher, feed-blog-rss, growth-case-study-asker] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'feed'.
Namespaced as louis-<category>-<skill> on registration.
-->


# HAQQ Press Releases Feed Surface

## Purpose

This feed surface delivers official HAQQ Legal AI / Louis press releases, partnership announcements, funding news, and institutional statements directly inside the platform. It gives users a vetted, primary-source news stream about the platform itself, separate from the product changelog (which covers technical changes) and the legal news feeds (which cover the outside legal world).

The primary users of this feed are:
- **Enterprise / eFirm account managers** who need to brief stakeholders on the platform's institutional credibility.
- **Individual practitioners** who want to understand the company's direction and trust signals (funding, partnerships, regulatory recognition).
- **Journalists and press contacts** accessing the platform to verify announcements.

## Content types

| Type | Description | Frequency |
|---|---|---|
| Product launch / major feature | New product lines, major releases | 1–4 per year |
| Partnership announcement | Bar association recognition, institutional partnerships, law school integrations | As they occur |
| Funding / investment round | Seed, Series A, etc. | Rare; high visibility |
| Legal tech award or recognition | Industry rankings, conference presentations | Occasional |
| Regulatory or compliance statement | Official compliance position on AI regulation, data protection policies | As required |
| Executive commentary | CEO / founder quotes on industry trends | Quarterly or as relevant |
| Event presence | Conference participation, MENA legal tech events | As scheduled |
| Crisis / clarification statement | Corrections to third-party coverage | As needed |

## Inputs / signals

| Signal | Source | Usage |
|---|---|---|
| `press_release_source` | HAQQ PR pipeline (CMS / Notion / press API) | Primary content source |
| `user.role` | User profile | Admins + account managers get all items; consumers get curated subset |
| `user.plan_tier` | Account tier | Enterprise users get exclusive early access to announcements |
| `user.language_preference` | User settings | Bilingual AR/EN where available |

## Personalization logic

For this feed, personalization is lighter than for legal-content feeds:

1. **Role filter**: enterprise admins see all items including regulatory compliance statements. Consumer-tier users see product and partnership items only; skip financial/IR-focused items.
2. **Language preference**: surface Arabic version of press releases where available. Flag "English only" where Arabic translation is not yet published.
3. **Recency**: press releases older than 90 days are archived and not surfaced in the main feed (accessible via search/archive).
4. **Priority override**: funding announcements and regulatory statements are always surfaced regardless of role filter.

## Output spec

```json
{
  "id": "pr-item-uuid",
  "type": "partnership",
  "headline": "Louis Partners with Beirut Bar Association to Provide Access to AI Legal Tools for Members",
  "summary": "HAQQ Legal AI and the Beirut Bar Association announce a formal partnership providing all BBA members access to Louis at a reduced tier, with dedicated Arabic-language support.",
  "published_at": "2025-04-15T09:00:00Z",
  "language": "EN",
  "arabic_available": true,
  "source_url": "https://louis.law/press/bba-partnership",
  "contact": "press@haqq.ai",
  "is_pinned": false
}
```

## Quality bar

- **Exact attribution**: press releases must be verbatim from official source. AI summaries are permitted for in-feed display but must clearly link to the full original.
- **No embellishment**: the summary must not add claims not present in the original release.
- **Sensitive communications**: regulatory statements and crisis communications should be reviewed by a human editor before publishing to the feed, even if the content is already public.
- **Bilingual accuracy**: Arabic versions must be official translations, not AI-translated versions of the English release, unless explicitly labeled as such.

## Failure modes

- **PR source unavailable**: cache the last known set of releases. The press feed is low-velocity; weekly cache is acceptable.
- **No new releases in 60+ days**: surface an "About Louis" card (key facts, mission statement) as a placeholder to avoid an empty section.
- **Third-party publication links**: if a press release references a third-party article, link to the third-party but verify the link is live before surfacing.

## Related skills

- [[feed-changelog-watcher]]
- [[feed-status-incident-watcher]]
- [[feed-blog-rss]]
- [[growth-case-study-asker]]
