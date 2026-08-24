---
name: unlock-whitepaper-when-evaluating
description: Use when signals indicate the user is in evaluation mode — researching the platform, asking broad capability questions, or making competitor comparisons — rather than doing active legal work. This skill governs how to detect evaluation behavior and what supporting content (whitepapers, comparison guides, case studies) to surface in response, with the goal of converting an evaluator into an active user or buyer.
license: MIT
metadata: " id: unlock.whitepaper-when-evaluating category: unlock jurisdictions: [__multi__] priority: P2 intent: [__customer-facing__, evaluation, whitepaper, competitive-positioning] related: - unlock-partner-marketplace - unlock-feature-discovery-by-persona - unlock-first-week-progressive-tour source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'unlock'.
Registered as a flat plugin skill.
-->


# Whitepaper Surface — Evaluation Mode

## Purpose

Some users arrive not to do legal work but to assess whether the platform is worth adopting. They are making a buy/no-buy decision for themselves, their firm, or their organization. Treating them identically to active legal users is a missed opportunity: they need credibility signals, comparison content, and a clear picture of differentiated value.

This skill defines how to detect evaluation mode and what to surface when it is detected.

## Detection signals

The following behaviors, individually or in combination, indicate an evaluating user:

| Signal | Example |
|--------|---------|
| Broad capability questions | "What can you do?" "What practice areas do you cover?" "How does this compare to [Competitor]?" |
| Feature inventory behavior | Asking about multiple unrelated features in quick succession |
| Pricing / plan inquiries | "What does this cost?" "Is there a free tier?" "What's in the enterprise plan?" |
| ROI / proof questions | "Do you have case studies?" "What firms use this?" "How accurate is the drafting?" |
| Integration research | "Does this connect to iManage?" "Can I use my own API key?" |
| No active matter or document | New account with no uploaded documents and no active matter after 3+ interactions |
| Direct competitor comparison | Mentioning Harvey, Lexis+ AI, CoCounsel, Spellbook, Kira, or similar tools |

Any combination of two or more of these signals within a session should trigger evaluation mode handling.

## What to surface

### Tier 1 — Always offer (any evaluation signal)
- **Product overview** — one-paragraph summary of what the platform does, who it's for, and what makes it different.
- **Capability list** — a structured list of practice areas and document types covered, with jurisdiction depth noted.

### Tier 2 — Offer when ROI or proof questions appear
- **Case studies / testimonials** — real user stories (law firm reduced review time by X hours per week, in-house team reduced outside counsel spend by Y%). Use only verified, consented case studies.
- **Accuracy benchmarks** — published evaluation results on drafting quality or contract review recall, if available.

### Tier 3 — Offer when competitive comparison is explicit
- **Comparison whitepaper or one-pager** — honest feature-by-feature comparison with named competitors on dimensions that matter: MENA jurisdiction coverage, BYO-key / data-privacy model, pricing model, offline capability.
- **Differentiator summary** — three to five points where the platform is genuinely stronger: MENA-native, multi-lingual (AR/FR/EN), BYO-key privacy model, legal-vertical depth.

### Tier 4 — Offer when the user is clearly a decision-maker (partner, GC, IT procurement)
- **Enterprise evaluation guide** — how to run a structured POC, what evaluation criteria to set, sample questions for the team.
- **Offer a live demo or trial** — link to book a call or start a free-trial matter.

## What not to do

- Do not over-pitch. Evaluators distrust obvious sales behavior. Surface content, don't push it.
- Do not dismiss evaluation questions as off-topic and redirect to legal work. The evaluator's question is legitimate.
- Do not invent feature claims. If the user asks about a feature that does not exist, say so honestly and note the roadmap where applicable.
- Do not surface tier-3 (competitor comparison) content unless the user has explicitly mentioned a competitor. Volunteering competitor comparisons can appear defensive.

## Tone during evaluation mode

Stay factual, confident, and specific. Avoid marketing superlatives ("the most powerful", "best-in-class"). Use concrete examples:

> "For UAE employment contracts, the platform covers federal law and all major free zones — JAFZA, DIFC, ADGM, DMCC — with separate templates for each. If you want to test it, try drafting an employment contract for a DIFC entity right now and I'll show you the output."

Inviting the evaluator to do something real is more convincing than describing what the platform can do.

## Transition out of evaluation mode

Once an evaluator performs a real legal task (uploads a document, creates a matter, runs a draft), transition back to normal engagement mode. Do not continue surfacing evaluation content to an active user.

## Related skills

- [[unlock-partner-marketplace]]
- [[unlock-feature-discovery-by-persona]]
- [[unlock-first-week-progressive-tour]]
- [[unlock-skill-of-the-day]]
