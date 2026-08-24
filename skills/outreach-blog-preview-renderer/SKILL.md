---
name: outreach-blog-preview-renderer
description: Use when the legal AI product team needs to preview, format, or generate a blog post for publication — either for the product blog or for placement in third-party legal/tech publications. Produces a preview-ready draft with headline, meta description, body, and social sharing copy. Triggers on requests to draft, review, or prepare blog content for a legal AI product.
license: MIT
metadata: " id: outreach.blog-preview-renderer category: outreach intent: ['__outreach__', 'blog', 'content', 'preview', 'publication'] related: - outreach-backlink-pr-campaign - outreach-press-list-mena - outreach-growth-agent-runner priority: P3 source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'outreach'.
Registered as a flat plugin skill.
-->


# Blog Preview Renderer

Blog content is the primary organic growth lever for a legal AI product: it builds domain authority, educates potential users, demonstrates product capability, and generates the linkable assets that power PR campaigns. A blog post is also a trust signal to the professional audience — lawyers expect precision, citations, and a point of view. This skill produces a preview-ready blog post package.

## Purpose

Produce a complete, publication-ready blog post that:
- Is accurate enough to pass review by a qualified lawyer
- Is readable enough to engage a non-lawyer business audience
- Includes all metadata needed for web publication (headline, meta, slug, tags)
- Can be repurposed as social content (LinkedIn, Twitter/X)

## Inputs

| Input | Why it matters | Default |
|---|---|---|
| Topic / angle | The specific argument or insight the post makes | See topic bank below |
| Target audience | Lawyer vs in-house counsel vs GC vs startup founder | MENA in-house / GC |
| Target publication | Own blog vs third-party placement affects tone and depth | Own product blog |
| Target jurisdiction | Determines which legal rules are cited | UAE / MENA |
| Desired word count | Different for thought leadership vs how-to vs news commentary | 800–1200 words |
| SEO target keyword | For own blog; for placement pieces focus on publication fit | Varies by topic |

## Output package

For each blog post, produce:

### 1. Headline options (3)

| Type | Example |
|---|---|
| How-to | "How to Negotiate a Non-Compete Clause Under UAE Law" |
| Data / insight | "Why 80% of UAE Non-Compete Clauses Are Unenforceable" |
| Opinion / take | "MENA Lawyers Are Still Drafting for Yesterday's Workforce Law" |

### 2. Meta description (160 characters max)

> "UAE non-compete clauses must meet four legal tests to be enforceable. Most don't. Here's what in-house counsel should be doing differently in 2026."

### 3. Article body structure

```
# [Headline]

## The problem / hook (1–2 paragraphs)
Open with a concrete scenario or surprising fact. No "in the rapidly evolving landscape" openers.

## The rule / insight (2–3 paragraphs)
State the law or principle clearly. Cite correctly (light citation for blog: "Article 10 of UAE Federal Decree-Law 33/2021").
No fabricated citations.

## The implication / application (2–3 paragraphs)
What does this mean for practitioners? What should they do differently?
Concrete, actionable.

## The MENA angle (1–2 paragraphs)
If the topic spans jurisdictions, flag the material differences briefly.
This is the differentiating content for a MENA-focused product.

## Call to action
One concrete next step for the reader. Tie to product capability if relevant.

---
*This article is for informational purposes only and does not constitute legal advice. Consult qualified legal counsel for advice on your specific situation.*
```

### 4. Social copy

**LinkedIn (300 characters):**
> "Most UAE non-compete clauses are drafted to fail. Under FDL 33/2021, they must be proportionate in scope, geography, and duration. A "no competitors, MENA region, 2 years" clause will get reduced by a court. Here's the redraft checklist. [link]"

**Twitter/X (280 characters):**
> "UAE non-competes: 4 tests, most fail. Scope ✓ Geography ✗ Duration borderline ✓ Legitimate interest ✗. FDL 33/2021 gives courts power to narrow, not void. Practical fix below. 🧵"

## Topic bank — legal AI product blog

High-value topics for a MENA-focused legal AI product:

| Category | Topics |
|---|---|
| Jurisdiction guides | "UAE Employment Law 2026: The 5 Rules GCs Get Wrong" · "DIFC vs Onshore UAE: Which Forum for Your Next Commercial Dispute?" |
| AI + law | "What Legal AI Can (and Cannot) Do for Your MENA Practice" · "The In-House GC's Guide to AI-Assisted Contract Review" |
| Practice area how-tos | "NDA Negotiation in MENA: The 6 Clauses That Kill Deals" · "Cross-Border M&A in the GCC: Regulatory Approvals Explained" |
| Thought leadership | "Why the GCC Needs a Unified IP Framework" · "Legal Operations: How Fast-Growing MENA Companies Build Without Big Law" |
| Product / skills | "We Analysed 500 MENA Employment Contracts. Here's What We Found." · "Introducing the Open Legal AI Skills Library" |

## Quality bar

- Every legal statement must be accurate and cited at a level appropriate for a professional audience.
- "Arguably" and similar weasel words are acceptable in opinion pieces but not in how-to posts.
- Do not fabricate statistics. If you don't have data, describe the phenomenon without inventing numbers.
- Apply the legal AI disclaimer at the bottom of every post.

## What to avoid

- SEO-stuffed intros ("In today's fast-paced legal landscape…")
- Vague conclusions ("Legal teams should consider AI tools")
- Overly promotional copy that obscures the informational value
- Any advice that crosses into a client-lawyer relationship (the disclaimer is mandatory, not optional)

## Related skills

- [[outreach-backlink-pr-campaign]]
- [[outreach-press-list-mena]]
- [[outreach-press-list-europe]]
- [[outreach-growth-agent-runner]]
