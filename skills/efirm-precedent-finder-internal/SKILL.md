---
name: efirm-precedent-finder-internal
description: Use when a lawyer needs to locate an internal firm precedent — a previously used and approved document or clause — to use as the starting point for a new draft. The skill searches the firm's knowledge base by document type, jurisdiction, governing law, practice area, and keyword, returning ranked matches with recency, approval status, and a brief description of how each precedent differs. Part of the eFirm firm-management product suite.
license: MIT
metadata: " id: efirm.precedent-finder-internal category: efirm jurisdictions: [__multi__] priority: P2 intent: [precedent, knowledge-management, search, drafting, KM] related: - efirm-knowledge-base-curation - efirm-template-library-firm-branded - efirm-document-versioning-rule - efirm-matter-creation-flow source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'efirm'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Precedent Finder — Internal

## When to use this

Use this skill when:
- A lawyer is starting a draft and wants to know whether the firm has an approved baseline for that document type.
- A partner wants to confirm which version of a standard clause the firm uses in a particular jurisdiction.
- A new associate is researching the firm's approach to a recurring legal issue (e.g., change-of-control provisions in KSA-law agreements).
- A knowledge management partner is conducting a gap analysis to identify document types not yet in the KB.
- AI-assisted drafting needs to retrieve the correct KB baseline before generating or augmenting a draft.

Always search the internal precedent library before starting from scratch or using a generic external template. The firm's KB reflects hard-won negotiating positions, jurisdiction-specific adaptations, and compliance-reviewed language.

## Search dimensions

A precedent search can be run on any combination of the following parameters:

| Parameter | Examples |
|---|---|
| Document type | NDA / SPA / SHA / Employment Agreement / Engagement Letter |
| Practice area | Corporate / Dispute / Employment / IP / Real Estate / Regulatory |
| Jurisdiction(s) | UAE / KSA / DIFC / ADGM / LB / UK / FR / US |
| Governing law | UAE / English / DIFC / KSA / French |
| Language | Arabic / English / Bilingual-AR-EN |
| Matter type | Transaction / Litigation / Advisory / Regulatory |
| Keyword | Free text search on document title, clause summary, or KB description |
| Approved by | Specific partner (useful for finding the partner's preferred formulations) |
| Last reviewed | After [date] (filters for currency; avoids stale precedents) |
| Access tier | Firm-wide / Practice-area / Partner-only |

## Ranking and result display

Results are returned ranked by:
1. **Match precision** (document type + jurisdiction match = highest weight).
2. **Recency** (last-reviewed date — more recent ranked higher).
3. **Usage frequency** (most-used precedents ranked higher — signals firm standard).

For each result, display:

```
PRECEDENT MATCH — [Rank]

Document:        [Title + version]
Type:            [Document type]
Practice:        [Practice area]
Jurisdiction:    [Jurisdiction(s)]
Governing law:   [Law]
Language:        [Language]
Last reviewed:   [Date] by [Partner ID]
Status:          [Active / Under review / Superseded]
Access:          [Firm-wide / Practice / Partner-only]
KB note:         [1–2 sentence description of what makes this precedent notable — 
                  e.g., "Standard SPA for minority acquisitions in KSA; includes 
                  Sharia-compliant governing law and SAGIA approval condition"]
Location:        [DMS path / link]
```

If a result has status **Under review**, surface a warning: "This precedent is currently under review and may not reflect the latest legal requirements. Confirm currency with [Practice Group Partner] before use."

If a result has status **Superseded**, do not return it as a primary result — return it only if requested, with a clear warning and a pointer to the successor document.

## Gap detection

If the search returns no results for a document type + jurisdiction combination, surface a gap notice:

```
PRECEDENT GAP DETECTED

No internal precedent found for:
  Document type:   [Type]
  Jurisdiction:    [Jurisdiction]
  Governing law:   [Law]

Options:
  1. Draft from scratch (use [[efirm-template-library-firm-branded]] if a generic 
     template is available).
  2. Adapt nearest available precedent — closest match: [nearest result].
  3. Request a new precedent be commissioned (notify KM partner).

If you draft this from scratch and the result is reusable, please submit it to 
the Knowledge Base via [[efirm-knowledge-base-curation]] after partner review.
```

## AI-assisted retrieval

When a drafting skill (e.g., [[efirm-template-library-firm-branded]] or [[efirm-engagement-letter-draft]]) invokes the precedent finder:

1. The skill supplies: document type + jurisdiction + governing law.
2. The finder returns the top-ranked Active match.
3. The calling skill uses the returned document as its baseline.
4. The KB version number and "last reviewed" date are recorded in the draft's audit trail so it is clear which baseline was used.

This ensures AI-generated drafts are always rooted in the firm's approved language, not generic output.

## Access control enforcement

The finder enforces KB access tiers:
- A user with practice-area-only access cannot retrieve partner-only precedents.
- The system does not reveal the existence of partner-only documents to unauthorized users.
- Access requests for higher tiers go through the KM partner.

## Maintenance integration

The precedent finder logs every search (anonymized) so the KM partner can:
- Identify high-frequency search queries that return no results (gaps to fill).
- Identify low-search precedents that may be candidates for retirement.
- Monitor whether lawyers are using approved precedents or bypassing the KB.

## Related skills

- [[efirm-knowledge-base-curation]]
- [[efirm-template-library-firm-branded]]
- [[efirm-document-versioning-rule]]
- [[efirm-matter-creation-flow]]
- [[efirm-partner-review-routing]]
