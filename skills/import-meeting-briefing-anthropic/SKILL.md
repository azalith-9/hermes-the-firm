---
name: import-meeting-briefing-anthropic
description: Use when migrating a meeting-briefing skill originally built for the Anthropic the agent API into the mini-hermes-the-firm format. The adapter maps legacy meeting-preparation logic — agenda analysis, participant profiling, key-issue summaries, and action-item tracking — into the standard skill model for use in legal and deal-team contexts.
license: MIT
metadata: " id: import.meeting-briefing-anthropic category: import jurisdictions: [__multi__] priority: P3 intent: [__import__, meeting-briefing, legal-ops, migration, anthropic] related: [import-contract-review-anthropic, import-nda-triage-anthropic, import-vendor-due-diligence-patrick-munro, ops-meeting-prep] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'import'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Import: Meeting Briefing (Anthropic)

## What it does

This import adapter migrates a **meeting-briefing skill** originally authored for Anthropic's the agent API into the `mini-hermes-the-firm` standard format. Legal and deal teams routinely prepare structured briefing documents before client meetings, negotiation sessions, regulatory hearings, and board presentations. A meeting-briefing skill automates the preparation: given inputs about the meeting, it generates a concise, well-structured brief that tells every participant what they need to know before walking into the room.

The Anthropic-native version may have used a system prompt for meeting prep, a calendar-integration hook, or a document-analysis pipeline feeding into a briefing template. This adapter normalises all of those shapes.

## Import config

| Field | Source mapping | Default if absent |
|---|---|---|
| `meeting_type` | Legacy `type` | `negotiation_session` |
| `participant_profiling` | Legacy `profiles` boolean | `true` |
| `agenda_parsing` | Legacy `parse_agenda` boolean | `true` |
| `document_inputs` | Legacy `docs` array | None (optional) |
| `key_issues_limit` | Legacy `max_issues` | `5` |
| `action_tracking` | Legacy `action_items` boolean | `true` |
| `output_length` | Legacy `length` | `concise` (max 2 pages equivalent) |
| `language` | Legacy `lang` | `en` |

## Dry-run preview

```
IMPORT PREVIEW — meeting-briefing-anthropic
Source shape     : Anthropic meeting-briefing system prompt
Meeting type     : negotiation_session (default)
Participant profiles: enabled
Agenda parsing   : enabled
Key issues       : max 5
Action tracking  : enabled
Output length    : concise (2-page equivalent)
```

## Briefing structure (post-import)

### 1. Meeting overview
- Purpose and expected outcome
- Date, time, forum (virtual / in-person / hybrid)
- Governing confidentiality constraints (e.g. legal privilege, NDA in place)

### 2. Participants
| Name | Role | Organisation | Known position / interests | Watch-outs |
|---|---|---|---|---|
| [name] | [role] | [org] | [known stance] | [sensitivities] |

### 3. Agenda items
For each item:
- Background (1–2 sentences)
- Our position / objective
- Likely counterparty position
- Decision to be made / outcome sought

### 4. Key documents
- List any contracts, term sheets, or regulatory materials being discussed; with one-line status note.

### 5. Key issues (max 5)
The most important substantive issues, ranked by priority. Each issue: background → our position → counterparty position → risk if unresolved.

### 6. Action items (pre-meeting)
What must be done before the meeting: approvals needed, information to obtain, positions to confirm.

### 7. Post-meeting action-item template
Pre-formatted table for capturing decisions and owners during or after the meeting.

## Legal-context specifics

- **Privilege**: if the meeting involves legal advice, mark the brief "Privileged and Confidential — Attorney-Client Communication" (common law) or equivalent (civil law: secret professionnel).
- **Regulatory hearings**: for meetings with regulators (DFSA, CBUAE, ACPR, FCA), adapt the participant-profiling section to include the regulator's known supervisory priorities and any outstanding examination findings.
- **Negotiation sessions**: link to the relevant `import-legal-simulation-patrick-munro` or `import-mediation-dispute-analysis-jinzhe-tan` output if a dispute is being negotiated.
- **Arabic language**: for meetings with UAE government counterparts or MENA clients, add a brief Arabic-language summary block.

## Failure modes

| Error | Likely cause | Resolution |
|---|---|---|
| `agenda_empty` | No agenda provided by user | Generate placeholder agenda from meeting type; flag as draft |
| `participants_unknown` | No participant list | Prompt user; generate blank participant table |
| `output_too_long` | Legacy prompt produced verbose output | Enforce `output_length: concise` override |
| `privilege_not_marked` | Legal briefing lacks privilege header | Auto-prepend privilege header if meeting involves legal advice |

## Related skills

- [[import-contract-review-anthropic]]
- [[import-nda-triage-anthropic]]
- [[import-vendor-due-diligence-patrick-munro]]
- [[import-legal-simulation-patrick-munro]]
- [[ops-meeting-prep]]
