---
name: prompt-pack-vendor-risk-assessment-questionnaire
description: Use when a company needs to generate a structured due-diligence questionnaire to assess risks before onboarding a vendor or renewing a material vendor contract — covering data security practices, compliance certifications, business continuity, subcontractor management, insurance, financial stability, and incident notification procedures. Particularly important for regulated entities in MENA (financial services, healthcare, government) where third-party risk management is increasingly required by regulation.
license: MIT
metadata: " id: prompt-pack.vendor-risk-assessment-questionnaire category: prompt-pack practice_area: corporate-commercial jurisdictions: [UAE, KSA, LB, EG, DIFC, ADGM, GCC, EU, UK] priority: P2 intent: [compliance, vendor-risk-assessment-questionnaire, due-diligence, procurement, third-party-risk] related: - prompt-pack-vendor-data-protection-addendum - prompt-pack-vendor-agreement-red-flag-scan - prompt-pack-transition-services-agreement - kb-aml-kyc-mena - review-commercial-contract source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'prompt-pack'.
Registered as a flat plugin skill.
-->


# Vendor Risk Assessment Questionnaire

## When to use this

Use this skill when a procurement, legal, compliance, or IT team needs to assess a vendor before contracting, when renewing a material vendor relationship, or when conducting a periodic third-party risk review. A vendor risk assessment questionnaire (VRAQ) is the primary tool for documenting that the company has exercised reasonable due diligence over its supply chain.

Typical triggers:
- New vendor onboarding where the vendor will handle sensitive data, critical infrastructure, or regulated activities
- Annual or biennial renewal review for tier-1 and tier-2 vendors
- Post-incident review — a vendor security incident prompts a formal reassessment
- Regulatory requirement — financial regulators in UAE (CBUAE, SCA), KSA (SAMA), DIFC (DFSA), and Egypt (CBE) increasingly mandate third-party risk management programs for regulated entities

The output of this skill is a question bank that the company can send to the vendor, score, and use as the basis for a risk rating (Low / Medium / High / Critical).

## Required inputs

| Input | Why it matters | Sensible default |
|-------|---------------|-----------------|
| Company name and primary sector | Shapes the emphasis of the questionnaire (financial, healthcare, tech) | Prompt user |
| Vendor name and services to be provided | Determines which risk domains are most relevant | Prompt user |
| Tier classification | Tier 1 (critical / sensitive data); Tier 2 (significant); Tier 3 (low-risk) | Classify based on data sensitivity and business criticality |
| Data types involved | Drives the data security and compliance sections | Prompt user — personal data, financial data, health data, government data |
| Applicable regulatory frameworks | Determines which compliance certifications are required | Based on jurisdiction and sector |

## Optional inputs

- **Prior incident history** — if the vendor has a known breach or regulatory action, include targeted questions
- **Sub-contractor / fourth-party risk scope** — whether to include questions about the vendor's own supply chain
- **Financial credit risk threshold** — prompts financial stability section if vendor is a critical sole-source
- **Industry-specific requirements** — SWIFT CSP for financial institutions; PCI-DSS for payment processing; HIPAA for healthcare (if US nexus)

## Questionnaire structure

The following is the recommended question bank, organized by risk domain. Each domain should produce a score (1–5 scale or RAG: Red / Amber / Green).

---

### Section 1 — Company Information and Governance

1.1 Provide the vendor's full legal name, registration number, jurisdiction of incorporation, and registered address.

1.2 Who is the vendor's data protection officer (DPO) or privacy contact? Provide name and contact details.

1.3 Does the vendor have a current privacy policy that complies with applicable data protection law? (Attach or provide URL.)

1.4 Has the vendor been subject to any regulatory investigation, sanction, or fine in the past 3 years? If yes, describe.

1.5 Is the vendor subject to any current litigation that could materially affect its ability to perform services?

1.6 Does the vendor have a code of conduct or ethics policy? Is it enforced with sanctions for violations?

---

### Section 2 — Information Security

2.1 Does the vendor hold any of the following certifications? (Check all that apply; provide certificate and expiry date.)
- ISO 27001
- SOC 2 Type I / Type II
- PCI-DSS (if applicable)
- CSA STAR
- NIST CSF alignment

2.2 Describe the vendor's access control mechanisms, including multi-factor authentication (MFA) enforcement and least-privilege policies.

2.3 How is data encrypted at rest and in transit? Specify encryption standards (e.g., AES-256, TLS 1.3).

2.4 How frequently does the vendor conduct vulnerability assessments and penetration testing? Who performs them?

2.5 Does the vendor have a Secure Development Lifecycle (SDLC) process? Describe key security gates.

2.6 How is privileged access (admin accounts, root access) managed and monitored?

2.7 What is the vendor's patch management policy? Average time to patch critical vulnerabilities?

2.8 Is the vendor's IT environment cloud-hosted, on-premises, or hybrid? If cloud, identify cloud provider(s) and data residency location(s).

---

### Section 3 — Data Protection and Privacy

3.1 For each category of personal data the vendor will process, describe the legal basis under which it processes that data.

3.2 Does the vendor have a data processing agreement (DPA) template? Attach.

3.3 Will personal data be processed in, or transferred to, countries outside the controller's jurisdiction? If yes, identify countries and transfer mechanism (e.g., SCCs, adequacy decision, TDRA/SDAIA approval).

3.4 Does the vendor use sub-processors? If yes, provide a list with names, locations, and roles.

3.5 How does the vendor handle data subject rights requests (access, erasure, portability)? What is the response timeline?

3.6 What is the vendor's data retention and deletion policy? Describe the certified deletion process.

---

### Section 4 — Security Incident and Breach Notification

4.1 Describe the vendor's security incident response plan. Who is the primary point of contact for incident notification?

4.2 What is the vendor's contractual commitment for notifying customers of a security incident? (Target: within 24–48 hours of discovery.)

4.3 Has the vendor experienced any data breaches or security incidents in the past 3 years? If yes, describe nature, scope, and remediation actions.

4.4 Does the vendor carry cyber liability / data breach insurance? Provide coverage limits and insurer name.

---

### Section 5 — Business Continuity and Disaster Recovery

5.1 Does the vendor have a documented Business Continuity Plan (BCP) and Disaster Recovery Plan (DRP)? Date of last test?

5.2 What is the vendor's Recovery Time Objective (RTO) and Recovery Point Objective (RPO) for critical services?

5.3 Where are the vendor's primary and backup data centers located? Are they geographically separated?

5.4 Describe the vendor's redundancy and failover architecture.

5.5 Has the vendor experienced any service outages exceeding [4 hours] in the past 24 months? If yes, describe cause and resolution.

---

### Section 6 — Subcontractor and Fourth-Party Management

6.1 Does the vendor use subcontractors to deliver any part of the services? If yes, list names, roles, and jurisdictions.

6.2 Does the vendor require its subcontractors to comply with security and data protection standards equivalent to those required by this questionnaire?

6.3 How does the vendor monitor and audit its subcontractors?

6.4 Does the vendor have a policy for terminating subcontractors who fail to meet security or compliance requirements?

---

### Section 7 — Compliance and Regulatory

7.1 Identify the data protection and privacy regulations to which the vendor is subject. How does the vendor demonstrate compliance?

7.2 Does the vendor have an AML / KYC compliance program (if applicable to the services)? Describe key controls.

7.3 Is the vendor subject to any sanctions or export control restrictions? How does it screen for prohibited parties?

7.4 Does the vendor comply with applicable local content or Saudization / Emiratization requirements in relevant jurisdictions?

7.5 Does the vendor have a whistleblower / reporting hotline for compliance concerns?

---

### Section 8 — Insurance Coverage

8.1 Provide evidence of the following insurance policies (provide certificate of insurance):
- General liability: [minimum USD 5M per occurrence]
- Professional indemnity / E&O: [minimum USD 5M per claim]
- Cyber liability / data breach: [minimum USD 5M per claim]
- Workers' compensation: [as required by law]

8.2 Are the above policies on an occurrence or claims-made basis?

---

### Section 9 — Financial Stability

9.1 Provide the vendor's most recent audited financial statements (or last 2 years if available).

9.2 Is the vendor subject to any insolvency proceedings, creditor protection, or material debt covenant defaults?

9.3 What is the vendor's largest customer concentration? (No single customer should represent > 30% of revenue for a tier-1 vendor without additional due diligence.)

---

## Scoring and risk rating

| Score | Risk level | Recommended action |
|---|---|---|
| 90–100% compliant | Low | Proceed to contract; annual review |
| 70–89% | Medium | Negotiate contractual mitigants; quarterly check-in |
| 50–69% | High | Senior sign-off required; enhanced contractual terms; semi-annual audit |
| < 50% | Critical | Do not onboard without remediation plan; escalate to C-suite and legal |

## Jurisdictional notes

- **UAE / DIFC / KSA financial sector:** CBUAE, DFSA, and SAMA require regulated entities to maintain third-party risk management frameworks; this questionnaire can form the basis of the required vendor assessment documentation
- **KSA:** Vendors handling government or health data must typically store and process that data within Saudi Arabia; cloud-based vendors should specifically answer the data residency questions (§2.8, §3.3)
- **Egypt:** CBE Circular on Cybersecurity (2021) requires banks to assess vendors; adapt questions to CBE framework
- **EU DORA (Digital Operational Resilience Act):** Financial entities in the EU under DORA must maintain registers of ICT third-party providers; this VRAQ should feed into that register

## Limits and escalation

- A completed VRAQ is not a guarantee of vendor security; it is evidence of due diligence
- Escalate to security review by a qualified CISO or third-party assessor for tier-1 vendors handling critical data
- Legal review required before signing contracts with vendors rated High or Critical

## Related skills

- [[prompt-pack-vendor-data-protection-addendum]]
- [[prompt-pack-vendor-agreement-red-flag-scan]]
- [[prompt-pack-transition-services-agreement]]
- [[kb-aml-kyc-mena]]
- [[heuristic-always-state-jurisdiction-first]]
