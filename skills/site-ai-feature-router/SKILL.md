---
name: site-ai-feature-router
description: Use when a site visitor's search query or navigation intent matches a named AI feature, skill, calculator, or tool library within the legal AI platform. Routes the user to the dedicated feature page for that capability rather than returning a generic search result. Applies to all jurisdictions and user types interacting with the platform's public-facing site.
license: MIT
metadata: " id: site.ai-feature-router category: site jurisdictions: [__multi__] priority: P3 intent: [site, routing, feature-discovery, search, navigation] related: - site-feature-router - site-legal-document-router - site-clause-router - site-solutions-router - site-prompt-library-suggester source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'site'.
Namespaced as louis-<category>-<skill> on registration.
-->


# AI Feature Router — Site Navigation

## Purpose

When a site visitor's search query or navigational intent clearly signals interest in a specific AI-powered capability — a named skill, a calculator tool, or a library of prompts — route them directly to the dedicated feature page rather than a generic search result page. This improves discoverability of the platform's capabilities and reduces the number of clicks between intent and value.

## Inputs / signals

| Signal type | Examples | Target |
|-------------|---------|--------|
| Named skill query | "NDA review", "contract risk analyzer", "employment clause checker" | `/features/[skill-slug]` |
| Named calculator / tool | "notice period calculator", "penalty clause estimator", "limitation period checker" | `/tools/[tool-slug]` |
| Prompt library query | "legal prompts", "AI prompts for lawyers", "prompt library" | `/tools/prompts` — see [[site-prompt-library-suggester]] |
| Feature category | "document drafting AI", "contract review AI", "legal research AI" | `/features/[category]` |
| Capability comparison | "compare AI legal tools", "vs Harvey", "vs Spellbook" | `/vs/[competitor]` — see [[site-compare-us-router]] |

## Logic

```
1. Parse the incoming search query or navigation path.
2. Match against the feature index (skills, calculators, prompt packs) by:
   a. Exact slug match (highest confidence).
   b. Semantic match against feature name and description (medium confidence).
   c. Category-level match (lower confidence — route to category page, not specific feature).
3. If match confidence > threshold:
   → 301-redirect or in-page navigation to `/features/[slug]` or `/tools/[slug]`.
4. If no match:
   → Fall through to general search results or [[site-legal-document-router]] / [[site-solutions-router]] as appropriate.
5. Track click-through events for conversion analytics.
```

## Output

A navigation action: redirect or deep-link to the matched feature page. The feature page provides:
- Feature name and one-paragraph description.
- Screenshot or demo of the feature in action.
- CTA (call-to-action): "Try in Louis" button.
- Jurisdiction and practice-area tags.
- Related features.

## Why this matters

Feature discoverability is a primary growth lever for legal AI platforms. Lawyers and legal teams searching for "contract risk review" or "NDA drafting AI" are high-intent visitors — routing them to the right feature page in one step (rather than requiring them to navigate a generic product page) significantly improves conversion rates and reduces bounce.

## Related skills

- [[site-feature-router]] — general feature-page routing (feature slug → explanation + CTA)
- [[site-legal-document-router]] — routing for document-library queries
- [[site-clause-router]] — routing for clause-specific queries
- [[site-solutions-router]] — routing based on user persona
- [[site-prompt-library-suggester]] — routing to the prompt library
