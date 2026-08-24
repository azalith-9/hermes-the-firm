---
name: feed-case-law-new-publications
description: Use when the platform needs to surface newly published court decisions, tribunal awards, and appellate judgments relevant to a user's practice area and jurisdictions. Monitors official court gazettes, legal databases, and open-access repositories across MENA (UAE, KSA, Lebanon, Egypt), DIFC, ADGM, and secondary jurisdictions (UK, EU, FR) to alert practitioners to case law that may affect pending matters or established positions.
license: MIT
metadata: " id: feed.case-law-new-publications category: feed jurisdictions: [LB, KSA, UAE, DIFC, ADGM, EG, FR, UK, EU] priority: P3 intent: [__feed__, case-law-monitoring, jurisdiction-watch, legal-research] related: [feed-gazettes-watcher, feed-regulator-bulletins-mena, feed-legal-news-mena, ops-churn-risk-detector, kb-litigation-mena] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'feed'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Case Law New Publications Feed

## Purpose

This feed surface monitors official and semi-official sources for newly published court decisions and arbitral awards across the user's active jurisdictions, then delivers them as structured, summarized items in the Louis feed panel.

For practicing lawyers and in-house counsel, staying current on case law is a core professional obligation. This surface removes the manual labor of visiting multiple court portals and reduces the risk that a practitioner misses a decision that overturns a position they have relied on.

## Monitored sources by jurisdiction

### UAE (federal + emirate)
- Federal Supreme Court (Mahkama al-Ittihaddiya al-Ulya) published decisions
- Dubai Court of Cassation (Mahkamat al-Naqd) case summaries
- Abu Dhabi judicial summaries (where publicly released)
- Ministry of Justice case database (where accessible)

### DIFC / ADGM
- DIFC Courts Judgments database (publicly available at difccourts.ae)
- ADGM Courts Judgments (adgmcourts.com)
- DIFC-LCIA (now DIAC) published awards (where parties consent to publication)

### KSA
- Board of Grievances (Diwan al-Mazalim) summaries
- Labor Courts published decisions
- Saudi Center for Commercial Arbitration (SCCA) published awards

### Lebanon
- Court of Cassation (Mahkamat al-Tamyiz) published decisions via Adel database
- Court of Appeals commercial decisions
- Arbitration Centre of Lebanon (ACL) awards (where published)

### Egypt
- Court of Cassation decisions (published via Egyptian Knowledge Bank / EKB)
- Cairo Regional Centre for International Commercial Arbitration (CRCICA) awards

### International / secondary
- UK Supreme Court and Court of Appeal decisions (relevant for DIFC/ADGM common-law development)
- European Court of Justice (ECJ) decisions (relevant for EU-connected matters)
- ICC, LCIA, DIAC, ICSID published awards (redacted versions)

## Personalization logic

1. **Jurisdiction filter**: only surface decisions from courts/tribunals in the user's active jurisdiction list.
2. **Practice-area tagging**: decisions are tagged by practice area (contract, tort, employment, IP, real estate, corporate). Filter to user's primary and secondary practice areas.
3. **Matter relevance**: if the user has active matters, run lightweight keyword match against case subject matter; boost relevance score for hits.
4. **Overruling alert** (high priority): if a decision expressly overrules or distinguishes a prior decision that was previously surfaced to this user, flag with an "Overruling — review required" label.
5. **Recency**: decisions published within 30 days receive full visibility; 30–90 days with freshness decay; beyond 90 days only if matched to active matter.

## Output spec

```json
{
  "id": "case-feed-uuid",
  "court": "DIFC Courts — Court of First Instance",
  "case_reference": "CFI-2025-00142",
  "decided_date": "2025-04-28",
  "published_date": "2025-05-10",
  "parties": "Redacted / [Company A] v [Company B]",
  "subject_tags": ["commercial contract", "force majeure", "governing law"],
  "jurisdiction": "DIFC",
  "practice_areas": ["commercial", "litigation"],
  "summary": "...", // AI-generated 3-5 sentence neutral summary
  "significance": "high | medium | low",
  "overruling_flag": false,
  "source_url": "https://...",
  "relevance_score": 0.91
}
```

## Significance scoring

| Score | Criteria |
|---|---|
| High | Overrules or significantly qualifies prior authority; Supreme Court / Court of Cassation level; novel issue |
| Medium | Appellate level; applies established principle to new fact pattern; useful as precedent |
| Low | First-instance; routine application; useful for research but no headline shift |

## Quality bar

- AI summaries must be neutral and attribution-accurate. Do not characterize a decision as establishing a rule unless the court's language supports that characterization.
- Never fabricate case references. If a source provides a reference number, reproduce it exactly; if not, mark as "reference not published."
- Flag decisions where English summary is AI-translated from Arabic — always note "AI translation from Arabic; verify original."

## Failure modes

- **Source unavailable**: mark the source as "temporarily unavailable" and use cached data from last successful pull. Alert the ops team if a source is down > 48 hours.
- **No decisions matching user profile**: widen to jurisdiction-only filter (drop practice area filter) and surface top 5 most-significant decisions from the period.
- **Paywalled content**: surface title, court, date, and reference only; mark as "full text requires subscription."

## Related skills

- [[feed-gazettes-watcher]]
- [[feed-regulator-bulletins-mena]]
- [[feed-legal-news-mena]]
- [[ops-churn-risk-detector]]
- [[kb-litigation-mena]]
