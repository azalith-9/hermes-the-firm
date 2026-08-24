---
name: connector-scheduled-tasks
description: Use when a legal-AI workflow needs to create, manage, or trigger recurring automated tasks — deadline reminders, periodic risk scans, weekly digest emails, document expiry alerts, or regulatory-change monitoring. This is a built-in platform capability, not an external integration. Triggers on any request to "remind me," "check this weekly," "alert me when," or "run this every [interval]" within a legal workflow context.
license: MIT
metadata: " id: connector.scheduled-tasks category: connector jurisdictions: [__multi__] priority: P2 intent: [__connector__] related: [connector-calendar, connector-gmail, connector-hubspot-crm, connector-posthog] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'connector'.
Registered as a flat plugin skill.
-->


# Connector — Scheduled Tasks

## What it does

The Scheduled Tasks connector is the platform's built-in cron-like automation layer. It allows legal workflows to be repeated at defined intervals without requiring the user to manually trigger them each time. Unlike the calendar connector (which manages personal calendar events), scheduled tasks run autonomously in the background and surface outputs to the user through notifications, emails, or dashboard updates.

This is an **internal platform capability** — not an integration with an external scheduling service. It is implemented as a server-side job queue with a cron scheduler.

## When to use this

Use scheduled tasks for anything that is:
- **Recurring and predictable** in interval (daily, weekly, monthly).
- **Monitor-then-alert** in nature (check for a condition; notify if condition met).
- **Not date-specific** (for fixed-date events, use [[connector-calendar]] instead).
- **Automated by design** (the user should not have to remember to trigger it).

## Setup

No external setup or API keys are required — scheduled tasks run on the platform's internal infrastructure.

Users create and manage tasks through the assistant interface:
- "Remind me every Monday to review pending DIFC filing deadlines" → creates a weekly task.
- "Alert me if there are new UAE labor law ministerial decisions" → creates a monitoring task with keyword triggers.
- "Send me a weekly digest of matter activity every Friday at 5pm GST" → creates a timed digest task.

Each task is stored in the platform's task registry with:
- Task ID and name.
- Schedule (cron expression or human-readable interval).
- Target action (function/skill to invoke).
- Output channel (in-platform notification, email, Slack).
- Owner (user ID).
- Status (active / paused / error).

## Task types

### Type 1 — Deadline reminders

Monitor a set of deadlines (from the matter registry or calendar) and send alerts at configurable intervals before the deadline:

```
Example configuration:
  Deadline: DIFC filing for Al-Hassan — 15 June 2024
  Alert schedule: 30 days before, 14 days before, 7 days before, 1 day before
  Channel: email + in-platform notification
  Action: surface deadline details + link to the draft document
```

Especially important for:
- Court filing deadlines (most jurisdictions impose strict consequences for missing).
- Regulatory response windows (e.g., DFSA response to a supervisory inquiry).
- Contract notice periods (e.g., termination notice deadlines).
- Option periods in commercial contracts.

### Type 2 — Regulatory monitoring

Periodically scrape a regulatory authority's publications page (via [[connector-firecrawl]]) and alert when new content matching defined keywords is published:

```
Example configuration:
  Source: CBUAE website (cbuae.gov.ae/news)
  Keywords: ["circular", "banking", "licensing", "AML"]
  Schedule: daily at 08:00 GST
  Alert: if new content found → notify compliance team + link to content
```

Useful for:
- Monitoring CBUAE, DFSA, ADGM FSRA, SAMA, BdL for new circulars.
- Tracking UAE Official Gazette for new decrees affecting client industries.
- Following FATF/MENAFATF guidance updates.

### Type 3 — Periodic risk scans

Run a risk-assessment skill against an active matter at regular intervals:

```
Example configuration:
  Matter: TechCo DIFC setup
  Skill: review-corporate-registry + ofac-screening
  Schedule: monthly on the 1st
  Output: diff vs last scan → surface only changes
```

Useful for ongoing due diligence on key counterparties or monitoring a client's regulatory compliance posture.

### Type 4 — Weekly digests

Aggregate and summarize activity from the past period and deliver as a structured email or in-platform report:

- Matter activity digest (new documents, events, notes from the past week).
- Skill usage summary (for platform administrators).
- Churn-risk summary (for customer-success team) — feeds from [[connector-posthog]].
- Pipeline update (for sales team) — feeds from [[connector-hubspot-crm]].

### Type 5 — Document expiry alerts

Track contracts and documents with defined expiry or renewal dates:

```
Example configuration:
  Document: Facility Agreement — Expiry 1 March 2025
  Alert schedule: 90 days before, 30 days before
  Action: notify responsible lawyer + generate renewal checklist
```

Relevant for:
- Loan facility renewal periods.
- Trade license renewals (UAE trade licenses expire annually; DIFC/ADGM licenses have defined renewal dates).
- NDA confidentiality period expiry.
- Power of attorney validity (Lebanese PoAs are typically issued for 1 year; UAE PoAs require Tawqi3i notarization renewal).

## Task management

Users can manage their tasks via the assistant:
- "Show me all my active scheduled tasks."
- "Pause the weekly digest until I return from leave."
- "Change the deadline reminder for Al-Hassan to 14-day and 3-day only."
- "Delete the monitoring task for UAE gazette — that matter is closed."

The assistant presents a list of current tasks with status and last-run time before making any modifications.

## Permissions & safety

- **User-owned tasks only.** A user can only create, modify, or delete tasks they own. Firm-wide tasks (e.g., a compliance-team-wide monitoring task) are created by an admin user and are read-only for other team members.
- **No autonomous write operations in tasks.** Scheduled tasks can read data and send notifications, but they cannot autonomously draft and send legal documents or emails. Any output requiring action must surface to a human for review first.
- **Rate limiting.** To prevent runaway task creation, a single user is limited to 50 active tasks. Platform-wide job queue is protected from overload.
- **Failure notification.** If a scheduled task fails three consecutive times (e.g., a scraped page structure changed), the owner is notified with the error detail and the task is paused pending review.

## Failure modes

| Failure | Cause | Resolution |
|---|---|---|
| Task not firing | Cron expression error | Validate cron expression; notify user; pause and correct |
| Scrape source changed | Regulatory website redesign broke the scraper | Alert user; update source URL; use [[connector-firecrawl]] with updated selector |
| Email digest not delivered | Email service issue | Retry; check delivery logs; surface in-platform if email fails |
| Escalation storm | Mass alert firing at once (e.g., 50 deadlines on the same day) | Implement digest batching; max 10 alerts per email; rest in platform |

## Related skills

- [[connector-calendar]]
- [[connector-gmail]]
- [[connector-hubspot-crm]]
- [[connector-posthog]]
- [[connector-firecrawl]]
