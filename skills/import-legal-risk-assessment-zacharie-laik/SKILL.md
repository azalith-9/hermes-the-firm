---
name: import-legal-risk-assessment-zacharie-laik
description: Use when migrating the Zacharie Laik legal risk-assessment methodology into the mini-hermes-the-firm format. This import adapter preserves the Laik practitioner framework — structured risk identification, qualitative scoring, and mitigation sequencing — mapping it into the standard skill model with MENA and civil-law jurisdictional context. Triggers when importing a risk-assessment skill attributed to or modelled on the Laik approach.
license: MIT
metadata: " id: import.legal-risk-assessment-zacharie-laik category: import jurisdictions: [FR, LB, UAE, EU, __multi__] priority: P3 intent: [__import__, legal-risk, risk-assessment, migration, practitioner-methodology] related: [import-legal-risk-assessment-anthropic, import-contract-review-anthropic, import-statute-analysis-rafal-fryc, review-legal-risk-generic] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'import'.
Registered as a flat plugin skill.
-->


# Import: Legal Risk Assessment (Zacharie Laik)

## What it does

This import adapter migrates a **legal risk-assessment skill modelled on the Zacharie Laik practitioner methodology** into the `mini-hermes-the-firm` standard format. Laik's approach is practitioner-sourced and emphasises structured qualitative analysis over checkbox scoring — each risk is characterised by its legal basis, the factual trigger, and a concrete mitigation path, rather than a simple numeric score.

The adapter is distinct from the generic Anthropic risk-assessment import (`import-legal-risk-assessment-anthropic`) in that it preserves the **practitioner-voice framing**: risks are described as a lawyer would advise a client, with the reasoning chain visible.

## Import config

| Field | Source mapping | Default if absent |
|---|---|---|
| `risk_framework` | Legacy `framework` field | Laik qualitative model |
| `issue_description_style` | Legacy `style` | `practitioner_narrative` |
| `legal_basis_required` | Legacy `cite_law` boolean | `true` |
| `mitigation_required` | Legacy `mitigation` boolean | `true` |
| `severity_scale` | Legacy `severity` | HIGH / MEDIUM / LOW |
| `output_schema` | Legacy `format` | `issue_sheet` per risk |
| `jurisdiction` | Legacy `jurisdiction` | `FR` (Laik's primary jurisdiction) |
| `language` | Legacy `lang` | `fr` |

## Dry-run preview

```
IMPORT PREVIEW — legal-risk-assessment-zacharie-laik
Source shape     : Practitioner risk-assessment (Laik methodology)
Framework        : Qualitative narrative per issue
Issue style      : practitioner_narrative (legal basis + factual trigger + mitigation)
Language         : French (default — override if needed)
Jurisdiction     : FR (civil law; override for MENA deployments)
Output           : issue_sheet per identified risk
Mitigation       : required for each issue
```

## Laik methodology (post-import skill structure)

The Laik risk-assessment model produces one **issue sheet** per identified risk:

```
ISSUE #N: [Short title]

Legal basis    : [Statute, article, or principle creating the risk]
Factual trigger: [The specific clause, fact pattern, or omission that activates risk]
Risk category  : [Contract / Regulatory / Litigation / IP / Data / Employment / Corporate]
Severity       : HIGH / MEDIUM / LOW
Likelihood     : HIGH / MEDIUM / LOW
Risk level     : [Matrix output]
Mitigation     : [Concrete remediation step — specific clause wording, process change,
                  or escalation path]
Residual risk  : [Risk remaining after mitigation — if any]
```

This structure ensures that every identified risk has a navigable reasoning chain rather than a bare score, which is more useful for legal advice memos and board presentations.

## Civil-law specifics (FR / Lebanon / UAE onshore)

The Laik methodology was developed primarily for French civil-law contexts and translates naturally to Lebanon (French-inspired civil code) and UAE/KSA onshore (also civil-code jurisdictions). Key differences the post-import skill surfaces:

- **Good faith obligation** (Art 1104 French Civil Code; Lebanese Code of Obligations Art 221): contracts must be negotiated, formed, and performed in good faith; risk analysis should flag provisions that could be characterised as bad-faith or abusive.
- **Unfair terms** (Art L212-1 French Consumer Code; DIFC Consumer Protection regime): asymmetric indemnity or limitation clauses may be struck as unfair in B2C contexts.
- **Causa / objet** (French and Lebanese law): void contracts where the cause is unlawful; flag KSA Shariah non-compliance as equivalent cause-invalidating issue.
- **Mandatory provisions** (ordre public): labour-law mandatory provisions in France; federal labour law mandatory provisions in UAE; ensure contract does not contract out.

## Output schema (post-import)

The skill produces:

1. **Executive summary**: overall risk profile (1–2 paragraphs, practitioner voice)
2. **Issue sheets**: one per identified risk (structure above)
3. **Priority matrix**: table of all issues sorted by risk level
4. **Next steps**: ordered action list (legal review, renegotiation, escalation)

## Failure modes

| Error | Likely cause | Resolution |
|---|---|---|
| `language_conflict` | Source in French; deployment context English | Set `language: en` override; preserve legal precision in translation |
| `legal_basis_missing` | Legacy omitted citations | Flag each issue as `basis: unverified`; prompt user to add |
| `civil_law_mismatch` | Deployed in DIFC/ADGM common-law context | Add jurisdiction-override flag; note common-law equivalents |
| `issue_sheets_empty` | Source had no identified issues | Re-run with full document context; check extraction quality |

## Related skills

- [[import-legal-risk-assessment-anthropic]]
- [[import-contract-review-anthropic]]
- [[import-statute-analysis-rafal-fryc]]
- [[review-legal-risk-generic]]
- [[review-contract-generic]]
