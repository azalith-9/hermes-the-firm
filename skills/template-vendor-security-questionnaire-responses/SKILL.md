---
name: template-vendor-security-questionnaire-responses
description: Use when completing enterprise vendor security questionnaires for law-firm or in-house procurement of Louis. Provides pre-approved standard responses to common security, compliance, and data-governance questions — SOC 2, ISO 27001, GDPR, penetration testing, tenant isolation, encryption, audit logs, data export, and residency. Reduces sales-cycle friction for enterprise deals.
license: MIT
metadata: " id: template.vendor-security-questionnaire-responses category: template priority: P1 intent: [__template__] related: [template-client-data-explainer, template-firm-ai-policy] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'template'.
Registered as a flat plugin skill.
-->


# Template — Vendor Security Questionnaire Responses

## When to use this

Use this template when:
- An enterprise law firm or in-house legal department sends a vendor security questionnaire (VSQ) as part of procurement.
- IT security or risk teams ask formal written questions about Louis's security posture.
- A procurement process requires ISO 27001, SOC 2, or equivalent certification evidence.

For conversational data-trust questions, use [[template-client-data-explainer]] (shorter, plain-language). This template provides the formal, Q&A-format responses expected in structured security questionnaires.

**Important:** Answers below reflect HAQQ's status as of this version. Update responses when certifications are obtained, infrastructure changes, or new data-residency regions launch. Do not submit outdated questionnaire responses.

## Standard responses

### Security certifications

**Q: Are you SOC 2 Type II certified?**
A: SOC 2 Type II audit is in progress. We expect to complete Type II certification by Q3 2026. A SOC 2 Type I report may be available in advance; contact security@haqq.ai for current status.

**Q: Are you ISO 27001 certified?**
A: ISO 27001 certification is in progress. We expect to achieve certification in H2 2026. Our information security management system (ISMS) is operational and aligned to ISO 27001 controls; formal certification is pending the audit process.

**Q: Do you have a FedRAMP authorization?**
A: Not applicable at this time; Louis is a MENA-focused product and FedRAMP is not currently sought.

---

### Data protection and privacy

**Q: Are you GDPR compliant?**
A: Yes. We operate as a data processor under GDPR for all EU/EEA personal data. A Data Processing Agreement (DPA) is available and will be executed prior to onboarding. EU-region data hosting is available.

**Q: Do you offer a Data Processing Agreement (DPA)?**
A: Yes. Our standard DPA is available for review and execution. It covers sub-processor obligations, data subject rights support, breach notification, and transfer mechanisms (Standard Contractual Clauses where applicable).

**Q: Do you comply with UAE Personal Data Protection Law (PDPL)?**
A: Yes. We comply with UAE Federal Decree-Law No. 45/2021 (PDPL). Our data-handling practices align with PDPL requirements, including lawful-basis processing and data subject rights.

**Q: Do you comply with KSA PDPL?**
A: Yes. We comply with the Kingdom of Saudi Arabia Personal Data Protection Law (PDPL, Royal Decree M/19). Data subjects' rights under KSA PDPL are supported.

---

### Penetration testing and vulnerability management

**Q: Do you conduct penetration testing?**
A: Yes. We conduct annual third-party penetration tests. Test results and remediation status are available under NDA for enterprise clients. Contact security@haqq.ai.

**Q: Do you have a vulnerability disclosure policy?**
A: Yes. Our vulnerability disclosure policy is available at [security policy URL]. Reports should be submitted to security@haqq.ai. We acknowledge receipt within 48 hours and provide remediation timelines within 14 days.

**Q: What is your patch management policy?**
A: Critical security patches are applied within 72 hours of release. High-severity patches within 14 days. We follow a continuous delivery model; infrastructure is updated on a rolling basis.

---

### Tenant isolation and multi-tenancy

**Q: Is data isolated between tenants?**
A: Yes. Row-Level Security (RLS) is enforced at the database layer. Each tenant's data is logically isolated; no cross-tenant queries are possible. Tenant-scoped API keys are used for all data access.

**Q: Is your architecture multi-tenant or single-tenant?**
A: Multi-tenant with strong logical isolation by default. Dedicated single-tenant deployments are available for enterprise clients with specific isolation requirements — contact sales@haqq.ai.

---

### Encryption

**Q: Is data encrypted in transit?**
A: Yes. All data in transit is encrypted using TLS 1.2 or higher. We do not support TLS 1.0 or 1.1.

**Q: Is data encrypted at rest?**
A: Yes. All data at rest is encrypted using AES-256 via the hosting provider's key-management service (Supabase / AWS KMS).

**Q: Do you support customer-managed encryption keys (CMEK)?**
A: Not currently available on standard plans. CMEK can be discussed for enterprise contracts — contact sales@haqq.ai.

---

### Data residency

**Q: Where is data hosted?**
A: Default: EU region (Supabase / AWS eu-west). EU-region hosting is available for all clients.

**Q: Is KSA or UAE data residency available?**
A: KSA and UAE regional hosting is on our roadmap for 2026. For clients with mandatory in-country hosting requirements, contact sales@haqq.ai to discuss timing and dedicated-deployment options.

**Q: Do subprocessors have access to client data?**
A: Subprocessors access data only as necessary to provide the contracted service, under data-processing agreements. Our subprocessor list is available on request. Key subprocessors include the cloud hosting provider (Supabase / AWS) and AI model providers. AI model providers do not use client data for model training.

---

### Audit and access logs

**Q: Do you maintain audit logs?**
A: Yes. A full audit trail is maintained for all AI-assisted actions — user, action type, document reference, timestamp. Audit logs are tenant-scoped and available to the firm's administrator on request. Log retention: 2 years by default (configurable).

**Q: Can we access audit logs directly?**
A: Yes via the admin dashboard for self-service. Full log export (JSON) is available on request and via API for enterprise accounts.

---

### Data export and deletion

**Q: Can we export our data?**
A: Yes. A full JSON archive of your matter data, documents, and audit logs is available on request and via API for enterprise accounts.

**Q: What happens to our data if we cancel?**
A: Upon account termination or deletion request, all tenant data (documents, matter records, AI outputs, audit logs) is fully purged within 30 days. Written confirmation of deletion is provided.

---

### Business continuity

**Q: What is your RTO / RPO?**
A: Recovery Time Objective (RTO): 4 hours. Recovery Point Objective (RPO): 1 hour. We operate multi-AZ deployments with automated failover. Business continuity and disaster recovery documentation is available under NDA.

**Q: Do you have cyber insurance?**
A: Yes. We maintain cyber liability insurance. Certificate of insurance available on request.

---

## Responses requiring escalation

The following questions should be escalated to the HAQQ security team before answering:
- Custom SLA commitments beyond standard terms
- Right-to-audit clauses (on-site or third-party audit rights)
- Requests for proprietary architectural diagrams
- Questions about specific AI model providers (confidential subprocessor)

## Related skills

- [[template-client-data-explainer]]
- [[template-firm-ai-policy]]
