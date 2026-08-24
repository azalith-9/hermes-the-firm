---
name: justice-message-actions
description: Use to determine which per-message action affordances to surface in the Louis chat UI after each assistant response. Applies context-sensitive rules to show or hide Copy, Regenerate, Save as snippet, Send to matter, Cite in document, Add to drafting board, Mark as wrong, and Share — adapting to output type, content sensitivity, and user role. Covers all jurisdictions; UI-routing skill with no practice area restriction.
license: MIT
metadata: " id: justice.message-actions category: justice jurisdictions: [__multi__] priority: P2 intent: [ui-routing, message-actions, affordances, per-message-ui] related: [justice-slash-commands, justice-result-page-routing, justice-product-demo-context-memory] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'justice'.
Registered as a flat plugin skill.
-->


# Justice — Message Actions

## Purpose

After every assistant message, the UI surfaces a contextual action bar. This skill defines the logic for which actions appear, when they are visible, and when they are suppressed. The goal is to make every useful output immediately actionable without cluttering every response with buttons the user doesn't need.

## Full action inventory

| Action | Description |
|---|---|
| **Copy** | Copy full message text to clipboard |
| **Edit** (user messages only) | Re-edit the user's prior message and re-run |
| **Regenerate** (assistant messages only) | Re-run the previous prompt to get an alternative response |
| **Save as snippet** | Save the message to the user's personal snippet library for reuse |
| **Send to matter** | Attach the message / output to the active matter file |
| **Cite in document** | Insert the output as a footnote or inline citation in the active document |
| **Add to drafting board** | Push the output to the drafting board as a block |
| **Mark as wrong** | Flag the response for quality feedback / retraining pipeline |
| **Share via secure link** | Generate a time-limited, access-controlled share link |

## Routing logic

Show or suppress actions based on the following signals:

### Always show
- **Copy**: always visible on any assistant message
- **Regenerate**: always visible on the most recent assistant message
- **Edit**: always visible on the most recent user message

### Show for long / substantive assistant messages
Threshold: message > ~150 words, or message contains a structured output (table, numbered list, clause, draft)

- **Save as snippet** — user may want to reuse the formulation
- **Send to matter** — likely a substantive work product worth filing

### Show when output type is detected

| Output type | Show action |
|---|---|
| Legal citation present (case name, article reference) | **Cite in document** |
| Draft contract / clause / document output | **Add to drafting board** + **Send to matter** |
| Research memo or analysis | **Send to matter** + **Save as snippet** |
| Translation output | **Add to drafting board** (bilingual comparison) |
| Numbered steps / procedure | **Save as snippet** |
| Error explanation / feedback | **Mark as wrong** (prominent) |

### Suppress for sensitivity

| Condition | Suppressed action(s) |
|---|---|
| PII detected in the message (name, ID number, phone, email) | **Share via secure link** — hide or require explicit confirmation |
| Privileged content flagged (attorney-client privilege marker) | **Share via secure link** — require explicit override |
| Message from a guest / unauthenticated user | **Send to matter**, **Add to drafting board** (require sign-in prompt instead) |
| Message in a read-only matter | **Send to matter** — replace with "View matter" |

### Mark as wrong — prominence rules

- If the response was short (< 50 words) and the user has been quiet for > 30 seconds: surface **Mark as wrong** more prominently (tooltip or label visible without hover)
- If the user sends a follow-up like "that's wrong", "incorrect", "not right": auto-prompt **Mark as wrong** with a one-click confirmation

## Implementation notes

- Actions render as icon buttons in a toolbar below the message bubble, with labels on hover
- On mobile: actions collapse into a "..." overflow menu; Copy and Regenerate remain pinned
- "Send to matter" requires an active matter to be set; if no matter is active, show "Add to matter" with a matter-selector prompt
- All user-facing action labels must be localized (Arabic / French / English)
- Action events are analytics-tracked for product usage insights (event: `message_action_triggered`, properties: action name, message type, matter context)

## Related skills

- [[justice-slash-commands]]
- [[justice-result-page-routing]]
- [[justice-product-demo-context-memory]]
