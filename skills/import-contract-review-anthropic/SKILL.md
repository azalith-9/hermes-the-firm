---
name: import-contract-review-anthropic
description: Use when migrating a contract-review skill or workflow originally built for Anthropic's the agent API into the mini-hermes-the-firm skill format. This import adapter maps the legacy Anthropic contract-review data shape — prompt templates, clause flags, risk buckets, and output schemas — into the standard skill model. Triggers on any import of Anthropic-native contract analysis configurations.
license: MIT
metadata: " id: import.contract-review-anthropic category: import jurisdictions: [__multi__] priority: P3 intent: [__import__, contract-review, migration, anthropic, skill-import] related: [review-contract-generic, import-nda-triage-anthropic, import-tabular-review-lawvable, import-legal-risk-assessment-anthropic] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'import'.
Registered as a flat plugin skill.
-->


# Import: Contract Review (Anthropic)

## What it does

This import adapter migrates a **contract-review skill** originally authored for Anthropic's the agent API into the `mini-hermes-the-firm` standard SKILL.md format. The legacy skill may have been built as a raw system-prompt file, a JSON config blob, a `claude.ai` Projects instruction, or a structured prompt-pack; this adapter normalises all of those shapes into a deployable skill entry.

The resulting skill enables the agent to systematically review commercial contracts — identifying missing clauses, anomalous terms, risk exposure, and jurisdiction-specific traps — while preserving all prompt logic from the original Anthropic-native implementation.

## Import config

| Field | Source mapping | Default if absent |
|---|---|---|
| `skill_id` | Legacy `id` or filename stem | `review-contract-anthropic` |
| `prompt_template` | Legacy system prompt text | Extract from file body |
| `risk_buckets` | Legacy risk categories array | HIGH / MEDIUM / LOW |
| `clause_flags` | Legacy clause checklist | Standard 12-clause set (see below) |
| `output_schema` | Legacy response format | Structured markdown table |
| `jurisdiction` | Legacy `jurisdiction` or `locale` field | `__multi__` |
| `language` | Legacy `lang` field | `en` |
| `model_hint` | Legacy `model` field | `claude-sonnet-4-5` |

## Dry-run preview

Before committing the import, the adapter emits a preview block:

```
IMPORT PREVIEW — contract-review-anthropic
Source shape : Anthropic system-prompt JSON
Target skill : review-contract-anthropic
Clause flags : 12 detected (termination, indemnity, liability cap, IP assignment,
               governing law, dispute resolution, confidentiality, payment terms,
               warranties, force majeure, assignment, data protection)
Risk buckets : HIGH / MEDIUM / LOW
Output schema: markdown table
Jurisdictions: __multi__ (no jurisdiction lock detected in source)
```

The user must confirm before the skill is written to disk.

## Standard clause checklist (default)

When the legacy config did not specify a clause list, the import seeds these 12 standard clauses for contract review:

1. **Termination** — grounds, notice period, consequences
2. **Indemnification** — scope, caps, carve-outs
3. **Liability cap** — amount, exclusions (gross negligence, fraud)
4. **IP assignment / licensing** — ownership, work-for-hire, licence grant
5. **Governing law & jurisdiction** — choice of law, seat of arbitration
6. **Dispute resolution** — arbitration vs litigation, escalation ladder
7. **Confidentiality / NDA** — scope, duration, permitted disclosures
8. **Payment terms** — currency, timing, late-payment interest
9. **Warranties & representations** — scope, survival period
10. **Force majeure** — definition, notice, relief, termination trigger
11. **Assignment & change of control** — consent requirements
12. **Data protection** — DPA obligations, sub-processing, breach notification

## Jurisdictional notes

MENA-specific traps surfaced during review after import:

- **UAE / KSA onshore**: civil-code jurisdictions; liquidated-damages clauses (penalty clauses) must not be unconscionably disproportionate or courts may reduce them. Verify Arabic language requirement for government contracts.
- **DIFC / ADGM**: common-law; DIFC Contract Law and ADGM Contract Regulations apply. Penalty clauses enforceable if genuine pre-estimate of loss.
- **Lebanon**: French-inspired civil law; Articles 221–230 Code des Obligations et des Contrats govern damages; force majeure construction differs from Anglo-American standard.
- **Egypt**: Civil Code (Law 131/1948); courts routinely re-examine penalty clauses.
- **France**: GDPR + French data-protection overlay; specific consumer-protection rules if B2C.

## Failure modes

| Error | Likely cause | Resolution |
|---|---|---|
| `schema_mismatch` | Legacy output format uses XML or HTML | Map via `output_schema: markdown` override |
| `clause_list_empty` | Source used implicit checks, no list | Apply default 12-clause set |
| `jurisdiction_conflict` | Source locks to US; target is MENA | Override with `jurisdictions: [__multi__]` |
| `prompt_too_long` | Legacy prompt exceeds context on import | Split into system + user template parts |

## Related skills

- [[review-contract-generic]]
- [[import-nda-triage-anthropic]]
- [[import-legal-risk-assessment-anthropic]]
- [[import-tabular-review-lawvable]]
- [[review-nda-bilateral]]
