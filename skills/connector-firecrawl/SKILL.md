---
name: connector-firecrawl
description: Use when a legal-AI workflow needs to convert any publicly accessible URL into clean, LLM-ready markdown — for example, to retrieve a regulatory authority's latest guidance, a court's published judgment, a government gazette notice, or a law firm's published article for research or analysis. Requires a per-tenant Firecrawl API key. Triggers on any request to read or summarize a web page, scrape a regulatory site, or ingest an external URL as context for legal analysis.
license: MIT
metadata: " id: connector.firecrawl category: connector jurisdictions: [__multi__] priority: P2 intent: [__connector__] related: [connector-eur-lex, connector-legifrance, connector-legal-data-hunter, connector-companies-house-uk] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'connector'.
Registered as a flat plugin skill.
-->


# Connector — Firecrawl

## What it does

Firecrawl is a web-scraping and content-extraction service that converts any URL — including JavaScript-rendered pages — into clean markdown suitable for LLM processing. In a legal-AI context, it serves as the general-purpose web-content ingestion layer when no structured API connector exists for a particular source.

Core capabilities:
- Converts a single URL to markdown (stripping navigation, ads, and boilerplate).
- Crawls multi-page documentation or regulation sites with configurable depth.
- Extracts structured data from HTML tables (e.g., fee schedules, sanctions lists in HTML format).
- Handles JavaScript-rendered pages (single-page apps, dynamic government portals).

## Setup / auth

Authentication uses a **per-tenant Firecrawl API key**:
- Obtained from the Firecrawl dashboard (`firecrawl.dev`).
- Stored in the platform's secrets manager under the tenant's configuration.
- Key is passed as a Bearer token in the `Authorization` header.
- Rate limits depend on the plan; legal-use volumes are typically within the standard plan.

Each tenant has their own API key to ensure usage tracking and cost isolation. Never share a Firecrawl API key across tenants.

## Capabilities

| Capability | Notes |
|---|---|
| Single URL to markdown | Core function; strips boilerplate; returns clean text |
| JavaScript-rendered pages | Headless browser rendering; handles SPAs |
| Crawl (multi-page) | Configurable depth and domain scope |
| HTML table extraction | Returns tables as markdown or JSON |
| PDF URL to markdown | Downloads and extracts text from PDFs linked at the URL |
| Screenshot of page | Returns a PNG of the rendered page |
| Structured data extraction | With a schema, returns JSON matching the schema from page content |

## Usage patterns

### Pattern 1 — Regulatory guidance retrieval

```
User: "Get the latest DIFC DIFCA circular on AML requirements"
→ Connector scrapes the DIFCA website for the relevant circular URL
→ Firecrawl converts the page to clean markdown
→ Returns the circular text as context for analysis or citation
```

### Pattern 2 — Government gazette monitoring

Many MENA government decisions are published in official gazettes (e.g., UAE Official Gazette, Saudi Umm al-Qura, Lebanese Official Journal) which do not have structured APIs:
- Use Firecrawl to retrieve the latest gazette issue from the official URL.
- Extract relevant notices (new laws, ministerial decisions, court rule amendments).
- Surface changes relevant to matters currently in the work queue.

### Pattern 3 — Counterparty website for due diligence context

Before a client meeting or due-diligence review, scrape the counterparty's corporate website to extract:
- Business description and sector.
- Key management team.
- Publicly disclosed subsidiaries or affiliates.
- Any red flags in published materials (sanctions disclosures, litigation mentions).

Note: website content is marketing material — treat it as orientation, not verified fact.

### Pattern 4 — Case law from court publication portals

Some MENA courts publish judgments on their websites (e.g., DIFC Courts Case Register, Abu Dhabi courts). Use Firecrawl to retrieve judgment text where no structured API exists:
- Provide the judgment URL.
- Return clean markdown for analysis.
- Cross-reference the judgment details with [[connector-legal-data-hunter]] for MENA-specific structuring.

### Pattern 5 — Monitoring a regulatory authority for updates

Set up a scheduled crawl (via [[connector-scheduled-tasks]]) to check a regulatory authority's "news" or "publications" page periodically and alert the relevant matter team when new content appears that matches monitored keywords.

## What Firecrawl does NOT do

- **No login-walled content.** Firecrawl cannot authenticate to sites requiring a username/password. Use dedicated authenticated connectors (e.g., [[connector-legifrance]] for French law, [[connector-eur-lex]] for EU law).
- **No Westlaw / LexisNexis.** These are paywalled and have terms of service prohibiting scraping.
- **No PACER.** US federal court filings (PACER) require a registered account and separate integration.
- **No real-time data.** Firecrawl captures a snapshot; for live-updating data (e.g., share prices, live sanctions lists), use purpose-built connectors.

## Jurisdictional relevance for MENA practice

| Source type | Availability via Firecrawl | Notes |
|---|---|---|
| UAE Federal laws portal (moj.gov.ae) | Good | Some pages JS-rendered; Firecrawl handles this |
| DIFC Courts (difccourts.ae) | Good | Judgment register publicly accessible |
| Lebanon Official Journal (gazetteofficielle.gov.lb) | Partial | Arabic/French; occasional PDF-only editions |
| KSA Umm al-Qura (uqn.gov.sa) | Good | Arabic; Firecrawl returns Arabic markdown |
| ADGM legal resources (adgm.com) | Good | English; well-structured HTML |
| Egypt Official Gazette (vetogate.com mirrors) | Partial | Official site inconsistent; use mirrors carefully |

When returning content from Arabic-language sources, preserve the Arabic text in the markdown output — do not silently transliterate or omit Arabic characters.

## Permissions & safety

- **Respect robots.txt.** Firecrawl respects `robots.txt` by default. Do not override this for government or court sites.
- **No credential-passing.** Never pass authentication tokens or session cookies to Firecrawl — the content will transit Firecrawl's infrastructure.
- **Rate limiting.** For periodic crawls of the same site, add a minimum 60-second delay between requests to avoid overloading government web servers.
- **Content accuracy.** Scraped content must be cited with the source URL and retrieval date. Never present scraped regulatory text as definitively current without noting the retrieval timestamp.
- **PII in scraped content.** If a scrape returns pages containing personal information (e.g., a court judgment with an individual's name and address), handle as PII — do not store beyond the immediate session unless explicitly authorized.

## Failure modes

| Failure | Cause | Resolution |
|---|---|---|
| `403 Forbidden` | Site blocks scrapers | Try with a user-agent string; some sites allow with proper UA |
| Empty markdown | JavaScript-heavy SPA not rendered | Check if Firecrawl's JS rendering is enabled; increase render wait time |
| Truncated content | Page too long | Use Firecrawl's `limit` and `offset` pagination |
| PDF not parsed | PDF is scanned image (not text-layer) | Route to multimodal OCR handler instead |
| Rate limit exceeded | Too many requests on the plan | Queue requests; upgrade plan if needed |

## Related skills

- [[connector-eur-lex]]
- [[connector-legifrance]]
- [[connector-legal-data-hunter]]
- [[connector-companies-house-uk]]
- [[connector-scheduled-tasks]]
