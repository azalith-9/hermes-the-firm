---
name: tool-e-signature-orchestrator
description: Use when orchestrating e-signature workflows after a document has been drafted or reviewed. Routes to the correct e-signature platform by jurisdiction — Tawqi3i or Nafath (KSA), UAE Pass (UAE government-facing), DocuSign Connect (commercial cross-border), ITIDA-licensed providers (Egypt), qualified TSPs under eIDAS (EU). Handles signer order, witness requirements, notarisation triggers, and apostille/legalisation flags for cross-border execution.
license: MIT
metadata: " id: tool.e-signature-orchestrator category: tool jurisdictions: [KSA, UAE, EG, LB, EU, __multi__] priority: P1 intent: [e-signature] related: [tool-docx-extractor, draft-nda-bilateral, pa-workflow-transactional, kb-e-signature-law-mena] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'tool'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Tool — E-Signature Orchestrator

## What it does

Selects and configures the appropriate e-signature platform for a document based on jurisdiction, document type, and the parties' identities. Creates the signing envelope with correct signer order, field placement, and callback URLs. Flags additional formality requirements — witness execution, notarisation, or apostille — before the signing workflow is initiated.

## Setup / auth

Each supported platform requires its own API credentials:

| Platform | Auth method | Notes |
|---|---|---|
| **DocuSign Connect** | OAuth 2.0 (JWT grant) | Requires DocuSign developer account; Connect plan for API access |
| **Adobe Acrobat Sign** | OAuth 2.0 | Adobe Sign API; similar capabilities to DocuSign |
| **Tawqi3i (KSA)** | API key + SFDA integration | Saudi national e-signature; integrate via Tawqi3i developer portal |
| **UAE Pass** | OAuth 2.0 + PKI | UAE digital identity; integrate via UAE Pass developer portal (TDRA) |
| **ITIDA-licensed TSPs (Egypt)** | Varies by provider | Egypt IT Industry Development Authority licensed providers |

## Platform routing rules

### KSA

| Scenario | Platform |
|---|---|
| KSA government or government-adjacent agreements | **Tawqi3i** (Saudi national e-signature, legally recognised under KSA E-Transactions Law) |
| B2C consumer-facing agreements (KSA individuals) | **Nafath** (National Single Sign-On identity for consumer authentication) |
| Cross-border commercial agreements (international counterparties) | **DocuSign** or **Adobe Sign** — internationally recognised; counterparty-agnostic |

**KSA note:** The KSA E-Transactions Law (Royal Decree M/18) recognises electronic signatures but specifies that certain documents (e.g., personal status matters, real estate transfers) must be executed in hard copy before a notary (Mojaz or MOJ Najiz). Do not route those documents through e-signature without flagging.

---

### UAE

| Scenario | Platform |
|---|---|
| UAE government-facing agreements (government entity counterparty) | **UAE Pass** (PKI-based; TDRA-recognised) |
| Commercial B2B agreements (UAE + international) | **DocuSign Connect** |
| Consumer / individual signatory in UAE | UAE Pass available; DocuSign also accepted |

**UAE note:** UAE Federal Decree-Law No. 46/2021 on Electronic Transactions and Trust Services recognises electronic signatures. Certain documents still require physical notarisation under the Notary Public Law — e.g., powers of attorney to be used with government entities, some real-estate transactions.

---

### Egypt

- **ITIDA-licensed providers** are required for "advanced" electronic signatures under Egypt's E-Signature Law No. 15/2004.
- DocuSign and Adobe Sign may be used for standard commercial agreements between sophisticated parties, but the "qualified" level requires an ITIDA-accredited trust service provider.
- For real-estate and corporate actions, a notarised hard copy remains the standard.

---

### Lebanon

- **E-Signature Law 81/2018** recognises qualified electronic signatures.
- Qualified signatures require a certificate from an accredited Lebanese Certification Authority (CA).
- For commercial contracts between businesses, DocuSign/Adobe Sign are commonly accepted in practice.
- For agreements requiring Lebanese notary certification, physical execution is required.

---

### EU

- **eIDAS Regulation (EU) No. 910/2014** governs electronic signatures.
- Three tiers: Simple Electronic Signature (SES), Advanced (AES), Qualified (QES).
- QES (highest tier) is legally equivalent to a handwritten signature across all EU member states; requires a Qualified Trust Service Provider (QTSP) — e.g., GlobalSign, DocuSign EU, Adobe Sign EU.
- For high-value or regulated transactions in the EU (financial services, real estate), QES may be required.

## Output schema

```json
{
  "platform": "DocuSign",
  "envelopeId": "ENV-2026-001",
  "signerOrder": [
    { "role": "Seller", "name": "Ahmed Al Rashid", "email": "ahmed@corp.ae", "order": 1 },
    { "role": "Buyer", "name": "Sarah Johnson", "email": "sarah@intl.com", "order": 2 }
  ],
  "fields": [
    { "type": "signature", "signerRole": "Seller", "page": 12, "x": 100, "y": 400 },
    { "type": "date", "signerRole": "Seller", "page": 12, "x": 200, "y": 400 }
  ],
  "callbackUrl": "https://api.haqq.ai/webhooks/esign/completed",
  "validityFlags": {
    "witnessRequired": false,
    "notarisationRequired": false,
    "apostilleRequired": false,
    "notes": "Standard commercial NDA — no additional formality required"
  }
}
```

## Validity guardrails — pre-flight checks

Before initiating the signing workflow, run the following checks:

| Check | Rule | Flag if |
|---|---|---|
| **Witness requirement** | UAE: certain commercial deeds and powers of attorney require 2 witnesses | Document type is a deed or POA |
| **Notarisation** | UAE: POAs for government use; KSA: certain commercial agreements; LB: real estate transfers | Document type triggers notarisation under applicable law |
| **Apostille / legalisation** | Cross-border execution where the receiving jurisdiction requires apostille (Hague Convention member) or full legalisation chain | One party is in a non-Hague country (e.g., some MENA jurisdictions are not Hague members) |
| **Arabic language requirement** | KSA: government contracts must be in Arabic; UAE: Arabic is the controlling language for onshore contracts | Document is English-only for a jurisdiction requiring Arabic |
| **Age / capacity** | Minor signatories not permitted; corporate signatories require authorised signatory confirmation | Signatory is unknown or underage |

## Failure modes

| Failure | Response |
|---|---|
| Tawqi3i / UAE Pass auth failure | Surface re-authentication prompt; do not proceed without valid signature certificate |
| Signatory email bounce | Flag before envelope is sent; request corrected email |
| Notarisation flagged but workflow sent anyway | Hard stop — do not allow sending if notarisation pre-check fails |
| Callback URL unreachable | Log failure; retry 3× with exponential backoff; alert the user |

## Related skills

- [[tool-docx-extractor]]
- [[draft-nda-bilateral]]
- [[pa-workflow-transactional]]
- [[kb-e-signature-law-mena]]
