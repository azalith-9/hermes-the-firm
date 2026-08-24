---
name: tool-rag-public-legal-corpus
description: Use when retrieving from the indexed corpus of public legal texts — court judgments (DIFC, ADGM, UK, US, EU), statutes, official gazettes, and regulatory instruments — to support legal research, precedent finding, or statute verification. Organized as per-jurisdiction indexes. Lower precedence than firm KB and personal KB; complements premium databases. Best for DIFC/ADGM case law, GCC statutes, and curated public corpora not fully covered by Westlaw or LexisNexis.
license: MIT
metadata: " id: tool.RAG-public-legal-corpus category: tool jurisdictions: [__multi__] priority: P2 intent: [public-corpus, legal-research, statute-lookup, case-law, rag-retrieval] related: [tool-rag-firm-knowledge, tool-rag-personal-knowledge, tool-lexisnexis, tool-thomson-reuters-westlaw, tool-legifrance-fr, tool-legal-data-hunter] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'tool'.
Namespaced as louis-<category>-<skill> on registration.
-->


# RAG — Public Legal Corpus

## What it does

This tool retrieves from a curated, pre-indexed corpus of public legal texts organized into per-jurisdiction indexes. Unlike live database queries (Westlaw, LexisNexis), this corpus is pre-processed and embedded for fast semantic retrieval — trading real-time currency for speed and cost efficiency.

The public legal corpus is the default research layer when:
- Premium database credentials are not configured for the tenant
- The query is about well-established statutory provisions unlikely to have changed recently
- The jurisdiction is a MENA court system better covered by this corpus than by Westlaw/LexisNexis
- The user needs quick retrieval during drafting without a full research query

## Corpus structure

### Per-jurisdiction indexes

| Jurisdiction | Content | Currency |
|---|---|---|
| DIFC | All DIFC Laws, DIFC Courts judgments (Court of First Instance + Court of Appeal + DIFC Arbitration Institute), DIFC Authority regulations | Updated quarterly |
| ADGM | ADGM Acts, ADGM Courts judgments, FSRA regulations, ADGM Registrar guidance | Updated quarterly |
| UAE (onshore) | UAE Federal Laws (Commercial Companies Law, Civil Transactions Law, Commercial Code), CBUAE circulars, DED guidance | Updated semi-annually |
| KSA | Saudi Company Law, Saudi Civil Transactions Law, SAMA circulars, CMA regulations, MOC guidance | Updated semi-annually |
| LB | Lebanese Code of Commerce, Code of Obligations and Contracts, BDL circulars, selected Court of Cassation judgments | Updated annually |
| EG | Egyptian Civil Code, Egyptian Commercial Companies Law, EFSA regulations | Updated annually |
| UK | Selected House of Lords / Supreme Court judgments, key CA decisions (particularly arbitration, contract, company law) | Updated quarterly |
| US | SCOTUS opinions, selected federal circuit court opinions, major securities law cases | Updated quarterly |
| EU | CJEU opinions on jurisdiction, data protection (GDPR), competition | Updated quarterly |
| FR | Code civil (consolidated), Code de commerce, selected Cassation judgments | Updated semi-annually via Legifrance |
| GCC | GCC Secretariat instruments, uniform GCC laws | Updated annually |

### Document types indexed
- Court judgments (full text where available, summary where full text is restricted)
- Statutory texts (consolidated, with version dates)
- Regulatory instruments (circulars, guidance notes, rulebooks)
- Official gazette publications (for recent statutory instruments)
- Selected academic commentary (law review articles on MENA law, DIFC/ADGM practitioners' guides)

## Retrieval precedence

| Priority | Source | Use when |
|----------|--------|---------|
| 1 | Firm KB ([[tool-rag-firm-knowledge]]) | Firm-specific precedent exists |
| 2 | Personal KB ([[tool-rag-personal-knowledge]]) | User's personal uploaded documents |
| 3 | Live database (Westlaw / LexisNexis) | Real-time currency needed; credentials available |
| 4 | **This tool — Public corpus** | Default; no credentials or speed/cost priority |
| 5 | Web search | Freshness needed beyond corpus currency |

## Capabilities

### Semantic search
```
Input:  {
  query: "DIFC Court approach to liquidated damages clauses",
  jurisdiction: "DIFC",
  documentTypes: ["case_law"]
}
Output: [
  {
    title, court, date, citation,
    snippet, similarity, url,
    fullTextAvailable: bool
  }
]
```

### Statute lookup (exact article)
```
Input:  {
  articleRef: "Article 58 DIFC Contract Law",
  jurisdiction: "DIFC"
}
Output: { text, version, effectiveDate, consolidationDate }
```

### Parallel statute comparison
```
Input:  {
  topic: "force majeure definition",
  jurisdictions: ["DIFC", "UAE-onshore", "KSA", "LB"]
}
Output: { comparison: [{ jurisdiction, articleRef, text }] }
```

## Currency and staleness

**Important limitation**: this corpus is periodically refreshed, not real-time. Currency varies by jurisdiction and document type. For:
- Recent cases (< 6 months): use live database or web search
- Recent regulatory circulars (< 12 months): use web search (site:cbuae.gov.ae, site:sama.gov.sa, etc.)
- Emergency legislation / COVID-era decrees: verify against official gazette

Every result is tagged with `corpusDate` — the date this document was last ingested. If `corpusDate` is more than 12 months ago for a fast-moving area (fintech, crypto, AI regulation), flag for verification.

## Citations

Retrieved corpus passages are cited as:
- For case law: standard legal citation format (e.g., `[2021] DIFC CFI 034`)
- For statutes: article reference + version date (e.g., `DIFC Contract Law, Art. 58, as of 2023`)
- For regulatory instruments: `[Corpus: CBUAE Circular 2023/01]` with corpus ingestion date

Always distinguish corpus-retrieved citations from live-database-retrieved citations in the output — the former may not reflect the most current version.

## Output schema

```json
{
  "results": [
    {
      "title": "Al Khorafi v. Bank Sarasin-Alpen (ME) Ltd",
      "citation": "[2011] DIFC CA 001",
      "court": "DIFC Court of Appeal",
      "date": "2011-04-15",
      "jurisdiction": "DIFC",
      "documentType": "case_law",
      "snippet": "...",
      "similarity": 0.88,
      "corpusDate": "2024-10-01",
      "fullTextAvailable": true,
      "url": "https://difccourts.ae/..."
    }
  ],
  "totalResults": 5,
  "corpusCurrencyWarning": null,
  "queryTimestamp": "2026-05-14T10:00:00Z"
}
```

## Related skills

- [[tool-rag-firm-knowledge]] — firm KB; higher precedence
- [[tool-rag-personal-knowledge]] — user personal KB; higher precedence
- [[tool-lexisnexis]] — live premium database; higher precedence when credentialed
- [[tool-thomson-reuters-westlaw]] — live premium database for US/UK/AU
- [[tool-legifrance-fr]] — live official French text; more current than corpus for FR
- [[tool-legal-data-hunter]] — orchestrator that combines this and other sources
