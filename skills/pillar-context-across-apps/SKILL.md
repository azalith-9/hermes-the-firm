---
name: pillar-context-across-apps
description: Internal architectural principle establishing that a user's matter context — parties, jurisdiction, documents, prior analysis — follows them across all product surfaces (chat, document editor, drafting tool, calculators, matter view). Use when designing any new surface, integration, or skill to understand how context is persisted and accessed.
license: MIT
metadata: " id: pillar.context-across-apps category: pillar jurisdictions: [__multi__] priority: P3 intent: [__internal__] related: [pillar-architectural-bet-no-fine-tuning, pillar-document-comprehension-structural, pillar-legal-skills-authoring, pillar-live-data-mcp, eng-context-store] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'pillar'.
Registered as a flat plugin skill.
-->


# Architectural Pillar: Context Across Apps

## Scope

This pillar establishes that **matter context is a first-class, persistent object** in the Louis architecture. A user's context — who the parties are, which jurisdiction applies, what documents have been analyzed, what questions have been asked and answered — must be available uniformly across every product surface.

The user has one identity and many touchpoints. The legal AI experience must feel like one continuous conversation, not a series of isolated tool invocations.

---

## The principle

> User's matter context follows them across surfaces (chat, doc, drafting, calculator, matter view). One identity, many touchpoints.

---

## Why this matters

### Legal work is inherently multi-surface
A lawyer reviewing a contract does not think of it as "a chat session" and "a document editor" and "a research query" — they think of it as a matter. When they ask a question in chat, they expect the answer to be informed by the document they just uploaded. When they switch to a drafting tool, they expect it to know the parties' names and jurisdiction.

Without cross-surface context, every surface starts from scratch. The AI asks for information the user already provided. Answers are inconsistent because different surfaces have different context. The user loses trust.

### Consistency is a legal quality requirement
In legal work, inconsistency is not just annoying — it is dangerous. A drafting tool that generates a different defined term than the one used in the reviewed document creates a contractual inconsistency. A research answer that ignores the jurisdiction the user told the chat interface is wrong.

### Context is how skills get jurisdiction and party data
Many skills require jurisdiction, party identities, governing law, and document references as inputs. The cross-surface context store is the mechanism by which these inputs are automatically available to skills without the user re-entering them.

---

## Context object structure

The matter context object holds, at minimum:

```
matter:
  id:            [unique matter identifier]
  label:         [human-readable matter name]
  jurisdiction:  [primary jurisdiction code: LB, UAE, DIFC, KSA, EG, FR, UK, US, …]
  governing_law: [if different from jurisdiction of parties]
  parties:
    - role: [Buyer / Seller / Employer / Employee / Client / Counterparty / …]
      name: [party name]
      type: [individual / company / government]
      jurisdiction: [party's home jurisdiction]
  documents:
    - id:    [document identifier]
      label: [document name]
      type:  [contract / court filing / regulation / correspondence / …]
      parsed: [reference to parsed AST — see [[pillar-document-comprehension-structural]]]
  prior_analysis:
    - question: [user's question]
      answer:   [summary of answer]
      skill:    [skill that answered it]
      date:     [timestamp]
  preferences:
    language:   [en / ar / fr]
    persona:    [active persona id]
```

---

## How context flows across surfaces

| Surface | Reads from context | Writes to context |
|---------|-------------------|------------------|
| Chat interface | Jurisdiction, parties, prior Q&A | New Q&A pairs |
| Document upload | — | Document object + parsed AST |
| Drafting tool | Jurisdiction, parties, document defined terms | New draft document |
| Legal calculator | Jurisdiction, party types | Calculation result + parameters |
| Matter dashboard | All | User-initiated edits to any field |
| Research | Jurisdiction | Research results + sources |

---

## Implications for skill design

Skills that receive context from the context store must:
1. **Declare their context dependencies** in their Required Inputs section — this lets the router pre-populate them automatically
2. **Not re-ask for context that's already known** — if jurisdiction is in the context store, the skill must use it, not prompt the user again
3. **Update the context store when they produce outputs** that should be remembered (e.g., a drafting skill should write the output document back to the matter's document list)

Skills that modify shared context (e.g., changing the governing-law assumption) must signal this change so other surfaces refresh.

---

## Privacy and data handling

Matter context contains potentially sensitive client data. The context store must:
- Be scoped to the authenticated user (or firm workspace)
- Not leak context between unrelated matters
- Apply data retention policies (configurable per workspace, with jurisdiction-specific defaults — e.g., DIFC Data Protection Law, UAE Federal Decree-Law 45/2021)
- Be exportable and deletable to support subject-access and erasure requests

---

## Failure modes

| Failure | Consequence | Mitigation |
|---------|-------------|-----------|
| Context store unavailable | Surface starts from scratch; user must re-enter context | Graceful degradation: prompt user for context rather than failing |
| Context outdated | Analysis uses stale parties / jurisdiction | Timestamp context entries; surface staleness warnings after configurable period |
| Context overload | Too much prior context crowds the prompt | Summarize and compress prior analysis; load only relevant entries |
| Cross-matter contamination | Context from one matter bleeds into another | Strict matter-id scoping; audit log |

---

## Caveats and currency

The context store implementation is an engineering concern (see [[eng-context-store]] for the technical spec). This pillar defines the *requirement* — that context must flow — not the implementation mechanism. The implementation may evolve as the product scales.

---

## Related skills

- [[pillar-architectural-bet-no-fine-tuning]] — the broader architectural philosophy
- [[pillar-document-comprehension-structural]] — how documents become structured context
- [[pillar-live-data-mcp]] — live data that supplements stored context
- [[pillar-legal-skills-authoring]] — how skills declare and consume context
- [[eng-context-store]] — engineering implementation of the context object
