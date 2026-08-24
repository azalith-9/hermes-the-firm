---
name: ops-crash-report-formatter
description: Use when a client-side crash (browser console error, mobile app crash) or backend failure (HTTP 500, unhandled exception) occurs during a legal AI session. Formats raw crash data — stack traces, source-map decoded frames, device/OS info, last user actions — into a structured incident ticket with severity classification and owner routing to Linear and Slack.
license: MIT
metadata: " id: ops.crash-report-formatter category: ops jurisdictions: [__multi__] priority: P2 intent: [crash, ops, incident, stack-trace, error-reporting] related: [ops-bug-report-collector, ops-error-classifier, ops-linear-triage-from-chat-bug-report] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'ops'.
Registered as a flat plugin skill.
-->


# Ops — Crash Report Formatter

## Purpose

Raw crash data — minified stack traces, browser user-agent strings, native crash dumps — is unreadable to engineers during an incident. This skill takes a raw crash event and produces a structured, human-readable incident ticket with enough context to diagnose and assign the issue immediately.

## When to use this

Activate when any of the following is detected:

- **Browser console error**: uncaught JavaScript exception, `TypeError`, `ReferenceError`, unhandled promise rejection.
- **Mobile crash**: native iOS/Android crash report from Sentry or similar.
- **Backend 500**: HTTP 500 or unhandled exception in the API layer.
- **LLM provider error**: upstream model API returns a 5xx or times out.
- **Tool/connector failure**: a connected tool (document parser, search, filing system) throws an error that surfaces to the user.

## Input

The formatter receives a raw crash event object. Typical fields:

```json
{
  "errorType": "TypeError",
  "message": "Cannot read properties of undefined (reading 'clauses')",
  "stackTrace": "<minified JS stack>",
  "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)...",
  "sessionId": "<UUID>",
  "userId": "<anonymized ID>",
  "tenantId": "<UUID>",
  "matterId": "<UUID or null>",
  "lastEvents": ["document_upload", "skill_route", "draft_start"],
  "timestamp": "2026-05-14T09:12:00Z",
  "environment": "production"
}
```

## Formatting steps

### 1. Stack trace cleanup
- Decode minified stack traces using the source map for the current build version.
- Identify the top 5 frames in the decoded stack, prioritizing application code over library code.
- Highlight the frame where the exception originated.

### 2. Source-map decoding
- Map minified filenames and line numbers to original source paths.
- Example: `bundle.js:1:98234` → `src/components/DraftBoard/ClauseParser.tsx:87:12`

### 3. Browser / OS / device extraction
Parse the user-agent string into:
- Browser name and version
- OS name and version
- Device type (desktop / mobile / tablet)

### 4. Last user actions
Extract the last 5 events from the session event log, in chronological order. These represent the user's path leading to the crash. Redact any content from document text — keep only event names and metadata (e.g., `document_upload: NDA_v2.docx, 45KB` not the document content).

### 5. Context fields
- **Tenant ID**: always included for routing and isolation.
- **Matter ID**: included if the crash occurred in a matter context (helps identify if a specific matter's data is involved).
- **Jurisdiction**: included if known from the session context.
- **Skill route**: if the crash occurred during an AI skill invocation, include the skill ID and the router decision for that turn.

### 6. Severity classification

| Level | Criteria |
|-------|----------|
| P0 | Crash affects all users or all instances of a feature; data loss possible; production outage |
| P1 | Crash reproducible for a class of users (e.g., all users uploading PDFs > 10MB); no data loss |
| P2 | Crash isolated to specific session/user/configuration; workaround available |
| P3 | Non-blocking visual glitch or cosmetic error |

### 7. Owner assignment

| Crash origin | Suggested owner |
|---|---|
| Frontend (browser JS, React component) | Frontend lead |
| Backend API (Node/Python server) | Backend lead |
| AI/skill layer (model error, router failure) | AI team |
| Infrastructure (database timeout, memory) | Infra/DevOps |
| Third-party connector (Stripe, HubSpot, etc.) | Ops lead |

## Output format

The formatter produces a structured incident ticket:

```markdown
**Crash Report — [Severity] — [Error Type]**
Occurred: [timestamp]
Environment: production

**Error**: [error type] — [message]
**Origin**: [decoded source location]

**Stack trace (top 5 frames)**:
1. ClauseParser.tsx:87 — parseClauseArray()
2. DraftBoard.tsx:203 — handleDocumentLoad()
3. ...

**User context**:
- Browser: Chrome 124 / macOS 14.4 / Desktop
- Session: [session ID]
- Tenant: [tenant ID]
- Matter: [matter ID or "none"]

**Last 5 user actions**:
1. document_upload (NDA_v2.docx, 45KB)
2. skill_route → draft-nda-unilateral
3. draft_start
4. [error occurred here]

**Severity**: P1
**Suggested owner**: Frontend lead
**Routing**: Linear DES-incident + Slack #louis-incidents
```

## Routing

After formatting, the incident ticket is:
- Created as a Linear issue in the `DES-incident` project with the classified severity.
- Posted to the Slack channel `#louis-incidents` as a thread message with the formatted summary.
- If P0: additionally pages the on-call engineer via PagerDuty or equivalent.

## Related skills

- [[ops-bug-report-collector]] — collects user-reported bugs that may not produce crashes
- [[ops-error-classifier]] — classifies errors by type to determine retry vs escalation
- [[ops-linear-triage-from-chat-bug-report]] — triage workflow for submitted issues
