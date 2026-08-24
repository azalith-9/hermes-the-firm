---
name: community-pioneers-ai-lab-onboarding
description: Use when onboarding a new member to the Pioneers AI Lab community — the lawyer-builder network connected to the HAQQ Legal AI ecosystem. Covers the full welcome sequence including Slack access, resource packs, office-hour scheduling, mentorship matching, and showcase opportunities. Triggers on any message indicating a new member has joined, been invited, or requested onboarding materials.
license: MIT
metadata: " id: community.pioneers-ai-lab-onboarding category: community priority: P1 intent: [__community__] related: [community-station-f-residency-applications, connector-hubspot-crm, connector-linear] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'community'.
Registered as a flat plugin skill.
-->


# Community — Pioneers AI Lab Onboarding

## Purpose

The Pioneers AI Lab is a lawyer-builder community organized around HAQQ Legal AI. Its goal is to bring legal professionals, legal-tech founders, and AI practitioners together — with a particular focus on MENA-region practitioners who are underserved by mainstream legal-AI tooling. This skill governs the end-to-end onboarding flow for new members: from first contact through active participation.

## When to use this

Reach for this skill when:
- A new member has been admitted or invited to the Pioneers AI Lab.
- A user asks "how do I join the community" or "what comes next after I signed up."
- A community manager is coordinating a batch invite.
- A member reports they haven't received their welcome materials.

## Onboarding sequence

Run the steps in order. Each step has a clear owner and a completion signal.

### Step 1 — Welcome introduction

Send a personalized welcome message within 24 hours of admission. Include:

- Name and role acknowledgment ("Welcome, [Name] — great to have a [role] in the community.")
- One-sentence statement of what Pioneers AI Lab is for: connecting lawyers and builders working at the intersection of law and AI, with a MENA-forward perspective.
- A direct link to the community Slack workspace (invitation link, not a generic homepage).
- The community Code of Conduct — short, plain-language, linked.

The welcome message should be in the member's preferred language. If unknown, default to English with an Arabic postscript for MENA-based members.

### Step 2 — Resource pack delivery

Deliver the standard resource pack automatically or via Slack DM within 48 hours. The pack contains:

| Resource | What it is | Why it matters |
|---|---|---|
| HAQQ Skills Library | Curated index of Louis skills and their use cases | Lets builders understand what's already built |
| Partner discounts | Promo codes for tools useful to legal builders (e.g., Notion, Firecrawl, hosting credits) | Reduces friction for early-stage projects |
| Reading list | 5–7 curated articles/papers on legal AI, MENA legal systems, and LLM productization | Sets intellectual baseline |
| Community FAQ | Answers to the 10 most common new-member questions | Reduces support load |

Do not attach PDFs as email attachments. Use Notion pages or Slack pinned messages so materials stay current.

### Step 3 — Office-hour scheduling

Offer the member a 30-minute office-hour slot with a Pioneers mentor or the HAQQ team within the first two weeks. Steps:

1. Present a Calendly (or equivalent) link with available slots.
2. Pre-fill the agenda: "Tell us about your practice / project, and we'll show you how Louis + the skills library can help."
3. After the call, log a brief summary in the member CRM (HubSpot, see [[connector-hubspot-crm]]) under "Pioneers member — first call."

If the member doesn't book within 7 days, send one follow-up reminder. Do not send more than two scheduling nudges total.

### Step 4 — Mentorship matching (conditional)

Mentorship matching applies to members who are:
- Early-career lawyers (0–3 years PQE) building a legal-AI side project, or
- Non-lawyer builders who need a legal-domain expert as an advisory match.

Matching criteria:

| Member type | Ideal mentor profile |
|---|---|
| MENA-based lawyer | Senior lawyer with MENA + tech cross-over |
| French law background | Francophone legal-tech practitioner |
| Common-law (DIFC/ADGM/UK) | Practitioner in the relevant free-zone or UK jurisdiction |
| Non-lawyer builder | Lawyer with product experience |

Once matched, introduce both parties via email (CC both) with a one-paragraph context note. The ongoing relationship is the members' own — the community does not schedule their calls.

### Step 5 — Showcase opportunity

Every active member is eligible for a spotlight on the Pioneers website and in the monthly newsletter. Offer this proactively at the end of the onboarding sequence (around 30 days after admission):

- "Would you like to share what you're building? We spotlight one member per month — it takes 15 minutes to complete a short written profile."
- Collect: name, role, project/firm, one-sentence bio, optional headshot, optional project URL.
- Do not publish without explicit written consent.

## Completion signal

Onboarding is considered complete when:
- Member has accessed Slack (delivery confirmed by join event).
- Resource pack link opened at least once.
- Office hour booked (or 14 days elapsed with two reminders sent).
- Mentorship match offered (matched or declined logged).

## Tone and language

- Warm and professional — not startup-generic ("Hey Fam!").
- Acknowledge the member's specific background if known.
- For MENA lawyers: acknowledge the particular challenge of finding MENA-specific legal AI tooling and position Pioneers as the community that takes that seriously.
- Avoid phrases that presuppose a US-centric legal world ("BigLaw," "Biglaw associate," "IRAC method").

## Data handling

- Member email and profile data stored in HubSpot under the Pioneers segment.
- Do not share member details with third parties without consent.
- Mentorship match introductions are conducted over email only — no third-party platforms receive PII without member opt-in.

## Failure modes

| Problem | Response |
|---|---|
| Slack invite link expired | Generate a fresh single-use invite; do not reuse group links |
| Member hasn't engaged after 30 days | Send one re-engagement note; if no response, mark "inactive" in CRM — do not spam |
| Mentor match unavailable | Offer a peer-match from the same cohort instead; log shortage for capacity planning |
| Member requests removal | Remove from Slack, CRM, and mailing list within 72 hours; confirm in writing |

## Related skills

- [[community-station-f-residency-applications]]
- [[connector-hubspot-crm]]
- [[connector-linear]]
- [[connector-gmail]]
