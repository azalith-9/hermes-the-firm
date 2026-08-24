---
name: docs-terms-of-service-summary
description: Use when a user, prospect, or legal reviewer asks what the Louis Terms of Service say in plain language, particularly around acceptable use, IP ownership, liability limits, data handling commitments, or contract termination. Provides a plain-English summary of each key section so users can understand their rights and obligations without reading dense legalese. Not a substitute for the full ToS for legal professionals.
license: MIT
metadata: " id: docs.terms-of-service-summary category: docs jurisdictions: [__multi__] priority: P2 intent: [terms of service, acceptable use, liability, data handling, ToS summary] related: [docs-security-overview, docs-tenant-isolation-explainer, docs-whitepaper-general] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'docs'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Terms of Service — Plain-English Summary

> **Disclaimer**: This is a summary for orientation purposes only. The full, legally binding Terms of Service govern your relationship with HAQQ. In case of conflict between this summary and the full ToS, the full ToS controls. Legal professionals evaluating the ToS for their organization should read the full document.

## 1. Acceptable Use Policy (AUP)

**What you can do**: Use Louis to draft, review, summarize, and analyze legal documents; generate legal research; and assist with legal workflows in a professional capacity.

**What you cannot do**:
- Use Louis to generate false legal advice intended to deceive clients.
- Attempt to extract, reverse-engineer, or scrape the underlying models.
- Upload documents containing third-party confidential information you are not authorized to process through a third-party service (check your client engagement letters and NDAs).
- Use the platform for any purpose that violates applicable law or professional conduct rules in your jurisdiction.
- Share account credentials across users — each user must have their own account.

**Consequence**: AUP violations may result in suspension or termination of your account.

## 2. Intellectual property

**Your content**: Documents, data, and outputs you generate remain your property (or your clients' property). HAQQ does not claim ownership of your uploaded documents or the AI-generated outputs you create.

**Louis's IP**: The platform, underlying models, skill library, and related technology remain HAQQ's intellectual property. You receive a license to use the platform — you do not acquire ownership of it.

**No-training default**: HAQQ will not use your uploaded documents or conversation history to train AI models. This is a contractual commitment. Enterprise customers may further specify this in their DPA.

## 3. Liability cap

**Standard cap**: HAQQ's total liability to you in any 12-month period is capped at the fees you paid in that period.

**Consequential damages excluded**: HAQQ is not liable for lost profits, lost data, business interruption, or any indirect or consequential losses, even if foreseeable.

**What this means in practice**: If Louis produces an incorrect output that causes harm, the platform's liability is limited. Legal professionals remain responsible for the advice and documents they produce — Louis is a tool, not a lawyer. Always review AI outputs before sending them to clients or filing them with courts or regulators.

## 4. Indemnity

You agree to indemnify HAQQ against third-party claims arising from your use of the platform in violation of the AUP or applicable law. HAQQ indemnifies you against third-party claims that the platform itself infringes third-party IP (limited to the platform, not your generated content).

## 5. Data handling

- Documents are stored encrypted at rest (AES-256) and in transit (TLS 1.3).
- Tenant isolation prevents your data from being accessible to other customers.
- HAQQ acts as a data processor under GDPR (and equivalent frameworks) when processing personal data on your behalf. A Data Processing Agreement (DPA) is available for Enterprise customers.
- Data retention: your data is retained for the duration of your subscription plus a configurable grace period; you can export or delete your data at any time.
- See [[docs-security-overview]] and [[docs-tenant-isolation-explainer]] for technical details.

## 6. Termination

**By you**: Cancel at any time from your billing settings. Access continues until the end of the current billing period (no pro-rata refunds for partial periods on standard plans).

**By HAQQ**: HAQQ may suspend or terminate your account immediately for material AUP violations or non-payment (with notice and cure period for non-payment).

**Data on termination**: After termination, you have 30 days to export your data. After 30 days, data is permanently deleted (some anonymized metadata may be retained for compliance purposes).

## 7. Governing law and disputes

- The ToS is governed by the laws of [the jurisdiction specified in your agreement — check your subscription order form].
- Enterprise agreements may specify a different governing law by mutual agreement (common for MENA customers: UAE law, DIFC law, or the law of the customer's jurisdiction).
- Disputes are resolved first by good-faith negotiation, then by binding arbitration under the rules specified in the ToS.

## 8. Changes to the ToS

HAQQ may update the ToS with 30 days' notice for material changes. Continued use after the effective date constitutes acceptance. For Enterprise customers with fixed-term contracts, material ToS changes cannot be imposed mid-term without consent.

## Where to find the full ToS

`https://haqq.ai/legal/terms` — always check for the current version. The date at the top of the full document controls.

## Related skills

- [[docs-security-overview]]
- [[docs-tenant-isolation-explainer]]
- [[docs-whitepaper-general]]
- [[docs-roi-calculator]]
