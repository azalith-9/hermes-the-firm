---
name: wiki-skill
description: Use when a user asks about how the Louis / mini-hermes-the-firm skill library is organized, how to discover available skills, what categories exist, how skills are loaded and routed, or how to author new skills. Acts as a meta-reference for the skill system itself — useful for developers, legal engineers, and power users navigating the skill registry.
license: MIT
metadata: " id: wiki.skill category: wiki jurisdictions: [__multi__] priority: P3 intent: [__wiki__, skill registry, skill authoring, skill routing, skill categories] related: [wiki-topic, wiki-research, router-skill-dispatch] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'wiki'.
Registered as a flat plugin skill.
-->


# Skill Library Reference

## Scope

This pack is the meta-reference for the Louis / mini-hermes-the-firm skill library. It explains how skills are organized, discovered, loaded, and authored. Use it when navigating the registry, debugging skill routing, or authoring new skills.

The live index is maintained in `[[_REGISTRY.md]]`. This pack provides the conceptual framework behind it.

---

## What Is a Skill?

A skill is a self-contained, structured instruction pack that tells the AI how to handle a specific legal task with expert-level precision. Skills replace ad-hoc prompting with repeatable, auditable, expert-calibrated behaviors.

Each skill:
- Has a unique `id` in `category.slug` form
- Belongs to exactly one `category`
- Carries metadata for routing (intent, jurisdictions, priority)
- Contains a body of substantive guidance — methodology, quality bar, output format
- Is versioned and can be updated independently

---

## Category Taxonomy

| Category | Description | Examples |
|----------|-------------|---------|
| `draft` | Document drafting skills | NDA, employment contract, SPA |
| `review` | Contract review and risk analysis | MSA deep review, IP ownership check |
| `research` | Legal research and jurisdiction lookup | Licensing requirements, case law |
| `workflow` | Multi-step orchestrated task packs | Incorporation pack, due diligence pack |
| `wiki` | Knowledge reference packs (this category) | Space law, startup, VC |
| `kb` / `ref` | Deep knowledge bases on a practice area | AML/CTF, employment law |
| `heuristic` | Always-on behavioral rules | State jurisdiction first, no legal advice |
| `conversation` | Intake flows and conversational patterns | Employment contract intake |
| `router` | Skill routing and dispatch logic | PA workflow router |
| `output` | Output formatting preferences | Executive summary first |
| `efirm` | eFirm (practice management) integrations | Matter creation, time entry |
| `tool` | Calculator and utility tools | EOSG calculator |
| `eval` | Evaluation and quality checking | Hallucination detector |
| `safety` | Safety and compliance guardrails | Jurisdiction disclaimer |
| `persona` | AI persona definition | Louis voice, tone |

---

## Skill ID Naming Convention

```
<category>.<slug>[-<qualifier>]
```

Examples:
- `draft.NDA-mutual` — mutual NDA drafting skill
- `review.MSA-deep-review` — MSA deep review skill
- `workflow.startup-incorporation-pack` — startup incorporation workflow
- `wiki.research` — this pack

In the new SKILL.md format the `id` is in `category.slug` form in the frontmatter; wikilinks use the hyphenated form: `[[draft-nda-mutual]]`.

---

## How Skills Are Loaded

Skills are loaded by the router (`[[router-skill-dispatch]]`) based on:

1. **Intent matching** — user's message is matched against `intent` metadata fields
2. **Practice area** — matched against declared `practice_area`
3. **Jurisdiction** — filtered to skills covering the relevant jurisdiction
4. **Priority** — P0 skills load first; P3 load opportunistically
5. **Explicit invocation** — user or orchestrating workflow explicitly names a skill

Skills can also be loaded programmatically via workflow orchestrators (e.g., `[[workflow-startup-incorporation-pack]]` explicitly loads 10+ drafting skills in parallel).

---

## How to Author a New Skill

### Step 1 — Identify the gap

Look at the registry. Is there already a skill for this task? If yes, consider enriching it rather than adding a new one.

### Step 2 — Choose the right category

Use the taxonomy above. The category determines the file location and the body structure template to follow.

### Step 3 — Draft the frontmatter

```yaml
---
name: wiki-skill
description: <routing-focused, "Use when…", 1-4 sentences>
license: MIT
metadata:
  id: <category.slug>
  category: <category>
  practice_area: <if applicable>
  jurisdictions: [<list or __multi__>]
  priority: <P0|P1|P2|P3>
  intent: [<2-6 routing keywords>]
  related: [<related skill names>]
  source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm)
  version: "1.0"
---
```

### Step 4 — Write the body

Use the structure for your category (see ENRICHMENT_GUIDE.md). Minimum target: 120 lines of genuinely useful content. No padding; no `[INSERT X]` placeholders unless it is a fill-in template.

### Step 5 — Cross-link

Add `[[wikilink]]` references in the body to related skills. Update the registry.

### Step 6 — Review

- Does every claim hold up legally for the stated jurisdictions?
- Is the output format actionable?
- Are jurisdiction-specific traps flagged?
- Is the quality bar stated clearly?

---

## Priority Levels

| Level | Meaning | Loading behavior |
|-------|---------|-----------------|
| P0 | Critical, core workflow skills | Always loaded when task matches |
| P1 | Important, high-value skills | Loaded on task match |
| P2 | Useful, secondary skills | Loaded when context suggests it |
| P3 | Reference / wiki skills | Loaded on demand; not auto-pushed |

Wiki skills (this category) are typically P3 — they are reference material, not active task orchestrators.

---

## Skill Versioning

Skills use semantic versioning `major.minor`. Breaking changes (new required inputs, output format changes) increment the major version. Enrichments and corrections increment the minor version. The registry tracks the current version for each skill.

---

## How to Use This Pack

Reference this pack when:
- Exploring the skill library to find the right skill for a task
- Authoring or updating a skill
- Debugging why a skill was or was not loaded for a given prompt
- Training a new team member on the Louis skill architecture

---

## Caveats & Currency

The registry is a living document. Category taxonomy and naming conventions may evolve. Always consult `[[_REGISTRY.md]]` for the current authoritative list.

## Related Skills

- [[wiki-topic]]
- [[wiki-research]]
- [[router-skill-dispatch]]
- [[heuristic-always-state-jurisdiction-first]]
- [[output-executive-summary-first]]
