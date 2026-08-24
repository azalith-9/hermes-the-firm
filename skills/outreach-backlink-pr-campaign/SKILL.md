---
name: outreach-backlink-pr-campaign
description: Use when the legal AI product team needs to run a backlink acquisition and PR campaign to build domain authority, attract legal-professional audiences, and generate organic traffic. Covers campaign design, target publication identification, pitch copy, and follow-up sequencing for a legal-tech product operating primarily in MENA and international markets.
license: MIT
metadata: " id: outreach.backlink-PR-campaign category: outreach intent: ['__outreach__', 'backlinks', 'PR', 'SEO', 'legal-tech', 'growth'] related: - outreach-press-list-mena - outreach-press-list-europe - outreach-press-list-enriched - outreach-blog-preview-renderer - outreach-growth-agent-runner priority: P3 source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'outreach'.
Registered as a flat plugin skill.
-->


# Backlink PR Campaign

Backlinks from authoritative legal, tech, and business publications are the highest-leverage organic growth action for a legal AI product: they improve search ranking, build professional credibility, and drive direct referral traffic from the exact audience (lawyers, in-house counsel, legal operations professionals) who will evaluate and adopt the product.

## Purpose

Design and execute a PR-driven backlink campaign targeting:
1. Legal trade publications (primary — highest domain authority for the target audience)
2. Legal-tech and startup publications (secondary — growth community, investor awareness)
3. Regional business press in MENA and Europe (tertiary — market visibility)
4. Law school and bar association portals (niche — credibility with legal professionals)

## Inputs

| Input | Why it matters | Default |
|---|---|---|
| Product positioning | The angle of each pitch must match what you want the publication to say | "AI legal assistant built for MENA practice" |
| Target jurisdictions | Determines which publications and which beat journalists are relevant | UAE, KSA, Lebanon + UK/France secondary |
| Recent news hooks | PR pitches need a news angle — product launch, funding, partnership, landmark use case | Most recent milestone |
| Existing content assets | Backlinks require something to link to — blog post, research, tool, dataset | Skills library, blog |
| Team spokesperson | Journalists want a named person to quote | GC or founder |

## Campaign steps

### Step 1 — Audit existing backlinks

Before building new ones, know what you have:
- Run the domain through Ahrefs, Semrush, or Moz to see current referring domains, DR score, and anchor text distribution.
- Identify broken backlinks and reclaim them first (highest-ROI action).
- Identify competitor backlinks — which publications cover your competitors? Those are warm targets.

### Step 2 — Build the target list

Use [[outreach-press-list-mena]], [[outreach-press-list-europe]], and [[outreach-press-list-enriched]] to populate the outreach list with:
- Publication name and URL
- Journalist name and beat
- Recent articles on relevant topics (personalise the pitch)
- Contact email or submission form
- Domain Rating (DR) and monthly traffic estimates

Prioritise: DR 50+ publications first; legal trade press over general tech press for conversion quality.

### Step 3 — Develop the pitch angles

Different publications need different angles:

| Audience | Angle | Hook |
|---|---|---|
| MENA legal press (e.g., Law.com MENA, Lexology) | First AI tool built natively for MENA legal practice | "75% of Gulf legal disputes involve multi-jurisdiction issues — here's how AI changes that" |
| Legal-tech press (e.g., Legaltech News, Legal Futures) | Open-source legal AI skills library | "We published 200 reusable legal AI skills — free" |
| Regional business press (e.g., Arabian Business, L'Orient Today) | GC productivity and cost story | "The $500/hr problem: how AI cuts legal overhead for fast-growing MENA companies" |
| Law school portals | Educational resource | "Free legal AI skills library for law students and new associates" |

Each pitch: 3–4 sentences. Subject line under 60 characters. Named journalist. Personal hook referencing their recent work.

### Step 4 — Create linkable assets

A backlink campaign without linkable assets is a press release campaign (low conversion). Build:
- **Research report**: MENA legal AI adoption survey, or a multi-jurisdiction comparison study (the skills library is source material)
- **Free tool**: a public-facing version of a specific skill (non-compete checker, NDA analyser)
- **Data**: if usage data can be shared without privacy issues, "X thousand legal questions answered across MENA" is a newsworthy number
- **Expert commentary**: founder/GC bylines placed in target publications

### Step 5 — Outreach and follow-up sequence

| Day | Action |
|---|---|
| D0 | Send initial pitch email — personalised, concise, with the linkable asset linked |
| D7 | One follow-up if no response — 2 sentences, new angle |
| D14 | Final attempt — offer an alternative (quote, data point, expert comment) if they won't run the full story |
| D21 | Move to "inactive" list; try again in 3 months with new hook |

Response rate benchmarks: cold outreach to journalists = 5–15%; warm (referral or prior coverage) = 25–40%.

### Step 6 — Track and measure

| Metric | Target | Tool |
|---|---|---|
| New referring domains / month | 5–10 for an early-stage campaign | Ahrefs / Semrush |
| Domain Rating change | +2–5 DR / quarter | Ahrefs |
| Referral traffic from PR links | Track in analytics | GA4 / PostHog |
| Anchor text distribution | Branded + natural language mix; avoid over-optimised exact-match | Ahrefs |

## Quality bar

- Never submit generic or AI-generated pitches without personalisation — journalists delete them instantly.
- Always verify journalist contact details before sending — outdated contacts waste outreach budget.
- A placed article with a do-follow link from a DR 70+ legal publication is worth more than 50 directory links.

## What to avoid

- **Link farms and directories**: low-quality backlinks can harm domain authority.
- **Over-optimised anchor text**: "best legal AI MENA" as anchor text from 20 sources triggers a penalty.
- **Paid links** without disclosure: violates Google Webmaster Guidelines and creates reputational risk in a professional services context.
- **Pitching without an asset**: "we have a product" is not a pitch.

## Related skills

- [[outreach-press-list-mena]]
- [[outreach-press-list-europe]]
- [[outreach-press-list-enriched]]
- [[outreach-blog-preview-renderer]]
- [[outreach-growth-agent-runner]]
