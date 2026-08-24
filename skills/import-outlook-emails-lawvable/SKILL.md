---
name: import-outlook-emails-lawvable
description: Use when migrating a Lawvable Outlook email-processing skill into the mini-hermes-the-firm format. This adapter maps the legacy Lawvable email-ingestion configuration — Microsoft Graph API authentication, email threading, legal-matter tagging, privilege flagging, and action-item extraction — into the standard skill model. Triggers on import of any Lawvable-native Outlook integration workflow.
license: MIT
metadata: " id: import.outlook-emails-lawvable category: import jurisdictions: [__multi__] priority: P3 intent: [__import__, outlook, email-processing, lawvable, migration, legal-ops] related: [import-meeting-briefing-anthropic, import-docx-processing-anthropic, import-pdf-processing-anthropic, connector-outlook-graph] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'import'.
Registered as a flat plugin skill.
-->


# Import: Outlook Emails (Lawvable)

## What it does

This import adapter migrates a **Lawvable Outlook email-processing skill** into the `mini-hermes-the-firm` standard format. Lawvable is a legal AI platform; its Outlook integration allows emails to be ingested, analysed, and routed into legal workflows. This adapter maps the Lawvable data model to the `mini-hermes-the-firm` connector/import format so the email-processing logic continues to work in the new environment.

Legal email processing has specific requirements beyond standard email handling: **privilege detection**, **matter tagging**, **deadline identification** (limitation periods, response deadlines, regulatory notification windows), and **client-communication classification** (privileged, third-party, administrative).

## Import config

| Field | Source mapping | Default if absent |
|---|---|---|
| `auth_method` | Legacy `auth` | `microsoft_graph_oauth2` |
| `mailbox_scope` | Legacy `mailbox` | `shared_legal_mailbox` |
| `thread_depth` | Legacy `thread_depth` | `full` (entire conversation chain) |
| `privilege_detection` | Legacy `detect_privilege` boolean | `true` |
| `matter_tagging` | Legacy `matter_tags` config | Auto-detect from subject line + sender |
| `action_extraction` | Legacy `extract_actions` boolean | `true` |
| `deadline_detection` | Legacy `detect_deadlines` boolean | `true` |
| `output_format` | Legacy `format` | `email_brief` |
| `language` | Legacy `lang` | `auto-detect` |

## Dry-run preview

```
IMPORT PREVIEW — outlook-emails-lawvable
Source shape       : Lawvable Outlook email integration
Auth               : Microsoft Graph OAuth2
Mailbox            : shared_legal_mailbox
Thread depth       : full
Privilege detection: enabled
Matter tagging     : auto-detect
Action extraction  : enabled
Deadline detection : enabled
Output             : email_brief
```

## Email processing pipeline (post-import)

1. **Authentication**: Microsoft Graph API OAuth2; application-level permissions for shared mailbox access; ensure `Mail.Read` and `Mail.ReadBasic` scopes; do not request `Mail.Send` unless required.
2. **Ingestion**: fetch emails with metadata (sender, recipients, date, subject, attachments); preserve threading via `conversationId`.
3. **Privilege classification**:
   - Attorney-client privilege: sender or recipient is `[name]@[lawfirm]`; subject line contains "privileged", "legal advice", "confidential"
   - Work product: created in anticipation of litigation
   - Mark non-privileged external communications separately
4. **Matter tagging**: match subject/sender against matter reference database; tag with matter ID.
5. **Language detection**: detect Arabic, French, English, other; route accordingly.
6. **Action extraction**: identify:
   - Requests for action (reply needed, document needed, decision needed)
   - Deadlines stated in email body
   - Regulatory notification windows (e.g. "please respond by [date]")
7. **Output**: structured email brief per thread.

## Legal-specific processing rules

- **Privileged emails must never be sent to third-party AI services** without explicit client consent and appropriate DPA/NDA coverage.
- **Arabic emails**: UAE government correspondence and local counsel emails are frequently in Arabic; ensure Arabic-language parsing is enabled.
- **Bilingual threads**: MENA legal correspondence often mixes Arabic and English in the same thread; handle language switches gracefully.
- **Regulatory correspondence**: emails from DFSA, CBUAE, UAE Ministry of Justice, Lebanese Ministry of Justice, ACPR (France) should be flagged with HIGH priority and deadline detection applied rigorously.
- **Limitation period triggers**: a demand letter or notice of claim starts the limitation clock; always flag and record the date received.

## Failure modes

| Error | Likely cause | Resolution |
|---|---|---|
| `auth_failure` | OAuth2 token expired or scope insufficient | Refresh token; verify `Mail.Read` scope is granted |
| `thread_truncated` | Legacy set `thread_depth: 1` | Override to `full` for legal context |
| `privilege_false_positive` | Law firm email domain not configured | Configure firm domains in privilege-detection config |
| `arabic_garbled` | Encoding issue in Arabic emails | Force `encoding: utf-8`; re-ingest |
| `deadline_missed` | Email contained informal deadline not detected | Expand deadline-detection keywords to include informal language |

## Related skills

- [[import-meeting-briefing-anthropic]]
- [[import-docx-processing-anthropic]]
- [[import-pdf-processing-anthropic]]
- [[connector-outlook-graph]]
- [[ops-legal-inbox-triage]]
