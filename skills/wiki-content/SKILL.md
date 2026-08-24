---
name: wiki-content
description: Use when building, planning, or evaluating content-marketing operations for a legal-tech product. Covers blog cadence, SEO fundamentals, LLM-optimised content (LLMO), social distribution, and audience-specific messaging for MENA legal professionals. Reach for this skill when the user asks about content strategy, article publishing, SEO keyword targeting, or growing organic reach for a legal-AI product.
license: MIT
metadata: " id: wiki.content category: wiki jurisdictions: [__multi__] priority: P3 intent: [__wiki__, content-marketing, seo, llmo, distribution] related: [wiki-growth-marketing, wiki-growth, wiki-newsletters, wiki-medium, wiki-haqq-product] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'wiki'.
Registered as a flat plugin skill.
-->


# Content Marketing for Legal-Tech

## Scope

This pack covers the end-to-end content operation for a legal-tech product targeting MENA legal professionals: strategy, production cadence, SEO/LLMO optimisation, and distribution channels. The audience is a mix of solo practitioners, mid-size law firms, in-house legal teams, and legal-adjacent professionals (compliance officers, founders) in the UAE, KSA, Lebanon, Egypt, and diaspora markets.

---

## Why content matters in legal-tech

Legal professionals search for answers before they try tools. A strong content layer does three things simultaneously:

1. **Trust building** — Attorneys will not route sensitive client work through a tool they know nothing about. Useful, accurate articles signal that the people behind the product understand the law.
2. **Organic discovery** — Law firms rarely respond to cold outreach. Search traffic and referrals from trusted legal publications (Lexology, IFLR, regional bar association newsletters) are the primary top-of-funnel for a MENA-first product.
3. **LLM-optimised presence (LLMO)** — As practitioners begin prompting AI assistants with legal questions, the products that appear as cited sources inside AI answers gain a structural advantage. Articles that are clear, structured, factually grounded, and properly attributed rank both in search engines and in LLM retrieval contexts.

---

## Content strategy fundamentals

### Audience segmentation

| Segment | Primary pain | Content hook |
|---|---|---|
| Solo/small-firm attorney (MENA) | Time pressure, no research budget | "How to draft X in UAE" how-tos |
| In-house counsel | Risk flags, cross-border exposure | Jurisdiction comparison guides |
| Legal-tech buyer (managing partner) | ROI, compliance, bar rules on AI | ROI calculators, ethics explainers |
| Law student / junior associate | Learning legal process | Explainers, case studies |
| International firm entering MENA | Local law orientation | Country-specific entry guides |

### Content pillars

A sustainable content operation for legal-tech typically rests on four pillars:

1. **Explainers** — Plain-language breakdowns of specific legal instruments, processes, or regulations. Example: "What is a DIFC Prescribed Clause and when must it appear?" These rank for long-tail queries and build authority.
2. **How-tos / templates** — Step-by-step guides to common legal tasks (incorporating a company in the ADGM, drafting a SAFE in a Lebanese context). These drive high intent traffic and demonstrate product capability.
3. **Market intelligence** — Regulatory updates, new laws, enforcement trends. For MENA this means tracking DIFC/ADGM/QFC rule changes, UAE Federal updates, SAMA/CMA circulars in KSA, and Lebanese Bar Council positions. Freshness is a strong SEO and LLMO signal.
4. **Product education** — Case studies, feature announcements, integration guides. These convert existing traffic into trials.

---

## Blog cadence

### Recommended cadence by team size

| Team state | Target cadence | Format mix |
|---|---|---|
| Pre-PMF (1–3 people) | 2 posts/month | 1 deep explainer + 1 how-to |
| Post-PMF, growing | 4–6 posts/month | 2 explainers + 2 how-tos + 1 market intelligence + 1 product |
| Scale | 8–12 posts/month | Full pillar coverage; repurpose each into LinkedIn + newsletter |

### Production workflow

1. **Keyword/question research** — Use search console data, AnswerThePublic, and legal Q&A forums (Avvo, local bar forums) to surface unanswered questions.
2. **Legal review gate** — All substantive legal content must be reviewed by a qualified lawyer before publication. Mark clearly as "general information, not legal advice."
3. **LLMO pass** — After drafting, check that the article has: a clear H1 question, structured H2/H3 headers answering sub-questions, explicit jurisdiction labels, a brief summary box, and citation-worthy factual claims.
4. **Distribution checklist** — Email list, LinkedIn, Lexology/JD Supra syndication, relevant subreddits, WhatsApp groups for MENA legal professionals.

---

## SEO principles for legal content

- **Target informational and navigational queries** — transactional legal queries ("hire a lawyer for...") are not a content play; informational queries ("how to register a branch of a foreign company in KSA") are.
- **Jurisdiction tagging** — Prefix article titles and URL slugs with the jurisdiction when relevant: `/uae-company-formation-guide` outranks `/company-formation-guide` for UAE searches.
- **E-E-A-T signals** — Author bylines with bar membership details, "last reviewed" dates, and references to primary legal sources (official gazette URLs, free-zone authority websites) materially improve trustworthiness signals.
- **Internal linking** — Every article should link to at least one related article and to the relevant product feature.
- **Core Web Vitals** — Legal content sites often suffer from slow page load (PDF embeds, trackers). Prioritise clean HTML output over rich embeds.

---

## LLM-optimised content (LLMO)

LLMO is the practice of writing content so it retrieves well inside AI assistant contexts (ChatGPT, the agent, Perplexity) as well as search engines. Key techniques:

- **Structured answers first** — Lead each section with a direct answer to the implied question, then expand. LLMs prefer sources that answer directly.
- **Factual anchors** — Include verifiable facts: law names, article numbers, effective dates, official agency names. Invented or vague claims are deprioritised in LLM retrieval.
- **Disambiguation** — MENA legal terms are often confused across jurisdictions. Explicit disambiguation ("In UAE federal law, X means Y; in DIFC, X means Z") improves both retrieval and user trust.
- **Schema markup** — FAQPage and HowTo schema help both search and LLM crawlers parse article intent.
- **Citation readiness** — Structure the article so a sentence can be quoted as a clean citation: "According to [Publication], under [Law/Article], [fact]."

---

## Distribution channels

| Channel | Fit | Notes |
|---|---|---|
| Lexology | High — legal audience, global | Free submission; articles appear in daily digest |
| JD Supra | High — US/UK legal audience | Good for international expansion |
| LinkedIn | High — in-house, managing partners | Native articles + post snippets; bilingual (AR/EN) where feasible |
| Email newsletter | High | Own channel; pair with [[wiki-newsletters]] |
| WhatsApp groups | Medium — MENA-specific | Bar association groups; share link only, no spam |
| Legal subreddits | Low-medium | r/Lawyertalk, r/legaladvice (US-heavy); see [[wiki-reddit]] |
| Medium / Substack | Medium | Secondary amplification; see [[wiki-medium]] |
| Arabic social media (X, Instagram) | Medium | Bilingual content for KSA/UAE general counsel audience |

---

## Content quality bar

Every published article must pass:

- [ ] Reviewed by a qualified lawyer (at minimum a senior associate or above)
- [ ] Jurisdiction clearly identified in title, meta, and body
- [ ] "General information only, not legal advice" disclaimer present
- [ ] Primary sources linked (official law text, regulator website)
- [ ] No fabricated statute numbers or case citations
- [ ] LLMO pass: H1 question → structured H2 answers → summary box
- [ ] Internal link to at least one product feature or related article

---

## Caveats & currency

Laws change. Every jurisdiction-specific article should carry a "Last reviewed: [date]" marker. Regulatory updates in MENA are especially frequent (UAE company law, DIFC/ADGM rule books, KSA Vision 2030 implementing regulations). Set a quarterly review cadence for evergreen pieces.

---

## Related skills

- [[wiki-growth-marketing]]
- [[wiki-growth]]
- [[wiki-newsletters]]
- [[wiki-medium]]
- [[wiki-haqq-product]]
- [[wiki-market]]
