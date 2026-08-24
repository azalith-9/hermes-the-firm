---
name: docs-status-page-reader
description: Use when the platform or a specific Louis component (API, chat, OCR, drafting engine, citation lookup) appears degraded or unavailable, and the system or a user needs to surface the current operational status. Drives in-product status banners, support triage, and incident communication by reading the live status page and reporting per-component health.
license: MIT
metadata: " id: docs.status-page-reader category: docs jurisdictions: [__multi__] priority: P2 intent: [status, incident, degraded service, uptime, system health] related: [docs-security-overview, docs-tenant-isolation-explainer, docs-sso-saml-setup] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'docs'.
Registered as a flat plugin skill.
-->


# Status Page Reader — Louis Platform Health

## Purpose

This skill surfaces real-time operational status for each Louis platform component. It is used in two contexts:

1. **In-product banners** — when the application detects latency or errors, it calls this skill to retrieve the authoritative status and display a user-friendly notice rather than a generic error.
2. **Support triage** — when a user reports an issue, this skill is the first check: is this a platform incident or a user-specific problem?

## Status page URL

`https://louis.haqq.ai/status`

## Platform components monitored

| Component | Description | User impact when degraded |
|---|---|---|
| **API** | Core REST/GraphQL API layer | All features unavailable; login may fail |
| **Chat** | AI chat interface and model inference | Conversations not loading or slow |
| **OCR** | Document ingestion and optical character recognition | PDF/image uploads fail; extracted text unavailable |
| **Drafting** | AI drafting engine | Draft generation fails or times out |
| **Citations** | Legal citation lookup and validation | Citation insertion returns no results |

## Status levels

| Level | Color | Meaning |
|---|---|---|
| **Operational** | Green | Component fully functional |
| **Degraded Performance** | Yellow | Component functional but slower or partially limited |
| **Partial Outage** | Orange | Some users or features affected |
| **Major Outage** | Red | Component unavailable for all or most users |
| **Under Maintenance** | Blue | Planned maintenance window |

## In-product behavior

When the API or Chat component is degraded or worse:
- Display a banner at the top of the application:
  > "Some features may be unavailable. Check [status.haqq.ai](https://louis.haqq.ai/status) for updates."
- Do not suppress individual error messages — surface them alongside the banner.
- Do not retry indefinitely; apply exponential back-off and surface a clear "Try again later" message after 3 failures.

When OCR is degraded:
- Show a specific message on the document upload dialog:
  > "Document processing is currently experiencing delays. Your upload will be queued and processed once the service recovers."

When Drafting is degraded:
- Disable the "Generate Draft" button and display:
  > "The drafting engine is temporarily unavailable. Please try again shortly."

## Support triage logic

```
User reports issue
  → Read status page
  → If any relevant component is not Operational:
      "We're aware of an issue affecting [component]. Our team is working on it.
       Follow https://louis.haqq.ai/status for updates."
  → Else:
      Collect user-specific diagnostics (browser, account, specific document, error message)
      Escalate to support ticket
```

## Incident communication standards

- **Detection to first update**: target < 15 minutes for Major Outage.
- **Update frequency during incident**: every 30 minutes until resolved.
- **Post-incident review**: published on the status page within 5 business days for Major Outage or incidents lasting > 2 hours.
- **Customer notification**: Enterprise customers with SLA agreements receive direct email notification within 30 minutes of a Major Outage declaration.

## How to subscribe to status updates

Users can subscribe to status page notifications at `https://louis.haqq.ai/status/subscribe`:
- Email notifications for all incidents.
- Webhook option for enterprise integrations (pipe alerts into Slack, PagerDuty, or your own monitoring).

## Related skills

- [[docs-security-overview]]
- [[docs-tenant-isolation-explainer]]
- [[docs-sso-saml-setup]]
