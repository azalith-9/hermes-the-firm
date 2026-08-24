---
name: connector-notion
description: Use when a legal-AI workflow needs to read Notion pages or write to Notion databases — for example, importing a knowledge base from Notion into the platform, exporting a generated document or research memo to a Notion page, or syncing matter notes to a team workspace in Notion. Requires Notion OAuth per-workspace authorization. Triggers on requests to read from or write to Notion, or when a knowledge-base import/export workflow is initiated.
license: MIT
metadata: " id: connector.notion category: connector jurisdictions: [__multi__] priority: P2 intent: [__connector__] related: [connector-google-drive, connector-apple-notes, connector-gmail, connector-linear] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'connector'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Connector — Notion

## What it does

The Notion connector enables bidirectional content flow between the legal-AI platform and Notion workspaces. Notion is used by law firms, legal-ops teams, and in-house legal departments as a knowledge base, internal wiki, and operational workspace. This connector allows the AI assistant to:

- **Read** Notion pages and database records as context for legal-AI tasks.
- **Write** generated content (research memos, document drafts, matter summaries) to Notion pages.
- **Sync** structured data between Notion databases and the platform (e.g., matter lists, client directories, task trackers).

## Setup / auth

Authentication uses **Notion's OAuth 2.0** integration flow:

1. The platform creates a Notion integration in `notion.so/my-integrations`.
2. A workspace admin authorizes the integration and selects which pages/databases to share.
3. The connector receives an access token scoped to the shared pages/databases only.
4. Tokens stored per-tenant in the platform's secrets manager.

**Important:** Notion access is page-level, not workspace-level. The workspace admin explicitly selects which pages and databases the integration can access. The connector cannot read pages that were not shared with the integration.

Two integration levels:
- **Internal integration:** for a single Notion workspace (law firm using one Notion account).
- **Public integration (OAuth):** for multi-tenant use where different firms have separate Notion workspaces.

## Capabilities

| Capability | Direction | Notes |
|---|---|---|
| Read a page (full content) | Read | Returns blocks as markdown |
| Read a database (all rows) | Read | Returns as structured records |
| Query a database (filtered/sorted) | Read | Filter by property; sort by date or name |
| Create a new page | Write | Under a specified parent page or database |
| Append to an existing page | Write | Adds content at the end of a page |
| Update a database record | Write | Modify properties of an existing row |
| Search pages by keyword | Read | Searches titles and content |
| Read comments | Read | Retrieves comments on a page |
| Post a comment | Write | Adds a comment to a page |

## Usage patterns

### Pattern 1 — Import firm knowledge base

Many firms use Notion as their internal precedent library and procedure manual. Import this as context for the AI assistant:
- List all pages in the designated knowledge-base section.
- Retrieve page content.
- Index into the platform's skill/context layer for retrieval during drafting.
- Schedule a weekly re-sync to pick up updates (via [[connector-scheduled-tasks]]).

### Pattern 2 — Export research memo to Notion

After the AI generates a research memo (e.g., on KSA VAT treatment of cross-border services):
- Create a new Notion page in the "Legal Research" database.
- Populate with the memo content.
- Set properties: matter reference, author (user), date, status (Draft).
- Return the Notion page URL to the user.

### Pattern 3 — Matter status tracking

Sync matter status from the legal-AI platform to a Notion project-tracker database:
- Update the "Status" property as matters progress.
- Add deadline dates as Notion date properties.
- Post AI-generated matter summaries as page content.

### Pattern 4 — Firm procedure import for onboarding

When a new firm signs up, they can import their existing Notion-based procedure guides directly into the platform as context for AI-assisted workflows. The connector reads the pages; the platform processes them into structured context entries.

### Pattern 5 — Collaborative annotation

After a contract review, post the AI-generated review notes as Notion page content with structured properties:
- High-risk clauses: listed with article numbers and risk ratings.
- Comments added to each section for lawyer review.
- Lawyers use Notion's native comment feature to respond; the connector can read those comments back into the platform for iterative review.

## Knowledge-base considerations for legal use

When using Notion as a legal knowledge base, note:

- **Version control.** Notion pages don't have true version control — only edit history. For precedents that must be version-locked (e.g., a signed template), store the authoritative version as a PDF in [[connector-google-drive]] and use Notion for working notes only.
- **Structured vs unstructured.** Notion databases (with typed properties) are significantly more useful for structured legal data (matter lists, jurisdiction tables) than free-form pages. Encourage firms to use databases over wiki-style pages for any data they want the AI to query.
- **Arabic and RTL content.** Notion supports RTL text but the AI extraction may lose formatting for RTL pages. Flag this to the user if Arabic content is detected in a retrieved page.
- **Access control.** Notion's page-level access control means sensitive pages (e.g., a partner's personal client list) should not be shared with the integration. Work with the firm admin to define clear boundaries before setting up the integration.

## Permissions & safety

- **Minimum surface.** Only share with the integration the pages and databases that are needed for the legal-AI workflow. The connector must not request access to "All pages in workspace."
- **No write to sensitive pages.** The connector must not write to pages tagged as "Confidential" or "Client Matter — Private" without explicit user instruction.
- **Audit log.** All reads and writes are logged with user ID, page ID, and timestamp.
- **Tenant isolation.** Each tenant's Notion workspace is separate; cross-tenant page access is prohibited.

## Failure modes

| Failure | Cause | Resolution |
|---|---|---|
| `Object not found` | Page not shared with the integration | Ask workspace admin to add the page to the integration's access list |
| Integration disconnected | Workspace admin revoked access | User must re-authorize; send re-auth prompt |
| Block type unsupported | Notion page uses a block type the API doesn't serialize well (callout, toggle) | Convert to plain text; note formatting may be simplified |
| Database property type mismatch | Platform expects a date but property is text | Validate property types on schema import; prompt user to correct |
| Rate limit (`429`) | Notion API is rate-limited at 3 requests/second | Implement request queue with 350ms spacing |

## Related skills

- [[connector-google-drive]]
- [[connector-apple-notes]]
- [[connector-gmail]]
- [[connector-linear]]
- [[connector-scheduled-tasks]]
