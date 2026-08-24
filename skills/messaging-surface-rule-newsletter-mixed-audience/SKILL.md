---
name: messaging-surface-rule-newsletter-mixed-audience
description: "Use when drafting or reviewing email newsletter content for a legal AI assistant where the subscriber list includes both lawyers and non-lawyer consumers — such as a general product newsletter, a legal tech update, or a monthly digest. Defines how to handle dual-audience copy in a single email: which sections to segment, which claims to use, how to manage the subscriber experience when lawyer and consumer readers receive the same content, and the specific compliance requirements for email marketing."
license: MIT
metadata: " id: messaging.surface-rule.newsletter-mixed-audience category: messaging jurisdictions: [__multi__] priority: P2 intent: [messaging, newsletter, email-marketing, mixed-audience, B2C, B2B] related: [messaging-compliance-checker, messaging-bridge-line, messaging-allowed-claims-consumer, messaging-allowed-claims-lawyer, messaging-banned-claims-consumer, messaging-surface-rule-waitlist-email] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'messaging'.
Registered as a flat plugin skill.
-->


# Messaging — Surface Rule: Newsletter (Mixed Audience)

## When this applies

This skill applies to **email newsletters sent to a subscriber list that includes both lawyers and non-lawyers** — typically the main product newsletter, investor update distribution, or any list that has grown organically across user types. A mixed-audience newsletter is one of the harder messaging challenges: it must serve two audiences with different sensitivities in a single sequential document.

The alternative — running fully separate lawyer and consumer newsletters — is ideal but operationally complex. This skill defines how to manage both audiences within one email when segmentation is not yet feasible.

---

## Behavior — The Mixed Newsletter Rule

The core rule: apply the **more conservative of the two** applicable messaging standards to any claim that appears in a shared section of the email. When a section can be segmented or marked as audience-specific, use the appropriate rule for that audience.

---

## Newsletter Structure for Mixed Audiences

### Recommended structure

| Section | Audience | Rule |
|---------|----------|------|
| Header / subject line | Both | Bridge line territory only; no banned claims for either audience |
| Opening (intro paragraph) | Both | Bridge line; general product news; no audience-specific claims |
| Feature spotlight — consumer | Consumer (labelled or segmented) | Consumer allowed claims; "legal information" framing |
| Feature spotlight — professional | Lawyer (labelled or segmented) | Lawyer allowed claims; productivity and capability framing |
| Company news / milestone | Both | Factual; bridge line consistent |
| Content / education section | Both | Legal information content (not legal advice); educational framing |
| CTA | Audience-appropriate | Separate CTAs for consumer tier and professional tier where possible |
| Footer | Both | Standard legal disclaimer; unsubscribe; both tier links |

### Subject line rules

- Subject lines reach the full mixed list — apply bridge line rules and the more conservative claim standard
- Allowed: "Legal understanding for everyone — see what's new in Louis"
- Allowed: "New: Multi-jurisdiction contract review — LB, UAE, KSA"
- Blocked: "Skip the lawyer — Louis does it for you"
- Blocked: "Replace your associates with AI drafting"
- No outcome claims in subject lines: "Win your contract negotiation with Louis" — blocked

### Preheader text

- Same rules as subject line
- Preheader + subject line read together — ensure combined message is compliant

---

## Segmented Sections (Recommended Approach)

When the ESP (email service provider) supports dynamic content or segmentation, mark sections as audience-specific:

- **[For Lawyers]** — section visible only to professional-tier subscribers
- **[For Everyone]** — section visible to all
- **[For Individual Users]** — consumer-tier only

Segmented sections allow:
- The lawyer section to use productivity claims and professional vocabulary
- The consumer section to use situation-driven plain-language framing
- Neither section to appear to the wrong audience

If segmentation is not available, default to the more conservative standard for all shared sections.

---

## Content Section — Legal Information in Newsletters

Mixed-audience newsletters often include a content section: legal updates, a knowledge piece, or a jurisdiction explainer. This content must:

- Be framed as **legal information**, not legal advice
- Include a disclaimer if discussing a specific legal topic: "This is general information about [topic] in [jurisdiction]. For advice specific to your situation, consult a qualified lawyer."
- Use plain language accessible to non-lawyers while remaining accurate for lawyer readers
- Not make claims about the newsletter constituting legal guidance

---

## Email Marketing Compliance

All emails must comply with applicable email marketing law:

| Framework | Requirement |
|-----------|-------------|
| UAE Electronic Transactions Law | Commercial emails require clear sender identification and opt-out |
| GDPR (for EU subscribers) | Consent-based marketing; clear unsubscribe; data processing disclosure |
| CAN-SPAM (US subscribers) | Accurate subject lines; physical address in footer; unsubscribe mechanism |
| Lebanon (pending e-commerce law) | Best practice consent and opt-out |
| KSA (Anti-Spam Regulation) | Consent required; opt-out mandatory |

All commercial newsletters must include:
- Sender name and email address (not spoofed)
- Physical or registered address in footer
- One-click unsubscribe link
- Clear identification that the email is a commercial communication if it is one

---

## Examples

**Strong mixed-audience opening paragraph:**
> "This month in Louis: new multi-jurisdiction contract review, KSA employment coverage expansion, and a new plain-language explainer on DIFC arbitration clauses — whether you're a lawyer or you're just trying to understand your contract."

**Weak (apply bridge line fix):**
> "This month: why you don't need a lawyer for most contract situations — and how Louis handles it for you."

---

## Related skills

- [[messaging-compliance-checker]]
- [[messaging-bridge-line]]
- [[messaging-allowed-claims-consumer]]
- [[messaging-allowed-claims-lawyer]]
- [[messaging-banned-claims-consumer]]
- [[messaging-surface-rule-waitlist-email]]
