---
name: eval-rubric-language-quality-ar
description: Use when scoring the Arabic language quality of AI legal outputs. A 0–5 rubric covering grammatical correctness, legal register, terminology precision, script directionality, and dialect appropriateness for MENA legal practice. Arabic legal output requires MSA with correct technical terminology — not informal Arabic or transliterated loanwords.
license: MIT
metadata: " id: eval.rubric.language-quality-AR category: eval jurisdictions: [__multi__] priority: P2 intent: [__eval__, arabic, language-quality, rubric, mena] related: [eval-rubric-language-quality-en, eval-llm-as-judge-system-prompt, eval-benchmark-runner, eval-dataset-multilingual-prompts] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'eval'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Eval Rubric — Language Quality (Arabic)

## When to use this

Apply whenever an AI legal output is in Arabic or contains a substantial Arabic component. This rubric is scored independently of legal accuracy — correct law stated in poor Arabic is a quality failure for a MENA legal AI product. Arabic legal writing has strict conventions in professional practice; outputs that deviate from these conventions undermine user trust.

Requires a human Arabic legal reviewer for high-stakes outputs; LLM judges have limited reliability for detecting subtle Arabic legal register issues.

## Scoring (0–5)

| Score | Label | Criteria |
|---|---|---|
| **5** | Excellent | Grammatically correct MSA throughout; correct legal terminology (مكافأة نهاية الخدمة, اتفاقية عدم الإفصاح, قانون العمل); appropriate formal register for the document type; no transliterated loanwords where Arabic equivalents exist; RTL formatting correct; legal style appropriate to the jurisdiction (Khaleeji vs Levantine legal conventions where relevant) |
| **4** | Good | Grammatically correct with minor issues; terminology mostly correct; 1–2 instances of unnecessary transliteration or informal register |
| **3** | Acceptable | Substantially correct but notable terminology issues (e.g., using "كونفيدنشيالتي" instead of "سرية"; using dialectal words in a formal contract); or occasional grammatical errors that do not obscure meaning |
| **2** | Poor | Multiple grammatical errors; significant terminology problems; mixed register (formal and informal in the same document); RTL formatting issues |
| **1** | Very poor | Barely intelligible Arabic; heavy transliteration; appears to be machine-translated from English without legal register correction |
| **0** | Fail | Not Arabic (wrong language output for an Arabic-input request), or completely garbled |

## Sub-criteria

### Grammatical correctness
Arabic grammar is complex and unforgiving in formal legal writing. Key checks:
- **Case endings (إعراب)**: In formal written Arabic, case endings should be used in formal document titles and key phrases. Their absence is acceptable in running text (as in newspaper Arabic) but notable in highly formal contracts.
- **Agreement**: Adjective-noun agreement in gender and number; verb-subject agreement.
- **Dual and plural**: Correct use of dual (مزودان, طرفان) vs plural; sound plural vs broken plural.
- **Relative clauses**: الذي / التي / الذين / اللاتي — correct usage.

### Legal terminology accuracy
Arabic legal vocabulary has standard terms; informal or transliterated alternatives are unacceptable in professional documents:

| Concept | Correct Arabic term | Do not use |
|---|---|---|
| Non-disclosure agreement | اتفاقية عدم الإفصاح / اتفاقية السرية | "NDA" alone or "ان دي اي" |
| Employment contract | عقد العمل | "كونتراكت" |
| End-of-service gratuity | مكافأة نهاية الخدمة | EOSG in Arabic text |
| Penalty clause | شرط الغرامة / شرط الجزاء | "بنلتي كلوز" |
| Force majeure | قوة قاهرة | "فورس ماجور" |
| Governing law | القانون الحاكم | "قانون الجورننج" |
| Arbitration | التحكيم | "أربتريشن" |
| Indemnification | التعويض / التضمين | "إنديمنفكيشن" |

### Register appropriateness
- **Formal contracts and legal opinions**: Modern Standard Arabic (الفصحى), formal register, no dialect.
- **Client-facing explanations**: Standard Arabic acceptable; slight informality acceptable but not Levantine or Gulf dialect in the formal answer.
- **Intake / clarifying questions**: Dialect is acceptable if matching the user's dialect (the system may mirror the user's register for conversational turns).

### Script and directionality
- Arabic text must be genuinely RTL — not ASCII-art right-alignment but actually rendered in the correct Unicode range.
- No mixing of Arabic and Latin character sets within the same word.
- Numbers in Arabic legal contracts: Eastern Arabic numerals (٠١٢٣٤٥٦٧٨٩) are preferred in KSA and Lebanon; Western Arabic numerals (0123456789) acceptable in UAE/DIFC. Either is acceptable as long as consistent.

### Jurisdiction-specific Arabic conventions
- **KSA**: Formal Arabic; Hejazi/Najdi legal conventions; longer sentences; classical references to Shariah principles acceptable.
- **UAE/GCC**: Gulf variant; slightly more concise; mixing Western Arabic numerals is common.
- **Lebanon**: Lebanese legal Arabic influenced by French; loan structures from French legal vocabulary are acceptable (e.g., أمر أداء / ordonnance).

## Human review requirement

LLM judges are unreliable for Arabic legal register at score levels 3–5. For critical deployments:
- Have a native Arabic legal professional review a 10% random sample of Arabic outputs quarterly.
- Focus human review on: contract clause terminology, procedural Arabic (عرائض, استدعاءات), and corporate Arabic (اندماج, استحواذ).

## Related skills

- [[eval-rubric-language-quality-en]] — parallel rubric for English language quality
- [[eval-llm-as-judge-system-prompt]] — applies this rubric (with caveats for LLM Arabic limitations)
- [[eval-benchmark-runner]] — orchestrates scoring
- [[eval-dataset-multilingual-prompts]] — primary dataset for Arabic language quality testing
