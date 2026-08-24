---
name: strategy-customers
description: Use when defining ideal customer profiles, informing product prioritisation, tailoring messaging, or training sales teams on Louis's target buyer segments. Covers four primary MENA ICP tiers — MENA law firms (5–50 lawyers), MENA in-house counsel, MENA solo practitioners, and MENA law students — plus the secondary Western-firms segment. Internal use only.
license: MIT
metadata: " id: strategy.customers category: strategy jurisdictions: [__multi__] priority: P3 intent: [__internal__] related: [strategy-competitors, strategy-markets, strategy-growth-strategy, strategy-messaging-bible, site-use-case-router] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'strategy'.
Registered as a flat plugin skill.
-->


# Strategy — Customer Segments & ICP

## Purpose

This skill defines Louis's ideal customer profiles (ICP) and secondary segments. Use it when making product, pricing, messaging, or channel decisions — every tradeoff should be evaluated against how it serves these segments.

## Primary segments

### Segment 1 — MENA law firms (5–50 lawyers)

**Who they are:** Mid-tier and boutique law firms headquartered in UAE, KSA, Lebanon, Egypt, Qatar, or Kuwait. Typically serve regional corporate clients, government entities, and GCC-deal inbound from international firms.

**Pain points:**
- Associates spend disproportionate time on research and first drafts across multiple civil-law and common-law systems.
- No budget for BigLaw-tier legal AI at $1,500+/seat/month.
- Document work spans Arabic and English; bilingual tools are almost non-existent.
- Fear of AI errors on jurisdiction-specific law (e.g., UAE Federal Decree-Laws, KSA Ministerial Decisions).

**What Louis delivers:**
- MENA-jurisdictional skill library covering UAE (federal + DIFC/ADGM), KSA, LB, EG.
- Bilingual drafting and review.
- Transparent skill routing so supervising partners can see exactly what the AI did.
- Affordable firm-tier pricing designed for sub-50 seat teams.

**Decision maker:** Managing partner or COO; champion is often a senior associate or IT lead.

---

### Segment 2 — MENA in-house counsel (regional GCs at large UAE/KSA enterprises)

**Who they are:** Legal departments at large GCC enterprises — sovereign wealth fund portfolio companies, telecoms, banks, real-estate groups, and government-adjacent entities. Often one GC + 2–5 lawyers supporting hundreds of internal clients.

**Pain points:**
- Volume of contracts (NDAs, vendor agreements, employment contracts) vastly outpaces legal headcount.
- External counsel spend is under pressure; need to do more in-house.
- Compliance with UAE Corporate Governance Code, KSA Vision 2030 regulatory wave, and PDPL/data-privacy frameworks creates new research burden.

**What Louis delivers:**
- High-volume contract review with risk flagging (saves review time per document).
- Regulatory compliance research across GCC-specific frameworks.
- Integration into existing matter-management and CLM workflows.
- Arabic-controlled-language documents (required for KSA government contracts).

**Decision maker:** GC or CLO; procurement involves IT security and data-governance teams. Expect a full vendor-security questionnaire — see [[template-vendor-security-questionnaire-responses]].

---

### Segment 3 — MENA solo practitioners (Arabic-first)

**Who they are:** Individual lawyers practising across MENA, often in local courts with Arabic as the primary working language. High volume, low margin; any time savings directly translate to income or capacity.

**Pain points:**
- Drafting from scratch for every client is the norm; no associate leverage.
- Arabic legal AI tools barely exist; Google Translate is the current state.
- Fear of licensing / bar-rule issues with AI use.

**What Louis delivers:**
- Arabic-first UI and drafting.
- Free tier with enough value to deliver ROI on day one (EOSG calculator, deadline calculator, first-draft NDA).
- Clear bar-rule guidance baked into outputs so the practitioner knows what to review.

**Acquisition:** PLG (Product-Led Growth) — discover via Google/App Store, free tools, bar-association referral.

---

### Segment 4 — MENA law students

**Who they are:** Students at law faculties across UAE, KSA, Lebanon, Egypt, Jordan. Future practitioners and in-house counsel. High social media influence; strong word-of-mouth.

**Pain points:**
- Limited access to MENA legal databases (expensive or fragmented).
- Moot court prep and research are time-consuming.
- English-only tools disadvantage Arabic-native students.

**What Louis delivers:**
- Free-tier access to research tools and the Justinian legal education module.
- MENA legal research without a $2,000/year database subscription.
- Builds habits early; converts to paid on job placement.

**Acquisition:** University partnerships (KSA + UAE + Lebanon); student pricing tier.

---

## Secondary segment — Western firms doing MENA deals

**Who they are:** London, Paris, New York, and Dubai magic-circle / US-law-firm practitioners handling MENA inbound M&A, project finance, or sovereign debt. They have Harvey or CoCounsel for their home jurisdiction; they need MENA-specific cover.

**What Louis delivers:** MENA-jurisdiction add-on layer — comparative law analysis, DIFC/ADGM precedent search, Arabic document translation/review, KSA regulatory compliance check.

**Go-to-market:** Partnership with international firms' BD functions; white-label option for MENA desk.

## Segment prioritisation

For product investment decisions, prioritise in order:
1. MENA mid-tier law firms (highest willingness to pay + skill library leverage)
2. MENA in-house counsel (high ACV if enterprise deals close)
3. MENA solo practitioners (volume PLG; low ACV but critical for market share)
4. Law students (future pipeline; keep free tier viable)
5. Western firms (opportunistic; high ACV but long sales cycle)

## Related skills

- [[strategy-competitors]]
- [[strategy-markets]]
- [[strategy-growth-strategy]]
- [[strategy-messaging-bible]]
- [[site-use-case-router]]
- [[template-vendor-security-questionnaire-responses]]
