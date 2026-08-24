---
name: docs-changelog-reader
description: Use when a user asks what has changed in the platform recently, wants to understand new features, or an administrator needs to communicate recent updates to their team. This is a platform documentation skill covering the in-app changelog reader — how updates are categorized, surfaced, and filtered by user cohort (admins see admin changes; lawyers see lawyer-relevant changes).
license: MIT
metadata: " id: docs.changelog-reader category: docs jurisdictions: [__multi__] priority: P2 intent: [__docs__, changelog, release notes, product updates, new features] related: [docs-legal-ai-workspace-guide, docs-faq-pack, docs-legal-os-overview] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'docs'.
Registered as a flat plugin skill.
-->


# Changelog Reader

## What it does

The in-app changelog reader surfaces recent product changes to users directly inside the platform, without requiring them to check an external blog or release notes page. It is designed to:

- Inform legal professionals of new drafting skills, updated clause libraries, or jurisdiction coverage expansions that are immediately relevant to their work.
- Alert administrators to security updates, configuration changes, and compliance-relevant platform changes.
- Reduce support tickets by proactively communicating breaking changes or deprecated features.

## Update categories

Every changelog entry is tagged with one or more categories:

| Category | What it covers |
|---|---|
| **New feature** | A capability that did not exist before (e.g., "New: KSA PDPL compliance checklist skill") |
| **Improvement** | Enhancement to an existing feature (e.g., "Improved: Arabic-English bilingual export quality") |
| **Fix** | Bug or error correction (e.g., "Fixed: Ejari registration date calculation in UAE lease templates") |
| **Breaking** | A change that requires user or admin action (e.g., "Breaking: Legacy API v1 endpoints deprecated — migrate to v2 by [date]") |
| **Security** | Security patches, vulnerability remediations, or certificate updates |
| **Compliance** | Changes driven by regulatory developments (e.g., "Updated: UAE Corporate Tax clause library to reflect June 2023 guidance") |

## User cohort filtering

The changelog is filtered by user role so each user sees the updates most relevant to them:

| User role | What they see |
|---|---|
| **Workspace administrator** | All updates including admin configuration changes, security updates, API changes, billing updates |
| **Lawyer / legal professional** | New and improved drafting skills, jurisdiction coverage changes, document review enhancements, compliance-related legal content updates |
| **Paralegal / legal ops** | Document management updates, workflow improvements, matter management changes |
| **Developer** | API changes, SDK updates, webhook changes, breaking changes |
| **All users** | Security fixes affecting all users, feature launches relevant to all roles |

Cohort filtering is based on the role assigned in the workspace user management. Administrators can view the full unfiltered changelog at any time.

## Data source

The changelog reader pulls from one of two sources depending on deployment:

- **Cloud (SaaS)**: pulls from the platform's release-notes API (`GET /api/v1/changelog`). Updates are published within 24 hours of deployment.
- **On-premise / enterprise**: pulls from a `changelog.md` file included in the deployment package, or from a self-hosted release-notes endpoint configured by the IT administrator.

The release-notes API supports:
- `from_date` / `to_date` filter
- `category` filter
- `user_role` cohort filter
- Pagination

## Accessing the changelog

- **In-app**: the changelog is accessible via the **?** / Help icon in the top navigation bar → **What's New**. A notification badge appears when there are unread entries matching the user's cohort.
- **API**: see [[docs-dev-hub-api-reference]] for the `/changelog` endpoint schema.
- **Email digest**: workspace administrators can configure a weekly or monthly email summary of changes for distribution to their team.

## Format of a changelog entry

Each entry follows this structure:

```
[Date] — [Category tag(s)]
Title: [Feature/change name]
Summary: [1–3 sentences describing the change and why it matters]
Impact: [Who is affected; action required if any]
Link: [Detailed documentation page if applicable]
```

## How to use this doc

Direct users here when they ask:
- "What's new in the platform?"
- "When did you add [feature]?"
- "Has anything changed with [jurisdiction]'s templates recently?"
- "I got a notification about a breaking change — what do I need to do?"

For detailed documentation on specific features mentioned in the changelog, direct to [[docs-legal-ai-workspace-guide]] or the specific feature documentation page.

## Related skills

- [[docs-legal-ai-workspace-guide]]
- [[docs-faq-pack]]
- [[docs-legal-os-overview]]
- [[docs-dev-hub-api-reference]]
