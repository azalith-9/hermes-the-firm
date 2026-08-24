---
name: messaging-surface-rule-in-app-non-lawyer-fork
description: Use when writing or reviewing in-app copy, onboarding messages, tooltips, upsell prompts, or notifications displayed to non-lawyer consumer users of a legal AI assistant. The non-lawyer fork uses empowering plain-language framing, situational prompts, and "legal understanding" positioning — always distinct from legal advice. Applied by messaging-compliance-checker for any in-app asset tagged to a consumer or non-professional persona.
license: MIT
metadata: " id: messaging.surface-rule.in-app-non-lawyer-fork category: messaging jurisdictions: [__multi__] priority: P2 intent: [messaging, in-app, consumer, non-lawyer, UX-copy, onboarding] related: [messaging-compliance-checker, messaging-allowed-claims-consumer, messaging-banned-claims-consumer, messaging-surface-rule-in-app-lawyer-fork, onboarding-b2c-vs-b2b-fork] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'messaging'.
Registered as a flat plugin skill.
-->


# Messaging — Surface Rule: In-App Non-Lawyer Fork

## When this applies

Once a user has been classified as a **non-lawyer consumer** (via persona quiz default, email domain, or explicit self-identification — see [[onboarding-b2c-vs-b2b-fork]]), all in-app copy shown to that user follows the consumer-fork rules defined here. This covers:

- Welcome and onboarding screens
- Feature discovery tooltips
- Empty-state prompts across all product areas
- Upsell and plan-upgrade prompts
- In-product notifications and status messages
- Error messages and escalation copy
- Help text and guidance overlays

Consumer users are private individuals, SME founders, students, and anyone who is not a licensed legal practitioner. The in-app experience must be empowering, plain-language, and never imply the product provides legal advice.

---

## Behavior — The Consumer Voice

In-app copy in the consumer fork assumes the user:
- Has no formal legal training
- Is dealing with a real situation that feels confusing or stressful (a contract to sign, a landlord dispute, a job loss, a business to start)
- Needs orientation, plain-language explanation, and process guidance
- Is not looking for a lawyer replacement but for enough understanding to feel in control

Copy must reflect these assumptions. Use plain English. Ground every message in the user's situation. Avoid jargon — if legal terminology is essential, always explain it. End complex-situation guidance with a "talk to a lawyer" prompt.

---

## Copy Rules by In-App Location

### Onboarding / Welcome Screen

| Element | Consumer fork rule |
|---------|------------------|
| Welcome headline | Warm, empowering: "Welcome. Let's make sense of your legal situation." |
| Sub-copy | State what the tool does: "Louis explains your rights, translates legal jargon, and helps you prepare for any legal situation." |
| Disclaimer | Prominent and plain: "Louis provides legal information, not legal advice. For complex situations, we'll tell you when to speak to a lawyer." |
| First action | Situational prompt chips: "I got a contract to sign", "I have a landlord issue", "I'm starting a business" |

### Feature Tooltips and Discovery

- Lead with what the user gets, in their language
- "Upload your lease and Louis will explain every clause in plain English." (not "AI-powered document analysis")
- Use empathy phrases at the start of complex features: "Contracts can be confusing. Here's what Louis will check for you."
- Always end document-generation tooltips with: "Your draft is a starting point — a lawyer can review it before you use it."

### Empty-State Prompts

- Situational and inviting: "What are you trying to figure out today?"
- Persona-aware chips: for consumer users, offer: "Explain this contract", "Know my rights", "Start a business", "Write a basic agreement"
- Never: "No documents yet — upload one." (not actionable enough for a non-technical consumer)

### Upsell / Plan Upgrade Prompts

- Frame around access to more help, not capability metrics
- "For deeper analysis and longer documents, upgrade to Louis Pro — from $[X]/month."
- Value anchor allowed: "That's less than an hour of lawyer time — for a whole month of legal clarity."
- Never: "Save thousands on lawyer fees" — banned under [[messaging-banned-claims-consumer]]

### Error and Escalation Copy

- Empathetic: "We couldn't analyse that document. Make sure it's a standard contract or agreement — and try again."
- Escalation prompt: "This situation sounds complex. For matters involving [court proceedings / criminal issues / children], please speak to a qualified lawyer."
- Use warm language; do not leave the user feeling abandoned: "Louis can help with a lot — but for this situation, a lawyer's guidance is essential."

### "Talk to a Lawyer" Trigger

In-app copy for consumer users must always include a "talk to a lawyer" trigger when:
- The user's described situation involves urgent risk (eviction, employment termination, debt enforcement)
- The document is high-stakes and finalising a legal position (not just exploring)
- The user asks about criminal, family law, or court proceedings

The trigger copy: "For this situation, speaking to a qualified lawyer is important. Louis can help you prepare — but your lawyer should make the final call."

---

## Banned Patterns in Consumer Fork

These patterns are blocked on the consumer fork:

- "No lawyer needed" — [[messaging-banned-claims-consumer]] absolute ban
- "Legal advice" used to describe what Louis provides — UPL trigger
- "You'll win" or any outcome framing
- Technical legal jargon without explanation (not banned but fails accessibility bar)
- Cold transactional language ("Your session has expired. Log in to continue.") — consumer fork uses warmer language

---

## Examples

**Strong consumer-fork in-app copy:**
> "Your lease looks like a standard residential rental. Louis spotted 2 clauses that could be negotiated — here's what they mean and how to approach it. Before you sign, it's worth a 30-minute lawyer check if anything worries you."

**Weak (avoid in consumer fork):**
> "Contract analysis complete. 2 flags identified. Review report."

**Strong upgrade prompt:**
> "You've asked 5 questions this month. Upgrade to Pro for unlimited questions, document analysis, and multi-jurisdiction coverage — for less than the cost of one lawyer consultation."

**Weak upgrade prompt (avoid):**
> "Free tier limit reached. Upgrade to continue."

---

## Related skills

- [[messaging-compliance-checker]]
- [[messaging-allowed-claims-consumer]]
- [[messaging-banned-claims-consumer]]
- [[messaging-surface-rule-in-app-lawyer-fork]]
- [[onboarding-b2c-vs-b2b-fork]]
- [[onboarding-empty-state-prompts]]
