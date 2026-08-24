---
name: justice-product-demo-deep-link
description: Use when a user arrives at the Louis chat from a specific feature, use-case, or campaign page (a "deep link"), so that the demo experience opens with context already loaded and skips generic orientation. The deep-link context should pre-fill the demo's first example and tailor skill suggestions to the entry point. Works within the broader product demo system; covers all jurisdictions.
license: MIT
metadata: " id: justice.product-demo.deep-link category: justice jurisdictions: [__multi__] priority: P1 intent: [__justice__, demo, deep-link, landing-page, feature-entry, personalization] related: [justice-intent-product-demo-request, justice-product-demo-context-memory, justice-product-demo-recap, justice-result-page-routing] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'justice'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Justice — Product Demo: Deep Link

## Purpose

When a user clicks "Chat with Louis" from a specific feature page, use-case landing page, or ad campaign, the general demo intro ("Louis is a legal AI assistant…") is redundant — the user already has context. This skill maps the entry URL to a tailored demo opening, so the first message is specific, relevant, and immediately valuable.

## Inputs / signals

The deep-link context is passed as a parameter (e.g., `?demo_context=contract-review` or via referrer header parsing). The assistant should:

1. Detect or receive the entry page / campaign ID
2. Look up the mapping in the table below
3. Open the demo at the appropriate step, skipping or compressing the generic orientation

## Deep-link mapping table

| Entry page / context | Opening line | Demo focus | First example |
|---|---|---|---|
| `/features/doc-workspace` | "You were looking at the doc workspace — let me show you how it handles a real contract." | Doc workspace: create, edit, export | Create a new employment contract in the workspace |
| `/features/contract-review` | "You were checking out contract review — let me run one right now." | Contract review flow | Paste a sample clause and run a review |
| `/features/bilingual-drafting` | "Arabic + English drafting — let me show you the bilingual view." | Bilingual side-by-side draft | Draft a short NDA clause in Arabic and English simultaneously |
| `/features/skills-router` | "You were looking at the skills router — here's how it picks the right tool for each task." | Router observability + skill list | Show router decision for 3 different inputs |
| `/use-cases/law-firm` | "You were looking at how Louis works for law firms — let me walk you through a firm workflow." | End-to-end firm flow: matter → draft → review → sign | Create a matter, draft a contract, run a review |
| `/use-cases/in-house` | "You were looking at the in-house counsel workflow — let me show you contract intake to approval." | Contract intake → review → approval | Run a high-volume MSA review pass |
| `/use-cases/solo-practitioner` | "Solo practice — let me show you how Louis handles your whole workflow." | Solo workflow: draft, review, send | Generate an engagement letter |
| `/ai-features/research` | "You were checking out the research feature — let me run a quick research memo." | Legal research memo | Research a specific legal question (ask user for topic) |
| `/pricing` | "You were looking at pricing — any feature you want to try before deciding?" | User-directed; offer a quick showcase of any feature | User chooses |
| Campaign: `mena-launch` | "Welcome — Louis was built for MENA law. Let me show you Arabic drafting." | MENA + Arabic features | Arabic NDA clause |
| Campaign: `bar-prep` | "Studying for the bar? I'm Justinian — let me show you the exam prep mode." | Justinian: bar prep, flashcards | Flashcard set from UAE Labor Law |

## Behavior rules

- **Skip the generic intro** for all deep-link entries; the user knows why they're here
- **Start with a doing moment**, not an explaining moment — run the first example immediately or ask for the minimum input to run it
- **Acknowledge the entry context** briefly in the opening line (one sentence), then move to action
- **If the entry context is ambiguous** (e.g., homepage with no context): fall back to the standard [[justice-intent-product-demo-request]] demo flow
- **Do not run the deep-link flow for logged-in users** who are already working — they are not in demo mode

## Coordination with other demo skills

- After the deep-link opening, hand off to [[justice-product-demo-context-memory]] to continue capturing session context
- At session close or sign-up intent, trigger [[justice-product-demo-recap]] for a tailored wrap-up
- If the user's interest diverges from the entry page (e.g., arrived at `/features/contract-review` but starts asking about billing), pivot gracefully and update the context accordingly

## Related skills

- [[justice-intent-product-demo-request]]
- [[justice-product-demo-context-memory]]
- [[justice-product-demo-recap]]
- [[justice-result-page-routing]]
