---
name: import-statute-analysis-rafal-fryc
description: Use when migrating the Rafal Fryc statute-analysis methodology into the mini-hermes-the-firm format. This adapter preserves structured legislative text analysis — section-by-section decomposition, applicability scoping, definitional chain tracing, and cross-reference mapping — mapped into the standard skill model. Strong for civil-code jurisdictions (France, Lebanon, UAE onshore, Poland) and EU regulatory instruments. Triggers on import of any statute-analysis skill attributed to the Fryc approach.
license: MIT
metadata: " id: import.statute-analysis-rafal-fryc category: import jurisdictions: [FR, LB, UAE, EU, PL, __multi__] priority: P3 intent: [__import__, statute-analysis, legislative-analysis, migration, civil-law] related: [import-legal-risk-assessment-zacharie-laik, import-contract-review-anthropic, import-legal-simulation-patrick-munro, kb-gdpr-data-protection] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'import'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Import: Statute Analysis (Rafal Fryc)

## What it does

This import adapter migrates a **statute-analysis skill modelled on the Rafal Fryc methodology** into the `mini-hermes-the-firm` standard format. The Fryc methodology is a structured approach to legislative text: it treats a statute or regulation as a formal system, tracing definitions through their references, mapping the applicability scope before interpreting substantive obligations, and surfacing interpretive conflicts between provisions.

This methodology is particularly valuable for civil-law jurisdictions where statutes are the primary source of law (France, Lebanon, UAE Civil Code, EU Regulations) — unlike common-law jurisdictions where case law often fills the gaps that civil codes leave open.

## Import config

| Field | Source mapping | Default if absent |
|---|---|---|
| `analysis_mode` | Legacy `mode` | `full` (definition + scope + obligations + cross-references) |
| `definitional_chain` | Legacy `trace_definitions` boolean | `true` |
| `cross_reference_map` | Legacy `map_xrefs` boolean | `true` |
| `applicability_scope` | Legacy `check_scope` boolean | `true` |
| `conflict_check` | Legacy `check_conflicts` boolean | `true` |
| `output_format` | Legacy `format` | `statute_analysis_memo` |
| `jurisdiction` | Legacy `jurisdiction` | `FR` (Fryc's primary) |
| `language` | Legacy `lang` | `fr` |

## Dry-run preview

```
IMPORT PREVIEW — statute-analysis-rafal-fryc
Source shape       : Statute analysis (Fryc methodology)
Mode               : full
Definitional chain : traced
Cross-references   : mapped
Applicability scope: checked
Conflict check     : enabled
Language           : French
Jurisdiction       : France (civil law; override for other jurisdictions)
Output             : statute_analysis_memo
```

## Fryc analysis methodology (post-import)

### Step 1 — Applicability scoping
Before analysing what the statute requires, determine who it applies to:
- **Personal scope**: which persons, entities, or roles does the statute address? What are the thresholds (e.g. company size, turnover, number of employees)?
- **Material scope**: which activities, transactions, or subject matter does it cover?
- **Territorial scope**: which geographic locations or establishments does it reach?
- **Temporal scope**: when did it enter into force? Are there transitional provisions? Has it been amended?

### Step 2 — Definitional chain tracing
Statutes define key terms, but definitions reference other definitions. The Fryc approach traces the complete definitional chain:

```
DEFINED TERM → definition → references to OTHER defined terms
                         → traces each referenced term in turn
                         → flags circular definitions (common in EU regulations)
```

Example (GDPR): "personal data" → "identified or identifiable natural person" → "identifiable" → "identification by reference to an identifier" → back to "identifiers" (non-exhaustive list)

### Step 3 — Obligation mapping
For each substantive provision:
- Who is the **obligated person**? (controller, processor, employer, operator)
- What is the **obligation**? (must, shall, is required to)
- What are the **conditions**? (triggers, thresholds, exceptions)
- What is the **consequence** of non-compliance? (penalty, sanction, nullity, liability)

### Step 4 — Cross-reference mapping
Identify internal and external cross-references:
- Internal: "as defined in Article X", "subject to Article Y"
- External: references to other statutes, EU instruments, implementing regulations
- Flag any reference to a provision that has been repealed, amended, or is pending

### Step 5 — Interpretive conflict identification
- Are there two provisions that apply to the same situation but point in different directions?
- Does a later provision override an earlier one (lex posterior)?
- Does a specific provision override a general one (lex specialis)?
- Are there gaps (situations the statute does not address) that must be filled by analogy or judicial construction?

## Output schema

```
STATUTE ANALYSIS MEMO

Instrument     : [statute name, number, date]
Jurisdiction   : [jurisdiction]
Analysis date  : [date]

1. APPLICABILITY SCOPE
   Personal scope  : [who it applies to]
   Material scope  : [what it covers]
   Territorial scope: [where it applies]
   In force since  : [date]; last amended: [date]

2. KEY DEFINITIONS
   [Term] : [definition + chain trace]
   ...

3. OBLIGATION MAP
   [Party] must [obligation] when [conditions] under Art [X]
   Penalty for non-compliance: [consequence]
   ...

4. CROSS-REFERENCES
   Internal: [list]
   External: [list; flag repealed/amended]

5. INTERPRETIVE ISSUES
   [Conflict or gap description]
   Recommended approach: [interpretation method]
```

## Jurisdictional notes

| Jurisdiction | Civil-law interpretation rules |
|---|---|
| France | Code Civil Art 4: judge cannot refuse to decide even if law is silent; systematic interpretation preferred |
| Lebanon | Code of Obligations (French-inspired); Arabic and French versions both official |
| UAE Civil Code | Federal Law 5/1985; good faith (Art 246) central; Arabic prevails over English |
| EU Regulations | Teleological and comparative interpretation across 24 official languages; CJEU rulings binding |
| Poland | Constitutional Tribunal doctrine; EU law primacy since accession |

## Failure modes

| Error | Likely cause | Resolution |
|---|---|---|
| `definition_chain_circular` | Statute has circular definitions | Flag and note; trace as far as possible |
| `cross_reference_broken` | References to repealed provisions | Flag as "REPEALED — verify current equivalent" |
| `applicability_unclear` | Statute silent on scope | Apply ejusdem generis / in dubio mitius as appropriate |
| `jurisdiction_mismatch` | Fryc (civil law) methodology applied to common law statute | Note differences; statute interpretation rules differ |

## Related skills

- [[import-legal-risk-assessment-zacharie-laik]]
- [[import-contract-review-anthropic]]
- [[import-legal-simulation-patrick-munro]]
- [[kb-gdpr-data-protection]]
- [[import-legal-risk-assessment-anthropic]]
