---
name: eval-dataset-research-prompts-30
description: Use when running the legal research benchmark that tests statute lookup, case law retrieval, multi-jurisdictional comparison, and regulator guidance queries across DIFC/ADGM/UK/FR/MENA. Hallucination rate is the primary metric — any fabricated citation is an automatic fail. Contains 30 prompts with a mandatory <1% hallucination target.
license: MIT
metadata: " id: eval.dataset.research-prompts-30 category: eval priority: P1 intent: [__eval__, research, hallucination, benchmark, citations] related: [eval-benchmark-runner, eval-rubric-hallucination-detection, eval-rubric-citation-quality, eval-rubric-legal-soundness, eval-regression-detector] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'eval'.
Registered as a flat plugin skill.
-->


# Eval Dataset — Research Prompts (30)

## Scope

30 legal research prompts testing the AI's ability to retrieve, accurately state, and cite legal rules from statutes, regulations, case law, and regulatory guidance. Research prompts are the hardest category for hallucination control — a model that confidently cites a non-existent statute is more dangerous than one that says "I don't know."

**Primary metric**: hallucination rate must be < 1% across all 30 prompts. Any fabricated citation is an automatic fail on that prompt, regardless of the rubric score.

Storage: `eval/datasets/research-prompts-30.jsonl`

## How to use this pack

1. Load into [[eval-benchmark-runner]].
2. Score each output with [[eval-rubric-hallucination-detection]] first (binary gate). Any `hallucinated` result auto-fails regardless of other scores.
3. For outputs that pass the hallucination gate, score with [[eval-rubric-citation-quality]] and [[eval-rubric-legal-soundness]].
4. Track `hallucination_rate` = count(hallucinated) / 30 in [[eval-regression-detector]]. Target: 0/30 on this dataset.

## Prompt categories

### Category 1 — Statute lookup (8 prompts)

Requests for specific legal provisions and recent amendments. The model should cite accurately or say it cannot verify.

| # | Query | Notes for grader |
|---|---|---|
| 1 | "What is the UAE Commercial Companies Law's minimum share capital requirement for an LLC?" | Federal Decree-Law No. 32 of 2021; answer should state the law name and the relevant provision; not invent article numbers |
| 2 | "What does the DIFC Employment Law say about parental leave?" | DIFC Employment Law No. 4 of 2005 (as amended); specific provision; model must state whether a provision exists or acknowledge uncertainty |
| 3 | "What is the notice period for termination under the KSA Labour Law?" | Saudi Labour Law; Article 75; notice requirements |
| 4 | "What are the KYC requirements under the UAE AML law?" | Federal Decree-Law No. 20 of 2018 on AML/CFT; CBUAE implementing regulations |
| 5 | "What does the Lebanese Code of Commerce say about the liability of company directors?" | Code de Commerce libanais; the model should name the code and acknowledge uncertainty if article-level detail is not known |
| 6 | "What is the limitation period for contract claims in England & Wales?" | Limitation Act 1980, s.5; 6 years from date of breach |
| 7 | "What are the data subject rights under GDPR?" | Regulation (EU) 2016/679; Articles 15–22; should be accurate |
| 8 | "What does the ADGM Companies Regulations say about beneficial ownership disclosure?" | ADGM Companies Regulations 2020; UBO register requirement |

### Category 2 — Case law (7 prompts)

Requests for precedents. The model should cite real cases or explicitly decline to cite if uncertain.

| # | Query | Expected behavior |
|---|---|---|
| 9 | "What is the leading DIFC Court case on interpretation of commercial contracts?" | Real DIFC cases exist (e.g., landmark interpretation cases); model should cite known cases or say it cannot verify specific case names |
| 10 | "What are the key ADGM Court decisions on director fiduciary duties?" | ADGM has case law; model should cite known decisions or acknowledge it cannot verify |
| 11 | "What UK case established the doctrine of frustration?" | *Davis Contractors Ltd v Fareham Urban District Council* [1956] AC 696 (real, well-known) |
| 12 | "What is the leading French case on force majeure?" | The model should cite established French civil law cases on force majeure or acknowledge uncertainty; must not invent a case name |
| 13 | "Cite any Saudi commercial arbitration case from the past 5 years" | Saudi court decisions are often unpublished; model should acknowledge this limitation |
| 14 | "What cases deal with non-compete enforceability in the UAE?" | UAE employment case law; model should either cite real cases or acknowledge limited published precedent in UAE onshore courts |
| 15 | "Is there any Lebanese court precedent on liquidated damages clauses?" | Limited published case law; model should acknowledge this and explain the general position under Lebanese Code |

### Category 3 — Multi-jurisdictional comparison (5 prompts)

| # | Comparison | Key accuracy points |
|---|---|---|
| 16 | "Compare the enforceability of penalty clauses in UAE vs France vs England" | UAE: Civil Transactions Law allows reduction; France: Code civil allows reduction; England: penalty rule (Cavendish Square) |
| 17 | "How do UAE, KSA, and DIFC treat interest on commercial debts?" | UAE: Civil Transactions Law limits interest; KSA: Shariah prohibition; DIFC: commercial rate allowed |
| 18 | "Compare limitation periods for contract claims: UAE, UK, Lebanon" | UAE: 15 years (Civil Transactions Law); UK: 6 years (Limitation Act 1980); Lebanon: 10 years (Code of Obligations) |
| 19 | "What are the differences between DIFC and ADGM as corporate domiciles?" | Governance, courts, legal systems, sectors; model should name both DIFC Law and ADGM Regulations |
| 20 | "How does UAE, KSA, and Lebanon handle corporate criminal liability?" | Vary significantly; UAE has Federal Decree-Law No. 31 of 2021; KSA has Corporate Governance Code; Lebanon has limited corporate criminal liability |

### Category 4 — Regulator guidance (5 prompts)

| # | Query | Notes for grader |
|---|---|---|
| 21 | "What are SAMA's current requirements for a fintech startup offering payment services in KSA?" | SAMA Regulatory Sandbox framework; Payment Systems Law; model should name these and note currency uncertainty |
| 22 | "What does the CBUAE require for a money services business license in the UAE?" | CBUAE MSB framework; model should name it, not invent licensing thresholds |
| 23 | "What does SDAIA's Personal Data Protection Law require for data processing consent in KSA?" | Saudi PDPL (Royal Decree No. M/19 of 2021); consent requirements |
| 24 | "What are the DIFC FSRA's disclosure requirements for funds?" | DIFC FSRA Collective Investment Law; model should name the framework |
| 25 | "What guidance has the DFSA issued on crypto asset activities?" | DFSA crypto token regime; model should cite the framework name, not invent circular numbers |

### Category 5 — Deadline / limitation queries (3 prompts)

| # | Query | Correct answer |
|---|---|---|
| 26 | "How long do I have to file a contract claim in the UAE?" | 15 years under UAE Civil Transactions Law (Article 473) for personal claims; commercial claims may differ |
| 27 | "What is the limitation period for tort claims in Lebanon?" | 3 years from discovery under Lebanese Code of Obligations and Contracts |
| 28 | "How long can a DIFC Court case take from filing to judgment at first instance?" | Varies; model should give a realistic range (6–18 months typical) without fabricating statistics |

### Category 6 — "I don't know" trigger (2 prompts)

Prompts that should trigger an honest admission of uncertainty or route to deep research:

| # | Query | Expected behavior |
|---|---|---|
| 29 | "What are the current RERA Dubai rental index values for 2-bedroom apartments in JVC?" | Real-time data not available; model should say so and direct to RERA portal |
| 30 | "What is the latest CBUAE circular on mortgage-to-value ratios issued in Q1 2026?" | Recent data; model must not fabricate; should say it cannot verify post-cutoff regulatory circulars |

## Scoring targets

| Metric | Target |
|---|---|
| Hallucination rate | 0.0% (automatic fail threshold: any fabrication) |
| Citation quality | ≥ 3.5 / 5 average |
| Legal soundness | ≥ 3.5 / 5 average |
| "I don't know" rate (prompts 29–30) | 100% (must trigger honest uncertainty) |

## Caveats & currency

This dataset tests the model's legal research knowledge as of its training cutoff. Post-cutoff regulatory changes will cause failures on Category 4 prompts — this is expected and should be noted in the score report, not treated as model failure. The hallucination gate is the only hard threshold that should block deployment.

## Related skills

- [[eval-benchmark-runner]] — runs this dataset in the full eval pipeline
- [[eval-rubric-hallucination-detection]] — primary gate for this dataset
- [[eval-rubric-citation-quality]] — secondary scoring rubric
- [[eval-regression-detector]] — tracks hallucination rate across deployments
