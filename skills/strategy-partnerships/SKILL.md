---
name: strategy-partnerships
description: Use when planning or executing Louis's partnership strategy across integration, distribution, and data-partnership classes. Covers Microsoft, Google, DocuSign, Tawqi3i integrations; bar-association and university distribution channels in KSA, UAE, and Lebanon; and legal-database data partnerships for MENA jurisdiction corpora. Internal use only.
license: MIT
metadata: " id: strategy.partnerships category: strategy jurisdictions: [__multi__] priority: P3 intent: [__internal__] related: [strategy-growth-strategy, strategy-customers, strategy-markets, strategy-fundraising, tool-e-signature-orchestrator] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'strategy'.
Registered as a flat plugin skill.
-->


# Strategy — Partnerships

## Purpose

This skill defines Louis's three partnership classes, priority targets within each, and the sequencing logic for outreach. Use it when planning BD conversations, structuring a partnership agreement, or evaluating an inbound partnership inquiry.

## Partnership taxonomy

### Class 1 — Integration partners

Integration partners make Louis more powerful by connecting it to tools lawyers already use.

| Partner | Integration value | Priority |
|---|---|---|
| **Microsoft 365 / Teams** | Word add-in for in-document drafting + review; Teams bot for matter queries; Outlook integration for email drafting | High — enterprise firms run on M365 |
| **Google Workspace** | Docs add-on; Google Calendar for deadline management | Medium — more common in startups and younger firms |
| **DocuSign** | E-signature orchestration after draft completion; completion webhook to update matter status | High — dominant e-signature in MENA cross-border deals |
| **Tawqi3i (KSA)** | National e-signature for KSA-governed documents; required for government-facing agreements | Critical for KSA market entry |
| **UAE Pass** | PKI-based digital identity + signature for UAE government-facing documents | Critical for UAE government-sector clients |
| **DIFC / ADGM court portals** | Direct case-search integration for litigation workflows | Medium — reduces friction for court research |

**Partnership model for integrations:** API-level connector + listed in partner directory. Prefer marketplace listings (Microsoft AppSource, Google Workspace Marketplace) for self-serve discovery.

---

### Class 2 — Distribution partners

Distribution partners control access to Louis's target ICP and can deliver warm introductions at scale.

| Partner | Reach | Model |
|---|---|---|
| **KSA bar association (Saudi Bar Association)** | Largest MENA bar body; tens of thousands of licensed lawyers | Endorsed-partner status; CPD credit for Louis training; bulk-license program |
| **UAE bars (Abu Dhabi + Dubai)** | UAE federal and emirate-level practice coverage | Co-branded tool kit; conference sponsorships; member discount |
| **Lebanon bar (Beirut + Tripoli)** | Lebanese Bar Association has strong institutional influence | Student-chapter program; clinic licensing |
| **King Abdulaziz University Law Faculty (KSA)** | Large law faculty; strong industry placement | Free student access; clinic licensing; faculty research partnership |
| **American University of Beirut (AUB) Law** | Most internationally connected Lebanese law school | Research partnership; moot court sponsorship |
| **American University of Sharjah / UAE University** | UAE-based feeder for MENA law firms | Student tier; co-branded content |
| **MENA legal recruitment firms** | Reach hiring lawyers at the career-change moment | Referral program; sponsored content |

**Lead with universities (KSA + UAE + Lebanon).** Student adoption is the lowest-cost acquisition channel with the highest lifetime value — students graduate, join firms, and become internal champions.

---

### Class 3 — Data partners

Data partners provide MENA-specific legal corpora that no competitor can easily replicate.

| Partner | Data value | Notes |
|---|---|---|
| **GCC legal database providers** (e.g., Gulf Legal DB, LexisNexis MENA, MenaRA) | Case law, legislation, ministry decisions in Arabic + English | License for training data or retrieval-augmented generation |
| **UAE Ministry of Justice** | Official federal legislation, regulations, ministerial circulars | Public domain; but structured machine-readable formats require partnership |
| **KSA Nazaha / Bawabah Al Mohakami** | KSA court decisions (partially public) | Arabic court decisions are the hardest MENA corpus to obtain |
| **DIFC and ADGM court registries** | Common-law judgments; well-structured and publicly available | Direct scrape + API possible; partnership strengthens institutional credibility |
| **Lebanese Official Gazette (Journal Officiel)** | Lebanese legislation, decrees, regulations | Partially digitised; a partnership accelerates structured access |

**Strategic priority:** KSA Arabic court decisions and KSA ministerial decisions are the single hardest and most valuable corpus to obtain. A data partnership here creates a durable competitive moat.

## Partnership sequencing

**Q1–Q2 (current):** DocuSign integration (quick win; high user-visible value). UAE/KSA university pilots.

**Q3–Q4:** Tawqi3i and UAE Pass integrations (required for government-sector sales). Saudi Bar Association endorsement outreach.

**Year 2:** Microsoft 365 add-in (required for enterprise firm sales). KSA legal database data-licensing agreement.

## Partnership agreement templates

For integration partners: use a standard API-access agreement with data-processing addendum. Ensure:
- No training on tenant data by the integration partner
- Audit logging for all data passed to the partner
- Termination and data-purge provisions

For distribution partners: use a referral / reseller agreement with:
- Revenue share or flat referral fee per converted account
- No exclusivity (maintain ability to partner with all bar associations)
- Co-marketing obligations defined (webinar, co-branded content)

For data partners: use a data-licensing agreement with:
- Clear permitted-use scope (retrieval-augmented generation; no model training without explicit re-grant)
- Attribution requirements if data is surfaced in outputs
- Audit rights

## Related skills

- [[strategy-growth-strategy]]
- [[strategy-customers]]
- [[strategy-markets]]
- [[strategy-fundraising]]
- [[tool-e-signature-orchestrator]]
