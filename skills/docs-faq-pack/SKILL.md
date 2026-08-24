---
name: docs-faq-pack
description: Use when a user asks a general question about the platform that is likely to have a standardized answer — pricing, security, supported jurisdictions, features, integrations, training, or how to get started. This skill compiles the top frequently asked questions from sales and support tickets, organized by category, to provide rapid accurate answers without routing to a full documentation section.
license: MIT
metadata: " id: docs.faq-pack category: docs jurisdictions: [__multi__] priority: P2 intent: [__docs__, faq, pricing, security, features, integrations, support] related: [docs-billing-and-credits, docs-enterprise-deployment, docs-data-residency-mena, docs-legal-ai-workspace-guide, docs-compare-us] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'docs'.
Registered as a flat plugin skill.
-->


# FAQ Pack

## Pricing

**Q: Is there a free plan?**
Yes. The free plan includes 50 usage credits per month and access to core drafting skills (NDA, basic employment contract templates, standard clause library). No credit card required.

**Q: How does pricing work?**
Two-layer model: a per-seat subscription for access to the platform, plus usage credits for premium features (deep research, multi-doc compare, OCR ingestion). See [[docs-billing-and-credits]] for tier details.

**Q: Can I be invoiced instead of paying by card?**
Yes, on enterprise plans. Net-30 invoice billing in USD, AED, SAR, or EUR. Contact the sales team to set up.

**Q: Do unused credits roll over?**
Monthly plan: no rollover. Annual plan: unused credits roll over within the plan year. Consult current plan terms in **Settings → Billing**.

**Q: Is there a BYO-key option?**
Yes. Users can bring their own API key (Anthropic the agent, OpenAI, or similar) and the platform will route AI calls through their key. Credit consumption is reduced to infrastructure-only when a BYO key is used.

---

## Security

**Q: Where is my data hosted?**
Default: EU Frankfurt (AWS eu-central-1). MENA/GCC hosting (Bahrain region) is available on request for enterprise customers. Saudi Arabia region hosting is on the roadmap for 2026 Q2. See [[docs-data-residency-mena]].

**Q: Is my data used to train AI models?**
No. Legal document content, conversation history, and client matter data are never used to train or fine-tune AI models. This is a contractual commitment in the Terms of Service and the Data Processing Agreement.

**Q: Do you have a SOC 2 report?**
SOC 2 Type II attestation is available on request under NDA for enterprise customers.

**Q: What encryption does the platform use?**
AES-256 at rest; TLS 1.2+ in transit. Customer-managed encryption keys (BYOK) available on enterprise plans.

**Q: Can we use SSO?**
Yes. SAML 2.0 and OIDC supported. Compatible with Okta, Azure AD, Google Workspace, and other major IdPs. SCIM 2.0 for automated provisioning. Enterprise plan required.

---

## Jurisdictions and legal coverage

**Q: Which jurisdictions do you cover?**
Primary: UAE (onshore, DIFC, ADGM), Saudi Arabia, Lebanon, Egypt. Secondary: France, UK, EU, US (Delaware), Singapore, OHADA, GCC cross-border. Best-in-class for MENA; basic coverage for other jurisdictions.

**Q: Can the platform draft in Arabic?**
Yes. Native Arabic drafting is supported. Bilingual (Arabic-English) output is available for most document types. Arabic-script trademark handling is covered for MENA filings.

**Q: Do you cover Islamic finance?**
Yes. Murabaha, ijarah, diminishing musharaka, and sukuk intake and drafting skills are included.

**Q: Is Sharia inheritance planning covered?**
Yes, in the will intake skill. The platform flags Sharia mandatory share rules and the DIFC/ADGM Will option for non-Muslims. For detailed Sharia jurisprudence calculations, the platform recommends engaging a specialized Islamic estate attorney.

**Q: Do you cover KSA Vision 2030 regulatory sectors?**
The clause library and skill set are updated for major regulatory changes. The platform follows KSA MISA, SAMA, ZATCA, SAIP, and SDAIA regulatory updates. Specific recent amendments: verify with the changelog or ask directly about the specific regulation.

---

## Features

**Q: What document types can the platform draft?**
Over 200 document types including: NDAs, employment contracts, SHAs, MSAs, loan agreements, leases, powers of attorney, wills, trademark filings, litigation briefs, corporate resolutions, term sheets, and more.

**Q: Can I upload a contract for review?**
Yes. Upload a PDF or Word document and invoke a review skill. The platform will redline, flag risks, and summarize deviations from market standard.

**Q: Does the platform compare two contract versions?**
Yes. Multi-document compare generates a redline comparison and a structured change summary. Costs credits (see [[docs-billing-and-credits]]).

**Q: Is there an OCR function for scanned documents?**
Yes. OCR ingestion converts scanned PDFs to searchable text before analysis. Costs credits per page.

**Q: Can I track matters?**
Yes. The matter management feature organizes documents, conversations, and deadlines by client matter. Integration with HubSpot, Stripe, NetSuite, QuickBooks, and Xero is available on enterprise plans.

---

## Integrations

**Q: What integrations are available?**
Current: HubSpot (CRM), Stripe (billing), NetSuite, QuickBooks, Xero (accounting). API available for custom integrations. See [[docs-dev-hub-api-reference]].

**Q: Is there a Microsoft Word add-in?**
Not currently. The platform is browser-first. Documents can be exported as .docx for Word editing. A Word add-in is on the roadmap — verify current status with the product team.

**Q: Is there a mobile app?**
Yes. iOS and Android. See [[docs-mobile-app-onboarding]] for setup. Core drafting and matter access supported; some features are web-only.

---

## Training and onboarding

**Q: Is training available?**
Yes. Self-serve: onboarding tutorial, in-app guides, video library. Enterprise: live onboarding sessions with the customer success team; train-the-trainer programs for large rollouts.

**Q: How long does it take to get up and running?**
For self-serve: under 30 minutes to first document draft. For enterprise: 4–6 weeks for full deployment including SSO and integrations. See [[docs-enterprise-deployment]].

**Q: Is there documentation?**
Yes. Full user guide at [[docs-legal-ai-workspace-guide]]. Developer documentation at [[docs-dev-hub-api-reference]]. FAQ at this page. Support tickets via the in-app help widget.

---

## Support

**Q: How do I get support?**
In-app help widget (bottom right) for live chat. Email support for non-urgent questions. Enterprise customers have a named CSM and priority support queue.

**Q: What is the uptime SLA?**
Professional/Team: 99.5% uptime. Enterprise: 99.9% uptime with P1 incident resolution within 4 hours.

**Q: Can I export all my data?**
Yes. Self-serve export of all documents, matters, and audit logs available in **Settings → Data Export**. Enterprise customers can configure automated export via SIEM or API.

---

## Related skills

- [[docs-billing-and-credits]]
- [[docs-enterprise-deployment]]
- [[docs-data-residency-mena]]
- [[docs-legal-ai-workspace-guide]]
- [[docs-compare-us]]
