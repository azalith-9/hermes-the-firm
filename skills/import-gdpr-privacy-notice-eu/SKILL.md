---
name: import-gdpr-privacy-notice-eu
description: Use when migrating a GDPR privacy-notice drafting or review skill originally built for the EU context into the mini-hermes-the-firm format. The adapter maps legacy notice templates, Article 13/14 disclosure checklists, and layered-notice structures into the standard skill model, with support for French (CNIL), UK (ICO), and cross-border EDPB guidance. Also relevant for UAE PDPL and Lebanon privacy-notice equivalents.
license: MIT
metadata: " id: import.gdpr-privacy-notice-eu category: import jurisdictions: [EU, UK, FR, UAE, LB, EG] priority: P3 intent: [__import__, gdpr, privacy-notice, data-protection, migration, eu] related: [import-politique-confidentialite-fr, import-dpia-sentinel, import-gdpr-breach-sentinel, draft-privacy-notice-gdpr, kb-gdpr-data-protection] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'import'.
Registered as a flat plugin skill.
-->


# Import: GDPR Privacy Notice (EU)

## What it does

This import adapter migrates a **GDPR-compliant privacy notice skill** into the `mini-hermes-the-firm` standard format. The source skill may have been a drafting template, a review checklist, or both; the adapter detects the mode and maps it to the appropriate skill category (`draft` or `review`).

A GDPR privacy notice is a legally mandated transparency document. Articles 13 and 14 of the GDPR prescribe the **minimum mandatory content** depending on whether data is collected directly from the data subject (Art 13) or obtained from a third-party source (Art 14). Non-compliance can trigger GDPR enforcement and fines up to €20 million or 4% of global annual turnover (whichever is higher).

## Import config

| Field | Source mapping | Default if absent |
|---|---|---|
| `notice_type` | Legacy `type` field | `art13` (direct collection) |
| `layered_notice` | Legacy `layered` boolean | `false` |
| `language` | Legacy `lang` | `en` |
| `controller_details` | Legacy `controller` object | Prompt user |
| `dpo_contact` | Legacy `dpo` object | Prompt user if DPO appointed |
| `retention_schedule` | Legacy `retention` table | Prompt user |
| `legal_bases` | Legacy `bases` array | Prompt user (no default — must be explicit) |
| `output_format` | Legacy `format` | `structured_markdown` |

## Dry-run preview

```
IMPORT PREVIEW — gdpr-privacy-notice-eu
Source shape  : GDPR privacy-notice template
Notice type   : Art 13 (direct collection)
Language      : English
Layered       : No
Controller    : [needs population]
Legal bases   : [needs population — no default]
Output        : structured_markdown
```

## GDPR Article 13 mandatory disclosure checklist

Post-import, the skill verifies or drafts all required elements:

**Identity and contact details**
- [ ] Name and address of controller
- [ ] Contact details of DPO (if appointed)

**Purpose and legal basis**
- [ ] Purpose(s) of processing
- [ ] Legal basis for each purpose (Art 6; Art 9 if special-category)
- [ ] Legitimate interests (if relied on — must be specified, not generic)

**Recipients and transfers**
- [ ] Categories of recipients
- [ ] Third-country transfers — adequacy decision or safeguards (SCCs, BCRs)

**Retention**
- [ ] Retention period or criteria used to determine it

**Data subject rights**
- [ ] Right of access (Art 15)
- [ ] Right to rectification (Art 16)
- [ ] Right to erasure (Art 17)
- [ ] Right to restriction (Art 18)
- [ ] Right to data portability (Art 20) — where applicable
- [ ] Right to object (Art 21) — where applicable
- [ ] Right to withdraw consent (Art 7(3)) — where processing based on consent
- [ ] Right to lodge complaint with supervisory authority

**Automated decision-making**
- [ ] Existence of automated decision-making including profiling (Art 22)
- [ ] Logic involved and significance of consequences

## Layered notice structure

When `layered_notice: true`, the skill produces:

- **Layer 1** (condensed — max 200 words): who is collecting, for what purpose, and how to find out more
- **Layer 2** (full notice): all Art 13/14 mandatory elements
- **Layer 3** (supplementary): technical annexes (retention schedule, sub-processor list)

## Jurisdictional notes

| Jurisdiction | Key addition vs GDPR baseline |
|---|---|
| France (CNIL) | French language required for consumer-facing notices; CNIL recommends explicit mention of right to define post-death data directives (Loi Informatique et Libertés Art 85) |
| UK (ICO) | UK GDPR post-Brexit; ICO Right to Know format preferred; mention ICO as competent authority (not EDPB) |
| UAE (PDPL) | Federal Decree-Law 45/2021 requires privacy notice to data subject at time of collection; include UAE competent authority reference |
| Lebanon | No enacted DPL; GDPR-standard notice used contractually or as best practice |
| Egypt | Data Protection Law 151/2020; privacy notice required; Arabic language advisable for domestic data subjects |

## Common import issues

| Issue | Resolution |
|---|---|
| Legal bases left blank | These cannot be defaulted — prompt user to confirm each processing purpose's legal basis explicitly |
| Retention period missing | Flag as HIGH-risk gap; a notice without retention information violates Art 13(2)(a) |
| US-style notice imported | Strip "California Privacy Rights" sections; re-map to GDPR rights catalogue |
| Multiple controllers | Add joint-controller arrangement reference (Art 26) |

## Related skills

- [[import-politique-confidentialite-fr]]
- [[import-dpia-sentinel]]
- [[import-gdpr-breach-sentinel]]
- [[draft-privacy-notice-gdpr]]
- [[kb-gdpr-data-protection]]
