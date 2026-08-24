---
name: site-use-case-router
description: Use when routing a user — via onboarding, chat intent detection, or a sales-signal — to the correct `/use-cases/:slug` marketing page. Matches the user's job-to-be-done against a catalogue of practice-area use-case pages and surfaces the right one as a deep-link, either during onboarding or after a successful task. Applies across all jurisdictions and practice areas supported by Louis.
license: MIT
metadata: " id: site.use-case-router category: site jurisdictions: [__multi__] priority: P1 intent: [__site__] related: [site-tools-router, router-intent, onboarding-flow, strategy-customers] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'site'.
Registered as a flat plugin skill.
-->


# Site — Use Case Router

## Purpose

The Use Case Router is the bridge between a user's expressed job-to-be-done and the corresponding product marketing page under `/use-cases/:slug`. It serves three contexts:

1. **Onboarding** — "What brings you here today?" → detect intent → deep-link to use-case page that shows concrete product capabilities for that workflow.
2. **Post-task engagement** — after a successful chat task, suggest a related use-case page to deepen product stickiness.
3. **Sales-signal handling** — when a conversation shows commercial intent (pricing questions, team-size queries, ROI framing), surface the most relevant use-case page to accelerate conversion.

## Use-case page catalogue

| Slug | Practice area | Primary user persona |
|---|---|---|
| `contract-drafting` | Transactional | Associates, solo practitioners |
| `contract-review` | Transactional / Risk | In-house counsel, associates |
| `legal-research` | All | Associates, students |
| `m-and-a-due-diligence` | M&A / Corporate | Senior associates, GCs |
| `employment-law` | Employment | In-house HR-legal, boutique firms |
| `litigation-prep` | Litigation | Litigation associates, barristers |
| `regulatory-compliance` | Regulatory | GCs, compliance officers |
| `startup-incorporation` | Corporate / Startup | Solo practitioners, startup founders |
| `data-privacy` | Data / Tech | In-house tech counsel, DPOs |

Each page must show **real product capabilities** for that use case — actual skill invocations, sample outputs, and (where available) ROI metrics or case studies. Never promise a feature not yet shipped.

## Routing logic

### Step 1 — Intent detection

Extract the user's primary intent signal from one of:
- Direct statement ("I need to review an NDA")
- Practice area keywords (employment, M&A, privacy, litigation)
- Document type named (share purchase agreement, employment contract, DPDP notice)
- Workflow phrase ("due diligence", "regulatory filing", "court deadline")

### Step 2 — Slug mapping

```
intent → slug mapping (deterministic):

contract drafting / NDA / SPA / MOU  → contract-drafting
contract review / redline / risk flag → contract-review
legal research / case law / statute   → legal-research
M&A / due diligence / acquisition     → m-and-a-due-diligence
employment / EOSG / termination       → employment-law
litigation / court filing / pleading  → litigation-prep
regulatory / compliance / licensing   → regulatory-compliance
incorporation / company formation     → startup-incorporation
GDPR / data privacy / DPO             → data-privacy
```

When intent is ambiguous or maps to multiple slugs, prefer the slug that matches the user's **stated persona** (e.g., in-house counsel → regulatory-compliance over contract-drafting even for contract work).

### Step 3 — Surface the link

**Onboarding context:** After intent detection, render a card or button: "Explore how Louis helps with [use case] →" linking to the use-case page.

**Post-task context:** After successful task completion, inject a soft prompt: "Want to learn more about how Louis handles [related use case]?" with the deep-link.

**Sales-intent context:** Insert the use-case page link into the chat reply naturally: "Here's how teams like yours use Louis for [use case]: [link]."

## Content standards for use-case pages

Each `/use-cases/:slug` page must include:
- **Hero** — one-sentence capability statement specific to the use case.
- **How it works** — 3–5 concrete steps with sample AI output snippets (real, not illustrative).
- **Jurisdictions supported** — explicit list; do not imply coverage where it is not yet built.
- **Testimonials / case studies** — real quotes or anonymised stats; do not fabricate.
- **ROI metric** (where available) — e.g., "Reduces NDA first-draft time from 45 min to 4 min."
- **CTA** — "Try it free" → onboarding flow with use case pre-selected.

## Edge cases

- **Unknown intent:** Do not force-route. Ask one clarifying question: "Is this for drafting, reviewing, or researching?"
- **Multiple intents in one session:** Route to the first detected intent; after task completion, offer the second.
- **Non-supported jurisdiction:** Do not route to a use-case page that claims coverage not yet available; instead acknowledge the gap and offer the closest supported alternative.

## Do not

- Route to a use-case page that does not match the user's actual task — mismatched routing destroys trust.
- Promise features not yet built on any use-case page.
- Use use-case routing as a hard-redirect that interrupts an in-progress task.

## Related skills

- [[site-tools-router]]
- [[router-intent]]
- [[onboarding-flow]]
- [[strategy-customers]]
