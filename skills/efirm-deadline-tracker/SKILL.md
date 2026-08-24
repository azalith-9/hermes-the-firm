---
name: efirm-deadline-tracker
description: Use when a lawyer or legal team needs to surface, organize, and monitor all deadlines on an active matter — including statutory limitation periods, court-ordered deadlines, internal milestones, and client-driven dates. For each deadline the skill assigns an owner, defines pre-deadline tasks, documents consequences of a miss, and triggers a graduated escalation chain (T-14/7/3/1). Pairs with the date-tool deadline calculator for jurisdiction-aware holiday exclusion.
license: MIT
metadata: " id: efirm.deadline-tracker category: efirm jurisdictions: [__multi__] priority: P1 intent: [deadline, calendar, limitation, court-dates, escalation, malpractice] related: - efirm-matter-creation-flow - efirm-conflict-check - efirm-team-handoff-summary - efirm-client-update-email-draft source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'efirm'.
Registered as a flat plugin skill.
-->


# Deadline Tracker

## When to use this

Use this skill when:
- A new matter is opened — all known deadlines must be entered at intake.
- A new court order, regulatory response, or contract milestone is issued — add immediately.
- A team member is departing or changing role — full deadline handoff required before departure.
- A deadline is approaching and status needs to be confirmed.
- The managing partner is reviewing matter health across the firm's active caseload.

Missed deadlines are a primary cause of legal malpractice claims in every jurisdiction. The tracker is not optional — it is a risk-management system.

## Deadline categories

### Category 1: Statutory deadlines

Set by law; failure is typically fatal and irreversible.

Examples:
- **Limitation periods**: UAE Civil Code (Art. 473 — general 15 years; specific periods vary); Lebanese Code of Obligations and Contracts; DIFC Contract Law; KSA Commercial Court rules; US state statutes of limitations.
- **Appeal windows**: typically 30–60 days from judgment (varies sharply by jurisdiction and court level).
- **Regulatory response deadlines**: government authority response periods; failure may result in default approval or adverse finding.
- **Arbitration notice deadlines**: notice of dispute must be sent within contractual window.

**Calculation note**: Statutory deadlines must account for jurisdiction holidays. Pair with [[tool-date-tool-deadline-calculator]] to exclude weekends and public holidays (GCC Friday/Saturday; LB/FR/EU Sunday + legal holidays; US federal holidays; DIFC/ADGM per DIFC/ADGM court rules).

### Category 2: Court-ordered deadlines

Set by a court, arbitration panel, or regulatory authority.

- Failure to comply with court orders can result in: sanctions, adverse inference, default judgment, contempt.
- These deadlines are generally non-negotiable without a formal extension application.
- **Immediately entered** into the tracker on receipt of any court order.

### Category 3: Internal milestones

Set by the firm; failure affects quality, not (directly) the legal outcome.

Examples:
- First draft of transaction document to partner for review.
- Internal sign-off on litigation strategy before court filing.
- Client approval deadline for a document.
- Billing cutoff for the matter.

These feed into the overall matter timeline and client update schedule.

### Category 4: Client-driven deadlines

Defined by the client or the engagement scope.

Examples:
- Target transaction closing date.
- Board meeting date by which advice must be ready.
- Regulatory submission date the client has committed to.

Treat these with urgency — client-driven deadlines affect commercial outcomes and the client relationship.

## Per-deadline record

For each deadline, capture:

| Field | Description |
|---|---|
| Deadline ID | Unique identifier |
| Matter ID | Links to the matter |
| Deadline type | Statutory / Court-ordered / Internal / Client-driven |
| Description | Plain-language description of what is due |
| Date + Time | Exact date; time if relevant; timezone explicit |
| Jurisdiction | Governs holiday calculation |
| Owner (primary) | Named attorney responsible |
| Owner (backup) | Secondary responsible if primary unavailable |
| Pre-deadline tasks | Ordered list of steps required before the deadline |
| Consequences of miss | Factual description of what happens if deadline is missed |
| Status | Open / In progress / Complete / Overdue |
| Notes | Any extensions, waivers, or relevant history |

## Escalation chain

| Trigger | Action |
|---|---|
| T-14 days | Assign owner; brief the team; ensure pre-deadline tasks are allocated |
| T-7 days | Status check — owner confirms progress; any blockers escalated |
| T-3 days | Red-alert if completion is not on track; managing partner notified |
| T-1 day | Partner escalation if not confirmed complete; consider extension application if available |
| Day of deadline | Confirm completion and record timestamp; document filing proof |
| Post-deadline | If missed: assess remediation options; notify partner; assess disclosure obligations |

The T-3 and T-1 escalations must generate **automatic notifications** — not rely on manual review.

## Consequences of a miss — by deadline type

| Type | Typical consequence |
|---|---|
| Limitation period | Claim permanently barred; malpractice liability to client |
| Appeal window | Right of appeal lost; judgment becomes final |
| Court order | Sanctions, adverse inference, contempt of court, default judgment |
| Regulatory response | Default approval (sometimes favorable) or adverse finding |
| Arbitration notice | Arbitration right lost |
| Internal milestone | Matter quality risk; client dissatisfaction |
| Client-driven | Commercial harm to client; relationship damage |

## Holiday calendars — jurisdiction reference

| Jurisdiction | Weekend | Key holidays affecting deadlines |
|---|---|---|
| UAE (federal) | Fri–Sat | National Day, Eid al-Fitr, Eid al-Adha, Islamic New Year, Prophet's Birthday (dates vary) |
| KSA | Fri–Sat | National Day, Founding Day, Eid al-Fitr, Eid al-Adha |
| DIFC / ADGM | Fri–Sat (with adjustments) | Follow UAE federal holidays + DIFC/ADGM court-specific closures |
| Lebanon | Sun | National holidays including Independence Day; courts closed in August (by custom) |
| France | Sun | Legal public holidays per Labour Code |
| UK | Sun | Bank holidays per Banking and Financial Dealings Act |
| US | Sun | Federal holidays; state holidays vary by state |

Always verify the specific court or authority's holiday schedule — court closures do not always match general public holidays.

## Output format

### Active deadlines list (matter view)

```
DEADLINE TRACKER — [Matter] — [Date]

ID    | Description                  | Due Date  | Type       | Owner   | Status    | Alert
──────────────────────────────────────────────────────────────────────────────────────────
DL001 | File reply brief             | 2025-06-15 | Court     | [Name]  | In progress | T-7
DL002 | Deliver draft SPA to partner | 2025-06-10 | Internal  | [Name]  | Open      | T-14
DL003 | Regulatory submission        | 2025-07-01 | Client    | [Name]  | Open      | —
```

### Escalation notification (auto-generated)

```
DEADLINE ALERT — T-[N] — [Matter ID]

Deadline:       [Description]
Due:            [Date]
Owner:          [Name]
Backup:         [Name]
Status:         [Confirmed on track / At risk / Not started]
Consequence:    [If missed: ...]
Action needed:  [Specific action required from recipient]
```

## Integration points

- Links to [[efirm-client-update-email-draft]]: upcoming deadlines and decisions populate the "Next Steps" section automatically.
- Links to [[efirm-team-handoff-summary]]: all open deadlines are listed on handoff.
- Links to [[efirm-matter-creation-flow]]: deadlines entered at matter creation are immediately tracked.

## Related skills

- [[efirm-matter-creation-flow]]
- [[efirm-client-update-email-draft]]
- [[efirm-team-handoff-summary]]
- [[efirm-conflict-check]]
- [[tool-date-tool-deadline-calculator]]
