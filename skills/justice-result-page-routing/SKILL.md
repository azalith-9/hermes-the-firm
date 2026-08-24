---
name: justice-result-page-routing
description: Use to decide, after a substantive AI task completes, whether to display the output inline in chat or route the user to a dedicated result page (doc workspace, memo viewer, compare viewer, citation report, etc.). Applies a deterministic threshold based on output type, length, and follow-up tool needs. Covers all jurisdictions; no practice area restriction — this is a UI-routing and output-orchestration skill.
license: MIT
metadata: " id: justice.result-page-routing category: justice jurisdictions: [__multi__] priority: P2 intent: [routing, output-routing, result-page, ui-orchestration] related: [justice-message-actions, justice-slash-commands, justice-product-demo-context-memory] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'justice'.
Registered as a flat plugin skill.
-->


# Justice — Result Page Routing

## Purpose

Not every output belongs in the chat stream. Long drafts, structured memos, multi-document comparisons, and outputs that need follow-up tools should route to a purpose-built result page. This skill defines the decision rules for when to stay in chat vs when to route out.

## Inputs / signals

The routing decision uses four signals:

1. **Output type** — what kind of result was produced
2. **Output length** — word / line count
3. **Follow-up tooling** — does the output need further manipulation (editing, TOC, citation linking, comparison)?
4. **User intent** — did the user explicitly say "show me the result page" or "open in workspace"?

## Routing decision table

| Output type | Length threshold | Route to |
|---|---|---|
| Document draft (contract, brief, memo, letter) | > 200 words | Doc workspace (draft loaded) |
| Document draft | ≤ 200 words | Inline in chat (with "Open in workspace" option) |
| Legal research memo | Any | Memo viewer + bibliography panel |
| Multi-document comparison | Any | Compare viewer (side-by-side diff) |
| Translation | Any | Side-by-side bilingual viewer |
| Cap table reconciliation | Any | Cap table viewer |
| Citation check / cite-check | Any | Citation report viewer |
| Summary or brief answer | Any | Inline in chat |
| Flashcard set | > 10 cards | Flashcard viewer / export |
| Flashcard set | ≤ 10 cards | Inline in chat |
| Contract redline / tracked-changes | Any | Doc workspace (track-changes mode) |
| Data extraction (from document) | Any | Structured table viewer |

## Inline chat threshold

Keep output in chat when **all** of the following are true:

- Output is ≤ 500 lines
- Output does not require follow-up tools (no edit, compare, TOC, citation cross-reference needed)
- User's stated intent is conversational ("what does this clause mean?") not work-product ("draft me a lease")
- Output does not benefit from anchors, headings, or cross-references that would be navigable in a dedicated view

Route to a result page when **any** of the following are true:

- Output > 500 lines
- Output is a structured work product (contract, memo, redline)
- Output requires follow-up tools available only in a result page (doc editor, citation linker, compare panel)
- User explicitly requests a result page ("open in workspace", "show me the full document")

## Result page types and their URLs

| Result page | URL pattern | What it contains |
|---|---|---|
| Doc workspace | `/workspace/:doc_id` | Full editor, track-changes, export, matter filing |
| Memo viewer | `/research/:memo_id` | Research memo with TOC + bibliography panel |
| Compare viewer | `/compare/:job_id` | Side-by-side doc comparison with delta summary |
| Bilingual viewer | `/translate/:job_id` | Side-by-side source + translation, term glossary |
| Cap table viewer | `/captable/:job_id` | Reconciled cap table with shareholder summary |
| Citation report | `/citecheck/:job_id` | Flagged citations with status (found / missing / incorrect) |
| Flashcard viewer | `/flashcards/:set_id` | Spaced-repetition interface + export to Anki / CSV |

## UX rules

- Always show an **"Open in [viewer]"** button in chat even when displaying a short output inline — give the user the option
- For very long outputs routed to a result page, show a **brief summary in chat** (3–5 lines) so the user gets immediate signal: "I've drafted a 12-clause NDA — opening it in the doc workspace now. Here's a quick summary: …"
- If routing to a result page, do **not** also dump the full output into chat — it creates duplication and confusion
- On mobile, result pages render in a slide-over sheet rather than full navigation; chat remains accessible

## Related skills

- [[justice-message-actions]]
- [[justice-slash-commands]]
- [[justice-product-demo-context-memory]]
