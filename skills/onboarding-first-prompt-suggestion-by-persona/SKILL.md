---
name: onboarding-first-prompt-suggestion-by-persona
description: Use when a user opens a new chat session for the first time, or returns to a blank composer, and the system must offer persona-appropriate starter prompt suggestions. Defines the specific suggested prompts for each user persona — lawyer, partner, in-house counsel, law student, SME founder, and consumer — along with the rendering rules, refresh logic, and time-of-day awareness. These are the clickable chips below the composer that guide a user's first interaction and reduce blank-page paralysis.
license: MIT
metadata: " id: onboarding.first-prompt-suggestion-by-persona category: onboarding priority: P0 intent: [onboarding, starter-prompts, persona, chips, first-use, engagement] related: [onboarding-empty-state-prompts, onboarding-persona-detection-questions, onboarding-b2c-vs-b2b-fork, onboarding-feature-discovery-tour] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'onboarding'.
Registered as a flat plugin skill.
-->


# Onboarding — First Prompt Suggestions by Persona

## When this applies

At the start of every new chat session — especially on first sign-in and after the persona detection flow — the composer surfaces **3 clickable prompt chips** tailored to the user's detected persona. These chips:
- Eliminate blank-page paralysis for new users
- Signal the product's capability range immediately
- Set the right expectation for tone and depth of response
- Refresh to avoid staleness after each session

This skill defines the specific prompt text, persona mapping, rendering rules, and refresh logic.

---

## Prompt Sets by Persona

### `associate` / `partner` (lawyers in private practice)

Prompt chips rotate across this bank; show 3 at a time:

1. "Review this MSA from a [client-side / vendor-side] perspective"
2. "Draft a mutual NDA for [purpose] under [jurisdiction] law"
3. "Compare non-compete enforceability across LB, KSA, UAE"
4. "Summarise the key risks in this shareholder agreement"
5. "What's the governing law analysis for this cross-border contract?"
6. "Draft a term sheet for a [Series A / seed / bridge] round"
7. "Flag all liability caps and exclusions in this services agreement"
8. "Explain ADGM employment law requirements for a new hire"

**Tone:** Professional, task-specific, jurisdiction-aware

### `in-house-counsel`

1. "Summarise the legal risk in this [contract / policy / vendor agreement]"
2. "Draft a client alert email about [recent regulation or topic]"
3. "What's our exposure on this [vendor / employment / data privacy] issue?"
4. "Review our standard procurement template against DIFC contract law"
5. "Help me draft a data processing agreement for a new SaaS vendor"
6. "Summarise the key obligations in this insurance policy"
7. "What internal approvals does this contract require under our policy matrix?"

**Tone:** Risk-focused, practical, policy-aware

### `law-student` (Justinian / educational)

1. "Explain the consideration doctrine using a worked example"
2. "Help me outline an IRAC for [legal issue]"
3. "Quiz me on UAE Decree-Law 33/2021 employment provisions"
4. "What's the difference between civil and common law on contract formation?"
5. "Help me understand how damages are calculated in a breach of contract case"
6. "Explain the key duties of a company director under DIFC Companies Law"
7. "Walk me through the stages of a commercial arbitration under DIAC rules"

**Tone:** Pedagogical, Socratic where appropriate, example-heavy

### `sme-founder` (business owners, entrepreneurs)

1. "Draft a basic NDA I can use with vendors and employees"
2. "Is this employment offer letter fair? Review it for me"
3. "Help me incorporate in [jurisdiction] — what's the process?"
4. "What contracts do I need before taking on my first client?"
5. "Review my freelancer agreement — am I protected?"
6. "What are the Saudization requirements if I hire in KSA?"
7. "Help me understand this SaaS agreement I'm being asked to sign"

**Tone:** Plain English, practical, no assumptions about legal knowledge

### `louis-twin` (consumer / individual)

1. "I got laid off — what are my rights in [jurisdiction]?"
2. "Help me write a will (I'm in [LB / UAE / KSA])"
3. "I want to start a freelance business — what contracts do I need?"
4. "My landlord is refusing to return my deposit — what can I do?"
5. "Explain this clause in my new employment contract"
6. "What happens if I don't pay a debt in UAE?"
7. "Help me understand the process for a divorce in Lebanon"

**Tone:** Empathetic, plain language, always include "talk to a lawyer" context for high-stakes situations

---

## Rendering Rules

### Display format

- 3 prompt chips visible at a time below the composer input
- Each chip: max 60 characters (truncate with "..." on overflow)
- Chips are clickable: one click populates the composer with the full prompt text (editable before sending)
- Do not auto-submit on click — let the user edit the prompt to add their specific document, jurisdiction, or detail

### Rotation logic

- Do not show the same 3 chips twice in a row
- After each message, refresh chips to reflect the next logical step in the conversation flow
- After first message, transition from "starter prompts" to "follow-up prompts" based on the topic detected

### Jurisdiction personalisation

Where the user's jurisdiction preference is known from the persona quiz or prior prompts:
- Replace `[jurisdiction]` placeholders with the known jurisdiction: "Review this NDA under **UAE law**"
- For multi-jurisdiction users (in-house counsel, partner at regional firm), show the primary jurisdiction first

---

## Time-of-Day Variants

| Time window | Prompt flavour adjustment |
|-------------|--------------------------|
| Monday morning | Proactive: "Start your week — what needs drafting or reviewing?" |
| Friday afternoon | Wrap-up: "Finish strong — any contracts to review before the weekend?" |
| Day before a public holiday | "Quick win before [holiday name]?" |

These time-of-day variants are optional and should only be used where they feel natural, not intrusive.

---

## After the First Message

Once the user sends their first message:
- Remove the starter prompt chips
- Surface 2–3 **follow-up prompt suggestions** based on the response (e.g., after a contract review → "See redlined version", "Identify the jurisdiction of this contract", "Compare with market standard")
- These follow-up chips are generated contextually, not from a fixed bank

---

## Failure Mode

If persona detection has not completed and no persona is known:
- Default to `louis-twin` (consumer) chips
- After the user's first message, infer persona from prompt content and update chips accordingly

---

## Related skills

- [[onboarding-empty-state-prompts]]
- [[onboarding-persona-detection-questions]]
- [[onboarding-b2c-vs-b2b-fork]]
- [[onboarding-feature-discovery-tour]]
