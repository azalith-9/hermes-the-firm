---
name: site-marketplace-router
description: Use when a site visitor navigates to or searches for the platform's marketplace — a planned phase-2 feature for browsing third-party legal templates, lawyer services, or skill add-ons. Routes to the marketplace landing page or a filtered category view. Currently a placeholder for a phase-2 surface; the skill defines the intended routing architecture for when the marketplace launches.
license: MIT
metadata: " id: site.marketplace-router category: site jurisdictions: [__multi__] priority: P3 intent: [site, routing, marketplace, phase-2, navigation] related: - site-legal-document-router - site-feature-router - site-solutions-router - site-ai-feature-router source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'site'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Marketplace Router — Site Navigation

## Purpose

Route visitors to the platform's legal marketplace — a planned phase-2 feature that allows browsing and purchasing/accessing:
- Third-party legal document templates (vetted by jurisdiction-specialist lawyers).
- Add-on AI skills (specialist skills contributed by law firms or legal tech providers).
- Lawyer matching / referral services (connecting users with vetted lawyers in specific jurisdictions).
- Legal research subscriptions or integrations.

As of the current version, this is a **phase-2 feature**. The routing architecture is defined here so the implementation can be built against a stable spec.

## Inputs / signals

| Signal | Target |
|--------|--------|
| Direct `/marketplace` navigation | Marketplace landing page |
| "Buy template", "premium template", "download legal doc" | Marketplace document category |
| "Find a lawyer", "lawyer referral", "legal help in [jurisdiction]" | Marketplace lawyer-matching category |
| "Add-on skill", "specialist skill", "DIFC arbitration skill" | Marketplace skills category |
| "Legal marketplace", "legal template store" | Marketplace landing page |

## Intended marketplace architecture (phase 2)

### Categories
1. **Documents & Templates** — jurisdiction-tagged templates from vetted contributors; one-time purchase or subscription.
2. **Skills & Add-ons** — specialist AI skills for niche practice areas or jurisdictions; installed to the user's account.
3. **Lawyer Connect** — verified lawyer profiles; initial consult booking; jurisdiction and practice-area filtered.
4. **Integrations** — connector skills linking to external legal research databases, court filing systems, or practice management tools.

### Listing requirements (for marketplace contributors)
- Jurisdiction(s) covered: explicit list.
- Last reviewed date: mandatory; auto-expires after 12 months if not renewed.
- Lawyer-authored / reviewed badge: requires licensed practitioner attestation.
- Pricing: clear; one-time, subscription, or per-use.
- Refund policy: template for standard terms.

### Routing logic (planned)
```
1. Parse navigation intent (see signals above).
2. Route to /marketplace?category=[category]
3. Within category, support filters: jurisdiction, practice area, price range, rating.
4. Each listing links to a detail page with preview, reviews, and purchase/install CTA.
5. After purchase/install: route back to product or to the installed template/skill.
```

## Current state — pre-launch

Until the marketplace launches:
- Route `/marketplace` requests to a "coming soon" page with email capture (waitlist for marketplace).
- Route "buy template" or "premium template" requests to the free document library ([[site-legal-document-router]]) with an upsell note about the upcoming marketplace.
- Route "find a lawyer" requests to the relevant bar association directory or legal aid resource.

## Related skills

- [[site-legal-document-router]] — existing document library (phase 1)
- [[site-feature-router]] — feature-page routing
- [[site-solutions-router]] — persona routing that may surface marketplace features to relevant personas
- [[site-ai-feature-router]] — AI skill feature routing
