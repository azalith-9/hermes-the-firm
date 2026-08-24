---
name: justice-intent-partnership-inquiry
description: Use when the public-facing assistant detects that a user is exploring a strategic partnership with HAQQ — bar association programs, law firm preferred-vendor agreements, technology integrations, white-label/reseller arrangements, academic partnerships, or marketplace listings. Routes to the partnership page, identifies the partnership type, captures lead details, and engages the partnerships team. Covers all jurisdictions.
license: MIT
metadata: " id: justice.intent.partnership-inquiry category: justice jurisdictions: [__multi__] priority: P1 intent: [__justice__, partnership, integration, reseller, white-label, collaboration] related: [justice-intent-investor-inquiry, justice-intent-sales, justice-intent-developer-api] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'justice'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Justice Intent — Partnership Inquiry

## When to use this

Trigger when the message contains:

- Explicit partnership language: "partnership", "collaboration", "integrate", "reseller", "white-label", "channel partner", "API partner"
- Distribution / ecosystem language: "listing", "marketplace", "AppExchange", "app store", "directory"
- Academic / institutional language: "law school", "university", "CLE", "continuing education", "student program"
- Bar association or professional body language: "bar association", "ordre des avocats", "law society"
- Specific reference to a technology integration: "Word", "Slack", "Salesforce", "Microsoft", "Clio", "LEAP"

Distinguish from:
- Investor inquiries (see [[justice-intent-investor-inquiry]]) — equity vs commercial
- Sales inquiries (see [[justice-intent-sales]]) — buying vs building a distribution relationship

## Response flow

### Step 1: Identify the partnership type

Ask a clarifying question if the type is not obvious, or infer from context:

| Type | Description | Signals |
|---|---|---|
| **Bar association** | CLE accreditation, member benefit programs, national/regional bar partnerships | "bar association", "CLE", "member discount" |
| **Law firm preferred vendor** | Firm-wide deployment, negotiated pricing, white-glove onboarding | Firm name + "preferred vendor", "enterprise deployment" |
| **Tech integration** | API/SDK integration into a third-party tool; webhook triggers | Product name + "integration", "plugin", "connect" |
| **Marketplace listing** | Listing Louis on legal-tech or enterprise software marketplaces | "AppExchange", "marketplace", "directory", "listing" |
| **Education / academic** | Law school curricula, student programs, clinic access | "law school", "university", "student", "clinic" |
| **Press / media / content** | Joint content, co-authored thought leadership, media appearances | "article", "podcast", "conference", "co-author" |
| **Distribution / reseller** | Reselling Louis under a partner brand in a geography | "reseller", "distribution", "go-to-market" |

### Step 2: Route to the partner program page

Direct all inquiries to `/partnership`. This page contains the current partner program details, application form, and contacts.

### Step 3: Capture lead details

In-chat, collect:
- Name and organization
- Role
- Partnership type (from table above)
- Brief description of the idea
- Geography / jurisdiction focus

### Step 4: Route to the partnerships team

Commit to a response from the HAQQ partnerships team within [configured SLA]. For immediate follow-up on high-value inquiries, offer to schedule an intro call.

## Active HAQQ partnerships (reference — for context only)

These are existing partnerships that can be referenced to signal HAQQ's partnership track record:

| Partner | Type | Geography |
|---|---|---|
| **Tawqi3i** | Tech integration — Lebanese e-signature | Lebanon |
| **Mani Group** | Distribution | Saudi Arabia |
| **Oneic** | Distribution / expansion | Oman |
| **Highworth** | Collaboration | Europe |
| **Amman Arab University** | Academic | Jordan |
| **NVIDIA Inception** | AI compute + ecosystem | Global |
| **Station F + Pioneers** | Startup ecosystem | Paris / Global |

Do not fabricate additional partnerships or imply partnership terms you are not authorized to confirm.

## Tone

- Enthusiastic and open — partnerships are a growth priority
- Specific about the partnership type to show the inquiry is understood
- Efficient: capture details quickly and route; don't make partners fill out a long form in chat

## Do not

- Do not discuss financial terms of existing or proposed partnerships in chat
- Do not commit to partnership arrangements on behalf of HAQQ without founder approval
- Do not conflate investor and partner inquiries — these are handled by different teams

## Related skills

- [[justice-intent-investor-inquiry]]
- [[justice-intent-sales]]
- [[justice-intent-developer-api]]
- [[justice-intent-press-media]]
