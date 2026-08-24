---
name: messaging-banned-claims-consumer
description: Use when reviewing consumer-facing copy, ads, social content, emails, or landing pages for a legal AI assistant to identify claims that must never appear on B2C surfaces. Defines the hard-line banned phrases, framing patterns, and implied meanings that create unauthorized-practice-of-law (UPL) risk, consumer protection liability, or brand damage. Triggers whenever copy is submitted for marketing review, compliance check, or influencer approval on consumer channels.
license: MIT
metadata: " id: messaging.banned-claims-consumer category: messaging priority: P0 intent: [messaging, banned, consumer, UPL, compliance, copy-review] related: [messaging-allowed-claims-consumer, messaging-compliance-checker, messaging-bridge-line, messaging-hard-rule-bible-signoff-required, messaging-surface-rule-influencer-brief] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'messaging'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Messaging — Banned Consumer Claims

## When this applies

This skill contains the **hard-line prohibition list** for all consumer-facing copy for a legal AI assistant. It applies to every B2C surface: the homepage, landing pages, social media ads, influencer briefs, email campaigns, in-app notifications, and any other material visible to non-lawyer end users. There are no exceptions for platform, audience size, or campaign urgency.

When copy is submitted for compliance review, this list is checked first and is **blocking**: a single banned claim requires full copy revision before publication.

---

## Behavior — The Bright Lines

The following claims and framings are **absolutely prohibited** on consumer surfaces. No context, disclaimer, or fine print makes them acceptable.

---

## Banned Framing — Verbatim and Category

### Lawyer Replacement

| Banned | Why |
|--------|-----|
| "Replaces your lawyer" | Direct UPL trigger; asserts the product performs licensed legal services |
| "No lawyer needed" | Equivalent to the above; discourages professional consultation |
| "Skip the lawyer" | Positions the product as a substitute for professional advice |
| "DIY legal" (when used to imply full legal substitute) | Blurs the line between legal information and legal services |
| "Handle it yourself — no legal fees" | Implies the product performs the legal work |

### Outcome Guarantees

| Banned | Why |
|--------|-----|
| "Win your case" | False guarantee; bar advertising rules in all MENA jurisdictions prohibit outcome claims |
| "Guaranteed outcome" | Same; also triggers consumer protection / false advertising liability |
| "We got them their money back" (specific results) | Testimonials implying guaranteed results are prohibited |
| "Guaranteed to save you money" | Combination outcome + financial claim without substantiation |

### Legal Practice Framing

| Banned | Why |
|--------|-----|
| "Free legal advice" | "Legal advice" in consumer context implies licensed-lawyer advice; even if the tier is free, this claim is prohibited |
| Anything implying licensed legal practice | Any phrase that positions the product as providing legal advice, legal opinions, or legal representation |

### Cost Competition with Lawyers

| Banned | Why |
|--------|-----|
| "Save thousands on legal fees" (price-undercutting framing) | Positions the product as a lawyer substitute on cost grounds; triggers bar relationship damage and brand integrity risk |
| "Cheaper than a lawyer" (as a primary positioning claim) | The product partners with lawyers; undercutting framing undermines that relationship |

---

## Why These Rules Exist

### 1. Unauthorized Practice of Law (UPL) Risk
Most MENA jurisdictions (Lebanon, KSA, UAE) and common-law jurisdictions (DIFC, ADGM, UK, US) prohibit the provision of legal advice, legal opinions, and legal representation by unlicensed entities. Marketing copy that implies such provision exposes the company to regulatory action and potential criminal liability in some jurisdictions.

### 2. Consumer Protection — False Advertising
Consumer protection laws (UAE Federal Law on Consumer Protection, KSA Consumer Protection Regulation, UK Consumer Protection from Unfair Trading Regulations, US FTC Act) prohibit false or misleading claims. Outcome guarantees ("win your case") and unsupported quantitative claims are per se violations in most jurisdictions.

### 3. Brand Integrity — Lawyer Partnership Model
The product's commercial model depends on lawyers trusting it. Consumer-side copy that positions the product as a lawyer substitute damages that relationship and is commercially self-defeating.

### 4. Insurance and E&O Exposure
Claims that imply legal advice delivery can void errors and omissions insurance coverage and expose the company to professional liability claims even absent a formal lawyer-client relationship.

---

## Where These Bans Apply

- All consumer-facing surfaces: homepage, product pages, landing pages, in-app copy
- All paid advertising: search, display, social (Meta, TikTok, Snapchat, LinkedIn consumer targeting)
- All organic social media posts and story content
- All email marketing and push notifications
- All influencer briefs, sponsored posts, and affiliate content
- All PR quotes, press releases, and media kits (consumer-facing sections)
- Any B2B asset where non-lawyer consumers are part of the audience

---

## Compliance Enforcement

1. **Pre-publication review:** All marketing copy is reviewed through [[messaging-compliance-checker]] before any consumer-facing asset ships.
2. **Bible signoff:** New claim types not appearing on the allowed list require legal and product sign-off per [[messaging-hard-rule-bible-signoff-required]].
3. **Influencer briefs:** Include this banned-words list verbatim per [[messaging-surface-rule-influencer-brief]].
4. **Retroactive review:** Existing live assets are audited quarterly; any banned claim found in a live asset triggers immediate takedown.

---

## Examples — Banned vs Allowed

| Banned | Allowed alternative |
|--------|---------------------|
| "No lawyer needed" | "Helps you prepare for a lawyer conversation" |
| "Free legal advice" | "Free legal information — always suggest a lawyer for complex situations" |
| "Win your case with Louis" | "Understand your options before you go to court" |
| "Save thousands on legal fees" | "Understand your rights — for free" |
| "Skip the lawyer" | "Start here. Then talk to a lawyer." |
| "Replaces your lawyer" | "Helps you get more out of every lawyer meeting" |
| "DIY legal — no professional needed" | "Legal templates you can review with your lawyer" |

---

## Edge Cases

| Situation | Rule |
|-----------|------|
| User-written review using "replaced my lawyer" | Do not republish, feature, or amplify without edit |
| Influencer ad-lib on video using banned phrase | Require re-shoot or overlay disclaimer |
| "Cheaper than lawyers" in a cost-comparison chart | Chart allowed only if framed as "cost of understanding" not "cost of legal services" |
| Academic or media quote referencing "legal advice AI" | Clarify in response and do not re-use in marketing |
| Disclaimer at bottom of ad covering UPL concern | Disclaimer does not cure a banned claim in the main copy |

---

## Do not

- Assume a small or niche audience exempts copy from these rules
- Assume a disclaimer negates a banned claim in the headline or body
- Allow any claim through on the basis that "everyone in the industry says this" — our standard is independent of industry practice
- Permit time-pressure exceptions ("the campaign launches tomorrow") — launch late rather than publish banned copy

---

## Related skills

- [[messaging-allowed-claims-consumer]]
- [[messaging-compliance-checker]]
- [[messaging-bridge-line]]
- [[messaging-hard-rule-bible-signoff-required]]
- [[messaging-surface-rule-influencer-brief]]
- [[messaging-outcome-claims-banned]]
