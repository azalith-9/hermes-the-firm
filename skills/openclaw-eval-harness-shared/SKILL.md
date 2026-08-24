---
name: openclaw-eval-harness-shared
description: Use when evaluating the quality, accuracy, or safety of a legal AI skill against a standardized benchmark. The shared eval harness provides community-maintained datasets (NDA, employment, real estate, research), rubrics for legal soundness and hallucination detection, multi-judge scoring to reduce bias, and a public leaderboard for comparing skill quality across providers and versions.
license: MIT
metadata: " id: openclaw.eval-harness-shared category: openclaw priority: P2 intent: [openclaw, eval, benchmark, legal-ai-quality, rubric, hallucination] related: [openclaw-public-skill-registry, openclaw-contrib-template, openclaw-skill-portability-claude-codex-gemini] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'openclaw'.
Namespaced as louis-<category>-<skill> on registration.
-->


# OpenClaw — Shared Eval Harness

## Purpose

Legal AI skills need to be evaluated against a consistent, reproducible quality bar before they are trusted in professional practice. The OpenClaw Shared Eval Harness is a community-maintained open-source framework that lets skill authors, AI vendors, and legal professionals benchmark legal AI quality across four dimensions: legal soundness, citation quality, hallucination rate, and jurisdictional accuracy.

The harness is intentionally open: anyone can contribute datasets, rubrics, or judge prompts. Vendors may run their models against the harness to produce publicly comparable scores.

## Components

### 1. Datasets

Community-contributed prompt/answer pairs organized by practice area:

| Dataset | Description | Coverage |
|---------|-------------|----------|
| NDA dataset | Drafting, review, red-flag analysis | UAE (onshore + DIFC), LB, UK, US |
| Employment dataset | Contracts, non-competes, termination analysis | UAE, KSA, LB, UK, US |
| Real estate dataset | Lease review, SPA analysis, title issues | UAE, LB, EG, UK |
| Research dataset | Regulatory questions, statute lookup, comparative law | Multi-jurisdiction |
| Corporate dataset | SHA, MOU, acquisition terms | DIFC, ADGM, GCC |

Each entry in a dataset contains:
- `prompt`: the user input (in the most realistic form possible)
- `reference_answer`: the expected correct response, authored or reviewed by an admitted lawyer
- `jurisdiction`: the applicable legal system
- `practice_area`: the skill category being tested
- `difficulty`: easy / medium / hard / trap (where the correct answer is counterintuitive)

### 2. Rubrics

Evaluation rubrics define what a correct response looks like across dimensions:

**Legal soundness** (0–5 scale)
- 5: Fully accurate, complete, and actionable; no material omission
- 4: Accurate with minor gaps that would not mislead a practitioner
- 3: Mostly accurate but missing at least one material point
- 2: Partially accurate; some claims are wrong or misleading
- 1: Mostly wrong; could lead a practitioner to a harmful conclusion
- 0: Completely wrong or hallucinates legal authority

**Citation quality** (0–3 scale)
- 3: All citations accurate and correctly formatted for the jurisdiction
- 2: Citations present but minor formatting or pin-cite errors
- 1: Citations present but at least one is fabricated or wrong
- 0: No citations where they were required, or all citations fabricated

**Hallucination rate** (binary per claim)
- A claim is a hallucination if it asserts a specific legal fact (statute number, article, case name, threshold) that is factually wrong or non-existent.
- Report hallucination rate as: (number of hallucinated claims) / (total verifiable claims).

**Jurisdictional accuracy** (0–2 scale)
- 2: Response correctly identifies and applies the applicable jurisdiction
- 1: Response applies the wrong jurisdiction but still gives technically correct advice for that jurisdiction
- 0: Response conflates jurisdictions or applies a clearly wrong legal system

### 3. Judge models

Single-judge evaluation introduces model-specific bias. The harness uses a panel of at least three judge models (e.g., the agent, GPT-4, Gemini) to score each response independently. The final score is the median across judges after excluding outliers.

Judge prompts are templated and version-controlled in the repository. They include:
- The rubric being applied
- The reference answer (for grounded evaluation)
- Instructions to score independently without knowing which vendor produced the candidate answer

### 4. Leaderboard

Aggregate scores per vendor/model/skill version are published to the OpenClaw public leaderboard. The leaderboard shows:
- Overall score per dataset
- Per-rubric breakdown
- Version history (so regressions are visible)
- Whether the run was community-verified or vendor-self-reported

Leaderboard entries that are vendor-self-reported are labelled as such; community-verified runs (where an independent reviewer replicated the evaluation) receive a verified badge.

## Running the harness

```bash
# Install
git clone https://github.com/sboghossian/mini-hermes-the-firm
cd mini-hermes-the-firm/eval

# Run against a specific skill + dataset
python run_eval.py \
  --skill draft-nda-unilateral \
  --dataset nda \
  --model claude-sonnet-4-5 \
  --judges claude,gpt-4o,gemini-1.5-pro \
  --output results/my-run.json
```

Results are written to a JSON file with per-prompt scores and the aggregated summary. To submit to the leaderboard, open a PR against `eval/results/` with your run file.

## Contributing datasets and rubrics

Contributors should:
1. Author reference answers in consultation with an admitted lawyer in the relevant jurisdiction.
2. Label each entry with accurate jurisdiction and difficulty tags.
3. Flag "trap" entries — cases where the obvious (but wrong) answer is a common AI failure mode.
4. Submit via a PR with a brief description of the gap being filled.

Do not submit synthetic reference answers generated purely by AI without practitioner review — the harness is only as good as its ground truth.

## Caveats

- Eval scores measure skill output quality at a point in time against a fixed dataset. They are not a guarantee of performance in production.
- Legal standards change. Datasets should be reviewed for currency at least annually. Outdated reference answers are labelled with a staleness warning.
- The harness tests the AI output, not the underlying law. Verify any regulatory claims against primary sources before acting on them in practice.

## Related skills

- [[openclaw-public-skill-registry]] — the registry of skills being evaluated
- [[openclaw-contrib-template]] — how to contribute skills and datasets
- [[openclaw-skill-portability-claude-codex-gemini]] — test portability across providers
