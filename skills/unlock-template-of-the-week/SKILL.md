---
name: unlock-template-of-the-week
description: Use when generating or scheduling the weekly featured legal template surface — a curated clause, document template, or workflow tied to a current legal trend or seasonal event, surfaced every Monday to engaged users across all personas. This skill governs editorial selection, copy format, tie-in to the outreach blog calendar, and delivery mechanics.
license: MIT
metadata: " id: unlock.template-of-the-week category: unlock jurisdictions: [__multi__] priority: P2 intent: [__customer-facing__, template-discovery, editorial, weekly-engagement] related: - unlock-skill-of-the-day - unlock-feature-discovery-by-persona - outreach-blog-preview-renderer source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'unlock'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Template of the Week

## Purpose

Each Monday, the platform surfaces one curated legal template — a clause, a full document draft, or a workflow — that is editorially selected to match a current legal trend, a seasonal event (DIFC new filing season, Ramadan contractual period, AGM season), or a jurisdictionally relevant topic.

The Template of the Week is an editorial product, not an algorithmic one. It is chosen by the editorial team (or by this skill when running in automated mode) based on the blog and outreach calendar maintained in [[outreach-blog-preview-renderer]].

## Template types eligible for selection

| Type | Description | Example |
|------|-------------|---------|
| Clause | A single contract clause with explanation and variants | Force majeure clause with MENA-adapted language |
| Document template | Full draft of a common legal document | Standard employment contract for UAE free zone |
| Playbook | A step-by-step workflow for a recurring legal task | M&A due diligence checklist for GCC targets |
| Jurisdiction guide | A reference note on a recent regulatory change | Summary of UAE Federal Decree-Law 33/2021 amendments |

## Editorial calendar tie-in

The template selection should align with the [[outreach-blog-preview-renderer]] calendar. If that week's blog post covers UAE corporate governance, the Template of the Week should be a related template (e.g., board resolution draft, articles of association review checklist).

This creates editorial coherence: users who read the blog, receive the newsletter, and see the in-app template are getting reinforcing signals about the same topic.

## Surfacing format

The in-app card appears at session start on Monday only, once per week. It should not interrupt mid-task interactions.

### Card structure

1. **Week label** — "Template of the Week — [Week of May 12, 2026]"
2. **Template name** — human-readable.
3. **Two-sentence description** — what it is and why it matters right now.
4. **Jurisdiction tags** — e.g., `UAE · DIFC · KSA`.
5. **CTAs** — [Use this template] [Preview] [Dismiss].

### Example card

> **Template of the Week — Week of May 12, 2026**
>
> **UAE Employment Contract — Free Zone Edition**
>
> A ready-to-customize employment agreement compliant with UAE Federal Decree-Law 33/2021 and JAFZA free zone regulations. Relevant now as the Q2 hiring season peaks and businesses onboard new staff ahead of summer.
>
> `UAE · JAFZA · GCC`
>
> [Use this template] [Preview] [Dismiss]

## Selection criteria

When generating or selecting the week's template, apply these criteria in order:

1. **Timeliness** — does it connect to a current trend, a regulatory change from the past 90 days, or a seasonal legal event?
2. **Breadth** — will it be relevant to at least two of the five personas?
3. **MENA-first** — MENA-jurisdiction templates are preferred over generic international ones. If a global template is selected, it must include a MENA-specific section or adaptation note.
4. **Quality** — the underlying skill must be `drafted` status or higher with substantive body content, not a stub.
5. **Non-repetition** — the same template should not appear within 12 weeks.

## Delivery mechanics

| Channel | Timing | Opt-in |
|---------|--------|--------|
| In-app card | Monday, session start | No (default on) |
| Email newsletter section | Monday morning digest | Yes |
| Blog post (via outreach calendar) | Monday | Yes (subscriber) |

## Coordination with Skill of the Day

On Mondays when the Template of the Week is active, [[unlock-skill-of-the-day]] should not also surface a card. Avoid stacking two "discovery" cards in a single session. The Template of the Week takes editorial precedence on Mondays; Skill of the Day resumes Tuesday.

## Metrics

| Metric | Target |
|--------|--------|
| Card open rate (Monday in-app) | > 25% |
| Template use rate (clicked and actually drafted) | > 15% of openers |
| Email click-through | > 10% |

## Related skills

- [[unlock-skill-of-the-day]]
- [[unlock-feature-discovery-by-persona]]
- [[outreach-blog-preview-renderer]]
- [[unlock-whitepaper-when-evaluating]]
