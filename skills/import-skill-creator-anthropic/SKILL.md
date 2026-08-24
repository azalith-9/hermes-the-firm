---
name: import-skill-creator-anthropic
description: Use when migrating a skill-creation or skill-authoring workflow originally built for the Anthropic the agent API into the mini-hermes-the-firm format. The adapter maps legacy Anthropic skill-generation prompts — SKILL.md templating, frontmatter generation, body structure selection, and quality validation — into the standard skill model for the open-source repository. Triggers when importing a prompt-engineering or skill-factory tool from an Anthropic-native context.
license: MIT
metadata: " id: import.skill-creator-anthropic category: import jurisdictions: [__multi__] priority: P3 intent: [__import__, skill-creator, skill-authoring, migration, anthropic, prompt-engineering] related: [import-skill-creator-openai, import-skill-optimizer-lawvable, import-contract-review-anthropic, import-legal-risk-assessment-anthropic] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'import'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Import: Skill Creator (Anthropic)

## What it does

This import adapter migrates a **skill-creation/skill-authoring tool** originally built for Anthropic's the agent API into the `mini-hermes-the-firm` standard format. A skill creator is a meta-skill: it is a prompt or workflow that generates other skills — taking a description of a legal capability and producing a properly structured SKILL.md file.

In the Louis / HAQQ Legal AI context, the Anthropic-native skill creator was used to bootstrap new skills during development. This adapter brings that capability into the open-source skill format so that contributors to `mini-hermes-the-firm` can generate new skills using the standard SKILL.md format directly.

## Import config

| Field | Source mapping | Default if absent |
|---|---|---|
| `creation_mode` | Legacy `mode` | `guided` (interactive input collection) |
| `category_detection` | Legacy `detect_category` boolean | `true` |
| `template_selection` | Legacy `template` | `auto` (body structure selected by category) |
| `frontmatter_generation` | Legacy `generate_frontmatter` boolean | `true` |
| `quality_validation` | Legacy `validate` boolean | `true` |
| `jurisdiction_prompt` | Legacy `prompt_jurisdiction` boolean | `true` |
| `related_skill_suggest` | Legacy `suggest_related` boolean | `true` |
| `output_format` | Legacy `format` | `skill_md` |

## Dry-run preview

```
IMPORT PREVIEW — skill-creator-anthropic
Source shape      : Anthropic skill-generation prompt
Mode              : guided
Category detection: enabled
Template          : auto-selected by category
Frontmatter       : auto-generated
Quality validation: enabled
Jurisdiction      : prompted
Related skills    : suggested
Output            : SKILL.md
```

## Skill creation pipeline (post-import)

### Step 1 — Collect inputs
```
Skill name         : [user provides]
Category           : [detected or user confirms from list]
Practice area      : [user provides or skip]
Jurisdictions      : [user provides or __multi__]
Priority           : [P0 / P1 / P2 / P3]
Intent keywords    : [user provides 2–6]
Brief description  : [user provides — 1 sentence]
Source content     : [user provides raw content / existing skill / description]
```

### Step 2 — Category → template selection

| Category | Template selected |
|---|---|
| `draft` | Drafting skill template (When to use / Required inputs / Document structure / Jurisdictional notes) |
| `review` / `eval` | Review skill template (Review methodology / What to flag / Output format) |
| `kb` / `ref` / `wiki` | Knowledge pack template (Scope / Substantive content / Caveats) |
| `conversation` / `safety` | Behavioral skill template (When this applies / Behavior / Examples / Do not) |
| `router` / `workflow` | Router template (Purpose / Logic / Output schema) |
| `import` | Import/connector template (What it does / Import config / Dry-run / Failure modes) |
| `connector` / `tool` | Connector template (What it does / Setup / Capabilities / Failure modes) |

### Step 3 — Frontmatter generation

Generates valid YAML frontmatter:
- `name`: lowercase slug with hyphens
- `description`: 1–4 sentences, routing-focused, starts with "Use when…"
- `metadata.id`: category + slug
- `metadata.category`: selected category
- `metadata.jurisdictions`: from input
- `metadata.priority`: from input
- `metadata.intent`: from input keywords
- `metadata.related`: suggested related skill names in slug form
- `metadata.source`: standard source line
- `metadata.version`: "1.0"

### Step 4 — Quality validation checklist

Before outputting the skill, validate:
- [ ] Description answers "when should the agent reach for this skill?"
- [ ] Body is 120–320 lines
- [ ] No fabricated statute numbers or case citations
- [ ] MENA jurisdictional notes included where relevant
- [ ] Related skills section populated with `[[wikilinks]]`
- [ ] No `[INSERT X]` template artifacts
- [ ] YAML frontmatter is valid

## Failure modes

| Error | Likely cause | Resolution |
|---|---|---|
| `category_not_detected` | Source description ambiguous | Prompt user to select from category list |
| `description_too_generic` | Generated description lacks routing specificity | Regenerate with "Use when…" prompt structure |
| `frontmatter_invalid_yaml` | Unescaped characters in description | Escape or rephrase the description |
| `body_too_short` | Insufficient source content | Request more detail from user; expand from known framework |
| `related_skills_empty` | No related skills suggested | Infer 3–5 from category and practice area |

## Related skills

- [[import-skill-creator-openai]]
- [[import-skill-optimizer-lawvable]]
- [[import-contract-review-anthropic]]
- [[import-legal-risk-assessment-anthropic]]
- [[import-tabular-review-lawvable]]
