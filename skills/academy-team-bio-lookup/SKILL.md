---
name: academy-team-bio-lookup
description: "Use when surfacing HAQQ team bios on demand — founder, leadership, advisors, and key hires — typically for partner pages, event speaker profiles, press inquiries, investor materials, or in-product 'meet the team' screens. Returns a structured bio with role, background summary, and (where available) LinkedIn reference. Calibrated to the audience: investor bio differs from press bio which differs from conference speaker card."
license: MIT
metadata: " id: academy.team-bio-lookup category: academy jurisdictions: [__multi__] priority: P3 intent: [__customer-facing__, team, bios, about-us] related: [academy-company-bio, academy-partnership-pitch, academy-vc-program-pitch] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'academy'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Team Bio Lookup — HAQQ Leadership and Advisor Profiles

## When to use this

Invoke when:
- A partner page or website needs team bio cards
- An investor asks "who is behind HAQQ?"
- An event organizer needs a speaker bio for a HAQQ team member
- A press inquiry requires a founder or leadership quote attribution
- An in-product "About" screen needs team profiles

## Bio structure — standard format

Each team bio should contain:

| Field | Description |
|---|---|
| Name | Full name |
| Title | Current role at HAQQ |
| Photo | Reference to photo asset (if available) |
| Short bio (50–75 words) | Role summary, relevant background, why they are at HAQQ |
| Long bio (150–200 words) | Career arc, key achievements, HAQQ focus area, personal anchor |
| LinkedIn | Profile URL |
| Audience variant | Investor / Press / Partner / Conference |

## Bio categories

### Founders and C-Suite
The core leadership team building HAQQ. Bios in this category should emphasize:
- Domain expertise (legal, technology, MENA market)
- Founding story and mission motivation
- Specific jurisdictional or technical depth
- Prior company-building or legal-practice experience

### Advisors
HAQQ's advisor network includes legal practitioners, technologists, and regional market experts. Advisor bios should:
- Highlight the specific area of advisory contribution (e.g., "MENA regulatory strategy", "AI infrastructure", "bar association relations")
- Note the advisor's primary affiliation (law firm, university, company)
- Be shorter than founder bios: 50–100 words for most contexts

### Key Hires
Senior hires in product, engineering, legal, and operations. Bios should:
- Focus on what the individual brings to HAQQ's specific growth phase
- Mention notable prior experience briefly
- Keep length proportionate to seniority

## Tone guidelines by audience

| Audience | Tone | Emphasis |
|---|---|---|
| Investor / VC | Confident, track-record-focused | Prior experience, domain depth, execution credibility |
| Press / Journalist | Accessible, quotable | Founding story, mission, MENA context |
| Partner / BD | Professional, collaborative | Relevant expertise, relationship-building background |
| Conference / Event | Engaging, punchy | Key credential + hook for the audience |
| In-product / Users | Warm, human | Why this person cares about legal access |

## What to exclude from all bios

- Do not include personal information beyond what the individual has publicly shared (no home city, no personal family details)
- Do not fabricate credentials, positions, or dates
- Do not describe advisors as "employees" or "team members" if they are advisors
- Do not include any financial information (compensation, equity) in any public-facing bio

## Keeping bios current

Bios should be reviewed and updated:
- When a team member's title or role changes
- When a significant new achievement or milestone is announced (funding round, award, publication)
- At least annually for active team members and key advisors

## Related skills

- [[academy-company-bio]]
- [[academy-partnership-pitch]]
- [[academy-vc-program-pitch]]
