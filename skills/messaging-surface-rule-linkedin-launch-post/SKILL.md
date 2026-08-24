---
name: messaging-surface-rule-linkedin-launch-post
description: Use when drafting a LinkedIn post to announce a product launch, major feature release, funding round, or partnership for a legal AI assistant. Defines the structure, claim standards, tone, and compliance requirements for LinkedIn organic content from the company account or founder's personal account. LinkedIn has a dual audience (lawyers and non-lawyers) and a professional register; apply both consumer and lawyer messaging rules simultaneously unless the post is explicitly targeted to one audience.
license: MIT
metadata: " id: messaging.surface-rule.linkedin-launch-post category: messaging jurisdictions: [__multi__] priority: P2 intent: [messaging, LinkedIn, launch, product-announcement, social-media, B2B] related: [messaging-compliance-checker, messaging-bridge-line, messaging-allowed-claims-lawyer, messaging-allowed-claims-consumer, messaging-banned-claims-lawyer, messaging-hard-rule-preapproved-press-quotes-only] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'messaging'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Messaging — Surface Rule: LinkedIn Launch Post

## When this applies

This skill applies to LinkedIn posts announcing a product launch, major update, funding announcement, partnership, or milestone from the company's LinkedIn page or the founder/CEO's personal LinkedIn account. It also governs sponsored LinkedIn content that appears in the form of a post. LinkedIn launch posts have outsized impact in the legal tech sector — they are seen by lawyers, investors, media, and regulators simultaneously.

---

## Behavior — The LinkedIn Dual-Audience Rule

LinkedIn is a **mixed professional audience**. A post from a legal AI company's LinkedIn will be seen by:
- Lawyers (partners, associates, in-house counsel) evaluating the product
- Legal tech investors and analysts
- General professionals and potential consumer users
- Journalists and regulators

Apply **both** consumer and lawyer messaging rules. The post must not contain claims banned on either surface. Use the bridge line as the guiding frame.

---

## Post Structure — Launch Announcement

A compliant LinkedIn launch post follows this structure:

### 1. Hook (first 1–2 lines — visible before "see more")
- The first two lines are critical: they determine whether someone expands the post
- Lead with a problem statement, a milestone, or the "why now"
- Allowed: "Today we're launching [X] — built for legal professionals who spend too many hours on [pain point]."
- Allowed: "Legal understanding shouldn't require a law degree."
- Avoided: "Disrupting the legal industry" (overused; generic; triggers skepticism from lawyer audience)

### 2. What It Is (short product description)
- 2–4 sentences; stay within the bridge line
- State what the product does, not what the AI technology is
- Include jurisdictional scope if relevant: "covering Lebanon, UAE, KSA, DIFC, and ADGM from day one"
- Use factual capability framing: "drafts, reviews, and explains" — not "replaces"

### 3. Who It's For (audience framing)
- Both audiences when relevant: "For legal professionals who want to move faster — and for everyone who deserves to understand the law."
- If the launch is specifically a professional feature, focus on that audience but include a bridge-line nod to the broader mission

### 4. Social Proof (optional but powerful)
- Include one pre-approved quote from a beta user or partner if available
- All quotes must be pre-approved per [[messaging-hard-rule-preapproved-press-quotes-only]]
- Format: "Name, Role at Firm: '[quote]'"
- Never fabricate or attribute quotes before receiving written approval

### 5. Call to Action
- Clear, specific, and low-friction: "Try it free at [link]" / "Request early access" / "Read more about what we built"
- Avoid: "Get your free legal advice today" — banned

### 6. Hashtags
- Use 3–5 targeted hashtags: #LegalTech, #LegalAI, #MENA, #LegalInnovation, #[JurisdictionSpecific]
- Avoid spam-style hashtag lists
- Avoid: #LegalAdvice — associates the product with professional legal advice services

---

## Compliance Requirements

Before any LinkedIn launch post is published:

1. Full compliance check via [[messaging-compliance-checker]] — all four passes
2. Any quotes included verified via [[messaging-hard-rule-preapproved-press-quotes-only]]
3. Any new metrics or capability claims verified via [[messaging-hard-rule-bible-signoff-required]]
4. Bridge line consistency confirmed

---

## Tone

| Dimension | Guidance |
|-----------|----------|
| Register | Professional, confident — not breathless or hyperbolic |
| Voice | Founder/company voice — honest about what the product is and isn't |
| Length | 150–350 words for a launch post; longer is allowed if substance warrants it |
| Lawyer sensitivity | Do not position as a threat to legal employment; use augmentation framing throughout |
| Consumer accessibility | Avoid heavy legalese; the post will be seen by non-lawyers too |

---

## Examples

**Strong launch post opening:**
> "Today we're launching Louis — a legal AI assistant built for MENA's legal landscape. Lebanon, UAE, KSA, DIFC, ADGM. Multi-jurisdiction from day one."

**Weak (avoid):**
> "Say goodbye to expensive lawyers! Louis is here to disrupt legal services forever."

**Strong product description:**
> "Louis drafts contracts, reviews documents, and explains legal concepts — in plain English and Arabic. For law firms, it's a workbench. For everyone else, it's a guide."

**Weak:**
> "Louis replaces the need for legal advice for most situations."

---

## Related skills

- [[messaging-compliance-checker]]
- [[messaging-bridge-line]]
- [[messaging-allowed-claims-lawyer]]
- [[messaging-allowed-claims-consumer]]
- [[messaging-banned-claims-lawyer]]
- [[messaging-hard-rule-preapproved-press-quotes-only]]
