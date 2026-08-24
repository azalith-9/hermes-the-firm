---
name: eval-rubric-legal-soundness
description: Use when scoring AI legal output on whether it correctly states the law and applies it correctly to the facts presented. A 0–5 rubric covering rule statement accuracy, application reasoning, citation reliability, jurisdiction fit, and currency of the law. The primary quality rubric and a deployment blocking gate if it drops significantly.
license: MIT
metadata: " id: eval.rubric.legal-soundness category: eval priority: P0 intent: [__eval__, legal-accuracy, rubric, soundness, quality] related: [eval-rubric-citation-quality, eval-rubric-jurisdiction-awareness, eval-rubric-completeness, eval-rubric-hallucination-detection, eval-llm-as-judge-system-prompt, eval-benchmark-runner] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'eval'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Eval Rubric — Legal Soundness (0–5)

## When to use this

Apply to every legal AI output that makes substantive legal assertions — analysis, advice, research, and drafting. Legal soundness is the primary quality dimension: a well-written response stating wrong law is dangerous; a poorly formatted response stating correct law is at least safe to act on.

This rubric is a **deployment blocking gate**: if the aggregate legal soundness score drops > 3% vs the previous run, [[eval-regression-detector]] blocks the deployment for investigation.

Run via [[eval-llm-as-judge-system-prompt]] using an ensemble of judge models.

## Scoring (0–5)

| Score | Label | Criteria |
|---|---|---|
| **5** | Excellent | All legal propositions correctly stated; citations real and accurate; application reasoning sound and properly tied to the stated facts; counter-arguments or alternative interpretations addressed where they exist; law is current as of the response date |
| **4** | Good | Legal propositions mostly correct; minor citation inaccuracy (formatting issue or slightly wrong article number) or one missed nuance that does not materially affect the conclusion |
| **3** | Acceptable | Substantial correct content with at least one moderate error — a wrong article number, a missed exception to a rule, or an application that reaches the right conclusion by imperfect reasoning |
| **2** | Poor | Significant legal errors or missing an applicable rule that would materially change the advice; would mislead a practitioner who relies on it without independent verification |
| **1** | Very poor | Multiple serious errors; foundational rule stated wrong; wrong law applied to the jurisdiction |
| **0** | Wrong / harmful | Materially incorrect to the point of being dangerous to act on — e.g., stating that a type of clause is enforceable when it is void in the stated jurisdiction; advising that no formality is required when notarization is mandatory |

## Sub-criteria

### Rule statement
Is the cited rule the right one, and is it correctly articulated?
- Is the legal rule identified at the right level of specificity? (Not just "UAE law governs" but the specific statute and principle)
- Is the rule accurately paraphrased? (Not overstated, not understated)
- Are exceptions to the rule mentioned where they are material?
- Is the rule the one that actually applies to the stated facts? (Not a general principle when a specific rule exists)

### Application
Does the analysis correctly apply the rule to the facts?
- Is the application logical? Does it follow from the stated rule?
- Are key counter-considerations addressed? (e.g., "The contract says X, but UAE courts have the power to modify penalty clauses under Article 390 of the Civil Transactions Law")
- Is the conclusion justified by the stated rule and facts?

### Citations
Are the cited authorities real, correctly attributed, and not fabricated?
(Note: deep citation quality analysis is in [[eval-rubric-citation-quality]]; this sub-criterion is a light check to catch obvious hallucinations)

### Jurisdiction fit
Does the answer cover the right jurisdiction?
(Note: deep jurisdiction analysis is in [[eval-rubric-jurisdiction-awareness]]; this sub-criterion catches cases where clearly wrong law is applied)

### Currency
Is the law as stated current as of the response date?
- Laws that have been repealed or significantly amended without acknowledgment score lower.
- A response that cites the old UAE Labour Law (Federal Law No. 8 of 1980) without noting it was replaced by Federal Decree-Law No. 33 of 2021 scores ≤ 3.
- For post-training-cutoff changes: the model is not expected to know, but must say "as of my knowledge cutoff" when there is reasonable risk of change.

## MENA-specific legal soundness checkpoints

The following are common failure points for generic LLMs on MENA legal matters — grade strictly on these:

| Issue | Failure mode |
|---|---|
| EOSG calculation | Wrong formula (21-day vs 30-day, partial vs full for short tenure); ignoring DIFC vs onshore distinction |
| Penalty clauses | Stating they are per se enforceable without noting UAE/Lebanon courts' power to reduce |
| Non-competes | Stating they are easily enforceable in KSA (they are not) |
| Interest | Not flagging Shariah prohibition in KSA; not noting UAE Civil Transactions Law position |
| Company formation | Confusing DIFC, ADGM, onshore, and free-zone rules |
| Property ownership | Not flagging foreign ownership restrictions in UAE onshore / KSA |
| Choice of law | Not noting that UAE Labour Law protections cannot be waived by choice of foreign law for UAE-sited employees |

Outputs that make any of these errors score ≤ 3 on legal soundness regardless of overall quality.

## Use in automated scoring

Inject this rubric definition into [[eval-llm-as-judge-system-prompt]]. Weight it 0.35 (highest weight) in the composite score:

```
composite_score = 0.35 × legal_soundness
               + 0.20 × citation_quality
               + 0.20 × jurisdiction_awareness
               + 0.15 × completeness
               + 0.10 × (binary hallucination gate)
```

## Limits & escalation

A legal soundness score alone does not determine whether an output is safe to act on. Always pair with [[eval-rubric-hallucination-detection]] (existence gate) and [[eval-rubric-jurisdiction-awareness]] (applicability gate). A score of 4/5 on legal soundness from a model that regularly fabricates citations is meaningless without the hallucination gate.

## Related skills

- [[eval-rubric-citation-quality]] — deep citation quality analysis
- [[eval-rubric-jurisdiction-awareness]] — jurisdiction accuracy
- [[eval-rubric-completeness]] — whether all applicable rules were addressed
- [[eval-rubric-hallucination-detection]] — binary fabrication gate
- [[eval-llm-as-judge-system-prompt]] — applies this rubric in the automated pipeline
- [[eval-benchmark-runner]] — runs this rubric across all benchmark datasets
