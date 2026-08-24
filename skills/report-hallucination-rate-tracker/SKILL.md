---
name: report-hallucination-rate-tracker
description: Use when the product or quality team needs to measure, track, and trend the rate at which the AI assistant generates fabricated legal content — false citations, invented statute numbers, nonexistent cases, or wrong regulatory thresholds — broken down by skill, model, and jurisdiction. This is an internal quality-assurance report. Trigger on the weekly quality-review schedule or whenever a concerning spike in user-reported errors is observed.
license: MIT
metadata: " id: report.hallucination-rate-tracker category: report jurisdictions: [__multi__] priority: P3 intent: [__internal__, hallucination, quality-assurance, eval, llm-judge] related: [report-weekly-ai-quality-trend, report-competitor-output-comparison-weekly, eval-output-quality, ref-vocabulary] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'report'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Hallucination Rate Tracker — Weekly Report

Internal quality-assurance report tracking the rate at which the AI assistant produces legally false content. Hallucination in a legal AI product is not a UX inconvenience — it is a professional-liability risk and the primary reason users stop trusting the product.

## Why this matters

A lawyer who acts on a fabricated statute loses in court, or worse, misleads a client. Even a single confirmed hallucination — a case citation that doesn't exist, an article number with the wrong content, a regulatory threshold that is off by an order of magnitude — can end a firm's relationship with the product. Tracking hallucination rate weekly enables:

- Early detection of regression when models are updated
- Identification of which skill categories carry the highest fabrication risk
- Validation that grounding / RAG improvements are working
- Evidence for compliance and due-diligence conversations with enterprise clients

## Sampling methodology

### Sample size
100 conversations per week, drawn from:
- Production traffic (random sample, anonymized, PII-stripped)
- Synthetic benchmark prompts (the fixed eval set)

### Stratification
Ensure the sample is stratified by:
- **Skill category**: at least 10% from each major category (research, review, draft, kb)
- **Jurisdiction**: at minimum one slice each for LB, KSA, UAE-onshore, DIFC, ADGM, and one non-MENA
- **Model version**: if multiple models are in rotation, sample proportionally

### Selecting conversations with citation-risk
Not every conversation can produce a hallucination — a purely procedural task has low risk. Pre-filter for conversations that:
- Contain a specific statute or regulation name
- Reference a case or ruling
- State a numerical threshold (penalty amount, limitation period, ownership percentage)
- Name a specific regulatory body and an attributed position

## Verification protocol

### For each flagged assertion

1. **Identify the claim**: Extract the precise factual assertion (e.g., "Article 14 of UAE Federal Decree-Law No. 33 of 2021 limits non-compete duration to two years").
2. **Primary-source check**: Verify against the canonical authoritative source (official gazette, DIFC Laws portal, BOE, etc.). Do not verify against secondary commentary — only primary sources count.
3. **Classify the finding**:
   - **Verified correct**: assertion matches primary source verbatim or in substance
   - **Plausible, unverified**: claim sounds reasonable but could not be confirmed against primary source (counts as half-hallucination for rate purposes — signals a RAG gap)
   - **Confirmed hallucination**: assertion is demonstrably wrong — wrong article number, nonexistent case, wrong threshold, wrong jurisdiction rule

### Double-check method
Every "confirmed hallucination" classification requires:
- Manual expert check (a lawyer familiar with the jurisdiction), AND
- LLM-judge second opinion using the verification prompt:

```
You are a legal fact-checker. Here is an assertion: [assertion]. 
Here is the relevant primary source text: [retrieved text].
Does the assertion accurately reflect the source? Answer: ACCURATE / INACCURATE / CANNOT VERIFY. 
Explain your reasoning in one sentence.
```

The LLM-judge result is logged but a human expert has final say on classification.

## Output format

### Weekly summary header
```
Week: [ISO week + dates]
Sample: [N conversations, X containing citation-risk assertions]
Model version(s): [list]

Overall hallucination rate: X% (N confirmed / Y assertions checked)
Change vs last week: ▲/▼ X pp
Change vs 4-week avg: ▲/▼ X pp
```

### Rate by skill category

| Skill category | Assertions checked | Confirmed hallucinations | Rate |
|----------------|-------------------|--------------------------|------|
| research — statute lookup | N | N | X% |
| research — case law | N | N | X% |
| research — regulation | N | N | X% |
| draft | N | N | X% |
| review | N | N | X% |
| kb / ref | N | N | X% |
| **Total** | **N** | **N** | **X%** |

### Rate by jurisdiction

| Jurisdiction | Assertions checked | Confirmed hallucinations | Rate | Notable pattern |
|---|---|---|---|---|
| LB | N | N | X% | |
| KSA | N | N | X% | |
| UAE-onshore | N | N | X% | |
| DIFC | N | N | X% | |
| ADGM | N | N | X% | |
| EU/FR | N | N | X% | |
| Other | N | N | X% | |

### Top-5 confirmed hallucinations this week
For each:
- Skill that produced it
- The fabricated assertion (verbatim)
- What the primary source actually says
- Root-cause hypothesis (training cutoff gap? RAG miss? prompt induced fabrication?)
- Remediation action (skill update, KB update, RAG index update, model guardrail)

## Alert thresholds

| Metric | Yellow alert | Red alert — escalate immediately |
|--------|-------------|----------------------------------|
| Overall weekly rate | > 3% | > 7% |
| Any single skill rate | > 5% | > 12% |
| Any single jurisdiction | > 8% | > 15% |
| Week-on-week delta | > +2 pp | > +5 pp |

Red-alert triggers a same-day incident review. If the affected skill is in production, consider disabling it until root cause is addressed.

## Remediation workflow

1. **Identify root cause**: RAG miss (document not indexed), training cutoff (law changed after training), prompt design flaw (model is encouraged to speculate), or model-specific tendency.
2. **Fix**: Update KB / RAG index → re-test on eval set → deploy if rate improves.
3. **Verify**: Next week's tracker must show rate improvement in the affected category.
4. **Post-mortem**: For any confirmed hallucination that reached a paying user, write a one-paragraph post-mortem and log it in the incident register.

## Related skills

- [[report-weekly-ai-quality-trend]]
- [[report-competitor-output-comparison-weekly]]
- [[eval-output-quality]]
- [[ref-vocabulary]]
- [[router-confidence-scorer]]
