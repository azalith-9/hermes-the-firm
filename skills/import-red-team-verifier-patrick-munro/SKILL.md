---
name: import-red-team-verifier-patrick-munro
description: Use when migrating the Patrick Munro red-team verification methodology into the mini-hermes-the-firm format. This adapter maps adversarial stress-testing logic for legal documents and AI-generated legal output — deliberate challenge of assumptions, identification of counter-arguments, and verification of factual and legal accuracy — into the standard skill model. Triggers when importing any red-team or adversarial-review skill attributed to the Munro approach.
license: MIT
metadata: " id: import.red-team-verifier-patrick-munro category: import jurisdictions: [DIFC, ADGM, UK, UAE, __multi__] priority: P3 intent: [__import__, red-team, verification, adversarial-review, migration] related: [import-legal-simulation-patrick-munro, import-vendor-due-diligence-patrick-munro, import-tech-contract-negotiation-patrick-munro, import-legal-risk-assessment-anthropic] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'import'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Import: Red Team Verifier (Patrick Munro)

## What it does

This import adapter migrates a **red-team verification skill modelled on the Patrick Munro methodology** into the `mini-hermes-the-firm` standard format. Red-teaming in the legal context means deliberately challenging the document, analysis, or argument under review — as a sophisticated adversary would — to surface weaknesses before they are exploited by a counterparty, court, or regulator.

The Munro red-team approach applies to three contexts:

1. **Document red-teaming**: stress-testing a contract, legal opinion, or regulatory submission against the strongest objections
2. **AI output verification**: challenging the agent-generated legal analysis to detect hallucinations, unsupported conclusions, and jurisdiction errors
3. **Argument red-teaming**: testing the legal arguments in a brief or submission against the opposition's best counter-arguments

## Import config

| Field | Source mapping | Default if absent |
|---|---|---|
| `red_team_mode` | Legacy `mode` | `full` (document + argument + ai_output) |
| `challenge_depth` | Legacy `depth` | `3` (three levels of challenge) |
| `adversary_persona` | Legacy `adversary` | `senior_opposing_counsel` |
| `hallucination_check` | Legacy `check_hallucinations` boolean | `true` |
| `jurisdiction_check` | Legacy `check_jurisdiction` boolean | `true` |
| `citation_check` | Legacy `check_citations` boolean | `true` |
| `output_format` | Legacy `format` | `red_team_report` |
| `governing_law` | Legacy `governing_law` | `DIFC` |

## Dry-run preview

```
IMPORT PREVIEW — red-team-verifier-patrick-munro
Source shape      : Adversarial verification skill (Munro methodology)
Mode              : full (document + argument + AI output)
Challenge depth   : 3 levels
Adversary persona : senior_opposing_counsel
Hallucination check: enabled
Jurisdiction check : enabled
Citation check     : enabled
Output             : red_team_report
Governing law      : DIFC
```

## Red-team methodology (post-import)

### Level 1 — Surface challenges
- What is the weakest factual assertion in the document?
- What is the most ambiguous term or provision?
- What is the most one-sided clause?

### Level 2 — Legal challenges
- What statutory or regulatory provision most directly undermines the position?
- What is the strongest precedent (or closest analogy) the opponent would cite?
- Where does the document fail to comply with a mandatory legal requirement?

### Level 3 — Strategic challenges
- What procedural or jurisdictional argument could be used to challenge enforcement?
- What counterparty behaviour could make this document unenforceable?
- What change in circumstances (economic, regulatory, political) would destroy the basis for this position?

### AI output verification track

When verifying AI-generated legal analysis:

1. **Citation check**: verify every statute, article number, and case citation against known reliable sources. Flag any citation that cannot be verified — it may be a hallucination.
2. **Jurisdiction check**: verify that every legal proposition is attributed to the correct jurisdiction and legal system (common law vs civil law; onshore vs DIFC/ADGM).
3. **Date check**: verify that cited legislation is in force as of the relevant date; check for recent amendments.
4. **Internal consistency check**: verify that conclusions follow from premises; flag logical gaps.
5. **Completeness check**: are there mandatory requirements or standard clauses missing that a practitioner would expect?

## Red-team report output

```
RED TEAM REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Document reviewed  : [title]
Review date        : [date]
Adversary persona  : senior_opposing_counsel
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHALLENGE #1 [LEVEL 1 / SURFACE]
Challenge          : [the challenge]
Weakness exploited : [specific provision or assertion]
Severity           : HIGH / MEDIUM / LOW
Recommended fix    : [specific revision]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[repeat for each challenge]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AI OUTPUT VERIFICATION
Hallucinations detected : [count] — [list]
Jurisdiction errors     : [count] — [list]
Citation warnings       : [count] — [list]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Overall verdict : PASS / NEEDS REVISION / FAIL
```

## MENA-specific red-team flags

- **Arabic language prevailing clause**: if a bilingual contract's Arabic version differs from the English version, the Arabic governs in UAE/KSA — challenge any analysis based solely on the English text.
- **Shariah-compliance assumption**: challenge any financial provision not reviewed for Shariah compliance in KSA or conservative UAE contexts.
- **Notarisation requirement**: challenge enforceability of contracts in Lebanon or UAE civil jurisdictions where the transaction type requires notarial form.
- **DIFC/ADGM jurisdiction validity**: challenge whether the parties actually have a legitimate connection to justify DIFC/ADGM governing law.

## Failure modes

| Error | Likely cause | Resolution |
|---|---|---|
| `only_surface_challenges` | Legacy limited to Level 1 | Override `challenge_depth: 3` |
| `hallucination_check_disabled` | Legacy AI-output track disabled | Enable for all AI-generated content |
| `adversary_too_gentle` | Persona set to "neutral reviewer" | Override to `senior_opposing_counsel` |
| `jurisdiction_not_checked` | Citation check only | Enable separate `jurisdiction_check: true` |

## Related skills

- [[import-legal-simulation-patrick-munro]]
- [[import-vendor-due-diligence-patrick-munro]]
- [[import-tech-contract-negotiation-patrick-munro]]
- [[import-legal-risk-assessment-anthropic]]
- [[review-contract-generic]]
