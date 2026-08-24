---
name: unlock-cross-product-bridge
description: Use when a user in one product context would clearly benefit from moving to another product in the suite — Justinian (legal education) users who are ready for Louis (legal practice), free public-tool users who should subscribe, Louis subscribers who have enterprise-tier usage patterns, or enterprise clients who should explore white-label or API access. Applies the right bridge message at the right moment without interrupting the current task.
license: MIT
metadata: " id: unlock.cross-product-bridge category: unlock jurisdictions: [__multi__] priority: P2 intent: [product-bridge, cross-sell, tier-upgrade, justinian-to-louis] related: [unlock-contextual-upsell, unlock-case-study-relevant-to-user, unlock-empty-state-suggestions] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'unlock'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Cross-Product Bridge

## What it does

The Cross-Product Bridge identifies moments when a user's behavior signals readiness to move between products in the suite, and delivers a targeted bridge message. Unlike the Contextual Upsell (which handles tier upgrades within the same product), the cross-product bridge operates at product-level transitions.

## Product map

| From | To | Signal | Bridge message |
|---|---|---|---|
| Justinian (education) | Louis (practice) | User passes a Justinian assessment at 80%+ / completes a simulation course / asks a "real client scenario" question | "You're ready to work on real matters. Louis is the practice tool — try your first NDA draft." |
| Louis public tool (no account) | Louis subscription | User returns to the public tool 3+ times or asks a question requiring firm KB / document upload | "You're getting real use out of this — create a free account to save your work and access more." |
| Louis free / starter | Louis Pro / Business | Covered by [[unlock-contextual-upsell]] — invoke that skill | See [[unlock-contextual-upsell]] |
| Louis (individual Pro) | Louis Business / eFirm | User mentions "our team", "share this with a colleague", or "our firm's template" | "Louis Business supports team accounts with a shared firm KB and matter management. Talk to us." |
| Louis Business | Enterprise / API | User asks about integration, white-label, high-volume API, or mentions procurement process | "Louis Enterprise supports API access and custom deployment. Let's talk." |

## When to apply

### Justinian → Louis bridge
Trigger when:
- A Justinian user's session history shows they are past foundational learning and asking questions that have real practice implications ("What would I actually do if a client had this problem?")
- Justinian module completion in corporate law, contract drafting, or MENA commercial practice
- Justinian user asks to "practice on a real document"

Bridge copy:
> "You've been working through contract law in Justinian — that knowledge applies directly to real drafting work. Louis is where your peers draft actual NDAs, review counterparty documents, and run KYC checks. Want to try drafting a real NDA right now?"

### Public tool → subscription bridge
Trigger when:
- Same user (identified by browser fingerprint or soft login) returns to the public tool 3+ times in 7 days
- User attempts an action that requires a login (saving, uploading, firm KB access)
- User's session exceeds 20 minutes — signals genuine engagement

Bridge copy:
> "You've been getting real use out of Louis. Create a free account to save your work, upload documents, and access the full drafting toolkit — no credit card needed."

### Louis individual → team bridge
Trigger when:
- User says "our firm", "my team", "share with a colleague", "our template"
- User has 5+ sessions per week (power user who likely has colleagues with the same problem)
- User asks about invoice-level billing or expense reporting (signals corporate purchase intent)

Bridge copy:
> "It sounds like your whole team could benefit. Louis Business adds a shared firm knowledge base, team matter management, and billing under a single firm account. Want to see how it works?"

### Louis → Enterprise / API bridge
Trigger when:
- User mentions "integration with our system", "white-label", "our platform"
- User asks about bulk document processing, API access, or SLA guarantees
- Tenant admin asks about SOC 2, data residency, custom deployment

Bridge copy:
> "What you're describing is Louis Enterprise — custom deployment, API access, and data residency controls. Our team would love to walk you through it. [Schedule a call] or [email us]."

## Behavior rules

### Do
- Match the bridge message exactly to the signal that triggered it
- Make the next step frictionless (one click to sign up, one click to book a call)
- Show the bridge at the natural end of a task, not mid-flow
- If the user dismisses the bridge, respect it for the session and flag for email follow-up instead

### Do not
- Do not show more than one cross-product bridge message per session
- Do not combine a cross-product bridge with a contextual upsell in the same moment — choose one
- Do not bridge a user who has already been on the target product (Justinian user who previously had a Louis account — this is a re-engagement message, not a bridge)
- Do not interrupt a time-sensitive task (signing deadline, urgent research)

## Measurement

Track:
- Bridge click-through rate by bridge type
- Conversion to trial / paid on bridged product within 7 days
- Justinian → Louis conversion pipeline length (from bridge impression to first paid session on Louis)

## Examples

**Good — signal-matched**:
> User says "Can I share this draft with my colleague for review?" → "Louis Business supports shared matter files and team accounts. [Learn more about Business] [Maybe later]"

**Bad — generic**:
> User is using Louis normally → "Did you know we have other products?" (no signal, no context)

## Related skills

- [[unlock-contextual-upsell]] — handles tier upgrades within Louis (free → Pro → Business)
- [[unlock-case-study-relevant-to-user]] — social proof to support bridge conversion
- [[unlock-empty-state-suggestions]] — initial engagement for users who have just crossed into a new product
