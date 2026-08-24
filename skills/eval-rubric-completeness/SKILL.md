---
name: eval-rubric-completeness
description: Use when scoring AI legal output on whether it addresses the question fully. A 0–5 rubric that checks for all material aspects, relevant edge cases, and structural completeness appropriate to the output type — IRAC for analysis, full document structure for drafts, all relevant axes for comparisons.
license: MIT
metadata: " id: eval.rubric.completeness category: eval priority: P0 intent: [__eval__, completeness, rubric, legal-output, quality] related: [eval-rubric-legal-soundness, eval-rubric-jurisdiction-awareness, eval-llm-as-judge-system-prompt, eval-benchmark-runner, eval-dataset-nda-prompts-30] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'eval'.
Registered as a flat plugin skill.
-->


# Eval Rubric — Completeness

## When to use this

Apply whenever an AI legal output needs to be assessed for whether it answered the question fully and in the appropriate structure. Completeness is distinct from legal soundness: a response can be legally accurate but incomplete (e.g., correctly stating one rule but missing three others that also apply).

Run in the [[eval-llm-as-judge-system-prompt]] ensemble as part of the standard rubric set.

## Scoring (0–5)

| Score | Label | Criteria |
|---|---|---|
| **5** | Excellent | All material aspects addressed; relevant edge cases and alternative views surfaced; structured appropriately for the answer type (IRAC for analysis, complete document for draft, structured table for comparison); next steps or recommendations offered where relevant |
| **4** | Good | Addresses the question fully with minor gaps (e.g., one secondary consideration not mentioned, or recommendations omitted) |
| **3** | Acceptable | Substantive coverage with 1–2 notable gaps — a major consideration missed, or a required clause omitted from a draft, or a key jurisdiction not covered in a comparison |
| **2** | Poor | Partial answer; misses an important dimension (e.g., analyzes termination rights but does not address notice periods; or drafts an NDA missing the governing law clause) |
| **1** | Largely incomplete | Addresses a fraction of the question; the user would need to ask multiple follow-ups to get a complete answer |
| **0** | Fail | Empty, off-topic, or so incomplete as to be useless |

## Sub-criteria by output type

### For drafts (contract, NDA, agreement, letter)

A draft is complete when it contains all structurally required clauses for its document type and jurisdiction. Check against the standard clause inventory:

**NDA (mutual)** — minimum complete set:
- Definition of Confidential Information (with carve-outs: public domain, prior knowledge, independent development, compelled disclosure)
- Obligations of confidentiality (standard of care)
- Permitted use / purpose limitation
- Duration of obligations (separate from agreement term)
- Return or destruction of materials
- No license / IP ownership
- Governing law and jurisdiction
- Entire agreement / severability

A draft missing any of these is ≤ 3/5 on completeness.

**Employment contract (UAE)** — minimum complete set:
- Parties identification
- Job title and description
- Remuneration (including allowances separately stated)
- Working hours
- Annual leave (≥ 30 calendar days per UAE Labour Law)
- Probation period (≤ 6 months)
- Termination and notice period
- EOSG entitlement clause
- Governing law (UAE)

**Lease agreement (UAE, RERA-compliant)** — minimum complete set:
- Parties; property description; term
- Rent amount and payment schedule
- Security deposit terms
- Ejari/Tawtheeq registration clause
- Maintenance obligations (landlord vs tenant)
- Termination and renewal
- Governing law; dispute resolution (RDSC)

### For legal analysis (advisory, review)

A complete analysis follows IRAC structure:
- **Issue**: states the legal question precisely
- **Rule**: identifies the applicable legal rule(s) with authority
- **Application**: applies the rule to the specific facts
- **Conclusion**: states a clear outcome or recommendation
- **Edge cases / caveats**: flags material uncertainties

An analysis that stops at "Rule" without application scores ≤ 2/5. An analysis that correctly applies the law but does not give a conclusion scores ≤ 3/5.

### For comparisons (multi-jurisdiction, side-by-side)

A complete comparison:
- Covers all jurisdictions requested
- Applies the same axes to each jurisdiction (consistent structure)
- Flags where data is uncertain or law is unclear
- Includes a practical summary ("for a UAE/KSA crossborder transaction, prefer X because…")

### For research responses

A complete research response:
- Identifies the primary source(s) (statute, case, regulation)
- States the relevant rule accurately
- Acknowledges limitations (post-cutoff changes, unpublished case law)
- Offers next steps (where to find updated information)

## Common failure modes

| Failure mode | Typical score |
|---|---|
| NDA draft missing governing law clause | ≤ 2 |
| Employment contract missing EOSG clause in MENA context | ≤ 2 |
| Analysis with no conclusion or recommendation | ≤ 3 |
| Comparison covering only 2 of 3 requested jurisdictions | ≤ 3 |
| Research response with no citation of primary authority | ≤ 3 |
| Excessive hedging ("consult a lawyer") with no substantive content | 1 |

## Relationship to other rubrics

- **Legal soundness** (correct law) + **Completeness** (full coverage) = full answer quality.
- A response can score 5/5 on legal soundness but 2/5 on completeness if it correctly discusses only one applicable rule while missing two others.
- Completeness is scored independently — do not adjust for legal soundness issues.

## Related skills

- [[eval-rubric-legal-soundness]] — legal accuracy of what is present (vs completeness of what is included)
- [[eval-rubric-jurisdiction-awareness]] — jurisdiction coverage is a component of completeness for cross-border tasks
- [[eval-llm-as-judge-system-prompt]] — applies this rubric in the automated scoring pipeline
- [[eval-benchmark-runner]] — orchestrates scoring
- [[eval-dataset-nda-prompts-30]] — primary dataset where completeness is frequently tested
