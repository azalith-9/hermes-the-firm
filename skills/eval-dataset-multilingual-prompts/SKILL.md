---
name: eval-dataset-multilingual-prompts
description: Use when running the multilingual benchmark that tests language detection accuracy, output language matching, Arabic legal terminology quality, and bilingual document formatting across English, Arabic, French, and mixed-language inputs. Key metric is language-match rate ≥ 95%.
license: MIT
metadata: " id: eval.dataset.multilingual-prompts category: eval priority: P0 intent: [__eval__, multilingual, arabic, french, language-detection] related: [eval-benchmark-runner, eval-rubric-language-quality-ar, eval-rubric-language-quality-en, eval-regression-detector, eval-dataset-nda-prompts-30] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'eval'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Eval Dataset — Multilingual Prompts

## Scope

~50 prompts across English, Arabic (MSA, Levantine, Gulf), French (Lebanese-French and standard), mixed AR/EN, and explicit translation/bilingual-formatting requests. Tests the full multilingual pipeline from language detection through output generation. Correct language handling is a hard requirement for MENA legal practice — a lawyer who writes in Arabic and gets an English response has a broken product experience.

Key metric: **language-match rate ≥ 95%** (output language matches input language, unless user explicitly requests otherwise).

Storage: `eval/datasets/multilingual-prompts.jsonl`

## How to use this pack

1. Load into [[eval-benchmark-runner]] with [[eval-rubric-language-quality-ar]] and [[eval-rubric-language-quality-en]] as scoring rubrics.
2. For each response, run automated language detection on the output and compare to the input language.
3. Compute `language_match_rate` = (correct_language_responses / total).
4. For Arabic outputs, submit a sample to a human Arabic legal reviewer quarterly.
5. Feed results to [[eval-regression-detector]].

## Categories

### Category 1 — Arabic-only inputs (~12 prompts)

Test that Arabic input produces Arabic output with correct legal terminology.

**MSA (Modern Standard Arabic) — formal legal register:**
- "أعدّ لي عقد عمل بموجب قانون العمل الإماراتي." (Draft an employment contract under UAE Labour Law.)
- "ما هي شروط اتفاقية عدم الإفصاح في القانون اللبناني؟" (What are the NDA requirements under Lebanese law?)
- "راجع هذا البند وحدد المخاطر القانونية." (Review this clause and identify legal risks.)

**Levantine Arabic (Lebanese dialect) — client-facing register:**
- "بدي تعاقد عمل للبنان، شو بدك مني؟" (I want an employment contract for Lebanon, what do you need from me?)
- "هالعقد مظبوط؟ شو في غلط فيه؟" (Is this contract correct? What's wrong with it?)

**Gulf Arabic (UAE/KSA dialect):**
- "أبغى أسوي عقد NDA للسعودية." (I want to make an NDA for Saudi Arabia.)
- "وش الفرق بين عقد العمل في الإمارات وفي المملكة؟" (What's the difference between employment contracts in UAE vs KSA?)

**Expected behavior**: Output in Arabic (MSA preferred for legal documents, dialect acceptable for conversational clarifications); legal terminology must be accurate (مكافأة نهاية الخدمة not just "gratuity transliterated"; اتفاقية عدم الإفصاح not "NDA in Arabic letters").

### Category 2 — French-only inputs (~10 prompts)

**Lebanese-French (legal-professional register):**
- "Rédigez un contrat de travail conforme au Code du travail libanais." (Draft an employment contract compliant with the Lebanese Labour Code.)
- "Quelle est la durée maximale de la période d'essai au Liban?" (What is the maximum probation period in Lebanon?)
- "Vérifiez cette clause de confidentialité pour un accord soumis au droit français." (Review this confidentiality clause for a French-law agreement.)

**Standard French (France / EU):**
- "Rédigez un NDA selon le droit français."
- "Expliquez les règles RGPD applicables à ce contrat de traitement de données."

**Expected behavior**: Output in French; legal terms in French (clause de confidentialité, rupture conventionnelle, période d'essai).

### Category 3 — Mixed Arabic-English inputs (~10 prompts)

Common in MENA legal practice: a message that switches languages mid-sentence.

- "Review هذا العقد and tell me what's missing." (English request with Arabic object)
- "أريد NDA لـ DIFC — what are the key clauses?" (Arabic request with English terms)
- "هل الـ force majeure clause مناسبة للعقود الإماراتية؟" (Arabic question with English legal term)

**Expected behavior**: Respond in the dominant language of the prompt (usually Arabic if the grammatical structure is Arabic). Do not mix languages in the response unless the question specifically asks for it.

### Category 4 — Bilingual document requests (~10 prompts)

Explicit requests for side-by-side bilingual documents:
- "Draft an NDA with Arabic on the left and English on the right."
- "أعطني عقد العمل بالعربي والإنجليزي جنب بعض." (Give me the employment contract in Arabic and English side by side.)
- "I need a bilingual lease agreement (AR/EN) for a UAE property — Arabic is the controlling language."

**Expected behavior**: Output formatted in two columns or clearly alternating sections; "controlling language" statement included (Arabic version controls); legal terminology consistent between both versions.

### Category 5 — Translation requests (~8 prompts)

- "Translate this English NDA clause into Arabic."
- "ترجم هذه الفقرة من العربية إلى الإنجليزية." (Translate this paragraph from Arabic to English.)
- "Translate this NDA governing law clause from French to English."

**Expected behavior**: Accurate legal translation (not machine-literal); terminology matches the target jurisdiction's conventions.

## Scoring dimensions

| Dimension | Method | Target |
|---|---|---|
| Language match rate | Automated language detection on output | ≥ 95% |
| Arabic legal term accuracy | Human rater (sample) | ≥ 4.0/5 |
| French legal term accuracy | LLM judge | ≥ 3.5/5 |
| Bilingual formatting | Rule-based check (two-column/alternating present) | ≥ 90% of bilingual requests |
| Controlling language statement | String match check | 100% of bilingual drafts |

## Caveats & currency

- Arabic legal dialect varies by country; Gulf Arabic and Levantine Arabic are distinct. The product targets legal professionals who primarily write MSA — but intake may be in dialect.
- French legal vocabulary in Lebanon differs slightly from Metropolitan French (Lebanese lawyers use Code de la Route, Code des Obligations et des Contrats, etc.).
- Automated language detection tools (langdetect, fastText) struggle with short Arabic inputs and mixed text. Human review of a 10% sample each quarter is necessary.

## Related skills

- [[eval-benchmark-runner]] — orchestrates this dataset
- [[eval-rubric-language-quality-ar]] — Arabic quality scoring rubric
- [[eval-rubric-language-quality-en]] — English quality scoring rubric
- [[eval-regression-detector]] — tracks language-match rate across deployments
