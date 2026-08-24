---
name: import-politique-confidentialite-fr
description: Use when migrating a French politique de confidentialité (privacy policy) drafting or review skill into the mini-hermes-the-firm format. The adapter maps French-language GDPR privacy-policy templates and CNIL compliance checklists into the standard skill model, covering mandatory GDPR/CNIL disclosure requirements, the Loi Informatique et Libertés overlay, and French plain-language expectations. Primary jurisdiction France; also relevant for French-speaking MENA entities subject to GDPR.
license: MIT
metadata: " id: import.politique-confidentialite-FR category: import jurisdictions: [FR, EU, LB] priority: P3 intent: [__import__, politique-confidentialite, gdpr, cnil, france, migration] related: [import-gdpr-privacy-notice-eu, import-politique-cookies-fr, import-politique-lanceur-alerte-fr, draft-privacy-notice-gdpr, kb-gdpr-data-protection] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'import'.
Registered as a flat plugin skill.
-->


# Import: Politique de Confidentialité (France)

## What it does

This import adapter migrates a **French politique de confidentialité (privacy policy) skill** into the `mini-hermes-the-firm` standard format. In France, the privacy policy is the primary transparency instrument under GDPR as implemented through the Loi Informatique et Libertés (as amended). The CNIL provides detailed guidance on what a compliant politique de confidentialité must contain.

This is the French-language, France-specific cousin of the `import-gdpr-privacy-notice-eu` skill: it preserves the French drafting conventions, CNIL-specific requirements, and Loi Informatique et Libertés overlay that do not exist in the generic EU GDPR template.

## Import config

| Field | Source mapping | Default if absent |
|---|---|---|
| `policy_type` | Legacy `type` | `politique_de_confidentialite` |
| `audience` | Legacy `audience` | `b2c` (consumer-facing) |
| `language` | Legacy `lang` | `fr` |
| `cnil_format` | Legacy `cnil_layered` boolean | `true` (layered notice format) |
| `post_mortem_clause` | Legacy `post_mortem` boolean | `true` (Loi Informatique et Libertés Art 85) |
| `cookies_separate` | Legacy `separate_cookie_policy` boolean | `true` |
| `dpo_contact` | Legacy `dpo` | Prompt user if DPO appointed |
| `output_format` | Legacy `format` | `full_policy_fr` |

## Dry-run preview

```
IMPORT PREVIEW — politique-confidentialite-FR
Source shape   : French privacy policy template / checker
Type           : politique_de_confidentialite
Audience       : B2C
Language       : French
CNIL layered   : enabled
Post-mortem    : enabled (Loi I&L Art 85)
Cookies        : separate policy referenced
Output         : full_policy_fr
```

## CNIL mandatory content checklist

A CNIL-compliant politique de confidentialité must include:

### Identité du responsable de traitement
- [ ] Nom et coordonnées du responsable de traitement
- [ ] Coordonnées du DPO (si désigné)

### Finalités et bases légales
- [ ] Finalité(s) précise(s) de chaque traitement
- [ ] Base(s) légale(s) correspondante(s) (consentement, contrat, obligation légale, intérêt légitime, intérêts vitaux, mission d'intérêt public)
- [ ] Pour l'intérêt légitime : description de l'intérêt poursuivi

### Destinataires et transferts
- [ ] Catégories de destinataires
- [ ] Transferts hors UE : mécanisme de protection (décision d'adéquation, clauses contractuelles types, BCR)

### Durées de conservation
- [ ] Durée de conservation ou critères pour la déterminer — pour chaque traitement

### Droits des personnes concernées
- [ ] Droit d'accès (Art 15 RGPD)
- [ ] Droit de rectification (Art 16)
- [ ] Droit à l'effacement (Art 17)
- [ ] Droit à la limitation (Art 18)
- [ ] Droit à la portabilité (Art 20)
- [ ] Droit d'opposition (Art 21)
- [ ] Retrait du consentement (Art 7(3))
- [ ] Droit de réclamation auprès de la CNIL
- [ ] **Droit relatif aux directives post-mortem** (Loi Informatique et Libertés Art 85) — spécifique à la France

### Profilage et décisions automatisées
- [ ] Existence de décisions automatisées incluant le profilage (Art 22 RGPD)
- [ ] Logique impliquée et portée des conséquences

### Cookies et traceurs (si applicable)
- [ ] Référence à la politique cookies distincte ou section dédiée
- [ ] Conformité CNIL recommandation du 17 septembre 2020 (consentement préalable pour cookies non essentiels)

## French specifics vs GDPR baseline

| Element | French specificity |
|---|---|
| Langue | La politique doit être en français si le site s'adresse à des personnes établies en France (Loi Toubon) |
| Post-mortem | Droit de définir les directives relatives aux données post-décès — obligatoire en France |
| Réclamation CNIL | Mention expresse de la possibilité de saisir la CNIL (Commission Nationale de l'Informatique et des Libertés) |
| Cookies | Référence obligatoire à la politique cookies si cookies utilisés ; consentement exprès requis hors cookies fonctionnels |
| Profilage commercial | CNIL recommande clarté spécifique sur toute utilisation des données à des fins de ciblage publicitaire |

## Common import issues

| Issue | Resolution |
|---|---|
| Policy drafted in English | Translate to French; apply Loi Toubon compliance |
| Post-mortem clause missing | Add Art 85 clause — mandatory in France |
| DPO not named | Prompt user; if no DPO, state that clearly |
| Cookie policy merged into main policy | Recommend separation (CNIL best practice) |
| Intérêt légitime undefined | Flag HIGH risk; must specify the precise interest |

## Related skills

- [[import-gdpr-privacy-notice-eu]]
- [[import-politique-cookies-fr]]
- [[import-politique-lanceur-alerte-fr]]
- [[draft-privacy-notice-gdpr]]
- [[kb-gdpr-data-protection]]
