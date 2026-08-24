---
name: docs-cookie-policy-summary
description: Use when a user asks what cookies the platform uses, how to manage cookie preferences, or what data is collected via cookies. This is a platform documentation skill providing a plain-English summary of the cookie policy covering essential, functional, analytics, and marketing cookie categories, and explaining how self-serve consent controls work.
license: MIT
metadata: " id: docs.cookie-policy-summary category: docs jurisdictions: [__multi__] priority: P2 intent: [__docs__, cookies, consent, privacy, GDPR, tracking] related: [docs-data-residency-mena, docs-legal-ai-workspace-guide, docs-faq-pack] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'docs'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Cookie Policy Summary

## Purpose

This documentation provides a plain-English explanation of how the platform uses cookies and similar tracking technologies, what data they collect, and how users can manage their cookie preferences. The full legal cookie policy is available at `/legal/cookie-policy`.

## What cookies are

Cookies are small text files placed on a user's device by a website or application. They serve different purposes — from keeping the user logged in (essential), to remembering display preferences (functional), to helping the product team understand how users navigate the platform (analytics), to serving personalized advertisements (marketing).

## Cookie categories

### Essential cookies

**Cannot be disabled.** These are required for the platform to function. Without them, the user cannot log in, maintain a session, or access secure areas.

Examples:
- `session_token`: keeps the user authenticated during a session.
- `csrf_token`: prevents cross-site request forgery attacks.
- `workspace_id`: identifies the active workspace for multi-workspace users.

**Data collected**: session identifiers only; no personal data beyond what is necessary for authentication.

### Functional cookies

**Can be disabled**, but disabling them degrades the user experience. These remember user preferences.

Examples:
- `ui_language`: stores the user's preferred interface language (English / Arabic).
- `theme_preference`: stores the user's light/dark mode selection.
- `last_matter_id`: reopens the user's most recent matter on login.

**Data collected**: preference identifiers; no browsing history or personal data shared with third parties.

### Analytics cookies

**Can be disabled.** These collect aggregate data about how the platform is used — which features are used most, where users encounter friction, how long tasks take. The product team uses this data to improve the platform.

Analytics provider: PostHog (privacy-preserving analytics; data processed in EU by default). No personally identifiable information is included in analytics events unless the user has consented to identified analytics.

**Data collected**: page views, feature interaction events, session duration, browser type, device type, jurisdiction preferences (aggregated). IP addresses are anonymized.

### Marketing cookies

**Can be disabled.** These track whether a user came from a marketing campaign (ad, email, referral link) and whether they converted (signed up, upgraded). Used for measuring the performance of marketing campaigns.

Marketing provider: varies (verify current list in the full cookie policy). Data shared only with the specific provider of the campaign channel that drove the visit.

**Data collected**: referral source, campaign identifier, conversion event. No legal document content is ever included in marketing data.

## Self-serve consent controls

Users can manage cookie preferences at any time:

1. **On first visit**: a cookie consent banner is displayed. Users can Accept All, Reject Non-Essential, or open the Cookie Settings panel to configure categories individually.
2. **After login**: navigate to **Settings → Privacy → Cookie Preferences** to modify consent at any time.
3. **Via the consent management widget**: the cookie icon in the bottom navigation bar opens the preferences panel.

Changes take effect immediately. Withdrawing consent for analytics or marketing cookies stops new data collection from that point; it does not retroactively delete previously collected aggregate data.

## Regulatory compliance

| Regulation | Compliance approach |
|---|---|
| **GDPR (EU)** | Consent-based cookies (analytics, marketing) require explicit opt-in. Consent records are logged and available for audit. |
| **UK GDPR** | Same as EU GDPR; separate consent mechanism for UK users post-Brexit. |
| **ePrivacy Directive (Cookie Law)** | Platform complies with the requirement for prior informed consent before placing non-essential cookies. |
| **UAE PDPL** | Cookies that collect personal data are disclosed; data subjects have the right to withdraw consent. |
| **KSA PDPL** | Cookie data is treated as personal data where it can identify the user; consent is obtained prior to non-essential cookie placement. |

## What cookies do NOT contain

- Confidential legal document content.
- Client matter data.
- Draft text or conversation content.
- Passwords or authentication credentials.

All legal work product is stored server-side, encrypted at rest, and governed by the data residency and security policy — not by cookies.

## Related skills

- [[docs-data-residency-mena]]
- [[docs-legal-ai-workspace-guide]]
- [[docs-faq-pack]]
