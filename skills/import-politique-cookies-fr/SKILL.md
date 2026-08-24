---
name: import-politique-cookies-fr
description: Use when migrating a French cookie policy (politique de cookies) drafting or review skill into the mini-hermes-the-firm format. The adapter maps French CNIL cookie-compliance logic — consent requirements for non-essential cookies, exemption categories, cookie-banner specifications, and retention limits — into the standard skill model. Primary jurisdiction France; relevant for any EU/EEA entity targeting French users.
license: MIT
metadata: " id: import.politique-cookies-FR category: import jurisdictions: [FR, EU] priority: P3 intent: [__import__, cookies, cnil, france, migration, privacy] related: [import-politique-confidentialite-fr, import-gdpr-privacy-notice-eu, import-politique-lanceur-alerte-fr, kb-gdpr-data-protection] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'import'.
Registered as a flat plugin skill.
-->


# Import: Politique de Cookies (France)

## What it does

This import adapter migrates a **French politique de cookies (cookie policy) skill** into the `mini-hermes-the-firm` standard format. The CNIL's September 2020 recommendation (and subsequent guidance) set specific requirements for cookie consent in France that go beyond the generic GDPR Article 6 framework: explicit, informed, and granular consent is required for all non-essential cookies before they are placed, with a dedicated consent mechanism that meets the CNIL's technical specifications.

The French cookie framework is among the strictest in the EU: the CNIL has issued enforcement decisions against major operators for non-compliant cookie banners, and fines can reach €200,000 per violation.

## Import config

| Field | Source mapping | Default if absent |
|---|---|---|
| `policy_type` | Legacy `type` | `politique_cookies` |
| `cookie_categories` | Legacy `categories` array | Standard 5-category taxonomy |
| `consent_mechanism` | Legacy `consent_tool` | `cmp` (Consent Management Platform) |
| `retention_period` | Legacy `retention_days` | `13 months` (CNIL maximum) |
| `analytics_exemption` | Legacy `analytics_exempt` boolean | `false` (requires explicit check) |
| `language` | Legacy `lang` | `fr` |
| `output_format` | Legacy `format` | `full_cookie_policy_fr` |

## Dry-run preview

```
IMPORT PREVIEW — politique-cookies-FR
Source shape      : French cookie policy template / checker
Cookie categories : 5-category taxonomy
Consent mechanism : CMP
Retention         : 13 months (CNIL maximum)
Analytics exempt  : requires verification
Language          : French
Output            : full_cookie_policy_fr
```

## CNIL cookie taxonomy (5 categories)

| Category | Description | Consent required? |
|---|---|---|
| **Essentiels** | Session, login, shopping cart, load balancing | No — exempt |
| **Analytiques** | Audience measurement (e.g. Matomo, AT Internet — CNIL-approved config) | Potentially exempt if CNIL-configured; otherwise yes |
| **Publicitaires** | Behavioural advertising, retargeting | Yes — explicit consent |
| **Réseaux sociaux** | Social sharing buttons, embedded feeds | Yes — explicit consent |
| **Personnalisation** | User-preference storage (language, display) beyond session | Depends on purpose |

## Analytics exemption (CNIL specifics)

The CNIL grants a limited exemption for analytics cookies that meet **all** of these conditions:
- Purpose strictly limited to audience measurement for the controller (no cross-site or cross-service sharing)
- Strictly anonymised data (no IP address stored, no cross-device linking)
- Data not combined with other processing for other purposes
- CMP must still inform users of the cookies, even if consent is not required
- AT Internet and Matomo in CNIL-approved configurations qualify; Google Analytics requires consent (CNIL deliberation 2022)

## Cookie banner CNIL requirements

A compliant cookie banner must:
- [ ] Be displayed **before any non-exempt cookie is set**
- [ ] Offer an **equally prominent** "Accepter tout" (accept) and "Refuser tout" (refuse) button — the refuse option must be as easy to click as the accept option
- [ ] Allow granular consent by category
- [ ] Not use dark patterns (pre-ticked boxes, deceptive visual hierarchy)
- [ ] Record and store proof of consent (timestamp, version of policy, user ID or session)
- [ ] Allow withdrawal of consent as easily as it was given

## Cookie policy mandatory content

The politique de cookies must disclose:

- [ ] Definition and purpose of cookies
- [ ] List of cookies placed: name, provider, purpose, duration, category
- [ ] How to manage cookies (browser settings + CMP)
- [ ] Consequences of refusal (functionality impact)
- [ ] Duration: CNIL maximum 13 months for consent storage; 25 months for cookie lifetime
- [ ] Link to the main politique de confidentialité
- [ ] How to contact the DPO / controller regarding cookie concerns

## Common import issues

| Issue | Resolution |
|---|---|
| Banner pre-ticks non-essential cookies | Flag HIGH risk; CNIL enforcement priority |
| Refuser button harder to find than Accepter | Flag HIGH risk; equal prominence required |
| Analytics assumed exempt | Verify CNIL configuration; flag if Google Analytics used without consent |
| No consent storage | Flag HIGH risk; no proof of consent = GDPR violation |
| Policy only in English | Translate to French; Loi Toubon compliance required for French users |

## Related skills

- [[import-politique-confidentialite-fr]]
- [[import-gdpr-privacy-notice-eu]]
- [[import-politique-lanceur-alerte-fr]]
- [[kb-gdpr-data-protection]]
- [[draft-privacy-notice-gdpr]]
