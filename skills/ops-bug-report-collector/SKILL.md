---
name: ops-bug-report-collector
description: Use when a user in a legal AI chat session signals that something is broken, behaving unexpectedly, or producing an error. Guides the assistant through detecting bug signals in conversation, gathering structured context from the user, automatically collecting session metadata, and submitting a properly classified Linear issue — all while enforcing PII redaction and tenant isolation.
license: MIT
metadata: " id: ops.bug-report-collector category: ops priority: P0 intent: [ops, bug-report, linear, incident, user-feedback] related: [ops-feature-request-collector, ops-linear-triage-from-chat-bug-report, ops-crash-report-formatter, ops-error-classifier] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'ops'.
Registered as a flat plugin skill.
-->


# Ops — Bug Report Collector

## When to use this

This skill activates when any of the following occur during a legal AI chat session:

- The user uses language that signals a malfunction: "this isn't working", "bug", "broken", "error", "that's wrong", "weird", "not what I expected", "try again", "this is wrong".
- A model failure event occurs (LLM provider error, tool failure, timeout, null response).
- A downstream tool returns an error during an agentic workflow (document upload failure, skill routing failure, connector timeout).
- The user reports that an output contradicted something they know to be true in their jurisdiction.

Do not activate on user disagreement with a legal interpretation — that is a [[review]] or escalation issue, not a bug. Activate only when the system itself appears to have failed.

## Detection heuristics

The assistant should watch for these signals, weighted by severity:

| Signal | Severity | Example |
|--------|----------|---------|
| Explicit "bug" or "error" language | High | "There's a bug" / "I got an error" |
| User repeats the same query multiple times | Medium | Third identical request in a row |
| User expresses frustration after a response | Medium | "That's completely wrong again" |
| Model returns a null, empty, or truncated response | High | Tool output: `{}` |
| Backend 5xx logged for the session | High | Server-side signal |
| Skills router fires an unexpected fallback | Medium | Router reaches default catch |

## Collection flow

### 1. In-chat prompt

At the next natural turn break (not mid-generation), surface:

> It looks like something might not be working as expected. Would you like me to create a bug report so the team can look into it?
>
> [**Yes, report it**]  [**No thanks**]

If the user selects "Yes, report it" (or equivalent affirmative), proceed to gather context.

### 2. Structured context gathering

Ask the following questions, one at a time:

1. "What were you trying to do?"
2. "What happened instead?"
3. "What did you expect to happen?"
4. "Do you have a screenshot or error message you can paste?"

Keep it short — the goal is to capture the user's description in their words. Do not paraphrase or interpret at this stage.

### 3. Auto-collected metadata

In parallel with the user's responses, automatically collect:

- User ID (anonymized tenant-scoped identifier, not raw email)
- Session ID
- Browser / OS / device (from user-agent)
- Last 5 messages in the conversation (redacted — see Privacy section)
- Skills router decision log for the affected turn
- Server-side error logs for the session (if accessible via backend API)
- Timestamp of the failure event
- Matter ID and jurisdiction (if the user was in a matter context)

### 4. Severity auto-detection

Classify severity based on the collected context:

| Level | Criteria |
|-------|----------|
| P0 | Outage (affects all users), data loss, security incident, loss of client work |
| P1 | Feature broken for many users, payment processing failure, frequent crashes in a session |
| P2 | Edge-case failure, single-user issue, incorrect output in a narrow case |
| P3 | Cosmetic, minor annoyance, non-blocking |

When in doubt, err toward higher severity — the triage skill can downgrade; under-triaged P0s cause real harm.

### 5. Linear submission

Create a Linear issue in the `LOUIS-BUGS` project with:

- **Title**: Short description derived from user's "what were you trying to do" answer
- **Description**: Structured report with all collected metadata and user quotes
- **Labels**: severity (P0–P3), persona (lawyer / consumer / enterprise), surface (web / mobile / word-plugin)
- **Priority**: mapped to severity level
- **Assignee**: auto-assigned per triage rules (see [[ops-linear-triage-from-chat-bug-report]])

### 6. User confirmation

After successful submission:

> Created Linear issue LOUIS-1234. The engineering team will investigate. Would you like to receive updates when this is resolved?
>
> [**Yes, notify me**]  [**No thanks**]

If the user opts in to updates, store their preference against the Linear issue for later follow-up.

## Privacy

Legal AI sessions may contain highly sensitive client information. The following redaction rules are non-negotiable:

- **PII redaction**: remove all names, email addresses, phone numbers, passport/ID numbers, company names, and case-specific identifiers before submission to Linear. Replace with `[REDACTED]`.
- **Client confidentiality**: never include the substantive content of a user's legal documents in a bug report. Capture only the structural context (e.g., "user was drafting an NDA" not the NDA text itself).
- **Tenant isolation**: bug reports from Tenant A must never appear in Tenant B's issue tracker, even if both use the same Linear workspace. Enforce workspace or label scoping.
- **Audit log**: maintain an audit log of every data element captured in a bug report, so users can request deletion.

## User control

- Users can opt out of bug reporting for a session by saying "don't log this" or pressing the opt-out button.
- Users who opt out can still manually report by revisiting the prompt or navigating to the Help menu.
- The opt-out preference is session-scoped, not account-scoped (users may want to report on the next session).

## Critical rules

- **Capture user's actual words** — do not paraphrase or sanitize the description.
- **Do not fabricate** bug details — if you cannot determine the cause, leave the cause field empty.
- **Never collect** the full text of a document under review as part of a bug report.
- **Respect timing** — do not interrupt a user mid-task to ask about a bug from 5 turns ago. Wait for a natural break.

## Related skills

- [[ops-feature-request-collector]] — the parallel flow for capturing feature requests
- [[ops-linear-triage-from-chat-bug-report]] — the downstream triage workflow that routes submitted bugs
- [[ops-crash-report-formatter]] — for formatting backend crash events into structured incident tickets
- [[ops-error-classifier]] — classifies errors by type to determine the right action
