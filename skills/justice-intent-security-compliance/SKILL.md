---
name: justice-intent-security-compliance
description: Use when the public-facing assistant detects that a user — typically a procurement officer, law firm IT lead, in-house counsel, or compliance officer — is asking about data security, privacy compliance, data residency, SOC 2, GDPR, PDPL, or other regulatory requirements before adopting Louis. Routes to security documentation, addresses common enterprise security questions, and escalates to the security team for formal vendor assessments. Covers all jurisdictions.
license: MIT
metadata: " id: justice.intent.security-compliance category: justice jurisdictions: [__multi__] priority: P1 intent: [__justice__, security, compliance, data-privacy, gdpr, pdpl, soc2, vendor-assessment] related: [justice-intent-sales, justice-intent-developer-api, justice-intent-investor-inquiry, justice-intent-feature-question] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'justice'.
Registered as a flat plugin skill.
-->


# Justice Intent — Security & Compliance

## When to use this

Trigger when the message contains any of the following:

- Security posture questions: "Is Louis secure?", "How do you handle my data?", "Where is data stored?", "data residency"
- Privacy regulation references: "GDPR", "PDPL" (Saudi or UAE), "data protection", "privacy policy", "DPA"
- Enterprise procurement signals: "vendor assessment", "security questionnaire", "infosec review", "pen test results", "SOC 2", "ISO 27001"
- Legal-specific compliance concerns: "client confidentiality", "privilege", "professional secrecy", "bar ethics and AI"
- Data handling questions: "do you train on my data?", "do you store my documents?", "who can see my files?", "encryption"
- Jurisdiction-specific requirements: "UAE data localization", "KSA NCA requirements", "DIFC Data Protection Law"

## Response pattern

### Step 1: Acknowledge the legitimacy of the question

Security and compliance questions are high-stakes for law firms — client confidentiality is foundational to legal professional ethics in every jurisdiction. Treat these inquiries with priority.

### Step 2: Route to security documentation

Direct to `/security` (the canonical security page) for the full security white paper, compliance certifications, and DPA template.

### Step 3: Address common questions directly

| Question | Answer |
|---|---|
| **Do you train on my data?** | No. Customer documents are not used to train any model. Each session is isolated. |
| **Where is data stored?** | Configurable by region for enterprise customers; default is [configured region]. EU and MENA data residency options available for enterprise. |
| **Is data encrypted?** | Yes — at rest (AES-256) and in transit (TLS 1.3). |
| **Who can access my documents?** | Only authorized users on your workspace. HAQQ staff cannot access customer documents except as required for technical support (audited). |
| **BYO-key model** | Enterprise customers can supply their own Anthropic API key — data passes through the customer's key and is not processed via HAQQ's key. |
| **SOC 2** | In progress / [current status — verify before responding]. |
| **GDPR compliance** | DPA available on request; data processor agreement covers EU data subjects. |
| **Saudi PDPL compliance** | Louis's data handling is designed to align with PDPL (Saudi Arabia Personal Data Protection Law, effective 2023 / amended 2024) requirements for cross-border processing. |
| **UAE PDPL / DIFC Data Protection** | UAE Federal PDPL (Federal Decree-Law 45/2021) and DIFC Data Protection Law 2020 — DPA available; data residency options available for UAE enterprise. |
| **Client privilege / professional secrecy** | Louis does not break privilege. Documents processed remain within the customer's workspace. HAQQ recommends reviewing local bar rules on AI use before sharing privileged materials with any AI tool. |

### Step 4: Escalate for formal vendor assessments

For enterprise procurement requiring formal security questionnaires (SIG, CAIQ, custom):
1. Route to the enterprise sales team via `/enterprise` or `/security/contact`
2. Provide a completion timeline estimate for the questionnaire
3. Note that a formal DPA, NDA, and MSA can be executed ahead of deployment

## Bar ethics and AI (MENA + key jurisdictions)

Many law firms — particularly those regulated by bar associations in Lebanon, UAE, France, and KSA — need to understand bar ethics guidance on AI use:

| Jurisdiction | Key guidance |
|---|---|
| **Lebanon (Beirut Bar)** | No specific AI guidance as of 2024; general professional secrecy obligations (art. 22+ Code of Professional Conduct) apply |
| **UAE** | Dubai Legal Affairs Department and DIFC Courts have issued guidance on AI-assisted legal work; confidentiality obligations unchanged |
| **KSA** | Saudi Authority for Lawyers — AI use must comply with existing professional conduct rules; no dedicated AI ethics rules as of 2024 |
| **France** | Conseil National des Barreaux — issued guidance in 2023 on AI and professional secrecy; use of AI for privileged matters requires precautions |
| **UK (SRA)** | Solicitors Regulation Authority — guidance on AI use published 2023; firms must ensure adequate supervision of AI outputs |

Recommend that users check with their bar association for current guidance, as this area is evolving rapidly.

## Do not

- Do not make unverified claims about specific certifications (SOC 2 Type II, ISO 27001) unless they have been confirmed as current
- Do not claim absolute data privacy without noting that terms and privacy policy are the binding documents
- Do not fabricate data residency regions or pricing for data residency options

## Related skills

- [[justice-intent-sales]]
- [[justice-intent-developer-api]]
- [[justice-intent-feature-question]]
- [[justice-intent-investor-inquiry]]
