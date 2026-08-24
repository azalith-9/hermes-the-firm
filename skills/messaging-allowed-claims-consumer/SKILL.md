---
name: messaging-allowed-claims-consumer
description: Use when drafting or reviewing consumer-facing copy, social posts, ads, email campaigns, or marketing materials for a legal AI assistant. Defines the precise framing, outcome statements, and channel-specific tone that are permitted when addressing non-lawyer end users — positioning the product as a legal information and orientation tool, not a legal advice or practice replacement service. Pair with messaging-banned-claims-consumer to establish the full boundary.
license: MIT
metadata: " id: messaging.allowed-claims-consumer category: messaging priority: P0 intent: [messaging, consumer, marketing, copy, claims, B2C, UPL] related: [messaging-banned-claims-consumer, messaging-bridge-line, messaging-allowed-claims-lawyer, messaging-compliance-checker, messaging-outcome-claims-allowed] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'messaging'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Messaging — Allowed Consumer Claims

## When this applies

This skill governs all copy directed at **non-lawyer consumers** (the B2C audience): individuals facing a legal situation — employment dispute, contract review, family matter, business start-up, landlord/tenant issue, immigration query — who are not licensed legal professionals. It applies to:

- Homepage hero and sub-sections
- Social media ads and organic posts (Instagram, TikTok, Meta, Twitter/X)
- Search and display advertising
- Email campaigns (waitlist, onboarding, retention)
- In-app copy visible to consumer-tier users
- Influencer brief copy

If copy could be read by both consumers and lawyers, use the more restrictive consumer rules.

---

## Behavior — The Permitted Frame

The product is a **legal information and orientation tool**. Every allowed claim must fit within this frame. The operative question: "Does this claim assert that the product replaces, substitutes for, or provides the equivalent of advice from a licensed lawyer?" If yes, it is banned. If no, it may be allowed — subject to tone rules below.

---

## Allowed Framing (Verbatim and Paraphrased)

These phrases and their close variants are pre-cleared for consumer surfaces:

| Claim type | Allowed formulation |
|------------|---------------------|
| Understanding | "Helps you understand your legal situation" |
| Orientation | "Orients you to the law" |
| Preparation | "Prepares you for a conversation with a lawyer" |
| Information | "Provides legal information (not legal advice)" |
| Better questions | "Knows the rules so you can ask better questions" |
| Template generation | "Drafts a starting template you can review with a lawyer" |
| Plain language | "Translates legal jargon into plain English" |
| Process | "Tells you what to expect from the process" |
| Rights awareness | "Helps you know your rights" |
| Option mapping | "Shows you what your options might be" |

**Always** append "review with a lawyer" framing when templates or document drafts are involved. No template or draft should be presented as final or ready-to-sign without that qualifier.

---

## Allowed Outcome Claims

These are the permitted outcome-level statements for consumers. Each must be accurate and not overstate capability:

- **Legal understanding** — "I understand what this contract means"
- **Legal orientation** — "I know where to start"
- **Awareness of rights** — "I know what I'm entitled to in this situation"
- **Knowledge of options** — "I understand what choices I have"
- **Procedural preparation** — "I know what to expect at the hearing"
- **Template generation** — "I have a starting draft to take to my lawyer"

Each claim must be framed around what the *user* achieves, not what the product guarantees. Say "helps you understand" not "you will understand."

---

## Tone for Consumer Marketing

| Dimension | Guidance |
|-----------|----------|
| Register | Empowering, not intimidating |
| Language level | Plain English (Flesch-Kincaid 8th grade target for digital ads) |
| Second person | Use "you" throughout — not "users" or "clients" |
| Situational | Ground claims in relatable life events: a job loss, a rental dispute, a business launch, a family matter |
| Reassuring | Acknowledge that legal situations are stressful before presenting the tool as help |
| Not prescriptive | Do not tell the user what outcome they will achieve; describe the process the tool supports |

**What empowering looks like in practice:**
- "You shouldn't have to hire a lawyer just to understand what a contract says."
- "Know your rights — before you need a lawyer."
- "Legal clarity, in plain language."

---

## Channel-Specific Rules

### Instagram / TikTok
- Visual, situation-driven storytelling ("You just got a lease renewal with new terms…")
- Lead with the user's problem; the product is the resolution mechanism
- Maximum 1 call to action
- Plain language; no citations, no legalese in copy
- Avoid anything that reads like a legal ruling or verdict claim

### Meta / Google Display Ads
- Jurisdiction-specific where possible ("Help with your Saudi employment contract", "Know your UAE tenant rights")
- Use situational micro-copy: "Got a non-compete? Here's what it means."
- No guarantee language; no outcome specificity

### LinkedIn (B2C crossover)
- More measured, professional register
- Slightly longer form allowed (200–300 words)
- Can reference the tool's knowledge base, coverage, or accuracy
- Still consumer rules apply; do not claim lawyer-level competence

### Email (waitlist, onboarding, retention)
- Warm, helpful, conversational
- Zero jargon in subject lines
- First email: set expectations ("Louis is a legal information assistant — here's what that means")
- Subsequent emails: situational use cases ("Starting a business this month? Here's what contracts you'll need.")

### Search Ads
- Jurisdiction-specific ad groups (KSA, UAE, LB, UK, US)
- Keywords: "understand contract", "know my rights", "legal help without a lawyer" — allowed
- Keywords to avoid: "legal advice", "lawyer replacement", "legal services" — may trigger bar advertising concerns

---

## Examples

**Allowed:**
> "Louis explains what your employment contract means — in plain language. So you can ask better questions when you talk to a lawyer."

**Allowed:**
> "Understand your lease, your rights, and what you can negotiate — before you sign."

**Not allowed (see [[messaging-banned-claims-consumer]]):**
> "No lawyer needed — Louis handles it."

**Not allowed:**
> "Win your case with Louis."

---

## Edge Cases

| Situation | Rule |
|-----------|------|
| User-generated testimonial referencing legal advice | Do not amplify or publish without legal-framing edit |
| Celebrity or influencer using "legal advice" in sponsored post | Correct in brief and require revision before publication |
| Comparison ad vs lawyer costs | Allowed if framed as "understanding vs fees" not "replacement vs fees" — see [[messaging-pricing-framing-b2c]] |
| Crisis situations (domestic violence, urgent eviction) | Add "Seek immediate legal counsel" regardless of any other copy |

---

## Do not

- Imply the product gives legal advice, legal opinions, or legal representation
- Promise specific legal outcomes
- Suggest that using the product eliminates the need for a lawyer
- Use the word "free legal advice" — even if the product has a free tier
- Reference specific case wins or dollar amounts recovered

---

## Related skills

- [[messaging-banned-claims-consumer]]
- [[messaging-bridge-line]]
- [[messaging-allowed-claims-lawyer]]
- [[messaging-compliance-checker]]
- [[messaging-outcome-claims-allowed]]
- [[messaging-pricing-framing-b2c]]
