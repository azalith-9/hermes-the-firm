---
name: wiki-product-mgmt
description: Use when applying specific product management tools and processes — roadmapping, prioritisation frameworks (RICE, MoSCoW), stakeholder management, sprint planning, and how to run these processes effectively in a legal-AI product team context. Reach for this skill when the user asks about how to build a product roadmap, how to prioritise between competing features, or how to manage stakeholders (legal domain experts, engineers, investors) in a legal-tech product organisation.
license: MIT
metadata: " id: wiki.product-mgmt category: wiki jurisdictions: [__multi__] priority: P3 intent: [__wiki__, product-roadmap, prioritisation, RICE, MoSCoW, stakeholders, sprint] related: [wiki-product, wiki-haqq-product, wiki-engineering, wiki-design, wiki-leadership-people] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'wiki'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Product Management: Roadmapping, Prioritisation, and Stakeholders

## Scope

This pack covers the operational practice of product management: how to build and maintain a product roadmap, how to prioritise between competing feature requests, and how to manage the specific stakeholder dynamics of a legal-AI product team. It complements [[wiki-product]] (which covers foundational frameworks like JTBD and OKRs) with the recurring process work of a PM.

---

## Roadmapping

A product roadmap communicates direction and priority. It is not a delivery schedule — it is a prioritised list of bets, with rough horizons, that can and should change as new information arrives.

### Roadmap types

| Type | Use when | Format |
|---|---|---|
| **Now / Next / Later** | Early-stage; high uncertainty | Three-column Kanban with themes or user stories |
| **Quarterly theme roadmap** | Post-PMF; quarterly planning cadence | Themes per quarter with outcome goals |
| **Feature backlog** | Operational backlog; sprint planning input | Prioritised list with RICE scores |
| **Investor roadmap** | Fundraising or board communication | High-level milestones; outcome-focused |

For a legal-AI product, the quarterly theme roadmap is recommended once you have at least one clear user segment (see [[wiki-product]]'s wedge model). Themes provide direction without over-committing to specific features before discovery is complete.

### Roadmap disciplines

- **Review monthly**: the roadmap is not a static document. Re-prioritise as user interviews, usage data, and market signals arrive.
- **Publish to the team**: every engineer and designer should know what the next 3 months look like. Context on the "why" of each theme reduces misbuilding.
- **Separate "what we're building" from "why we're building it"**: the roadmap is the "what"; the PRD (see [[wiki-product]]) is the "why" and "how". Do not write a roadmap that specifies implementation details.
- **Reserve slack**: plan to 70–80% of capacity. The remaining 20–30% accommodates urgent bugs, unexpected discoveries, and quality improvements. Over-scheduled roadmaps collapse on first contact with reality.

---

## Prioritisation frameworks

### RICE

RICE scores features for development priority:

```
RICE Score = (Reach × Impact × Confidence) / Effort

Reach: How many users will this affect per quarter? (estimate from data)
Impact: How much will it improve the target metric? (0.25 = minimal, 0.5 = low, 1 = medium, 2 = high, 3 = massive)
Confidence: How confident are you in the estimates? (50% = low, 80% = medium, 100% = high)
Effort: How many person-weeks does this require?
```

**Example for a legal-AI feature:**
```
Feature: Arabic-language output for contract review
Reach: 400 users/quarter (estimate of Arabic-primary users)
Impact: 2 (high — unlocks a segment that currently cannot use the product)
Confidence: 80%
Effort: 6 person-weeks

RICE = (400 × 2 × 0.8) / 6 = 107
```

RICE is most useful when comparing similar types of features with similar data confidence. Do not over-engineer the scores; the discipline of going through the exercise is more valuable than the precision of the output.

### MoSCoW

MoSCoW categorises requirements by urgency:
- **Must have**: non-negotiable; the product cannot ship without this
- **Should have**: important but not blocking; defer only if necessary
- **Could have**: nice to have; include if capacity allows
- **Won't have (this time)**: explicitly de-scoped for this cycle; may reconsider later

MoSCoW is best used for sprint or milestone scoping when there is a fixed capacity and the question is "what goes in?" rather than "what gets done first?"

**Legal-AI application**: when scoping the first skill for a new practice area (e.g. UAE real estate), use MoSCoW to distinguish: Must — basic lease review flag; Should — full landlord-tenant rights analysis; Could — comparison with KSA equivalent; Won't (this sprint) — Arabic-language output version.

---

## Stakeholder management

### The legal-AI stakeholder landscape

A legal-AI PM must manage a distinctive set of stakeholders:

| Stakeholder | Primary concern | Key dynamic |
|---|---|---|
| **Domain lawyers** (advisors, pilot users) | Legal accuracy | Will veto a feature that produces wrong outputs; slow to approve; essential for credibility |
| **Engineers** | Feasibility, technical debt | Will push back on vague requirements; need clear acceptance criteria |
| **Designers** | User experience, comfort-UI mandate | Will flag when requirements create UX friction; need design review time in the sprint |
| **Investors / board** | Metrics, market opportunity | Want evidence of traction; interpret roadmap as commitment |
| **Legal professionals (users)** | Time savings, risk reduction | Want reliability above novelty; will abandon if one bad output |
| **Firm buyers (managing partners)** | Cost justification, compliance | Need evidence, not demos; procurement time is long |

### Navigating domain lawyers as stakeholders

Legal practitioners have high standards for accuracy. A junior associate who finds a hallucinated statute number in an AI output will immediately distrust the entire tool. This creates a specific stakeholder management challenge: domain lawyers are slow to approve, but their approval is the only credible quality signal.

Strategies:
- Establish a small advisory group of practitioners (3–5 across jurisdictions) who commit to monthly reviews of new skill outputs
- Create a systematic review process: every new skill must pass a legal review gate before public release (see [[wiki-engineering]] for deployment gates)
- Be transparent about limitations: "this skill covers DIFC employment law; it does not cover UAE federal labour law" is better than a broadly accurate but sometimes wrong combined skill

### Managing the roadmap with investors

Investors see the roadmap as a commitment; PMs know it is a hypothesis. Manage this tension by:
- Presenting the roadmap as themes with outcomes ("we will achieve [X] activation improvement by [Q]") rather than feature lists ("we will ship [Y] features")
- Reporting on outcome metrics in board updates, not just feature completion ("activation rate reached 38%, target was 40%" is more useful than "we shipped 7 features")
- Being explicit about what changed and why when priorities shift ("we deprioritised feature X because discovery showed users prefer Y")

---

## Sprint planning and execution

For a legal-AI product team running 2-week sprints:

### Sprint planning (2–3 hours)

1. Review the sprint goal (derived from the quarterly theme)
2. Pull from the top of the prioritised backlog into the sprint
3. Engineers estimate effort and raise blockers
4. PM clarifies acceptance criteria for each ticket
5. Confirm the sprint is feasible (capacity check against velocity)

### Definition of Done for legal-AI features

A ticket is done when:
- [ ] Code merged to main and deployed to staging
- [ ] Unit and integration tests passing
- [ ] Design review completed (designer signed off against Figma frame)
- [ ] Legal review completed (for any skill that produces substantive legal output)
- [ ] Accessibility check passed
- [ ] Documentation / skill metadata updated
- [ ] Feature flag set for staged rollout

---

## Caveats & currency

Prioritisation frameworks are aids to decision-making, not decision-making machines. A RICE score of 120 vs 115 does not mean one feature is objectively better than the other. The value of the process is in making assumptions explicit and facilitating team discussion. Adapt to what your team actually uses; the right process is the one that produces better decisions and clearer communication in your specific context.

---

## Related skills

- [[wiki-product]]
- [[wiki-haqq-product]]
- [[wiki-engineering]]
- [[wiki-design]]
- [[wiki-leadership-people]]
