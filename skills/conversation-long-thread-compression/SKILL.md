---
name: conversation-long-thread-compression
description: Use when a legal AI conversation exceeds approximately 50 turns or approaches 80% of the context window, and the agent must compress older turns into a structured matter-summary without losing any material decisions, open issues, or user preferences. This is a core behavioral skill that applies to all legal matter types across all jurisdictions. Triggers automatically on context pressure, at major matter milestones, or on explicit user request.
license: MIT
metadata: " id: conversation.long-thread-compression category: conversation priority: P0 intent: [__core__, context compression, thread summary, matter memory] related: [conversation-session-memory-recap, conversation-professional-b2b, conversation-uncertainty-language] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'conversation'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Long-Thread Compression

## When this applies

Activate when any of the following conditions are true:

1. The conversation has exceeded approximately **50 turns** (a "turn" being one user message + one assistant response).
2. The estimated context window utilization is **at or above 80%** (based on estimated token count or explicit signal from the runtime environment).
3. A major **matter milestone** has been reached: a document has been finalized, a negotiation round has concluded, or a filing has been submitted.
4. The user explicitly requests: "summarize this thread", "compress the context", "give me a summary of where we are", or similar.
5. Before **exporting or sharing** the thread (e.g., sending a matter summary to a client or colleague).

This skill does not apply to short, fresh conversations or to single-turn queries with no ongoing matter context.

## Behavior

Compress older conversation turns into a single, structured matter-summary block. Replace compressed turns with the block in place. Keep the most recent 5–10 turns full and uncompressed — they contain the live working context that must not be flattened.

### What to preserve — no exceptions

Every piece of information in the following categories must survive compression, even if it requires multiple sentences:

- **Matter context**: parties (full names, roles), document type, purpose of the matter, deadline.
- **Jurisdiction and governing law**: confirmed or tentative.
- **Key decisions made**: any clause, position, or agreement that was reached — include the turn number where confirmed, the precise term agreed, and by whom.
- **Open issues**: explicitly list every unresolved item, every pending question, and every "I'll check this" noted during the thread.
- **User preferences expressed**: drafting style, tone, formatting preferences (e.g., "user prefers IRAC for analysis", "client wants bilingual AR-EN final draft", "use numbered clauses not lettered").
- **Skill IDs invoked**: which skills have already been run (prevents re-running intake already completed).
- **Client instructions and constraints**: deadlines, redline instructions, negotiating positions, budget constraints.

### What to drop — no exceptions

- Verbose back-and-forth on questions that have already been resolved.
- Confirmations and simple acknowledgments ("Got it, I'll add that", "OK, proceeding").
- Pleasantries and social exchange.
- Earlier exploratory queries that were subsequently superseded by cleaner instructions.
- Intermediate draft versions that were replaced — keep only the most recent version state and the decisions made on each revision cycle.

## Compression format

Replace older turns with a single, delimited system-style note in this format:

```
[CONTEXT FROM EARLIER TURNS — COMPRESSED]

Matter: [Document type] — [Party A] x [Party B]
Jurisdiction: [governing law + forum]
Purpose: [one-sentence statement of the matter objective]
Deadline: [if set]

Decisions made:
- [Decision 1] (turn [N])
- [Decision 2] (turn [N])
- [Decision 3] (turn [N])

Open issues:
- [Issue 1] — [status: awaiting client input / pending research / to be drafted]
- [Issue 2] — [status]

User preferences:
- [Preference 1]
- [Preference 2]

Skills invoked: [skill-id-1], [skill-id-2]

[END COMPRESSED CONTEXT]
```

### Example

```
[CONTEXT FROM EARLIER TURNS — COMPRESSED]

Matter: MSA Negotiation — Acme Group (Provider) x Globex DMCC (Customer)
Jurisdiction: DIFC law; DIFC Courts
Purpose: Closing a 3-year managed technology services agreement within 30 days
Deadline: Execution by 14 June 2025

Decisions made:
- Aggregate liability cap: 100% of fees paid in the prior 12 months (turn 12)
- IP ownership: all custom deliverables assigned to Customer; background IP retained by Provider with license-back (turn 18)
- Dispute resolution: DIAC arbitration, Dubai seat, English language, 3-person tribunal (turn 22)
- Data protection: DIFC DPA addendum to be attached as Exhibit C (turn 28)

Open issues:
- Termination for convenience notice period: Provider wants 90 days; Customer wants 45 days — unresolved (turn 31)
- Material adverse change definition: Provider's counsel has not confirmed acceptance of Globex's proposed language (turn 35)
- Confidentiality survival period: Customer wants 5 years post-term; Provider accepted 3 years; compromise not yet reached (turn 38)

User preferences:
- IRAC structure for legal analyses
- Bilingual AR-EN for the final execution version
- Track-changes / redline style: IILR redline format preferred

Skills invoked: conversation-intake-msa, draft-msa

[END COMPRESSED CONTEXT]
```

## When to notify the user

- **Before compressing**: notify the user once (briefly) that you are compressing older turns to preserve context quality. Example: *"This thread is getting long — I'm compressing earlier turns into a structured summary to preserve context. Here's what I've captured:"* (then show the compressed block).
- **After compressing**: the compressed block is visible to the user and can be edited or corrected.
- Do not compress silently without any notification — the user should know the compression occurred and should have an opportunity to correct any errors in the summary.

## Quality standards

- **No information loss**: a practitioner reading only the compressed block should be able to fully reconstruct the state of the matter without reading any earlier turns.
- **Precise language**: use the same legal precision as the underlying conversation. Do not paraphrase "24-month aggregate liability cap" as "limited liability" — the precision matters.
- **No invented decisions**: only record decisions that were actually made in the thread. Do not fill in gaps with assumptions.
- **Turn references**: include turn numbers for key decisions where feasible — they allow the user to scroll back to verify if needed.

## Edge cases

- **User corrects the summary**: accept corrections immediately and update the compressed block. If a correction reveals that a decision was misrecorded during the session, flag it as an open issue for re-confirmation.
- **Multiple matters in one thread**: if the thread covers more than one matter (e.g., NDA first, then a follow-on MSA), create separate compressed blocks per matter. Do not conflate them.
- **Confidential matter**: the compressed block should not be copied out of the session without appropriate privilege and confidentiality review. Flag if the user is about to share the thread.
- **Short threads approaching the limit suddenly**: a rapid influx of long documents (uploaded contracts, lengthy research) can fill the context faster than turn-count suggests. Trigger compression based on estimated token utilization, not just turn count.

## Do not

- Compress without preserving open issues — partial information is worse than no information in a legal context.
- Drop user preferences — they took effort to elicit and re-eliciting them wastes the user's time.
- Over-compress to a single line — the compression block should be as long as it needs to be to capture the matter state completely.
- Compress the most recent 5–10 turns — these are the live working context.

## Related skills

- [[conversation-session-memory-recap]]
- [[conversation-professional-b2b]]
- [[conversation-uncertainty-language]]
