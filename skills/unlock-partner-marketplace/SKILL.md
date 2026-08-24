---
name: unlock-partner-marketplace
description: Use when a user or admin asks about third-party integrations, partner firms, sponsored legal content, or an app/connector marketplace within the platform. This skill describes the planned partner marketplace surface — its scope, phased launch timeline (planned 2027), content types, and what to communicate to users who inquire about it before launch.
license: MIT
metadata: " id: unlock.partner-marketplace category: unlock jurisdictions: [__multi__] priority: P2 intent: [__customer-facing__, marketplace, integrations, partnerships] related: - unlock-whitepaper-when-evaluating - unlock-feature-discovery-by-persona - unlock-template-of-the-week source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'unlock'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Partner Marketplace

## Purpose

The partner marketplace is a curated surface within the platform where users can discover, install, and manage:

1. **Integrations** — third-party connectors (document management systems, e-signature platforms, billing tools, court e-filing portals, data providers).
2. **Partner firms** — verified law firms, notaries, and legal service providers that users can engage directly from the platform.
3. **Sponsored content** — vetted, editorially-reviewed legal templates, playbooks, and knowledge packs provided by partner organizations.

## Current status

The marketplace is **not launched as of 2026**. It is planned for **2027**. No marketplace UI exists in the product as of the current release.

### What this means in practice
- Do not surface marketplace UI or deep-links to users in the current product version.
- When a user asks "Can I connect to [tool]?" or "Are there other firms I can reach through Louis?", acknowledge that a marketplace is planned and provide the workaround or direct connector that exists today (e.g., eFirm integration, Zapier, or manual export).
- Do not promise specific integrations or partner firms by name unless they are confirmed and documented.

## Planned marketplace content types

### Integration partners (phase 1 focus)
| Category | Example connectors |
|----------|--------------------|
| Document management | iManage, NetDocuments, SharePoint |
| E-signature | DocuSign, Adobe Sign, Tawqi3i (MENA) |
| E-filing | ADGM court portal, DIFC courts, Lebanese Notary registry |
| Billing & matter | Clio, Leap, Practice Evolve |
| Data & research | vLex, Westlaw Arabia, Al-Muqtafi |

### Partner firms
Verified directories of:
- Law firms with MENA footprints (UAE, KSA, LB, EG) willing to accept referrals
- Notary publics certified in specific jurisdictions for Tawqi3i-level attestation
- Freelance legal translators (Arabic ↔ English ↔ French) certified for sworn translation

### Sponsored content
Third-party legal templates and practice guides that have been:
- Reviewed by Louis's editorial team for accuracy
- Jurisdiction-tagged
- Clearly labeled as "Sponsored by [Firm Name]" to maintain transparency

Sponsored content is never ranked above native skills in the skills router. It appears in a distinct "Partner Resources" section.

## Governance principles

1. **Opt-in only** — users choose which integrations to enable. No auto-connection to any third-party service.
2. **Least privilege** — integrations request only the permissions they need (read-only where possible).
3. **Revenue model** — revenue sharing with integration partners is disclosed in terms. Sponsored content is clearly labeled.
4. **MENA-first curation** — priority given to partners with genuine MENA presence and legal standing.
5. **Data residency** — partner integrations that handle user documents must meet the platform's data residency requirements (user data does not leave the agreed jurisdiction without consent).

## Communicating the roadmap to evaluators

When a user is clearly in evaluation mode (comparing features to competitors, asking about integration depth), acknowledge the marketplace roadmap honestly:

> "A full partner marketplace — integrations, firm directory, and sponsored content — is on the roadmap for 2027. Today, we support [list current integrations]. If a specific integration is important to your evaluation, let me know and I can check whether it's in the near-term build plan."

This is more credible than vague promises and builds trust during the sales cycle.

## Related skills

- [[unlock-whitepaper-when-evaluating]]
- [[unlock-feature-discovery-by-persona]]
- [[unlock-template-of-the-week]]
- [[unlock-power-user-shortcuts]]
