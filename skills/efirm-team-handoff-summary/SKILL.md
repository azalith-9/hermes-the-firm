---
name: efirm-team-handoff-summary
description: Use when responsibility for a matter (or part of a matter) is transferring from one lawyer or team to another — whether due to departure, leave, role change, or phase transition. The skill generates a structured handoff summary covering matter status, open issues, upcoming deadlines, client relationship notes, billing status, and access/permissions checklist. Part of the eFirm firm-management product suite.
license: MIT
metadata: " id: efirm.team-handoff-summary category: efirm jurisdictions: [__multi__] priority: P2 intent: [handoff, transition, matter-transfer, continuity, risk-management] related: - efirm-matter-creation-flow - efirm-deadline-tracker - efirm-client-update-email-draft - efirm-document-versioning-rule - efirm-partner-review-routing source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'efirm'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Team Handoff Summary

## When to use this

Use this skill when:
- An associate or partner is leaving the firm or going on extended leave and their matters must be transferred.
- A matter transitions from one phase to another with a different team lead (e.g., transactional team hands off to litigation team after a deal dispute arises).
- A client relationship is being transferred to a new relationship partner.
- Co-counsel is stepping in to cover a hearing or filing at short notice.
- A new associate is joining the matter team and needs to be brought up to speed efficiently.

Poor handoffs cause dropped deadlines, duplicated effort, inconsistent client communication, and billing errors. A structured handoff summary eliminates these failure modes.

## Required inputs

| Input | Source |
|---|---|
| Matter ID and title | eFirm matter record |
| Outgoing lawyer name and role | eFirm user record |
| Incoming lawyer name and role | As provided |
| Handoff effective date | As provided |
| Access to all matter documents and time records | DMS + billing system |

## Handoff summary structure

### Section 1: Matter overview

```
MATTER HANDOFF SUMMARY

Matter:          [ID] — [Title]
Client:          [Client name]
Matter type:     [Corporate / Dispute / Employment / etc.]
Status:          [Active / Pending / Closing]
Phase:           [e.g., Due diligence / Negotiations / Execution / Post-closing]
Outgoing:        [Name], [Role] — effective [Date]
Incoming:        [Name], [Role]
Prepared by:     [Outgoing lawyer]
Date:            [Date]
Reviewed by:     [Responsible partner]
```

### Section 2: Matter status narrative

A 3–5 paragraph plain-language briefing:
1. **Background**: what is this matter about? Who are the parties? What does the client want?
2. **Progress to date**: what has been done? What milestones have been reached?
3. **Current status**: where are we right now? What is the most recent development?
4. **Key open issues**: what are the 3–5 most important unresolved questions or tasks?
5. **Client relationship notes**: communication preferences; sensitivities; recent interactions; tone of relationship.

### Section 3: Open deadlines

All open deadlines from [[efirm-deadline-tracker]], confirmed current:

```
ID    | Description              | Due Date  | Type       | Status      | Action needed
──────────────────────────────────────────────────────────────────────────────────────
DL001 | [Description]            | [Date]    | [Type]     | [Status]    | [Action]
```

For each deadline within 14 days of handoff: explicitly confirm status and assign to incoming lawyer.

### Section 4: Open tasks and instructions

Granular task list for the incoming lawyer:

```
OPEN TASKS

Priority | Task description               | Context / background        | Deadline
─────────────────────────────────────────────────────────────────────────────────────
HIGH     | [Task 1]                       | [Why this is urgent]        | [Date]
HIGH     | [Task 2]                       | ...                         | [Date]
MEDIUM   | [Task 3]                       | ...                         | [Date]
LOW      | [Task 4]                       | ...                         | —
```

### Section 5: Client contacts

```
CLIENT CONTACTS

Name:         [Contact name]
Role:         [Title at client]
Email / Tel:  [Details]
Notes:        [Preferred communication; language; availability; sensitivities]

[Repeat for each key contact]
```

Include any important context: does the client prefer WhatsApp over email (common in MENA)? Is there a main contact who acts as gatekeeper? Is there political sensitivity between contacts?

### Section 6: Counterparty and third-party contacts

```
OTHER KEY CONTACTS

Party:        [Name / firm]
Role:         [Opposing counsel / Counterparty CFO / Expert witness / Regulator]
Contact:      [Name, email, phone]
Relationship: [Cooperative / Neutral / Adversarial]
Notes:        [Any important context]
```

### Section 7: Document map

```
DOCUMENT MAP

Location:       [DMS folder path]
Key documents:
  - [Doc 1 — e.g., "Current draft SPA v3.1 — last updated [date]"]
  - [Doc 2 — e.g., "Due diligence report — final"]
  - [Doc 3 — e.g., "Client approval email re: indemnity position"]
  
In progress:
  - [Doc being drafted — current status — who is drafting]

Pending from counterparty:
  - [Document we are waiting for — since when]
```

### Section 8: Billing status

```
BILLING STATUS

Fees billed to date:         $X
Fees outstanding (invoiced): $Y  (aging: [current/30+/60+ days])
Unbilled WIP:                $Z
Budget remaining:            $A  (of $B agreed budget)
Next billing cycle:          [Date]
Billing notes:               [Any billing sensitivities; disputes; client feedback]
```

### Section 9: Access and permissions checklist

Before handoff is complete, confirm:

- [ ] Incoming lawyer added to matter team in eFirm
- [ ] DMS folder access granted to incoming lawyer
- [ ] Billing system timekeeper access configured
- [ ] Client portal access transferred (if applicable)
- [ ] Email thread / correspondence access confirmed
- [ ] Outgoing lawyer access removed (if full transfer)
- [ ] Responsible partner record updated in eFirm

### Section 10: Handoff completion confirmation

Outgoing and incoming lawyers must both sign off:

```
HANDOFF CONFIRMATION

Outgoing lawyer: [Name]     Date: [Date]     Signature: ____________
Incoming lawyer: [Name]     Date: [Date]     Signature: ____________
Supervising partner: [Name] Date: [Date]     Signature: ____________
```

This is the record that the handoff was properly executed — it is filed in the matter record.

## Common handoff failures

- **No deadline confirmation**: the most dangerous failure. Before handoff, every deadline must be confirmed current and assigned.
- **No client notification**: clients should be informed when their relationship partner or primary contact changes. The outgoing lawyer or responsible partner should send a brief introductory communication.
- **Access not transferred**: incoming lawyer unable to access documents; outgoing lawyer retaining access to closed or transferred matters creates a data governance issue.
- **Verbal-only handoff**: undocumented handoffs create disputes about who was responsible for what. Always document.
- **No billing note**: incoming lawyer inherits billing disputes without context.

## Related skills

- [[efirm-matter-creation-flow]]
- [[efirm-deadline-tracker]]
- [[efirm-client-update-email-draft]]
- [[efirm-document-versioning-rule]]
- [[efirm-partner-review-routing]]
