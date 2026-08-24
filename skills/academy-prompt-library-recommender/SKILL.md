---
name: academy-prompt-library-recommender
description: Use when a user needs help discovering which prompts in the 152-prompt library are most relevant to their role, jurisdiction, and recent work. Produces personalized prompt recommendations with progressive disclosure (3–5 at a time), and learns from user engagement signals to improve future recommendations. Triggers on "what should I try?", "show me useful prompts", or when a user profile indicates a gap between their stated role and their actual usage patterns.
license: MIT
metadata: " id: academy.prompt-library-recommender category: academy jurisdictions: [__multi__] priority: P3 intent: [__customer-facing__, discovery, prompts, personalization] related: [academy-use-case-explainer, academy-feature-explainer, academy-legal-ai-skills-catalog, academy-solutions-by-persona] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'academy'.
Registered as a flat plugin skill.
-->


# Prompt Library Recommender — Personalized Prompt Discovery

## When to use this

Invoke when:
- A new user asks "where do I start?" or "what should I try first?"
- A returning user asks "what prompts are useful for [practice area]?"
- A user's usage profile shows they are only using a fraction of relevant capabilities
- A user selects a role or jurisdiction during onboarding and needs a contextual starting pack
- An in-product empty state needs to surface relevant entry points

## What the Prompt Library is

The Louis Prompt Library contains **152 curated prompts** — pre-written starting points for common legal tasks. These are not templates that substitute for skill judgment; they are **well-formed entry points** that help users:
- Understand how to phrase requests to get better outputs
- Discover capabilities they did not know existed
- Build their own prompt habits faster by starting from proven examples

Prompts are organized by category, practice area, jurisdiction, and role.

## Recommendation algorithm — how it works

### Inputs

| Input | Source | Weight |
|---|---|---|
| User role | Profile / onboarding | High |
| Primary jurisdictions | Profile / onboarding | High |
| Recent activity | Session history (anonymized) | Medium |
| Practice areas worked in | Inferred from recent docs / skills used | Medium |
| Prompts already used | Usage log | Excludes already-used from recommendations |
| Explicit "not useful" signals | User dismiss / thumbs-down | Excludes category |

### Logic

1. **Filter by jurisdiction**: surface only prompts relevant to the user's stated jurisdictions. A Beirut lawyer does not need KSA-specific prompts as a priority.
2. **Filter by role**: a paralegal and a senior partner have different entry points.
3. **Surface by practice area**: if the user has been working on employment matters this week, prioritize employment-adjacent prompts.
4. **Progressive disclosure**: show 3–5 prompts, not 50. The goal is actionable discovery, not an overwhelming catalog.
5. **Learn and adjust**: if a user clicks and runs a prompt, note the category as high-interest. If a user dismisses repeatedly, reduce that category's frequency.

## Recommendation output format

Each recommendation surfaces:
1. **Prompt title** (e.g., "Review a UAE employment contract for mandatory clause gaps")
2. **One-sentence description** (what it does and when to use it)
3. **Practice area and jurisdiction tags**
4. **"Try it" button** that pre-fills the prompt into the chat input
5. **Related prompts** (1–2 links to similar prompts the user might also want)

## Prompt packs by role — defaults

### BigLaw / Large-Firm Associate
- Draft an NDA (jurisdiction-selectable)
- Review a services agreement for risk (jurisdiction-selectable)
- Summarize a contract in plain language for a client briefing
- Flag missing standard clauses in a draft SPA
- Generate a redline comparison summary

### In-House Counsel
- Review a vendor contract against standard in-house positions
- Generate a contract register entry from an uploaded agreement
- Summarize key obligations and renewal dates from a services contract
- Draft an employment offer letter (jurisdiction-selectable)
- Identify regulatory compliance obligations in a new market

### Solo Practitioner
- Draft a standard retainer / engagement letter
- Explain a legal provision in plain language (for client)
- Summarize what a court judgment means in practical terms
- Draft a simple services agreement for a client

### Law Student / Bar Candidate
- Generate a case brief in IRAC format
- Explain a legal principle with examples
- Quiz me on [subject area] at [difficulty level]
- Draft a sample exam answer for [fact pattern]
- Build a study plan for bar exam preparation

### Paralegal
- Extract key dates, parties, and obligations from a contract
- Summarize a document for file management
- Check a draft for formatting and cross-reference consistency
- Generate a document checklist for a closing

## Quality standards for prompt recommendations

- **Relevance over completeness.** Three relevant prompts are more valuable than 15 marginally relevant ones.
- **Don't re-recommend.** Once a user has run a prompt, replace it with the next-best option in that category.
- **Explain the recommendation.** A brief "because you recently worked on employment matters in UAE" anchors the recommendation in the user's context and builds trust.
- **Not prescriptive.** Recommendations are suggestions. The user sets direction; the recommender surfaces options.

## Edge cases

- **New user with no history**: default to the role-based starter pack. Prompt for role during onboarding if not set.
- **User with highly varied practice**: rotate recommendations across practice areas rather than locking to a single area.
- **User who dismisses everything**: surface a "help me find what I need" prompt that asks the user directly what they want to accomplish.

## Related skills

- [[academy-use-case-explainer]]
- [[academy-feature-explainer]]
- [[academy-legal-ai-skills-catalog]]
- [[academy-solutions-by-persona]]
