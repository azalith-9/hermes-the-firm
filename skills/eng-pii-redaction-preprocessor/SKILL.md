---
name: eng-pii-redaction-preprocessor
description: Use when building or configuring the PII redaction layer that sanitizes user-submitted text before it is sent to an LLM or stored in a database. Covers entity detection patterns, redaction strategies, audit logging, and reconstruction for legal AI pipelines where client-confidential data must never leak into training or third-party model calls.
license: MIT
metadata: " id: eng.PII-redaction-preprocessor category: eng jurisdictions: [__multi__] priority: P2 intent: [__eng__, pii, redaction, privacy, preprocessing] related: [eng-tenant-isolation-row-level-security, eng-supabase-edge-functions-patterns, eng-rag-chunking-rules-legal-docs, safety-client-confidentiality-cross-tenant] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'eng'.
Namespaced as louis-<category>-<skill> on registration.
-->


# PII Redaction Preprocessor

## What it does

The PII redaction preprocessor is a text-transformation pipeline stage that detects and removes or masks personally identifiable information (PII) from user-submitted legal content before that content is forwarded to an external LLM API call, stored in a search index, or written to a shared database table. In a multi-tenant legal AI product this is a critical safety control: a client of Firm A must never have their counterpart names, passport numbers, or contract figures embedded in a vector store that another tenant can retrieve.

The preprocessor runs synchronously in the request path (≤ 50 ms budget) or, for large document uploads, as an async pre-indexing job.

## Setup / auth

No external auth required. The preprocessor is a pure-text pipeline component that can be deployed as:

- A Supabase Edge Function (`functions/redact-pii/index.ts`) invoked before any call to the LLM or embedding API.
- A middleware layer in the Express/Hono backend, mounted before the chat-route handler.
- A standalone Node.js worker for batch document ingestion.

Dependencies: `@presidio/presidio-js` (if using Microsoft Presidio via REST), or a custom regex+NER approach. For MENA content, a regex-first approach with Arabic-aware patterns is more reliable than English-trained NER models.

## Capabilities

### Entity types to detect and redact

| Category | Examples | Redaction token |
|---|---|---|
| Full name | "Ahmad Al-Rashidi", "Marie Dupont" | `[PERSON]` |
| National ID / Iqama / Emirates ID | 784-XXXX-XXXXXXX-X | `[NATIONAL_ID]` |
| Passport number | any 7–9 char alphanumeric | `[PASSPORT]` |
| Phone number | +961-X-XXX-XXXX, +971-5X-XXXXXXX | `[PHONE]` |
| Email address | RFC 5321 pattern | `[EMAIL]` |
| IBAN / bank account | LB62XXXX… | `[FINANCIAL_ACCOUNT]` |
| Company registration number | Lebanon: ش.م.م XXXXXX, UAE: CN-XXXXXXXX | `[COMPANY_REG]` |
| Address / property number | plot numbers, parcel IDs | `[ADDRESS]` |
| Date of birth | explicit DOB patterns | `[DOB]` |
| Contract monetary amounts | optional — flag rather than redact | `[AMOUNT]` |

### Redaction modes

- **Replace** (default): substitute with typed token (`[PERSON]`). Preserves sentence structure for downstream LLM comprehension.
- **Mask**: overwrite with `█` characters of equal length. Used for rendered PDFs.
- **Hash**: replace with a consistent HMAC-SHA256 keyed hash. Allows cross-document entity resolution without revealing the value. Use for analytics pipelines where re-identification must remain possible under a controlled key.
- **Delete**: remove entity and surrounding whitespace. Use only when the surrounding sentence still makes sense.

## Usage patterns

### Pattern 1 — Inline chat message preprocessing

```typescript
// supabase/functions/chat/index.ts (simplified)
import { redactPII } from "../_shared/pii-redactor.ts";

const userMessage = req.body.message;
const { redacted, auditLog } = redactPII(userMessage, {
  mode: "replace",
  locale: detectLocale(userMessage), // "ar" | "en" | "fr"
});

// Forward redacted text to LLM; store auditLog for compliance
const llmResponse = await callClaude(redacted);
```

### Pattern 2 — Document ingestion before embedding

```typescript
// Before chunking and embedding a uploaded contract PDF
const rawText = await extractTextFromPDF(file);
const { redacted, auditLog } = redactPII(rawText, { mode: "hash", hashKey: TENANT_HASH_KEY });
const chunks = chunkLegalDocument(redacted); // see eng-rag-chunking-rules-legal-docs
await embedAndStore(chunks, tenantId);
```

### Pattern 3 — Audit trail

Every redaction run should emit a structured log entry:

```json
{
  "runId": "uuid",
  "tenantId": "t_xxx",
  "userId": "u_xxx",
  "entitiesFound": [
    { "type": "PERSON", "count": 3, "positions": [[12, 24], [88, 102], [211, 225]] },
    { "type": "PHONE", "count": 1, "positions": [[400, 413]] }
  ],
  "mode": "replace",
  "inputLengthChars": 4820,
  "processedAt": "2026-05-14T09:00:00Z"
}
```

Store in `pii_audit_log` table (append-only, tenant-scoped, RLS-protected).

## Permissions & safety

- The redactor must run **before** any call to the external LLM API. Never pass raw user text containing PII to the agent/GPT/Gemini without this gate.
- The audit log must be stored even when redaction finds zero entities (zero-finding logs help detect evasion).
- Hash mode keys must be per-tenant, stored in Supabase Vault (not in code or `.env` files).
- For bilingual AR/EN documents, run two passes: one with Arabic-aware patterns first, then English.
- GDPR / PDPL (UAE Federal Decree-Law No. 45 of 2021) and Lebanon Law 81 on electronic transactions all require documented evidence that PII is handled appropriately. The audit log is that evidence.

## Failure modes

| Failure | Impact | Mitigation |
|---|---|---|
| False negative (PII not detected) | PII sent to external model | Ensemble detection: regex + NER; review audit samples weekly |
| False positive (non-PII redacted) | LLM loses useful context | Use typed tokens so LLM infers entity type; tune regex thresholds |
| Performance degradation | Chat latency spikes | Run async for large docs; timeout at 200 ms and log |
| Hash key rotation | Re-identification broken | Version hash keys; store version alongside hash |
| Arabic diacritic variants | Names missed | Normalize Unicode before pattern matching |

## Related skills

- [[eng-tenant-isolation-row-level-security]] — RLS ensures redacted data is tenant-scoped in the database
- [[eng-rag-chunking-rules-legal-docs]] — chunking runs after redaction in the document pipeline
- [[eng-supabase-edge-functions-patterns]] — deployment pattern for the redactor as an Edge Function
- [[safety-client-confidentiality-cross-tenant]] — policy that mandates this technical control
