---
name: messaging-hard-rule-preapproved-press-quotes-only
description: Use when any third-party quote — from media coverage, a customer testimonial, an investor statement, a bar association endorsement, or a partner reference — is proposed for use in customer-facing marketing copy. This hard rule requires that every such quote be pre-approved before use, with consent documented. Prevents defamation risk, misattribution, compliance exposure from republishing quotes that contain banned claims, and reputational damage from quotes taken out of context.
license: MIT
metadata: " id: messaging.hard-rule.preapproved-press-quotes-only category: messaging jurisdictions: [__multi__] priority: P2 intent: [messaging, hard-rule, press-quotes, testimonials, compliance, governance] related: [messaging-compliance-checker, messaging-hard-rule-bible-signoff-required, messaging-surface-rule-press-release, messaging-allowed-claims-lawyer, messaging-allowed-claims-consumer] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'messaging'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Messaging — Hard Rule: Pre-Approved Press Quotes Only

## When this applies

This rule applies to every customer-facing surface and asset that includes a third-party quote, endorsement, or attributed statement. It is not limited to press coverage — it covers:

- **Media and press quotes**: excerpts from news articles, legal technology publications, analyst reports, or podcast interviews
- **Customer testimonials**: statements attributed to law firm clients, enterprise customers, or individual users
- **Investor and partner endorsements**: quotes from VCs, strategic partners, law firms, or bar associations
- **Influencer statements**: any claim attributed to a paid or organic influencer in a sponsored context
- **Expert commentary**: quotes from lawyers, legal academics, or regulators used to support product claims

This is a **blocking hard rule**: an asset containing an unverified or unapproved quote cannot ship until the quote is verified, consent is confirmed, and approval is documented.

---

## Behavior — The Pre-Approval Requirements

### Requirement 1: Source Verification

Every proposed quote must be traceable to a specific, dated, verifiable source:
- Press and analyst quotes: article URL, publication date, journalist name
- Customer testimonials: original communication (email, survey response, interview transcript) with date
- Investor/partner statements: written or recorded approval from the named party
- Influencer statements: final approved script or content brief signed off before publication

### Requirement 2: Consent Confirmation

Before using any quote in marketing materials:

| Quote type | Consent required |
|------------|-----------------|
| Press quote (verbatim from published article) | Confirm republication rights or fair use scope; do not assume press quotes are freely reusable in paid advertising |
| Customer testimonial | Written consent from the individual and, for law firm clients, from the firm's marketing/communications officer |
| Expert endorsement | Written agreement specifying which claims the expert endorses and in which contexts |
| Influencer content | Signed influencer brief confirming the pre-approved script and claiming responsibility for compliance with ASA/FTC/local disclosure rules |

### Requirement 3: Compliance Check

Every quote must pass the same compliance standards as original copy:
- Does the quote contain any claim from [[messaging-banned-claims-consumer]] or [[messaging-banned-claims-lawyer]]? If yes → require revised quote or do not use
- Does the quote imply a guaranteed outcome, case win, or cost-undercutting claim? If yes → blocked
- Does the quote make a new capability or accuracy claim not in the bible? If yes → triggers [[messaging-hard-rule-bible-signoff-required]] for the embedded claim

**Key trap:** A quote that is accurate and lawfully made by the original speaker can still be prohibited from republication in marketing copy if it contains claims that violate the messaging framework. Republishing is a new act of marketing.

### Requirement 4: Documentation

Maintain a centralised press quotes register with:
- Quote text (verbatim as approved for use)
- Source (publication/speaker/date)
- Consent record (file reference)
- Compliance check result and reviewer
- Permitted use scope (surfaces, duration, geographic market)
- Expiry or review date (all approvals reviewed at least annually)

---

## What Happens Without Pre-Approval

| Risk | Description |
|------|-------------|
| Defamation | Republishing a quote out of context, or attributing a quote to someone who didn't say it, creates defamation exposure |
| False endorsement | Using a quote to imply an endorsement the speaker did not give violates consumer protection laws in UAE, KSA, UK, and US |
| Bar advertising violations | A quote from a lawyer client or bar official used in marketing copy may trigger bar advertising restrictions if it implies guaranteed outcomes or comparative claims |
| Influencer non-disclosure | Republishing influencer content without disclosure of the commercial relationship violates FTC (US), ASA (UK), and CAP rules; similar requirements exist in UAE and KSA |
| Brand damage | A quote approved in one context may be damaging in another (e.g., a quote about AI speed being used next to a claim about accuracy — implying speed was prioritized over accuracy) |

---

## Application by Surface

| Surface | Specific requirement |
|---------|---------------------|
| Homepage testimonials | Written consent + compliance check; review annually |
| Press release "quote from partner/lawyer" | Confirm quote in writing with the named party before issuing release |
| Sales deck client references | Written consent from client; flag if client is a regulated firm (law firm conflicts may arise) |
| Influencer posts | Full pre-approved script; influencer cannot deviate without re-approval; paid status must be disclosed per applicable jurisdiction rules |
| LinkedIn organic sharing of press article | Permitted without pre-approval if sharing the article link and using verbatim headline only; if paraphrasing or extracting a quote, requires pre-approval |
| App store reviews | Cannot be editorially selected or featured without review against compliance standards |

---

## Exemptions (narrow)

| Situation | Treatment |
|-----------|-----------|
| Internal documents (investor updates, board materials) | Not customer-facing; pre-approval not required but prudent for accuracy |
| Organic social shares of articles by individual employees | Not a company marketing act; but flag if the employee is acting in a company representative capacity |
| Academic or editorial use of quotes | Not marketing; pre-approval not required |

---

## Related skills

- [[messaging-compliance-checker]]
- [[messaging-hard-rule-bible-signoff-required]]
- [[messaging-surface-rule-press-release]]
- [[messaging-surface-rule-influencer-brief]]
- [[messaging-allowed-claims-consumer]]
- [[messaging-allowed-claims-lawyer]]
