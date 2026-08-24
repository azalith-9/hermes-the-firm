---
name: safety-pii-redaction-before-rag
description: Use when personal data in user-uploaded documents or query content must be redacted before indexing to the vector store or before sending to a third-party LLM provider. Defines the full redaction taxonomy (names, national IDs, IBANs, phones, emails, addresses, health data), placeholder naming conventions, the tenant-scoped reverse-map for rehydration, and the opt-out mechanism for eFirm matters requiring real identifiers. Core to GDPR/PDPL data-minimization obligations and bar-rules confidentiality.
license: MIT
metadata: " id: safety.PII-redaction-before-RAG category: safety jurisdictions: [US, UK, LB, KSA, UAE, DIFC, ADGM, GCC, EU, FR] priority: P0 intent: [safety, PII, redaction, RAG, data-minimization, confidentiality] related: - safety-bar-rule-1-6-confidentiality-ai - safety-client-confidentiality-cross-tenant - safety-bar-rules-confidentiality - safety-cross-border-data-transfer-gcc-eu - safety-attorney-work-product-ai-handling source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'safety'.
Registered as a flat plugin skill.
-->


# PII Redaction Before RAG / External Calls

## When to use this

Apply before:
1. **Indexing user-uploaded documents** to the vector store (RAG ingestion pipeline).
2. **Sending content to a third-party LLM endpoint** (e.g., the underlying language model API).
3. **Sending content to any external service** — translation API, classification service, etc.

**Default**: redaction is on by default for all tenants. Opt-out is available per-matter for eFirm tenants where substance review requires real identifiers.

**Do not apply** for internal operations within the tenant boundary where the tenant has consented to processing real identifiers (e.g., the final response sent back to the originating user).

## Why this matters

- **Bar-rules confidentiality (Rule 1.6 and analogs)**: disclosing client information to AI vendors without appropriate safeguards may breach confidentiality obligations — see [[safety-bar-rule-1-6-confidentiality-ai]].
- **GDPR / PDPL data-minimization principle**: only process personal data to the extent necessary for the purpose. If the LLM can answer the legal question on pseudonymized data, sending real identifiers is unnecessary processing.
- **Cross-border transfer risk reduction**: pseudonymized data is lower risk for cross-border transfers under GDPR and GCC PDPLs — see [[safety-cross-border-data-transfer-gcc-eu]].
- **Training data risk**: some AI providers may train on inputs; redaction ensures that even if training occurs, client identifiers are not incorporated.

## Redaction taxonomy

### What to redact — replace with semantic placeholders

| PII type | Placeholder format | Notes |
|----------|-------------------|-------|
| Personal names (natural persons) | `[PERSON_1]`, `[PERSON_2]` | Preserve role distinctions: `[CLAIMANT]`, `[RESPONDENT]`, `[WITNESS_1]` where role matters |
| Corporate names (non-public parties) | `[COMPANY_A]`, `[COMPANY_B]` | Use `[CLIENT_CO]` vs `[COUNTERPARTY_CO]` to preserve relational context |
| National ID numbers, passport numbers, civil registration numbers | `[NAT_ID]` | Any government-issued identifier |
| IBAN, bank account numbers, routing numbers | `[ACCOUNT]` | Financial account identifiers |
| Credit/debit card numbers | `[CARD]` | Full and partial card numbers |
| Phone numbers | `[PHONE]` | Include country code format variants |
| Email addresses | `[EMAIL]` | |
| Physical addresses (below city level) | `[ADDRESS]` | City and country can remain; street / building / apartment level redacted |
| Health information | `[HEALTH]` | Diagnoses, medications, procedures, clinical notes |
| Financial position data (net worth, salary, detailed financials) | `[FINANCIAL]` | Where not already in public corporate filings |
| Biometric data | `[BIOMETRIC]` | Where referenced in documents |

### What NOT to redact

| Content | Reason |
|---------|--------|
| Entity names of publicly listed companies where they are the matter subject | These are public facts; redaction would impair the legal analysis |
| Court case captions for already-public rulings | Public record; citation value is lost by redaction |
| Statutory / regulatory text being analyzed | This is the legal content, not PII |
| Jurisdiction, date, and document type | Needed for legal analysis context |
| Judge names, court names, prosecutor names in public proceedings | Public officials acting in public capacity |

## Placeholder naming conventions

Use **role-based placeholders** where possible rather than generic numbered ones:
- `[CLAIMANT]` / `[DEFENDANT]` rather than `[PERSON_1]` / `[PERSON_2]` — preserves the legal relationship while redacting identity.
- `[CLIENT_CO]` / `[TARGET_CO]` for M&A matters — preserves deal structure.
- `[LESSOR]` / `[LESSEE]` for lease matters.

Where multiple instances of the same category exist and roles aren't distinct:
- `[PERSON_1]`, `[PERSON_2]`, `[PERSON_3]` — consistent numbering within a document; cross-reference map held in reverse-map.

## Reverse map — rehydration

The redaction engine maintains a **tenant-scoped, encrypted reverse map** that records the correspondence between each placeholder and the original value.

- The reverse map is stored in encrypted storage scoped to the originating tenant.
- It is never shared with any other tenant.
- It is never sent to external APIs.
- When the final response is generated and returned to the originating user within the tenant boundary, placeholders in the response can be rehydrated to the original values using the reverse map.
- The reverse map is deleted when the matter reaches its retention limit (see [[safety-client-data-retention-mena-rules]]).

## Opt-out mechanism

eFirm matters can opt out of PII redaction on a per-matter basis when:
- The matter requires real identifiers for conflict-checking purposes.
- The lawyer needs real names in the AI response for drafting a document where names are required.
- Substance review of a document requires the original identifying context.

**Opt-out process**:
1. Supervising lawyer (or firm admin) toggles the per-matter opt-out flag in the matter dashboard.
2. The opt-out action is logged with user ID, matter ID, timestamp, and stated reason.
3. The opt-out can be reversed at any time; re-enabling redaction applies to subsequent operations.

The opt-out does **not** authorize sending unredacted data to external AI providers without appropriate DPA and confidentiality controls — the opt-out only removes the automatic pre-send redaction step; underlying contractual safeguards with the AI vendor remain required.

## Regulatory alignment

| Regulation | Relevant principle | How redaction satisfies it |
|-----------|-------------------|---------------------------|
| GDPR Art. 5(1)(c) — data minimization | Collect/process only what is necessary | Sending pseudonymized queries to LLM minimizes personal data processed by the vendor |
| GDPR Art. 25 — data protection by design | Technical measures from design stage | Redaction is default-on, not an afterthought |
| KSA PDPL Art. 9 — accuracy and minimization | Minimize personal data in processing | Pseudonymization reduces exposure |
| UAE PDPL Art. 4 — data protection principles | Security and minimization | Technical safeguard against vendor exposure |
| ABA Rule 1.6 / bar analogs | Confidentiality of client information | Prevents client identifiers reaching AI vendor without adequate controls |

## Common mistakes

- **Redacting too little**: forgetting partial identifiers (last 4 of SSN, partial email domain, partial address) that could allow re-identification.
- **Redacting too much**: removing entity names that are necessary for the legal analysis (public companies, government bodies, courts).
- **Losing role context**: replacing all names with generic `[PERSON_N]` without preserving the relational role (claimant vs defendant) — this makes the legal analysis less accurate.
- **Forgetting the reverse map**: redacting without maintaining the reverse map means responses come back with placeholders and the user cannot read them.
- **Not logging opt-outs**: opt-out actions without logging create an audit gap.

## Related skills

- [[safety-bar-rule-1-6-confidentiality-ai]] — bar-rules confidentiality obligations for AI tools
- [[safety-client-confidentiality-cross-tenant]] — cross-tenant isolation guarantees
- [[safety-bar-rules-confidentiality]] — confidentiality architecture overview
- [[safety-cross-border-data-transfer-gcc-eu]] — cross-border transfer risk reduction through pseudonymization
- [[safety-attorney-work-product-ai-handling]] — work-product protection and AI tool use
