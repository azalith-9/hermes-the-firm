---
name: import-legal-simulation-patrick-munro
description: Use when migrating the Patrick Munro legal simulation methodology into the mini-hermes-the-firm format. This import adapter preserves adversarial scenario modelling — moot-court style argument construction, counterparty position mapping, and litigation outcome simulation — mapping it into the standard skill model. Suitable for dispute-risk assessment, negotiation preparation, and legal education contexts across common-law and civil-law jurisdictions.
license: MIT
metadata: " id: import.legal-simulation-patrick-munro category: import jurisdictions: [DIFC, ADGM, UK, UAE, LB, __multi__] priority: P3 intent: [__import__, legal-simulation, dispute-modelling, negotiation, migration] related: [import-mediation-dispute-analysis-jinzhe-tan, import-red-team-verifier-patrick-munro, import-vendor-due-diligence-patrick-munro, casesim-dispute-moot] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'import'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Import: Legal Simulation (Patrick Munro)

## What it does

This import adapter migrates a **legal simulation skill modelled on the Patrick Munro adversarial methodology** into the `mini-hermes-the-firm` standard format. The Munro simulation approach treats legal analysis as a structured adversarial exercise: the agent plays both sides — claimant and respondent — constructing the strongest plausible argument for each position, then renders a simulated outcome with reasoning.

This is distinct from a standard risk-assessment. The simulation is designed to surface arguments that a skilled opponent would make, preparing the legal team for what they will actually face in negotiation, arbitration, or litigation — rather than what a neutral analysis would highlight.

## Import config

| Field | Source mapping | Default if absent |
|---|---|---|
| `simulation_mode` | Legacy `mode` field | `bilateral` (both sides) |
| `forum` | Legacy `forum` or `venue` | `arbitration` |
| `governing_law` | Legacy `governing_law` | `DIFC` (Munro's primary jurisdiction) |
| `argument_depth` | Legacy `depth` | `full` (all sub-arguments) |
| `outcome_confidence` | Legacy `confidence_score` boolean | `true` |
| `output_format` | Legacy `format` | `moot_brief` |
| `persona` | Legacy `role` | `senior_barrister` |

## Dry-run preview

```
IMPORT PREVIEW — legal-simulation-patrick-munro
Source shape    : Adversarial legal simulation (Munro methodology)
Mode            : bilateral (claimant + respondent positions)
Forum           : arbitration (DIFC default)
Governing law   : DIFC
Depth           : full
Output          : moot_brief (structured argument + simulated outcome)
Persona         : senior_barrister
```

## Simulation structure (post-import)

### Step 1 — Claimant's best case
- Identify the strongest legal grounds for the claimant
- State the cause of action, legal basis, factual support
- Anticipate and rebut the respondent's likely defence
- Quantify relief sought

### Step 2 — Respondent's best case
- Identify the strongest defences and counterclaims
- Challenge the claimant's legal grounds
- Present alternative factual narrative where applicable
- Identify procedural bars (limitation, jurisdiction, standing)

### Step 3 — Simulated outcome
- Weigh claimant vs respondent arguments
- Apply governing-law doctrine and precedent framework
- Render simulated outcome: **Likely to succeed / Uncertain / Likely to fail**
- Confidence level: HIGH / MEDIUM / LOW
- Key swing factors that could change the outcome

### Step 4 — Strategic implications
- Settlement value range (if financial dispute)
- Negotiation leverage points for each side
- Recommended next steps

## Jurisdictional notes

| Jurisdiction | Simulation considerations |
|---|---|
| DIFC | Common law; DIFC Courts; precedent-based; English Court of Appeal decisions persuasive |
| ADGM | Common law; ADGM Courts; highly similar to DIFC approach |
| UAE onshore | Civil law; Federal Civil Procedure Code; no formal precedent doctrine |
| Lebanon | Civil law + commercial courts; French procedural influences; arbitration via Beirut Chamber |
| UK | Litigation vs arbitration path distinct; costs-shifting (loser pays) changes settlement calculus |
| KSA | Shariah-based; Board of Grievances jurisdiction; arbitration under Saudi Arbitration Law 34/2012 |

## Use cases

- **Pre-litigation risk assessment**: simulate the opponent's arguments before filing or responding to a claim
- **Negotiation preparation**: identify the counterparty's leverage points before entering settlement talks
- **Deal red-teaming**: stress-test contractual positions from the other side's perspective
- **Legal education / moot preparation**: practise argument construction with AI-powered opposition

## Failure modes

| Error | Likely cause | Resolution |
|---|---|---|
| `single_sided_output` | Source only modelled one party | Override `simulation_mode: bilateral` |
| `governing_law_mismatch` | DIFC config used in civil-law context | Override `governing_law` and note doctrinal differences |
| `outcome_overconfident` | Legacy assigned HIGH confidence broadly | Calibrate: most disputes are `MEDIUM` confidence; flag swing factors |
| `facts_insufficient` | Sparse fact pattern | Request additional context before running simulation |

## Related skills

- [[import-mediation-dispute-analysis-jinzhe-tan]]
- [[import-red-team-verifier-patrick-munro]]
- [[import-vendor-due-diligence-patrick-munro]]
- [[casesim-dispute-moot]]
- [[review-legal-risk-generic]]
