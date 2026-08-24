---
name: pillar-live-data-mcp
description: Internal architectural principle establishing that Louis accesses current legal data — sanctions lists, company registries, official gazettes, court databases — through live MCP-style connectors rather than relying on frozen training data. Use when designing data connectors, evaluating the currency of regulatory information, or understanding why certain legal data sources must be queried in real time.
license: MIT
metadata: " id: pillar.live-data-MCP category: pillar jurisdictions: [__multi__] priority: P3 intent: [__internal__] related: [pillar-architectural-bet-no-fine-tuning, pillar-legal-skills-authoring, pillar-context-across-apps, eng-mcp-connectors, connector-sanctions-screening] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'pillar'.
Registered as a flat plugin skill.
-->


# Architectural Pillar: Live Data via MCP Connectors

## Scope

This pillar establishes that **certain categories of legal data must always be current** and therefore cannot be encoded in static training data or skill files. Louis accesses this data through live connectors — modeled on the Model Context Protocol (MCP) pattern — that query authoritative sources at inference time.

---

## The principle

> Live data via MCP-style connectors > frozen training data. Sanctions, registries, gazettes always current.

---

## Why some legal data must be live

### Law changes; training data does not
A foundation model's training cutoff means it knows only what was true as of a past date. But legal compliance often depends on current-state data:

- **Sanctions lists**: an entity on the OFAC SDN list today may not have been on it at the model's training cutoff — and vice versa. A stale sanctions check is a compliance failure.
- **Company registries**: ownership, directorship, and registered address information changes continuously. A due-diligence check based on outdated registry data may miss red flags.
- **Official gazettes**: new regulations, decrees, and ministerial orders are published continuously. A legal analysis that misses last month's amendment to the UAE Commercial Companies Law is unreliable.
- **Court databases**: judgment enforcement, case status, and precedent develop in real time.
- **Exchange rates / financial thresholds**: AML transaction-monitoring thresholds, tariff rates, and other numerically precise regulatory values change.

### The cost of stale data in legal AI is high
In most software, stale data causes minor inconvenience. In legal AI, stale data can cause:
- A compliant transaction to be wrongly flagged (false positive, business disruption)
- A non-compliant transaction to be cleared (false negative, regulatory breach, liability)
- Legal advice based on repealed law
- Missed deadlines because a statute of limitations was incorrectly stated

---

## Data categories requiring live connectors

| Category | Examples | Why live |
|----------|---------|---------|
| Sanctions and AML lists | OFAC SDN, EU Consolidated List, UN Security Council List, UAE Local Terrorist Designations (Cabinet Decision 20/2019), Saudi SAFIU list | Lists updated daily or in real time; stale list = compliance failure |
| Company registries | UAE Ministry of Economy, DIFC CR, ADGM Register, Saudi MISA (SAGIA), Lebanon CCR, Egypt GAFI, French RCS | Ownership / beneficial owner / dissolution status changes |
| Official gazettes | UAE Federal Gazette, Saudi Umm Al-Qura, Lebanese Official Gazette (Jarida Rasmiyya), Egyptian Official Gazette, DIFC Gazette | New laws, amendments, decrees; can change the applicable legal framework |
| Court databases | DIFC Courts eCourt (public judgments), Dubai Courts (where public), Saudi MOJ Najiz | Precedent, enforcement status, appeal outcomes |
| Currency and financial data | Central bank exchange rates, SAMA LIBOR successor rates | Contractual calculations, AML thresholds |
| IP registries | UAE MOCCAE trademark database, Saudi SAIP, Lebanese trademark registry | Search results for trademark clearance; registration status |
| Real estate registries | Dubai Land Department, Abu Dhabi DARI | Property ownership, encumbrances, valuations |

---

## MCP connector design principles

Each live-data connector must implement:

1. **Authentication**: API key, OAuth, or institutional credentials — stored in secrets management, never in skill files
2. **Query interface**: structured input (entity name, identifier, date range, jurisdiction) → structured output
3. **Caching policy**: define what can be cached and for how long (sanctions lists: no cache or very short; gazette: cache until next issue; company registry: cache with staleness flag)
4. **Failure handling**: if the live source is unavailable, the connector must return a clear "unavailable" signal rather than silently returning stale data or nothing
5. **Audit trail**: every live query must be logged with timestamp, query parameters, and result summary — for compliance and debugging
6. **Source attribution**: the output must cite the source and the date/time of query so the user and the legal record know what data was used

---

## How connectors interact with skills

Skills that require live data declare their connector dependencies in their inputs section:

```
Required inputs:
  - party_name: [entity to screen]
  - query_date: [effective date for screening; defaults to today]

Connector calls:
  - connector-sanctions-screening(party_name, query_date) → sanctions_result
  - connector-company-registry(party_name, jurisdiction) → registry_result
```

The router pre-fetches connector data before loading the skill into the prompt. The skill receives the connector output as structured context, not as a raw API response.

---

## What connectors do not replace

Live connectors are not a substitute for legal judgment:
- A connector confirms that an entity is (or is not) on a sanctions list **today**. It does not determine whether a transaction is prohibited — that requires legal analysis of the applicable sanctions regime.
- A gazette connector retrieves the text of a new decree. It does not interpret its application to a specific fact pattern.
- A registry connector returns ownership information. It does not assess whether the ownership structure raises AML concerns.

The skill layer provides the judgment; the connector layer provides the data.

---

## Coverage by jurisdiction

| Jurisdiction | Key live data sources (target) |
|-------------|-------------------------------|
| UAE | MOE company registry, MOCCAE trademark, DLD, Dubai Courts public judgments, Federal Gazette |
| DIFC | DIFC CR, DIFC Courts eCourt |
| ADGM | ADGM Register |
| KSA | MISA (SAGIA), Umm Al-Qura gazette, Najiz courts portal |
| Lebanon | Nufous civil registry (limited API), CCR company registry, Official Gazette |
| Egypt | GAFI registry, Official Gazette |
| Global | OFAC SDN, EU Consolidated Sanctions List, UN SC Sanctions List, INTERPOL (limited) |

Coverage is prioritized by jurisdiction importance and API availability. Not all sources have public or affordable APIs; some require institutional subscriptions.

---

## Caveats and currency

The connector landscape changes as jurisdictions launch new digital registries and APIs. This pillar should be reviewed when new MENA digital government initiatives launch. The UAE's DIFC and ADGM are generally ahead of the region on digitization; Lebanon's registry access remains largely manual as of the drafting of this pillar.

---

## Related skills

- [[pillar-architectural-bet-no-fine-tuning]] — why live data complements the no-fine-tuning approach
- [[pillar-legal-skills-authoring]] — how skills declare connector dependencies
- [[pillar-context-across-apps]] — how connector results are stored in matter context
- [[eng-mcp-connectors]] — engineering implementation of the MCP connector layer
- [[connector-sanctions-screening]] — the sanctions screening connector
