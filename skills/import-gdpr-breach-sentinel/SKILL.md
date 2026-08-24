---
name: import-gdpr-breach-sentinel
description: Use when migrating a GDPR personal-data breach sentinel skill into the mini-hermes-the-firm format. The adapter maps legacy breach-detection logic — severity scoring, the 72-hour supervisory-authority notification clock, data-subject communication triggers, and cross-border lead-authority routing — into the standard skill model. Covers EU GDPR, UK GDPR, UAE PDPL, and analogous MENA data-breach regimes.
license: MIT
metadata: " id: import.gdpr-breach-sentinel category: import jurisdictions: [EU, UK, UAE, LB, EG, FR] priority: P3 intent: [__import__, gdpr, data-breach, sentinel, migration, privacy-compliance] related: [import-dpia-sentinel, import-gdpr-privacy-notice-eu, kb-gdpr-data-protection, review-data-breach-response] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'import'.
Registered as a flat plugin skill.
-->


# Import: GDPR Breach Sentinel

## What it does

This import adapter migrates a **GDPR personal-data breach sentinel skill** into the `mini-hermes-the-firm` standard format. A breach sentinel monitors incident reports and security alerts, applies the Article 33/34 GDPR decision tree, and outputs a triage record that tells the legal/privacy team exactly what must be done and within what deadline.

Under GDPR Article 33(1), a personal data breach **must be notified to the competent supervisory authority within 72 hours** of discovery — unless the breach is unlikely to result in a risk to the rights and freedoms of natural persons. Article 34 imposes a separate obligation to notify affected data subjects **without undue delay** when the breach is likely to result in **high risk**.

## Import config

| Field | Source mapping | Default if absent |
|---|---|---|
| `breach_categories` | Legacy `incident_types` array | Confidentiality / Integrity / Availability |
| `severity_matrix` | Legacy `risk_matrix` | GDPR WP250 criteria |
| `notification_clock` | Legacy `sla_hours` | `72` hours (Art 33) |
| `subject_notification_threshold` | Legacy `high_risk_threshold` | `HIGH` risk |
| `lead_authority_routing` | Legacy `dpa_routing` | EDPB one-stop-shop rules |
| `record_template` | Legacy `breach_log_template` | Art 33(5) mandatory fields |
| `jurisdiction` | Legacy `jurisdiction` | `EU` |

## Dry-run preview

```
IMPORT PREVIEW — gdpr-breach-sentinel
Source shape   : GDPR breach-response config
Breach types   : Confidentiality / Integrity / Availability
Severity matrix: WP250 criteria (data type × affected population × likelihood)
Clock          : 72h supervisory authority; undue delay for data subjects
Lead authority : EDPB one-stop-shop (cross-border EU)
Record         : Art 33(5) breach register fields
```

## Breach triage decision tree (post-import logic)

```
INCIDENT DETECTED
       │
       ▼
Is personal data involved?
  No → Not a personal data breach. Log as internal incident only.
  Yes ↓
       ▼
Is there a risk to rights and freedoms?
  Unlikely → Document decision; no DPA notification required (Art 33(1) proviso)
  Possible or Certain ↓
       ▼
Notify supervisory authority within 72h (Art 33)
       │
       ▼
Is risk HIGH?
  No → Notification to data subjects NOT required (Art 34(1) n/a)
  Yes → Notify affected data subjects without undue delay (Art 34(1))
```

## Severity scoring (WP250 / EDPB guidelines)

The sentinel scores breaches on three axes:

| Axis | Criteria | Score |
|---|---|---|
| **Data type** | Special-category (health, biometric, political, financial) | +2 |
| | Identifiable personal data | +1 |
| | Pseudonymised / encrypted (attacker cannot decode) | 0 or -1 |
| **Affected population** | >100,000 data subjects | +2 |
| | 1,000–100,000 | +1 |
| | <1,000 | 0 |
| **Likely consequences** | Identity theft, financial loss, discrimination likely | +2 |
| | Inconvenience, temporary loss | +1 |
| | Minimal | 0 |

Total score → LOW (0–1) / MEDIUM (2–3) / HIGH (4–6).

## Notification record (Art 33(5) mandatory fields)

The sentinel generates a breach record containing:

1. Nature of the breach (confidentiality / integrity / availability)
2. Categories and approximate number of data subjects concerned
3. Categories and approximate number of personal data records concerned
4. Name and contact details of the DPO (if appointed)
5. Likely consequences of the breach
6. Measures taken or proposed to address the breach, including to mitigate its possible adverse effects

## Jurisdictional notes

| Jurisdiction | Framework | Key difference vs GDPR |
|---|---|---|
| EU | GDPR Art 33–34 | Baseline; 72h clock; EDPB one-stop-shop |
| UK | UK GDPR / DPA 2018 | ICO as lead; same 72h clock; post-Brexit no EDPB |
| France | GDPR + CNIL | CNIL is French lead DPA; CNIL notification portal |
| UAE | PDPL Art 14 | "Prompt notification" to UAE competent authority; no explicit 72h; controller also notifies data subjects if "significant harm" likely |
| Lebanon | No enacted DPL | Apply GDPR standard as contractual obligation / best practice |
| Egypt | Law 151/2020 | Notification to NCIDP within "reasonable time"; implementing regulations set specific timelines |

## Failure modes

| Error | Likely cause | Resolution |
|---|---|---|
| `severity_matrix_empty` | Legacy had no risk matrix | Apply WP250 default scoring |
| `clock_not_set` | Legacy had no SLA field | Default to 72h; flag for user confirmation |
| `authority_unknown` | No DPA mapped for jurisdiction | Prompt user; default to EDPB for cross-border |
| `record_template_missing` | No breach-log template in source | Generate from Art 33(5) mandatory fields |

## Related skills

- [[import-dpia-sentinel]]
- [[import-gdpr-privacy-notice-eu]]
- [[kb-gdpr-data-protection]]
- [[review-data-breach-response]]
- [[draft-dpa-processor-agreement]]
