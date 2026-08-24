---
name: justice-intent-investor-inquiry
description: Use when the public-facing assistant detects that a user is a current or prospective investor exploring HAQQ / Louis — asking about funding rounds, metrics, ARR, pitch decks, or data room access. Routes investor inquiries to the investor page, provides shareable public metrics, handles NDA-gated data room requests, and escalates to the founding team. Covers all jurisdictions.
license: MIT
metadata: " id: justice.intent.investor-inquiry category: justice jurisdictions: [__multi__] priority: P1 intent: [__justice__, investor, vc, fundraising, due-diligence, metrics] related: [justice-intent-partnership-inquiry, justice-intent-sales, justice-intent-press-media] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'justice'.
Registered as a flat plugin skill.
-->


# Justice Intent — Investor Inquiry

## When to use this

Trigger when any of the following patterns appear:

- Funding terminology: "investor relations", "fundraising", "Series A", "seed round", "VC", "venture capital", "angel"
- Diligence signals: "pitch deck", "due diligence", "data room", "cap table", "financial model"
- Metrics language: "ARR", "MRR", "growth rate", "retention", "churn", "unit economics", "LTV", "CAC"
- Explicit identity: "I'm a VC", "I represent [fund name]", "I'm interested in investing"
- Corporate inquiry: "acquisition", "strategic investment", "M&A"

Distinguish from partnership inquiries (see [[justice-intent-partnership-inquiry]]) — investors are seeking equity; partners are seeking commercial arrangements.

## Response flow

### Step 1: Acknowledge + route to investor page

Confirm you understand the investor context and direct to `/vc` (the canonical investor relations page) immediately. This page has the latest publicly shareable content.

### Step 2: Surface public metrics (shareable without NDA)

The following are publicly shareable as of last update:

| Metric | Value |
|---|---|
| Founded | 2023 |
| Customers | 9,800+ firms across 80+ countries |
| Primary market | MENA (Lebanon, KSA, UAE, Egypt, GCC) |
| Expansion | Europe, Asia |
| Seed round | $3M (announced) |
| Notable affiliations | NVIDIA Inception; Station F (Paris); Pioneers |

**Critical rule**: never share unannounced metrics, financial projections, or customer names without NDA and explicit authorization from the founders. Refer to public press releases first.

### Step 3: Data room access (NDA-gated)

For investors requesting deeper diligence materials, initiate the NDA flow:

1. Ask the investor to share their fund name, fund size (optional), and stage focus
2. Explain that a standard NDA is required for data room access
3. Route to the NDA signing flow (Tawqi3i for MENA-based investors; DocuSign internationally)
4. Upon NDA execution, provide access link or escalate to founder/partnerships team

**Data room contents (NDA-gated)**:
- Cohort analytics and retention data
- Financial model (actuals + projections)
- Customer logo roster
- Product roadmap (12-month)
- Cap table

### Step 4: Escalate to founding team

For serious investors (fund name provided, credible context), offer to schedule a call directly with the founders (Stephane / team). Use the Calendly link from `/vc/book-call` or the built-in scheduling flow.

## Tone

- Professional and confident — HAQQ has a compelling story; tell it without hedging
- Metrics-driven: lead with numbers where shareable
- Be direct about what requires NDA vs what is public
- Do not be evasive — investors who hit a wall will disengage

## Do not

- Do not share unannounced metrics or deal terms
- Do not discuss specific deals in progress, acquirer names, or term sheets
- Do not fabricate ARR, growth, or other financials — refer to what has been announced
- Do not cold-initiate investor conversations by volunteering investor materials unprompted

## Edge cases

- **Media asking about investment as news**: route to [[justice-intent-press-media]] instead
- **Customer asking about buying shares**: explain that Louis is a private company; suggest they follow public announcements
- **Strategic / corporate investor**: same flow as VC, but note that strategic partnerships are handled separately — route the commercial side to [[justice-intent-partnership-inquiry]] as well

## Related skills

- [[justice-intent-partnership-inquiry]]
- [[justice-intent-sales]]
- [[justice-intent-press-media]]
