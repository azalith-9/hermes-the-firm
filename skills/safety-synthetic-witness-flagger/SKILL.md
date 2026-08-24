---
name: safety-synthetic-witness-flagger
description: Use when a lawyer submits a deposition transcript, witness statement, sworn declaration, or affidavit for review, and there is any question about whether the testimony may be AI-generated, fabricated, or subject to coordinated coaching. Applies style heuristics, LLM-generation tells, cross-document consistency checks, and implausibility markers to flag specific anomalies — but never labels testimony as fake. Routes high-stakes cases to forensic linguists.
license: MIT
metadata: " id: safety.synthetic-witness-flagger category: safety jurisdictions: [US, UK, DIFC, ADGM, LB, KSA, UAE, GCC, EU] priority: P0 intent: [safety, evidence, synthetic-witness, forensic-linguistics, testimony-integrity] related: - safety-deepfake-evidence-detector - safety-ai-disclosure-required-tribunals - safety-bar-rule-1-1-competence-ai - review-evidence-integrity source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'safety'.
Registered as a flat plugin skill.
-->


# Synthetic Witness Flagger

## When to use this

Apply when:
- A lawyer uploads a witness statement, deposition transcript, sworn declaration, or affidavit and asks for a credibility or integrity assessment.
- Opposing counsel has produced witness testimony that appears unusually polished, inconsistent, or implausible.
- Multiple witness statements in a case share suspicious textual similarities.
- The client or supervising lawyer has concerns that testimony may have been generated or substantially drafted by AI.
- Discovery review surfaces testimony documents with unusual characteristics.

## Hard limit — what this skill does and does not do

**Does**: flag specific textual, structural, and factual anomalies that warrant professional investigation; suggest targeted deposition follow-up questions; recommend forensic-linguistics expert referral for high-stakes cases.

**Does not**: label any witness statement, deposition, or declaration as fake, fabricated, or AI-generated. Such a determination requires a qualified forensic linguist with validated methodology — AI-based assessment is a triage and flagging tool only.

Standard output concluding line:
> These flags are for your professional assessment only — they are not a determination of authenticity. Consider targeted deposition follow-up on the flagged items, and for high-stakes cases, instruct a forensic linguistics expert.

## Triage methodology

### Check 1 — Boilerplate and cross-witness phrase analysis

AI-generated or coaching-influenced testimony across multiple witnesses often shows:
- **Identical or near-identical phrasing** of the same factual event across independent witnesses.
- **Boilerplate-rotation**: the same stock phrases reworded slightly ("I observed" vs "I noticed" vs "I saw" for the same event) — suggesting a template with minor variation rather than independent recall.
- **Identical structure**: all witness statements following the same exact chronological and paragraph structure, which authentic independent accounts rarely do.

**Flag signal**: if two or more witnesses use the same sentence (or variants within a few words) to describe the same event, flag for explanation.

### Check 2 — LLM-generation textual tells

AI-generated text typically exhibits:
- **Smoothed, hedged prose**: no rough edges, hesitations, or idiosyncratic personal style; everything sounds clean and considered.
- **Absence of concrete sensory detail**: real witnesses typically provide specific, idiosyncratic sensory memories (the smell in the room, the exact color of a shirt, the background noise). LLM-generated accounts tend to describe events in generic, abstract terms.
- **Uniform register**: authentic testimony shifts register — more formal in direct examination, more colloquial in cross; AI-drafted statements maintain uniform register throughout.
- **No authentic faltering**: real deposition transcripts include "um", "well", corrections, and self-interruptions. A suspiciously clean transcript (every sentence grammatically perfect) warrants attention.
- **Hedged but complete recall**: AI-generated testimony often says "I believe" or "I think" (hedging) while still providing suspiciously complete and internally consistent accounts.

### Check 3 — Improbable recall

- **Verbatim conversation from years ago**: no human reliably recalls the exact words of a conversation from several years prior. A witness who provides verbatim dialogue from a 2019 meeting in a 2025 deposition warrants scrutiny.
- **Precise times and dates without documentation support**: authentic recall is usually approximate ("sometime in the morning", "mid-2020"); specific clock times and calendar dates without corroborating records suggest reconstruction.
- **Perfect chronological detail**: authentic memory has gaps and is non-linear; seamless chronological narratives without gaps or "I don't remember" moments are a flag.

### Check 4 — Inconsistency with case record

- Does the testimony contradict established documentary evidence (emails, invoices, travel records)?
- Are dates, locations, and participants consistent with known facts about the parties?
- Does the claimed sequence of events match what is physically or logistically plausible?

### Check 5 — Date and location inconsistencies

- GPS-anchored or timestamped records (email metadata, phone records, building access logs) can sometimes directly contradict location or timing claims.
- Flag any testimony element that can be cross-checked against objective records and appears inconsistent.

## Output format

```
## Witness Statement Integrity Assessment — Preliminary Flags

Document: [filename / description]
Assessed by: AI triage — NOT a forensic determination

### Flags:

Flag 1 — [Check category]: [Specific passage or characteristic]
Detail: [Why this is a flag; what authentic testimony typically looks like by contrast]
Suggested deposition follow-up: [Specific question to test the witness's genuine recall]

Flag 2 — [Check category]: [Specific passage or characteristic]
...

### Overall assessment:
[X] flags identified. These flags are for your professional assessment only — they are not a determination of authenticity or fabrication. Consider targeted deposition follow-up on flagged items. For high-stakes cases, instruct a forensic linguistics expert.
```

## Suggested deposition follow-up templates

For implausible recall:
> "You stated [verbatim quote]. How do you recall those exact words? What documentation are you relying on for that specific detail?"

For cross-witness phrase similarity:
> "I'd like to ask you about this phrase in your statement: [phrase]. Did anyone assist you in drafting this statement? Did you review any other statements or documents before preparing yours?"

For absent sensory detail:
> "You describe [event] — can you tell me more specifically what you personally observed? What did the room look, smell, or sound like at that moment?"

## Jurisdictional context — implications for proceedings

| Jurisdiction | Mechanism for challenging testimony integrity | Key standards |
|-------------|----------------------------------------------|--------------|
| US | Deposition + Daubert motion for forensic linguistic expert | FRCP 26 for expert disclosure; FRE 702 for admissibility of expert opinion |
| UK | CPR Part 35 joint or single expert; cross-examination | Forensic Science Regulator codes; CPR 32 for witness statements |
| DIFC / ADGM | Expert evidence application; cross-examination under DIFC ER | Common-law heritage; court-managed expert process |
| MENA (civil law) | Court-appointed expert (khabir) is primary mechanism | Party-instructed private expert has supporting role; court expert is decisive |
| France | Expert judiciaire appointed by court; contradictoire process | Code de procédure civile Art. 263+ |

## Escalation — forensic linguistics experts

For high-stakes cases (criminal trials, major commercial arbitration, regulatory proceedings), instruct a qualified forensic linguist:
- **What they do**: apply validated scientific methodology to analyze authorship, stylistic consistency, and evidence of AI generation using tools with known error rates (as required under Daubert / CPR 35).
- **Certification bodies**: International Association of Forensic Linguists (IAFL); national forensic science regulators.
- **Expert report**: must meet the applicable court's requirements for expert evidence (disclosed in advance, prepared for cross-examination, signed declaration of independence).

## Related skills

- [[safety-deepfake-evidence-detector]] — complementary skill for digital media evidence integrity
- [[safety-ai-disclosure-required-tribunals]] — disclosure obligations for AI-assisted court work
- [[safety-bar-rule-1-1-competence-ai]] — competence duties when using AI analysis in proceedings
- [[review-evidence-integrity]] — broader evidence integrity review workflow
