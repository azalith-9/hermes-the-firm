---
name: connector-linear
description: Use when the legal-AI product team needs to read, create, or update issues in the Linear project-management system — including automated bug report creation from chat, feature-request capture, sprint status queries, and pull-request linking. An internal engineering and ops connector; not a legal-content tool. Triggers on requests to create a bug or feature request, check sprint status, or link a chat session outcome to a Linear issue.
license: MIT
metadata: " id: connector.linear category: connector priority: P0 intent: [__connector__] related: [connector-hubspot-crm, connector-posthog, connector-github, connector-figma] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'connector'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Connector — Linear

## What it does

Linear is the issue-tracker and project-management tool for the legal-AI product team. This connector is the integration layer between the AI assistant, the product's automated monitoring, and the engineering team's Linear workspace.

Core functions:
- **Read** — retrieve issue details, search issues by query, list team sprints and project status.
- **Write** — create bug reports and feature requests from chat-captured signals, update issue status.
- **Watch** — monitor issue status changes and surface updates to relevant users.

This connector is used internally by the platform team — it is not exposed to end-user lawyers as a legal-workflow tool.

## Setup / auth

Two authentication methods are supported:

### OAuth 2.0 (preferred for user-scoped actions)
- User authorizes via Linear OAuth flow.
- Access token scoped to the user's teams and workspace.
- Suitable when an engineer or PM needs to perform actions under their own identity.

### Personal Access Token (PAT — for service accounts)
- Generate a PAT in Linear Settings → API.
- Scope to the specific teams and projects the service account needs.
- Used for automated actions (bug report creation, status monitoring).
- Stored in the platform's secrets manager; rotated every 90 days.

### Workspace configuration
1. Select the Linear workspace on initial connector setup.
2. Map team identifiers to their workflow purposes (e.g., "DES" team = design, "ENG" team = engineering, "OPS" team = operations).
3. Configure webhook subscriptions for the issue events the platform should monitor.

## Capabilities

| Capability | Auth required | Notes |
|---|---|---|
| Read issue by ID | Read | Returns full issue detail including description, labels, assignee, status |
| Search issues | Read | Full-text search + filter by label, assignee, project, status |
| List team members | Read | Useful for assignee suggestions |
| List teams and projects | Read | For routing new issues to the right team |
| Create new issue | Write | With title, description, team, label, priority |
| Update issue status | Write | Move through the team's workflow states |
| Add comment to issue | Write | For logging automation-generated notes |
| Create sub-issue | Write | For breaking down a bug into sub-tasks |
| Watch issue for status changes | Webhook | Subscribe to `issueUpdated` events |
| Link pull request | Write via PR integration | Associate a GitHub PR with a Linear issue |

## Use cases

### Bug report collection (from chat)

When a user reports a product issue in chat (e.g., "the NDA generator crashed mid-generation"), the assistant:
1. Asks one clarifying question: "What browser / device, and what were you doing just before the crash?"
2. Creates a Linear issue in the `ENG` team with:
   - Title: formatted bug title.
   - Description: user-provided context + session ID + timestamp.
   - Label: `bug` + severity (P0/P1/P2 based on impact).
   - Assignee: on-call engineer (from a configured rotation list).
3. Returns the Linear issue URL to the user with "I've logged this as ENG-[N]. Our team will follow up within [SLA]."

### Feature request collection

When a user expresses a feature wish ("I wish Louis could auto-file documents with the DIFC Court"):
1. Confirm interest: "Should I log this as a feature request for the product team?"
2. On confirmation, create a Linear issue in the `PROD` team with:
   - Title: feature request summary.
   - Description: verbatim user request + context.
   - Label: `feature-request` + relevant practice area tag.
3. Return the issue URL.

Do not over-promise. Never say the feature will be built — say it will be reviewed.

### Sprint planning integration

Retrieve the current sprint status for a team:
- List issues in the current cycle with their status (In Progress / In Review / Done / Backlog).
- Surface any overdue issues (due date passed + not Done).
- Flag blockers (issues with the `blocked` label).

Useful for daily standups or asynchronous status digests.

### Status dashboard

Aggregate issue counts per label and per status for a product health view:
- Open bugs by severity.
- Feature requests by vote count or recency.
- Deployment blockers.

### Pull request linking

When a PR is opened in GitHub that references a Linear issue (via the `ENG-123` convention in the PR title or branch name), the connector can:
- Look up the Linear issue.
- Update its status to "In Review."
- Add a comment linking the PR URL.

## Permissions model

| User type | Linear access level | Permitted actions |
|---|---|---|
| Chat users (end-users) | None (create via service account only) | Submit bug/feature reports; view issue URL |
| Platform engineers | Team member | Full read/write on their team |
| Senior engineers / PMs | Team admin | Cross-team visibility; priority changes |
| Admin | Workspace admin | Global; required for webhook setup and integration config |

A user should never be able to read another user's private issue comments or attached files they are not authorized to see.

## Tenant isolation

Each tenant connects their own Linear workspace:
- The connector stores the workspace ID per tenant.
- All API calls from a given tenant are scoped to their workspace.
- Cross-tenant issue creation or reading is prohibited and treated as a security incident.

## Audit logging

All chat-driven Linear actions are logged:
- Actor: user ID (for user-initiated) or service account (for automated).
- Action: create / update / comment.
- Issue ID and team.
- Timestamp (UTC).

Audit logs are retained for 90 days.

## Failure modes

| Failure | Cause | Resolution |
|---|---|---|
| `Unauthorized` | PAT expired or revoked | Rotate PAT; alert platform engineer |
| Team not found | Team ID changed (Linear allows renaming) | Refresh team list from workspace; update mapping |
| Issue creation fails | Description too long (>64KB) | Truncate description; attach full context as a comment |
| Webhook not delivered | Network interruption | Linear retries for 24h; implement a reconciliation job to catch missed events |
| Duplicate issue | Same bug reported by multiple users | Implement deduplication by checking for open issues with similar title in the last 7 days before creating |

## Related skills

- [[connector-hubspot-crm]]
- [[connector-posthog]]
- [[connector-figma]]
