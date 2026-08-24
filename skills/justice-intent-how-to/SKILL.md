---
name: justice-intent-how-to
description: Use when the public-facing assistant detects a procedural or task-oriented question from a user who wants to know how to accomplish something within Louis or with the legal system — "How do I draft a contract?", "How do I upload a document?", "How do I start a case?". Routes to step-by-step in-chat guidance, help documentation, or onboarding flows. Covers all jurisdictions; central to the Justice accessibility mission of making legal processes legible to non-experts.
license: MIT
metadata: " id: justice.intent.how-to category: justice jurisdictions: [__multi__] priority: P1 intent: [__justice__, how-to, tutorial, step-by-step, onboarding, procedural] related: [justice-intent-feature-question, justice-intent-support, justice-intent-chitchat, justice-intent-legal-research] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'justice'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Justice Intent — How-To

## When to use this

Trigger when the message begins or implies "how do I…", "can you show me how…", "walk me through…", "what are the steps to…", or "I don't know how to…"

Two distinct sub-intents to handle differently:

| Sub-intent | Signal | Handling |
|---|---|---|
| **Product how-to** | "How do I upload a document?", "How do I run a review?" | Step-by-step product guidance |
| **Legal how-to** | "How do I file a labor complaint?", "How do I register a company?" | Jurisdiction-specific procedural guidance + escalation flag |

## Product how-to: response pattern

For questions about using Louis itself:

1. Identify the product feature or workflow being asked about
2. Give numbered steps (3–7 steps, each actionable)
3. Include a keyboard shortcut or slash command where relevant (see [[justice-slash-commands]])
4. Link to the help doc or feature page if one exists (`/help/:slug`)
5. Offer to run the task together ("Want me to start the review right now?")

### Common product how-to flows

**Draft a contract**
1. Click "New document" (or type `/draft [contract type]`)
2. Select your jurisdiction and language
3. Answer the drafting prompts or paste your brief
4. Review the draft; use "Edit" or "Track changes" to refine
5. Send to matter or export

**Review a contract**
1. Paste the contract text or upload a PDF/DOCX
2. Type `/review` or click "Review document"
3. Select review type (general, clause-by-clause, risk-only)
4. Review the flagged issues in the result panel
5. Click any flag to get an explanation + suggested redline

**Set up a matter**
1. Go to Matters → New matter
2. Add matter name, client, practice area, jurisdiction
3. Invite team members (if on a team plan)
4. Upload documents into the matter file
5. All subsequent drafts/reviews in that context auto-attach to the matter

## Legal how-to: response pattern

For procedural legal questions (how to file, register, complain, appeal):

1. Identify the jurisdiction from context or ask ("Are you in Lebanon, UAE, KSA, or elsewhere?")
2. Give the correct procedural steps for that jurisdiction
3. Flag if the user should engage a licensed lawyer at any specific step
4. Offer to draft the relevant document (complaint letter, application form, etc.)
5. Cite the relevant body (e.g., "Ministry of Labor", "Commercial Court", "DIFC Courts") without fabricating article numbers

### Jurisdiction signals to watch for

- Lebanon: references to Beirut, lira/dollar dual currency, syndicat, kafala, confessional personal status
- UAE: references to Emirates, visa, DIFC, free zones, Ministry of HR
- KSA: references to kingdom, Vision 2030, SAGIA/MISA, Iqama, labor ministry
- France: references to URSSAF, prud'hommes, préfecture, infogreffe

## Accessibility note (Justice mission)

Many how-to questions come from people who cannot afford a lawyer or do not know the system. The response should:
- Never assume the user has legal knowledge
- Explain acronyms on first use
- Flag when official forms or fees are required
- Offer to draft any document needed (complaint letter, demand letter, contract)
- Flag when the stakes are high enough that a licensed lawyer is essential

## Do not

- Do not assume the user has access to paid legal resources
- Do not give a how-to answer without first identifying the jurisdiction for legal how-to questions
- Do not fabricate procedural timelines or statutory deadlines — flag them as approximate and direct to the official body

## Related skills

- [[justice-intent-feature-question]]
- [[justice-intent-support]]
- [[justice-intent-chitchat]]
- [[justice-intent-legal-research]]
- [[justice-slash-commands]]
