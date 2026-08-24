---
name: report-competitor-output-comparison-weekly
description: Use when the product team needs a structured weekly comparison of AI-generated legal outputs across competing platforms (Louis, Harvey, CoCounsel, Spellbook, Genie) on the same prompt set, with scoring on output quality, citation accuracy, and MENA-jurisdiction fit. This is an internal quality-intelligence report, not a user-facing skill. Trigger on the weekly reporting schedule or when competitive positioning analysis is requested.
license: MIT
metadata: " id: report.competitor-output-comparison-weekly category: report jurisdictions: [__multi__] priority: P3 intent: [__internal__, competitive-analysis, benchmarking, quality-comparison] related: [report-weekly-ai-quality-trend, report-hallucination-rate-tracker, report-jurisdiction-coverage-matrix, eval-output-quality] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'report'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Competitor Output Comparison — Weekly Report

Internal weekly intelligence report comparing AI-generated legal outputs across competing platforms. Used to track competitive differentiation, identify quality gaps, and surface areas where Louis leads or lags on MENA-specific legal work.

## Purpose

This report answers three questions every week:

1. **Quality**: On the same benchmark prompt set, whose output is more accurate, better structured, and more useful to a practicing lawyer?
2. **Citations**: Who hallucinates less? Who cites authoritative primary sources correctly?
3. **MENA fit**: Which platform understands MENA jurisdictions (LB, KSA, UAE onshore, DIFC, ADGM, EG) at a practitioner level?

## Inputs

### Prompt set
A fixed, versioned set of 20–30 prompts covering:
- Statute lookup (UAE, KSA, Lebanon)
- Contract redline (employment, NDA, SPA)
- Jurisdiction comparison (e.g., non-compete enforceability across UAE / KSA / DIFC)
- Sanctions screening scenario
- AML/KYC question with Arabic-entity names
- Regulatory licensing question (fintech, healthcare)
- Case-law search for a DIFC or onshore UAE matter

Prompt set is frozen for 4-week rolling windows, then updated to prevent platforms from "learning" the benchmark.

### Platforms to test

| Platform | Notes |
|----------|-------|
| **Louis** (this product) | Current production version; note skill version |
| **Harvey** | US-native, common-law-centric; weak on Arabic-script entities |
| **CoCounsel** (Casetext/Thomson Reuters) | Strong on US case law; limited MENA |
| **Spellbook** | Contract-focused; no MENA-specific KB |
| **Genie AI** | Template-oriented; check MENA expansion progress |

Add or remove platforms each quarter as the landscape shifts. Document platform version / model version used in every run.

## Methodology

### Step 1 — Run prompts
Submit each prompt verbatim to each platform. Record:
- Exact response (copy full output, do not paraphrase)
- Latency (seconds to full response)
- Any refusals or hedging behavior

### Step 2 — Score each output

Score on four dimensions, each 1–5:

| Dimension | 1 (Poor) | 5 (Excellent) | Weight |
|-----------|----------|---------------|--------|
| **Legal accuracy** | Wrong law, wrong jurisdiction, fabricated rule | Correct, well-supported by primary sources | 40% |
| **Citation quality** | No citations or hallucinated citations | Verified primary sources, correct article/decree numbers | 30% |
| **MENA fit** | Treats question as US/UK matter; ignores MENA specifics | Correctly applies MENA-specific rules, naming correct regulators, local thresholds | 20% |
| **Output structure** | Unstructured prose; no actionable hierarchy | Clearly organized, executive summary, flagged risks, actionable | 10% |

### Step 3 — Hallucination check
For every citation or statute number produced by any platform:
- Check against authoritative source (official gazette, DIFC Laws portal, BDE BOE, etc.)
- Tag each as: **verified** / **plausible but unverified** / **confirmed hallucination**
- Calculate hallucination rate per platform per prompt category

### Step 4 — MENA-specific sub-assessment
For prompts touching MENA law:
- Did the platform name the correct regulator (DFSA vs SCA vs SAMA vs BDL)?
- Did it apply Arabic/Islamic law concepts correctly (EOSB, Sharia compliance, Kafala)?
- Did it handle Arabic entity names and transliteration robustly?
- Did it distinguish onshore UAE from DIFC/ADGM free-zone regimes?

## Output Format

### Executive summary (top of report)
```
Week: [ISO week number + dates]
Prompts run: [N]
Platforms tested: [list]
Model versions: [list]

Headline finding: [1-2 sentences — who led, who lagged, any notable shift vs last week]

MENA-fit leader: [platform]
Citation accuracy leader: [platform]
Hallucination rate (lowest): [platform] at [X]%
```

### Per-prompt comparison table

| Prompt | Louis | Harvey | CoCounsel | Spellbook | Genie | Notes |
|--------|-------|--------|-----------|-----------|-------|-------|
| UAE non-compete review | 4.2 | 2.8 | 2.1 | 3.0 | 1.9 | Harvey missed FDL 33/2021 entirely |
| … | … | … | … | … | … | … |

### Hallucination rate table

| Platform | Prompts with hallucinated citations | Rate |
|----------|-------------------------------------|------|
| Louis | X / N | X% |
| Harvey | X / N | X% |
| … | … | … |

### Narrative findings
3–5 bullet points per platform, covering:
- What they do well
- Where Louis has a material lead
- Where Louis should improve
- Any new feature or capability spotted

### Action items
Concrete follow-up items for the Louis team, tagged by owner:
- **Content**: KB gaps surfaced by competitive comparison
- **Skill quality**: Prompts where Louis underperformed; route to skill owner
- **Model**: Cases where a different model config would help

## Quality bar
- Every citation claim in a competitor output must be independently verified before scoring as "hallucination confirmed."
- Scoring must be done blind where possible — two scorers before seeing each other's scores.
- LLM-judge can assist on structure/clarity scoring; human expert must validate legal-accuracy scores on MENA-specific prompts.

## Cadence
- Run: Monday morning
- Published: Wednesday EOD to product + legal leads
- Archived: in the internal quality-reports folder, linked from weekly digest

## Related skills

- [[report-weekly-ai-quality-trend]]
- [[report-hallucination-rate-tracker]]
- [[report-jurisdiction-coverage-matrix]]
- [[eval-output-quality]]
- [[report-skill-adoption-by-tier]]
