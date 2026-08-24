---
name: connector-gmail
description: Use when a lawyer or legal-operations user wants to search, label, draft, or manage email threads in Gmail in the context of a legal matter — including matter-linked email tracking, client correspondence management, counterparty communication review, and deadline-triggering emails. Requires Google OAuth per-user authorization. Triggers on requests to search email, draft a reply, track correspondence for a matter, or identify emails containing legal notices or deadlines.
license: MIT
metadata: " id: connector.gmail category: connector jurisdictions: [__multi__] priority: P2 intent: [__connector__] related: [connector-google-drive, connector-calendar, connector-notion, connector-hubspot-crm] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'connector'.
Registered as a flat plugin skill.
-->


# Connector — Gmail

## What it does

The Gmail connector integrates with the user's Gmail account to enable matter-linked email management within the legal-AI platform. Its three core functions are:

1. **Search and retrieve** — finding relevant email threads by sender, recipient, keyword, date range, or matter tag.
2. **Label and organize** — applying labels to tag emails with matter references, urgency flags, or workflow stages.
3. **Draft and reply** — composing draft replies based on context, which the lawyer reviews before sending.

The connector never sends email autonomously. All outbound email actions require explicit human confirmation.

## Setup / auth

Authentication uses **Google OAuth 2.0** with per-user delegation:

- Each lawyer authorizes their own Gmail account — no admin-wide delegation unless the firm has Google Workspace with explicit domain-wide delegation configured and consented to.
- OAuth scopes:
  - `gmail.readonly` — for search and read operations.
  - `gmail.labels` — for creating and applying labels.
  - `gmail.compose` — for creating draft messages.
  - `gmail.modify` — for labeling, archiving, and marking read/unread.
- Do not request `gmail.send` scope unless the firm has explicitly enabled AI-assisted sending (with appropriate workflow approvals). Default: drafts only, user sends manually.
- Tokens stored per-user, encrypted at rest; refresh tokens rotated every 6 months.

## Capabilities

| Capability | Scope required | Notes |
|---|---|---|
| Search threads by keyword, sender, date | `gmail.readonly` | Full Gmail search operators supported |
| Read full email thread content | `gmail.readonly` | Including attachments metadata (not content) |
| Apply / remove labels | `gmail.labels` + `gmail.modify` | Create matter-reference labels |
| Create draft reply | `gmail.compose` | Draft created; not sent until user approves |
| Create draft new email | `gmail.compose` | As above |
| Mark as read / unread | `gmail.modify` | Used in workflow automations |
| Archive thread | `gmail.modify` | Removes from inbox; does not delete |
| Download email attachment | `gmail.readonly` | Returns attachment as bytes; routes to [[connector-google-drive]] or matter workspace |

## Usage patterns

### Pattern 1 — Matter-linked email threading

When a lawyer opens a matter, automatically search Gmail for emails matching:
- The client's email address.
- The matter reference number (if used in subject lines).
- Key counterparty names.

Return a chronological thread summary: date, direction (in/out), snippet, and any attachments. The lawyer confirms which threads to link to the matter.

### Pattern 2 — Legal notice identification

```
User: "Any emails from opposing counsel about the Al-Hamdan matter this week?"
→ Search: sender:opposing-counsel@firm.com after:2024-06-01 "Al-Hamdan" OR "matter ref 2024-045"
→ Returns matching threads with date, snippet, and attachment list
→ If any email contains a deadline notice or formal letter, flag for lawyer review
```

### Pattern 3 — Draft a formal response

```
User: "Draft a response to this letter from opposing counsel declining mediation"
→ Read the source email thread
→ Draft a reply applying the firm's tone and the matter's procedural context
→ Mark as [DRAFT] and present to lawyer for review before sending
```

### Pattern 4 — Deadline email monitoring

Set a Gmail search alert (via [[connector-scheduled-tasks]]) for emails containing:
- Keywords: "deadline," "notice period," "time to respond," "filing by," "limitation."
- Senders: court registries, regulatory authorities, known counterparties.

Surface matching emails to the matter dashboard with priority flagging.

### Pattern 5 — Label organization for matter management

Create a Gmail label scheme mirroring the matter reference system:
- `Matters/2024-045 Al-Hamdan`
- `Matters/2024-046 Fintech Acquisition`

Apply labels to threads automatically when a new matter email is identified, or manually on lawyer instruction.

## Professional-responsibility considerations

- **Attorney-client privilege.** Emails between lawyer and client are privileged. The connector must never route privileged email content to external services without explicit user authorization.
- **No autonomous sending.** Legal correspondence has professional-responsibility implications. All outbound emails require human review and explicit send confirmation.
- **Opposing counsel emails.** Emails to or from opposing counsel should be flagged with a note that they may be discoverable. Never automatically forward or share these.
- **Confidentiality tags.** If an email's subject or body contains terms like "PRIVILEGED AND CONFIDENTIAL" or "WITHOUT PREJUDICE," apply a confidentiality label automatically and alert the lawyer before any further processing.

## Permissions & safety

- **Read before you write.** Always present the email content to the lawyer before drafting a response — never draft a reply from a summary alone.
- **No bulk archiving.** Archiving operations must be confirmed by the user. Bulk operations require explicit approval with a preview of affected threads.
- **Audit log.** Every search, label application, and draft creation is logged with user ID, timestamp, and the search query used.
- **Tenant isolation.** Each lawyer's Gmail access is scoped to their own account. No cross-user email access.

## Failure modes

| Failure | Cause | Resolution |
|---|---|---|
| `Insufficient permission` | Scope not granted for the operation | Prompt user to re-authorize with additional scope |
| Search returns too many results | Overly broad query | Narrow by date range, sender, or matter reference |
| Draft created but not visible | Gmail filter hiding drafts | Direct user to check Drafts folder and any filters |
| Attachment too large | >25MB limit for Gmail attachments | Split or route via [[connector-google-drive]] share link |
| Thread deleted | User deleted the email | Irretrievable; check Google Vault if firm uses it |

## Related skills

- [[connector-google-drive]]
- [[connector-calendar]]
- [[connector-notion]]
- [[connector-hubspot-crm]]
