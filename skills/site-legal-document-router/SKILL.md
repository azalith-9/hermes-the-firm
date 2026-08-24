---
name: site-legal-document-router
description: Use when a site visitor searches for or navigates to a legal document type in the document library. Routes requests to the document library page filtered by document type and/or jurisdiction, allowing users to browse templates, view sample documents, and access AI-assisted drafting for a specific document category (NDA, employment agreement, SHA, lease, etc.) across MENA and other covered jurisdictions.
license: MIT
metadata: " id: site.legal-document-router category: site jurisdictions: [__multi__] priority: P3 intent: [site, routing, document-library, templates, navigation] related: - site-clause-router - site-ai-feature-router - site-feature-router - site-solutions-router source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'site'.
Registered as a flat plugin skill.
-->


# Legal Document Router — Site Navigation

## Purpose

Route visitors who are searching for a specific type of legal document — template, sample, or AI-generated draft — to the document library page for that document type, pre-filtered by jurisdiction where determinable. The document library is the platform's self-serve template repository and primary document-discovery surface.

## Inputs / signals

| Signal type | Examples | Filter applied |
|-------------|---------|----------------|
| Document name | "NDA template", "employment agreement", "shareholders agreement" | `doc_type=[slug]` |
| Document + jurisdiction | "UAE NDA", "KSA employment contract", "Lebanon lease agreement" | `doc_type=[slug]&jurisdiction=[jur]` |
| Document + party type | "freelancer contract", "SaaS agreement", "B2B services contract" | `doc_type=[slug]&context=[context]` |
| Broad category | "contract templates", "corporate documents", "family law forms" | `category=[category]` |
| Direct `/documents` navigation | Landing on `/documents` | Show all, default sort (most popular / recently updated) |

## Logic

```
1. Parse: document name keyword + optional jurisdiction keyword.
2. Match document name against document registry (exact or fuzzy):
   - NDA, confidentiality agreement → nda
   - Employment agreement, employment contract → employment-agreement
   - Shareholders agreement, SHA, JV agreement → shareholders-agreement
   - Lease, tenancy agreement → lease-agreement
   - Service agreement, consultancy agreement → service-agreement
   - ... (full registry maintained separately)
3. Match jurisdiction from query (UAE, KSA, LB, DIFC, ADGM, etc.)
4. Route to: /documents?type=[slug]&jurisdiction=[jur]
5. If no document match: route to /documents (unfiltered) with search bar focused.
```

## Document library page requirements

Each filtered document library page shows:
- Document type name + plain-language description.
- Sample document preview (first page / key sections).
- Jurisdiction variants (e.g., UAE onshore version vs DIFC version vs KSA version).
- Last updated date and jurisdiction law status note (law changes — always verify).
- CTA options: "View template", "Draft with AI", "Download PDF sample".
- Lawyer review badge (if the template has been reviewed by a jurisdiction-specialist lawyer).

## MENA document library priorities

The following document types are high-priority for MENA coverage and should be surfaced prominently:
- **NDA / Confidentiality Agreement**: UAE onshore, DIFC, KSA, Lebanon, Egypt variants.
- **Employment Agreement**: UAE Labour Law (Federal Decree-Law No. 33 of 2021), KSA Labour Law, Lebanese Labour Code.
- **Shareholders Agreement / JV Agreement**: DIFC, ADGM, UAE onshore, KSA.
- **Commercial Lease**: UAE (RERA-governed), KSA, Lebanon.
- **Service Agreement / Consultancy Agreement**: UAE, KSA, DIFC.
- **Loan Agreement**: UAE, KSA, DIFC, ADGM — noting Islamic finance alternatives.
- **Trademark License**: UAE, KSA (noting GCC trademark system).
- **Power of Attorney**: UAE (notarized), KSA (notarized Tawthiq), Lebanon.

## Jurisdictional caveat (mandatory on all document pages)

Every document page must include:
> *This template is for general guidance only. Legal requirements vary by jurisdiction and change over time. Have any document reviewed by a qualified lawyer in the relevant jurisdiction before signing or filing.*

## Related skills

- [[site-clause-router]] — routing for specific clause queries within documents
- [[site-ai-feature-router]] — routing to AI drafting features
- [[site-feature-router]] — general feature-page routing
- [[site-solutions-router]] — persona-based routing to document types relevant to that persona
