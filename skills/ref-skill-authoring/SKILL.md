---
name: ref-skill-authoring
description: Use as a reference guide for authoring new skills for the Louis / mini-hermes-the-firm skill library — covering how to identify a genuine skill gap, choose the right category, define intent keywords for router pickup, set priority, write the frontmatter and body, cross-link with wikilinks, test routing, and iterate. Follow this guide precisely to ensure new skills integrate correctly with the router and maintain the quality bar of the library.
license: MIT
metadata: " id: ref.skill-authoring category: ref priority: P1 intent: [__ref__, skill-authoring, skill-creation, platform, meta] related: - ref-anti-patterns - ref-verification - ref-setup-checklist - ref-mcp-hardening source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'ref'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Reference — Skill Authoring Guide

## Scope

This guide is for anyone creating new skills for the Louis / mini-hermes-the-firm skill library — whether a legal AI engineer, a practising lawyer contributing domain expertise, or a contributor to the open-source repository. It covers the complete skill authoring process from identifying a gap through to router validation.

---

## Step 1 — Identify a genuine gap

Before authoring a new skill, confirm that no existing skill already covers the use case:

1. Search the skill library by category and intent keywords: does a skill exist that handles this task?
2. Check related skills: would adding a section or sub-skill to an existing skill be better than creating a new one?
3. Is the gap meaningful? A skill that is only marginally different from an existing skill dilutes the library and confuses the router. New skills should address a distinct use case that the router cannot currently handle well.

**Gap test:** "If I search for this use case in the library, will I find a relevant skill? If yes, I don't need a new skill — I may need to improve the existing one."

---

## Step 2 — Choose the right category

Category determines the skill's routing behavior, its expected body structure, and which other skills it will appear alongside. Choosing the wrong category is the most common authoring error.

| Category | When to use |
|---|---|
| `draft` | Skills that produce a drafted document (contract, policy, letter, pleading) |
| `prompt-pack` | Lightweight prompt templates for common drafting or analysis tasks; shorter than full draft skills |
| `review` | Skills for reviewing, redlining, or analyzing an existing document |
| `eval` / `intel` | Research and analysis skills; not producing a document |
| `kb` | Knowledge pack — substantive reference content by topic and jurisdiction |
| `ref` | Meta-reference skills about the platform, workflow, or quality control |
| `public-tool` | Free-tier public-facing tools (NDA generator, contract summarizer, etc.) |
| `heuristic` | Short behavioral rules that apply broadly across many tasks |
| `conversation` / `safety` | Behavioral and safety guardrails |
| `router` | Routing and orchestration logic |

---

## Step 3 — Define intent keywords

Intent keywords are how the router finds the skill. They must be:
- **Specific enough** to distinguish this skill from similar ones: `trademark-license-agreement` not just `trademark`
- **Plural enough** to catch the common ways a user might phrase the request: include the document type, the action (drafting, review, compliance), and the practice area
- **Consistent with naming conventions**: lowercase, hyphen-separated, no spaces

**Good intent keywords:**
```yaml
intent: [drafting, trademark-license-agreement, ip, trademark, licensing, royalty]
```

**Bad intent keywords** (too generic):
```yaml
intent: [ip, licensing]
```

**Rule:** At least one intent keyword should be the exact document type or task name, hyphenated. This is the primary routing signal.

---

## Step 4 — Set priority

| Priority | When to use |
|---|---|
| P0 | Core safety and compliance guardrails; never bypass |
| P1 | High-traffic foundational skills (NDA, employment contract, conflict check) |
| P2 | Standard practice-area skills; the majority of the library |
| P3 | Niche skills; long-tail use cases; not time-critical |

P0 and P1 skills are loaded eagerly into the router's priority index; P2 and P3 are available but not pre-loaded. This affects routing speed.

---

## Step 5 — Write the frontmatter

Follow the exact format from the ENRICHMENT_GUIDE.md:

```yaml
---
name: ref-skill-authoring
description: <1–4 sentences; start with "Use when…"; mention practice area, jurisdictions, and key triggers; max ~700 chars>
license: MIT
metadata:
  id: <category.slug format>
  category: <category>
  practice_area: <if applicable>
  jurisdictions: [<list>]
  priority: P0|P1|P2|P3
  intent: [<keyword list>]
  related: [<related skill names, converted to standard form>]
  source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm)
  version: "1.0"
---
```

**Description quality check:**
- Does it start with "Use when..." or a clear capability statement?
- Does it mention at least one specific jurisdiction?
- Does it mention the practice area?
- Is it under 700 characters?
- Would a router reading it know immediately whether this skill is relevant to a given query?

---

## Step 6 — Write the body

Apply the body structure for the skill's category from the Enrichment Guide. The key principles:

- **Every section must add information a practitioner would act on.** If a section cannot meet this test, cut it.
- **Length guidance:** 120–320 lines for most skills; thin sources need more expansion; rich sources need tightening
- **Preserve all legal substance** from the source: jurisdiction notes, thresholds, defaults, lists
- **MENA-first:** Contrast civil-law and common-law handling; flag the classic traps
- **No fabricated citations:** Never invent statute article numbers, case names, or pin-cites
- **Wikilinks:** Use `[[skill-name]]` cross-references throughout the body; use the standard name form (lowercase, hyphen-separated)

**Body section completeness check (for drafting skills):**
- [ ] When to use this
- [ ] Required inputs (table with "why it matters" and default)
- [ ] Optional inputs
- [ ] Document structure (numbered, clause by clause)
- [ ] Jurisdictional notes (table with MENA jurisdictions)
- [ ] Drafting standards
- [ ] Common mistakes
- [ ] Related skills

---

## Step 7 — Cross-link with wikilinks

Every skill must end with a `## Related skills` section. The wikilinks in this section are how the skill set stays interconnected.

**Format:**
```markdown
## Related skills

- [[prompt-pack-nda-unilateral]]
- [[kb-ip-mena]]
- [[heuristic-always-state-jurisdiction-first]]
```

**Rules:**
- Convert old-style ID format (`draft.NDA-unilateral`) to the new form (`draft-nda-unilateral`)
- Include 3–8 related skills; more is noise, fewer is unhelpful
- At least one wikilink should point to a more specific skill (narrower scope) and at least one to a more general skill (broader scope)

---

## Step 8 — Test routing

After writing the skill, verify that the router picks it up for the intended queries:

1. Write 5 test queries that should trigger this skill
2. Write 3 test queries that should NOT trigger this skill (they should trigger a different skill)
3. Run the test queries through the router; verify the results
4. If the skill is not triggered by the should-trigger queries: add more specific intent keywords; improve the description
5. If the skill is triggered by the should-not-trigger queries: narrow the intent keywords; check for overlap with existing skills

---

## Step 9 — Iterate based on eval results

After the skill has been used in real sessions:
- Review sessions where the skill was invoked: did the output quality meet the bar?
- Check for common user corrections after the skill output: these indicate gaps in the skill's required inputs or document structure
- Update the skill based on feedback; increment the version number

**Version control:** Skills are versioned (version: "1.0", "1.1", "2.0"). Minor improvements: increment minor version. Major restructuring or substantive legal update: increment major version. Add a brief change log comment in the YAML frontmatter if useful.

---

## Quick authoring checklist

- [ ] Gap confirmed: no existing skill covers this use case
- [ ] Category chosen correctly
- [ ] Intent keywords: at least one is the exact document/task name
- [ ] Priority set correctly
- [ ] Frontmatter complete and valid YAML
- [ ] Description: "Use when..." format; < 700 chars; mentions jurisdiction and practice area
- [ ] Body: correct structure for the category; 120–320 lines; no fabricated citations
- [ ] Jurisdictional notes: MENA jurisdictions addressed
- [ ] Common mistakes section
- [ ] Related skills section with wikilinks
- [ ] Router tested with 5 should-trigger and 3 should-not-trigger queries

---

## Related skills

- [[ref-anti-patterns]]
- [[ref-verification]]
- [[ref-setup-checklist]]
- [[ref-mcp-hardening]]
