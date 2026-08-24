---
name: import-legal-risk-assessment-anthropic
description: Use when migrating a legal risk-assessment skill originally authored for the Anthropic the agent API into the mini-hermes-the-firm format. The adapter maps legacy risk-scoring matrices, issue taxonomies, severity buckets, and remediation guidance into the standard skill model. Supports multi-jurisdictional risk frameworks covering MENA (UAE, KSA, LB, EG), EU, UK, and France.
license: MIT
metadata: " id: import.legal-risk-assessment-anthropic category: import jurisdictions: [__multi__] priority: P3 intent: [__import__, legal-risk, risk-assessment, migration, anthropic] related: [import-legal-risk-assessment-zacharie-laik, import-contract-review-anthropic, import-red-team-verifier-patrick-munro, review-legal-risk-generic] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'import'.
Registered as a flat plugin skill.
-->


# Import: Legal Risk Assessment (Anthropic)

## What it does

This import adapter migrates a **legal risk-assessment skill** originally built for Anthropic's the agent API into the `mini-hermes-the-firm` standard format. Legal risk-assessment skills sit at the core of any AI-assisted legal workflow: they identify legal exposure in contracts, transactions, regulatory submissions, or operational processes, score each issue by severity and likelihood, and recommend remediation.

The Anthropic-native implementation may have used a flat system-prompt with a bespoke risk taxonomy, a JSON schema for structured output, or a chain-of-thought prompt. This adapter detects the shape and maps it forward.

## Import config

| Field | Source mapping | Default if absent |
|---|---|---|
| `risk_taxonomy` | Legacy `categories` or `risk_types` | 8-category legal taxonomy (see below) |
| `severity_scale` | Legacy `severity` field | HIGH / MEDIUM / LOW |
| `likelihood_scale` | Legacy `likelihood` field | HIGH / MEDIUM / LOW |
| `risk_matrix` | Legacy `matrix` object | 3×3 (severity × likelihood) |
| `output_schema` | Legacy `format` | `structured_markdown_table` |
| `remediation_guidance` | Legacy `recommendations` boolean | `true` |
| `jurisdiction` | Legacy `jurisdiction` | `__multi__` |
| `scope_limit` | Legacy `scope` note | None (full document scope) |

## Dry-run preview

```
IMPORT PREVIEW — legal-risk-assessment-anthropic
Source shape  : Anthropic risk-assessment system prompt
Risk taxonomy : 8-category (contract / regulatory / litigation / IP / data /
                employment / corporate / financial)
Matrix        : 3×3 severity × likelihood
Output        : structured markdown table + narrative summary
Remediation   : enabled
Jurisdiction  : __multi__
```

## Default risk taxonomy (8 categories)

When the legacy config did not define risk categories, the adapter seeds:

| # | Category | Description |
|---|---|---|
| 1 | **Contract risk** | Unfavourable terms, missing clauses, enforceability gaps |
| 2 | **Regulatory / compliance risk** | Non-compliance with applicable statutes or regulations |
| 3 | **Litigation risk** | Exposure to claims, disputes, or enforcement action |
| 4 | **IP risk** | Ownership uncertainty, infringement exposure, licensing gaps |
| 5 | **Data protection risk** | GDPR / PDPL / local privacy-law violations |
| 6 | **Employment risk** | Labour-law non-compliance, wrongful termination exposure |
| 7 | **Corporate / governance risk** | Director duties, shareholder rights, constitutional issues |
| 8 | **Financial / credit risk** | Payment default, security gaps, guarantee exposure |

## Risk matrix (default 3×3)

| | **HIGH likelihood** | **MEDIUM likelihood** | **LOW likelihood** |
|---|---|---|---|
| **HIGH severity** | CRITICAL | HIGH | MEDIUM |
| **MEDIUM severity** | HIGH | MEDIUM | LOW |
| **LOW severity** | MEDIUM | LOW | NEGLIGIBLE |

## Output schema (post-import)

```markdown
## Legal Risk Assessment

| # | Issue | Category | Severity | Likelihood | Risk Level | Recommendation |
|---|---|---|---|---|---|---|
| 1 | [issue description] | Contract | HIGH | MEDIUM | HIGH | [action] |
...

### Summary
Overall risk profile: [HIGH / MEDIUM / LOW]
Critical issues: [count]
Immediate action required: [list]
```

## MENA jurisdictional risk flags

The imported skill surfaces these MENA-specific risks automatically:

- **UAE onshore**: penalty clauses disproportionate to actual damage may be reduced by courts under UAE Civil Transactions Law; flag if liquidated damages exceed a plausible estimate of actual loss.
- **KSA**: Shariah-compliance check required for interest (riba) provisions; late-payment clauses must use agreed compensation formulae, not compound interest.
- **Lebanon**: macro-economic instability creates FX risk in USD-denominated contracts payable locally; flag currency and force-majeure provisions.
- **DIFC / ADGM**: common-law jurisdiction; English-law concepts of penalty clauses apply; check for exclusions of consequential loss.
- **Egypt**: Civil Code Art 224 allows courts to reduce or increase agreed penalties; assess proportionality.

## Failure modes

| Error | Likely cause | Resolution |
|---|---|---|
| `taxonomy_not_mapped` | Legacy used custom category names | Auto-map to nearest standard category + flag for review |
| `matrix_missing` | No risk matrix in source | Apply default 3×3 |
| `output_unstructured` | Legacy output was free-form narrative | Wrap in structured table post-import |
| `jurisdiction_mismatch` | Source assumed US law | Flag MENA-specific differences |

## Related skills

- [[import-legal-risk-assessment-zacharie-laik]]
- [[import-contract-review-anthropic]]
- [[import-red-team-verifier-patrick-munro]]
- [[review-legal-risk-generic]]
- [[review-contract-generic]]
