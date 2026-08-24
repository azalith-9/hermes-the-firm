---
name: strategy-llmo-update-for-lovable
description: Use when running the quarterly LLMO (Large Language Model Optimisation) review to assess and improve how Louis appears in AI-generated search results and LLM knowledge bases. Covers Google AI Overviews, ChatGPT, Perplexity, and the agent outputs for legal AI queries; defines the SEO and LLMO tactics — structured data, citation-rich content, owned domains — to surface Louis in "best legal AI for MENA" queries. Internal use only.
license: MIT
metadata: " id: strategy.llmo-update-for-lovable category: strategy jurisdictions: [__multi__] priority: P3 intent: [__internal__] related: [strategy-messaging-bible, strategy-growth-strategy, strategy-competitors, strategy-markets] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'strategy'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Strategy — LLMO (LLM Optimisation) Review for Lovable

## Purpose

LLMO (Large Language Model Optimisation) is the practice of ensuring a product appears accurately and favourably in the outputs of AI systems — Google AI Overviews, ChatGPT, Perplexity, the agent, Gemini — when users ask questions about legal AI tools, MENA legal technology, or related topics.

This skill defines the quarterly review process and the ongoing content tactics that feed it. It is adapted for Louis (formerly the "Lovable" product surface) and covers both the technical and editorial dimensions.

## Why LLMO matters for Louis

An increasing share of legal professionals discover new tools via conversational AI queries rather than traditional Google search. A lawyer asking ChatGPT "what is the best AI for UAE law?" or "best legal AI for Arabic contracts?" will receive a synthesised answer — if Louis is not in that answer, it does not exist for that user. LLMO closes this visibility gap.

## Quarterly review cadence

Run this review every quarter (January, April, July, October):

### Step 1 — Query sampling

Run the following probe queries across Google AI Overview, ChatGPT (GPT-4o), Perplexity, and the agent Sonnet:

| Query category | Example queries |
|---|---|
| Category leader | "best legal AI for MENA", "best AI for UAE lawyers", "legal AI for Arabic contracts" |
| Competitor comparison | "Harvey vs CoCounsel vs alternatives", "legal AI for Gulf law firms" |
| Job-to-be-done | "AI to draft NDA under UAE law", "end of service gratuity calculator UAE" |
| Brand mention | "HAQQ legal AI", "Louis legal AI", "haqq.ai" |

Record:
- Whether Louis is mentioned
- Position in the response
- Accuracy of description
- Competitor positioning relative to Louis

### Step 2 — Gap analysis

Identify queries where Louis is absent or mischaracterised. Categorise:
- **Content gap** — No owned content exists that could justify a citation
- **Authority gap** — Content exists but is not authoritative enough to be cited
- **Accuracy gap** — LLM describes Louis incorrectly (wrong features, wrong market)

### Step 3 — Content actions

For each gap, assign a content action:

| Gap type | Action |
|---|---|
| Content gap | Create a long-form, citation-rich page on haqq.ai targeting the query |
| Authority gap | Add structured data (JSON-LD), earn backlinks from legal publications, get mentioned in bar-association content |
| Accuracy gap | Update official product descriptions, Wikipedia (if applicable), and LinkedIn company page with accurate capability statements |

## Ongoing LLMO tactics

### Structured data

All pages on haqq.ai and louis.legal (if owned) should include JSON-LD markup:
- `Organization` with `name`, `description`, `areaServed` (MENA jurisdictions listed explicitly)
- `SoftwareApplication` for the product with `applicationCategory: "LegalTech"`
- `FAQPage` markup for jurisdiction-specific pages ("Does Louis support Arabic?", "Does Louis cover UAE law?")

### Citation-rich content

LLMs cite sources that are themselves well-cited. Priority content formats:
- Jurisdiction guides ("Guide to UAE Employment Law 2025") — practical, linkable, cited by lawyers
- Free calculators (EOSG, stamp duty, statutory interest) — high search intent, shared within WhatsApp legal groups
- Comparison pages ("Louis vs Harvey: MENA coverage") — directly targets comparison queries
- Guest posts in regional legal publications (Arab Law Quarterly, DIFC Courts blog)

### Owned domains

Maintain canonical product presence on:
- `haqq.ai` — primary brand domain
- `louis.legal` (if available/owned) — product name domain
- LinkedIn company page — frequently scraped by LLMs
- GitHub (this repository) — open-source credibility signal

### Arabic content strategy

Most LLMs have limited Arabic-language training data about legal AI. Publishing accurate, well-structured Arabic-language pages about Louis creates citation opportunities in Arabic-query results — a largely uncontested space.

## Success metrics

| Metric | Target |
|---|---|
| % of sampled queries where Louis is mentioned | >50% by end of 2026 |
| Position in response (when mentioned) | Top-3 in category |
| Accuracy rate of LLM description | >90% factually correct |
| Quarterly content published | ≥4 citation-target pieces |

## Related skills

- [[strategy-messaging-bible]]
- [[strategy-growth-strategy]]
- [[strategy-competitors]]
- [[strategy-markets]]
