---
name: wiki-strategy
description: Use when a user asks about business strategy frameworks, competitive positioning, go-to-market theory, or how to apply strategy thinking to legal-tech products and incumbent disruption in the MENA legal market. Provides a reference on core strategy frameworks (Porter, jobs-to-be-done, blue ocean, wedge) with explicit legal-tech application and MENA market context.
license: MIT
metadata: " id: wiki.strategy category: wiki jurisdictions: [__multi__] priority: P3 intent: [__wiki__, strategy, competitive positioning, legal-tech disruption, porter, jobs-to-be-done, blue ocean] related: [wiki-startup, wiki-sales, wiki-vc-startups, wiki-tech] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'wiki'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Business Strategy Frameworks

## Scope

This pack covers core business strategy frameworks and their application to legal-tech product strategy and MENA market entry. It is relevant to founders, legal-tech product managers, and legal professionals advising on business restructuring, M&A rationale, or competitive positioning.

---

## Framework 1 — Porter's Five Forces

Michael Porter's framework assesses the structural attractiveness of an industry based on five competitive forces:

| Force | Meaning | Legal-tech application |
|-------|---------|----------------------|
| Threat of new entrants | How easy is it for new players to enter? | AI lowers barriers dramatically; open-source LLMs allow new entrants; but regulation (law firm licensing), data moats, and customer trust slow entry |
| Bargaining power of buyers | How much leverage do customers have? | Law firms have high switching costs (trained staff, integrated workflows); in-house teams have lower switching costs |
| Bargaining power of suppliers | How much leverage do input providers have? | LLM providers (Anthropic, OpenAI, Google) have high bargaining power; data providers and bar associations have limited but real leverage |
| Threat of substitutes | Could customers solve the problem differently? | Law firms can: (a) hire more associates, (b) send to offshore LPO, (c) use a different legal-tech tool — substitution risk is high |
| Competitive rivalry | How intense is competition among existing players? | Intense: numerous legal-tech vendors, price pressure, low differentiation in generic AI tools; differentiation on jurisdiction-specific depth, MENA focus, integration depth |

**Legal-tech insight**: the most defensible legal-tech positions are those that create **workflow lock-in** (deep integration with matter management, billing, document management systems) and **jurisdiction-specific data moats** (training data, regulatory databases that new entrants cannot easily replicate).

---

## Framework 2 — Jobs-to-Be-Done (JTBD)

Clayton Christensen's JTBD theory: customers do not buy products; they hire products to do a specific job. Understanding the job (not the feature) is the strategy insight.

### JTBD in Legal-Tech

| Job to be done | Current hire | Legal-tech hire |
|----------------|-------------|----------------|
| "Draft an NDA quickly without paying a lawyer $500" | Google + DIY | AI drafting tool |
| "Know whether this contract is safe to sign before my 3pm meeting" | Call outside counsel | Contract review AI |
| "Make sure our company is GDPR-compliant without hiring a full-time DPO" | Big 4 consultancy | Compliance SaaS |
| "Find precedents for structuring this deal" | Associate research | Research AI |

Knowing the job allows you to price against the true alternative (outside counsel fees, compliance consultancy), not against the cheapest software alternative.

### MENA-Specific Jobs

- "Understand what the new PDPL means for our company's data practices" — complex regulatory analysis in an unfamiliar framework
- "Generate an Arabic-language employment contract compliant with KSA Labour Code" — jurisdiction-specific, language-specific
- "Review this investor term sheet before my co-founder signs it" — time-sensitive, high stakes, typically without access to good local counsel

---

## Framework 3 — Wedge Strategy

A wedge is a narrow initial use case that serves as a low-friction entry point, leading to platform expansion over time.

### Classic Wedge Playbook

1. **Choose the entry wedge**: a specific task that (a) everyone in the target market does, (b) is painful enough to pay for, (c) is narrow enough to do well, and (d) naturally leads to adjacent jobs
2. **Nail the wedge**: build an order-of-magnitude better solution for the wedge before expanding
3. **Expand by adjacency**: once the wedge is won, the product expands into adjacent jobs the same buyer already has

### Legal-Tech Wedge Examples

- **NDA review** → all contract review → all legal workflow
- **Employment contract generator** → full HR legal suite → general corporate documents
- **GDPR compliance** → all data privacy regimes → all regulatory compliance
- **IP trademark filing** → full IP management → brand protection → commercial contracts

For MENA legal-tech:
- **DIFC / ADGM document library** → regional common-law practice platform
- **KSA labour contract compliance** → Saudi employment law platform → all Saudi corporate compliance
- Arabic contract translation + summary is a strong wedge: every MENA law firm has to handle Arabic contracts but AI tools have historically been English-only

---

## Framework 4 — Blue Ocean Strategy

Chan Kim and Renée Mauborgne: instead of competing in a "red ocean" (existing market, existing competition), create "blue ocean" (new market space, new demand, no competition).

**Eliminate-Reduce-Raise-Create grid** applied to legal-tech:

| Action | Example |
|--------|---------|
| Eliminate | Long onboarding; complex pricing tiers; billable hour model for routine tasks |
| Reduce | Cost per task; time to first output; human review required for low-risk items |
| Raise | Accuracy for jurisdiction-specific tasks; auditability of AI reasoning; speed of turnaround |
| Create | Real-time regulatory change alerts; automatic contract comparison against market standard; multi-language output |

**MENA blue ocean opportunities**:
- Arabic legal AI is genuinely underserved — most global players are English-first; a MENA-native Arabic legal AI creates a new market rather than competing with Clio, Harvey, or Ironclad
- Islamic finance document automation: a large, specialized market with limited technology coverage
- Cross-border MENA arbitration support: DIAC, ADCCAC proceedings in Arabic + English simultaneously

---

## Framework 5 — Incumbent Disruption Thesis (Legal-Tech)

Why traditional law firms are structurally vulnerable:

1. **Business model misalignment**: hourly billing incentivizes slow work; automation that saves client money also reduces law firm revenue — incumbents have structural disincentive to automate
2. **Fragmented market**: no single law firm dominates globally or in MENA; no one firm controls standard-setting
3. **Regulatory moat erosion**: unauthorized practice of law restrictions are slowly eroding as AI tools become "legal research" rather than "legal advice" — the regulatory protection that incumbents relied on is narrowing
4. **Talent arbitrage**: AI can replicate first-year associate work at essentially zero marginal cost; the economic case for large associate classes weakens
5. **Data advantage**: legal AI tools accumulate clause libraries, benchmark data, and market norms across thousands of deals — incumbents lack comparable structured databases

### Incumbent Response Patterns

Historically, incumbents respond via:
- **Acqui-hire** — buy the startup and absorb the talent; technology often dies in integration
- **Internal build** — launch an internal "innovation lab" with insufficient mandate; rarely succeeds at scale
- **Licensing** — white-label the legal AI tool; faster to market but limits differentiation
- **Ignore and wait** — bet on client inertia and regulatory protection; viable short-term, dangerous medium-term

---

## Strategic Synthesis for MENA Legal-Tech

The most defensible MENA legal-tech position combines:

1. **Deep jurisdiction specificity** — Arabic language, MENA civil law, Islamic finance compliance — not available from global competitors
2. **Workflow integration** — embedded in the daily workflow of MENA legal professionals, not a standalone tool
3. **Regulatory trust** — compliance with PDPL, UAE data residency requirements, confidentiality standards that international competitors often fail
4. **Network effects** — as more MENA firms use the platform, the clause library, benchmark data, and market norms improve, making the tool more valuable for all users

---

## How to Use This Pack

Reference when:
- Advising a legal-tech founder on positioning and competitive strategy
- Analyzing an M&A target's strategic position in the legal-tech landscape
- Developing a go-to-market strategy for a new legal product in MENA
- Structuring a strategic partnership agreement between a law firm and a legal-tech vendor

---

## Caveats & Currency

Strategy frameworks are analytical tools, not prescriptions. The legal-tech market landscape changes rapidly; specific competitive positions described here reflect conditions as of mid-2024. Verify current market positions and competitive dynamics independently.

## Related Skills

- [[wiki-startup]]
- [[wiki-sales]]
- [[wiki-vc-startups]]
- [[wiki-tech]]
- [[wiki-research]]
