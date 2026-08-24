---
name: outreach-press-list-enriched
description: Use when the legal AI product team needs a fully enriched press contact list — combining MENA, European, and global legal/tech publications with journalist beats, contact details, domain ratings, and recent coverage context. The enriched list is the input to the backlink PR campaign and press pitch workflows. Triggers when building or refreshing the master press outreach list.
license: MIT
metadata: " id: outreach.press-list-enriched category: outreach intent: ['__outreach__', 'press', 'media', 'contacts', 'enriched'] related: - outreach-press-list-mena - outreach-press-list-europe - outreach-backlink-pr-campaign - outreach-inbox-scan priority: P3 source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'outreach'.
Registered as a flat plugin skill.
-->


# Press List — Enriched

A raw list of publication names is not a press list. An enriched press list includes the specific journalist, their beat, their recent relevant coverage, the publication's domain rating, the right contact method, and a personalisation hook for the pitch. This skill produces the enriched format and explains how to maintain it.

## Purpose

Produce and maintain an enriched press list that enables:
- Personalised pitches to specific journalists (not generic "To the editor")
- Prioritised outreach by domain authority and audience fit
- Coverage tracking across the press contacts
- Campaign-ready input for [[outreach-backlink-pr-campaign]]

## Enriched record schema

Each entry in the enriched press list contains:

| Field | Description | Example |
|---|---|---|
| Publication | Full name | Legaltech News |
| URL | Domain | legaltechnews.com |
| Region | Geographic focus | US/Global |
| Audience | Who reads it | Legal professionals, LegalOps, GC |
| Beat | Topic coverage relevant to legal AI | AI + legal, legal ops, legal tech |
| Journalist name | Specific contact | Jane Doe |
| Journalist title | Their role | Senior Reporter |
| Contact | Email or DM handle | jdoe@legaltechnews.com |
| Recent coverage | Title of relevant recent article | "AI tools for mid-size law firms" (Jan 2026) |
| DR | Domain rating (Ahrefs) | 72 |
| Monthly traffic | Estimated | 120,000 |
| Outreach status | Not contacted / Pitched / Responded / Published | Not contacted |
| Notes | Personal connection, past coverage, specific interest | Covered our competitor in 2025 |

## Enrichment process

### Step 1 — Seed the list

Start with the base lists:
- MENA publications: [[outreach-press-list-mena]]
- European publications: [[outreach-press-list-europe]]
- Global legal-tech: see below

### Step 2 — Research journalists

For each publication:
- Find the journalist who covers legal technology or the relevant practice area
- Identify their 3 most recent relevant articles
- Note their email (from the publication's contact page or LinkedIn)
- Note any personal angle (conference speaker, prior quote about AI, etc.)

### Step 3 — Score by priority

```
Priority Score = (DR weight × 0.4) + (Audience fit × 0.4) + (Journalist accessibility × 0.2)
```

Where:
- DR weight: DR 70+ = 3; DR 50–70 = 2; DR 30–50 = 1
- Audience fit: Primary (lawyers/GC) = 3; Secondary (legal-tech) = 2; Tertiary (general business) = 1
- Journalist accessibility: Direct email = 3; LinkedIn active = 2; Only via submission form = 1

### Step 4 — Maintain freshness

Press lists go stale fast — journalists move between publications. Refresh:
- Full list: quarterly
- Active contacts (pitched or responded): monthly
- Beat verification: before each campaign

## Global legal-tech publications (always include)

| Publication | Focus | DR | Contact approach |
|---|---|---|---|
| Legaltech News | Legal technology, US focus | 72 | Direct journalist pitches |
| Legal Futures | UK legal sector, tech and innovation | 65 | Editor submissions |
| Artificial Lawyer | AI and legal specifically | 58 | Editor + journalist |
| CLOC (State of the Industry) | Legal operations | N/A (org) | Member relations |
| Above the Law | US legal profession | 78 | Contributor submissions |
| The American Lawyer | US big law | 75 | Press releases + journalist pitches |
| Law.com International | International legal | 80 | International desk |
| Legal IT Insider | Legal technology UK/EU | 55 | Editor email |

## Outreach tracking

Maintain a campaign status column and update after every contact:

| Status | Meaning |
|---|---|
| Not contacted | New lead — not yet pitched |
| Pitched D0 | Initial pitch sent |
| Pitched D7 | Follow-up sent |
| Pitched D14 | Final follow-up sent |
| Responded | Journalist engaged — in conversation |
| Published | Coverage placed — log the URL and date |
| Declined | Passed or not interested — note reason |
| Inactive | Not responded after 3 contacts — retry in 90 days |

## Related skills

- [[outreach-press-list-mena]]
- [[outreach-press-list-europe]]
- [[outreach-backlink-pr-campaign]]
- [[outreach-inbox-scan]]
- [[outreach-growth-agent-runner]]
