---
name: eval-rubric-citation-quality
description: Use when scoring AI legal output on citation quality — whether sources are real, accurately quoted, properly pin-cited, and correctly formatted. A 0–5 rubric where any fabricated citation scores 0 regardless of other quality. The primary early-warning system for the most dangerous failure mode in legal AI.
license: MIT
metadata: " id: eval.rubric.citation-quality category: eval priority: P0 intent: [__eval__, citation, hallucination, rubric, legal-accuracy] related: [eval-rubric-legal-soundness, eval-rubric-hallucination-detection, eval-llm-as-judge-system-prompt, eval-benchmark-runner, eval-regression-detector] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'eval'.
Registered as a flat plugin skill.
-->


# Eval Rubric — Citation Quality (0–5)

## When to use this

Apply this rubric whenever an AI legal output includes references to statutes, regulations, cases, or other legal instruments. It is the most important rubric for preventing harm: a practitioner who acts on a fabricated statute faces professional liability; a client who relies on an invented court ruling may lose their case.

Run in the [[eval-llm-as-judge-system-prompt]] ensemble on every research, advisory, and review output. Apply independently of [[eval-rubric-hallucination-detection]] — citation quality measures the *quality* of real citations, while hallucination detection is the binary gate.

## Scoring (0–5)

| Score | Label | Criteria |
|---|---|---|
| **5** | Excellent | All citations are real and verified; accurately quoted or paraphrased; pin-cited where appropriate (article number, paragraph, section); formatted per applicable citation style (Bluebook for US, OSCOLA for English, style appropriate to jurisdiction); every legal proposition has a supporting authority or is clearly marked as general background |
| **4** | Good | All citations real; minor formatting issues (e.g., missing year or publisher in case citation); or missing pin-cites in 1–2 instances; no misleading attribution |
| **3** | Acceptable | All citations real and substantively correct; inconsistent style across citation types; missing pin-cites in several instances; not misleading but would require cleanup before professional use |
| **2** | Poor | Most citations real but at least one is questionable (source may exist but quoted proposition is materially different from what it says) or clearly wrong (wrong jurisdiction statute cited) |
| **1** | Very poor | Mix of real and fabricated citations; or a single clearly fabricated source |
| **0** | Fail | Significant fabrication — invented case names, invented statute numbers, invented article numbers, invented pin-cites; or a single egregious fabrication on a material point |

**Hard rule**: any citation that does not exist in reality scores **0**, period. This overrides all other sub-criteria.

## Sub-criteria (applied at score levels 3–5)

### Existence
Does the cited source actually exist? Verification methods:
- For legislation: official government gazette, legislation.gov.uk, EUR-Lex, DIFC Laws, ADGM Laws portal, Saudi Official Gazette (Umm Al-Qura).
- For cases: official court registers, DIFC Courts Law Library, ADGM Courts Library, LexisNexis, Westlaw.
- For regulatory guidance: regulator websites (SAMA, CBUAE, FSRA, DFSA, SDAIA).

If a source cannot be verified through an authoritative channel, treat as uncertain; if the content is also unverifiable, treat as fabricated.

### Accuracy
Is the quoted or paraphrased proposition what the source actually says?
- Check: is the article/section cited the right one for the proposition stated?
- Check: is the case cited for the right legal principle (not a different holding)?
- Common failure mode: citing a real statute but for a proposition it does not contain.

### Pin-cite precision
For legal precision, citations should identify:
- **Legislation**: article number, clause number where relevant (not just "the Commercial Companies Law").
- **Cases**: paragraph number or page number; year; court identifier.
- **Regulatory guidance**: circular number or date of issuance; section reference.

Absence of pin-cites is a score deduction (3 or below) but not an automatic 0 unless the proposition is ambiguous without the pin-cite.

### Format consistency
The citation style should be consistent throughout the response:
- MENA jurisdictions: no single mandatory citation style exists; the model should adopt one style and use it consistently.
- DIFC/ADGM: OSCOLA-adjacent style is appropriate.
- UK matters: OSCOLA.
- US matters: Bluebook.
- French law: French academic citation style (loi n° XXXX-XXX du JJ mois AAAA).

### Completeness of citation coverage
Every legal proposition in the response should have either:
1. A supporting citation, or
2. An explicit statement that it is general background knowledge not requiring a specific source.

Unsupported specific factual claims about the law (e.g., "The limitation period is 7 years in Lebanon" stated without citation) are a deduction.

## Critical context

Fabricated citations are the **single most dangerous failure mode for legal AI.** The consequences of a practitioner or client relying on:
- An invented statute: can lead to criminal liability, professional sanctions, or catastrophic legal errors.
- An invented case: can lead to arguments rejected by courts and professional misconduct proceedings.
- A misattributed proposition: can lead to contractual arrangements that the cited authority does not actually support.

This rubric is the early-warning system. A model that scores consistently below 4.0 on citation quality should not be used for legal research tasks without a mandatory human verification step.

## Related skills

- [[eval-rubric-legal-soundness]] — legal accuracy beyond just citations
- [[eval-rubric-hallucination-detection]] — binary gate for fabrication (run before this rubric)
- [[eval-llm-as-judge-system-prompt]] — the judge prompt that applies this rubric
- [[eval-benchmark-runner]] — orchestrates scoring across all prompts
- [[eval-regression-detector]] — alerts when citation quality drops across deployments
