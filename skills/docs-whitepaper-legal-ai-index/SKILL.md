---
name: docs-whitepaper-legal-ai-index
description: Use when a reader asks about HAQQ's Legal AI Index — the quarterly benchmark measuring legal AI performance across jurisdictions, languages, and task types. Covers the methodology, evaluation dimensions, publication cadence (Q1–Q4), and the reproducible eval suite that lets practitioners and researchers validate the results. Useful for technical audiences, press, academic collaborators, and enterprise evaluators comparing AI tools on objective criteria.
license: MIT
metadata: " id: docs.whitepaper-legal-ai-index category: docs jurisdictions: [__multi__] priority: P2 intent: [legal AI benchmark, evaluation, index, performance metrics, research] related: [docs-whitepaper-general, docs-security-overview, docs-roi-calculator] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'docs'.
Registered as a flat plugin skill.
-->


# Legal AI Index — HAQQ Quarterly Benchmark Whitepaper

## What the Legal AI Index is

The HAQQ Legal AI Index is a quarterly publication benchmarking the performance of legal AI systems — including but not limited to Louis — across a standardized test suite of legal tasks. Its goals are:

1. **Transparency**: give legal professionals an objective basis for evaluating AI tools, rather than relying on vendor marketing.
2. **Accountability**: commit HAQQ to public, reproducible measurement of Louis's own performance.
3. **Research contribution**: provide a shared evaluation framework the academic legal-tech community can build on.
4. **MENA coverage**: be one of the first benchmarks to include Arabic-language legal tasks and MENA-jurisdiction legal questions as first-class evaluation dimensions.

## Publication cadence

| Edition | Coverage period | Target publication |
|---|---|---|
| Q1 | January – March | April |
| Q2 | April – June | July |
| Q3 | July – September | October |
| Q4 | October – December | January (following year) |

Each edition includes: new benchmark results, a methodology note on any changes to the eval suite, jurisdiction coverage updates, and a commentary section on observed trends.

## Methodology

### Task categories evaluated

| Category | Description | Example task |
|---|---|---|
| **Contract analysis** | Identify risk clauses, missing provisions, non-standard terms | "Find all liability cap deviations in this SPA" |
| **Legal drafting** | Generate a compliant first-draft document | "Draft an NDA under DIFC law" |
| **Regulatory QA** | Answer specific regulatory questions accurately | "What is the CDD threshold under UAE AML law?" |
| **Case/statute research** | Retrieve and summarize applicable law | "Summarize key provisions of KSA Labour Law on overtime" |
| **Bilingual tasks** | Arabic legal tasks and AR/EN bilingual document generation | "Draft an employment contract in Arabic and English" |
| **Translation quality** | Evaluate accuracy of Arabic ↔ English legal translation | Score against a reference translation by a qualified translator |

### Jurisdictions in scope

Current edition covers: UAE (onshore + DIFC + ADGM), KSA, Lebanon, Egypt, Qatar (QFC), Bahrain, and secondary coverage of UK, EU, and US for comparative benchmarking.

### Scoring dimensions

Each task is scored on:
- **Accuracy** (0–5): factual and legal correctness.
- **Completeness** (0–5): does the response cover all required elements?
- **Jurisdiction specificity** (0–5): does the response reflect the correct jurisdiction's law, not a generic or US-default answer?
- **Language quality** (0–5): for Arabic tasks, is the output in legal-register Arabic free of colloquialism and translation artifacts?
- **Hallucination rate**: percentage of responses containing fabricated statute numbers, case citations, or article numbers.

### Scoring panel

Results are evaluated by a panel including:
- Qualified lawyers admitted in the relevant jurisdiction.
- Legal linguists for Arabic-language tasks.
- A scoring rubric published alongside the results for reproducibility.

### Reproducible eval suite

The test prompts, scoring rubrics, and reference answers (where a ground truth exists) are published in a companion repository. Researchers and practitioners can:
- Run the eval suite against any model.
- Submit results to HAQQ for inclusion in future editions (with methodology disclosure).
- Fork and extend the suite for their own benchmarking.

## How to interpret the results

- **Scores are task-specific**: a model that performs well on US contract analysis may perform poorly on KSA regulatory QA.
- **Hallucination rate is the red-line metric**: for legal use, a model that fabricates statute numbers is dangerous regardless of its overall accuracy score.
- **Jurisdiction coverage gaps**: if a jurisdiction is not yet covered, do not infer performance from adjacent jurisdictions.
- **The Index benchmarks the AI output layer, not the full product**: a well-designed product (good prompting, good retrieval, human-in-the-loop review) may substantially outperform raw model benchmarks. Conversely, a high-scoring model used carelessly may underperform.

## How to obtain the whitepaper

Published at `https://haqq.ai/research/legal-ai-index`. Each edition is available as:
- PDF download (no registration required).
- Interactive results dashboard (registered users).
- Academic pre-print on request.

## Related skills

- [[docs-whitepaper-general]]
- [[docs-security-overview]]
- [[docs-roi-calculator]]
