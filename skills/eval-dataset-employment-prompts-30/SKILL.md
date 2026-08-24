---
name: eval-dataset-employment-prompts-30
description: Use when running the employment law benchmark that tests drafting, review, calculation, and advisory capabilities across LB/KSA/UAE/DIFC/UK/EU jurisdictions. Contains 30 prompts spanning contracts, termination, EOSG/EOSA calculations, non-compete analysis, and bilingual Arabic requests.
license: MIT
metadata: " id: eval.dataset.employment-prompts-30 category: eval priority: P0 intent: [__eval__, employment, benchmark, dataset, mena] related: [eval-benchmark-runner, eval-dataset-nda-prompts-30, eval-regression-detector, eval-rubric-legal-soundness, eval-rubric-jurisdiction-awareness] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'eval'.
Registered as a flat plugin skill.
-->


# Eval Dataset — Employment Prompts (30)

## Scope

30 employment-law prompts designed to benchmark the full range of employment AI capabilities across LB/KSA/UAE/DIFC/UK/EU. Employment law is one of the highest-demand practice areas in MENA (every company needs it), so quality here is directly tied to product-market fit. The EOSG/EOSA calculation prompts are particularly high-value — getting these wrong is an immediate trust failure.

Storage: `eval/datasets/employment-prompts-30.jsonl`

## How to use this pack

Same pipeline as [[eval-dataset-nda-prompts-30]]: load JSONL, run against production endpoint, score via [[eval-llm-as-judge-system-prompt]], aggregate, detect regressions in [[eval-regression-detector]].

Focus: after scoring, check that EOSG calculation prompts scored ≥ 4.0/5 on [[eval-rubric-legal-soundness]]. Calculation errors in this area are high-stakes.

## Prompt categories

### Category 1 — Drafting (10 prompts)
Contract and letter drafting across jurisdictions:

| # | Prompt type | Jurisdiction | Key signals to check |
|---|---|---|---|
| 1 | Employment contract (full) | UAE onshore | Probation ≤ 6 months, EOSG clause, Limited vs Unlimited contract |
| 2 | Employment contract (full) | DIFC | DIFC Employment Law compliance, at-will vs cause |
| 3 | Employment contract (full) | KSA | Saudi Nitaqat, Saudization %, 90-day probation |
| 4 | Employment contract (full) | Lebanon | Lebanese Labour Code, NSSF registration |
| 5 | Offer letter | UAE | Non-binding but professional; consistent with planned contract |
| 6 | Termination letter (with cause) | UAE | MOHRE process, 30-day notice (or pay in lieu) |
| 7 | Termination letter (redundancy) | UK | Statutory redundancy, selection criteria, consultation |
| 8 | Severance agreement | UAE | Waiver of EOSG claims; validity under UAE Labour Law |
| 9 | Non-compete clause | DIFC | 12-month max; geographic scope; consideration |
| 10 | Fixed-term contract | KSA | Auto-renewal rules; Saudi Labour Law Article 55 |

### Category 2 — Review (5 prompts)
Paste a contract extract and ask for risk analysis:

| # | Prompt type | Key signals |
|---|---|---|
| 11 | Review UAE employment contract — employer side | Identify probation clause trap, missing EOSG formula |
| 12 | Review UAE employment contract — employee side | Spot overly broad non-compete; missing end-of-service calc |
| 13 | Review DIFC employment contract | Check for DIFC Employment Law compliance gaps |
| 14 | Review non-compete clause — enforceability in KSA | KSA courts rarely enforce; flag risk |
| 15 | Review restrictive covenants — Lebanon | Limited enforceability under Lebanese law; flag |

### Category 3 — EOSG/EOSA Calculations (5 prompts)
End-of-service gratuity and allowance calculations with edge cases:

| # | Scenario | Key calculation notes |
|---|---|---|
| 16 | UAE: 7 years, terminated without cause, AED 25,000/month | Full formula: 21 days × 5 years + 30 days × 2 years; Article 51 UAE Labour Law |
| 17 | UAE: 3 years, resigned voluntarily | 1/3 of full gratuity for resignation 1–3 years |
| 18 | UAE: 6 years, resigned voluntarily | 2/3 of full gratuity for resignation 3–5 years |
| 19 | DIFC: 5 years, terminated | DIFC Employment Law basic wage × years; different formula from onshore |
| 20 | KSA: 10 years, terminated | 1/2 month per year for first 5 + 1 month per year after; Saudi Labour Law |

### Category 4 — Advisory (5 prompts)
Practical employment law questions:

| # | Scenario | Key signals |
|---|---|---|
| 21 | "Can I dismiss an employee on sick leave in the UAE?" | UAE: protected periods; medical leave rules |
| 22 | "What is the process for collective redundancy in the UK?" | TULRCA 1992; 45 days for 100+ employees |
| 23 | "Does a non-compete in Lebanon prevent my employee from joining a competitor?" | Very limited enforceability; case-by-case |
| 24 | "Can we put a UAE employee on unpaid leave due to business slowdown?" | Requires consent; Article 31 UAE Labour Law |
| 25 | "How many annual leave days does a DIFC employee get?" | DIFC: 20 days minimum after 1 year |

### Category 5 — Jurisdiction comparison (3 prompts)

| # | Prompt | Key signals |
|---|---|---|
| 26 | "Compare non-compete enforceability in UAE, KSA, and DIFC" | UAE onshore: moderate; KSA: low; DIFC: higher (common law) |
| 27 | "How does the probation period differ between UAE onshore and DIFC?" | UAE: 6 months max; DIFC: 6 months, different termination rights during probation |
| 28 | "What are the EOSG differences between UAE onshore and Abu Dhabi free zone?" | May differ by free zone regulations |

### Category 6 — Bilingual Arabic (2 prompts)

| # | Prompt | Key signals |
|---|---|---|
| 29 | Arabic-language request for UAE employment contract | Arabic output, correct legal terminology (عقد العمل، مكافأة نهاية الخدمة) |
| 30 | Arabic: "ما هي حقوق موظف في حالة الفصل التعسفي في الإمارات؟" | Answer in Arabic, UAE Labour Law reference |

## Scoring targets

| Category | Min acceptable score (legal soundness) |
|---|---|
| Drafting | ≥ 4.0 / 5 |
| Review | ≥ 3.5 / 5 |
| Calculation | ≥ 4.5 / 5 (calculation errors are high-impact) |
| Advisory | ≥ 3.5 / 5 |
| Comparison | ≥ 3.5 / 5 |
| Arabic | ≥ 3.5 / 5 language quality + ≥ 3.5 legal soundness |

## Caveats & currency

Employment law in MENA changes frequently. UAE Labour Law (Federal Decree-Law No. 33 of 2021) replaced the previous law; update prompts when further amendments are issued. KSA Labour Law has undergone significant reform since 2021. Review and update this dataset annually or when a major legislative change occurs.

## Related skills

- [[eval-benchmark-runner]] — runs this dataset in the full eval pipeline
- [[eval-dataset-nda-prompts-30]] — parallel dataset for NDA tasks (same pipeline)
- [[eval-rubric-legal-soundness]] — primary scoring rubric
- [[eval-rubric-jurisdiction-awareness]] — critical for the cross-jurisdiction comparison prompts
