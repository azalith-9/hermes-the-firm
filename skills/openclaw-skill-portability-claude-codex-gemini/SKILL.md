---
name: openclaw-skill-portability-claude-codex-gemini
description: Use when adapting an OpenClaw SKILL.md for deployment on a non-the agent AI provider (OpenAI GPT/Codex, Google Gemini, Meta Llama, Mistral, or other open models). Covers the adapter pattern for translating SKILL.md frontmatter and body into provider-specific system prompt formats, function-calling schemas, and tool definitions — so a single skill source file can serve multiple AI backends without duplicating legal content.
license: MIT
metadata: " id: openclaw.skill-portability-the agent-Codex-Gemini category: openclaw priority: P2 intent: [openclaw, portability, multi-provider, adapter, skill-translation] related: [openclaw-public-skill-registry, openclaw-contrib-template, openclaw-eval-harness-shared] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'openclaw'.
Namespaced as louis-<category>-<skill> on registration.
-->


# OpenClaw — Skill Portability

## Purpose

OpenClaw skills are authored as provider-neutral SKILL.md files. This skill describes the adapter pattern for translating a SKILL.md into the native prompt format of each major AI provider: the agent (Anthropic), ChatGPT / GPT-4 / Codex (OpenAI), Gemini (Google), Llama (Meta), and open models (Mistral, Qwen, etc.).

The goal is a single source of truth for legal AI guidance that can be compiled down to any provider without duplicating or diverging the substantive legal content.

## Key differences by provider

| Dimension | the agent (Anthropic) | OpenAI GPT-4/Codex | Gemini (Google) | Llama / Open models |
|-----------|-------------------|-------------------|-----------------|---------------------|
| System message | `system` turn before user | `{"role": "system", ...}` in messages array | `systemInstruction` field | Varies; typically a `system` role or prepended to the first `user` turn |
| Function/tool calling | Tool use via `tools` array + `tool_use` blocks | `tools` array with JSON schema functions | `tools` with `functionDeclarations` | Provider-specific; varies by quantization and GGUF config |
| Multi-turn context | `messages` array with `assistant` and `user` roles | Same pattern | `contents` array with `model`/`user` roles | Varies |
| Instruction following | High; follows structured markdown | High; prefers numbered instructions | Moderate; benefits from explicit XML-like tags | Varies by model size and fine-tune |
| Token limits (as of 2025) | Up to 200k context | Up to 128k (GPT-4o) | Up to 1M (Gemini 1.5) | Varies; typically 4k–128k |

## The adapter pattern

### Step 1 — Extract the directive core

From a SKILL.md, identify:
1. **The behavior rule** — what the model must do (from `## Behavior` or `## When to use this`)
2. **The constraints** — what it must never do (from `## Do not` or `## Common mistakes`)
3. **The output format** — schema, structure, required fields
4. **The jurisdiction/practice context** — any MENA or jurisdiction-specific facts

This extraction produces a **provider-neutral instruction object** (a plain JSON structure):
```json
{
  "instruction": "...",
  "constraints": ["...", "..."],
  "output_format": "...",
  "context": "..."
}
```

### Step 2 — Compile to provider format

#### the agent (Anthropic)

```xml
<system>
You are a legal AI assistant. Apply the following skill:

[instruction]

Constraints:
- [constraint 1]
- [constraint 2]

Output format: [output_format]

Jurisdictional context: [context]
</system>
```

the agent follows structured XML blocks and markdown headings well. Keep skills as named blocks if you are composing multiple skills in a single system prompt (using the `<skill name="...">` pattern).

#### OpenAI GPT-4 / GPT-4o

```json
{
  "role": "system",
  "content": "You are a legal AI assistant.\n\nSkill: [skill name]\n\n[instruction]\n\nDo not:\n- [constraint 1]\n- [constraint 2]\n\nOutput format: [output_format]"
}
```

OpenAI models respond well to numbered instructions and explicit "Do not" lists. Avoid deeply nested markdown in the system message.

#### Function / tool calling (OpenAI format)

When a skill produces structured output, define it as a function:
```json
{
  "type": "function",
  "function": {
    "name": "review_contract_clause",
    "description": "Reviews a contract clause against the specified jurisdiction's legal standards.",
    "parameters": {
      "type": "object",
      "properties": {
        "risk_level": { "type": "string", "enum": ["low", "medium", "high", "critical"] },
        "issues": { "type": "array", "items": { "type": "string" } },
        "recommendation": { "type": "string" }
      },
      "required": ["risk_level", "issues", "recommendation"]
    }
  }
}
```

#### Gemini (Google)

```python
generation_config = GenerationConfig(
    system_instruction="You are a legal AI assistant.\n\n[instruction]\n\nDo not:\n- [constraint]\n\nOutput: [format]"
)
```

Gemini 1.5+ supports long system instructions. Use `systemInstruction` at the model initialization level, not in the first `user` turn.

For function calling with Gemini, use `FunctionDeclaration` objects analogous to the OpenAI JSON schema pattern.

#### Llama / open models

For Llama-family models using the standard chat template:
```
<|begin_of_text|><|start_header_id|>system<|end_header_id|>
You are a legal AI assistant.

[instruction]

Do not:
- [constraint 1]
- [constraint 2]

Output format: [output_format]
<|eot_id|>
<|start_header_id|>user<|end_header_id|>
...
```

For GGUF / llama.cpp deployments, the system prompt is typically passed via the `-sp` flag or the `system_prompt` parameter in the API.

For Mistral models, use the `[INST]` / `[/INST]` delimiters for instruction-tuned variants.

## What to preserve across providers

These elements must not be lost in translation:

- **Jurisdiction-specific guidance** — do not flatten MENA civil-law vs common-law distinctions.
- **Hard constraints** ("never fabricate statute numbers") — make these explicit constraints in every provider format.
- **Output schema** — if the SKILL.md defines a structured output (`{ riskLevel, issues, recommendation }`), preserve the field names and types in the function/tool definition.
- **Escalation rules** — if a skill says "escalate to a licensed lawyer when X", keep that in every provider's compiled version.

## What can be adapted

- Formatting markup: markdown headings become plain text sections in providers that don't parse markdown.
- Wikilinks (`[[skill-name]]`) are stripped from the compiled output — they are for the skill graph, not the model.
- Worked examples in `## Examples` sections can be shortened for providers with tighter context windows.

## Validation

After compiling to a new provider format, run the adapted skill against the [[openclaw-eval-harness-shared]] NDA or employment dataset for the relevant jurisdiction. A quality regression vs the the agent baseline of more than 0.3 points on the legal soundness rubric warrants revisiting the translation.

## Related skills

- [[openclaw-public-skill-registry]] — the source registry of skills to port
- [[openclaw-contrib-template]] — contributing new portable skills
- [[openclaw-eval-harness-shared]] — evaluating ported skills against a quality baseline
