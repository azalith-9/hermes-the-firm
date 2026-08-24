---
name: eval-dataset-nda-prompts-30
description: Use when running the NDA benchmark that tests drafting, review, intake, and edge-case handling across LB/KSA/UAE/DIFC/FR/UK. Contains 30 prompts covering mutual and unilateral NDAs, bilingual AR/EN side-by-side, multi-party structures, and adversarial edge cases. Primary benchmark for confidentiality-related AI capabilities.
license: MIT
metadata: " id: eval.dataset.NDA-prompts-30 category: eval priority: P0 intent: [__eval__, nda, benchmark, dataset, mena, drafting] related: [eval-benchmark-runner, eval-dataset-employment-prompts-30, eval-regression-detector, eval-rubric-legal-soundness, eval-rubric-citation-quality, eval-rubric-jurisdiction-awareness, eval-rubric-completeness] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'eval'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Eval Dataset — NDA Prompts (30)

## Scope

30 NDA-related prompts spanning drafting, review, intake clarification, and edge cases. NDA drafting is the single highest-volume legal AI request globally — it is the entry point for most users of legal AI tools. Quality on this dataset directly correlates with first-impression retention.

Storage: `eval/datasets/NDA-prompts-30.jsonl`

Format: one JSON object per line:
```json
{
  "id": "nda-001",
  "prompt": "...",
  "category": "standard_draft",
  "jurisdiction": "UAE",
  "expected_signals": ["mutual", "confidential_info_defined", "governing_law_uae", "dispute_resolution"]
}
```

## How to use this pack

1. Run all 30 prompts against the deployed model.
2. Score each output against [[eval-rubric-legal-soundness]] + [[eval-rubric-citation-quality]] + [[eval-rubric-jurisdiction-awareness]] + [[eval-rubric-completeness]].
3. Aggregate scores; track week-over-week trend in [[eval-regression-detector]].
4. Flag any output where `expected_signals` are missing — even if the rubric score is acceptable, missing a governing-law clause is a structural gap.

## Prompt categories

### Category 1 — Standard draft (~6 prompts)

Drafting requests across jurisdictions for basic NDA types:

| # | Type | Jurisdiction | Key expected signals |
|---|---|---|---|
| 1 | Mutual NDA | UAE onshore | UAE Civil Transactions Law governing; Arabic available; 2-year term standard |
| 2 | Unilateral NDA | KSA | Saudi governing law; Shariah compliance note; Arabic version noted |
| 3 | Mutual NDA | DIFC | DIFC Contract Law; English language; common-law drafting style |
| 4 | Mutual NDA | Lebanon | Lebanese Code of Obligations; French or Arabic version option |
| 5 | Mutual NDA | France | Code civil; French governing law; RGPD data protection cross-reference |
| 6 | Mutual NDA | UK | English law; PECR note if digital communications involved |

### Category 2 — Review (~5 prompts)

Paste a draft NDA; ask for redlines or risk identification:

| # | Scenario |
|---|---|
| 7 | NDA with overly narrow definition of Confidential Information — model should flag |
| 8 | NDA that lacks a governing law clause — model should flag as critical gap |
| 9 | NDA with a 10-year term — model should flag as potentially unenforceable in civil law jurisdictions |
| 10 | NDA with a compelled disclosure clause — model should check it correctly handles court orders |
| 11 | NDA missing a return/destroy clause — model should flag |

### Category 3 — Intake / clarification (~5 prompts)

Ambiguous requests where the model should ask clarifying questions rather than draft:

| # | Ambiguous input |
|---|---|
| 12 | "I need an NDA." (no jurisdiction, no parties, no type specified) |
| 13 | "Draft an NDA for a tech deal." (insufficient — which jurisdiction? mutual or one-way?) |
| 14 | "NDA between my company and a Saudi partner." (type unclear; should ask mutual vs unilateral) |
| 15 | "I need an NDA urgently, can you just make a quick one?" (prompt for minimum viable info) |
| 16 | Arabic-language ambiguous request: "أريد NDA" (respond in Arabic, ask clarifiers in Arabic) |

**Expected behavior**: Ask for jurisdiction, party types, NDA type (mutual/unilateral), and confidential information scope before drafting.

### Category 4 — Edge cases (~5 prompts)

| # | Edge case | Expected handling |
|---|---|---|
| 17 | "Draft an NDA with confidential information defined as 'everything'" | Flag as overly broad; suggest standard scope with carve-outs |
| 18 | "Draft an NDA with a 99-year term" | Flag as potentially unenforceable; suggest 2–5 years with auto-renewal |
| 19 | "Draft an NDA with no governing law — I want it to be internationally neutral" | Explain why governing law is necessary; offer alternatives (ICC arbitration, DIFC as neutral) |
| 20 | "I want an NDA that says we own any ideas the other party shares with us" | Flag: an NDA is a confidentiality instrument, not an IP assignment — suggest adding a separate IP clause or using an NDA + IP assignment |
| 21 | "Make an NDA that's enforceable in both the UAE and the US simultaneously" | Multi-jurisdiction enforceability explanation; suggest appropriate governing law strategy |

### Category 5 — Bilingual AR/EN (~4 prompts)

| # | Request |
|---|---|
| 22 | "Draft a mutual NDA in Arabic and English, side by side. Arabic controls." |
| 23 | Arabic-only prompt: "أعدّ اتفاقية سرية بالعربي والإنجليزي." |
| 24 | "Translate this English NDA clause into formal Arabic." |
| 25 | "Is the Arabic version of this NDA consistent with the English version? Identify discrepancies." |

### Category 6 — Multi-party / consortium (~5 prompts)

| # | Scenario |
|---|---|
| 26 | Three-party mutual NDA (startup, investor, technology partner) under UAE law |
| 27 | Consortium NDA for a KSA government tender — 5 parties |
| 28 | "How should we structure an NDA for a joint venture where one party is a UAE company and one is a Saudi company?" |
| 29 | Multi-jurisdictional NDA with carve-out provisions per jurisdiction |
| 30 | NDA renewal and amendment — add a new party to an existing two-party NDA |

## Scoring targets

| Category | Legal soundness target | Jurisdiction awareness target | Completeness target |
|---|---|---|---|
| Standard draft | ≥ 4.0 | ≥ 4.0 | ≥ 4.0 |
| Review | ≥ 3.5 | ≥ 3.5 | ≥ 3.5 |
| Intake | N/A (evaluate on asking clarifiers) | N/A | N/A |
| Edge cases | ≥ 3.5 | ≥ 3.5 | — |
| Bilingual | ≥ 3.5 | ≥ 3.5 | ≥ 3.5 |
| Multi-party | ≥ 3.5 | ≥ 3.5 | ≥ 3.0 |

## Jurisdictional notes for graders

- **UAE onshore**: UAE Civil Transactions Law (Federal Law No. 5 of 1985) and Federal Decree-Law No. 4 of 2022 on Commercial Transactions govern. No statutory definition of "confidentiality agreement" — governed by general contract principles.
- **DIFC**: DIFC Contract Law (DIFC Law No. 6 of 2004) applies; common-law interpretation; English is the operative language.
- **KSA**: Saudi law is Shariah-based; commercial confidentiality enforced through general principles; Arabic is required for Saudi court proceedings.
- **Lebanon**: Code des Obligations et des Contrats (Code of Obligations and Contracts, 1932) governs; both French and Arabic are official court languages.
- **France**: Code civil (particularly obligations law post-2016 reform). RGPD applies to personal data provisions.

## Caveats & currency

Review the dataset annually. DIFC legislation updates regularly (check DIFC Laws portal); UAE Commercial Transactions Law amendments should trigger a dataset review.

## Related skills

- [[eval-benchmark-runner]] — orchestrates this dataset in the full eval pipeline
- [[eval-rubric-legal-soundness]] — primary scoring rubric
- [[eval-rubric-jurisdiction-awareness]] — jurisdiction accuracy scoring
- [[eval-rubric-completeness]] — structural completeness check
- [[eval-regression-detector]] — week-over-week trend tracking
