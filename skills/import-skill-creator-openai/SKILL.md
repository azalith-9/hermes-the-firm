---
name: import-skill-creator-openai
description: Use when migrating a skill-creation or skill-authoring tool originally built for the OpenAI API into the mini-hermes-the-firm format. The adapter maps legacy OpenAI skill-generation prompts — GPT-4 function-calling schemas, structured output formats, and skill-templating pipelines — into the standard SKILL.md format for the open-source repository. Triggers when importing any OpenAI-native prompt-engineering or skill-factory workflow.
license: MIT
metadata: " id: import.skill-creator-openai category: import jurisdictions: [__multi__] priority: P3 intent: [__import__, skill-creator, openai, migration, prompt-engineering, skill-authoring] related: [import-skill-creator-anthropic, import-skill-optimizer-lawvable, import-security-review-openai, import-tabular-review-lawvable] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'import'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Import: Skill Creator (OpenAI)

## What it does

This import adapter migrates a **skill-creation/skill-authoring tool originally built for the OpenAI API** into the `mini-hermes-the-firm` standard format. OpenAI-native skill creators typically use GPT-4's function calling, structured JSON output mode, or Assistant API tool definitions to generate skill configurations — these must be translated into the SKILL.md format used by this repository.

The key differences between OpenAI and Anthropic/Louis skill formats that this adapter handles:

| OpenAI format | mini-hermes-the-firm equivalent |
|---|---|
| `function_definitions` JSON array | SKILL.md with ## Capabilities section |
| `system_message` string | SKILL.md ## Behavior section |
| `tool_choice` schema | Routing via `intent` frontmatter field |
| `response_format: json_object` | Output schema in ## Output format section |
| `Assistant API` instruction | SKILL.md as standalone skill file |

## Import config

| Field | Source mapping | Default if absent |
|---|---|---|
| `source_format` | Legacy `format` | `function_calling` (most common OpenAI pattern) |
| `function_definitions` | Legacy `functions` array | Extract from source |
| `system_message` | Legacy `system` string | Map to skill body |
| `response_format` | Legacy `response_format` | Map to ## Output format section |
| `model_hint` | Legacy `model` field | `claude-sonnet-4-5` (Anthropic equivalent) |
| `category_detection` | Auto-detect from function names + description | Prompt if ambiguous |
| `output_format` | Target format | `skill_md` |

## Dry-run preview

```
IMPORT PREVIEW — skill-creator-openai
Source format  : function_calling (GPT-4)
Functions      : [count] function definitions detected
System message : [present / absent]
Response format: json_object → mapped to structured output section
Model          : gpt-4-turbo → mapped to claude-sonnet-4-5
Category       : [detected / needs confirmation]
Output         : SKILL.md
```

## Translation pipeline (post-import)

### Function definitions → skill body

OpenAI function definitions carry a `description` (purpose), `parameters` (inputs), and `returns` schema. These map as follows:

```json
// OpenAI input:
{
  "name": "review_contract",
  "description": "Review a contract for legal risks",
  "parameters": {
    "type": "object",
    "properties": {
      "contract_text": {"type": "string", "description": "Full contract text"},
      "jurisdiction": {"type": "string", "description": "Governing jurisdiction"}
    },
    "required": ["contract_text"]
  }
}
```

Maps to SKILL.md:
- `name: review-contract` (slugified)
- `## Required inputs` → `contract_text` (required), `jurisdiction` (optional with default)
- `## Output format` → derived from the function's return type or downstream usage

### System message → skill body

The OpenAI system message becomes the core of the SKILL.md body:
- Persona/role description → `## When to use this` or behavioral `## Behavior` section
- Step-by-step instructions → appropriate methodology section per category
- Output format instructions → `## Output format` section
- Constraints → `## Do not` or `## Limits & escalation` section

### Model-specific features that do not migrate directly

| OpenAI feature | Migration path |
|---|---|
| `function_calling` | Convert to the agent tool use or structured output; document in ## Capabilities |
| `gpt-4-vision` | the agent's native vision capability; may migrate directly |
| `Assistant API threads` | Stateless SKILL.md; conversation history managed externally |
| `Code Interpreter` | Not directly available; document as limitation |
| `Retrieval` | Map to document-ingestion import skills |

## Quality validation (post-import)

After translation, verify:
- [ ] All function parameters are represented as Required / Optional inputs
- [ ] Response format is documented in ## Output format
- [ ] MENA jurisdictional context is added where relevant (OpenAI skills are often US-centric)
- [ ] No OpenAI-specific syntax remains in the skill body
- [ ] Related skills section populated

## Failure modes

| Error | Likely cause | Resolution |
|---|---|---|
| `function_schema_too_complex` | Deeply nested parameter schemas | Flatten; document complex sub-objects as tables |
| `system_message_too_long` | 4000+ token system prompt | Summarise into skill body; move details to ## Document structure |
| `gpt4_features_not_available` | Code Interpreter or Retrieval used | Document limitation in ## Limits section |
| `category_ambiguous` | Function names not clearly legal | Prompt user to select category |
| `us_law_hardcoded` | Source assumed US jurisdiction | Add `jurisdictions: [__multi__]` and MENA notes |

## Related skills

- [[import-skill-creator-anthropic]]
- [[import-skill-optimizer-lawvable]]
- [[import-security-review-openai]]
- [[import-tabular-review-lawvable]]
- [[import-contract-review-anthropic]]
