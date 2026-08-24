---
name: efirm-time-entry-from-chat
description: Use when a lawyer's work activity is described or narrated in a chat or conversation interface and that activity needs to be converted into properly formatted billing time entries. The skill extracts task descriptions, duration estimates, matter references, and timekeeper identity from natural-language input and outputs structured time records ready for billing-system import. Part of the eFirm firm-management product suite.
license: MIT
metadata: " id: efirm.time-entry-from-chat category: efirm jurisdictions: [__multi__] priority: P2 intent: [time-entry, billing, timekeeping, natural-language, automation] related: - efirm-matter-summary-for-billing - efirm-finance-wip-aging-report - efirm-finance-utilization-dashboard - efirm-matter-creation-flow source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'efirm'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Time Entry from Chat

## When to use this

Use this skill when:
- A lawyer describes their day's work conversationally and wants it turned into proper time entries without manual form-filling.
- A voice note or chat message from a lawyer (e.g., "I spent about 2 hours this morning on the ACME SPA negotiations and then 45 minutes reviewing the employment agreements") needs to be converted to structured billing records.
- End-of-day or end-of-week time capture is being done in bulk from a narrative or meeting notes.
- A lawyer has been working in the field (court, client site, travel) and needs to record time quickly from a mobile interface.

Time capture is the first link in the revenue chain. Incomplete or delayed time entry leads to WIP understatement, billing disputes, and revenue leakage. Reducing the friction of time entry — by accepting natural-language input — is proven to improve capture rates.

## Input formats accepted

The skill accepts any of the following:

### 1. Casual narration

> "This morning I reviewed the term sheet for Al Baraka and sent comments to the client. Probably 90 minutes. Then had a call with opposing counsel on the DIFC arbitration for about 45 minutes."

### 2. Structured bullet list

> - ACME acquisition: drafted indemnity clause, 2 hrs
> - Call with Sarah re: employment matter: 30 min
> - Reviewed regulatory opinion for Noor Capital: 1 hr 15 min

### 3. Voice transcript (post-transcription)

Any text output from a voice memo or dictation app describing legal work performed.

### 4. Meeting notes

Calendar entries or meeting summaries that contain billable activity descriptions.

## Extraction logic

From each input, the skill extracts:

| Field | Extraction method | Notes |
|---|---|---|
| Matter reference | Named entity recognition (client name / matter name / matter number) | If ambiguous, prompt user to confirm |
| Task description | Verb + object extraction from narrative | Refined to billing-grade description (see below) |
| Duration | Time expressions ("2 hours", "90 minutes", "half an hour", "all morning") | Convert to decimal hours; flag estimates |
| Timekeeper | Inferred from context (logged-in user) or named in text | Confirm if different from session user |
| Date | Today's date as default; override if stated | Validate against working day (not weekend/holiday) |
| Activity code | Mapped from task description to firm's activity code list | Requires firm code table as reference |

## Billing-grade description standards

Raw chat language is not billing-ready. The skill rewrites descriptions to meet billing standards:

| Raw input | Billing-grade output |
|---|---|
| "reviewed documents" | "Reviewing and analysing draft share purchase agreement; preparing summary of open points for client" |
| "called opposing counsel" | "Telephone conference with opposing counsel re: DIFC arbitration procedural timetable; follow-up email summarising agreed steps" |
| "research" | "Legal research: enforceability of non-compete clauses under UAE Labour Law; preparation of research memorandum" |
| "meeting with client" | "Client meeting re: status of proposed acquisition of [Target]; discussion of due diligence findings and proposed timeline to signing" |

The skill errs toward specificity. If the raw input lacks enough context to write a specific description, it flags the entry and asks the user for a brief elaboration before finalizing.

## Output format

Each extracted time entry is output as:

```
TIME ENTRY

Timekeeper:     [Name / ID]
Date:           [YYYY-MM-DD]
Matter:         [Matter ID] — [Matter title]
Client:         [Client name]
Hours:          [X.X decimal]  [or "ESTIMATE — confirm"]
Activity code:  [Code] — [Description]
Narrative:      [Billing-grade description]
Status:         Draft — pending review
```

Multiple entries from a single input are presented as a numbered list. The user reviews, edits as needed, and confirms before records are written to the billing system.

## Confirmation step

Before any time entry is committed to the billing system, the skill presents a review summary:

```
REVIEW — [N] TIME ENTRIES — [Date]

1. [Matter ID]  [X.X hrs]  "[Description]"
2. [Matter ID]  [X.X hrs]  "[Description]"
...

Total hours captured: [Y.Y hrs]

Confirm to post / Edit individual entries / Discard
```

This step prevents errors from being committed to the billing record. The user can edit any field, split a combined entry into separate entries, or add a missing matter reference before confirming.

## Common issues and handling

| Issue | Handling |
|---|---|
| Ambiguous matter reference | Prompt: "Did you mean [Matter A] or [Matter B]? Both involve [Client]." |
| Duration not stated | Prompt: "How long did the [task description] take?" |
| Non-billable activity identified | Flag: "This appears to be non-billable (training / admin). Confirm activity code." |
| Duplicate entry risk | Warn if an entry with similar description on the same matter is already in draft status for the same date |
| Time > 12 hrs in one day | Flag for review — possible error or extreme circumstance |
| Weekend / holiday date | Warn: "[Date] is a [weekend / holiday]. Confirm you worked on this date." |

## Anti-patterns

- **Block billing via chat**: if the user narrates "spent the morning on various ACME matters", insist on task-level breakdown before creating entries. Block billing violates most billing guidelines and creates invoice disputes.
- **Recreating time from memory**: entries created more than 5 days after the fact should be flagged as "reconstructed" to alert the billing partner.
- **Over-precise time**: converting "a couple of hours" to exactly 2.00 hrs is fine; do not invent precision that the user did not express.

## Integration

- Confirmed entries are pushed to the billing system (Clio / Elite / Aderant / custom API).
- Entries in Draft status appear in the WIP report ([[efirm-finance-wip-aging-report]]) immediately; they do not appear in client-facing reports until confirmed.
- Utilization tracking ([[efirm-finance-utilization-dashboard]]) updates in real time as entries are confirmed.

## Related skills

- [[efirm-matter-summary-for-billing]]
- [[efirm-finance-wip-aging-report]]
- [[efirm-finance-utilization-dashboard]]
- [[efirm-matter-creation-flow]]
