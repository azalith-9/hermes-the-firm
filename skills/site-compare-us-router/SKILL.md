---
name: site-compare-us-router
description: Use when a site visitor navigates to or searches for a comparison between this legal AI platform and a named competitor (Harvey, Spellbook, CoCounsel, Genie AI, or similar). Routes to the appropriate /vs/[competitor] comparison page. Pages should present honest, accurate tradeoffs rather than one-sided marketing copy, to build credibility with legally-sophisticated audiences.
license: MIT
metadata: " id: site.compare-us-router category: site jurisdictions: [__multi__] priority: P3 intent: [site, routing, competitive-comparison, vs-pages, navigation] related: - site-solutions-router - site-feature-router - site-ai-feature-router source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'site'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Competitor Comparison Router — Site Navigation

## Purpose

Route visitors who are actively comparing legal AI platforms to the relevant `/vs/[competitor]` comparison page. These are high-intent visits from buyers in an evaluation process — the pages must be honest and credible, not marketing-only copy, to convert sophisticated legal buyers.

## Inputs / signals

| Signal | Target URL |
|--------|-----------|
| "/vs/harvey" or "compare to Harvey" | `/vs/harvey` |
| "/vs/spellbook" or "compare to Spellbook" | `/vs/spellbook` |
| "/vs/cocounsel" or "compare to CoCounsel" | `/vs/cocounsel` |
| "/vs/genie-ai" or "compare to Genie AI" | `/vs/genie-ai` |
| "best legal AI", "legal AI comparison", "Harvey alternative" | `/vs/` (comparison index page) |

## Logic

```
1. Parse URL path or search query for competitor name.
2. Match to known competitor slug (exact or fuzzy).
3. Route to /vs/[slug] if exact match.
4. Route to /vs/ (comparison index) if ambiguous or multiple competitors mentioned.
5. Track comparison page visits for intent analytics.
```

## Page content requirements

Each `/vs/[competitor]` page must present:

### Structure
1. **One-paragraph summary** of the comparison (honest; no hyperbole).
2. **Feature comparison table** — key capabilities, with accurate checkmarks; do not claim features the platform does not have.
3. **Jurisdiction coverage** — this platform's MENA/GCC coverage vs competitor's typically US/UK-focused coverage; this is a genuine differentiator.
4. **Pricing model** — if the platform offers free tiers or BYO-key, contrast with competitor pricing; accurate as of publication date.
5. **Use-case fit** — "better for X" vs "better for Y" should be honest. Lawyers value honesty over marketing spin.
6. **One-line verdict** — clear, balanced; avoid "we're the best" framing.

### Tone
- **Honest tradeoffs**: if a competitor has a genuine strength (e.g., a larger US case-law database), acknowledge it.
- **No false claims**: do not assert features or coverage that the platform does not have.
- **Legally sophisticated audience**: law-firm decision makers have a high tolerance-for-nuance and a low tolerance for sales BS. Credibility comes from accuracy.

## Known competitor context (as of May 2026)

| Competitor | Primary strength | Primary gap vs MENA-focused platform |
|-----------|-----------------|--------------------------------------|
| Harvey | Strong US BigLaw focus; deep integration with elite firms | Limited MENA/GCC coverage; less accessible for non-BigLaw |
| Spellbook | Contract review in Word; strong drafting UX | US/Canada-focused; limited MENA jurisdiction support |
| CoCounsel (Thomson Reuters) | Access to Westlaw legal research database | US-centric; subscription cost; limited MENA |
| Genie AI | Open-source document templates | Template library, not AI assistant; limited MENA jurisdiction templates |

## Related skills

- [[site-solutions-router]] — persona-based routing that may follow a comparison page visit
- [[site-feature-router]] — routing to specific features mentioned in comparison
- [[site-ai-feature-router]] — routing to AI feature pages for capability demonstrations
