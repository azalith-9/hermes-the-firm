---
name: import-nda-review-jamie-tso
description: Use when migrating the Jamie Tso NDA review methodology into the mini-hermes-the-firm format. This adapter preserves structured NDA review logic — mutual vs unilateral framing, confidentiality scope analysis, residuals clauses, permitted disclosures, and enforceability traps — mapped into the standard skill model. Particularly strong for technology-sector NDAs in DIFC, ADGM, UK, and US-influenced common-law drafting contexts.
license: MIT
metadata: " id: import.nda-review-jamie-tso category: import jurisdictions: [DIFC, ADGM, UK, UAE, __multi__] priority: P3 intent: [__import__, nda, confidentiality, review, migration] related: [import-nda-triage-anthropic, review-nda-bilateral, draft-nda-unilateral, review-contract-generic] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'import'.
Registered as a flat plugin skill.
-->


# Import: NDA Review (Jamie Tso)

## What it does

This import adapter migrates a **NDA review skill modelled on the Jamie Tso methodology** into the `mini-hermes-the-firm` standard format. The Tso NDA review approach is practitioner-sourced and technology-sector-oriented: it focuses on the practical enforceability of the confidentiality obligations, the commercial risk of residuals and carve-outs, and the interaction between the NDA and broader IP/employment arrangements.

This is distinct from the generic NDA triage (`import-nda-triage-anthropic`): the Tso review goes deeper on a specific NDA already in hand, rather than deciding whether to engage with it at all.

## Import config

| Field | Source mapping | Default if absent |
|---|---|---|
| `nda_type` | Legacy `type` | `mutual` |
| `sector` | Legacy `sector` | `technology` |
| `governing_law` | Legacy `governing_law` | `DIFC` |
| `review_depth` | Legacy `depth` | `full` |
| `residuals_check` | Legacy `check_residuals` boolean | `true` |
| `ip_interaction_check` | Legacy `check_ip` boolean | `true` |
| `term_check` | Legacy `check_term` boolean | `true` |
| `output_format` | Legacy `format` | `issue_table` |

## Dry-run preview

```
IMPORT PREVIEW — nda-review-jamie-tso
Source shape  : Practitioner NDA review (Tso methodology)
NDA type      : mutual
Sector        : technology
Governing law : DIFC
Review depth  : full
Residuals     : checked
IP interaction: checked
Term/duration : checked
Output        : issue_table
```

## Review checklist (post-import)

### Core obligation analysis
1. **Definition of Confidential Information** — Is it broad enough to protect genuinely sensitive information? Is it narrow enough to be workable? Does it exclude public domain, prior knowledge, and independently developed information with appropriate carve-outs?
2. **Obligations of the receiving party** — Non-disclosure, non-use, need-to-know access control, and protection standard (no lower than own confidential information).
3. **Permitted disclosures** — Legal compulsion (with notice obligation?), regulatory, professional advisors (with binding confidentiality obligations on them?).
4. **Residuals clause** — Does the NDA contain a residuals clause allowing the receiving party to use information retained in unaided memory? If yes, this is a significant carve-out; flag with HIGH severity in technology contexts.
5. **Term and duration** — Duration of confidentiality obligation post-termination; perpetual obligations are unusual and may be unenforceable in some jurisdictions.
6. **Return/destruction** — Obligations on termination; certifiable destruction standard.
7. **Remedies** — Specific performance and injunctive relief clauses; liquidated damages provisions.
8. **IP ownership** — Does the NDA inadvertently grant any licence or create any IP ownership risk?
9. **Employment / no-poach** — Does the NDA contain non-solicitation provisions? Are they enforceable?
10. **Governing law and dispute resolution** — Is the chosen forum appropriate and enforceable?

### Technology-sector specific checks (Tso methodology)
- **Source code and algorithms**: are these explicitly within the definition of Confidential Information?
- **Demo and trial use**: if the receiving party gets access to a product, is the scope of permitted evaluation use clearly limited?
- **Cloud/SaaS context**: does the NDA address data residency and sub-contractor access (e.g. cloud providers processing confidential data)?
- **Open-source contamination**: flag any risk that use of information could require open-sourcing under reciprocal licences.

## Jurisdictional enforceability notes

| Jurisdiction | Key enforceability issue |
|---|---|
| DIFC | Common law; injunctive relief readily available; residuals clause generally enforceable |
| UAE onshore | Civil law; confidentiality as trade secret protected under UAE Federal IP Law; penalty clauses assessed for proportionality |
| UK | Post-Brexit; common law; American Cyanamid test for interim injunctions; no equivalent to US trade-secrets statute |
| Lebanon | French-inspired civil code; breach of confidentiality can trigger tort liability (Art 124 Obligations Code); criminal penalties under specific sector laws |
| France | GDPR adds data-protection overlay; trade secrets protected under Loi relative au secret des affaires (2018) |

## Common issues flagged by Tso methodology
- Residuals clause buried in definitions (easy to miss; HIGH severity)
- Confidential Information definition circular or tautological
- No obligation to notify disclosing party before compelled disclosure
- NDA signed by entity without authority to bind the group
- Governing law is US state with specific non-compete / trade-secret overlay not suitable for MENA deployment

## Related skills

- [[import-nda-triage-anthropic]]
- [[review-nda-bilateral]]
- [[draft-nda-unilateral]]
- [[review-contract-generic]]
- [[import-tech-contract-negotiation-patrick-munro]]
