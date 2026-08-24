---
name: messaging-surface-rule-haqq-ai-homepage
description: Use when writing or reviewing copy for the main public homepage of a legal AI assistant. Defines the specific messaging constraints, section-level rules, and claim hierarchy for the homepage surface — which must serve both consumer and professional audiences simultaneously and is the primary surface for both first impressions and regulatory scrutiny. Applied as part of the messaging-compliance-checker pre-publication gate.
license: MIT
metadata: " id: messaging.surface-rule.haqq-ai-homepage category: messaging jurisdictions: [__multi__] priority: P2 intent: [messaging, homepage, surface-rule, B2C, B2B, mixed-audience] related: [messaging-compliance-checker, messaging-bridge-line, messaging-allowed-claims-consumer, messaging-allowed-claims-lawyer, messaging-banned-claims-consumer, messaging-surface-rule-landing-page-ab] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'messaging'.
Registered as a flat plugin skill.
-->


# Messaging — Surface Rule: HAQQ AI Homepage

## When this applies

This skill governs all copy appearing on the main public homepage (`haqq.ai` or equivalent root domain). The homepage is a **mixed-audience surface**: it is the first public-facing touchpoint for consumers discovering the product through search, social, or word of mouth, and simultaneously the first impression for lawyers, investors, and partners evaluating the company. It must pass both consumer and professional messaging rules at every section.

Apply this skill whenever:
- Homepage hero copy is being written or revised
- A new section is added to the homepage
- A/B tests are run on homepage headlines or CTAs
- The homepage is reviewed for compliance before a launch or campaign

---

## Section-Level Rules

### Hero (above the fold)

| Element | Rule |
|---------|------|
| Headline | Must be consistent with or derived from the bridge line; no outcome guarantees; no "replaces lawyers" framing |
| Sub-headline | Can be audience-specific (consumer OR professional); if mixed, use bridge line territory |
| Primary CTA | "Start free" or "Try Louis" — avoid "Get legal advice" or any UPL-triggering verb |
| Secondary CTA | "For law firms →" — allows homepage to bifurcate audiences from the first view without compromising either message |

**Approved hero framings:**
- "Legal understanding, for everyone." + "And for law firms — faster, smarter legal work."
- "Know your rights. Understand your contracts. Prepare for what's next."
- "Legal clarity — whether you're a first-time renter or a partner at a 200-person firm."

**Blocked hero framings:**
- "No lawyer needed."
- "AI-powered legal advice."
- "Replace your associates with AI."

### Value Proposition Section

- Present both consumer and professional value propositions in clearly separated visual or copy blocks
- Consumer block: "Helps you understand your legal situation" framing
- Professional block: productivity, speed, multi-jurisdiction coverage framing
- Do not blend the audiences in a single paragraph

### Social Proof / Testimonials

- All testimonials must be pre-approved per [[messaging-hard-rule-preapproved-press-quotes-only]]
- Do not include testimonials that contain outcome guarantees or banned claims — even if the speaker said it
- Show both consumer and professional testimonials where possible; avoid a page that reads as exclusively B2B or exclusively B2C

### Feature Section (How It Works)

- Frame features around user actions and understanding, not around the AI replacing professional judgment
- "Upload a contract and Louis explains every clause in plain language" — allowed
- "Louis reviews your contract so you don't need a lawyer" — banned

### Pricing Section (if present on homepage)

- Lead with free tier per [[messaging-pricing-framing-b2c]]
- Value anchor vs billable hour is allowed — see that skill for precise framing
- Do not make financial savings guarantees

### Trust / Compliance Section

- This section should explicitly state the product's positioning ("legal information, not legal advice") to proactively address UPL concerns
- Reference privacy standards, data security, and any applicable certifications
- Jurisdictional disclaimer: "Coverage and functionality vary by jurisdiction — see our coverage page"

### Footer

- Standard legal disclaimer: "Louis is a legal information tool, not a legal advice provider. For legal advice, consult a licensed lawyer in your jurisdiction."
- Privacy policy, terms of service, and copyright links required

---

## Compliance Check Requirements

Before any homepage copy ships:
1. Run through [[messaging-compliance-checker]] (all four passes)
2. Verify all testimonials against the press-quotes register
3. Confirm any new claims are in the messaging bible per [[messaging-hard-rule-bible-signoff-required]]
4. Confirm bridge line consistency across all sections
5. Confirm legal disclaimer is present and visible

---

## A/B Testing on the Homepage

Homepage A/B tests are permitted but require:
- Both variants to pass the compliance check before the test runs
- Neither variant to introduce claims outside the bible
- A/B test results to inform bible updates only after legal review confirms the winning variant is compliant

See [[messaging-surface-rule-landing-page-ab]] for landing page A/B-specific rules.

---

## Related skills

- [[messaging-compliance-checker]]
- [[messaging-bridge-line]]
- [[messaging-allowed-claims-consumer]]
- [[messaging-allowed-claims-lawyer]]
- [[messaging-banned-claims-consumer]]
- [[messaging-surface-rule-landing-page-ab]]
- [[messaging-hard-rule-bible-signoff-required]]
