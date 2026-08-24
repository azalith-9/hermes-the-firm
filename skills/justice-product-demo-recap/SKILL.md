---
name: justice-product-demo-recap
description: Use at the end of a product demo session to generate a warm, specific, non-salesy recap that summarizes what the user discovered, quantifies estimated time savings, and provides a personalized next step. Designed to convert demo engagement into trial sign-up or booked call. Pairs with context-memory and deep-link skills to draw on the session's captured context.
license: MIT
metadata: " id: justice.product-demo.recap category: justice jurisdictions: [__multi__] priority: P2 intent: [demo, recap, conversion, session-close, next-steps] related: [justice-product-demo-context-memory, justice-intent-product-demo-request, justice-intent-sales, justice-product-demo-deep-link] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'justice'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Justice — Product Demo: Recap

## Purpose

A demo that ends with "any questions?" converts poorly. A demo that ends with a specific, personalized recap — "here's what you saw, here's what it means for your practice, here's your next step" — converts significantly better. This skill generates that recap automatically at the close of a demo session.

## Trigger conditions

Trigger the recap when any of the following occur:

- User says "thanks", "great", "that's helpful", "I think I've seen enough", "what's next?"
- User asks about pricing or sign-up (transition to recap + CTA)
- Demo has reached Step 5+ of the [[justice-intent-product-demo-request]] flow and natural pause
- User has been inactive for > 3 minutes at the end of a demo session
- User explicitly requests a summary

## Recap structure

### Section 1: Top 3 wins (features the user engaged with)

Draw from [[justice-product-demo-context-memory]] to identify which features the user demonstrated interest in — questions asked, examples run, visible engagement. List 3, personalized:

> "Here's what stood out in your demo today:
> 1. **Bilingual NDA drafting** — you saw how the Arabic and English versions stay in sync as you edit
> 2. **Contract review** — the system flagged the missing governing law clause in under 30 seconds
> 3. **Matter management** — you asked about team access and saw how documents organize by matter automatically"

### Section 2: Time saved estimate

Calculate based on session context (volume, doc type, workflow):

| Context | Estimate |
|---|---|
| Solo practitioner, 10 contracts/month | "At your volume, Louis typically saves 8–12 hours per month on drafting and review" |
| 5-person firm, 30 contracts/month | "For a firm your size, typical time savings are 30–50 hours per month across the team" |
| No volume data captured | "Most users report cutting document drafting time by 60–70% for standard contract types" |

Frame conservatively — do not over-promise. These are representative averages, not guarantees.

### Section 3: Recommended next steps

Personalize to what the user showed interest in:

| Signal | Recommended next step |
|---|---|
| High buying intent (pricing questions, firm details shared) | "Book a 30-minute call with our team to configure Louis for [firm name]" + Calendly link |
| Curious but not yet buying | "Start a free trial — no credit card needed. Your first 5 documents are on us." |
| Specific feature interest | "Try [feature] yourself — here's a direct link to get started: [feature deep-link]" |
| Student / bar prep interest | "Sign up for the student plan and start your [exam] prep today" |
| Enterprise / IT involved | "We can run a formal evaluation including a security review — here's how to start" |

### Section 4: Pricing snapshot

One-line pricing summary for the user's apparent use case:

> "For a solo practitioner, the Pro plan is [price]/month — or start free and upgrade when you're ready."

Do not run a full pricing lecture. One sentence. Link to `/pricing` for details.

### Section 5: Trial / onboarding CTA

Close with one clear, simple call to action:

- **Primary CTA**: "Sign up free — no credit card: haqq.ai/signup"
- **Alternative CTA**: "Book a 30-minute live demo: haqq.ai/demo/book"
- **For enterprise**: "Start your firm evaluation: haqq.ai/enterprise"

## Tone

- Warm and specific — this is a conversation closer, not a sales pitch
- Specific details from the demo > generic praise ("You saw how the bilingual draft worked for your MSA" > "Louis is great at drafting")
- Never pushy — present the next step as easy and low-commitment
- Match the user's language (Arabic / French / English)

## Integration

Pair with [[outreach-userflow-analyzer]] (if available) for session engagement insights to feed back into the sales pipeline. Demo session events (steps completed, features engaged, time in session) should be logged for CRM handoff.

## Related skills

- [[justice-product-demo-context-memory]]
- [[justice-intent-product-demo-request]]
- [[justice-intent-sales]]
- [[justice-product-demo-deep-link]]
