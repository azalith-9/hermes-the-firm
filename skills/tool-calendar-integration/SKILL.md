---
name: tool-calendar-integration
description: Use when connecting a lawyer's Google Calendar, Outlook, or iCal to Louis for deadline management, court-date blocking, and statute-of-limitations reminders. Enables automatic calendar population from matter management, priority-based meeting-slot suggestions, and deep-work time blocking for drafting workflows. Pairs with the deadline calculator for end-to-end legal deadline orchestration.
license: MIT
metadata: " id: tool.calendar-integration category: tool jurisdictions: [__multi__] priority: P2 intent: [calendar, scheduling] related: [tool-date-tool-deadline-calculator, pa-workflow-litigation, efirm-deadline-tracker] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'tool'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Tool — Calendar Integration

## What it does

Integrates Louis with a lawyer's primary calendar (Google Calendar, Microsoft Outlook, Apple iCal) to provide deadline-aware scheduling, automatic court-date blocking, statute-of-limitations reminders, and deep-work time management for drafting tasks.

## Setup / auth

| Calendar provider | Auth method | Notes |
|---|---|---|
| **Google Calendar** | OAuth 2.0 (Google API) | Requires `https://www.googleapis.com/auth/calendar` scope; supports read + write |
| **Microsoft Outlook / Exchange** | OAuth 2.0 (Microsoft Graph API) | Requires `Calendars.ReadWrite` scope; works for O365 and Exchange Online |
| **Apple iCal / CalDAV** | CalDAV protocol | Less common for corporate environments; supports read + write via CalDAV server |

**Permission scope:** Request the minimum scope needed. If only deadline-blocking is required, prefer read + event-creation; do not request full calendar access unless needed.

**Multi-calendar support:** Lawyers typically have a personal, a shared firm, and a matter-specific calendar. Allow selection of target calendar for each event type during setup.

## Capabilities

### 1. Court-date auto-blocking

When a court date, hearing, or filing deadline is entered in matter management (via [[efirm-deadline-tracker]] or manual entry), automatically create a calendar event:
- Title: `[Matter ref] — [Event type] — [Court/Tribunal]`
- Duration: Estimated hearing length or full day for travel requirements
- Location: Court address (look up from jurisdiction directory)
- Description: Matter reference, case number, counsel present
- Reminders: 7 days, 1 day, 2 hours before

### 2. Deadline-driven meeting suggestions

When a matter has an upcoming deadline, Louis can analyse the lawyer's calendar and suggest:
- Optimal draft-review slots in the week before the deadline (avoiding back-to-back meetings)
- "Pre-deadline buffer" — block 1–2 hours the day before as protected time
- Avoid scheduling non-urgent meetings the day of a major filing

### 3. Statute of limitations reminders

For active matters, surface limitation deadlines as calendar events with advance reminders:
- 6 months before: informational reminder
- 3 months before: action-required reminder
- 30 days before: urgent alert
- Limitation period lookup integrates with [[tool-date-tool-deadline-calculator]] for jurisdiction-aware computation

### 4. Deep-work blocking for drafting

When a drafting task is assigned (contract draft, brief, opinion letter), block time on the calendar:
- Default: 2–3-hour focused blocks, morning preferred (configurable)
- Auto-label: "Louis Drafting Block — [Document name]"
- Do not create back-to-back drafting blocks with no break

## Output schema

```json
{
  "events": [
    {
      "id": "evt_001",
      "title": "M-2024-045 — Hearing — ADGM Court of First Instance",
      "start": "2026-06-15T09:00:00+04:00",
      "end": "2026-06-15T13:00:00+04:00",
      "location": "ADGM Courts, Abu Dhabi Global Market Square, Al Maryah Island",
      "matterId": "M-2024-045",
      "type": "court_hearing",
      "reminders": [
        { "minutesBefore": 10080, "method": "email" },
        { "minutesBefore": 1440, "method": "popup" }
      ],
      "calendarId": "primary"
    }
  ],
  "syncStatus": "success",
  "nextSyncAt": "2026-05-15T06:00:00Z"
}
```

## Usage patterns

### Pattern 1 — New matter onboarding

On matter creation, extract all known dates (court dates, filing deadlines, contractual milestones) → batch-create calendar events → confirm with user before committing.

### Pattern 2 — Weekly deadline sweep

Every Monday morning, run a look-ahead 14-day window → pull all matter deadlines → surface a digest ("You have 3 deadlines this week: ...") → offer to block preparation time.

### Pattern 3 — Deadline from chat

User: "I need to file a response in the DIFC Court within 21 days of today."
→ Compute due date using [[tool-date-tool-deadline-calculator]] (with DIFC court rules and UAE public holidays)
→ Offer to create calendar event → confirm → create.

## Permissions & safety

- Never delete existing calendar events; only create and update events created by Louis.
- Always confirm before creating recurring events or bulk-creating more than 5 events at once.
- Do not expose calendar data (meeting titles, locations) in chat unless the user has explicitly opened a scheduling context.
- Respect Hijri calendar awareness: in KSA and UAE, official deadlines may reference Hijri dates; convert to Gregorian before calendar entry and note the Hijri date in the event description.

## Failure modes

| Failure | Response |
|---|---|
| OAuth token expired | Prompt re-authentication; do not silently fail |
| Calendar write permission denied | Explain required scope; provide re-authorisation link |
| Duplicate event detected | Warn before creating; ask user to confirm or skip |
| Timezone mismatch | Always display timezone in event confirmation; default to user's registered timezone |

## Related skills

- [[tool-date-tool-deadline-calculator]]
- [[pa-workflow-litigation]]
- [[efirm-deadline-tracker]]
