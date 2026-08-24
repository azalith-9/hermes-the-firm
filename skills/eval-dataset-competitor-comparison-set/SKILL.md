---
name: eval-dataset-competitor-comparison-set
description: Use when running or interpreting the competitor comparison benchmark that measures the legal AI system's output quality against comparable tools on standardized legal tasks. Provides structured side-by-side scoring methodology, output dimensions, and the MENA-jurisdiction coverage gap analysis that differentiates this system.
license: MIT
metadata: " id: eval.dataset.competitor-comparison-set category: eval jurisdictions: [__multi__] priority: P2 intent: [__eval__, competitor, benchmarking, quality, differentiation] related: [eval-benchmark-runner, eval-rubric-legal-soundness, eval-rubric-jurisdiction-awareness, eval-rubric-hallucination-detection, eval-leaderboard-updater] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'eval'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Eval Dataset — Competitor Comparison Set

## Scope

A curated set of legal AI prompts run against this system and comparable legal AI tools (Harvey, Clio Duo, LexisNexis AI, generic the agent/GPT-4o) to produce a structured quality comparison. The primary hypothesis: this system outperforms general-purpose LLMs and US-centric legal AI tools on MENA-jurisdiction tasks (UAE, KSA, Lebanon, DIFC/ADGM) while being competitive on standard tasks.

Results feed [[eval-leaderboard-updater]] and the weekly AI quality trend report.

## How to use this pack

1. Select 20–30 prompts from the comparison set (see categories below).
2. Run each prompt through:
   - This system (production endpoint)
   - The baseline tool(s) (API or UI, documented)
3. Score each output with [[eval-llm-as-judge-system-prompt]] using [[eval-rubric-legal-soundness]], [[eval-rubric-jurisdiction-awareness]], and [[eval-rubric-hallucination-detection]].
4. Record scores and qualitative notes in the comparison spreadsheet.
5. Publish to the internal leaderboard monthly.

Never publish raw competitor output without legal review of their terms of service regarding benchmarking.

## Dataset categories

### Category A — MENA-jurisdiction tasks (primary differentiator, 10 prompts)
Tasks where MENA-specific knowledge matters:

| Prompt type | Sample prompt | Why it differentiates |
|---|---|---|
| EOSG calculation | "Calculate end-of-service gratuity for a UAE employee on AED 25,000/month with 7 years' service, terminated without cause." | DIFC vs onshore formula differs; generic LLMs conflate |
| DIFC contract review | "Review this clause for compliance with DIFC Contract Law." | US/UK tools apply wrong statute |
| Lebanese Commercial Code | "What are the notice requirements for dissolving a Lebanese LLC under the Commercial Code?" | Obscure to general tools |
| Notarization requirement | "Does this MOU need to be notarized (Tawtheeq) in Abu Dhabi to be enforceable?" | Tawtheeq nuance absent from US-centric tools |
| Arabic legal drafting | "Draft a non-disclosure clause in Arabic for use in a Saudi Arabia agreement." | Arabic output quality gap |

### Category B — Standard legal tasks (parity check, 10 prompts)
Tasks where all tools should perform comparably:

- Draft a mutual NDA under New York law.
- Summarize the material adverse change clause in this M&A agreement.
- What is the statute of limitations for breach of contract in England & Wales?
- Flag missing clauses in this employment contract.
- Explain the difference between an indemnity and a guarantee.

Scoring on these tasks validates that MENA specialization did not degrade baseline competence.

### Category C — Hallucination resistance (5 prompts)
Prompts that invite fabrication:
- "Cite the leading DIFC Court case on force majeure." (real cases exist; test if sources are accurate)
- "What does the SAMA circular on crypto custody say?" (real document exists; test accuracy)

These measure citation accuracy, not just refusal. A wrong-but-confident citation is worse than an admission of uncertainty.

### Category D — Tone and usability (5 prompts)
Prompts evaluated on response quality beyond legal accuracy:
- Explanation of a complex concept to a non-lawyer client.
- Structured comparison table of jurisdiction options.
- Bilingual (AR/EN) clause drafting.

## Scoring dimensions

For each prompt, record:

| Dimension | Method | Scale |
|---|---|---|
| Legal soundness | LLM judge using [[eval-rubric-legal-soundness]] | 0–5 |
| Jurisdiction accuracy | LLM judge using [[eval-rubric-jurisdiction-awareness]] | 0–5 |
| Hallucination | [[eval-rubric-hallucination-detection]] | clean / hallucinated / uncertain |
| Response completeness | LLM judge using [[eval-rubric-completeness]] | 0–5 |
| Language quality | Human rater for Arabic; LLM for EN | 0–5 |
| Time to first token (ms) | Measured | ms |

## Caveats & currency

- Competitor tools update frequently; scores can shift without any change to this system. Re-run quarterly.
- The comparison is directional, not definitive. Methodology differences (prompt wording, system prompt visibility, temperature) affect results.
- Do not use competitor output in marketing materials without legal review.
- This dataset is for internal improvement signal, not for published claims.

## Related skills

- [[eval-benchmark-runner]] — runs this dataset as part of the CI eval suite
- [[eval-rubric-legal-soundness]] — primary quality scoring rubric
- [[eval-rubric-jurisdiction-awareness]] — MENA jurisdiction gap measurement
- [[eval-leaderboard-updater]] — records scores to the internal trend dashboard
