---
name: tool-hubspot-crm-context
description: Use when a legal professional or business-development user needs to pull deal context from HubSpot CRM into an active Louis chat — including deal stage, counterparty contacts, and deal properties — to inform contract drafting or negotiation preparation. Triggers when the user mentions a deal name, counterparty, or asks to "pull from CRM" during a commercial or sales-side workflow.
license: MIT
metadata: " id: tool.HubSpot-CRM-context category: tool jurisdictions: [__multi__] priority: P2 intent: [crm-context, deal-data, sales-workflow, counterparty-info] related: [tool-rag-firm-knowledge, tool-sec-edgar-us, tool-uae-ded, tool-ksa-moc, tool-lb-commercial-register] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'tool'.
Namespaced as louis-<category>-<skill> on registration.
-->


# HubSpot CRM Context

## What it does

This tool pulls live deal and contact data from HubSpot CRM into the active Louis chat session. It enables legal professionals and business-development users to draft contracts, prepare for negotiations, or run counterparty checks with CRM context already loaded — no manual copy-paste of deal terms or counterparty names.

Typical use case: the user is about to draft an MSA or NDA and says "pull the HubSpot deal for Acme Corp." Louis retrieves the current deal stage, contacts, company properties, and any relevant deal notes, then uses them as pre-filled inputs for the drafting or review skill.

## Setup / auth

| Parameter | Description | Required |
|-----------|-------------|----------|
| `hubspotApiKey` | Private app token (scopes: `crm.objects.deals.read`, `crm.objects.contacts.read`, `crm.objects.companies.read`) | Yes |
| `portalId` | HubSpot portal / account ID | Yes |
| `dealId` | HubSpot deal ID (if known) | No — can search by name |
| `companyName` | Company name for deal search | Conditional |

**Auth best practice**: use HubSpot Private Apps (not OAuth) for server-to-server integration. Scope the token to read-only CRM objects. Do not grant write access unless the integration explicitly needs to update deal stages.

## Capabilities

### Deal lookup
```
Input:  { query: "Acme Corp MSA 2025" }
Output: {
  dealId, dealName, stage, amount, closeDate,
  companies: [{ name, domain, industry }],
  contacts: [{ firstName, lastName, email, role }],
  properties: { dealType, jurisdiction, governingLaw, ... }
}
```

### Contact fetch
```
Input:  { contactId: "12345" }
Output: { name, email, phone, title, company, recentActivity }
```

### Company enrichment
```
Input:  { companyId: "67890" }
Output: { name, domain, country, industry, revenue, employees, website }
```

### Deal notes and activity log
Retrieve recent notes, calls, and emails associated with a deal to surface negotiation history.

## Usage patterns

**Pattern 1 — Pre-fill NDA draft**
```
User: "Draft an NDA for the Acme deal."
→ Pull HubSpot deal "Acme" → extract company name, counterparty contact, deal jurisdiction
→ Pre-fill draft-nda-mutual with those values
→ User reviews and confirms before generation
```

**Pattern 2 — Negotiation prep**
```
User: "Prepare talking points for the Acme MSA negotiation tomorrow."
→ Pull deal stage, last notes, open issues from HubSpot
→ Combine with firm KB precedent on MSA positions
→ Output structured negotiation brief
```

**Pattern 3 — Counterparty due diligence trigger**
```
User: "Check the counterparty on the Acme deal."
→ Pull company domain + country from HubSpot
→ Route to appropriate registry tool (tool-uae-ded, tool-ksa-moc, etc.)
→ Return combined CRM + registry profile
```

**Pattern 4 — Update deal stage after signing**
```
User: "Mark the Acme MSA as Closed Won."
→ Requires write scope; confirm with user before calling HubSpot write API
→ Update deal stage in HubSpot
→ Confirm update + log in session
```

## Data mapping: HubSpot properties to legal context

| HubSpot Field | Legal Use |
|---------------|-----------|
| `dealname` | Document title / recitals |
| `closedate` | Agreement effective date or signature deadline |
| `amount` | Contract value / consideration |
| `deal_currency_code` | Currency clause |
| `hubspot_owner_id` | Responsible attorney / BD contact |
| `companies[0].country` | Jurisdiction flag → route to correct registry tool |
| Custom: `governing_law` | Governing law clause pre-fill |
| Custom: `contract_type` | Route to correct drafting skill |

If the tenant uses custom HubSpot properties for legal context (governing law, contract type, etc.), configure them in the tool's property mapping.

## Permissions & safety

- **Read-only by default.** Write operations (update deal stage, add notes) require explicit user instruction and a write-scoped token.
- **No storage** of CRM data beyond the current session. Do not persist contact details or deal terms in the firm KB without user consent.
- **PII awareness**: contact emails, deal amounts, and company revenue are sensitive. Apply data-handling policies consistent with GDPR (EU), PDPL (KSA), and UAE Personal Data Protection Law.
- **Tenant isolation**: each HubSpot portal is isolated per tenant. Cross-portal access is not permitted.

## Failure modes

| Failure | Symptom | Resolution |
|---------|---------|------------|
| Invalid API key | 401 unauthorized | Check token in tenant settings |
| Deal not found | Empty search result | Try alternate search terms; confirm deal exists in HubSpot |
| Rate limit | 429 response | Retry after 10 seconds; HubSpot limits at 100 requests/10 seconds |
| Missing custom properties | `null` on expected legal fields | Inform user; ask them to fill in manually |
| Outdated deal data | Stale contacts or stage | Flag that CRM data is as of fetch time; user should verify |

## Related skills

- [[tool-rag-firm-knowledge]] — firm's own precedents for the deal type
- [[tool-sec-edgar-us]] — public filing lookup for US-listed counterparties
- [[tool-uae-ded]] — UAE trade license lookup for UAE counterparties
- [[tool-ksa-moc]] — KSA commercial registry for Saudi counterparties
- [[tool-lb-commercial-register]] — Lebanon commercial register
