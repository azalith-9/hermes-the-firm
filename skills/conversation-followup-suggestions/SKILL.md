---
name: conversation-followup-suggestions
description: Use after every substantive legal-AI response to append exactly three concrete, action-first follow-up prompts that the user can click or select as their next step. Governs the format (3 chips, ≤8 words each), differentiation rules, and when to skip entirely. Applies to all personas and practice areas. Rendered as chip buttons in the frontend.
license: MIT
metadata: " id: conversation.followup-suggestions category: conversation priority: P1 intent: [__core__] related: [conversation-clarifying-questions, conversation-disclaimer, conversation-empathy-b2c] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'conversation'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Follow-up Suggestions

## When this applies

After every **substantive** legal-AI response — a response that answered a question, produced a document, completed a review, or provided analysis — append exactly three follow-up prompt suggestions. These are rendered by the frontend as clickable chip buttons below the message.

A "substantive" response is:
- A legal-content answer (not just a clarifying question).
- A completed document draft or document review.
- A research result or jurisdiction analysis.
- A strategy explanation or next-step guide.

## The rule: exactly 3

- **Less than 3 is anemic.** One or two suggestions implies the user's options are limited.
- **More than 3 is overwhelming.** Four or five suggestions creates decision paralysis.
- **Exactly 3.** No exceptions.

## Format rules

### Action-first, ≤8 words

Each suggestion must:
- **Start with an imperative verb** ("Draft," "Compare," "Explain," "Summarize," "File," "Find," "Show," "Calculate").
- **Be ≤8 words** — this is a chip, not a sentence.
- **Be immediately understandable** — no ambiguity about what clicking it will do.

Good:
- "Draft a counter-redline accepting clauses 1–3"
- "Compare these terms to our standard NDA"
- "Find a labor lawyer in Dubai"

Bad:
- "I could draft a counter-redline for you" (non-imperative; too long)
- "More information" (vague)
- "Legal options" (not action-first; too vague)

### Differentiated

The three suggestions must be meaningfully different from each other. Do not offer three variants of the same action:

Bad (all three are essentially "draft something"):
1. "Draft a response letter"
2. "Write a counter-proposal"
3. "Prepare a draft reply"

Good (three genuinely different next steps):
1. "Draft a response letter to the landlord"
2. "Explain the eviction timeline in Dubai"
3. "Find a tenant rights lawyer near me"

A good set covers different dimensions:
- **Create something** (draft, generate, prepare)
- **Understand something** (explain, summarize, compare, calculate)
- **Take an action** (find, file, schedule, connect)

### Matter-relevant

Suggestions must be specific to this conversation, not generic. After reviewing an employment contract:

Generic (bad):
1. "Draft a document"
2. "Explain the law"
3. "Get legal help"

Matter-specific (good):
1. "Redline clause 14 (IP assignment) — flag for negotiation"
2. "Compare non-compete scope to UAE Labor Law standards"
3. "Draft a clarification email to HR about clause 8"

## Examples by practice area

### After an NDA review

1. "Suggest a redline accepting clauses 1–3, rejecting 4"
2. "Draft a counter-proposal email to the other side"
3. "Compare these terms against our standard NDA template"

### After a jurisdiction analysis on arbitration

1. "Draft a DIAC arbitration clause for this contract"
2. "Compare DIFC-LCIA vs ICC for this dispute value"
3. "Explain the emergency arbitrator procedure under DIAC rules"

### After a consumer-facing employment termination answer

1. "Draft a formal grievance letter to my employer"
2. "Calculate my end-of-service gratuity under UAE Labor Law"
3. "Find a labor lawyer in [user's city]"

### After a data-privacy gap analysis

1. "Draft a GDPR-compliant privacy notice"
2. "Prioritize the remediation roadmap by risk level"
3. "Check if we need to appoint a DPO in the EU"

## When to skip

Do not append follow-up suggestions when:

| Condition | Why |
|---|---|
| Response was a clarifying question only | No substantive answer yet; suggestions would be premature |
| Response was admin/billing/settings | No legal content; irrelevant |
| User is in mid-OCR / document-processing flow | Mid-process state; suggestions would interrupt the flow |
| Response was a disclaimer-only refusal | Suggesting next steps after a refusal is confusing |
| The user has already selected a suggestion from the previous turn | You're executing that suggestion; don't pile on new ones until the result is delivered |

## Technical note — rendering

The frontend renders these as chip buttons below the assistant message. The text for each chip is:
- The suggestion text exactly as written (no markdown formatting in the chip text).
- If the user clicks a chip, the chip text is submitted as a new user message.

This means the text must work as a **natural-language prompt** when submitted — not as a heading or label. "Draft a counter-redline accepting clauses 1–3" works as a message; "Counter-redline" does not.

## Multilingual

For Arabic-language conversations, the suggestions must also be in Arabic:
- Imperative verb first (Arabic verb-first structure works well here).
- ≤8 Arabic words.
- Right-to-left rendering handled by the frontend.

For French-language conversations: same rules apply in French.

## Related skills

- [[conversation-clarifying-questions]]
- [[conversation-disclaimer]]
- [[conversation-empathy-b2c]]
