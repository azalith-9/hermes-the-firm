---
name: openclaw-contrib-template
description: Use when a contributor (lawyer, developer, or legal researcher) wants to author a new legal AI skill for the OpenClaw public registry. Defines the exact contribution workflow — fork, template, PR, lawyer review, merge, versioning, and attribution — plus the CC-BY-SA licensing terms that govern all community skills.
license: MIT
metadata: " id: openclaw.contrib-template category: openclaw priority: P2 intent: [openclaw, contribution, skill-authoring, community, registry] related: [openclaw-public-skill-registry, openclaw-eval-harness-shared, openclaw-skill-portability-claude-codex-gemini] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'openclaw'.
Registered as a flat plugin skill.
-->


# OpenClaw — Contribution Template

## Purpose

OpenClaw is the open-source layer of the HAQQ Legal AI skill ecosystem. Community members — lawyers, developers, legal researchers, and law students — can contribute legal AI skills that are reviewed, versioned, and published to the public registry. This skill defines the exact process for doing so.

## Contribution workflow

### Step 1 — Fork the registry repository

Fork `github.com/sboghossian/mini-hermes-the-firm`. Work in a feature branch named `skill/<your-skill-id>` (e.g., `skill/draft-mou-uae`).

### Step 2 — Create the skill file

Skills live under `skills/<category>/<skill-id>/SKILL.md`. Create that directory and file. Use the standard SKILL.md frontmatter template:

```markdown
---
name: openclaw-contrib-template
description: <1-4 sentences, third-person, routing-focused. Start with "Use when…">
license: MIT
metadata:
  id: <category.slug>
  category: <one of: draft | review | kb | research | conversation | router | connector | ops | onboarding | output | ...>
  practice_area: <omit for non-substantive skills>
  jurisdictions: [<LB | KSA | UAE | DIFC | ADGM | QFC | EG | FR | UK | US | EU | OHADA | GCC | __multi__>]
  priority: <P0 | P1 | P2 | P3>
  intent: [<2–6 routing keywords>]
  related: [<related-skill-slugs>]
  source: <your name or org + link if applicable>
  version: "1.0"
---

# Human-Readable Title

[body — see structure guide below]
```

### Step 3 — Write the body

The body length target is 120–320 lines of genuinely useful content. Choose the structure that fits the category:

- **Drafting skills**: When to use / Required inputs / Document structure / Jurisdictional notes / Drafting standards / Common mistakes / Related skills
- **Review / analysis**: When to use / Inputs / Review methodology / What to flag / Output format / Jurisdictional notes / Limits & escalation / Related skills
- **Knowledge packs**: Scope / substantive reference content / How to use / Caveats & currency
- **Conversational / behavioral**: When this applies / Behavior / Examples / Edge cases / Do not / Related skills

Quality bar — non-negotiable:
- Every sentence must add information a practitioner would act on.
- Do not fabricate statute numbers, article numbers, or case citations.
- If your skill covers MENA jurisdictions, distinguish civil-law (LB, KSA, UAE-onshore, EG, FR) from common-law (DIFC, ADGM, UK) handling.
- Include `[[wikilink]]` cross-references to related skills using `category-slug` form.

### Step 4 — Submit a pull request

Open a PR from your feature branch against `main`. The PR description must include:

- **Skill category and practice area**
- **Jurisdictions covered**
- **Brief rationale**: what gap this fills
- **Reviewer recommendation**: suggest a lawyer (by jurisdiction/practice area) if you know one in the community

### Step 5 — Lawyer review

Every skill that touches substantive law requires sign-off from at least one admitted lawyer in a covered jurisdiction before merge. The review process:

- Reviewer comments directly in the PR on any factual, statutory, or jurisdictional issue.
- Author revises and re-requests review.
- Reviewer approves or escalates to a second reviewer.
- Turnaround target: 14 days for community reviewers; expedited for HAQQ-seed skills.

Non-substantive skills (ops, tooling, formatting, connector) do not require lawyer review but still require a maintainer technical review.

### Step 6 — Merge and version

On merge the skill receives a canonical version (`"1.0"`). Subsequent updates increment following semver-lite conventions:

- Patch (`1.0 → 1.0.1`): typo, minor wording correction, non-substantive.
- Minor (`1.0 → 1.1`): adds a jurisdiction, new section, or expands substantive content.
- Major (`1.0 → 2.0`): rewrites core guidance, changes the skill's primary behavior.

### Step 7 — Author credit

The contributor's name (or GitHub handle, if preferred) is added to the skill's `source` field and to the registry author index. Attribution persists through all subsequent versions.

## Licensing

All community-contributed skills are published under **CC-BY-SA 4.0** (Creative Commons Attribution-ShareAlike 4.0 International). This means:

- Anyone may use, adapt, and redistribute the skill.
- Derivative works must carry the same CC-BY-SA licence.
- Attribution to the original author(s) is required.

The underlying software and tooling of the OpenClaw registry is MIT-licensed.

## What makes a good contribution

| Strong contribution | Weak contribution |
|---|---|
| Covers a specific jurisdiction with named statutes/frameworks | Generic advice not tied to any legal system |
| Fills a gap not already covered by an existing skill | Near-duplicate of an existing skill |
| Written by or reviewed by someone with relevant practice experience | Pure AI-generated content without practitioner review |
| Includes concrete examples, thresholds, or checklists | Vague guidance that could mean anything |
| Correctly cross-references related skills | No cross-references |

## What not to submit

- Content that provides personalized legal advice rather than practitioner guidance.
- Skills whose factual claims you cannot verify (statute numbers, case citations) — omit such claims rather than guess.
- Skills that are brand-marketing for a specific firm or product.
- Duplicate skills — check the registry search before authoring.

## Related skills

- [[openclaw-public-skill-registry]] — the registry that houses all contributed skills
- [[openclaw-eval-harness-shared]] — test your skill against the shared evaluation harness before submitting
- [[openclaw-skill-portability-claude-codex-gemini]] — adapt your skill for multiple AI providers
