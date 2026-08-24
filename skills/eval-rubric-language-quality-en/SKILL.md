---
name: eval-rubric-language-quality-en
description: Use when scoring the English language quality of AI legal outputs. A 0–5 rubric covering grammatical correctness, legal register, precision of expression, clarity for the intended audience (professional vs client-facing), and avoidance of verbose filler. Applies to outputs in English across all jurisdictions.
license: MIT
metadata: " id: eval.rubric.language-quality-EN category: eval jurisdictions: [__multi__] priority: P2 intent: [__eval__, english, language-quality, rubric, clarity] related: [eval-rubric-language-quality-ar, eval-llm-as-judge-system-prompt, eval-benchmark-runner, eval-dataset-nda-prompts-30] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'eval'.
Registered as a flat plugin skill.
-->


# Eval Rubric — Language Quality (English)

## When to use this

Apply whenever an AI legal output is in English. While English language quality is less likely to be the primary failure mode in a MENA legal AI (where legal accuracy and jurisdiction awareness matter more), poor language quality still undermines professional credibility and can obscure legal meaning. This rubric scores the writing quality independently of legal accuracy.

## Scoring (0–5)

| Score | Label | Criteria |
|---|---|---|
| **5** | Excellent | Grammatically correct throughout; legal register appropriate to context (contract drafting uses defined-term conventions, analysis uses precise legal vocabulary, client-facing explanations use plain language); no ambiguity in legal propositions; no padding or filler phrases; active voice preferred except where passive is legally conventional; consistent drafting style throughout |
| **4** | Good | Correct with minor issues (a stray comma splice, one sentence too long, slight inconsistency in heading capitalization) |
| **3** | Acceptable | Mostly correct with occasional grammatical errors or register inconsistencies that do not obscure meaning; or overuse of hedging language ("it may be argued that...") that pads without adding content |
| **2** | Poor | Multiple grammatical errors; significant register inconsistencies (mixing formal and casual in a contract); ambiguous drafting that a reader could reasonably misinterpret |
| **1** | Very poor | Barely professional; extensive errors; unclear what the output is trying to say |
| **0** | Fail | Wrong language (English output for an Arabic-input request) or completely incoherent |

## Sub-criteria

### Grammar and syntax
Basic correctness:
- Subject-verb agreement; pronoun-antecedent agreement.
- No dangling modifiers (especially in contract drafting where "as agreed by the Parties" must be unambiguous about what was agreed).
- Correct use of conditional constructions: "shall" (obligation), "may" (permission), "must" (strong obligation in modern drafting), "will" (future fact). Mixing these in a contract is a quality failure.
- Tense consistency: contracts are typically in present tense ("the Company shall pay"); analysis is typically in present tense for rules ("The law requires") and past tense for facts ("The contract stated").

### Legal register and vocabulary
English legal writing has two distinct registers:

**Formal drafting register** (contracts, letters before action, court submissions):
- Defined terms capitalized and in bold/italics on first introduction.
- No contractions ("doesn't", "can't") — use "does not", "cannot".
- No colloquialisms.
- "Shall" for obligations; avoid "will" for contractual obligations.
- Recitals begin "WHEREAS" or "BACKGROUND"; operative clauses begin with article numbers.

**Plain English register** (client advice, explanations, onboarding):
- Active voice preferred: "The law requires you to…" not "It is required by law that…"
- Short sentences: target ≤ 25 words per sentence in client-facing content.
- Define technical terms on first use: "EOSG (end-of-service gratuity)".
- No unexplained Latin or French legal phrases: "force majeure" should be glossed the first time it appears in client-facing content.

### Precision and unambiguity
Legal English must be unambiguous. Common precision failures:
- Vague pronoun references ("it" with multiple possible antecedents).
- Overloaded definitions ("Confidential Information means all information" — what does "all" include?).
- Ambiguous modification: "new employees and contractors" — are the contractors new too?
- Missing quantifiers: "within a reasonable time" — in a contract, specify days.

### Padding and filler
Common filler phrases that reduce quality without adding content:
- "It is important to note that…" — just state the point.
- "It should be mentioned that…" — just mention it.
- "Please be advised that…" — delete; just advise.
- "As per the above…" — refer to the specific clause.
- Excessive meta-commentary ("In order to fully answer your question, I will first…") in short advisory responses.

Excessive hedging is a quality failure: a response that says "I am not able to provide legal advice, but if I were to speculate, it might be possible that perhaps the law could require…" on a factual legal question is unhelpfully vague and scores ≤ 2.

### UK vs US English consistency
For DIFC/ADGM/UK matters, British English is conventional:
- "Labour" not "Labor"; "licence" (noun) not "license"; "organisation" not "organization".
- For UAE onshore, US English is not incorrect but inconsistency within a document is.
- Once a variant is chosen, stick to it throughout.

## Relationship to other rubrics

This rubric is orthogonal to legal accuracy. A grammatically perfect response that states the wrong law scores 5/5 here but 1/5 on [[eval-rubric-legal-soundness]]. A legally perfect response with 10 grammatical errors scores 5/5 on legal soundness but 2/5 here.

Use both rubrics together for a complete quality picture.

## Related skills

- [[eval-rubric-language-quality-ar]] — parallel rubric for Arabic language quality
- [[eval-llm-as-judge-system-prompt]] — applies this rubric in the evaluation pipeline
- [[eval-benchmark-runner]] — orchestrates scoring across all outputs
- [[eval-dataset-nda-prompts-30]] — English NDA drafts are a primary test surface for this rubric
