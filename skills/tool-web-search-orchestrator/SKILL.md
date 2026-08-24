---
name: tool-web-search-orchestrator
description: Use when legal research requires freshness that pre-indexed corpora cannot provide — recent statutory amendments, new regulator circulars, court decisions from the last 6 months, or breaking regulatory announcements. Batches multiple sub-queries into a single orchestrated call, prioritizes official government and regulator sources, and enforces the source allowlist to prevent hallucination from low-quality results. Never invoked for generic legal concepts or boilerplate generation.
license: MIT
metadata: " id: tool.web-search-orchestrator category: tool priority: P0 intent: [web-search, fresh-research, regulatory-updates, statute-currency] related: [tool-web-search-source-allowlist, tool-legal-data-hunter, tool-rag-public-legal-corpus, tool-legifrance-fr, tool-lexisnexis] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'tool'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Tool — Web Search Orchestrator

## What it does

The Web Search Orchestrator manages outbound web queries for legal research tasks where the pre-indexed corpora (firm KB, public legal corpus) do not have current information. It enforces a source allowlist, batches multiple sub-queries efficiently, and returns structured results with provenance so that downstream analysis can cite sources accurately.

This is the tool that asks: "Is this question about a recent change that my training data or pre-indexed corpus might have missed?" If yes, it goes to the web.

## When to invoke

### Invoke when:
- **Freshness required**: the question is about a regulatory change, court decision, or law amendment from the last 6–12 months
- **Official current text needed**: the user needs the current version of a regulation or statute that may have been amended recently
- **Regulator bulletin**: SAMA circular, CBUAE guidance note, DFSA consultation paper, SDAI decision — published in the last year
- **Breaking news with legal implications**: a major court judgment, a legislative development, a sanctions designation just announced
- **The local KB is silent**: neither firm KB, personal KB, nor the public legal corpus returned a relevant result

### Do not invoke for:
- Statute text that is well-established and unlikely to have changed (use [[tool-rag-public-legal-corpus]] or [[tool-legifrance-fr]])
- Generic legal concepts (limitation periods, consideration, force majeure) — the model already knows these
- Boilerplate clause drafting — no web access needed
- Queries the firm KB already answered comprehensively
- Fact-finding that requires accessing paywalled content (Westlaw, LexisNexis) — use those tools directly

## Source allowlist

The orchestrator enforces a strict source priority hierarchy. Sources are only queried or returned if they fall within the allowlist defined per tenant ([[tool-web-search-source-allowlist]]):

### Tier 1 — Official primary sources (highest authority)
- **Official Gazettes**: Umm Al-Qura (KSA — https://www.uqn.gov.sa), UAE Federal Gazette (https://moj.gov.ae/ar/legislations), Journal Officiel (France — via Legifrance), al-Jarida al-Rasmiyya (Lebanon), Official Gazette of Egypt
- **Court databases**: DIFC Courts (difccourts.ae), ADGM Courts (adgmcourts.com), BAILII (UK), CourtListener (US), EUR-Lex (EU)
- **Regulator websites**: SAMA (sama.gov.sa), CBUAE (centralbank.ae), BDL (bdl.gov.lb), CMA (cma.org.sa), SDAIA (sdaia.gov.sa), DFSA (dfsa.ae), FSRA (fsra.adgm.com), DIFC (difc.ae), ADGM (adgm.com)

### Tier 2 — Established legal publishers
- Practical Law (UK/Int'l) — uk.practicallaw.thomsonreuters.com
- LexisNexis news and analysis — www.lexisnexis.com
- IFLR (International Financial Law Review)
- Kluwer Arbitration Blog
- Out-Law (Pinsent Masons legal news)
- AL-Bayan Legal (Arabic-language legal analysis)
- Financier Worldwide
- Bloomberg Law News
- Law Society Gazette (UK)

### Tier 3 — Bar associations and professional bodies
- Law Society of England and Wales
- American Bar Association
- DIFC Dispute Resolution Authority
- Saudi Bar Association

### Tier 4 — Secondary / commentary (verify with primary)
- Major law firm client alerts (Clifford Chance, Freshfields, Al Tamimi, Baker McKenzie, Hadef & Partners, Dentons, etc.)
- Academic institutions' legal research blogs (Harvard Law Review, Oxford Human Rights Hub)

### Never use as primary source:
- Wikipedia — wrong for legal authority
- Reddit / legal forums — unverifiable
- News aggregators (Google News snippets, Yahoo News) — not primary
- LinkedIn posts — not authoritative

## Batching logic

Efficient web search batches related sub-queries:

```
User: "What are the latest UAE cybercrime law amendments and TDRA guidance?"

Decompose to:
  sub-query 1: "UAE Federal Decree-Law cybercrime amendments 2024 2025" → site:moj.gov.ae OR site:tdra.gov.ae
  sub-query 2: "TDRA UAE cybersecurity guidance circular 2024" → site:tdra.gov.ae
  sub-query 3: "UAE cybercrime law enforcement cases 2024" → site:adgmcourts.com OR site:difccourts.ae

Execute all 3 in parallel → merge results → deduplicate → rank
```

Maximum sub-queries per orchestrated call: 6. Beyond 6, apply iterative round — run the most important 6, evaluate gaps, then run the next round.

## Capabilities

### Structured query execution
```
Input:  {
  queries: [
    { q: "SAMA AML circular 2025", sites: ["sama.gov.sa"], dateFrom: "2025-01-01" },
    { q: "SAMA AML penalties enforcement", sites: ["sama.gov.sa", "out-law.com"] }
  ],
  jurisdiction: "KSA"
}
Output: {
  results: [
    {
      url, title, snippet, datePublished,
      sourceType: "regulator" | "court" | "publisher" | "bar" | "secondary",
      sourceTier: 1 | 2 | 3 | 4,
      relevanceScore: 0.88
    }
  ]
}
```

### Gazette scraping
For MENA official gazettes, the orchestrator can extract recent legislative instruments:
```
Input:  { gazette: "umm-al-qura", dateFrom: "2025-01-01", topic: "company law" }
Output: [ { title, issuedDate, arabicText, summary } ]
```

### Regulator bulletin feed
For regulators that publish RSS feeds or structured announcement pages:
```
Input:  { regulator: "cbuae", since: "2025-06-01" }
Output: [ { title, date, url, type: "circular" | "guidance" | "press_release" } ]
```

## Output format

Per result returned:
```json
{
  "url": "https://www.sama.gov.sa/...",
  "title": "SAMA AML/CFT Annual Progress Report 2024",
  "snippet": "...",
  "datePublished": "2025-03-15",
  "sourceType": "regulator",
  "sourceTier": 1,
  "relevanceScore": 0.91,
  "language": "ar",
  "translationRequired": true,
  "verifiedPrimary": true
}
```

The `verifiedPrimary` flag is set to `true` when the result is from a Tier 1 source (official government or regulator) and the URL directly matches the expected domain.

## Anti-patterns

| Anti-pattern | Why it's wrong |
|---|---|
| Citing Wikipedia for a statute | Wikipedia is not a primary source; statutes must come from official gazettes or Legifrance |
| Using news aggregator snippets as legal authority | News snippets are second-hand; always trace to the primary source |
| Forums as legal authority | Unverifiable; legally irrelevant |
| Not checking date | A result from 3 years ago may be superseded; always report and check `datePublished` |
| Accepting paywalled content snippet as full analysis | The snippet may not reflect the full picture; note truncation |

## Failure modes

| Failure | Symptom | Resolution |
|---------|---------|------------|
| No Tier 1 results | All results from Tier 3–4 only | Flag to user; primary source may not be indexed online |
| Outdated results | All results > 18 months old | Flag; report gap; recommend direct regulator contact |
| Arabic-only source | Result is Arabic text, no English | Flag; route to [[tool-ocr-arabic]] or translation if critical |
| CAPTCHA / bot detection | Web request blocked | Retry with backoff; route to official API if available |
| Paywalled result | 403 or login wall | Skip; report URL to user for manual access |

## Related skills

- [[tool-web-search-source-allowlist]] — per-tenant configuration of trusted source domains
- [[tool-legal-data-hunter]] — orchestrator that calls this tool plus database tools
- [[tool-rag-public-legal-corpus]] — pre-indexed corpus; check here before invoking web search
- [[tool-legifrance-fr]] — direct official API for French law (preferred over web scraping)
- [[tool-lexisnexis]] — premium database with more complete content than web search for supported jurisdictions
