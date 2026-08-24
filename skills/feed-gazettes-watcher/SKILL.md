---
name: feed-gazettes-watcher
description: Use when the platform needs to monitor official government gazettes across MENA jurisdictions (UAE, KSA, Lebanon, Egypt, Qatar, Bahrain, Kuwait, Oman) and surface newly enacted legislation, royal decrees, ministerial decisions, and regulatory circulars to users based on their practice area and jurisdiction settings. This is the primary legislative-monitoring feed for legal practitioners who need to catch law changes before they affect client matters.
license: MIT
metadata: " id: feed.gazettes-watcher category: feed jurisdictions: [UAE, KSA, LB, EG, QA, BH, KW, OM, DIFC, ADGM, GCC] priority: P3 intent: [__feed__, gazette-monitoring, legislation-watch, regulatory-change, MENA] related: [feed-regulator-bulletins-mena, feed-case-law-new-publications, feed-legal-news-mena, feed-changelog-watcher, kb-commercial-companies-mena] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'feed'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Gazettes Watcher Feed Surface

## Purpose

Official government gazettes are the authoritative source of enacted law in all MENA jurisdictions. A new law or royal decree does not exist — legally — until published in the official gazette. This feed surface monitors these sources continuously and alerts practitioners the moment a relevant legislative instrument is published.

For transactional lawyers, the gazettes watcher is a critical risk-management tool: a law change between signing and closing an M&A deal, or between drafting and executing a contract, can invalidate assumptions baked into the document. For in-house counsel, it drives the regulatory calendar.

## Monitored gazette sources

### UAE
- **Al-Jarida al-Rasmiya** (UAE Official Gazette) — federal laws, decrees, regulations
- Dubai Official Gazette — emirate-level regulations
- Abu Dhabi Official Gazette — emirate-level
- **DIFC Gazette** — laws, regulations, amendments by the DIFC Authority
- **ADGM Gazette** — ADGM Founding Law instruments, regulations

### KSA
- **Umm al-Qura** — official gazette; laws, royal decrees (marasim malakiya), ministerial decisions
- SAMA circulars (Central Bank — financial regulation)
- Capital Market Authority (CMA) announcements

### Lebanon
- **Al-Jarida al-Rasmiya** (Lebanese Official Gazette) — laws enacted by Parliament, legislative decrees, ministerial decisions
- Banque du Liban (BDL) circulars — banking and financial regulation

### Egypt
- **Al-Jarida Al-Rasmiya** (Official Gazette) — laws, presidential decrees, ministerial decisions
- Financial Regulatory Authority (FRA) bulletins
- Central Bank of Egypt (CBE) circulars

### Other GCC
- Qatar Official Gazette (Al-Jarida Al-Rasmiya)
- Bahrain Official Gazette
- Kuwait Official Gazette (Al-Kuwait Al-Youm)
- Oman Official Gazette (Al-Jarida Al-Rasmiya)

### International secondary
- EU Official Journal (OJEU) — for EU-related or EU-incorporated-party matters
- UK Statutory Instruments — for DIFC/ADGM common-law developments and UK-nexus transactions

## Personalization logic

1. **Jurisdiction filter**: monitor only the user's active jurisdiction set. Users with "GCC" in their profile get all GCC gazettes.
2. **Practice-area tagging**: each gazette item is tagged by subject matter using NLP classification (company law, employment, tax, IP, real estate, banking, arbitration, data protection, etc.). Surface only items matching user's practice areas.
3. **Significance scoring**: royal decrees and primary legislation score higher than ministerial circulars. New laws score higher than amendments.
4. **Impact assessment**: for items scoring "high significance," generate a 3-sentence impact note: what changed, who is affected, and what action may be required.
5. **Matter-level matching**: cross-reference gazette items against open matters. If a new decree affects the governing law of an active matter, generate a priority alert.

## Output spec

```json
{
  "id": "gazette-item-uuid",
  "source": "UAE Official Gazette",
  "instrument_type": "federal-law",
  "reference": "Federal Decree-Law No. 32 of 2021 (as amended)",
  "title": "On Commercial Companies",
  "jurisdiction": "UAE",
  "published_date": "2025-05-08",
  "effective_date": "2025-06-01",
  "subject_tags": ["corporate", "commercial-companies", "governance"],
  "significance": "high",
  "impact_note": "Amends share pledge provisions for onshore LLCs. Practitioners advising on UAE LLC financing should review pledge documentation against new requirements before closing.",
  "source_url": "https://...",
  "full_text_available": true,
  "relevance_score": 0.94
}
```

## Significance tiers

| Tier | Criteria | Alert mode |
|---|---|---|
| Critical | New primary law or major amendment; immediate client impact | In-app alert + email |
| High | Regulatory instrument; affects compliance obligations | Feed item with impact note |
| Medium | Ministerial circular; procedural change | Feed item, standard priority |
| Low | Administrative notice; no material legal change | Feed item, low visibility |

## Quality bar

- Never summarize a gazette item beyond what is stated in the published instrument. Do not characterize intent or predict application.
- Effective-date accuracy is critical — clearly distinguish publication date from effective date (laws frequently have delayed commencement provisions).
- Flag where an effective date is not stated (some instruments are effective immediately upon publication).
- Mark Arabic-only instruments as "Arabic original — AI-assisted summary; verify translation."

## Failure modes

- **Gazette source offline**: use cached last-known state; flag as "data as of [last pull date]." Do not show stale items without date disclosure.
- **Gazette format change** (common with government sources): flag the source as "parsing error — manual review required" in ops dashboard.
- **No matching items**: surface a "No new legislative activity in your jurisdiction this period" message rather than an empty section.
- **Duplicate instruments**: some items are published in both federal and emirate gazettes. Deduplication logic must check reference number + date, not title.

## Related skills

- [[feed-regulator-bulletins-mena]]
- [[feed-case-law-new-publications]]
- [[feed-legal-news-mena]]
- [[kb-commercial-companies-mena]]
- [[heuristic-always-state-jurisdiction-first]]
