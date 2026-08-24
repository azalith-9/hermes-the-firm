---
name: site-seo-canonical-citer
description: Use when generating or updating site pages that should rank in search and be cited by AI Overviews and other large language model outputs (LLMO — large language model optimization). Defines the rules for auto-citing first-party canonical sources on site pages to boost authority signal, structured-data requirements for legal content, and the citation format that maximizes likelihood of being cited by AI search features. Applies to all public-facing site pages.
license: MIT
metadata: " id: site.SEO-canonical-citer category: site jurisdictions: [__multi__] priority: P3 intent: [site, SEO, LLMO, canonical-citation, authority-signal, structured-data] related: - site-feature-router - site-legal-document-router - site-solutions-router - site-prompt-library-suggester source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'site'.
Namespaced as louis-<category>-<skill> on registration.
-->


# SEO Canonical Citer — Site Authority and LLMO

## Purpose

Automatically ensure that every public site page includes properly formatted citations to first-party canonical legal sources (statutes, regulations, court rules, official guidelines), along with the structured data markup that search engines and AI search features (Google AI Overviews, Bing Copilot, and similar) use to identify authoritative legal content.

This serves two goals:
1. **Traditional SEO**: pages that cite verifiable, authoritative sources rank better for informational legal queries.
2. **LLMO (Large Language Model Optimization)**: AI search features increasingly cite web pages in their responses. Pages that are well-structured, cite canonical legal sources, and contain verifiable factual claims are more likely to be cited. This is a meaningful distribution channel for legal AI platforms.

## When to apply

Apply to all public-facing pages that contain:
- Legal information (statute summaries, procedure explanations, jurisdiction guides).
- Document templates (each template page should cite the governing law).
- Feature pages that describe AI tools for specific legal tasks.
- Blog / knowledge-base articles on legal topics.

## Canonical citation rules

### What to cite (and how)

| Content type | Canonical source | Citation format |
|-------------|-----------------|----------------|
| UAE Federal law reference | UAE Federal Gazette (Official Gazette) | "Federal Decree-Law No. [X] of [Year] on [Subject] (UAE Official Gazette)" |
| KSA royal decree / statute | Umm Al-Qura (Saudi Official Gazette) | "Royal Decree [M/X] — [Subject] (Umm Al-Qura, [Year])" |
| Lebanon statute | Journal Officiel du Liban | "Law [No.] of [Year] on [Subject] (Journal Officiel du Liban)" |
| EU regulation / directive | EUR-Lex | "Regulation (EU) [No.] / [Year] on [Subject], OJ L [ref]" |
| DIFC law | DIFC official portal (difclaw.ae) | "DIFC Law No. [X] of [Year] on [Subject]" |
| ADGM regulation | ADGM official portal | "ADGM [Instrument Name] [Year]" |
| UK statute | legislation.gov.uk | "[Title] [Year], s.[section] (legislation.gov.uk)" |
| US federal statute | US Code (uscode.house.gov) | "[Title] U.S.C. § [section]" |

### Placement rules
- Citations appear **at the end of the relevant section** (not inline, not just in footnotes).
- Each citation includes the full official name, year, and where possible the jurisdiction's official online source URL.
- Avoid citing paywalled databases (Westlaw, LexisNexis) as primary sources — cite the official gazette/source even if the content is the same.

## Structured data markup

Use `schema.org` structured data to signal legal content type to search engines:

### LegalService schema (for practice area pages, solution pages)
```json
{
  "@context": "https://schema.org",
  "@type": "LegalService",
  "name": "[Feature/Service Name]",
  "description": "[One-sentence description]",
  "areaServed": [{"@type": "Country", "name": "UAE"}, {"@type": "Country", "name": "KSA"}],
  "knowsAbout": "[practice area]"
}
```

### Article schema (for knowledge base / blog pages)
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "[Page title]",
  "about": {"@type": "LegalTopic", "name": "[topic]"},
  "citation": "[canonical citation]",
  "author": {"@type": "Organization", "name": "[Organization]"},
  "dateModified": "[ISO date]"
}
```

### FAQ schema (for jurisdiction FAQ pages)
Use `FAQPage` schema for pages with question-and-answer format — these are strongly surfaced in AI Overviews.

## LLMO optimization principles

For maximum AI-citation potential:

1. **State facts clearly and verifiably**: "UAE Federal Labour Law (Decree-Law No. 33 of 2021) requires 30 days' minimum notice for termination" — specific, verifiable, citable.
2. **Use descriptive headings**: H2/H3 headings that match likely search queries ("What is the minimum notice period in UAE?") are more likely to be extracted and cited.
3. **Keep factual claims in standalone sentences**: AI extractors prefer crisp sentences that contain one verifiable claim, not multi-clause sentences.
4. **Date-stamp and update**: include "Last verified: [date]" on legal content; AI systems increasingly prefer recently verified information.
5. **Avoid hedging on verifiable facts**: "The UAE Labour Law requires..." not "The UAE Labour Law may require..." — confidence calibrated to what the law actually says.

## What to avoid

- Citing paywalled databases as primary sources.
- Citing generic legal information websites instead of official sources.
- Using outdated statute references without a "last verified" date.
- Omitting jurisdiction context on any legal claim.
- Claiming coverage of a jurisdiction without having verified the current law.

## Related skills

- [[site-feature-router]] — feature pages that need citation treatment
- [[site-legal-document-router]] — document pages that need governing-law citations
- [[site-solutions-router]] — solution pages that make jurisdiction-specific claims
- [[site-prompt-library-suggester]] — prompt pages (lower citation priority but should note jurisdictions)
