---
name: feed-status-incident-watcher
description: Use when the platform needs to monitor and surface Louis platform status events — incidents, degradations, scheduled maintenance, and recovery confirmations — to users in a non-intrusive but timely way. Integrates with the status page and incident management system to convert operational events into user-facing feed items, push alerts, and in-app banners calibrated to incident severity and user activity state.
license: MIT
metadata: " id: feed.status-incident-watcher category: feed jurisdictions: [__multi__] priority: P3 intent: [__feed__, system-status, incident-management, uptime-transparency] related: [feed-changelog-watcher, feed-haqq-press-releases, ops-churn-risk-detector] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'feed'.
Registered as a flat plugin skill.
-->


# Status Incident Watcher Feed Surface

## Purpose

Legal practitioners depend on Louis for time-sensitive work — deadlines, court filings, deal closings. Platform unavailability or degradation during a critical moment erodes trust disproportionately. This feed surface provides transparent, real-time, proactive communication about system status events, ensuring users are never left wondering whether a problem is on their side or the platform's.

The status incident watcher is the negative-space companion to [[feed-changelog-watcher]]: where the changelog communicates improvements, this surface communicates problems and resolutions.

## Event types and severity levels

| Severity | Definition | Examples |
|---|---|---|
| P0 — Critical outage | Full service unavailability; no users can access Louis | API down, auth service failure, database corruption |
| P1 — Major degradation | Core feature broken for significant user subset | AI skill responses failing, document generation broken |
| P2 — Minor degradation | Non-core feature impaired; workaround exists | Feed not updating, push notifications delayed |
| P3 — Maintenance | Planned downtime or partial service impact | Scheduled database migration, API version upgrade |
| Resolved | Recovery from P0/P1/P2 | Service restored; post-incident report pending |

## Monitoring sources

- **Status page** (e.g., statuspage.io or self-hosted): primary source of structured incident data.
- **Internal alerting** (PagerDuty / OpsGenie / equivalent): incident creation triggers feed item.
- **Synthetic monitoring**: automated health checks (endpoint uptime, AI response latency, document generation pipeline health).
- **User-reported issues**: if > N users report the same error within a short window, auto-escalate to P2.

## Delivery logic by severity

### P0 — Critical outage
- Immediate in-app banner (red) surfaced to all active users.
- Push notification to all users with notifications enabled.
- Email to enterprise/eFirm account admins.
- Status feed item: created within 5 minutes of incident declaration.

### P1 — Major degradation
- In-app banner (orange) surfaced to affected users.
- Push notification to users actively using the affected feature.
- Status feed item: created within 10 minutes.

### P2 — Minor degradation
- Status feed item only (no banner, no push unless user is actively experiencing the issue).
- Created within 30 minutes.

### P3 — Planned maintenance
- Status feed item + in-app notice created ≥ 24 hours before the maintenance window.
- Email to enterprise admins if downtime > 30 minutes.

### Resolved
- In-app banner cleared.
- Resolution status feed item surfaced to users who saw the incident item.
- Post-incident summary published ≤ 48 hours after P0/P1 resolution.

## Output spec

```json
{
  "id": "status-item-uuid",
  "incident_id": "INC-2025-0512-001",
  "severity": "P1",
  "status": "investigating | identified | monitoring | resolved",
  "title": "AI Skill Responses Intermittently Failing",
  "message": "We are investigating reports of intermittent failures when invoking legal drafting and review skills. Some users may experience errors or delayed responses. Our team has identified the issue and is deploying a fix.",
  "started_at": "2025-05-12T14:23:00Z",
  "resolved_at": null,
  "affected_features": ["draft-skills", "review-skills"],
  "source_url": "https://status.louis.law/incidents/INC-2025-0512-001",
  "updates": [
    {
      "timestamp": "2025-05-12T14:23:00Z",
      "status": "investigating",
      "message": "Investigating reports of AI skill failures."
    },
    {
      "timestamp": "2025-05-12T14:45:00Z",
      "status": "identified",
      "message": "Root cause identified: upstream model API rate limit. Fix deploying."
    }
  ]
}
```

## Communication tone guidelines

Status communications must be:
- **Honest**: acknowledge the impact accurately. Do not minimize a P1 as "minor."
- **Non-technical by default**: "AI responses are taking longer than usual" is better than "increased p99 latency on inference endpoint."
- **Action-oriented where possible**: if a workaround exists, state it. If the user should save their work before maintenance, say so.
- **Timely**: an incident update 2 hours after a P0 is declared is worse than no update; the target is < 15 minutes to first communication.
- **Closed-loop**: every incident must have a "Resolved" status update. Incidents cannot be quietly forgotten.

## Post-incident report format

For P0 and P1 incidents, publish a post-incident report:

1. **Summary**: what happened, what users experienced, duration.
2. **Root cause**: what caused the incident (non-technical summary).
3. **Resolution**: what was done to fix it.
4. **Prevention**: what changes will prevent recurrence.
5. **Timeline**: key timestamps in the incident lifecycle.

## Failure modes

- **Status page itself unavailable**: if the status page is unreachable, the in-app system falls back to a static banner: "We're experiencing technical difficulties. Our team is investigating. Check status.louis.law."
- **Overcommunication fatigue**: P2 incidents that resolve within 15 minutes should be suppressed from the user feed (log in ops only) unless the user was actively using the affected feature.
- **False alarms**: synthetic monitoring false positives should be resolved before surfacing to users. Target: zero false-alarm user notifications per month.

## Related skills

- [[feed-changelog-watcher]]
- [[feed-haqq-press-releases]]
- [[ops-churn-risk-detector]]
