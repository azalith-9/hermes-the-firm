---
name: import-security-review-openai
description: Use when migrating a security-review skill originally built for the OpenAI API into the mini-hermes-the-firm format. The adapter maps legacy security-analysis logic — threat modelling, vulnerability classification, OWASP alignment, data-protection risk flags, and remediation recommendations — into the standard skill model. Relevant for legal tech products, API security assessments, and AI-system due-diligence workflows.
license: MIT
metadata: " id: import.security-review-openai category: import jurisdictions: [__multi__] priority: P3 intent: [__import__, security-review, openai, migration, legal-tech, cybersecurity] related: [import-skill-creator-openai, import-red-team-verifier-patrick-munro, import-dpia-sentinel, import-gdpr-breach-sentinel] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'import'.
Registered as a flat plugin skill.
-->


# Import: Security Review (OpenAI)

## What it does

This import adapter migrates a **security-review skill originally built for the OpenAI API** into the `mini-hermes-the-firm` standard format. The source skill may have used GPT-4 function calling, a structured JSON-output mode, or a chain-of-thought system prompt to perform security analysis of code, API configurations, infrastructure, or AI-system deployments.

In the legal AI context, security review has specific importance: legal platforms process highly privileged and sensitive data (client communications, confidential contracts, personal data); a security vulnerability in the platform creates legal liability (data-breach notification obligations, professional-conduct risks, client loss). The security review skill feeds directly into DPIA analysis and breach-sentinel workflows.

## Import config

| Field | Source mapping | Default if absent |
|---|---|---|
| `review_scope` | Legacy `scope` | `api_and_data_handling` |
| `threat_model` | Legacy `threat_model` | `STRIDE` |
| `owasp_alignment` | Legacy `owasp` boolean | `true` |
| `ai_specific_checks` | Legacy `ai_checks` boolean | `true` |
| `data_protection_check` | Legacy `dp_check` boolean | `true` |
| `severity_scale` | Legacy `severity` | CRITICAL / HIGH / MEDIUM / LOW / INFO |
| `output_format` | Legacy `format` | `security_report` |
| `remediation_guidance` | Legacy `remediation` boolean | `true` |

## Dry-run preview

```
IMPORT PREVIEW — security-review-openai
Source shape     : OpenAI security-review skill
Scope            : api_and_data_handling
Threat model     : STRIDE
OWASP alignment  : enabled
AI-specific      : enabled
Data protection  : enabled
Severity         : CRITICAL / HIGH / MEDIUM / LOW / INFO
Output           : security_report
Remediation      : enabled
```

## Security review methodology (post-import)

### STRIDE threat model
| Threat | Description | Example in legal AI context |
|---|---|---|
| **S**poofing | Impersonating a user or system | Forged JWT tokens granting access to another client's matter files |
| **T**ampering | Modifying data in transit or at rest | Injection into AI prompts to alter contract analysis output |
| **R**epudiation | Denying actions; lack of audit trail | No logging of who accessed privileged documents |
| **I**nformation disclosure | Exposing sensitive data | Client data leaking between tenants in multi-tenant SaaS |
| **D**enial of service | Degrading or blocking availability | Prompt-flooding attacks causing API rate-limit exhaustion |
| **E**levation of privilege | Gaining higher access than authorised | User role escalation to access all matters |

### OWASP API Top 10 checks
1. Broken Object Level Authorisation (BOLA)
2. Broken Authentication
3. Broken Object Property Level Authorisation
4. Unrestricted Resource Consumption
5. Broken Function Level Authorisation
6. Unrestricted Access to Sensitive Business Flows
7. Server-Side Request Forgery (SSRF)
8. Security Misconfiguration
9. Improper Inventory Management
10. Unsafe Consumption of APIs

### AI-specific security checks
- **Prompt injection**: can a user craft input that overrides system instructions or exfiltrates data?
- **Training data leakage**: does the model regurgitate confidential data it was fine-tuned on?
- **Model output manipulation**: can adversarial input cause the model to produce legally inaccurate output that creates liability?
- **API key exposure**: are OpenAI/Anthropic API keys stored securely (not in client-side code or version control)?
- **Data retention policy**: is conversation history retained by the AI provider? For how long? Does the retention comply with legal professional privilege and GDPR?

### Data-protection security checks
- **Encryption at rest**: are client documents and AI outputs encrypted at rest?
- **Encryption in transit**: TLS 1.2+ for all API calls?
- **Access control**: role-based access control per matter; no cross-matter data access?
- **Audit logging**: complete, tamper-evident log of who accessed what, when?
- **Data residency**: is data processed in a jurisdiction compatible with client data-protection obligations (EU, UAE, etc.)?
- **Sub-processor DPAs**: are DPAs in place with all AI API providers (Anthropic, OpenAI)?

## Output schema

```
SECURITY REVIEW REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Scope          : [reviewed system/component]
Review date    : [date]
Threat model   : STRIDE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FINDING #1
Severity       : CRITICAL / HIGH / MEDIUM / LOW / INFO
Category       : [STRIDE / OWASP category]
Description    : [what the vulnerability is]
Impact         : [legal / regulatory / operational consequence]
Remediation    : [specific fix]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DATA PROTECTION SUMMARY
GDPR / PDPL exposure: [HIGH / MEDIUM / LOW]
Key issues           : [list]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Failure modes

| Error | Likely cause | Resolution |
|---|---|---|
| `openai_specific_checks` | Source contained GPT-4 API-specific checks | Map to provider-agnostic equivalents |
| `ai_checks_disabled` | Legacy only did traditional security review | Enable `ai_specific_checks: true` |
| `no_data_protection_track` | Source was pure AppSec review | Add data-protection check layer |
| `severity_scale_mismatch` | Legacy used 5-level vs 4-level | Map to CRITICAL/HIGH/MEDIUM/LOW/INFO |

## Related skills

- [[import-skill-creator-openai]]
- [[import-red-team-verifier-patrick-munro]]
- [[import-dpia-sentinel]]
- [[import-gdpr-breach-sentinel]]
- [[import-skill-creator-anthropic]]
