---
name: connector-apple-notes
description: Use when a user wants to pull content from Apple Notes into a legal-AI workflow — for example, retrieving a meeting note to draft follow-up correspondence, attaching a note to a matter, or searching notes for a client name or clause fragment. Supports read-only access via iCloud Documents or the macOS native helper; no write-back to Apple Notes. Relevant across all jurisdictions for any practice area where lawyers take notes in Apple Notes.
license: MIT
metadata: " id: connector.apple-notes category: connector jurisdictions: [__multi__] priority: P2 intent: [__connector__] related: [connector-google-drive, connector-notion, connector-calendar, connector-gmail] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'connector'.
Registered as a flat plugin skill.
-->


# Connector — Apple Notes

## What it does

The Apple Notes connector surfaces note content stored in iCloud from the user's Apple Notes app and makes it available as context within legal-AI workflows. It is **read-only**: the connector can retrieve and search notes but does not create, edit, or delete notes in the Apple Notes application.

Typical uses in a legal context:
- Pulling a handwritten (transcribed) client intake note to auto-populate a matter summary.
- Searching for a prior meeting note by client name or keyword before drafting correspondence.
- Attaching note content to a matter workspace as background context.
- Reviewing a note taken during a site visit or court attendance to draft a factual narrative.

## Setup / auth

Apple Notes does not expose a standard public OAuth API. Access is achieved via one of two mechanisms:

### Option A — macOS native helper (preferred)

On a macOS device where the user is signed in with their Apple ID:
- A local helper process reads from the Apple Notes SQLite store (located at `~/Library/Group Containers/group.com.apple.notes/NoteStore.sqlite`).
- No remote API call; no Apple ID credentials transmitted to external servers.
- Requires explicit user permission via macOS Privacy settings (Full Disk Access or Contacts access depending on macOS version).
- Works entirely offline.

This is the preferred method for law firms running on-premise or privacy-sensitive deployments.

### Option B — iCloud Documents API (limited)

Apple exposes some iCloud Drive content via the CloudKit/iCloud Documents API, but **Notes stored natively in Apple Notes are not accessible via CloudKit by third parties**. This path is only viable if the user has exported notes to iCloud Drive as text or PDF files.

Practically: if the user's workflow involves exporting notes to a shared iCloud folder, the connector can read those files via iCloud Drive access — but this is a workaround, not a native integration.

### Auth summary

| Method | Auth required | Online? | Write access? |
|---|---|---|---|
| macOS native helper | macOS Privacy grant | No | No |
| iCloud Documents | Apple ID OAuth (limited) | Yes | No (read-only) |

## Capabilities

| Capability | Status |
|---|---|
| List all notes (titles + snippets) | Supported (native helper) |
| Full-text search across notes | Supported |
| Retrieve full note content by title or ID | Supported |
| Retrieve notes from a specific folder/notebook | Supported |
| Read note attachments (images, PDFs) | Partial — text extraction only |
| Create or edit notes | Not supported |
| Delete notes | Not supported |

## Usage patterns

### Pattern 1 — Retrieve note by client name before drafting

```
User: "Draft a follow-up email to Al-Hassan re our 14 May call"
→ Connector searches Apple Notes for "Al-Hassan" + date proximity
→ Returns matching note as context
→ Draft email references the note's key points
```

### Pattern 2 — Attach notes to a new matter

When creating a new matter file, search Apple Notes for the client name and offer to import any matching notes as matter background. The user confirms which notes to attach before import.

### Pattern 3 — Post-hearing notes to narrative

```
User: "Summarize my notes from yesterday's DIFC hearing"
→ Connector retrieves notes from yesterday (date-filtered)
→ Returns content for summarization
→ Output: structured hearing summary for matter file
```

## Permissions & safety

- **Read-only at all times.** No write operations.
- **On-device processing preferred.** When using the macOS native helper, note content should not leave the device unless the user explicitly approves attaching content to an external system.
- **PII handling.** Apple Notes may contain highly sensitive client information — names, financial details, privileged communications. Treat every note as privileged until the user confirms otherwise.
- **No background scanning.** The connector must not proactively index all notes without explicit user initiation. Search is on-demand only.
- **Audit log.** Every note retrieval operation is logged with a timestamp and the user ID who triggered it.

## Failure modes

| Failure | Cause | Resolution |
|---|---|---|
| "No notes found" | Privacy permission not granted | Prompt user to grant Full Disk Access in System Settings → Privacy |
| Garbled content | Note contains handwriting/drawing (non-text) | Inform user; offer to transcribe image attachments if multimodal capability is available |
| Old/stale content | iCloud sync lag | Warn user that note content reflects the last successful iCloud sync; advise opening Notes.app to force sync |
| Notes from shared notebooks | Shared notebook content included | Surface shared-by attribution so the user knows the note's origin |

## Related skills

- [[connector-google-drive]]
- [[connector-notion]]
- [[connector-calendar]]
- [[connector-gmail]]
