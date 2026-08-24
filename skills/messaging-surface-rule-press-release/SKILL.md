---
name: messaging-surface-rule-press-release
description: Use when drafting or reviewing a press release for a legal AI assistant — covering product launches, funding announcements, partnership news, or regulatory developments. Defines the structure, quote standards, claim hierarchy, and compliance requirements specific to press releases, which are a high-trust, widely distributed format that must satisfy both the bridge line constraints and the higher journalistic accuracy standards that apply when copy may be reproduced verbatim by media outlets.
license: MIT
metadata: " id: messaging.surface-rule.press-release category: messaging jurisdictions: [__multi__] priority: P2 intent: [messaging, press-release, PR, media, launch-announcement, compliance] related: [messaging-compliance-checker, messaging-hard-rule-preapproved-press-quotes-only, messaging-bridge-line, messaging-allowed-claims-consumer, messaging-allowed-claims-lawyer, messaging-hard-rule-bible-signoff-required] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'messaging'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Messaging — Surface Rule: Press Release

## When this applies

This skill applies to all **press releases and media statements** issued by or on behalf of a legal AI company. Press releases are a high-stakes format: they are distributed to journalists, investors, regulators, and legal professionals simultaneously, they are published verbatim by newswire services, and they are frequently quoted out of context. Any claim in a press release that is inaccurate or non-compliant will be amplified, not contained.

This skill applies to:
- Product launch press releases
- Funding and investment announcements
- Partnership announcements (law firms, bar associations, technology partners)
- Executive appointment announcements
- Awards or recognition announcements
- Regulatory or market development commentary

---

## Behavior — Press Release Accuracy Standard

Press releases are held to a **higher accuracy standard** than general marketing copy. The test for every claim is not just "is this allowed under our messaging rules?" but also "would this claim hold up to fact-checking by a technology or legal journalist?"

Apply the four-pass compliance check via [[messaging-compliance-checker]] plus one additional pass:

**Pass 5 — Journalistic accuracy:** Is every factual claim (metrics, dates, funding amounts, customer numbers, jurisdiction coverage) verifiable against internal records? If not → revise before issuing.

---

## Press Release Structure

### Standard format

```
FOR IMMEDIATE RELEASE [or embargoed date]

[HEADLINE — max 12 words]
[Subheadline — max 20 words, optional]

[City, Date] — [Company name] today announced [what happened, in one sentence].

[Paragraph 1: What it is and why it matters — 3–5 sentences]

[Paragraph 2: Product/feature/funding detail — 3–5 sentences]

[Quote 1: Company spokesperson — 2–3 sentences]

[Paragraph 3: Market context or additional detail]

[Quote 2: Partner/investor/customer — 2–3 sentences, if applicable]

[Boilerplate: About [Company Name] — 3–5 sentences, always the same approved text]

[Legal disclaimer: 1–2 sentences]

###

Media contact: [Name, email, phone]
```

### Headline rules

| Rule | Detail |
|------|--------|
| Accuracy first | Must accurately describe what happened; no aspirational or future-state claims |
| No outcome claims | "Louis Launches to Win Your Legal Cases" — blocked |
| No displacement framing | "AI Startup Launches to Replace Law Firms" — blocked |
| Bridge line consistent | OK: "Louis Launches Legal AI for MENA — Covering Lebanon, UAE, and Saudi Arabia" |

### First paragraph

- State the news factually in the first sentence: what happened, who, when, where
- Do not bury the news; do not start with background
- No marketing superlatives in the first paragraph ("revolutionary", "world's first" — unless independently verifiable)

---

## Quote Standards

All quotes in press releases are subject to [[messaging-hard-rule-preapproved-press-quotes-only]]:

- **Company spokesperson quote**: must be reviewed and approved by the quoted individual before issuance; must not contain claims outside the messaging bible
- **Partner/investor/customer quote**: must have written approval from the quoted individual; must not contain banned claims — even if the person said it voluntarily; edit before use if banned language appears
- **No composite quotes**: do not amalgamate statements from different people or contexts into a single attributed quote

Quotes in press releases are frequently published verbatim by newswires and syndicated media. A banned claim in a quote becomes a public record attributed to a real person — creating defamation and compliance risk simultaneously.

---

## Metrics and Statistics in Press Releases

Any quantitative claim in a press release must:
- Be verifiable against internal data at the time of issuance
- Reference the source or methodology in the boilerplate or a footnote
- Use "approximately", "more than", "as of [date]" qualifiers for estimates
- Not be forward-looking revenue or customer projections unless in a separate "forward-looking statements" section with appropriate disclaimers

**Banned metric language in press releases:**
- Round numbers presented as exact ("1 million users" — unless exactly 1 million)
- Unsubstantiated comparatives ("the most accurate legal AI in the MENA region")
- Industry-size claims without sources ("a $50 billion market" — must cite the source)

---

## Boilerplate Requirements

The company boilerplate (the "About" paragraph) must:
- Be a pre-approved, stable text that does not change between releases without re-approval
- Include the legal disclaimer: "Louis provides legal information and drafting assistance. It is not a provider of legal advice or legal services. Users should consult a qualified lawyer for advice specific to their situation."
- State jurisdictions covered accurately (do not list a jurisdiction not yet launched in)

---

## Distribution and Clearance

Before a press release is distributed:
1. All four compliance-checker passes completed
2. All quotes confirmed in writing by the quoted person
3. All metrics verified against internal records
4. Legal and communications sign-off obtained
5. If the release contains any new claim type → [[messaging-hard-rule-bible-signoff-required]] completed

---

## Related skills

- [[messaging-compliance-checker]]
- [[messaging-hard-rule-preapproved-press-quotes-only]]
- [[messaging-bridge-line]]
- [[messaging-allowed-claims-consumer]]
- [[messaging-allowed-claims-lawyer]]
- [[messaging-hard-rule-bible-signoff-required]]
- [[messaging-outcome-claims-allowed]]
