---
name: site-clause-router
description: Use when a site visitor lands on /clauses or searches for a specific contract clause by name (e.g., "force majeure clause", "limitation of liability clause", "governing law clause"). Routes the user to the clause library with the appropriate filter pre-applied. Applies to all jurisdictions; the clause library may be further filtered by jurisdiction and document type.
license: MIT
metadata: " id: site.clause-router category: site jurisdictions: [__multi__] priority: P3 intent: [site, routing, clause-library, contract-clauses, navigation] related: - site-legal-document-router - site-ai-feature-router - site-feature-router - site-solutions-router source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'site'.
Registered as a flat plugin skill.
-->


# Clause Router — Site Navigation

## Purpose

Route users who are searching for specific contract clauses to the platform's clause library (`/clauses`) with the correct filter pre-applied. The clause library is a high-value entry point for lawyers and legal teams who want to browse, compare, or copy standard clauses for a given document type or jurisdiction.

## Inputs / signals

| Signal | Examples | Applied filter |
|--------|---------|----------------|
| Direct `/clauses` navigation | Landing on `/clauses` | Show all clauses, default sort |
| Named clause search | "force majeure clause", "material adverse change", "entire agreement", "non-compete clause" | Filter: clause name or type |
| Clause by document type | "NDA clauses", "employment contract clauses", "SPA representations" | Filter: document type |
| Clause by jurisdiction | "UAE governing law clause", "DIFC arbitration clause", "KSA force majeure" | Filter: jurisdiction |
| Clause by practice area | "M&A clauses", "employment clauses", "IP assignment clause" | Filter: practice area |

## Logic

```
1. Detect entry point: direct navigation to /clauses OR search query containing clause-related terms.
2. Parse filters from query:
   - Clause type / name keyword
   - Document type keyword
   - Jurisdiction keyword
   - Practice area keyword
3. Route to: /clauses?type=[type]&jurisdiction=[jur]&doc=[doc-type]
4. If no filters parseable: route to /clauses (unfiltered) with suggested top-level filter categories.
5. Within the clause library, each clause has:
   - Clause name + plain-language summary
   - Standard text (jurisdiction-tagged)
   - Alternative variants (negotiation-friendly vs. standard vs. restrictive)
   - Practice notes (when to use this variant; MENA-specific traps)
   - "Copy clause" + "Try in Louis" CTAs
```

## Key clause categories (MENA-relevant)

The clause library should prominently surface clauses that are especially important or contentious in MENA commercial practice:
- **Governing law and jurisdiction** — onshore UAE vs DIFC vs ADGM vs DIAC arbitration; KSA venue; Lebanon arbitration.
- **Force majeure** — civil-code jurisdictions (UAE, LB, KSA) have force majeure built into the civil code; common-law jurisdictions (DIFC, ADGM) require an explicit clause.
- **Limitation of liability / exclusion clauses** — enforceability varies significantly between civil-law (harder to exclude consequential loss) and common-law (can exclude if clearly drafted).
- **Liquidated damages / penalty clauses** — distinction between common-law (LD must be a genuine pre-estimate of loss) and civil-law (penalty clause allowed but court may adjust); KSA courts have latitude to reduce disproportionate penalties.
- **Non-compete / non-solicitation** — enforceability varies widely; UAE restricts enforcement in many contexts; Lebanese courts may not enforce unreasonably broad restrictions.
- **Entire agreement / merger clauses** — important in civil-law jurisdictions where pre-contractual representations may have legal effect even without a clause.

## Output

Route to `/clauses?[filters]`. If the user is in the AI chat (not the public site), offer to draft or explain the specific clause using the drafting skills.

## Related skills

- [[site-legal-document-router]] — document-library routing (broader than clause-level)
- [[site-ai-feature-router]] — routing to specific AI feature pages
- [[site-feature-router]] — general feature-page routing
- [[site-solutions-router]] — persona-based solution routing
