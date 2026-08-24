---
name: connector-calendar
description: Use when a user wants to read, create, or manage calendar events in the context of legal-matter workflows — scheduling hearings, blocking deadline time, creating client appointments, or surfacing upcoming events as deadline context for drafting. Supports Google Calendar, Microsoft Outlook/Exchange Calendar, and iCal. Triggers on requests to schedule, block, or review upcoming events and on any request that requires inserting a known legal deadline into the calendar.
license: MIT
metadata: " id: connector.calendar category: connector jurisdictions: [__multi__] priority: P2 intent: [__connector__] related: [connector-gmail, connector-google-drive, connector-apple-notes, connector-scheduled-tasks] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'connector'.
Registered as a flat plugin skill.
-->


# Connector — Calendar

## What it does

The Calendar connector integrates with the user's calendar system to support legal-workflow scheduling: reading upcoming events for context, creating events for hearings or deadlines, blocking deep-work time, and surfacing calendar data when calculating limitation periods or procedural deadlines.

This connector is calendar-provider agnostic. The three supported providers are:

| Provider | Protocol | Notes |
|---|---|---|
| Google Calendar | Google Calendar API v3 | Most common in MENA startups and SME firms |
| Microsoft Outlook / Exchange | Microsoft Graph API | Dominant in large law firms and enterprise in-house teams |
| Apple iCal | CalDAV | Less common; works for solo practitioners on macOS |

## Setup / auth

### Google Calendar
- OAuth 2.0 authorization via Google account.
- Scopes required: `calendar.readonly` (for read) + `calendar.events` (for write).
- Per-user delegation: each lawyer authorizes their own calendar; no admin-wide delegation unless the firm has Google Workspace with domain-wide delegation explicitly configured.

### Microsoft Outlook / Exchange
- OAuth 2.0 via Microsoft Identity Platform (Azure AD).
- Scopes: `Calendars.Read` + `Calendars.ReadWrite` for event creation.
- Supports both personal Microsoft accounts and Microsoft 365 work accounts.
- For large firms on Exchange on-premise: requires Exchange Web Services (EWS) connector — contact IT for service account credentials.

### Apple iCal
- CalDAV endpoint; credentials are the user's Apple ID (iCloud account) or the firm's CalDAV server address.
- No dedicated OAuth flow — uses application-specific password or SSO.

All auth tokens are stored per-user (never shared across tenant), encrypted at rest, and scoped to the minimum necessary permissions.

## Capabilities

| Capability | Supported |
|---|---|
| List upcoming events (next N days) | Yes |
| Search events by keyword / matter reference | Yes |
| Create a new event with attendees | Yes |
| Update an existing event (reschedule, add notes) | Yes |
| Delete an event | Yes (with confirmation) |
| Block time as "Focus / Deep Work" | Yes |
| Add a legal deadline as a calendar entry with reminder | Yes |
| Surface today's schedule as context | Yes |
| Detect scheduling conflicts before booking | Yes |

## Usage patterns

### Pattern 1 — Create a hearing entry from a court notice

```
User: "Add the DIFC Court CMC on 3 June at 10am to my calendar"
→ Connector creates event: "DIFC CMC — Al-Hassan v. TechCo"
  Date: 3 June, 10:00 GST (UTC+4)
  Reminder: 24h before + 1h before
  Description: matter reference number
```

### Pattern 2 — Block deadline prep time

When a filing deadline is identified (e.g., statement of claim due 15 June):
- Create a "Deadline: SoC filing — Al-Hassan" event on 15 June.
- Create a 3-day "SoC drafting block" event from 12–14 June (deep-work, marked Busy).
- Remind the user 7 days before the deadline.

### Pattern 3 — Surface today's schedule as context before drafting

```
User: "What's on today?"
→ Connector returns today's events with titles, times, and matter tags
→ Assistant uses this to orient scheduling suggestions
```

### Pattern 4 — Calculate and insert a limitation date

Given a cause of action date (e.g., breach occurred 1 March 2024):
- Assistant calculates the limitation period under applicable law (e.g., 3 years under UAE Civil Transactions Law, 6 years under DIFC Contract Law).
- Connector creates a calendar reminder: "Limitation deadline — [Matter]" on the calculated expiry date.
- Reminder set at 6 months, 3 months, and 1 month before.

**Important:** limitation period calculations must be confirmed by the lawyer. The connector inserts the event as a reminder, not a legal opinion.

## Legal deadline awareness

Jurisdictional limitation periods vary significantly across the practice areas most relevant to MENA users:

| Jurisdiction | Contract claims | Tort claims | Employment claims |
|---|---|---|---|
| UAE (onshore) | 15 years (Civil Transactions Law) | 3 years | 1 year |
| DIFC | 6 years (DIFC Contract Law) | 3 years | 6 months (DIFC Employment Law) |
| ADGM | 6 years (English Limitation Act applied) | 6 years | 6 months (ADGM Employment Reg.) |
| Lebanon | 10 years (Code des Obligations et Contrats) | 3 years | 1 year |
| KSA | No formal statute of limitations; governed by shari'a principles; 5-year administrative prescription in practice | — | 1 year (Labor Law) |
| UK | 6 years (Limitation Act 1980) | 3 years (personal injury) / 6 years (general) | 3 months (Employment Tribunal) |
| France | 5 years (Code Civil) | 5 years | 2 years (Labor Court) |

These figures are guidance only. Always verify against current legislation and any contract-specific limitation clauses.

## Permissions & safety

- **Minimum scope:** request only the scopes needed. For read-only use cases (surfacing context), request `calendar.readonly` only.
- **Event content:** calendar event titles and descriptions may contain client names and matter references. Treat as confidential.
- **No broadcasting:** do not create events on behalf of counterparties or external attendees without explicit user confirmation.
- **Deletion requires confirmation:** any delete or cancel operation must present the event details to the user and require an explicit "Yes, cancel this" before proceeding.
- **Audit log:** all create/update/delete operations logged with user ID and timestamp.

## Failure modes

| Failure | Cause | Resolution |
|---|---|---|
| Auth expired | OAuth token rotated or revoked | Prompt user to re-authorize |
| Time-zone mismatch | User's calendar is in a different zone than the hearing | Confirm time zone explicitly before creating hearing events (GST / CET / BST) |
| Attendee invite bounced | Incorrect email address for invitee | Flag to user; do not retry silently |
| Recurring event confusion | Event is part of a recurring series | Warn user before modifying; ask "this event only" vs "all future events" |
| Exchange EWS timeout | Large firm Exchange server slow | Retry with exponential backoff; alert user if unavailable >60s |

## Related skills

- [[connector-gmail]]
- [[connector-google-drive]]
- [[connector-apple-notes]]
- [[connector-scheduled-tasks]]
