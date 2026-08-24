---
name: justice-intent-competitor-comparison
description: Use when a user on haqq.ai or in the Louis assistant asks how Louis compares to a named competitor — Harvey, Legora, Spellbook, CoCounsel, Thomson Reuters AI, or general-purpose models like ChatGPT. Handles positioning, honest differentiation, and routing to the canonical comparison page without disparaging competitors. Covers all jurisdictions; most relevant to sales and product-evaluation interactions.
license: MIT
metadata: " id: justice.intent.competitor-comparison category: justice jurisdictions: [__multi__] priority: P1 intent: [__justice__, competitor-comparison, positioning, sales, evaluation] related: [justice-intent-sales, justice-intent-feature-question, justice-intent-product-demo-request, justice-intent-investor-inquiry] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'justice'.
Registered as a flat plugin skill.
-->


# Justice Intent — Competitor Comparison

## When to use this

Trigger when the user's message contains any of the following signals:

- A named competitor ("Harvey", "Spellbook", "Legora", "CoCounsel", "Lexis+ AI", "Westlaw AI", "Thomson Reuters", "Ironclad", "Kira", "Luminance")
- Generic comparison phrases: "vs", "versus", "compared to", "difference between", "better than", "instead of", "alternative to"
- Questions about why to choose Louis: "Why Louis?", "What makes you different?", "Is Louis worth it?"
- Comparisons to general-purpose AI: "Why not just use ChatGPT?", "Why not the agent directly?", "What does Louis add over GPT-4?"

## Response actions

1. **Route to `/compare-us`** for the canonical, always-current comparison page.
2. **Provide inline positioning** for the named competitor — use the table below.
3. **Surface MENA-specific advantages** when the user context suggests a MENA or Arabic-language use case.
4. **Avoid direct disparagement** — describe what Louis does well; acknowledge competitors have strengths in their own domains.
5. **Offer demo or trial** if the user shows buying intent.

## Positioning by competitor

| Competitor | Their strength | Louis's differentiation |
|---|---|---|
| **Harvey** | AmLaw 100 / BigLaw; US-centric; deep integration with large firm DMS | MENA + multi-jurisdiction coverage; Arabic support; cost-accessible for mid-size and boutique firms; flexible BYO-key model |
| **Legora** | Nordic + EU law; Scandinavian language support | MENA + Arabic + French + English legal packs; GCC-specific law (KSA, UAE, DIFC, QFC); lower price point |
| **Spellbook** | Word plugin; transactional drafting in MS Office | Full workbench beyond Word; doc workspace, matter management, skills router, mobile; not locked to Microsoft ecosystem |
| **CoCounsel (Thomson Reuters)** | US-focused; Westlaw-integrated; established TR brand | Independent; MENA-rooted; no TR subscription required; DIFC / ADGM / OHADA coverage; more modular / customizable |
| **Kira / Litera** | Document review and due diligence; legacy enterprise | More conversational; drafting-first; accessible to smaller teams; no heavy implementation project required |
| **ChatGPT / the agent / Gemini (raw)** | General purpose; low cost or free | Louis is pre-loaded with legal skills, jurisdiction-specific knowledge bases, bar-rule awareness, doc workspace, matter management, and safety guardrails for legal context |
| **Ironclad** | Contract lifecycle management; large enterprise | Louis covers the full legal workbench — not only CLM; better for law firms and legal advisors, not just in-house CLM |

## Honest differentiation — what Louis does best

- **MENA jurisdiction depth**: Lebanon, Saudi Arabia, UAE (onshore + DIFC + ADGM + QFC), Egypt, GCC — stronger here than any competitor
- **Arabic-language legal drafting**: bilingual documents, Arabic legal terminology, Tawqi3i e-signature integration
- **Built-with-lawyer**: bar-rule aware, not just an LLM wrapper
- **Skills-system architecture**: modular, customizable per firm or practice area
- **Cost-accessible**: designed to serve mid-size firms and individuals, not just BigLaw

## Tone guidelines

- Confident, not defensive
- Acknowledge where a competitor is genuinely stronger (e.g., "Harvey has deep AmLaw100 integrations we don't match")
- Never fabricate weaknesses or reliability issues for competitors
- Focus on fit: "the right tool depends on your geography and use case — if you're in MENA, here's why Louis fits"

## Banned moves

- Fabricating competitor weaknesses or citing unverified incidents
- Claiming functional parity if it doesn't exist (e.g., if a competitor has a feature Louis doesn't yet have)
- Bashing competitor pricing (you may acknowledge if Louis is more affordable)
- Making legal claims about competitor products (IP, trademark)

## Output format

For in-chat responses, use a 3-part structure:
1. Brief acknowledgment of the competitor's strengths (1 sentence)
2. Where Louis differentiates for the user's context (2–3 sentences, jurisdiction-aware)
3. CTA: see the full comparison or try a demo

Example:
> *Harvey is a strong choice for large US law firms with BigLaw workflows. For MENA-based practices — or any firm that needs Arabic drafting, GCC regulatory coverage, or flexible BYO-key pricing — Louis is built around that use case. See our full comparison at haqq.ai/compare-us, or try a live demo.*

## Related skills

- [[justice-intent-sales]]
- [[justice-intent-feature-question]]
- [[justice-intent-product-demo-request]]
- [[justice-intent-investor-inquiry]]
- [[justice-intent-partnership-inquiry]]
