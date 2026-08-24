---
name: efirm-client-update-email-draft
description: Use when a lawyer needs to draft a periodic status update email to a client on an active matter. The skill produces a structured, tone-calibrated draft covering status, next steps, decisions required, costs, and risks — adapting to the author's seniority level, matter type (litigation vs. transactional), client communication preference, and regional formality norms including MENA formal openings and US direct style.
license: MIT
metadata: " id: efirm.client-update-email-draft category: efirm jurisdictions: [__multi__] priority: P1 intent: [email, client-communication, status-update, matter-update] related: - efirm-matter-creation-flow - efirm-matter-summary-for-billing - efirm-deadline-tracker - efirm-team-handoff-summary source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'efirm'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Client Update Email Draft

## When to use this

Use this skill to produce a draft client update email when:
- A matter milestone has been reached (filing completed, hearing concluded, term sheet signed).
- A scheduled periodic update is due (weekly, bi-weekly, or monthly per engagement terms).
- An unexpected development requires prompt communication (court ruling, regulatory response, counterparty position change).
- The billing cycle is approaching and the client needs a costs-to-date summary before the invoice arrives.
- A decision needs to be escalated to the client and a clear written record is required.

## Required inputs

| Input | Why it matters |
|---|---|
| Matter ID / short title | Identifies the engagement |
| Author's role (Partner / Senior Associate / Associate / Junior) | Determines tone and level of detail |
| Matter type (Litigation / Transaction / Regulatory / Advisory) | Drives content structure and guarded vs. collaborative tone |
| Key events since last update | Core content of the status section |
| Next steps + timeline | Client needs to know what is happening and when |
| Decisions required from client | Explicit call-to-action prevents matter delays |
| Costs to date (billed + unbilled) | Client transparency; invoice preparation |
| Projected costs to completion | Budget management |

## Optional inputs

| Input | Effect on draft |
|---|---|
| Client communication preference (terse / standard / detailed) | Adjusts email length and level of explanation |
| Regional/cultural style (MENA formal / US direct / UK formal) | Adjusts salutation, closing, and formality register |
| Privileged status of content | Adds "Legally Privileged and Confidential" header |
| Risks / opportunities to flag | Adds a dedicated risks section |
| Prior update date | Creates continuity with "since our last update of [date]..." |
| Suggested send time | Output includes recommended send time |

## Email structure

Every client update email follows this structure. Sections may be abbreviated for terse preference but none are skipped entirely.

### 1. Subject line

```
[Matter Reference] — Status Update — [Month/Date]
```
For sensitive matters: omit identifying details from subject line; use coded reference only.

### 2. Opening (tone-calibrated)

**MENA formal** (Arabic-cultural register):
> We hope this message finds you well. We write to provide you with an update on the above-referenced matter.

**UK formal**:
> I write to provide you with a progress update on [matter description].

**US direct**:
> Quick update on [matter] — here's where things stand.

**Legally privileged header** (where applicable):
> LEGALLY PRIVILEGED AND CONFIDENTIAL — This communication is protected by legal professional privilege. Do not forward without authorisation.

### 3. Status summary

Answers: what has happened since the last update?

- Keep to 3–5 bullet points or a short paragraph.
- Litigation: neutral, factual, guarded — avoid characterizing the strength of the position (until instructed).
- Transaction: collaborative tone; "we have made good progress on X; the parties have agreed Y."
- Regulatory: formal; include any correspondence dates with the authority.

### 4. Next steps and timeline

```
NEXT STEPS

[Step 1] — [Description] — Target: [Date] — Owner: [Firm / Client / Counterparty]
[Step 2] — [Description] — Target: [Date] — Owner: [...]
```

Keep action items numbered and explicitly owned. Ambiguity about who acts next is a common source of matter delay.

### 5. Decisions required from client

Make this section unmissable. If no decisions are needed, write "No decisions required at this stage."

```
ACTION REQUIRED FROM YOU

1. [Decision / Instruction needed] — Deadline: [Date]
   [Brief context paragraph: why this decision is needed now and what the options are]

2. [...]
```

### 6. Costs to date and projection

```
COSTS SUMMARY

Fees billed to date:        $X
Fees unbilled (WIP):        $Y  (will be invoiced [billing period])
Total incurred to date:     $Z
Projected fees to [milestone]: $A–$B (estimate; subject to scope change)
Budget remaining:           $C
```

If a fee cap is being approached, flag it explicitly: "We are now at approximately 80% of the agreed budget of $[X]. Please let us know if you wish to discuss the scope before we reach the cap."

### 7. Risks and opportunities (if applicable)

Use only when there is something material to flag. Do not manufacture risk commentary.

- **Litigation**: "If the court rules against our motion on [date], the consequences would be [X]. We are preparing a contingency strategy."
- **Transaction**: "The counterparty has introduced a new condition on [issue]. We recommend [approach] to resolve this before signing."

### 8. Closing

**MENA formal**:
> Please do not hesitate to contact us should you have any questions. We remain at your disposal.

**UK / US**:
> Please feel free to call me directly if you would like to discuss any of the above.

### 9. Send-time recommendation

The skill outputs a suggested send time:
- Avoid Friday afternoon (MENA), Friday/Saturday (GCC weekend), Monday morning (inbox crowded).
- Prefer: Tuesday–Thursday, 9–11am local client time.
- For urgent updates: no delay; flag "Urgent" in subject.

## Tone calibration table

| Author level | Tone | Length | Technical depth |
|---|---|---|---|
| Senior partner | Strategic; decisive; confident | Short (5–8 paragraphs) | Summary only; no granular detail |
| Mid-level (3–7 PQE) | Detailed; collaborative | Medium (6–10 paragraphs) | Step-level detail; explain options |
| Junior (1–3 PQE) | Informative; deferential; clearly supervised | Long (if complex); supervised | Procedural; confirm everything |

Junior lawyers should always have updates reviewed by a supervising partner before sending on sensitive matters.

## What to avoid

- **Overconfidence in litigation outcomes**: never write "we expect to win" or "this is a strong case" — these create liability if the outcome differs.
- **Unilateral cost increases**: never bury a significant budget overage in a status email. It requires a dedicated conversation.
- **Vague timelines**: "shortly" and "soon" are not dates. Use specific dates or date ranges.
- **Missing the call to action**: if the client needs to decide something, put it in a clearly marked section — not buried in a paragraph.
- **Legal jargon without explanation**: write for the client's level of legal sophistication. Most clients want plain language.

## Related skills

- [[efirm-matter-creation-flow]]
- [[efirm-matter-summary-for-billing]]
- [[efirm-deadline-tracker]]
- [[efirm-team-handoff-summary]]
- [[efirm-finance-wip-aging-report]]
