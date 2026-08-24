---
name: justice-slash-commands
description: Use to handle slash-command inputs typed by users in the Louis chat interface. Defines the full command catalog, autocomplete behavior, parameter handling, and routing logic for each command. Each slash command is a shortcut to a Louis skill or workflow — this skill bridges user input to skill invocation. Covers all jurisdictions; no practice area restriction.
license: MIT
metadata: " id: justice.slash-commands category: justice jurisdictions: [__multi__] priority: P2 intent: [commands, slash-commands, shortcut, chat-input, skill-invocation] related: [justice-message-actions, justice-result-page-routing, justice-intent-how-to] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'justice'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Justice — Slash Commands

## Purpose

Slash commands are keyboard-first shortcuts in the Louis chat input. When a user types `/`, the interface surfaces an autocomplete dropdown. This skill defines every supported command, its parameters, its routing target, and its behavior on invocation.

## Trigger

A slash command is triggered when the user:
1. Types `/` at the start of a chat message (or after a space, for inline commands)
2. The autocomplete dropdown appears, filtered as the user continues typing
3. User selects a command (keyboard or click) or types the full command and presses Enter

## Command catalog

### Drafting

| Command | Parameters | Behavior |
|---|---|---|
| `/draft [type]` | Type: nda, employment-contract, lease, spa, moa, loi, demand-letter, etc. | Invokes the appropriate drafting skill; prompts for required inputs; routes output to doc workspace |
| `/clause [name]` | Name: confidentiality, governing-law, limitation-of-liability, dispute-resolution, etc. | Pulls the named clause from the firm's clause library + the Louis standard library; inserts inline or into active document |

### Review

| Command | Parameters | Behavior |
|---|---|---|
| `/review [type]` | Type: general, risk-only, clause-by-clause, redline | Invokes the contract review skill on the most recently uploaded or pasted document; routes output to result page or inline |

### Research

| Command | Parameters | Behavior |
|---|---|---|
| `/research [topic]` | Topic: free text (e.g., "termination for cause UAE", "PDPL obligations KSA") | Invokes the legal research skill; prompts for jurisdiction if not specified; routes output to memo viewer |
| `/citation [case or statute]` | Reference: free text | Looks up and formats the citation in the active citation style; inserts into active document or returns inline |

### Translation

| Command | Parameters | Behavior |
|---|---|---|
| `/translate [lang]` | Lang: ar, fr, en, or auto | Translates the selected text or last assistant message to the target language; routes to bilingual viewer if > 200 words |

### Navigation / context

| Command | Parameters | Behavior |
|---|---|---|
| `/matter [id or name]` | Matter ID or partial name | Switches the active matter context; all subsequent saves and sends attach to this matter |
| `/jurisdiction [code]` | Code: LB, UAE, DIFC, KSA, EG, FR, UK, US, etc. | Sets the active jurisdiction filter for all subsequent skills in this session |

### Utility

| Command | Parameters | Behavior |
|---|---|---|
| `/skills` | None | Lists all available skills (filterable by category or jurisdiction); links to each skill's description |
| `/help` | Optional: [topic] | Opens the help panel; if a topic is provided, jumps to the relevant help article |
| `/export` | Optional: [format] (pdf, docx, md) | Exports the current conversation or active document to the specified format |

## Autocomplete behavior

- Dropdown appears immediately on `/` keystroke
- Commands are filtered in real-time as the user types (e.g., `/dr` shows `/draft`)
- Each item in the dropdown shows: command name, parameter hint, one-line description
- Keyboard navigation: arrow keys to move, Enter to select, Escape to dismiss
- Frequently used commands surface at the top based on user history
- Commands unavailable in the current context (e.g., `/matter` when no matters exist) are shown grayed out with a tooltip explaining why

## Parameter handling

- Parameters after the command name are parsed in order: `/draft nda` → type=nda
- For commands with required parameters not provided (e.g., `/review` with no document uploaded), surface a prompt: "What document would you like me to review? You can paste it now."
- Multiple parameters separated by space: `/draft employment-contract uae ar` → type=employment-contract, jurisdiction=UAE, language=ar
- Quoted parameters for multi-word values: `/research "termination for cause" uae`

## Error handling

| Error condition | User-facing message |
|---|---|
| Unknown command (e.g., `/foo`) | "I don't recognize `/foo`. Try `/skills` to see all available commands." |
| Command used out of context (e.g., `/review` with no document) | "[Brief explanation of what's needed] — [prompt to provide it]" |
| Command unavailable on current plan | "This command requires the [Plan] tier. [Upgrade link]" |

## Related skills

- [[justice-message-actions]]
- [[justice-result-page-routing]]
- [[justice-intent-how-to]]
