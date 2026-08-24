---
name: import-mediation-dispute-analysis-jinzhe-tan
description: Use when migrating the Jinzhe Tan mediation and dispute-analysis methodology into the mini-hermes-the-firm format. This adapter preserves structured mediation-readiness analysis — party interests vs positions mapping, BATNA/WATNA scoring, settlement zone identification, and mediator-style reframing — and maps it into the standard skill model. Particularly valuable for cross-border commercial disputes in MENA, DIFC, ADGM, and Greater China corridors.
license: MIT
metadata: " id: import.mediation-dispute-analysis-jinzhe-tan category: import jurisdictions: [DIFC, ADGM, UAE, LB, UK, __multi__] priority: P3 intent: [__import__, mediation, dispute-analysis, adr, migration, settlement] related: [import-legal-simulation-patrick-munro, import-tech-contract-negotiation-patrick-munro, import-nil-contract-analysis-samir-patel, casesim-dispute-moot] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'import'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Import: Mediation Dispute Analysis (Jinzhe Tan)

## What it does

This import adapter migrates a **mediation and dispute-analysis skill modelled on the Jinzhe Tan methodology** into the `mini-hermes-the-firm` standard format. The Tan approach is rooted in interest-based negotiation theory (Fisher/Ury/Patton) and applies it to commercial legal disputes: it maps parties' **positions** (what they say they want) to their underlying **interests** (what they actually need), then identifies whether a negotiated settlement zone exists.

This is distinct from adversarial simulation (`import-legal-simulation-patrick-munro`): where simulation maximises each side's legal argument, the Tan methodology seeks the settlement path — it is the analytical counterpart to mediation itself.

## Import config

| Field | Source mapping | Default if absent |
|---|---|---|
| `analysis_mode` | Legacy `mode` | `full` (positions + interests + BATNA + zone) |
| `parties` | Legacy `parties` array | `[claimant, respondent]` |
| `batna_scoring` | Legacy `batna` boolean | `true` |
| `watna_scoring` | Legacy `watna` boolean | `true` |
| `settlement_zone` | Legacy `zopa` boolean | `true` |
| `reframing` | Legacy `mediator_reframes` boolean | `true` |
| `output_format` | Legacy `format` | `mediation_brief` |
| `governing_law` | Legacy `governing_law` | `__multi__` |

## Dry-run preview

```
IMPORT PREVIEW — mediation-dispute-analysis-jinzhe-tan
Source shape  : Interest-based mediation analysis (Tan methodology)
Mode          : full
Parties       : claimant + respondent
BATNA/WATNA   : enabled
Settlement zone: enabled (ZOPA analysis)
Reframing     : enabled (mediator-voice suggestions)
Output        : mediation_brief
```

## Analysis structure (post-import)

### 1. Position mapping
For each party, document the stated position:
- What are they publicly demanding?
- What is their opening offer / counter-offer?
- What is the legal claim or defence in formal proceedings?

### 2. Interest mapping
Beneath each position, identify underlying interests:
- Economic interests (cash, asset recovery, cost avoidance)
- Relationship interests (preservation of business relationship, reputation)
- Process interests (speed, confidentiality, certainty)
- Principled interests (fairness, precedent, moral validation)

### 3. BATNA / WATNA scoring

| Party | BATNA (Best Alternative to Negotiated Agreement) | WATNA (Worst Alternative) |
|---|---|---|
| Claimant | [strongest outcome if mediation fails] | [worst outcome if mediation fails] |
| Respondent | [strongest outcome if mediation fails] | [worst outcome if mediation fails] |

BATNA/WATNA scores determine each party's walk-away point and the **zone of possible agreement (ZOPA)**.

### 4. Settlement zone identification
If Claimant's WATNA > Respondent's BATNA → settlement zone exists.
If not → settlement zone is negative; flag that litigation may be preferred by one or both parties.

### 5. Mediator reframing (optional)
Suggest how a skilled mediator might reframe each party's position to surface interests:
- "What does Party A actually need that Party B could provide without the cost of [WATNA]?"
- Identify creative settlement structures (payment plans, non-monetary elements, apologies, reference letters) that may bridge the gap.

## Jurisdictional notes

- **DIFC / ADGM**: DIFC-LCIA Arbitration Centre and ADGM Courts both encourage mediation before arbitration; mediation is confidential and without-prejudice under DIFC Mediation Law DIFC Law No. 1 of 2021.
- **UAE onshore**: Ministerial Order No. 1 of 2021 reformed the Federal Civil Procedure Code to require mandatory reconciliation attempts in most civil matters before litigation; relevant to mediation readiness.
- **Lebanon**: Centre de Médiation et d'Arbitrage du Liban (CMAL) rules; parties may mediate before Beirut Court of Commerce arbitration.
- **GCC cross-border**: consider whether arbitration award would be enforceable under the New York Convention (UAE, KSA, Egypt, Lebanon are all signatories).

## Use cases

- **Pre-mediation brief preparation**: assess whether mediation is worth pursuing and the realistic settlement range before engaging a mediator
- **Settlement negotiation strategy**: identify each party's true interests and optimal settlement structure
- **Cross-border commercial disputes**: particularly effective where cost of arbitration is high relative to dispute value
- **Internal disputes**: applicable to joint-venture disagreements, shareholder disputes, and employment matters

## Failure modes

| Error | Likely cause | Resolution |
|---|---|---|
| `interests_not_identified` | Legacy only listed positions | Re-run with interest-elicitation prompts |
| `batna_overestimated` | Parties systematically overstate their litigation prospects | Apply litigation-cost discount and probability weighting |
| `zone_negative` | No settlement overlap | Flag; consider whether litigation economics may shift the zone |
| `confidentiality_breach_risk` | Mediation statements mixed with formal claims | Segregate mediation briefs; mark all as "without prejudice" |

## Related skills

- [[import-legal-simulation-patrick-munro]]
- [[import-tech-contract-negotiation-patrick-munro]]
- [[import-nil-contract-analysis-samir-patel]]
- [[casesim-dispute-moot]]
- [[review-legal-risk-generic]]
