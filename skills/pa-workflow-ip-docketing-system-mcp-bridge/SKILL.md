---
name: pa-workflow-ip-docketing-system-mcp-bridge
description: Use when a patent attorney or IP team needs to integrate the agent with a patent docketing system via MCP (Model Context Protocol) — pulling annuity calendars, office action deadlines, filing status, and portfolio renewal recommendations into AI-assisted workflow. Covers the bridge architecture, data schema, calendar management, and automated deadline alerts. Triggers when connecting the agent to a docketing system or when managing IP portfolio deadlines.
license: MIT
metadata: " id: pa-workflow.IP.docketing-system-MCP-bridge category: pa-workflow practice_area: IP intent: ['__workflow__', 'docketing', 'MCP', 'IP', 'deadlines', 'annuities'] related: - pa-workflow-ip-claim-drafting-from-disclosure - pa-workflow-ip-office-action-response-drafter - pa-workflow-ip-opposition-procedure-epo priority: P1 source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'pa-workflow'.
Namespaced as louis-<category>-<skill> on registration.
-->


# IP — Docketing System MCP Bridge

Patent docketing is one of the highest-risk activities in IP practice: a missed annuity payment or a lapsed office action deadline can result in permanent loss of patent rights. An MCP bridge between the agent and a patent docketing system enables AI-assisted deadline management, filing strategy, and portfolio analysis — while keeping the docketing system as the authoritative record.

## Purpose

Bridge the agent to a patent docketing system to:
1. Pull annuity payment calendars and flag upcoming due dates
2. Retrieve office action deadlines and status
3. Provide filing strategy input across the portfolio
4. Surface renewal recommendations (pay / abandon / sell / licence)
5. Generate portfolio health reports

## Architecture

### MCP integration model

The docketing system exposes its data as a set of MCP tools. the agent queries these tools, reasons over the returned data, and produces analysis and recommendations.

```
the agent ←→ MCP Tool: ip_docket_query
              ├── get_annuities_due(days_ahead: int) → AnnuityRecord[]
              ├── get_office_actions_pending() → OARecord[]
              ├── get_application_status(app_number: str) → ApplicationRecord
              ├── get_portfolio_summary(client_id: str) → PortfolioSummary
              └── update_deadline_note(record_id: str, note: str) → void
```

Supported docketing systems commonly used in MENA and global IP practice:
- CPI (Computer Packages Inc.) — widely used in MENA
- Anaqua
- Foundation IP
- IPManager
- Custom systems via REST API → MCP wrapper

### Data schema

**AnnuityRecord:**
```json
{
  "app_number": "EP19234567.8",
  "patent_number": "EP3456789",
  "title": "Automated Contract Analysis System",
  "jurisdiction": "EP",
  "annuity_year": 7,
  "due_date": "2026-08-15",
  "grace_period_expiry": "2026-10-15",
  "annual_fee": 1020.00,
  "currency": "EUR",
  "status": "pending",
  "client": "HAQQ Inc"
}
```

**OARecord:**
```json
{
  "app_number": "US18/123456",
  "office_action_type": "Non-Final Rejection",
  "date_issued": "2026-04-01",
  "statutory_deadline": "2026-10-01",
  "extended_deadline": "2027-01-01",
  "extension_fees": 3200.00,
  "status": "Response in preparation",
  "attorney": "Jane Doe"
}
```

## Capabilities

### 1. Annuity calendar management

Pull all annuities due in the next 90/180/365 days. Present as a prioritised table:

| Jurisdiction | App number | Title | Due date | Days remaining | Fee | Action |
|---|---|---|---|---|---|---|
| EP | EP3456789 | Contract Analysis | 2026-05-20 | 6 | EUR 1,020 | PAY — CRITICAL |
| US | US10,234,567 | NLP Engine | 2026-06-30 | 47 | USD 1,800 | Pay — HIGH |
| UAE | UAE/2023/12345 | AI Risk Tool | 2026-07-15 | 62 | AED 3,000 | Scheduled |

Flag any annuity within 30 days as CRITICAL; within 90 days as HIGH.

### 2. Office action deadline management

Pull all pending office actions. For each, show:
- The rejection or objection type
- The statutory deadline (and extended deadline with extension fees)
- The assigned attorney
- Days remaining

Trigger an alert when any OA has fewer than 60 days to statutory deadline.

### 3. Filing strategy analysis

For a specific application or family, the agent can:
- Review the portfolio geography and recommend where continuation applications should be filed
- Identify gaps (competitor jurisdictions not covered)
- Flag applications that may be candidates for acceleration (PPH — Patent Prosecution Highway available between major patent offices)
- Identify abandoned applications whose reactivation might be possible within the applicable time window

### 4. Renewal recommendations

For each patent approaching a renewal decision (especially high-cost annuities), apply the renewal decision framework:

| Criterion | Weight | Questions |
|---|---|---|
| Commercial use | High | Is the patented technology in active use or licensing? |
| Blocking value | High | Does the patent block a competitor's freedom to operate? |
| Portfolio role | Medium | Is it part of a claim family that protects a core product? |
| Jurisdiction value | Medium | Is the jurisdiction a key market or manufacturing location? |
| Annual cost | Variable | Does the annuity fee justify the remaining life? |

Recommendation output:
- **Pay**: high commercial or blocking value; technology still deployed
- **Watch**: borderline value; review again at next annuity
- **Abandon**: no active use, no blocking value, low commercial territory
- **Sell/Licence**: no active use but third-party value exists — consider monetisation

### 5. Portfolio health report

Weekly or monthly portfolio summary:
- Total active patents by jurisdiction
- Annuities due next 30/90/180 days (count and cost)
- Office actions pending (count, oldest, most urgent)
- Applications in examination
- Renewals recommended for decision this quarter

## Critical safeguards

- **the agent is advisory only.** Docketing system is the authoritative record. If there is any discrepancy between the agent's output and the docketing system, the docketing system governs.
- **Verify every deadline before acting.** Missed IP deadlines cannot always be recovered. Before instructing payment or abandonment, verify the deadline in the docketing system directly.
- **Payment authorisation is human-controlled.** the agent can recommend and schedule, but annuity payment requires human authorisation. Never configure the bridge to make payments automatically.
- **Jurisdiction-specific grace periods.** Many jurisdictions have grace periods for missed annuities — but they are short and fee-bearing. Do not miss the primary deadline in reliance on a grace period.

## MENA IP office notes

| Office | Notable rule |
|---|---|
| UAE (MOEI) | Patents valid 20 years; annuity payments required; Arabic filing for national phase |
| KSA (SAIP — Saudi Authority for IP) | National phase PCT; Arabic required; Sharia compliance review for biotech |
| GCC Patent Office | Covers all 6 GCC states with a single filing; annuities due annually |
| Egypt (EGPO) | National PCT phase; French-influenced examination procedure |
| EPO | Inter-regional coverage; annuities to national offices after grant |

## Related skills

- [[pa-workflow-ip-claim-drafting-from-disclosure]]
- [[pa-workflow-ip-office-action-response-drafter]]
- [[pa-workflow-ip-opposition-procedure-epo]]
- [[output-timeline-builder]]
