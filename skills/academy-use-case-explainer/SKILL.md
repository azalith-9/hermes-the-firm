---
name: academy-use-case-explainer
description: Use when a user describes what they want to accomplish and needs to be shown which Louis features and skills will help them do it. This skill starts from user intent (goal-first) and maps it to features — the reverse of the feature explainer, which starts from a feature name. Triggers on "I need to do X, how does Louis help?", "can Louis do Y?", or any use-case description that requires routing the user to the right entry point.
license: MIT
metadata: " id: academy.use-case-explainer category: academy jurisdictions: [__multi__] priority: P3 intent: [__customer-facing__, use-case, onboarding, discovery] related: [academy-feature-explainer, academy-ai-feature-explainer, academy-prompt-library-recommender, academy-solutions-by-persona, academy-legal-ai-skills-catalog] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'academy'.
Registered as a flat plugin skill.
-->


# Use Case Explainer — Goal-First Feature Discovery

## When to use this

Invoke when:
- A user says "I need to draft an NDA" → map to Drafting Board + Document Library
- A user says "I got a contract from a vendor and want to know if it's risky" → map to Risk Scanner
- A user says "I'm preparing for a deposition next week" → map to Casesim client Q&A prep + cross-examination rehearsal
- A user says "I need to understand what UAE labour law says about non-competes" → map to kb/research skills
- Any user statement that starts with "I need to…", "I want to…", "How do I…", or "Can Louis…"

**Key distinction from [[academy-feature-explainer]]:** that skill starts from a feature name and explains it. This skill starts from what the user wants to do and identifies the right feature path. Both skills end up describing features — but the entry point and the tone differ.

## Methodology — goal to feature mapping

### Step 1: Identify the user's goal
Parse the user's statement into:
- **Task type** (draft / review / research / simulate / learn / explain / find)
- **Document type** (NDA, employment contract, services agreement, court filing, etc.)
- **Jurisdiction** (explicit or inferred from context)
- **Urgency / complexity** (quick lookup vs. deep work)

### Step 2: Map to the right entry point

| Task type | Primary entry point | Secondary |
|---|---|---|
| Draft a document | Drafting Board + Document Library | Clause Library for specific provisions |
| Review / risk-check a document | Risk Scanner | Clause Library for replacement clauses |
| Research a legal question | Research / kb skills | Statute Explainer for specific provisions |
| Simulate litigation | Casesim skills (judge, opposing counsel, Q&A) | Justinian for foundational skills |
| Learn legal AI | Justinian / Learn Legal with AI curriculum | Prompt Library for entry prompts |
| Find a clause | Clause Library | Drafting Board for insertion |
| Understand a document | Contract Summarizer / Plain-language Explainer | Risk Scanner for risk context |
| Translate a legal document | Legal Translator | Contract Summarizer for context |

### Step 3: Walk the user through the entry point
Provide a concrete 2–3 step walkthrough:
1. What to click / type first
2. What input to provide
3. What output to expect

## Common use cases — mapped

### "I need to draft an NDA for a new partnership"
→ **Start with:** Drafting Board → select NDA template from Document Library → choose jurisdiction and position (mutual or unilateral) → fill party names and scope → review suggested clauses from Clause Library
→ **Output:** Draft NDA ready for review and redline
→ **Jurisdiction note:** if UAE, the document will auto-include an Arabic-language execution option; if DIFC, English-only is fine

### "I received a 40-page vendor contract and need to know if it's safe to sign"
→ **Start with:** Risk Scanner → upload the document → review the risk report (Critical / High / Medium / Low tiers)
→ **What to do with the output:** for each Critical or High item, check the recommended replacement clause in the Clause Library; decide whether to push back or accept
→ **Time to output:** typically under 60 seconds for a 40-page document

### "I need to prepare my client for a deposition next week"
→ **Start with:** [[casesim-client-q-and-a-prep]] → input the case facts and the deponent's role → Louis generates a question bank and scores difficulty → run roleplay rehearsal sessions
→ **Also consider:** [[casesim-cross-examination-rehearsal]] if you are preparing the opposing cross as well

### "What does UAE law say about annual leave?"
→ **Start with:** UAE Labour Law knowledge base → search "annual leave" → output: statutory entitlement, accrual rules, carryover limits, payment on termination
→ **Jurisdiction note:** confirm whether the employee is UAE-mainland or DIFC/ADGM (different regimes apply)

### "I need to negotiate a better limitation-of-liability clause"
→ **Start with:** Clause Library → search "limitation of liability" → filter by jurisdiction and position (seller-favorable / buyer-favorable / neutral) → review alternates and drafting notes
→ **Context:** if you have the current draft, also run it through the Risk Scanner first so you know what you are replacing and why

### "I'm a law student studying for the Lebanese bar — how do I use Louis?"
→ **Start with:** [[academy-justinian-tutor]] → select Lebanese law → pick a subject area → generate practice questions and case briefs
→ **Also:** [[academy-learn-legal-with-ai-curriculum]] for a structured 12-week program
→ **Free access:** verified students get free Justinian access through the [[academy-students-program]]

### "I want to compare how employment non-competes work in UAE vs Lebanon"
→ **Start with:** Research / comparative analysis skill → input: "non-compete clauses, employment context, UAE vs Lebanon"
→ **Output:** comparative table covering enforceability, scope limitations, remedies, and key differences in legal basis (UAE Labour Law vs Lebanese Labour Code)

## When Louis cannot help — escalation paths

Some user goals fall outside what Louis can deliver alone:
- **Specific legal advice on a live matter** → direct user to consult a qualified lawyer in the relevant jurisdiction
- **Court filings and procedural steps** → Louis can draft; a licensed lawyer must file
- **Notarization** → requires a physical or recognized e-notarization service (Tawqi3i for Lebanon)
- **Real-time regulatory monitoring** → Louis provides knowledge packs; for live monitoring, integrate a regulatory intelligence feed

## Related skills

- [[academy-feature-explainer]]
- [[academy-ai-feature-explainer]]
- [[academy-prompt-library-recommender]]
- [[academy-solutions-by-persona]]
- [[academy-legal-ai-skills-catalog]]
