---
name: pa-workflow-inhouse-friday-newsletter-status-synthesis
description: Use when an in-house legal team needs to synthesise the week's legal matters into a concise Friday status newsletter for the team, the GC, or the broader business. Reduces 2+ hours of weekly synthesis to a 5-minute AI-assisted draft. Triggers on requests for a weekly legal update, matter status report, or end-of-week team communication.
license: MIT
metadata: " id: pa-workflow.inhouse.friday-newsletter-status-synthesis category: pa-workflow intent: ['__workflow__', 'newsletter', 'status synthesis', 'weekly', 'in-house'] related: - pa-workflow-inhouse-board-deck-legal-section - pa-workflow-inhouse-cross-functional-translation - output-partner-memo-style priority: P1 source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'pa-workflow'.
Namespaced as louis-<category>-<skill> on registration.
-->


# In-House — Friday Newsletter (Status Synthesis)

The Friday legal newsletter is a Mark Pike pattern — a weekly communication from the GC or legal team that synthesises all active matters, flags emerging risks, and keeps the business informed without requiring everyone to attend a meeting. It is also a discipline tool: writing the newsletter forces the legal team to review every matter weekly, preventing things from falling through the cracks. This skill reduces the 2-hour manual synthesis to a 5-minute AI-assisted draft.

## Purpose

Produce a concise, scannable Friday newsletter that:
1. Identifies the top legal risks of the week (what the business needs to know)
2. Updates the status of all material active matters
3. Highlights the week's notable commercial and legal developments
4. Previews the upcoming week's key events and deadlines

## Inputs

| Input | Why it matters |
|---|---|
| Matter tracker / log | Current status of all active matters |
| Emails / notes from the week | Source material for highlights and risk flags |
| Deadlines calendar | Next week's critical dates |
| Commercial team updates | Deal activity, contract signings |
| Regulatory alerts (if tracked) | Regulatory developments from the week |
| Last week's newsletter | For continuity and "what changed" framing |

## Newsletter structure

### Section 1 — Top Legal Risks This Week

2–4 bullets. Each bullet: the risk in one sentence + what's being done about it.

> - **DFSA regulatory inquiry (Active)**: Information requests responded to this week; external counsel preparing supplemental response. Next: hearing scheduled for [date].
> - **Acme contract dispute (Developing)**: Counterparty has not responded to our settlement offer. Deadline for response: 21 May. If no response, we recommend instructing for arbitration.
> - **New data localisation requirement (Monitoring)**: UAE data protection authority published draft guidance. Assessment underway; initial read is that we need infrastructure changes by Q1 2027.

### Section 2 — Matter Status Updates

A brief table or bullet list by matter category:

**Litigation / Disputes:**
- Acme v. Company — [Court]: Hearing pending (see above)
- Employee claim [redacted name] — UAE Labour Court: Conciliation session scheduled 25 May
- IP dispute — resolved by settlement (AED 85K); settlement deed signed 13 May

**Regulatory:**
- DFSA inquiry (see above)
- Annual regulatory filing — UAE MoCI: submitted 10 May. Confirmation awaited.

**Transactions / Commercial:**
- GlobalCo MSA — reviewed and signed 12 May (AED 850K, 3-year term)
- NewCo JV — closing checklist with external counsel; estimated closing 30 June
- 14 NDAs processed this week — 12 auto-signed, 2 flagged for review (pending)

### Section 3 — Commercial Team Highlights

Brief summary of deal activity, relevant legal input provided, and any commercial-to-legal escalations:

> - Sales supported on 3 contract negotiations this week; material issues: IP ownership in dev contract (escalated to GC, resolved); indemnity cap in MSA (agreed at 12 months' fees).
> - Engineering requested DPA review for new AWS region; reviewed and approved.

### Section 4 — Heads-Up for Next Week

Key dates and anticipated legal events for the coming week:

> - 20 May: Response deadline — Acme settlement offer. If no response, decision required by GC on arbitration referral.
> - 22 May: Board meeting — legal section prepared (see attached draft).
> - 25 May: Labour court — employee claim conciliation session (external counsel attending).
> - 31 May: Quarterly regulatory filing deadline — Kenya subsidiary (currently tracking on time).

## Format and length

| Element | Target length |
|---|---|
| Full newsletter | 1 page (400–600 words) |
| Top risks section | 2–4 bullets |
| Matter status | One line per matter, no prose |
| Commercial highlights | 3–5 bullets |
| Next week preview | 3–5 dated items |

The newsletter must be scannable in 3 minutes. If a matter requires more than one line, it should be in a separate briefing note, not in the newsletter.

## Tone

- Direct and informative — not a legal memo, not casual chat
- First person plural ("we") for team communications; third person ("the legal team") for board-facing versions
- No jargon — the newsletter goes to the whole business, not just lawyers
- Action-oriented: every section ends with what is being done or what decision is needed

## Distribution variants

| Version | Audience | Adjustments |
|---|---|---|
| Internal legal team | GC + lawyers | Full detail; include privileged items |
| Business leadership | CEO, CFO, COO, function heads | Redact privileged and sensitive litigation detail; frame around business impact |
| Board pack appendix | Board directors | Abbreviate to top 3 risks + material matters only; see [[pa-workflow-inhouse-board-deck-legal-section]] |

## Automation with the agent

The synthesis workflow:
1. Dump matter tracker, email highlights, and deadline calendar into the agent
2. Run this skill: the agent produces the draft newsletter in the correct structure
3. GC reviews and adjusts (5 minutes)
4. Send

Without AI: 2+ hours of manual synthesis across multiple sources. With AI: 5 minutes of input preparation + 5 minutes of review.

## Related skills

- [[pa-workflow-inhouse-board-deck-legal-section]]
- [[pa-workflow-inhouse-cross-functional-translation]]
- [[output-partner-memo-style]]
- [[output-timeline-builder]]
