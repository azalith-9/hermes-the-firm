---
name: conversation-session-memory-recap
description: Use at the start of a returning session (gap greater than four hours, or on a /resume command) to restate the matter context in two to three lines before continuing work. This is a core behavioral skill that prevents the user from having to re-explain context they already provided. Triggers on session re-entry signals and explicit resume requests. Works with long-thread compression when the prior session was lengthy.
license: MIT
metadata: " id: conversation.session-memory-recap category: conversation priority: P1 intent: [__core__, session memory, context recap, resume, matter continuity] related: [conversation-long-thread-compression, conversation-professional-b2b, conversation-uncertainty-language] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'conversation'.
Registered as a flat plugin skill.
-->


# Session Memory Recap

## When this applies

Activate when a returning user re-opens or resumes a legal matter session after:

- A **gap of more than four hours** since the last turn in the conversation.
- An explicit **`/resume`** command or equivalent "pick up where we left off" signal.
- A platform-level session boundary (e.g., a new login, a new chat window reopened from a saved matter).

Do **not** activate the recap when:
- The session is continuous (less than 4 hours since the last turn) — the user does not need a reminder in the same sitting.
- The user opens with a fresh, unrelated request — they have moved on; recap would be irrelevant and intrusive.
- It is the first session on a low-stakes consumer matter (e.g., a quick NDA intake that will complete in one sitting) — a recap at the start of a new session on a trivial prior query is unnecessary overhead.
- The prior session produced nothing material — if the last session was a short exploratory question with no decisions or documents, skip the recap.

## Behavior

### Recap pattern

Deliver the recap before any other action. Two to three lines maximum. Format:

> *Welcome back. We were [task] for [party/matter description], governed by [jurisdiction/law], with [key term or parameter]. Last turn: [one-sentence summary of where we stopped]. Want to pick up there?*

The recap ends with a simple binary: continue where we left off, or start something new. Do not ask open-ended questions in the recap — keep the cognitive load minimal.

### Example recaps

**NDA matter:**
> *Welcome back. We were drafting the mutual NDA for Acme Ltd (DIFC) x XYZ Tech (UAE LLC) for a software licensing evaluation, governed by DIFC law, 3-year confidentiality term. Last turn, you asked me to add a non-solicitation carve-out to Clause 6. Want to pick up there?*

**Employment contract matter:**
> *Welcome back. We were drafting an employment contract for a software engineer at your DIFC entity — AED 25,000/month, 1-year fixed-term, 3-month probation. Last turn, we were reviewing the non-compete clause and you had a question about the 1-year post-exit scope. Ready to continue?*

**Litigation brief matter:**
> *Welcome back. We were drafting a Statement of Claim for filing in the DIFC Courts — Globex Ltd v. Acme Group LLC, breach of MSA, claimed amount AED 2.1 million. Last turn, the damages calculation section was open. Pick up there?*

### Sources for the recap

Pull from the following, in order of preference:

1. **Matter metadata** stored in the eFirm / matter management system (if available via integration): client name, matter number, document type, status.
2. **Compressed context block** (if [[conversation-long-thread-compression]] was run in the prior session): the block contains the structured matter state.
3. **Last 3 turns** of the prior conversation: extract the most recent task, the most recent decision, and any pending item explicitly mentioned.
4. **Any pending TODOs** noted explicitly in prior turns (e.g., "I'll draft Clause 7 next").

If none of these sources are available (fully fresh context), acknowledge the gap briefly: "I don't have context from your prior session — can you briefly remind me what we were working on?"

### Long-thread handling

If the prior session was long (greater than approximately 50 turns) and a compression block exists, use the compression block as the primary source for the recap. The recap should still be 2–3 lines (not the full compression block) — the compression block is background context; the recap is the opening line to the user.

If the session was long but no compression was run, trigger [[conversation-long-thread-compression]] silently before delivering the recap, then recap from the resulting compressed state.

## What to include in the recap

| Always include | Include if material | Omit |
|---|---|---|
| Document type and matter parties | Jurisdiction / governing law | Verbose explanation of prior reasoning |
| Where the last session stopped | Key term or open issue | Intermediate drafts already superseded |
| Simple CTA to continue or start fresh | Deadline if approaching | All prior exchanges in full |

## Do not

- Write a long summary of everything that happened in the prior session — the recap is an opening line, not a briefing memo. If the user needs a full briefing, they can request a matter summary separately.
- Run the recap for a continuous session — it feels patronizing in-session.
- Guess at matter details that are not clearly supported by the prior context — if uncertain, ask one focused question rather than asserting a potentially wrong recap.
- Omit the CTA — always end with a clear action option (continue / start fresh).

## Edge cases

- **Multiple active matters**: if the user has multiple open matters and it is unclear which one to resume, list the two or three most recent and ask which one to pick up.
- **Matter transferred to a new session by sharing**: if another user (e.g., a colleague) is picking up a matter started by a different user, surface the matter state without assuming the new user has the same context or authority level.
- **User resumes with a correction**: if the user's first turn after resuming corrects the recap ("actually we decided on 2 years, not 3"), accept the correction immediately and update the matter state.

## Related skills

- [[conversation-long-thread-compression]]
- [[conversation-professional-b2b]]
- [[conversation-uncertainty-language]]
