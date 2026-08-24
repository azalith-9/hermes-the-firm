---
name: eval-dataset-real-estate-prompts-30
description: Use when running the real estate law benchmark across UAE/KSA/Lebanon covering drafting, review, compliance (RERA/Ejari/Tawtheeq/Ejar), disputes, and property tax questions. Contains 30 prompts that test jurisdiction-specific rules including foreign ownership restrictions, RETT, and VAT on commercial rentals.
license: MIT
metadata: " id: eval.dataset.real-estate-prompts-30 category: eval priority: P1 intent: [__eval__, real-estate, property, benchmark, mena] related: [eval-benchmark-runner, eval-dataset-nda-prompts-30, eval-rubric-legal-soundness, eval-rubric-jurisdiction-awareness, eval-regression-detector] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'eval'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Eval Dataset — Real Estate Prompts (30)

## Scope

30 real-estate-law prompts across UAE (onshore, DIFC, Abu Dhabi, Dubai), KSA, and Lebanon. Real estate is the second-highest-demand practice area in MENA legal markets, and it has a dense set of jurisdiction-specific regulatory requirements (RERA, Ejari, Tawtheeq, Ejar, Oqood, foreign ownership rules, RETT, VAT) that generic AI tools get wrong. Quality on this dataset is a key differentiator.

Storage: `eval/datasets/real-estate-prompts-30.jsonl`

## How to use this pack

Same pipeline as [[eval-dataset-nda-prompts-30]]: load, run, score, aggregate, track regressions.

Focus: regulatory compliance prompts (Category 3) are the highest-value differentiator — correct answers require MENA-specific knowledge that general LLMs lack.

## Prompt categories

### Category 1 — Drafting (10 prompts)

| # | Document type | Jurisdiction | Key expected signals |
|---|---|---|---|
| 1 | Residential tenancy agreement | Dubai | RERA-compliant; Ejari registration clause; DLD standard form reference |
| 2 | Commercial lease | Abu Dhabi | Tawtheeq registration; VAT clause (5% on commercial); ADGM/onshore distinction |
| 3 | Residential tenancy | UAE (Abu Dhabi) | Ejari equivalent in Abu Dhabi = Tawtheeq; notice periods |
| 4 | Residential lease | Lebanon | Lebanese Rent Law; notice periods; Lebanese pound/USD clause |
| 5 | Commercial lease | KSA | Ejar platform registration requirement; Saudi Rent Law |
| 6 | Sale and purchase agreement | Dubai | DLD transfer procedure; 4% transfer fee; Oqood for off-plan |
| 7 | Sale and purchase agreement | KSA | RETT (Real Estate Transaction Tax) clause; 5% rate |
| 8 | Sublease agreement | Dubai | Must check head lease allows subletting; Ejari re-registration |
| 9 | Property management agreement | UAE | RERA licensed property manager requirement |
| 10 | Off-plan SPA | Dubai | RERA escrow requirement; developer obligations; completion milestone milestones |

### Category 2 — Review (5 prompts)

| # | Scenario | Key signals |
|---|---|---|
| 11 | Review residential lease (tenant side) — Dubai | Missing Ejari clause; below-market rent below RERA index |
| 12 | Review commercial lease (landlord side) — Abu Dhabi | VAT clause missing; Tawtheeq clause missing |
| 13 | Review eviction notice — Dubai | Check 12-month notice for personal use; RERA Rental Dispute Center requirement |
| 14 | Review off-plan SPA | RERA escrow missing; developer not licensed |
| 15 | Review sale and purchase agreement — KSA | RETT clause; foreign buyer restrictions check |

### Category 3 — Compliance (5 prompts)

Regulatory requirements — highest differentiation value:

| # | Question | Key answer |
|---|---|---|
| 16 | "What is Ejari and when must I register?" | Dubai's online tenancy registration system; mandatory for all residential and commercial leases in Dubai; required before disputes can be filed at RDSC |
| 17 | "What is Tawtheeq?" | Abu Dhabi's lease registration platform (equivalent to Ejari); mandatory |
| 18 | "What is Ejar?" | Saudi Arabia's lease registration platform; mandatory for all residential and commercial leases under Saudi Rent Law |
| 19 | "Can a non-UAE national own freehold property in Dubai?" | Yes, in designated freehold areas under Law No. 7 of 2006; restrictions apply outside these zones |
| 20 | "What are the foreign ownership rules for KSA property?" | Non-GCC nationals face significant restrictions; GCC nationals have broader rights; industrial/investment zones have different rules |

### Category 4 — Disputes (5 prompts)

| # | Scenario | Key signals |
|---|---|---|
| 21 | Tenant refused to pay rent — Dubai | RDSC (Rental Dispute Settlement Centre) process; 45-day notice before filing |
| 22 | Landlord wants to evict for personal use — Dubai | 12-month written notice; Article 25(2) of Law No. 26 of 2007 |
| 23 | Security deposit dispute — Dubai | RDSC has jurisdiction; deposit deductions rules |
| 24 | Construction defects dispute — UAE | RERA arbitration for off-plan; ADGM/DIFC Courts for high-value |
| 25 | Lease renewal dispute — Lebanon | Lebanese Rent Law (Law No. 160 of 1992 + amendments) |

### Category 5 — Tax and structuring (3 prompts)

| # | Question | Key answer |
|---|---|---|
| 26 | "Is VAT payable on commercial rent in the UAE?" | Yes, 5% VAT applies to commercial real estate leases; residential is zero-rated under UAE VAT Law |
| 27 | "What is RETT and how is it calculated?" | Saudi Real Estate Transaction Tax (RETT): 5% on the sale value of real estate in KSA; introduced 2020; replaced VAT on real estate transactions |
| 28 | "How can I structure a UAE property acquisition to minimize tax?" | UAE has no income tax or capital gains tax on real estate; structure issues relate to DLD fees (4%), mortgage fees, and corporate ownership vs individual |

### Category 6 — Bilingual (2 prompts)

| # | Request |
|---|---|
| 29 | Arabic-language request: "أعدّ عقد إيجار سكني لدبي وفق متطلبات هيئة التنظيم العقاري." |
| 30 | "Draft a bilingual (AR/EN) commercial lease for Abu Dhabi." |

## Scoring targets

| Category | Legal soundness target | Jurisdiction awareness target |
|---|---|---|
| Drafting | ≥ 4.0 | ≥ 4.0 |
| Review | ≥ 3.5 | ≥ 3.5 |
| Compliance | ≥ 4.5 (high differentiation value) | ≥ 4.5 |
| Disputes | ≥ 3.5 | ≥ 4.0 |
| Tax | ≥ 4.0 | ≥ 4.0 |

## Caveats & currency

UAE real estate regulation is active. RERA, DLD, and ADGM publish new circulars regularly. KSA real estate law has been evolving under Vision 2030 (expanded foreign ownership zones, new mortgage regulations). Review this dataset when major regulatory changes are announced. Do not invent regulatory thresholds — use only the named frameworks above.

## Related skills

- [[eval-benchmark-runner]] — orchestrates this dataset
- [[eval-rubric-legal-soundness]] — primary scoring
- [[eval-rubric-jurisdiction-awareness]] — critical for regulatory compliance prompts
- [[eval-regression-detector]] — tracks quality across deployments
