---
name: import-dpia-sentinel
description: Use when migrating a Data Protection Impact Assessment (DPIA) sentinel skill into the mini-hermes-the-firm format. The adapter maps legacy DPIA screening logic — risk thresholds, processing-activity categories, necessity/proportionality tests, and supervisory-authority notification triggers — into the standard skill model. Relevant across EU GDPR, UK GDPR, UAE PDPL, and Lebanon data-protection contexts.
license: MIT
metadata: " id: import.dpia-sentinel category: import jurisdictions: [EU, UK, UAE, LB, EG, FR] priority: P3 intent: [__import__, dpia, data-protection, gdpr, migration, privacy] related: [import-gdpr-breach-sentinel, import-gdpr-privacy-notice-eu, review-dpia-eu, kb-gdpr-data-protection] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'import'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Import: DPIA Sentinel

## What it does

This import adapter migrates a **DPIA (Data Protection Impact Assessment) sentinel skill** into the `mini-hermes-the-firm` standard format. A DPIA sentinel continuously monitors or screens processing activities to determine whether a formal DPIA is required, and if so, whether the assessment is adequate.

Under GDPR Article 35, certain categories of high-risk processing **mandate** a DPIA before processing begins. A sentinel skill automates this screening: given a description of a new or changed processing activity, it applies the Article 35(3) mandatory categories plus the supervisory authority's published criteria (the "blacklist") and flags whether a DPIA is triggered.

## Import config

| Field | Source mapping | Default if absent |
|---|---|---|
| `screening_criteria` | Legacy `triggers` or `criteria` array | GDPR Art 35(3) + CNIL/ICO blacklists |
| `risk_thresholds` | Legacy `risk_levels` | HIGH / MEDIUM / LOW |
| `output_mode` | Legacy `format` | `structured_report` |
| `jurisdiction` | Legacy `jurisdiction` | `EU` (GDPR) |
| `supervisory_authority` | Legacy `dpa` field | Inferred from jurisdiction |
| `notify_dpa_threshold` | Legacy `dpa_notification` | `HIGH` |
| `template_ref` | Legacy `dpia_template` | Standard 9-section template |

## Dry-run preview

```
IMPORT PREVIEW — dpia-sentinel
Source shape  : DPIA screening config
Screening     : GDPR Art 35(3) + CNIL blacklist (FR default)
Risk levels   : HIGH / MEDIUM / LOW
Notification  : Supervisory authority notified at HIGH
Output        : structured_report (JSON + narrative)
DPA           : CNIL (FR), ICO (UK), EDPB (cross-border)
```

## DPIA mandatory triggers (post-import logic)

The imported sentinel checks each new processing activity against:

### GDPR Article 35(3) mandatory categories
1. **Systematic and extensive profiling** with automated decision-making producing legal/significant effects on persons
2. **Large-scale processing of special-category data** (Article 9) or criminal-offence data (Article 10)
3. **Systematic monitoring of publicly accessible areas** on a large scale

### Supervisory-authority blacklists (examples)
- **CNIL (France)**: biometric data processing; loyalty programmes; social media monitoring; employee tracking; IoT combined with profiling; AI recruitment tools
- **ICO (UK)**: child data processing; matching/combining datasets from multiple sources; innovative technology use; denial of service decisions
- **EDPB**: any of the above at cross-border scale

### Additional high-risk indicators
- Processing data of vulnerable subjects (minors, patients, employees)
- Data transfer to third countries without adequacy decision
- Novel processing technology not previously assessed
- Processing enabling re-identification of pseudonymised data

## Output schema (post-import)

```json
{
  "dpia_required": true | false,
  "triggers": ["Art 35(3)(a)", "CNIL blacklist item 3"],
  "risk_level": "HIGH",
  "recommended_action": "Conduct full DPIA before processing begins",
  "dpa_notification_required": false,
  "notes": "Consult DPO. DPIA must be completed before go-live."
}
```

## Jurisdictional notes

| Jurisdiction | Framework | Key difference |
|---|---|---|
| EU | GDPR Art 35 | DPIA mandatory for Art 35(3) + DPA blacklists |
| UK | UK GDPR / DPA 2018 | ICO blacklist applies; adequacy bridges post-Brexit |
| UAE | PDPL (Fed. Decree-Law 45/2021) | No mandatory DPIA requirement by name, but risk assessment required for "sensitive data" processing and cross-border transfers |
| Lebanon | Draft Data Protection Law (pending) | No enacted DPIA requirement; GDPR standard applied as best practice |
| France | GDPR + CNIL guidance | CNIL blacklist of 16 processing types mandating DPIA |
| Egypt | Data Protection Law 151/2020 | Impact assessment referenced for sensitive data; implementing regulations govern threshold |

## Failure modes

| Error | Likely cause | Resolution |
|---|---|---|
| `criteria_empty` | Legacy config had no trigger list | Apply default GDPR Art 35(3) set |
| `jurisdiction_unknown` | Source had no jurisdiction field | Default to `EU`; prompt user to confirm |
| `template_missing` | Legacy referenced external template file | Regenerate from 9-section standard template |

## Related skills

- [[import-gdpr-breach-sentinel]]
- [[import-gdpr-privacy-notice-eu]]
- [[review-dpia-eu]]
- [[kb-gdpr-data-protection]]
- [[draft-dpa-processor-agreement]]
