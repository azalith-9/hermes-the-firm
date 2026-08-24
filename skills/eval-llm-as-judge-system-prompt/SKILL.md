---
name: eval-llm-as-judge-system-prompt
description: Use when configuring or invoking the LLM-as-judge evaluation system that scores legal AI outputs against multiple rubrics. Provides the canonical system prompt template, JSON output schema, ensemble configuration, and bias mitigation rules for automated quality scoring of legal AI responses.
license: MIT
metadata: " id: eval.LLM-as-judge-system-prompt category: eval priority: P0 intent: [__eval__, llm-judge, scoring, rubric, automated-eval] related: [eval-benchmark-runner, eval-rubric-legal-soundness, eval-rubric-citation-quality, eval-rubric-jurisdiction-awareness, eval-rubric-completeness, eval-rubric-hallucination-detection, eval-regression-detector] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'eval'.
Registered as a flat plugin skill.
-->


# LLM-as-Judge System Prompt

## When to use this

Use whenever an LLM is being invoked to evaluate another LLM's output in the legal AI evaluation pipeline. This system prompt is the contract between the benchmark runner and the judge model. It must be applied consistently across all judge invocations so that scores are comparable across runs.

Invoke via [[eval-benchmark-runner]] — do not call judge models directly without this prompt.

## Inputs

| Input | Required | Notes |
|---|---|---|
| User prompt | Yes | The original prompt sent to the system under test |
| AI response | Yes | The system's output to be judged |
| Active rubrics | Yes | Array of rubric definitions (from the rubric skills) |
| Jurisdiction context | Optional | Helps the judge apply the correct legal standard |
| Expected signals | Optional | From the dataset — helps judge detect missing elements |

## System prompt template

```
You are a senior legal AI quality evaluator. Your task is to score an AI legal assistant's response against a set of rubrics.

You will be given:
- The user prompt
- The AI response
- A list of rubrics, each with a name and scoring guide

IMPORTANT RULES:
1. Be strict on citation quality and hallucination. Any fabricated legal source (invented case name, invented statute number, invented article reference) is an automatic score of 0 on the citation_quality rubric regardless of other quality.
2. Evaluate jurisdiction accuracy as stated by the response — if the response applies the wrong jurisdiction's law, score jurisdiction_awareness ≤ 2.
3. Score based on what a competent legal practitioner in the relevant jurisdiction would expect. Do not inflate scores for responses that are well-written but legally incomplete.
4. Do not reward excessive hedging — a response that says "you should consult a lawyer" without providing any substantive analysis fails on completeness.
5. A response that partially answers the question scores proportionally — do not give 4/5 for a response that addresses only 70% of the question.

For each rubric, output a numeric score (per the rubric's scale) and a one-sentence rationale.

Then output an overall pass/fail and a 2–3 sentence summary highlighting the most important strengths and weaknesses.

Output format (JSON):
{
  "rubrics": {
    "legal_soundness": { "score": <0-5>, "rationale": "<one sentence>" },
    "citation_quality": { "score": <0-5>, "rationale": "<one sentence>" },
    "jurisdiction_awareness": { "score": <0-5>, "rationale": "<one sentence>" },
    "completeness": { "score": <0-5>, "rationale": "<one sentence>" },
    "hallucination": { "result": "clean" | "hallucinated" | "uncertain", "notes": "<if not clean, describe>" }
  },
  "overall": "pass" | "fail",
  "summary": "<2-3 sentences on strengths and key weakness>"
}

Pass/fail rule: fail if hallucination = "hallucinated", OR if legal_soundness ≤ 1, OR if jurisdiction_awareness = 0.
```

## Ensemble configuration

Run three judges per output; average numeric scores; use majority vote for `overall` pass/fail.

Recommended ensemble:
- GPT-4o (OpenAI)
- Gemini 1.5 Pro (Google)
- One of: Mistral Large, Command R+ (Cohere), or Llama 3.1 70B

**Do not use the agent as a judge when the system under test is also the agent** — same-family judging introduces a well-documented bias toward higher scores. If only one judge model is available, use a different provider than the system under test.

Judge models must be called with `temperature: 0` for reproducible scores.

## Bias mitigation rules

| Bias | Mitigation |
|---|---|
| Same-family bias (the agent judging the agent) | Always include at least one non-the agent judge; weight non-same-family judges 60% |
| Verbosity bias (longer = higher score) | Rubric for completeness explicitly checks whether all *required* elements are present, not whether the response is long |
| Formatting bias (well-structured = higher score) | Legal soundness rubric scores on legal accuracy, not presentation |
| Recency bias (latest info = better) | Jurisdiction awareness rubric allows for acknowledged uncertainty about post-cutoff changes |
| Language bias (English outputs scored higher) | For Arabic/French outputs, use a judge model that has strong multilingual capability; supplement with [[eval-rubric-language-quality-ar]] |

## Configured in Langfuse

The system prompt is stored as a Langfuse prompt named `llm-judge-v2` with variable injection points for the rubric definitions. Bind it to the rubric files in [[eval-rubric-legal-soundness]], [[eval-rubric-citation-quality]], etc. at the Langfuse prompt level, not in application code.

Update the Langfuse prompt version when the system prompt changes; old runs retain their prompt version for auditability.

## Caveats & currency

- Recalibrate against human gold-standard labels **quarterly**. Human lawyers should score a random sample of 50 outputs; compare to LLM judge scores. Calibrate if mean divergence > 0.5 points.
- LLM judges improve as underlying models improve. Reassess judge model selection annually.
- For the adversarial dataset ([[eval-dataset-adversarial-prompts]]), supplement with rule-based checks (refusal detected: yes/no) — LLM judges can be fooled by cleverly-framed jailbreaks that they also fall for.

## Related skills

- [[eval-benchmark-runner]] — calls this system prompt for each response in the eval pipeline
- [[eval-rubric-legal-soundness]] — rubric injected into this prompt
- [[eval-rubric-citation-quality]] — rubric injected into this prompt
- [[eval-rubric-jurisdiction-awareness]] — rubric injected into this prompt
- [[eval-rubric-completeness]] — rubric injected into this prompt
- [[eval-rubric-hallucination-detection]] — rubric injected into this prompt
- [[eval-regression-detector]] — consumes the scores this prompt produces
