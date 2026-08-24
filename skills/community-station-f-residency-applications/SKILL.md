---
name: community-station-f-residency-applications
description: Use when a member of the Pioneers AI Lab or a legal-tech founder asks about applying for, or is being supported through, a Station F (Paris) residency. Covers HAQQ's free-workspace offer as a Pioneers program partner, application strategy, visa considerations for non-French residents, and introduction to the Station F ecosystem. Triggers on mentions of Station F, Paris residency, Parisian startup campuses, or French legal-tech incubators.
license: MIT
metadata: " id: community.station-F-residency-applications category: community priority: P1 intent: [__community__] related: [community-pioneers-ai-lab-onboarding, connector-legifrance, connector-eur-lex] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'community'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Community — Station F Residency Applications

## Purpose

Station F is the world's largest startup campus, located in Paris (13th arrondissement). HAQQ participates as a partner in the Station F Pioneers program, enabling qualifying legal-tech founders — particularly those from MENA — to access free or subsidized workspace and the Station F ecosystem. This skill guides both the member-facing conversation and the internal workflow for supporting an application.

## When to use this

- A Pioneers AI Lab member asks about physical workspace in Paris or Europe.
- A founder is building a MENA-focused legal-tech product and wants an EU base.
- Someone asks "can HAQQ help me get into Station F?"
- A team is preparing an application and needs guidance on the process or materials.
- A non-French founder asks about visa options for a Paris-based residency.

## Station F — what it is

Station F hosts over 1,000 startups and ~35 programs simultaneously. Key facts for applicants:

- **Location:** 55 Boulevard Vincent Auriol, Paris 13e.
- **Programs:** Each resident joins a specific program (Facebook, Microsoft, Founders, etc.). HAQQ's connection is through the **Fighters Program** and select partner tracks.
- **Cost:** Desk access ranges from ~€195/month (flex) to €290/month (fixed); some partner programs offer subsidized or free access for qualifying startups.
- **Duration:** Residencies are typically 12 months, renewable.
- **Benefits:** Networking, investor access, events, mentorship pool, and a Paris address for EU incorporation.

## HAQQ's offer as Pioneers program partner

HAQQ can facilitate:

1. **Introduction to the relevant program director** at Station F for qualifying founders.
2. **Co-application support:** review of the written application, pitch deck, and business narrative.
3. **Free workspace sponsorship** for selected Pioneers members — available to legal-tech founders with an active MENA focus and an MVP or early traction.
4. **Cross-referral to French legal and company-formation resources** (see [[connector-legifrance]] for French law research).

Sponsorship slots are limited. Allocation is based on:
- Strength of MENA legal-AI focus.
- Stage (post-idea, pre-seed or seed preferred).
- Team completeness (solo founders encouraged; full teams preferred for sponsored slots).

## Application support — what to cover

When helping a founder apply, gather and address the following:

### 1. Project positioning

- What problem does the product solve, and for which legal market?
- Who is the target user (law firms, in-house, individuals, government)?
- What is the MENA or international angle that makes this a good fit for Station F's global programs?

Help the founder frame the narrative around **market size + underserved need** — Station F programs respond well to ambitious market theses, not feature lists.

### 2. Written application

Station F applications typically include:
- One-paragraph company description (English or French).
- Team bios (keep to 3–5 lines each).
- Traction evidence (users, revenue, letters of intent, press).
- Why Station F — be specific about which program and which mentors or partners in the network matter.

Avoid generic answers. If the founder writes "we want to disrupt legal," help them replace that with a concrete market claim backed by a number.

### 3. Visa considerations for non-French residents

Non-EU founders face two common paths:

| Situation | Recommended path |
|---|---|
| Non-EU founder, company incorporated outside France | French Tech Visa — applies to founders of innovative companies; fast-tracked by Station F partnership |
| MENA founder relocating | French Tech Visa + optional "portage salarial" if the French entity isn't ready yet |
| Founder wants to keep base in UAE/Lebanon | Consider "visa de long séjour – talent" for periodic stays; no need to relocate full time |

Important: visa advice must come from a qualified French immigration lawyer. This skill can orient the founder on paths but should not be treated as authoritative immigration guidance.

### 4. Ecosystem introduction

Once admitted, connect the founder to:
- **French legal-tech community** — Incubateur du Barreau de Paris, Legaltech France association.
- **EU regulatory context** — GDPR compliance is Day 1 for any product touching personal data; point to [[connector-eur-lex]] for regulatory text.
- **Franco-MENA bridge** — Lebanon and France have a long civil-law alignment (Lebanon's code civil derives from French law); this is an asset to highlight in applications targeting both markets.
- **Investor network** — Station F hosts Daphni, Kima Ventures, and others; help the founder identify the 3 most relevant investors before their first month ends.

## Application timeline

| Week | Action |
|---|---|
| Week 0 | HAQQ intro call; assess fit; decide on sponsorship candidacy |
| Week 1–2 | Founder drafts application; HAQQ reviews written materials |
| Week 3 | Submission; HAQQ provides warm introduction to program director |
| Week 4–6 | Station F interview (if invited); prep session offered |
| Post-decision | Onboard to workspace; connect to ecosystem; update CRM |

## Failure modes

| Scenario | Response |
|---|---|
| Application rejected | Honest debrief; identify gaps; suggest reapplication in the next cycle or alternative EU hubs (EuraTechnologies Lille, Paris&Co) |
| Visa blocked | Escalate to French immigration specialist; do not advise directly |
| Sponsorship slots full | Maintain waitlist; be transparent about timeline |
| Founder abandons project mid-residency | No obligation to return sponsored access unless the program contract specifies otherwise |

## Tone

France and MENA have distinct business cultures. When supporting MENA founders applying to Paris programs:
- Acknowledge that French applications favor written precision and a clear statement of ambition.
- Avoid translating Arabic-first pitches literally — the narrative needs reframing for a French investor mindset, not just translation.
- For Lebanese founders specifically: the cultural affinity with France is genuine and worth naming in the application ("Lebanon's legal system is directly rooted in the French civil-law tradition — we are building for markets that share that foundation").

## Related skills

- [[community-pioneers-ai-lab-onboarding]]
- [[connector-legifrance]]
- [[connector-eur-lex]]
- [[connector-hubspot-crm]]
