---
name: outreach-haqq-ai-viz
description: Use when the legal AI product team needs to create data visualisations, infographics, or visual explainers to support marketing, press, and outreach materials. Converts legal data, jurisdiction comparisons, and product metrics into shareable visual formats for social media, pitch decks, and publication placements. Triggers on requests for charts, infographics, or visual content for outreach use.
license: MIT
metadata: " id: outreach.haqq-ai-viz category: outreach intent: ['__outreach__', 'visualization', 'infographic', 'data', 'visual-content'] related: - outreach-backlink-pr-campaign - outreach-blog-preview-renderer - outreach-growth-agent-runner - outreach-video-asset-library priority: P3 source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'outreach'.
Namespaced as louis-<category>-<skill> on registration.
-->


# HAQQ AI Viz — Legal Data Visualisation for Outreach

Visual content dramatically outperforms text-only content in social sharing and press pickup. For a legal AI product, data visualisations serve a second purpose: they demonstrate analytical capability and build credibility with a professional audience that values rigour. This skill governs how to design, produce, and deploy visual content for outreach.

## Purpose

Produce visual outreach assets that:
- Communicate legal insights clearly to a professional audience
- Are accurate enough to withstand scrutiny from lawyers and journalists
- Are visually distinctive enough to be shared on social media
- Serve double duty as linkable assets for PR campaigns

## Inputs

| Input | Why it matters | Default |
|---|---|---|
| Data or legal insight to visualise | The underlying content — must be accurate | Skills library, jurisdiction research |
| Target format | Social card, infographic, chart, interactive, slide | Social card (1080x1080) |
| Target audience | Lawyer vs GC vs investor vs general public | MENA legal professional |
| Brand constraints | Colours, fonts, logo usage | Product brand guidelines |
| Distribution channel | LinkedIn, Twitter/X, press kit, pitch deck | LinkedIn primary |

## Visual format options

### 1. Jurisdiction comparison card

A visually formatted version of [[output-table-of-comparisons]], designed for social sharing:

```
[Header: "Non-Compete Rules: UAE vs KSA vs Lebanon vs DIFC"]
[4-column mini-table with colour-coded cells]
[Source citation at bottom: "Sources: FDL 33/2021; Saudi Labor Law; LB Labor Code; DIFC Law 4/2021"]
[Product logo]
```

Design principles: high contrast, max 4 columns, max 6 rows, no text smaller than 14pt in rendered size.

### 2. Legal rule explainer card

A single-insight visual:

```
[Bold headline: "UAE Non-Compete: 4 Tests"]
[Simple iconographic list:]
  📍 Proportionate scope
  🗺 Limited geography
  ⏱ Max 2 years
  🛡 Legitimate business interest
[Source: UAE FDL 33/2021 art 10]
[CTA: "Full analysis → [link]"]
```

### 3. Data chart

When product data or research data is available:
- Bar chart: "Non-compete clause validity rate by jurisdiction" (if survey data exists)
- Line chart: "Growth in MENA cross-border disputes" (if public data available)
- Funnel: "How a MENA contract review flows through AI"

**Critical:** only use real data in charts. Do not fabricate statistics or use placeholder numbers. If no data is available, use a conceptual diagram (flowchart, matrix) instead.

### 4. Process flow / flowchart

For product explainers:
```
User uploads contract → AI scans clauses → Risk flags generated → Lawyer reviews → Final advice
```

Flows are safe to create without data and are highly shareable as product marketing.

### 5. Quote card

A pull quote from a team member, advisor, or (with permission) a customer:
```
[Large quote text]
[Attribution: Name, Title]
[Context: "On the launch of [feature]"]
[Product logo]
```

## Accuracy rules for legal viz

- Every legal rule shown in a visual must be accurate and sourced.
- Source citation must appear on the visual (even if small) — not just in the caption.
- Do not use a jurisdiction in a comparison visual if you cannot verify the rule for that jurisdiction.
- Flag visualisations as "for informational purposes only" where they make legal claims.

## Production approach

For simple visuals (comparison cards, quote cards): produce as structured Markdown/HTML that can be rendered by the product's design system or pasted into Canva/Figma.

For complex infographics: produce a detailed brief (data, labels, layout description) for a designer or design tool to execute.

## Distribution checklist

Before publishing:
- [ ] Legal accuracy reviewed
- [ ] Source citation included on the visual
- [ ] "Not legal advice" disclaimer where applicable
- [ ] Correct image dimensions for platform (LinkedIn: 1200x627; Twitter: 1200x675; Instagram: 1080x1080)
- [ ] Alt text prepared for accessibility
- [ ] Caption/post copy prepared

## Related skills

- [[outreach-backlink-pr-campaign]]
- [[outreach-blog-preview-renderer]]
- [[outreach-growth-agent-runner]]
- [[outreach-video-asset-library]]
- [[output-table-of-comparisons]]
