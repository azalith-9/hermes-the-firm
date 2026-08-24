---
name: eval-rubric-jurisdiction-awareness
description: Use when scoring AI legal output on whether it correctly identifies, states, and applies the right jurisdiction's law. A 0–5 rubric that checks explicit jurisdiction declaration, correct rule application, conflict-of-laws handling, and DIFC/ADGM free-zone distinctions. Catastrophic mismatch (US law on a Saudi matter) scores 0.
license: MIT
metadata: " id: eval.rubric.jurisdiction-awareness category: eval priority: P0 intent: [__eval__, jurisdiction, mena, rubric, conflict-of-laws] related: [eval-rubric-legal-soundness, eval-rubric-completeness, eval-llm-as-judge-system-prompt, eval-benchmark-runner, eval-dataset-nda-prompts-30, eval-dataset-employment-prompts-30] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'eval'.
Registered as a flat plugin skill.
-->


# Eval Rubric — Jurisdiction Awareness

## When to use this

Apply to any output that involves substantive law — particularly when the user has specified or implied a jurisdiction. This rubric is especially important for MENA-focused legal AI because the gap between civil law (UAE onshore, KSA, Lebanon, France) and common law (DIFC, ADGM, UK) is vast, and between free-zone and onshore regimes within the UAE is significant.

A jurisdiction mismatch is not just a quality issue — it can cause concrete harm (e.g., advising that a penalty clause is enforceable when it is not in the stated jurisdiction).

## Scoring (0–5)

| Score | Label | Criteria |
|---|---|---|
| **5** | Excellent | Jurisdiction stated explicitly in the opening sentence or paragraph; correct jurisdiction-specific rules applied throughout; multi-jurisdictional issues flagged and addressed; free-zone vs onshore distinctions made where relevant; conflict-of-laws considerations surfaced for cross-border transactions |
| **4** | Good | Jurisdiction stated; correct rules applied with minor nuance missed (e.g., one secondary distinction not addressed) |
| **3** | Acceptable | Jurisdiction implied (not explicitly stated) but correct rules applied approximately; or stated but one secondary jurisdiction-specific rule missed |
| **2** | Poor | Wrong or vague jurisdiction stated (e.g., "under UAE law" when the matter is DIFC); or correct jurisdiction stated but wrong rules applied for that jurisdiction in 1–2 significant instances |
| **1** | Very poor | Jurisdictions confused or mixed without acknowledgment; rules from a different jurisdiction applied without flagging |
| **0** | Catastrophic mismatch | Applies entirely the wrong legal system (e.g., US law applied to a Saudi onshore matter; UK employment law applied to a UAE onshore employment contract without flagging the inapplicability) |

## Sub-criteria

### Did it ask for jurisdiction when missing?

For prompts that do not specify a jurisdiction, the model should ask before drafting or advising. Proceeding without jurisdiction is a risk even if the model guesses correctly. A failure to ask when jurisdiction is unspecified should reduce the score:
- If jurisdiction was inferrable from context and the model correctly identified it: no deduction.
- If jurisdiction was not inferrable and the model proceeded without asking: deduct 1 point.

### Did it apply jurisdiction-specific rules (not just general principles)?

General principles ("an NDA should define confidential information") are not jurisdiction-specific. Jurisdiction-specific rules are:
- UAE: UAE Civil Transactions Law limitation periods; UAE Labour Law EOSG formula; RERA Ejari requirements.
- KSA: Shariah compliance considerations; Saudi Labour Law specific articles; SAMA regulations.
- Lebanon: Code of Obligations and Contracts; Lebanese Labor Code; NSSF requirements.
- DIFC: DIFC Contract Law; DIFC Employment Law; DIFC Arbitration Law.
- ADGM: ADGM Companies Regulations; ADGM Arbitration Regulations.
- UK: Limitation Act 1980; TULRCA; Employment Rights Act 1996.
- France: Code civil; Code du travail; RGPD.

An output that cites only general principles without jurisdiction-specific rules scores ≤ 3.

### Did it flag conflict-of-laws issues for multi-party / cross-border transactions?

For transactions involving parties from different jurisdictions:
- Which law governs? (governing law clause)
- Which courts have jurisdiction? (dispute resolution clause)
- Are there mandatory law provisions that override the choice? (e.g., UAE Labour Law protections cannot be contractually waived for UAE-sited employees)
- For MENA: is there a language requirement? (KSA courts require Arabic; Lebanon accepts French and Arabic)

Failure to flag these in a cross-border transaction reduces the score.

### Did it surface free-zone vs onshore distinctions?

This is the most common MENA-specific failure mode for generic LLMs:

| Scenario | Required distinction |
|---|---|
| UAE employment contract | DIFC Employment Law ≠ UAE Labour Law (Federal Decree-Law No. 33 of 2021) |
| UAE company formation | Onshore LLC vs free-zone company vs DIFC entity — different governance rules |
| UAE dispute resolution | Onshore courts vs DIFC Courts vs ADGM Courts — different procedure, enforceability |
| Abu Dhabi real estate | Tawtheeq (Abu Dhabi) ≠ Ejari (Dubai) |
| UAE commercial transactions | Federal commercial law vs free-zone regulations |

Failure to distinguish onshore from DIFC/ADGM when the distinction materially affects the answer scores ≤ 2.

## Special cases

**GCC jurisdiction without specification**: If a user says "Gulf" or "GCC" without specifying a country, the model should note that GCC countries have different national laws (despite the GCC commercial framework) and ask for clarification. Proceeding as if "GCC = UAE" is a jurisdiction error.

**"MENA" jurisdiction**: "MENA" is a region, not a jurisdiction. If a user asks for "MENA jurisdiction" guidance, the model should ask which specific country/free-zone and explain why it matters.

**International arbitration**: If governing law is the law of one jurisdiction but dispute resolution is ICC/LCIA/DIAC arbitration, both the governing law *and* the arbitration seat's lex arbitri apply. The model should address both.

## Related skills

- [[eval-rubric-legal-soundness]] — whether the law stated is correct within the right jurisdiction
- [[eval-rubric-completeness]] — whether all jurisdictions were covered in a comparison task
- [[eval-llm-as-judge-system-prompt]] — applies this rubric in the evaluation pipeline
- [[eval-benchmark-runner]] — orchestrates scoring
- [[eval-dataset-nda-prompts-30]] — NDA prompts where jurisdiction confusion is common
- [[eval-dataset-employment-prompts-30]] — employment prompts with onshore/DIFC distinction
