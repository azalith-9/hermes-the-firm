---
name: pillar-legal-skills-authoring
description: Internal architectural principle establishing that legal skills are first-class artifacts — each skill is a versioned, reviewable markdown file with structured frontmatter. Use when designing the skill authoring workflow, reviewing skill quality, or understanding how skills are loaded, routed, and updated in the Louis system.
license: MIT
metadata: " id: pillar.legal-skills-authoring category: pillar jurisdictions: [__multi__] priority: P3 intent: [__internal__] related: [pillar-architectural-bet-no-fine-tuning, pillar-context-across-apps, pillar-live-data-mcp, eng-skill-registry, router-skill-selector] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'pillar'.
Registered as a flat plugin skill.
-->


# Architectural Pillar: Legal Skills Authoring

## Scope

This pillar defines the principle that **skills are the primary unit of legal knowledge** in the Louis system. Each skill is a standalone markdown file with structured YAML frontmatter. Skills are versioned, peer-reviewable by lawyers, swappable without code changes, and composable at runtime.

This principle is what makes the no-fine-tuning bet (see [[pillar-architectural-bet-no-fine-tuning]]) executable: the skill library is the expert knowledge layer.

---

## The principle

> Skills are first-class artifacts. Each skill = one markdown file with frontmatter. Versioned, reviewable, swappable.

---

## What a skill is

A skill is a markdown file that encodes **one unit of legal expert behavior** — either a piece of substantive legal knowledge, a behavioral rule, a document template, a workflow, or a persona. Every skill has:

1. **YAML frontmatter** — machine-readable metadata for routing, discovery, and version management
2. **A body** — human-readable expert content that instructs the model on how to handle the skill's domain

The frontmatter schema:
```yaml
---
name: pillar-legal-skills-authoring
description:   [1-4 sentences for routing — "Use when…"]
license:       MIT
metadata:
  id:          [dot-notation original id, e.g., draft.NDA-unilateral]
  category:    [draft | review | kb | persona | router | pillar | eng | …]
  practice_area: [corporate-commercial | employment | arbitration | …]
  jurisdictions: [LB | UAE | DIFC | KSA | EG | FR | UK | US | __multi__ | …]
  priority:    [P0 | P1 | P2 | P3]
  intent:      [routing keywords]
  related:     [list of related skill names]
  source:      [provenance note]
  version:     "x.y"
---
```

---

## Why skills as files

### Version control
Skills stored as files live in git. Every change is a diff. A lawyer can review a skill change the same way an engineer reviews a code change. History is preserved. Bad changes are reversible.

### Separation of concerns
Legal knowledge lives in skill files; model behavior lives in the foundation model; routing logic lives in the router. Each concern can be changed independently. Updating a skill does not require redeploying the model.

### Peer review
A subject-matter expert (e.g., a Lebanese law specialist) can review and approve changes to skills covering Lebanese law without needing to understand the underlying ML infrastructure. The review workflow is the same as code review.

### Composability
Multiple skills can be loaded into a single prompt at runtime. A user asking about an NDA in Lebanon might trigger: `draft-nda-unilateral` + `kb-lob-contracts-lebanon` + `persona-partner-mode` + `heuristic-no-us-style-boilerplate-in-civil-law-jx`. The router selects and composes.

### Discovery and coverage tracking
Because every skill has frontmatter, the system can generate a complete inventory of covered practice areas, jurisdictions, and document types — and, by inversion, identify gaps where no skill exists.

---

## Skill categories

| Category | Purpose |
|----------|---------|
| `draft` | Produce a specific legal document |
| `review` | Analyze and risk-flag a document |
| `kb` | Reference knowledge pack (law, thresholds, procedures) |
| `persona` | Define a user-type behavior profile |
| `router` | Routing, orchestration, triage logic |
| `heuristic` | A behavioral rule applied across many skills |
| `pillar` | Architectural principles (this category) |
| `prompt-pack` | Prompt templates from the prompt library |
| `eng` | Engineering/technical notes |
| `workflow` | Multi-step matter workflows |
| `output` | Output format specifications |
| `conversation` | Conversational behavior rules |
| `safety` | Safety and compliance guardrails |

---

## Skill quality standard

A skill should be:
- **Precise enough to be acted on**: every sentence must add information the model will use. No padding.
- **No wider than one topic**: a skill for NDA drafting should not also contain advice on employment contracts. Composability requires granularity.
- **Jurisdiction-specific where needed**: a generic skill is acceptable for widely shared principles; jurisdiction-specific details belong in jurisdiction-specific skills or in a jurisdictional notes section.
- **Accurate**: no fabricated statute numbers or case citations. Where uncertain, say so explicitly.
- **Interlinked**: related skills should be cross-referenced with `[[wikilinks]]` so the skill set is a navigable graph.

Thin skills (one or two sentences) are almost never useful as skills — they become useful only when expanded to real depth. The quality bar is: would a competent practitioner find this genuinely helpful?

---

## Skill lifecycle

```
Author (lawyer + engineer) → Draft skill → Peer review (SME lawyer) → 
Merge to main → Router picks up → Runtime use → Feedback / issue logged → 
Update skill → Review → Merge
```

Skills are never "done" — they are maintained like living documents. The legal landscape changes; skills must change with it.

Priority levels signal maintenance urgency:
- **P0**: mission-critical; must be accurate and current; reviewed quarterly
- **P1**: high-value; reviewed semi-annually
- **P2**: useful; reviewed annually or on-demand
- **P3**: supporting/internal; reviewed when foundational assumptions change

---

## How the router uses skills

The router (see [[router-skill-selector]]) matches the user's request against skills by:
1. Matching `intent` keywords against the request
2. Filtering by `jurisdictions` if jurisdiction is known from context
3. Filtering by `practice_area` if the matter area is known
4. Ranking by `priority`
5. Loading the top N matching skills into the prompt context

The `description` field is the most important routing signal — it must accurately answer "when should this skill be used?"

---

## Caveats

The skill-as-file approach works well for a skill library of hundreds to low thousands of skills. At very high scale (tens of thousands), indexing and retrieval become engineering concerns. See [[eng-skill-registry]] for the registry implementation.

---

## Related skills

- [[pillar-architectural-bet-no-fine-tuning]] — why skills replace fine-tuning
- [[pillar-context-across-apps]] — how skills declare and consume matter context
- [[pillar-live-data-mcp]] — live data as a complement to static skill knowledge
- [[eng-skill-registry]] — engineering implementation: how skills are indexed and loaded
- [[router-skill-selector]] — how the router selects and composes skills at runtime
