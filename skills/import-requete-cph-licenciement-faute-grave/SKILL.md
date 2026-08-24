---
name: import-requete-cph-licenciement-faute-grave
description: Use when migrating a French Conseil de Prud'hommes (CPH) pleading skill for gross-misconduct dismissal (licenciement pour faute grave) into the mini-hermes-the-firm format. The adapter maps legacy CPH claim-drafting logic — requête, articulation des faits, qualification juridique, and demande indemnitaire — into the standard skill model under French employment law. Primary jurisdiction France; Barème Macron indemnity rules and procedural requirements of the CPH apply.
license: MIT
metadata: " id: import.requete-CPH-licenciement-faute-grave category: import jurisdictions: [FR] priority: P3 intent: [__import__, cph, licenciement, faute-grave, employment-france, migration] related: [import-notification-licenciement, draft-lettre-licenciement-fr, kb-employment-law-fr, review-employment-termination] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'import'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Import: Requête CPH — Licenciement pour Faute Grave (France)

## What it does

This import adapter migrates a **CPH pleading skill for gross-misconduct dismissal** into the `mini-hermes-the-firm` standard format. The Conseil de Prud'hommes (CPH) is the French specialised labour tribunal that handles employment disputes. A requête (claim form) is the initiating document: it sets out the parties, the facts, the legal basis, and the relief sought.

In a licenciement pour faute grave (dismissal for gross misconduct), the employer bears the burden of proving the faute grave. If the employer fails, the employee is entitled to: the notice period (préavis), the statutory dismissal indemnity (indemnité de licenciement), and damages for dismissal without cause réelle et sérieuse (under the Barème Macron scale).

## Import config

| Field | Source mapping | Default if absent |
|---|---|---|
| `claim_type` | Legacy `type` | `licenciement_faute_grave_contest` |
| `party_plaintiff` | Legacy `demandeur` | Prompt user (salarié typically) |
| `party_defendant` | Legacy `défendeur` | Prompt user (employeur) |
| `faits_details` | Legacy `facts` | Prompt user — cannot default |
| `qualification_juridique` | Legacy `legal_basis` | Code du Travail Art L1234-1, L1234-5, L1234-9 |
| `demande_indemnitaire` | Legacy `relief` | Calculated from ancienneté + salaire |
| `barème_macron` | Legacy `barème` boolean | `true` |
| `procedure_phase` | Legacy `phase` | `bureau_de_conciliation` |
| `output_format` | Legacy `format` | `requête_cph_fr` |

## Dry-run preview

```
IMPORT PREVIEW — requete-CPH-licenciement-faute-grave
Source shape        : CPH pleading template (faute grave)
Claim type          : contest of licenciement pour faute grave
Qualification       : Code du Travail Art L1234-1, L1234-5, L1234-9
Barème Macron       : enabled
Procedure phase     : bureau de conciliation (first phase)
Relief              : [requires ancienneté + salaire input]
Output              : requête_cph_fr
```

## CPH procedure overview

The CPH process for an individual employment dispute follows these stages:

1. **Requête** — filed by the plaintiff (usually the salarié); submitted to the CPH registry; must include parties' identities, summary of facts, legal basis, and relief sought.
2. **Bureau de conciliation et d'orientation (BCO)** — compulsory conciliation hearing; parties must attend or be represented; if conciliation fails, case referred to bureau de jugement.
3. **Bureau de jugement** — full hearing before two employer-side and two employee-side judges (paritaire); written submissions and oral argument.
4. **Délibéré et jugement** — decision typically within 2–6 months of hearing; may be rendered immediately or at a later date.
5. **Appel** — appeal to Cour d'appel (chambre sociale) within 1 month of notification of judgment.

## Requête: mandatory content checklist

- [ ] **Identification du demandeur** — name, address, status (salarié)
- [ ] **Identification du défendeur** — employer name, SIREN, registered address
- [ ] **Contrat de travail** — type, date, classification, remuneration (reference to pay slips)
- [ ] **Faits** — chronological narrative of: the events constituting alleged faute grave, the disciplinary procedure (convocation, entretien), and the lettre de licenciement
- [ ] **Contestation des motifs** — legal challenge to the stated faute grave (evidence that the facts are inaccurate, insufficient for faute grave, or that procedure was defective)
- [ ] **Qualification juridique** — application of Code du Travail
- [ ] **Demande indemnitaire** — itemised relief (see below)
- [ ] **Pièces** — list of supporting documents (contract, pay slips, lettre de licenciement, exchange of correspondence)

## Demande indemnitaire (relief calculation)

For a successful contest of licenciement pour faute grave, the salarié claims:

| Head of relief | Legal basis | Calculation |
|---|---|---|
| Indemnité compensatrice de préavis | Art L1234-5 | Notice period × monthly gross salary |
| Indemnité de licenciement | Art L1234-9 | Statutory formula (1/4 month per year for first 10 years; 1/3 per year thereafter) |
| Dommages-intérêts pour licenciement sans cause réelle | Art L1235-3 (Barème Macron) | See Barème scale by ancienneté |
| Indemnité de congés payés sur préavis | Art L3141-26 | 10% of préavis indemnity |
| Dommages-intérêts pour préjudice moral | Case-by-case | Discretionary (courts vary widely) |

**Barème Macron caps** (see `import-notification-licenciement` for full scale): applies to the dommages-intérêts for dismissal without cause réelle et sérieuse; does NOT apply to préavis or statutory indemnity.

## Common defences by the employer (anticipate and rebut)

1. The facts constituting faute grave are established and uncontested
2. The disciplinary procedure was properly followed
3. The proportionality of the sanction was appropriate
4. Prior warnings support the conclusion of faute grave
5. The salarié's conduct breached a clear employer policy or professional obligation

## Failure modes

| Error | Likely cause | Resolution |
|---|---|---|
| `faits_vague` | Source had generic "misconduct" placeholder | Flag HIGH risk; specific factual narrative required |
| `barème_not_applied` | Legacy calculated old indemnity formula | Apply Barème Macron (post-Ordonnances 2017) |
| `préavis_missing` | Source only claimed licenciement indemnity | Add préavis claim (separate head of relief for faute grave contests) |
| `prescription_risk` | Claim filed > 1 year after dismissal | Flag prescription: Art L1471-1 — 1-year limitation for dismissal claims |

## Related skills

- [[import-notification-licenciement]]
- [[draft-lettre-licenciement-fr]]
- [[kb-employment-law-fr]]
- [[review-employment-termination]]
- [[import-legal-risk-assessment-zacharie-laik]]
