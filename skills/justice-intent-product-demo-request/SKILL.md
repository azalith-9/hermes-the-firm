---
name: justice-intent-product-demo-request
description: Use when the public-facing assistant detects that a user wants to see Louis in action — requesting a demo, walkthrough, or trial experience. Delivers a structured in-chat demo flow, routes to the demo page, schedules a live demo via Calendly, and tailors the demo to the user's context or the feature page they arrived from. Covers all jurisdictions; triggers sales lead capture for high-intent users.
license: MIT
metadata: " id: justice.intent.product-demo-request category: justice jurisdictions: [__multi__] priority: P1 intent: [__justice__, demo, walkthrough, trial, show-me, product-demo] related: [justice-intent-sales, justice-intent-feature-question, justice-intent-competitor-comparison, justice-product-demo-context-memory, justice-product-demo-recap] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'justice'.
Registered as a flat plugin skill.
-->


# Justice Intent — Product Demo Request

## When to use this

Trigger when any of the following patterns appear:

- "I want to see how this works"
- "Can you show me a demo?"
- "Walk me through Louis"
- "How does this work?" (when asked by a first-time visitor or about a specific feature)
- "I want to try"
- "Show me an example"
- "Can you do [X] for me?" (request to demonstrate a task, not to actually perform it as a work task)

Distinguish from genuine work tasks ("draft an NDA for me" from a signed-in user) — those should be routed to the appropriate drafting or review skill, not treated as a demo request.

## Response flow

### Option A: In-chat demo

Run the 6-step demo flow below directly in the chat interface. This is the default for visitors and trial users.

### Option B: Deep-link to demo page

Route to `/product-demo` where a structured interactive demo is hosted. Use this if the user prefers a self-guided experience or if in-chat rendering would be inadequate.

### Option C: Live demo (high-intent users)

Offer to schedule a live demo call. Detect high intent from: firm name provided, specific use case described, explicit mention of budget or timeline, team-size language ("for my firm", "for our practice"). Route to Calendly at `/product-demo/book` or the configured scheduling link.

## In-chat demo flow (6 steps)

**Step 1: Brief overview of Louis** (1 minute)
> "Louis is a legal AI assistant built specifically for MENA law firms and lawyers globally. I can draft contracts, review documents, research law, translate, and handle your full legal workflow — in Arabic, French, and English."

**Step 2: Sample drafting interaction**
> "Let me show you a quick NDA draft. Tell me: is this a one-way or mutual NDA? Who is the disclosing party? Governed by which country's law?"
> [Receive minimal inputs → generate a partial NDA draft with jurisdiction-appropriate boilerplate → show the result inline]

**Step 3: Sample review interaction**
> "Now let's try reviewing a contract. Paste any contract clause or a full document, and I'll flag risks, suggest redlines, and explain the issues — in plain language."
> [If user pastes: run a lightweight review pass → show 2–3 flags with explanations]

**Step 4: Show the skills router**
> "I have 200+ specialized legal skills — for different jurisdictions, practice areas, and task types. Here are a few relevant to what you described: [list 2–3 based on what the user mentioned]"

**Step 5: Pitch the firm features** (if applicable)
For users describing a law firm or team context:
> "For firms, Louis also handles matter management, team workspaces, billing integration, and custom skill packs for your practice area."

**Step 6: CTA**
> "Want to try it yourself? Sign up free at haqq.ai/signup — no credit card. Or book a 30-minute live demo and I'll walk you through your specific use case."

## Personalization (deep-link mode)

If the user arrived from a specific feature page, tailor the demo:

| Entry page | Demo focus |
|---|---|
| `/features/doc-workspace` | Show doc workspace: create, edit, export |
| `/features/contract-review` | Run a review on a sample clause they paste |
| `/features/bilingual-drafting` | Draft a short clause in both Arabic and English |
| `/use-cases/law-firm` | Show the full firm workflow: matter → draft → review → sign |
| `/use-cases/in-house` | Show the playbook: contract intake → review → approval |

## Sales handoff

Track demo engagement events. Flag hot leads (those who complete Step 4+, describe a real firm or case, or ask about pricing) for the sales team. Integrate with CRM via the demo analytics event stream.

See [[justice-product-demo-context-memory]] for in-session memory behavior (remember what the user said and reuse it in demo examples).

See [[justice-product-demo-recap]] for the end-of-session recap behavior.

## Related skills

- [[justice-intent-sales]]
- [[justice-intent-feature-question]]
- [[justice-intent-competitor-comparison]]
- [[justice-product-demo-context-memory]]
- [[justice-product-demo-recap]]
