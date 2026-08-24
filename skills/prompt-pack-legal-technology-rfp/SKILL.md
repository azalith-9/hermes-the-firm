---
name: prompt-pack-legal-technology-rfp
description: Use when a legal department or law firm is issuing a request for proposal (RFP) for a legal technology solution such as a contract management system, e-billing platform, matter management system, or legal research tool. Produces a structured RFP covering functional and technical requirements, security standards, integration needs, evaluation criteria, and pricing. Applicable to corporate legal departments and law firms of all sizes.
license: MIT
metadata: " id: prompt-pack.legal-technology-rfp category: prompt-pack practice_area: legal-ops-billing priority: P2 intent: [drafting, legal-technology-rfp] related: - prompt-pack-outside-counsel-guidelines - prompt-pack-legal-department-kpi-dashboard - prompt-pack-legal-budget-forecast - prompt-pack-master-services-agreement source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'prompt-pack'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Legal Technology RFP

## When to use this

Use this skill to draft a formal request for proposal for a legal technology product or service. The RFP structures the selection process, ensures vendors address the department's specific requirements, and creates a documented basis for the final vendor selection decision.

Triggers:
- "We need to select a contract lifecycle management system — draft us an RFP."
- "Issue an RFP for an e-billing platform."
- "We're buying a matter management system — what should the RFP cover?"
- "We need a legal research platform for our regional offices in the UAE and KSA."

## Required inputs

| Input | Why it matters | Default |
|---|---|---|
| Technology category | Scopes the functional requirements (CLM, e-billing, matter management, legal research, e-discovery, AI legal assistant) | Ask user |
| Company name and department | Names the RFP and contextualizes the requirements | Ask user |
| Current systems / integrations needed | Determines technical compatibility requirements | Ask user |
| Timeline for selection and deployment | Enables vendors to plan response and implementation | Ask user |
| User base size | Affects pricing; enterprise vs mid-market requirements | Ask user |

## Optional inputs

- Budget range (including for RFP anonymity — many organizations do not disclose budget in RFP)
- Geographic scope of deployment (single-country vs multi-region — important for MENA multi-language requirements)
- Data residency requirements (sensitive for government-linked entities in UAE/KSA with local data residency obligations)
- Existing vendor relationships to preserve or eliminate
- Diversity / ESG requirements for vendors

## RFP structure

### Section 1: Introduction and Background
- Brief description of the issuing organization and legal department
- Purpose of the RFP: selecting a [solution type] to support [business objectives]
- Current-state description: existing tools, pain points, reason for change
- Timeline: RFP issue date, questions deadline, response deadline, shortlist announcement, demonstrations, final selection

### Section 2: RFP Process
- Submission instructions (format, file type, contact details)
- Confidentiality: vendor responses treated as confidential
- Reservation of rights: company may reject any or all proposals, negotiate with multiple vendors, request additional information
- Conflict of interest disclosure requirement

### Section 3: Functional Requirements
List requirements by priority: **Required** (must-have) vs **Preferred** (nice-to-have).

**For a Contract Lifecycle Management (CLM) system, example requirements:**
| Req. ID | Requirement | Priority | Vendor response (Meets / Partial / Does not meet) |
|---|---|---|---|
| F01 | Self-service contract request intake by business users | Required | |
| F02 | AI-assisted contract drafting from approved templates | Required | |
| F03 | Clause library with pre-approved alternative positions | Required | |
| F04 | Automated routing for approval workflows | Required | |
| F05 | E-signature integration | Required | |
| F06 | Contract repository with full-text search | Required | |
| F07 | Obligation tracking and deadline alerts | Required | |
| F08 | Reporting: contract volume, cycle time, risk profile | Preferred | |
| F09 | Multilingual interface (Arabic / English) | Required for MENA deployment | |
| F10 | Support for Arabic right-to-left text in contracts | Required for MENA deployment | |

Adapt the requirements table to the specific technology category (e-billing, matter management, AI assistant, etc.).

### Section 4: Technical Requirements

| Req. ID | Requirement | Priority |
|---|---|---|
| T01 | Cloud-hosted (SaaS) with [SOC 2 Type II / ISO 27001] certification | Required |
| T02 | Single sign-on (SSO) via [SAML 2.0 / OAuth 2.0] | Required |
| T03 | API availability for integration with [ERP / HRIS / existing tools] | Required |
| T04 | Mobile application (iOS and Android) | Preferred |
| T05 | Data export in standard formats (CSV, JSON, PDF) | Required |
| T06 | Uptime SLA ≥ 99.5% | Required |
| T07 | Data residency: option to host data in [UAE / GCC / EU / US] region | Required / Preferred |
| T08 | Multi-tenant or dedicated instance | Specify per company requirement |

### Section 5: Security and Data Protection

- Data encryption in transit and at rest (AES-256 standard or equivalent)
- Access control: role-based permissions; principle of least privilege
- Audit logs: full activity logging, exportable for compliance review
- Data retention and deletion policies
- Penetration testing: frequency and most recent report availability
- Compliance: GDPR, UAE Personal Data Protection Law, KSA PDPL compliance confirmation
- Incident response: defined SLA for notification of data breaches

### Section 6: Integration Requirements

List all systems the solution must integrate with:
- ERP (SAP, Oracle, etc.)
- HRIS (Workday, SAP SuccessFactors)
- E-signature (DocuSign, Adobe Sign, or local alternatives)
- E-billing platform (if separate)
- Document management (SharePoint, NetDocuments)
- Identity provider (Azure AD, Okta)

### Section 7: Implementation and Support

- Implementation timeline: expected go-live date and milestone schedule
- Implementation methodology: vendor-led vs customer-led; professional services available?
- Training: type (live, on-demand, documentation) and scope
- Support model: SLA for support tickets (P1 critical, P2 major, P3 minor); named account manager?
- Maintenance windows and patch notification process
- Roadmap visibility: how does vendor share upcoming feature releases?

### Section 8: Pricing

Request:
- Per-seat / per-user pricing model with volume tiers
- Module pricing if the solution is modular
- Implementation and professional services costs
- Annual maintenance and support fees
- Multi-year pricing options (3-year commitment discount)
- Payment terms

Do not disclose the company's budget in the RFP; allow vendors to propose pricing based on requirements.

### Section 9: Evaluation Criteria

| Criterion | Weight |
|---|---|
| Functional fit to requirements | 30% |
| Technical architecture and security | 20% |
| Vendor stability and references | 15% |
| Implementation plan and timeline | 15% |
| Total cost of ownership (3 years) | 15% |
| MENA / Arabic language support | 5% |

### Section 10: Vendor Information Required

- Company overview, ownership, financial stability, years in operation
- Client references: 3 clients of similar size and in similar industry
- Current client count and retention rate
- Subcontractors / hosting providers
- Litigation and regulatory proceedings (if any)

## MENA-specific requirements to include

- **Arabic language support**: full RTL (right-to-left) interface and document support is essential for UAE, KSA, Egypt, Lebanon deployments where Arabic-language contracts must be drafted and managed.
- **Data residency**: UAE and KSA government-linked entities may be required to store data locally. Confirm whether the vendor can offer UAE or KSA data centers.
- **Local customer references**: ask for references from existing MENA or GCC clients.
- **VAT / e-invoicing compliance**: e-billing platforms must support VAT in UAE and KSA (including KSA Phase 2 e-invoicing ZATCA compliance).

## Common mistakes

- **Issuing an RFP without internal alignment on must-haves**: results in conflicting feedback during demos and inability to make a decision.
- **Not specifying integration requirements**: vendors will assume standard integrations; non-standard integrations discovered post-contract cause cost overruns.
- **Omitting data residency and privacy requirements**: critical oversight for MENA-region entities subject to local data protection laws.
- **Accepting vendor SaaS terms without review**: standard SaaS agreements favor vendors; negotiate data ownership, exit rights, and SLAs before signature. Use [[prompt-pack-master-services-agreement]] as a negotiation starting point.

## Related skills

- [[prompt-pack-outside-counsel-guidelines]]
- [[prompt-pack-legal-department-kpi-dashboard]]
- [[prompt-pack-legal-budget-forecast]]
- [[prompt-pack-master-services-agreement]]
