---
name: unlock-empty-state-suggestions
description: Use when a user faces a blank surface — a new chat, an empty document editor, a matter with no files, or a first-time session — and needs curated starter suggestions to overcome cold-start friction. Suggestions are matched to the user's role, jurisdiction, and recent activity context. Invoked automatically on empty-state render. Reduces abandonment from users who don't know where to start.
license: MIT
metadata: " id: unlock.empty-state-suggestions category: unlock jurisdictions: [__multi__] priority: P2 intent: [empty-state, starter-prompts, onboarding, cold-start] related: [unlock-contextual-upsell, unlock-case-study-relevant-to-user, unlock-cross-product-bridge] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'unlock'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Empty State Suggestions

## What it does

This skill generates and presents curated starter suggestions when a user encounters a blank surface in the product — a new chat session, a fresh document editor, an empty matter, or the first-ever session. Suggestions are personalized to the user's role, jurisdiction, and recent activity, and are designed to show the most compelling available action in a single glance.

"Cold start anxiety" — not knowing where to begin with a new tool — is one of the top causes of first-session abandonment. Starter suggestions solve it by immediately demonstrating what is possible and providing a low-friction first action.

## When this applies

| Surface | Trigger condition |
|---|---|
| New chat session | Session initiated with no pre-existing messages |
| Empty document editor | Document editor opened with no content |
| New matter | Matter created with no attached documents |
| First-ever session | User's account has zero prior sessions |
| Post-logout re-entry | User logs back in after 7+ day gap |

## Behavior

### Suggestion generation

The skill generates 3–5 suggestions, not more. More than 5 creates choice overload. Fewer than 3 feels sparse.

Each suggestion is a **one-click actionable prompt** — not a description, but a real request the user can submit immediately:
- Good: "Draft a mutual NDA for a SaaS partnership in UAE (DIFC governing law)"
- Good: "Check KSA company registration for [counterparty name]"
- Good: "Review this employment contract for red flags (UAE onshore law)"
- Bad: "Explore our NDA drafting features" (feature description, not a task)

### Personalization logic

The skill reads available signals to personalize:

| Signal | Source | Applied to |
|---|---|---|
| Declared role | Onboarding | Determines which task categories to prioritize |
| Jurisdiction | IP geolocation + onboarding | Pre-fills governing law in suggestions |
| Recent activity | Session history | Continues or extends prior work |
| Industry | Self-declared or CRM | Selects relevant transaction types |
| Plan tier | Subscription data | Only suggests tasks available on the user's plan |

### Suggestion categories by role

**In-house counsel (UAE/KSA/LB focus)**:
1. "Review and redline a vendor MSA — flag non-standard risk allocation"
2. "Screen [counterparty] against UN, OFAC, and local sanctions lists"
3. "Draft a governing-law clause for a cross-border supply agreement (UAE ↔ UK)"
4. "Summarize the material terms of this executed SPA in plain English"
5. "What are the UAE onshore requirements for a company notarization?"

**Private practice — corporate/commercial**:
1. "Draft a unilateral NDA for a preliminary discussion in KSA (Arabic + English bilingual)"
2. "Run a trademark clearance search for [mark name] in Classes 35 and 42 in the GCC"
3. "Generate a DIFC-law SHA term sheet for a Series A investment"
4. "Lookup the Lebanon commercial register for [entity name]"
5. "Identify the top 5 risk clauses in this counterparty draft and suggest revisions"

**Compliance officer**:
1. "Run an AML KYC check on [entity/individual name] against all three sanctions lists"
2. "Summarize CBUAE's latest AML circular and flag any changes to our existing policy"
3. "Draft an enhanced due diligence memo template for high-risk counterparties"
4. "What are the PDPL (KSA) data retention requirements for financial institutions?"
5. "Flag any OFAC 50% Rule exposure in [entity]'s ownership structure"

**Entrepreneur / startup founder**:
1. "Draft a co-founder agreement for a UAE-incorporated startup (Abu Dhabi / ADGM)"
2. "What licenses do I need to operate a fintech in Dubai?"
3. "Explain the DIFC vs ADGM vs onshore UAE choice for my holding structure"
4. "Draft an IP assignment clause for a contractor agreement (Lebanese law)"
5. "What are my obligations as a KSA LLC owner if a partner wants to exit?"

**Legal ops**:
1. "Build a contract intake form template for MSA requests"
2. "Summarize the clause-level differences between our standard NDA and this counterparty's version"
3. "Create a closing checklist for a UAE asset purchase transaction"
4. "Generate a contract metadata extraction schema for our contract repository"
5. "Identify all indemnification clauses across these 3 uploaded agreements"

### First-time user suggestions
For a brand-new user with no profile data:
1. "Draft a simple NDA for a business discussion"
2. "Check if a company name is available in the UAE"
3. "Explain the difference between DIFC, ADGM, and onshore UAE for setting up a company"
4. "Review this contract and tell me the 3 things I should be most concerned about"
5. "What is the standard termination-for-convenience clause under English law?"

These are chosen to be immediately useful to any legal professional regardless of jurisdiction.

### Pairing with case studies
At empty state, optionally pair one suggestion block with a relevant case study ([[unlock-case-study-relevant-to-user]]):

```
[Case study card — 2–3 sentences]
------
Try something similar:
[Suggestion 1]  [Suggestion 2]  [Suggestion 3]
```

## Display format

Suggestions are presented as clickable chips or cards:
- Maximum 2 lines of text per suggestion
- Clicking a suggestion pre-fills the chat input (user can edit before submitting)
- On mobile: horizontal scroll of chips (3 visible at once)
- On desktop: 3-column grid of cards

Do not show suggestions and a tutorial at the same time — one or the other. The goal is to get the user into their first productive action as fast as possible.

## Do not

- Do not suggest tasks that require a higher plan tier than the user is on
- Do not repeat the same set of suggestions on every empty state — vary them based on context
- Do not suggest tasks the user has already completed today (check session history)
- Do not show empty state suggestions if the user has already typed something — they have their own idea
- Do not make suggestions so specific they feel invasive ("Draft an NDA for Acme Corp based on your LinkedIn profile") — personalize to role and jurisdiction, not to specific named counterparties unless the user has provided them

## Measurement

Track per suggestion:
- Click rate (which suggestions are actually clicked)
- Completion rate (user completes the task after clicking the suggestion)
- Time-to-first-action (does showing suggestions reduce time to first submitted message?)
- Return rate (do users who engage with suggestions come back?)

Run A/B tests on:
- Number of suggestions (3 vs 5)
- Specificity level (generic vs jurisdiction-specific)
- With/without paired case study

## Related skills

- [[unlock-contextual-upsell]] — if the user clicks a suggestion that requires a higher tier
- [[unlock-case-study-relevant-to-user]] — optionally paired with suggestion block
- [[unlock-cross-product-bridge]] — if user is coming from a different product and sees empty state for the first time
