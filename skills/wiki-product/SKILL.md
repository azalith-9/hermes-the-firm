---
name: wiki-product
description: Use when discussing core product management fundamentals — discovery, product requirements documents (PRDs), OKRs, Jobs-to-be-Done (JTBD) frameworks, the Wedge model for market entry, and how these apply to building a legal-AI product. Reach for this skill when the user asks about product management methodology, how to write a PRD, how to apply OKRs, or how to think about product-market fit for a legal-AI product.
license: MIT
metadata: " id: wiki.product category: wiki jurisdictions: [__multi__] priority: P3 intent: [__wiki__, product-management, PRD, OKRs, JTBD, discovery, wedge] related: [wiki-product-mgmt, wiki-haqq-product, wiki-growth, wiki-market, wiki-design] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'wiki'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Product Management Fundamentals

## Scope

This pack covers foundational product management concepts for a legal-AI product team: discovery, PRD writing, OKRs, Jobs-to-be-Done, and the Wedge model for market entry. It is oriented toward founders and product managers who are building or iterating on a legal-AI product in a MENA or cross-border context.

---

## Product discovery

Discovery is the process of identifying what to build before committing engineering resources. The output of good discovery is not a feature list — it is a validated understanding of user problems and a testable hypothesis about how a specific solution will address them.

### Discovery methods for legal-AI

**User interviews**: the practitioner interview is the most important discovery input. Structure:
- Context (what does their day look like? what tools do they use?)
- Pain (what tasks do they dread most? where do they lose the most time?)
- Workaround (what do they do now to address the pain? what is the cobbled-together solution?)
- Value (if this pain went away, what would that free up?)

Avoid asking users what they want to build ("what features would you add?"). Users describe solutions from their limited perspective; your job is to find the underlying problem.

**Shadowing sessions**: observe a practitioner actually doing the work (contract review, research, client meeting prep). Problems that users don't mention in interviews often become obvious in shadowing — the frictions they've normalised and stopped noticing.

**Support ticket analysis**: what are the most common things users ask for help with? What errors do they make? Both reveal unmet needs.

**Competitive analysis**: what gaps exist in the tools users currently use? See [[wiki-legal-tech]] for the competitive landscape.

---

## Product Requirements Document (PRD)

A PRD is the contract between product and engineering for a specific feature or initiative. For a legal-AI product, a PRD should include:

### PRD template

```
## [Feature Name]

### Problem statement
What user problem does this solve? Why does it matter?
Who is the primary user? (e.g. "a DIFC-based associate reviewing a standard NDA")

### Success metrics
How will we know this worked? (e.g. "30% reduction in average NDA review time for active users")

### Non-goals
What is explicitly out of scope? This is as important as the goals.

### Requirements
Functional:
- [User can do X]
- [System does Y when Z]

Non-functional:
- Latency: [e.g. skill invocation < 5s p95]
- Jurisdiction: [works for DIFC, ADGM, UAE federal law]
- Language: [English + Arabic output option]
- Accessibility: [WCAG AA]

### Design / UX references
Link to Figma frames (see [[wiki-dev-design]])

### Open questions
[List unresolved decisions with owners and due dates]

### Legal / compliance considerations
[Any professional conduct, data privacy, or regulatory issues]
```

### PRD discipline

- A PRD is never "done" — it is a living document until the feature ships
- The PM owns the PRD but the team writes it together
- Engineering raises implementation concerns in the requirements phase, not after development starts
- Legal practitioners (or the legal PM) must review any skill-level PRD for professional accuracy

---

## OKRs (Objectives and Key Results)

OKRs set the direction for the team and provide shared accountability for outcomes, not just output.

### Format

```
Objective: [Inspiring, qualitative direction]
  Key Result 1: [Measurable, specific outcome]
  Key Result 2: [...]
  Key Result 3: [...]
```

### Legal-AI OKR examples

**Objective**: Make MENA legal practitioners confident enough in the product to use it for real client work.
- KR1: Activation rate (% of signups completing a real skill invocation) reaches 40% within 7 days
- KR2: 30-day retention for paid users reaches 70%
- KR3: Net Promoter Score from practicing lawyers reaches +40

**Objective**: Establish the product as the trusted reference for UAE employment law.
- KR1: 10 UAE employment law explainers published and indexed in Google top-5 results
- KR2: 200 new signups from organic search for UAE employment law queries
- KR3: 3 UAE law school courses integrate the product into curriculum

### OKR pitfalls in legal-AI

- KR that are outputs, not outcomes: "ship 5 new skills this quarter" is an output. "Increase skill invocations per active user" is an outcome.
- Setting OKRs without validating that the team has the capacity to reach them
- Too many OKRs: 3 objectives maximum per team per quarter; more dilutes focus

---

## Jobs-to-be-Done (JTBD)

JTBD is a framework for understanding user motivation: people "hire" a product to do a specific job in their life. The job has functional, emotional, and social dimensions.

### Applying JTBD to legal-AI

**Functional job**: draft a confidentiality agreement quickly and accurately so I can respond to this client request by end of day.

**Emotional job**: feel confident that I haven't missed anything important; reduce the anxiety of professional responsibility.

**Social job**: demonstrate to my senior partner that I can handle matters efficiently; justify my billing rate.

Understanding all three dimensions shapes which features to build and how to communicate them:
- Feature for functional job: fast, accurate document generation
- Feature for emotional job: risk highlighting, "what might I have missed?" check
- Feature for social job: matter summaries, output sharing, time-saved reporting

### Competing jobs

Not all legal professionals have the same job. A senior partner has a different JTBD than a junior associate:
- Junior associate: avoid mistakes, demonstrate competence, work faster under supervision
- Senior partner: originate clients, supervise quality, manage firm profitability

A legal-AI product that only serves the junior associate's JTBD will not be bought by the senior partner who controls the budget. Design for both.

---

## The Wedge model

The Wedge model (articulated by various startup strategists) is about finding the smallest, most clearly defined market entry point from which you can expand — rather than trying to solve all problems for all customers from day one.

### Applying the Wedge to MENA legal-AI

A clear wedge for HAQQ: **DIFC employment law document generation for boutique UAE law firms**

Why this is a good wedge:
- DIFC employment law is a specific, well-defined legal system (common law; English language; clear framework)
- Boutique UAE law firms are underserved by global legal-AI tools (too small for enterprise deals)
- Employment documents (NDAs, offer letters, employment contracts, termination letters) are high-volume and high-standardisation — well suited to AI generation
- DIFC boutique firm lawyers are relatively tech-forward and willing to try new tools

From this wedge, the expansion path is clear:
- DIFC employment → UAE onshore employment → KSA employment
- Employment documents → all employment law practice area (disputes, regulatory)
- Employment → other practice areas (commercial, real estate)
- Boutique firms → mid-size firms → in-house legal departments

The wedge principle: be irrefutably excellent at one specific thing before expanding. A tool that is "useful for most MENA legal tasks" loses to a tool that is "the definitive DIFC employment law assistant."

---

## Caveats & currency

Product management frameworks evolve; some practitioners prefer Shape Up (Basecamp) or continuous discovery over the sprint-based PRD/OKR model. The right framework depends on team size and culture — the key principle is systematic discovery before building, and outcome-based accountability over output-based reporting. Adapt the frameworks to what your team will actually use.

---

## Related skills

- [[wiki-product-mgmt]]
- [[wiki-haqq-product]]
- [[wiki-growth]]
- [[wiki-market]]
- [[wiki-design]]
