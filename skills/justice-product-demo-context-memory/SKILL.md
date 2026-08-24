---
name: justice-product-demo-context-memory
description: Use during a product demo session to retain and reuse context the user shared earlier in the session — industry, firm type, key facts, stated preferences — so that subsequent demo examples feel tailored rather than generic. Session memory is ephemeral (ends at session close unless the user signs up). Works alongside the demo recap and deep-link skills to create a coherent, personalized demo experience.
license: MIT
metadata: " id: justice.product-demo.context-memory category: justice jurisdictions: [__multi__] priority: P2 intent: [demo, memory, personalization, session-context] related: [justice-product-demo-recap, justice-intent-product-demo-request, justice-result-page-routing] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'justice'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Justice — Product Demo: Context Memory

## Purpose

A demo that reuses facts the user shared earlier is dramatically more persuasive than one using generic examples. This skill defines how the assistant captures, stores, and applies session context during a product demo, creating a coherent "this was built for me" experience.

## Inputs / signals to capture

Listen throughout the demo conversation for the following and store them in the session context object:

| Signal | Example | Store as |
|---|---|---|
| **Industry / sector** | "we do MSAs for marketing agencies" | `industry: marketing`, `doc_type: MSA` |
| **Firm type** | "I'm a solo practitioner", "we're a 20-person firm" | `firm_size: solo` or `firm_size: 20` |
| **Jurisdiction** | "most of our clients are in Lebanon" | `jurisdiction: LB` |
| **Practice area** | "we focus on corporate M&A" | `practice_area: corporate_ma` |
| **Pain point** | "contract review takes us forever" | `pain_point: contract_review_time` |
| **Current tools** | "we use Word and email" | `current_stack: word, email` |
| **Language preference** | responds in Arabic | `language: ar` |
| **Specific documents** | "we do employment contracts a lot" | `doc_focus: employment_contracts` |
| **Deal size or volume** | "about 30 contracts a month" | `volume: 30_monthly` |

## Memory rules

### Capture
- Capture context passively — do not run a questionnaire at the start. Let context emerge naturally.
- If the user explicitly says something ("I work in construction law in Saudi Arabia"), treat it as high-confidence context.
- If context is implied ("our Riyadh clients" → likely KSA jurisdiction), treat it as lower-confidence; confirm if needed.

### Apply
- In all subsequent demo examples, substitute the captured context for generic placeholders:
  - Generic: "Let me show you an NDA draft"
  - Personalized: "Let me show you an employment contract draft — typical for a Saudi-based firm like yours"
- When invoking a skill for demonstration, pre-fill jurisdiction, document type, and language from context
- When suggesting next steps, reference the user's stated pain points ("Given that contract review is your main bottleneck, here's what the review workflow looks like")

### Do not re-ask
- If the user already stated their jurisdiction, do not ask again later in the session
- If the user said they are a solo practitioner, do not show team-workflow steps as the primary demo

### Memory scope
- **Session only**: context memory lives for the duration of the demo conversation
- **Cleared at session close** unless the user creates an account — do not persist to local storage or backend without user consent
- If the user signs up, prompt: "Shall I save your preferences to your new account?" (opt-in)

## Integration with demo flow

The context memory feeds into:

1. **Example generation**: all example contracts, clauses, and research topics are drawn from the user's stated industry and jurisdiction
2. **Skill suggestions** (Step 4 of the demo flow): skills shown are filtered to the user's practice area
3. **ROI framing**: time-saved estimates reference the user's stated volume ("at 30 contracts/month, this saves you ~40 hours")
4. **Demo recap**: [[justice-product-demo-recap]] uses the session context to generate a tailored wrap-up

## Failure modes

| Situation | Handling |
|---|---|
| Context is ambiguous or contradictory | Use the more recent / more specific signal; proceed with a soft assumption and confirm if high-stakes |
| No context captured by Step 3 of demo | Ask one targeted question: "What type of work do you do most — drafting, reviewing, or research?" |
| User changes context mid-demo | Update immediately; acknowledge the change naturally ("Got it — let me switch to a construction contract example instead") |

## Related skills

- [[justice-product-demo-recap]]
- [[justice-intent-product-demo-request]]
- [[justice-result-page-routing]]
