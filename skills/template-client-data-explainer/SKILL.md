---
name: template-client-data-explainer
description: Use when a law firm or enterprise client asks how Louis handles their data — during procurement review, onboarding, or a client trust conversation. Produces a plain-language explainer covering storage, processing, retention, sharing, training restrictions, encryption, access controls, audit trail, and deletion. For formal security questionnaire responses, pair with the vendor-security-questionnaire-responses template.
license: MIT
metadata: " id: template.client-data-explainer category: template priority: P1 intent: [__template__] related: [template-vendor-security-questionnaire-responses, template-firm-ai-policy, safety-bar-rule-1-1-competence-ai] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'template'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Template — Client Data Explainer

## When to use this

Use this template when:
- A prospective or current client (law firm, in-house legal team, enterprise procurement) asks "what does Louis do with our data?"
- Onboarding a new firm account and the IT or data-governance team has questions.
- Responding to a data-privacy due-diligence request that does not rise to the level of a full security questionnaire.
- Preparing a plain-language data trust page for the Louis website or help centre.

For formal, structured security questionnaires (SOC 2, ISO 27001, vendor-risk forms), use [[template-vendor-security-questionnaire-responses]] instead.

## Template — Plain-language version

Adapt the language below to the recipient's sophistication level. For in-house IT/legal: keep technical terms. For solo practitioners: simplify.

---

**How Louis handles your data**

**Storage**
Your documents and matter data are stored in Supabase Postgres. EU-region hosting is available on request. Data for each client (tenant) is stored in a fully isolated environment — one firm's data is never accessible to another firm.

**Processing**
When you ask Louis to draft, review, or research, your content is sent to an AI model for that specific task only. Processing happens per-tenant; there is no pooling of data across firms.

**Retention**
By default, matter documents are retained for 7 years (consistent with standard professional-records retention for legal matters). This is configurable per tenant — you can request shorter or longer retention to match your firm's policy.

**Cross-tenant sharing**
Your data is never shared with other firms or users outside your tenant. Subprocessors (such as the AI model provider and the database host) are bound by a Data Processing Agreement (DPA). A copy of our DPA is available on request.

**AI training**
AI model providers do not use your data to train their models. This is contractually guaranteed in our subprocessor agreements. We rely on standard model APIs; your client documents never become training data.

**Encryption**
All data is encrypted in transit (TLS 1.2+) and at rest (AES-256). Encryption keys are managed by the hosting provider's key-management service.

**Access controls**
Row-Level Security (RLS) is enforced at the database layer, ensuring that each tenant can only access its own data. Within your firm, access is controlled by the roles and permissions your administrator configures.

**Audit trail**
A full audit log is maintained for all AI-assisted actions — who ran what task, on which document, at what time. This log is accessible to your firm administrator on request and supports your professional-responsibility obligations.

**Data deletion**
If you close your account or request deletion, all your firm's data is fully purged within 30 days. This includes all documents, matter records, and derived AI outputs. Deletion confirmation is available in writing.

---

## Customisation points

| Variable | Default | Override |
|---|---|---|
| Data region | EU (Supabase EU) | KSA and UAE region on roadmap; request during procurement |
| Retention period | 7 years | Configurable per tenant |
| DPA availability | Available on request | Provide pre-signed DPA for enterprise accounts |
| Subprocessor list | Available on request | Publish on trust page when list stabilises |

## Jurisdictional data-residency notes

| Jurisdiction | Requirement | Louis status |
|---|---|---|
| UAE | NESA data-localisation guidelines; ADGM GDPR-equivalent | EU region default; UAE region on roadmap |
| KSA | Cloud-first policy requires KSA-hosted data for government clients | KSA region on roadmap; flag during government-sector sales |
| EU / EEA | GDPR data-residency requirements | EU region available; SCCs cover non-EU subprocessors |
| Lebanon | No mandatory data-localisation currently | EU region default is compliant |

## Do not

- Do not claim SOC 2 Type II or ISO 27001 certification until achieved (see [[template-vendor-security-questionnaire-responses]] for current status).
- Do not promise KSA or UAE region availability until infrastructure is deployed.
- Do not describe data as "deleted immediately" — the 30-day purge window is the accurate commitment.

## Related skills

- [[template-vendor-security-questionnaire-responses]]
- [[template-firm-ai-policy]]
- [[safety-bar-rule-1-1-competence-ai]]
