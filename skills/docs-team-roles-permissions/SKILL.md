---
name: docs-team-roles-permissions
description: Use when an administrator needs to understand or explain the Louis role-based access control system, onboard new team members with the correct permissions, or determine which tier unlocks custom roles. Documents the five standard roles (Admin, Billing Admin, Lawyer, Paralegal, Viewer) and their permission sets, plus the Enterprise custom-role capability. Applicable across all jurisdictions.
license: MIT
metadata: " id: docs.team-roles-permissions category: docs jurisdictions: [__multi__] priority: P2 intent: [roles, permissions, access control, RBAC, team management, enterprise] related: [docs-security-overview, docs-sso-saml-setup, docs-tenant-isolation-explainer] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'docs'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Team Roles & Permissions

## Overview

Louis uses role-based access control (RBAC). Every user in an organization is assigned exactly one role. Roles are assigned by Admins at invitation time and can be changed by Admins at any time. On Enterprise tier, custom roles with granular permission scoping are available.

## Standard roles

### Admin
Full control over the organization.

| Permission | Admin |
|---|---|
| Invite / remove users | Yes |
| Change user roles | Yes |
| Configure SSO | Yes |
| Manage billing | Yes (unless Billing Admin is separate) |
| Access all workspaces | Yes |
| Create / delete workspaces | Yes |
| View all documents | Yes |
| Manage integrations | Yes |
| Export audit logs | Yes |

### Billing Admin
Handles billing and subscription management without full administrative access to legal content.

| Permission | Billing Admin |
|---|---|
| Manage subscription & payment | Yes |
| View invoices | Yes |
| Access legal workspaces | No |
| Invite users | No |
| View documents | No |

Use this role for finance team members who need to manage the subscription but must not access confidential legal documents.

### Lawyer
The primary professional user role.

| Permission | Lawyer |
|---|---|
| Create conversations | Yes |
| Upload documents | Yes |
| Generate drafts | Yes |
| Run contract reviews | Yes |
| Access shared workspaces | Yes (where invited) |
| Create workspaces | Yes |
| Share documents with team | Yes |
| View billing | No |
| Manage users | No |

### Paralegal
Same as Lawyer but without document creation and draft generation capabilities in restricted workspaces.

| Permission | Paralegal |
|---|---|
| View documents in accessible workspaces | Yes |
| Run AI queries on accessible documents | Yes |
| Upload documents (to own workspace) | Yes |
| Generate full drafts | Workspace-dependent |
| Create workspaces | No |
| Share documents organization-wide | No |

> **Note**: Paralegal access to specific workspaces is controlled by the workspace owner (a Lawyer or Admin). A Paralegal only sees what they have been explicitly granted access to.

### Viewer
Read-only access. Suitable for clients, compliance officers, or external auditors needing to review (but not interact with) specific documents.

| Permission | Viewer |
|---|---|
| View documents in accessible workspaces | Yes (read-only) |
| Download documents | Configurable |
| Run AI queries | No |
| Upload documents | No |
| Generate drafts | No |

## Permission matrix summary

| Permission | Admin | Billing Admin | Lawyer | Paralegal | Viewer |
|---|---|---|---|---|---|
| Invite users | Yes | No | No | No | No |
| Configure SSO | Yes | No | No | No | No |
| Manage billing | Yes | Yes | No | No | No |
| Create workspaces | Yes | No | Yes | No | No |
| Upload documents | Yes | No | Yes | Yes | No |
| Generate drafts | Yes | No | Yes | Partial | No |
| Run contract review | Yes | No | Yes | Yes | No |
| View documents | Yes | No | Yes | Partial | Partial |
| Export audit logs | Yes | No | No | No | No |

## Enterprise: custom roles

On the Enterprise tier, Admins can create custom roles with granular permission toggles. Use cases include:

- **Compliance Officer**: read-only access to all workspaces for audit purposes, plus export rights, but no draft generation.
- **External Counsel**: limited to a single matter workspace with expiry date.
- **Client Portal User**: can view and comment on shared documents only.

Custom roles are configured in **Settings → Organization → Roles → Custom Roles**.

## How to assign roles

1. Go to **Settings → Team**.
2. Click **Invite member** or select an existing member.
3. Set role from the dropdown.
4. For SSO-provisioned users, roles can be set automatically via group-to-role mapping (see [[docs-sso-saml-setup]]).

## Workspace-level permissions

Roles define the ceiling of access; workspace membership further scopes it down. A Lawyer with workspace access to "Matter A" cannot see documents in "Matter B" unless they are also added to "Matter B." Admins can always access all workspaces.

## Related skills

- [[docs-security-overview]]
- [[docs-sso-saml-setup]]
- [[docs-tenant-isolation-explainer]]
