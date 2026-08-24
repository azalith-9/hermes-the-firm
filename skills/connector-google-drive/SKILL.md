---
name: connector-google-drive
description: Use when a lawyer or legal-operations user needs to read, search, or attach Google Drive documents to a legal matter — including retrieving draft contracts, precedent documents, due-diligence files, or correspondence stored in Drive as context for AI-assisted drafting or review. Requires Google OAuth per-user authorization. Triggers on requests to access a Drive file, find documents by keyword, or attach Drive content to a matter workspace.
license: MIT
metadata: " id: connector.google-drive category: connector jurisdictions: [__multi__] priority: P2 intent: [__connector__] related: [connector-gmail, connector-notion, connector-calendar, connector-apple-notes] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'connector'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Connector — Google Drive

## What it does

The Google Drive connector provides access to documents, spreadsheets, PDFs, and other files stored in the user's Google Drive workspace. In a legal-AI context, its primary use is surfacing existing documents — precedents, draft contracts, due-diligence questionnaires, matter files — as context for AI-assisted drafting, review, and analysis.

Core functions:
- **Search** — find documents by keyword, file name, owner, or date.
- **Read** — retrieve the content of a document for use as context.
- **Attach to matter** — link a Drive document to a matter record.
- **Download** — export a Google Doc as a PDF or DOCX for further processing.

## Setup / auth

Authentication uses **Google OAuth 2.0** with per-user delegation:

- Each user authorizes their own Google Drive — no admin-wide delegation unless Google Workspace is configured with domain-wide delegation.
- OAuth scopes:
  - `drive.readonly` — for search and read operations.
  - `drive.file` — for creating or modifying files the app created (narrower than full Drive access).
  - `drive.metadata.readonly` — for file metadata only (name, owner, modified date) without reading content.
- Default to `drive.readonly` unless a write capability is explicitly required.
- Tokens stored per-user, encrypted at rest.

## Capabilities

| Capability | Scope | Notes |
|---|---|---|
| Search files by name or keyword | `drive.readonly` | Searches filenames and Google Docs full-text |
| Read Google Doc content | `drive.readonly` | Returns as plain text or markdown |
| Read Google Sheet data | `drive.readonly` | Returns rows/columns; useful for data-room indexes |
| Download as PDF | `drive.readonly` | Exports any Google Doc to PDF |
| Download as DOCX | `drive.readonly` | Exports for redlining in Word-based workflows |
| List folder contents | `drive.readonly` | Useful for matter folder inspection |
| Create a new document | `drive.file` | Only creates new files; does not modify existing |
| Upload a file | `drive.file` | Stores generated documents back to Drive |
| Share file (change permissions) | `drive` (full) | Requires explicit approval; high-risk |

## Usage patterns

### Pattern 1 — Retrieve a precedent before drafting

```
User: "Draft an NDA based on our standard template"
→ Search Drive for "NDA template" in the firm's Precedents folder
→ Return the most recent version as context
→ Draft a new NDA using the template as the base, adapting for the specific parties
```

### Pattern 2 — Data room indexing

For an M&A due diligence, the data room is often shared via Google Drive:
- List all files in the shared data room folder.
- Return a structured index: file name, type, last modified, and folder path.
- Flag missing items against a standard due-diligence checklist.

### Pattern 3 — Contract review from Drive

```
User: "Review the SPA at [Drive link]"
→ Retrieve the document content from Drive
→ Run the contract through the relevant review skill
→ Return a structured review with flagged clauses
```

### Pattern 4 — Generate and save a document back to Drive

After generating a contract draft:
- Export as DOCX.
- Upload to the designated matter folder in Drive.
- Return the Drive link for the lawyer to access.

### Pattern 5 — Matter folder organization

For each new matter, create a standard folder structure in Drive:
```
/Matters/2024-045 Al-Hamdan v. TechCo/
  ├── 01 Correspondence/
  ├── 02 Pleadings/
  ├── 03 Evidence/
  ├── 04 Research/
  └── 05 Drafts/
```
This can be automated via the connector on matter creation.

## Document security considerations

- **Shared drives.** In law firms using Google Workspace, most matter documents are in Shared Drives (formerly Team Drives). Confirm the user has access before attempting to read.
- **External sharing.** Do not change the sharing permissions of a client document without explicit lawyer instruction. Accidental "anyone with link" sharing of privileged documents is a confidentiality breach.
- **Version history.** Google Docs maintain version history. When reviewing a contract, confirm you are reading the current (most recent) version — not a draft that has since been superseded.
- **Privileged documents.** Documents in Drive may be attorney-client privileged or subject to work-product protection. Treat all matter documents as potentially privileged unless the user confirms otherwise.

## Permissions & safety

- **Read-first.** Default to `drive.readonly`. Escalate to write scope only when a write operation is explicitly requested.
- **No autonomous sharing.** Changing file permissions requires explicit human instruction and a confirmation step.
- **Audit log.** All reads, searches, and writes are logged with user ID, timestamp, and file ID.
- **Tenant isolation.** Each user's Drive access is scoped to their own account and shared drives they are members of.

## Failure modes

| Failure | Cause | Resolution |
|---|---|---|
| File not found | File deleted, moved, or access revoked | Check with the file owner; do not retry with a search for similar names |
| `403 Forbidden` | User lacks access to the specific file or shared drive | Request access through normal channels; do not attempt workaround |
| Export format unsupported | Non-Google file type (e.g., a PDF uploaded to Drive) | Download the raw file bytes instead of using the export API |
| Large document timeout | Google Doc >500 pages | Paginate the read; split into sections for processing |
| Drive API quota exceeded | High-volume firm with many concurrent users | Implement request queuing and respect `429` backoff |

## Related skills

- [[connector-gmail]]
- [[connector-notion]]
- [[connector-calendar]]
- [[connector-apple-notes]]
