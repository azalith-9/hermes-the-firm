---
name: feed-legal-news-mena
description: Use when the platform needs to surface curated legal and business news from MENA jurisdictions (UAE, KSA, Lebanon, Egypt, Qatar, Bahrain, Kuwait, Oman, plus DIFC and ADGM) into the user's feed. Aggregates news from regional legal publications, law firm alerts, and business media, filtered by practice area and jurisdiction. The primary awareness feed for MENA-focused practitioners who need to track the regional legal and regulatory environment without scanning multiple sources manually.
license: MIT
metadata: " id: feed.legal-news-MENA category: feed jurisdictions: [UAE, KSA, LB, EG, QA, BH, KW, OM, DIFC, ADGM, GCC, MENA] priority: P3 intent: [__feed__, legal-news, MENA, regional-monitoring, practice-area-watch] related: [feed-gazettes-watcher, feed-regulator-bulletins-mena, feed-case-law-new-publications, feed-blog-rss, ops-churn-risk-detector] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'feed'.
Registered as a flat plugin skill.
-->


# Legal News MENA Feed Surface

## Purpose

The legal news MENA feed is the broadest awareness surface in the Louis feed panel. Where the gazettes watcher tracks formal legislative instruments and the regulator bulletins feed tracks official regulatory communications, this feed covers the full landscape of legal and legal-adjacent news: court system reforms, bar association news, legal tech adoption, M&A deal activity, regulatory policy debates, and business news with direct legal implications.

This feed is particularly valuable for:
- **Transactional lawyers** monitoring deal activity and regulatory signals that affect their sector.
- **In-house counsel** tracking legal reform debates and regulatory posture shifts before they become binding law.
- **Legal tech practitioners** following the evolving AI-in-law landscape across MENA.
- **Junior associates and paralegals** building regional legal knowledge through a curated, structured feed.

## Monitored news sources

### MENA-specific legal press
- **Al-Tamimi & Company** client alerts and publications
- **Lexology** MENA legal commentary
- **Mondaq** MENA law category
- **Construction Law ME**, **IP ME**, **Finance Middle East** (sector-specific MENA legal)
- **Arab Monetary Fund** legal and financial publications
- **Gulf Business Law** and similar regional legal trade publications
- **Zawya** (business news with regulatory/legal feed) — GCC

### Arabic-language legal sources
- Al-Qanun Al-Duali (international law commentary in Arabic)
- Bar association newsletters (Beirut, Dubai, Abu Dhabi, Riyadh)
- Majles Al-Dawla (Lebanon State Council publications)

### International sources with MENA coverage
- **Law360** international/Middle East desk
- **Global Arbitration Review** (MENA arbitration coverage)
- **IFLR** (International Financial Law Review) — Gulf finance
- **PLC Cross-border** (relevant for DIFC/ADGM common-law developments)

## News categories and tagging

Each item is tagged with one primary category and optionally one or more secondary categories:

| Category | Examples |
|---|---|
| Legislation & regulation | New law passed, amendment tabled, ministerial consultation |
| Court system & judiciary | New appointment, procedural reform, court digitization initiative |
| Arbitration & ADR | New arbitration center, rule amendments, landmark award |
| Corporate & M&A | Deal announced/closed, merger review, shareholder dispute |
| Banking & finance | Central bank circular, Basel implementation, crypto regulation |
| Employment & labor | Labor law reform, visa changes, Saudization/Emiratization |
| Real estate | Freehold expansion, RERA regulation, strata law |
| IP & technology | Patent office news, AI regulation, data protection |
| Litigation | Landmark judgment reported in press, enforcement news |
| Legal tech | AI regulation debate, e-court adoption, blockchain contracts |

## Personalization logic

1. **Jurisdiction relevance**: items tagged to a jurisdiction must match the user's active jurisdictions. Pan-GCC or MENA-wide items are shown to any user with at least one GCC jurisdiction active.
2. **Practice-area priority**: items matching the user's primary practice area get boosted relevance score. Items from adjacent areas appear at lower priority. Items outside the user's practice profile are suppressed unless they are "must-know" significance.
3. **Language filter**: surface English-language items by default. If user has Arabic preference, prioritize Arabic-language items and supplement with English where Arabic is unavailable.
4. **Freshness**: items older than 7 days receive a significant freshness penalty. Breaking news (< 24 hours) is boosted.
5. **Deduplication**: many MENA legal news items are syndicated across Lexology, Mondaq, and law firm websites. Deduplicate by URL normalization and headline similarity.
6. **Churn-risk boost**: for users with `churn_risk_score > 0.7`, prioritize high-engagement items (M&A deal news, major regulatory changes) that are likely to spark a legal research or drafting session.

## Output spec

```json
{
  "id": "news-item-uuid",
  "source": "Al-Tamimi & Company",
  "title": "UAE Data Protection Law: DIFC and Mainland Compared",
  "summary": "...", // 2-3 sentence AI-generated neutral summary
  "published_at": "2025-05-13T07:30:00Z",
  "jurisdiction_tags": ["UAE", "DIFC"],
  "category": "IP & technology",
  "secondary_categories": ["legislation"],
  "language": "EN",
  "read_time_minutes": 4,
  "significance": "high",
  "source_url": "https://...",
  "relevance_score": 0.88,
  "is_bookmarked": false
}
```

## Significance scoring

| Score | Rationale |
|---|---|
| High | Major law change, landmark judgment, GCC-wide regulatory shift |
| Medium | Important sector development, substantive policy signal |
| Low | Routine deal announcement, procedural update, conference notice |

## Quality bar

- AI-generated summaries must neutrally represent the article. Do not characterize a bill as "likely to pass" or a policy as "likely to cause problems" unless the source makes that characterization.
- News items are not primary sources — they report on primary sources. Do not treat a news summary as legal authority. The feed is for awareness, not advice.
- Flag opinion/commentary pieces distinctly from news reporting, as the two carry different epistemic weight.

## Failure modes

- **Source unavailable**: fall back to cached items from last successful pull, capped at 14 days old.
- **Feed overload**: if > 20 items would be surfaced in one day for a user, apply a hard cap and queue the remainder for the next day.
- **Paywall-only item**: surface title, source, and date; mark as "Subscription required"; do not attempt to summarize content behind the paywall.

## Related skills

- [[feed-gazettes-watcher]]
- [[feed-regulator-bulletins-mena]]
- [[feed-case-law-new-publications]]
- [[feed-blog-rss]]
- [[ops-churn-risk-detector]]
