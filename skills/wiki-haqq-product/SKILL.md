---
name: wiki-haqq-product
description: Use when discussing the HAQQ Legal AI product vision, design philosophy, architecture decisions, or the roles of the Louis/Justinian/Justice AI triumvirate within the system. Covers the comfort-UI mandate, MENA-first and bilingual design requirements, jurisdiction-aware skill routing, and how the product's positioning as a developer platform for legal differs from pure legal-AI tools. Reach for this skill when the user asks about product strategy, HAQQ's differentiation, the AI architecture, or the legal-comfort vision.
license: MIT
metadata: " id: wiki.haqq-product category: wiki jurisdictions: [UAE, KSA, LB, EG, DIFC, ADGM, GCC] priority: P3 intent: [__wiki__, product-vision, MENA-first, comfort-UI, jurisdiction-aware, bilingual] related: [wiki-legal, wiki-design, wiki-market, wiki-legal-tech, wiki-engineering] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'wiki'.
Registered as a flat plugin skill.
-->


# HAQQ Legal AI — Product Vision

## Scope

This pack documents the HAQQ Legal AI product vision: the comfort-UI design mandate, MENA-first positioning, jurisdiction-aware architecture, bilingual design, and the roles of the three AI personas — Justinian, Louis, and Justice — within the system. It serves as the canonical product context for any feature, design, or strategy decision.

---

## Core vision

HAQQ Legal AI is built around a single north-star insight: **legal professionals adopt AI tools when those tools feel like trusted colleagues, not like search engines or chatbots**. The product is designed to feel calm, authoritative, and safe — particularly for practitioners in MENA markets where reputational risk is high and professional culture is relationship-oriented.

The product's positioning is not "fastest AI for legal tasks" — it is "the legal AI that MENA practitioners are comfortable enough to actually use for client work."

---

## The three AI personas

### Justinian — the legal educator

Justinian is the teaching persona. It explains legal concepts, walks practitioners through unfamiliar areas of law, runs Socratic case simulations, and serves as a legal research companion. Named after Emperor Justinian I, whose Corpus Juris Civilis systematised Roman law.

**Justinian's voice**: patient, structured, authoritative without being condescending. It cites sources and explains the "why" behind legal rules. It never pretends to give legal advice — it explains law.

**Primary users**: law students, junior associates, practitioners entering a new practice area, in-house counsel without litigation background.

### Louis — the legal assistant

Louis is the practitioner-facing assistant. It drafts documents, reviews contracts, answers specific legal questions, and routes tasks to the appropriate skills. Named as a reference to the French legal tradition (MENA civil law has deep French civil-law roots) and as an approachable professional persona.

**Louis's voice**: direct, practical, precise. It asks clarifying questions when necessary but does not over-explain. It surfaces risks clearly and routes to a lawyer when the situation warrants it.

**Primary users**: practicing lawyers using the product for day-to-day work — drafting, review, research, matter management.

### Justice — the access-to-justice interface

Justice is the public-facing interface for individuals who need legal information but cannot afford a lawyer. It operates under a stricter safety envelope than Louis — it explains rights and processes but never drafts documents or gives specific legal advice.

**Justice's voice**: warm, plain-language, multilingual. It prioritises clarity over comprehensiveness and always ends with an escalation path ("if this is urgent, contact [resource]").

**Primary users**: individuals in MENA navigating personal legal situations (tenant rights, employment disputes, family law questions).

---

## Comfort-UI mandate

Comfort-UI is a design directive, not just a visual style. It means:

1. **The interface does not demand** — no aggressive CTAs, no countdown timers, no "your free trial ends in X hours" banners.
2. **The interface does not surprise** — every AI action is predictable; outputs are labelled with their source skill; the user always knows what happened.
3. **The interface admits uncertainty** — when the AI is not confident, it says so. A practitioner who discovers an AI error they were not warned about will stop using the tool.
4. **The interface respects seniority** — senior practitioners do not want to be "guided through" tasks they have done a thousand times. Advanced mode should be available immediately.
5. **The interface is calm under pressure** — legal work happens in deadline contexts. The UI must perform reliably when the user is stressed; no spinner with no feedback, no modal storms.

Implementation: see [[wiki-design]] for the design system and [[wiki-frontend]] for the technology stack.

---

## MENA-first design

MENA-first means that MENA jurisdictions and MENA user needs are the primary design target, not an afterthought. Concretely:

- **Jurisdiction-aware skill routing**: the router knows the user's default jurisdiction(s) and surfaces the appropriate law, not generic global defaults.
- **Arabic-first option**: full Arabic-language interface available, including RTL layout, Arabic typography, and Arabic-language AI outputs.
- **Civil-law defaults**: most MENA jurisdictions use civil-law systems (influenced by French and Egyptian civil law). Skills should default to civil-law framings unless the user has selected a common-law context (DIFC, ADGM, UK).
- **Regional compliance context**: skills are aware of UAE PDPL, KSA PDPL, DIFC Data Protection Law, and other MENA-specific regulatory frameworks.

---

## Jurisdiction-aware architecture

Every skill invocation in the system carries a jurisdiction context. The routing layer maintains a jurisdiction stack:

```
User default jurisdiction(s) (set at onboarding)
  → Workspace jurisdiction override (set per firm account)
    → Matter jurisdiction override (set per matter)
      → Session jurisdiction override (set explicitly in conversation)
```

When a skill produces an output, it labels the jurisdiction that informed its answer. If the user's context is multi-jurisdictional (e.g. a UAE-incorporated company with a DIFC subsidiary), the skill flags cross-jurisdictional issues explicitly.

Skills that do not know which jurisdiction applies should ask before proceeding, not silently default to a single jurisdiction.

---

## Developer platform for legal positioning

HAQQ's strategic positioning is as a **developer platform for legal**, not a point solution. This means:

- The skill system is extensible — law firms and legal departments can author their own skills using the skill SDK
- The API is open — third-party integrations can invoke the skill layer
- The cookbook (planned) documents how to build legal workflows on the platform
- The pricing model should not punish power users or builders

This positioning differentiates HAQQ from single-workflow tools (e.g. a pure contract review tool) and from general-purpose AI (e.g. GPT-4 used ad-hoc without legal domain knowledge). It positions HAQQ as infrastructure for legal-AI applications in MENA.

---

## What the product is not

- Not a law firm replacement: HAQQ escalates to human lawyers at the limits of its confidence.
- Not a US-law tool repainted for MENA: the domain knowledge is MENA-primary.
- Not a closed enterprise product: the free tier (with BYO-key option) is a strategic commitment to access.
- Not a feed-driven product: the vertical command rail (not a social feed) is the primary interaction model.

---

## Caveats & currency

Product strategy evolves. The authoritative source for current product decisions is the canonical roadmap (see [[wiki-legal-tech]] for the competitive landscape that informs positioning). Feature flags and the current skill set may differ from this strategic vision during any given development sprint.

---

## Related skills

- [[wiki-legal]]
- [[wiki-design]]
- [[wiki-market]]
- [[wiki-legal-tech]]
- [[wiki-engineering]]
