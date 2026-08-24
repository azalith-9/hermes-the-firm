---
name: unlock-power-user-shortcuts
description: Use when a user exhibits power-user behavior (rapid successive commands, repeated navigation, high session depth) and has not yet been shown keyboard shortcuts or command-palette guidance. This skill defines the shortcuts to surface, the trigger conditions for revealing them, and the copy to use, covering the command palette, slash commands, and matter navigation accelerators.
license: MIT
metadata: " id: unlock.power-user-shortcuts category: unlock jurisdictions: [__multi__] priority: P2 intent: [__customer-facing__, shortcuts, power-user, productivity] related: - unlock-first-week-progressive-tour - unlock-feature-discovery-by-persona - unlock-skill-of-the-day source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'unlock'.
Registered as a flat plugin skill.
-->


# Power User Shortcuts

## Purpose

Experienced users move faster with keyboard-first navigation. This skill governs which shortcuts to surface, when to surface them, and how to introduce them without interrupting a user who is already in flow.

## Core shortcuts

| Shortcut | Action |
|----------|--------|
| `Cmd-K` (Mac) / `Ctrl-K` (Win) | Open command palette — search all skills, matters, documents, and actions from anywhere |
| `Cmd-/` / `Ctrl-/` | Open slash-command menu inline in the chat input |
| `Cmd-Shift-N` / `Ctrl-Shift-N` | Create a new matter instantly |
| `Cmd-Shift-D` / `Ctrl-Shift-D` | Open the drafting board for the current matter |
| `Cmd-Shift-R` / `Ctrl-Shift-R` | Start a document review on the most recently uploaded file |
| `Cmd-[` / `Cmd-]` | Navigate back / forward through the session history |
| `Esc` | Close any modal or palette without saving |

## Slash commands (in-chat)

Slash commands are available directly in the chat input bar. Type `/` to trigger autocomplete.

| Command | Effect |
|---------|--------|
| `/draft [doc type]` | Start a drafting session for a named document type |
| `/review` | Attach a document and begin a clause-by-clause review |
| `/matter [name]` | Switch to or create a matter |
| `/ask` | Free-form legal Q&A mode |
| `/clause [keyword]` | Search the clause library inline |
| `/translate [lang]` | Translate the last output into the specified language |
| `/summary` | Generate a one-paragraph summary of the current document or thread |

## When to surface shortcuts

Surface the shortcut discovery card on the **first power-use trigger**, defined as any of the following:

- User has submitted more than 10 messages in a single session.
- User has navigated to three or more distinct matters in one session.
- User types a slash `/` in the chat input before being shown the slash-command menu.
- User completes a document review in under 3 minutes (high-velocity usage signal).

The card should appear as a non-blocking tooltip or sidebar nudge — not a modal that interrupts the current task.

## Card copy

```
You're moving fast. Here are shortcuts that will speed you up even more:

  Cmd-K      Open anything (command palette)
  Cmd-/      Slash commands inline
  Cmd-Shift-N  New matter instantly

[See all shortcuts]  [Dismiss]
```

Show no more than three shortcuts in the initial reveal. Link to a full shortcuts reference page.

## Dismissal and persistence

- After the user dismisses the card, do not re-show it for at least 14 days.
- After the user clicks "See all shortcuts", mark the shortcut discovery milestone complete and do not resurface.
- Store the shortcut reference in the help panel so the user can access it anytime via `?` or `Cmd-?`.

## Mobile considerations

On mobile (touch surface), keyboard shortcuts do not apply. Substitute a "quick actions" gesture guide:
- Long-press on a document card → quick action menu
- Swipe left on a matter → archive / pin options
- Pull down from chat header → command search

Surface this guide only to users on mobile who have used the app five or more times.

## Related skills

- [[unlock-first-week-progressive-tour]]
- [[unlock-feature-discovery-by-persona]]
- [[unlock-skill-of-the-day]]
- [[unlock-template-of-the-week]]
