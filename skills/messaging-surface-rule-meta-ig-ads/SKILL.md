---
name: messaging-surface-rule-meta-ig-ads
description: Use when creating or reviewing paid advertising copy for Meta (Facebook) and Instagram placements promoting a legal AI assistant to a consumer audience. Defines the visual-first, situation-driven format, the specific character limits, the claim restrictions for paid social, and the Meta ad policy compliance requirements for legal services advertising. Both image ads and video Reels must satisfy these rules plus the base consumer messaging compliance standards.
license: MIT
metadata: " id: messaging.surface-rule.meta-IG-ads category: messaging jurisdictions: [__multi__] priority: P2 intent: [messaging, Meta, Instagram, paid-social, ads, consumer, B2C] related: [messaging-compliance-checker, messaging-allowed-claims-consumer, messaging-banned-claims-consumer, messaging-outcome-claims-allowed, messaging-pricing-framing-b2c] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'messaging'.
Registered as a flat plugin skill.
-->


# Messaging — Surface Rule: Meta / Instagram Ads

## When this applies

This skill applies to all **paid advertising on Meta platforms** — Facebook feed, Instagram feed, Instagram Stories, Instagram Reels, and Audience Network — for a consumer-facing legal AI assistant. It covers:

- Static image ads
- Carousel ads
- Video ads / Reels
- Story ads
- Boosted organic posts

Meta / Instagram ads are a primary consumer acquisition channel. They reach users who have no prior awareness of the product and will form their first impression from 3–5 seconds of creative. The messaging must be instantly clear, emotion-resonant, and compliance-safe.

---

## Meta Ad Policy — Legal Services Category

Meta classifies legal services advertising in a **special ad category** in some markets. Advertisers must:
- Declare the "Legal" special ad category in the Meta Ads Manager for ads about legal services or legal AI
- Note that special ad category restrictions may limit audience targeting (no age, gender, zip code targeting in some markets)
- Verify compliance with Meta's Advertising Standards for sensitive ad categories

**Key Meta policy rules for legal AI ads:**
- No claims that imply guaranteed legal outcomes
- No "before and after" legal outcome narratives
- No targeting of users based on sensitive personal characteristics (legal disputes, immigration status)
- Disclaimers may be required in ad copy or as a disclosure label

---

## Format Rules by Ad Type

### Static Image / Carousel

| Element | Rule |
|---------|------|
| Headline | Max 40 characters; plain language; no outcome claims; situational hook preferred |
| Primary text | Max 125 characters before truncation; lead with the user's situation |
| CTA button | "Learn More", "Sign Up", "Try for Free" — not "Get Legal Advice" |
| Image text | Meta penalises heavy text on images; keep to < 20% of image area; no legal disclaimers in image |

### Video / Reels

| Element | Rule |
|---------|------|
| First 3 seconds | Situation-driven hook: show the user's problem before the product |
| Voice-over | Must use allowed claims only; no script improvisation for paid content |
| On-screen text | Keep clear; include brief compliance framing if making a claim |
| End card | CTA + "legal information, not legal advice" disclaimer |
| Duration | 15–60 seconds optimal; 30–45 seconds for situation + solution + CTA |

---

## Messaging Rules for Meta / Instagram Ads

### Situation-first structure (required)

Meta ads perform best when they start with the viewer's problem. For legal AI, that means:

1. **Problem / situation** (3–5 seconds / 1–2 sentences): "You just got a new lease to sign. The clauses are confusing."
2. **Solution framing** (allowed claim): "Louis explains every clause in plain English — so you know what you're agreeing to."
3. **CTA**: "Try Louis free →"

This structure naturally avoids banned claims because it focuses on the user's experience, not on what Louis replaces.

### Jurisdiction-specific ad groups

- Run separate ad groups by jurisdiction where possible: UAE users see UAE-context creative, KSA users see KSA-context creative
- Jurisdiction-specific copy: "Understand your UAE labour contract" / "Know your rights as a tenant in Dubai"
- Do not run generic "any country" legal ads — the situational specificity increases engagement and reduces the risk of overclaiming coverage

### Claim standards

All outcome claims in Meta/Instagram ads must meet the standards in [[messaging-outcome-claims-allowed]]:
- "On average" or "most users" qualifiers required for time/productivity metrics
- Source disclosed in the ad (caption or on-screen text) or on the landing page linked from the ad
- No outcome guarantees under any circumstances

---

## Banned Patterns for Meta / Instagram Ads

- "Free legal advice" as a hook or headline — UPL trigger; Meta may also reject the ad
- Before/after legal outcome narratives ("John won his employment case after using Louis")
- Claims targeting users based on active legal disputes ("If you're in a lawsuit…")
- Outcome promises as a hook ("Win your next contract negotiation")
- Testimonials using banned claim language (even if user-sourced)

---

## Examples

**Strong Instagram ad (Reel structure):**
> [Visual: person staring at a document on their phone, confused expression]
> [Voice-over]: "Got a contract to sign and no idea what it means?"
> [Visual: Louis interface explaining a clause]
> [Voice-over]: "Louis explains every clause in plain English — so you know exactly what you're agreeing to."
> [End card]: "Try Louis free" + small text "Legal information, not legal advice."

**Weak (avoid):**
> [Visual: person relieved]
> [Text]: "Say goodbye to lawyer fees. Louis handles everything."

---

## Related skills

- [[messaging-compliance-checker]]
- [[messaging-allowed-claims-consumer]]
- [[messaging-banned-claims-consumer]]
- [[messaging-outcome-claims-allowed]]
- [[messaging-pricing-framing-b2c]]
- [[messaging-surface-rule-influencer-brief]]
