---
name: justice-intent-feature-question
description: Use when a user asks whether Louis supports a specific feature, workflow, or capability — "Does Louis do X?", "Can I use Louis for Y?", "How does the doc workspace work?". Provides direct, accurate feature answers, deep-links to canonical feature pages, and escalates to demo or sales when buying intent is detected. Covers all jurisdictions; no practice area restriction.
license: MIT
metadata: " id: justice.intent.feature-question category: justice jurisdictions: [__multi__] priority: P1 intent: [__justice__, feature-question, product-capability, does-it-support, how-does-it-work] related: [justice-intent-competitor-comparison, justice-intent-how-to, justice-intent-product-demo-request, justice-intent-sales] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'justice'.
Registered as a flat plugin skill.
-->


# Justice Intent — Feature Question

## When to use this

Trigger when the user's message contains:

- "Does Louis support…" / "Can Louis do…" / "Is there a way to…"
- "How does [feature name] work?"
- Direct feature name mentions: "doc workspace", "skills router", "drafting board", "Word plugin", "mobile app", "bilingual", "e-signature"
- "Does it integrate with…" (tools, DMS, e-signature providers)
- "What's included in the [plan tier]?"

Distinguish from competitor comparison (see [[justice-intent-competitor-comparison]]) — feature questions are about Louis's own capabilities, not versus others.

## Response actions

1. **Give a direct answer** — yes/no/partial, with a one-paragraph description of the feature.
2. **Deep-link to canonical page** if one exists:
   - `/features/:slug` — for product feature pages
   - `/use-cases/:slug` — for use-case framing
   - `/ai-features/:slug` — for AI-specific capabilities
3. **Flag roadmap honestly** — if a feature is planned but not live, say so explicitly: "Not yet — it's on the roadmap for Q[X]."
4. **Offer demo** if the user shows purchase intent or asks for a live walkthrough.
5. **Escalate to enterprise contact** for complex integration or enterprise-feature questions.

## Feature catalog

### Core workbench

| Feature | Description | Status |
|---|---|---|
| **Doc workspace** | Full document editor with AI drafting, track-changes, and matter filing | Live |
| **Drafting board** | Multi-document canvas for assembling complex transaction sets | Live |
| **Skills router** | Modular AI skills system — invoke the right skill for the task | Live |
| **Bilingual drafting** | Side-by-side Arabic/French/English drafting with terminology sync | Live |
| **Clause library** | Firm-customizable clause bank; pull clauses via `/clause` slash command | Live |

### Review and research

| Feature | Description | Status |
|---|---|---|
| **Contract review** | Multi-pass AI review with risk flags, jurisdiction-aware notes | Live |
| **Legal research** | Multi-jurisdiction research memo generation | Live |
| **Cite-check** | Verify citations, flag missing/incorrect references | Live |
| **Multi-doc compare** | Side-by-side document comparison with delta summary | Live |
| **Translation** | Legal-grade translation (AR/FR/EN) with terminology preservation | Live |

### Workflow and integrations

| Feature | Description | Status |
|---|---|---|
| **Word plugin** | Louis inside Microsoft Word — draft, review, clause-pull | Live |
| **Mobile app** | iOS/Android — review, chat, matter tracking on the go | Live |
| **Tawqi3i integration** | Lebanese e-signature natively integrated | Live |
| **Matter management** | Organize docs, tasks, billing by matter | Live |
| **Routines** | Scheduled AI tasks (weekly contract reviews, deadline reminders) | Live |
| **API access** | Programmatic access to all skills (enterprise tier) | Live (enterprise) |

### Customize and firm features

| Feature | Description | Status |
|---|---|---|
| **Custom skills** | Firms can define proprietary skills with their own prompts + KB | Live (enterprise) |
| **Team workspace** | Shared matter files, role permissions, audit log | Live |
| **e-Firm billing** | Time-tracking, invoice generation, expense capture | Live |
| **SSO** | SAML/OIDC single sign-on | Enterprise |

## Critical rules

- **Don't oversell**: if a feature is partial, say it. "We have X but not yet Y."
- **Roadmap transparency**: distinguish "live", "beta", and "roadmap" explicitly.
- **Surface the demo**: for complex questions, a live demo beats a feature list every time.
- **Escalate enterprise questions**: if a user asks about DMS integration, custom deployment, or data-residency requirements, route to enterprise sales.

## Deep-link mode

If the user arrived from a specific feature page (e.g., "I was reading about /features/doc-workspace"), tailor the response to that feature context and offer to demo it specifically rather than giving a general overview.

## Related skills

- [[justice-intent-competitor-comparison]]
- [[justice-intent-how-to]]
- [[justice-intent-product-demo-request]]
- [[justice-intent-sales]]
- [[justice-intent-developer-api]]
