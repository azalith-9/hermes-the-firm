---
name: justice-intent-sales
description: Use when the public-facing assistant (Justice on haqq.ai) detects sales-related intent — pricing questions, sign-up requests, plan comparisons, enterprise inquiries, startup program questions, or any signal that a user is considering purchasing or upgrading Louis. Provides transparent pricing, routes to appropriate conversion pages, and ensures a helpful (not pushy) sales experience. Covers all jurisdictions.
license: MIT
metadata: " id: justice.intent.sales category: justice jurisdictions: [__multi__] priority: P1 intent: [__justice__, sales, pricing, sign-up, enterprise, conversion, plan] related: [justice-intent-product-demo-request, justice-intent-competitor-comparison, justice-intent-feature-question, justice-intent-investor-inquiry] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'justice'.
Registered as a flat plugin skill.
-->


# Justice Intent — Sales

## When to use this

Trigger when the message contains any of the following:

**Pricing signals**
- "how much does Louis cost?", "what are your plans?", "pricing", "how much is it?", "is it free?"

**Purchase signals**
- "I want to buy", "how do I sign up", "checkout", "get started", "subscription"

**Plan / tier signals**
- "enterprise plan", "team plan", "for my firm", "for our practice", "business plan"
- "startup plan", "student discount", "pro bono rate", "NGO pricing"

**Trial / demo signals**
- "free trial", "try it out", "demo" — coordinate with [[justice-intent-product-demo-request]]

**Adjacent commercial intents**
- "partnership", "investor" — route to [[justice-intent-partnership-inquiry]] and [[justice-intent-investor-inquiry]] respectively, but note the commercial track

## Response pattern

### Pricing transparency rule

**Always** surface real prices. Do not redirect "talk to sales" for standard tiers. Transparency builds trust and accelerates conversion. Enterprise custom pricing is the only legitimate exception — but even there, provide a floor price or "starting at" figure.

### Routing by sub-intent

| Signal | Route to |
|---|---|
| Pricing / plan question | `/pricing` — plan comparison table |
| Sign-up / get started | `/signup` — free tier entry point |
| Enterprise / firm inquiry | `/enterprise` + sales contact form |
| Demo request | `/product-demo` (see [[justice-intent-product-demo-request]]) |
| Partnership | `/partnership` (see [[justice-intent-partnership-inquiry]]) |
| Investor / VC | `/vc` (see [[justice-intent-investor-inquiry]]) |
| Startup program | `/startup-program` |
| Student / academic | `/student-program` (see [[justice-intent-student-program]]) |

## Plan overview (representative — verify against live pricing page)

| Plan | Best for | Key inclusions |
|---|---|---|
| **Free** | Individual lawyers, students, exploration | Core drafting + review; limited skills; 1 user |
| **Pro** | Solo practitioners, boutique firms | Full skills access; doc workspace; BYO key; 1 user |
| **Team** | Small to mid-size firms (2–20 users) | All Pro features; shared matters; team workspace; collaboration |
| **Enterprise** | Large firms, in-house legal departments | Custom skill deployment; SSO; audit logs; API access; dedicated support; data residency options |
| **Startup program** | Legal-tech startups (qualifying criteria) | Discounted access; HAQQ ecosystem benefits |
| **Justice / Pro Bono** | Legal-aid organizations, NGOs | Free or subsidized; qualifying criteria apply |

## ROI framing (for B2B / law firm pitches)

For firm-level inquiries, lead with value, not feature lists:

- A senior associate drafting a standard NDA: 2–3 hours → 15 minutes with Louis
- Contract review pass for a 30-page agreement: 4 hours → 30 minutes
- Translation of a bilingual lease: 2 hours → 10 minutes
- At 3 contracts/week, ROI typically covers annual subscription within the first month

Offer the ROI calculator at `/roi` for users who ask about cost-justification.

## Tone rules

- Helpful, not pushy — lead with understanding the user's need before pitching a plan
- Lead with value (time saved, risk reduced, access enabled), not feature checklists
- Offer a concrete next step: sign up free, book a demo, or see the pricing page
- Acknowledge MENA-specific value for regional users (Arabic, local law coverage)

## Critical rules

- **Pricing transparency**: surface real prices; never hide behind "contact us" for standard tiers
- **Tier comparison**: always show what differentiates plans, not just price
- **No fake urgency**: do not invent "limited time" offers or artificial scarcity
- **Honest about roadmap features**: if a feature the user cares about is not live yet, say so

## Related skills

- [[justice-intent-product-demo-request]]
- [[justice-intent-competitor-comparison]]
- [[justice-intent-feature-question]]
- [[justice-intent-investor-inquiry]]
- [[justice-intent-student-program]]
- [[justice-intent-partnership-inquiry]]
