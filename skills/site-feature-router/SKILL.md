---
name: site-feature-router
description: Use when a site visitor navigates to or searches for a specific product feature by slug. Routes a feature slug to the corresponding feature explanation page, which includes a description, screenshot or demo, and a CTA to try the feature. This is the general feature routing handler; more specific routers (clause-router, ai-feature-router, legal-document-router) handle specialized sub-categories.
license: MIT
metadata: " id: site.feature-router category: site jurisdictions: [__multi__] priority: P3 intent: [site, routing, feature-pages, navigation, product-discovery] related: - site-ai-feature-router - site-clause-router - site-legal-document-router - site-solutions-router - site-compare-us-router source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'site'.
Registered as a flat plugin skill.
-->


# Feature Router — Site Navigation

## Purpose

Route any inbound feature slug — from URL path, site search, or in-app navigation — to the correct product feature explanation page. This is the **general-purpose** feature routing handler. Specialized sub-routers handle specific domains:
- AI skills and tools → [[site-ai-feature-router]]
- Contract clauses → [[site-clause-router]]
- Document library → [[site-legal-document-router]]
- Persona/solution pages → [[site-solutions-router]]

## Inputs / signals

| Signal | Examples |
|--------|---------|
| Direct URL path | `/features/contract-review`, `/features/nda-drafting`, `/features/clause-library` |
| Site search — feature keyword | "contract review", "draft NDA", "employment agreement generator" |
| In-app deep-link | From within the product, link to a feature explanation page |
| Marketing link | From email, ads, social — `/features/[slug]?utm_source=...` |

## Logic

```
1. Receive: feature slug from URL path OR parsed feature keyword from search.
2. Look up slug in feature registry:
   a. Exact slug match → route to /features/[slug]
   b. Keyword match → route to best-matching feature page
   c. Category match → route to /features (category filtered)
   d. No match → fall back to site search results
3. Render feature page:
   - Feature name + one-paragraph description
   - Screenshot or embedded demo
   - Jurisdiction and practice-area tags
   - "Try in Louis" CTA
   - Related features (2–3)
4. Track feature page view for analytics.
```

## Feature page content requirements

Each `/features/[slug]` page must include:

1. **Feature name**: clear, plain-language (e.g., "Contract Risk Review", not "ML-Powered Document Analyzer").
2. **One-paragraph description**: what it does, for whom, in what jurisdictions.
3. **Screenshot or demo**: visual proof of what the output looks like.
4. **Jurisdiction tags**: which jurisdictions are covered (especially MENA-specific features).
5. **Practice area tags**: M&A, employment, commercial, etc.
6. **CTA**: "Try this feature" or "Start free" depending on the user's auth state.
7. **Related features**: 2–3 links to related feature pages.

## URL convention

```
/features/[category]/[slug]     — for categorized features
/features/[slug]                — for top-level features
/tools/[slug]                   — for standalone calculators and tools
```

## Why this matters

Feature pages serve two audiences:
1. **Discovery**: site visitors who don't yet know the platform's full capability set — feature pages make capabilities tangible.
2. **Re-engagement**: existing users who want to deepen their use — feature pages surface capabilities they haven't tried yet.

A clean, fast feature-page routing layer is essential for both SEO (feature pages rank for "[tool type] legal AI" searches) and product-led growth (self-serve discovery of new capabilities).

## Related skills

- [[site-ai-feature-router]] — specialized routing for AI skill and calculator queries
- [[site-clause-router]] — routing for clause-specific queries
- [[site-legal-document-router]] — routing for document-library queries
- [[site-solutions-router]] — persona-based routing
- [[site-compare-us-router]] — competitor comparison routing
