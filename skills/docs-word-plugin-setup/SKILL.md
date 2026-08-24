---
name: docs-word-plugin-setup
description: Use when a user or IT administrator needs to install, configure, or troubleshoot the Louis Microsoft Word Add-in (Office Add-in, cross-platform). The plugin surfaces Louis's four key in-document capabilities — clause insertion, redlining/track changes, risk scanning, and citation insertion — without leaving the Word interface. Applicable across all jurisdictions and Office 365 / Microsoft 365 deployments.
license: MIT
metadata: " id: docs.word-plugin-setup category: docs jurisdictions: [__multi__] priority: P2 intent: [Word plugin, Office Add-in, Microsoft Word, clause insert, redline, citation] related: [docs-security-overview, docs-sso-saml-setup, docs-team-roles-permissions] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'docs'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Microsoft Word Plugin — Setup Guide

## Overview

The Louis Word Add-in is an Office Add-in (built on the Microsoft Office Add-ins platform) that runs inside Microsoft Word on Windows, macOS, and Word Online. It connects to your Louis account and surfaces four AI capabilities directly in the document ribbon without requiring copy-paste to an external browser tab.

### Key features

| Feature | What it does |
|---|---|
| **Clause insert** | Browse the Louis clause library and insert jurisdiction-specific standard clauses at cursor position |
| **Redline** | Send a selection or the whole document for AI review; receive tracked-changes redline suggestions inserted directly into Word |
| **Risk scan** | Run a risk analysis on the open document; highlights are inserted as Word comments color-coded by severity |
| **Citation insert** | Look up a legal citation (statute, case, regulation) and insert a correctly formatted reference at cursor |

## Prerequisites

- Microsoft Word 2016 or later (Windows or macOS), or Word Online (Microsoft 365).
- An active Louis account on any paid plan.
- Internet connectivity (the Add-in communicates with Louis's API; it does not work offline).
- For organization-wide deployment: Microsoft 365 admin access (to deploy via centralized Add-in management).

## Installation — Individual user

### Method A: Microsoft AppSource

1. In Word, go to **Insert → Add-ins → Get Add-ins**.
2. Search for "Louis Legal AI".
3. Click **Add**.
4. The Louis panel will appear in the right-hand task pane.
5. Click **Sign in** and authenticate with your Louis credentials (or use SSO if your organization has it configured).

### Method B: Direct manifest install (IT-managed)

1. Download the Add-in manifest XML from your Louis admin panel (**Settings → Integrations → Word Add-in → Download Manifest**).
2. In Word, go to **Insert → Add-ins → My Add-ins → Upload My Add-in**.
3. Browse to the downloaded manifest XML.
4. The Louis panel will load.

## Installation — Organization-wide deployment (IT/Admin)

For enterprise deployments where all users should have the Add-in pre-installed:

1. In the **Microsoft 365 Admin Center**, go to **Settings → Integrated apps**.
2. Click **Upload custom apps**.
3. Upload the manifest XML (download from Louis admin panel).
4. Assign to the relevant users, groups, or the entire organization.
5. Users will see the Louis Add-in automatically in Word within 24 hours (Microsoft's deployment propagation window).
6. For SSO organizations, users will authenticate via their existing IdP without a separate login prompt.

## Using the Add-in

### Clause insert
1. Place cursor where you want the clause.
2. In the Louis panel, go to **Clauses** tab.
3. Filter by jurisdiction and clause type (e.g., "Force Majeure — UAE Federal").
4. Click **Insert** to drop the clause at cursor, or **Preview** to review it first.
5. The inserted clause is editable like any Word text.

### Redline
1. Select the text to review, or leave nothing selected to review the whole document.
2. In the Louis panel, click **Redline**.
3. Choose review profile (e.g., "NDA Review — Buyer's Perspective").
4. Louis returns suggested changes as Word tracked changes (Accept/Reject in the standard Word interface).

### Risk scan
1. Open the document to scan.
2. In the Louis panel, click **Risk Scan**.
3. Select jurisdiction and document type.
4. Results appear as color-coded Word comments:
   - Red comment: high-risk clause.
   - Yellow comment: medium risk / negotiating point.
   - Blue comment: informational / standard clause confirmed.
5. Each comment includes a brief explanation and a suggested alternative.

### Citation insert
1. Place cursor at the citation location.
2. In the Louis panel, **Citations** tab → search for the statute, regulation, or case.
3. Select the citation format (Bluebook, OSCOLA, or a jurisdiction-specific style).
4. Click **Insert**.

## Troubleshooting

| Issue | Likely cause | Fix |
|---|---|---|
| Add-in panel won't load | Firewall blocking `api.haqq.ai` | Allow outbound HTTPS to `*.haqq.ai` on port 443 |
| "Not signed in" after login | Third-party cookies blocked | Enable cookies for `*.haqq.ai` in browser/Word settings |
| Redline not appearing as tracked changes | Word "Show Markup" is off | Enable **Review → Show Markup → All Markup** |
| Organization deployment not appearing | Propagation delay | Wait 24 hours; force refresh in Word |
| SSO loop | IdP session expired | Log out of the Add-in, re-authenticate via IdP |

## Data and privacy

- The Add-in sends only the text you explicitly submit (selection or document) to the Louis API.
- Text is transmitted over TLS 1.3.
- The full security and tenant-isolation guarantees of the Louis platform apply — see [[docs-security-overview]].
- Word document metadata (filename, author) is not sent unless explicitly included in the submission.

## Related skills

- [[docs-security-overview]]
- [[docs-sso-saml-setup]]
- [[docs-team-roles-permissions]]
