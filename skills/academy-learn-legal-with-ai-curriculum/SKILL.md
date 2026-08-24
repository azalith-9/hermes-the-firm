---
name: academy-learn-legal-with-ai-curriculum
description: Use when a lawyer, law student, or legal professional wants a structured self-paced curriculum to develop practical legal AI proficiency. Delivers a 12-week program covering AI fundamentals, prompt engineering for lawyers, document workflows, citation hygiene, clause libraries, jurisdiction navigation, professional ethics, and AI-disclosure obligations. Calibrated to MENA practitioners but applicable globally. Triggers on requests for training plans, AI upskilling curricula, or structured legal-tech learning paths.
license: MIT
metadata: " id: academy.learn-legal-with-ai-curriculum category: academy jurisdictions: [__multi__] priority: P3 intent: [__customer-facing__, curriculum, training, legal-ai-literacy] related: [academy-justinian-tutor, academy-legal-ai-skills-catalog, academy-students-program, academy-ai-feature-explainer] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'academy'.
Registered as a flat plugin skill.
-->


# Learn Legal with AI — 12-Week Curriculum

## When to use this

Invoke when:
- A lawyer or law student asks "how do I get good at using AI for legal work?"
- A firm's professional-development lead asks for a structured AI training program
- A user wants a self-paced roadmap to legal AI proficiency
- An academic program wants to integrate AI literacy into its legal curriculum
- A new Louis user wants a guided onboarding path beyond feature discovery

## Program overview

| Duration | Format | Target audience | Commitment |
|---|---|---|---|
| 12 weeks | Self-paced, module-based | Lawyers, law students, paralegals, in-house teams | ~2–4 hours/week |

The curriculum is divided into three phases:
- **Phase 1 (Weeks 1–4):** Foundations — understanding what AI does and does not do, and how to talk to it effectively
- **Phase 2 (Weeks 5–9):** Application — using AI across the core legal workflows
- **Phase 3 (Weeks 10–12):** Mastery and responsibility — advanced techniques, ethics, and disclosure obligations

## Week-by-week curriculum

### Phase 1: Foundations

**Week 1 — How AI Language Models Work (for Non-Engineers)**
- What an LLM is and is not (no memory between sessions by default, no real-time internet, probabilistic outputs)
- Why AI hallucinates and what that means for legal use
- How Louis's skill router differs from raw AI
- Exercise: three test prompts, analyze the outputs critically

**Week 2 — Prompt Engineering for Lawyers**
- The anatomy of a good legal prompt: role → task → context → constraints → output format
- Common errors: vague tasks, missing jurisdiction, missing document context
- Iterative prompting: how to refine when the first output is not right
- Exercise: rewrite 5 bad prompts into good ones; compare outputs

**Week 3 — Understanding Jurisdictional AI**
- Why jurisdiction matters to AI outputs
- How to specify your jurisdiction clearly and what changes when you do
- MENA-specific: civil law vs common law; onshore vs DIFC/ADGM; Arabic-language contracts
- Exercise: same contract question, prompt it for three different jurisdictions, compare the substantive differences in output

**Week 4 — Citation Hygiene and Verification**
- AI citation errors: how they happen, how to spot them
- Verification workflow: for each AI-cited statute or case, always verify against the primary source
- When to trust and when to verify: low-stakes vs high-stakes contexts
- Exercise: use Louis's citations engine on a real clause question; verify each citation

### Phase 2: Application

**Week 5 — Document Workflows: Drafting with AI**
- From blank page to first draft: using the Document Library and Drafting Board
- Filling variable fields intelligently; handling ambiguity
- Internal consistency checking (defined terms, cross-references)
- Exercise: draft a one-page services agreement for UAE, then for Lebanon — note the mandatory differences

**Week 6 — Document Workflows: Review and Risk Scanning**
- Uploading a contract for review: what to expect
- Reading the risk scanner output: severity tiers, what to act on first
- Distinguishing commercial risk from enforceability risk
- Exercise: upload an unknown contract, score the issues before and after the risk scan, calibrate your own judgment

**Week 7 — The Clause Library in Practice**
- Finding the right clause variant for your client's negotiating position
- Bilingual clause comparison (AR ↔ EN): how to use it, what to watch for
- Customizing library clauses without breaking them
- Exercise: negotiate a limitation-of-liability clause through three rounds using library alternates

**Week 8 — Jurisdiction Navigation**
- Using Louis for multi-jurisdictional matters
- Flagging mandatory provisions by jurisdiction
- Cross-border contract traps: choice of law, mandatory language requirements, notarization
- Exercise: spot 5 jurisdiction-specific mandatory requirements in a model MENA employment contract

**Week 9 — Legal Research with AI**
- Using AI to surface applicable legal frameworks (not to replace primary research)
- Structuring research questions for better outputs
- Combining AI research with primary-source verification
- Exercise: research the rules on non-compete clauses across UAE, KSA, and Lebanon — use Louis to surface the framework, verify two provisions against primary sources

### Phase 3: Mastery and Responsibility

**Week 10 — Advanced Techniques**
- Chain prompting: break complex tasks into sequential sub-prompts
- Using AI for negotiation preparation: what would opposing counsel argue?
- Scenario planning with AI: sensitivity analysis, outcome ranges
- Exercise: run a settlement EV analysis using [[casesim-settlement-vs-trial-ev-calculator]] and critique the assumptions

**Week 11 — Professional Ethics and AI**
- Competence obligation: most bar associations now say competence includes understanding tools you use
- Confidentiality: what data goes to the AI? what is the data-processing agreement?
- Supervision: who is responsible for AI output in a client matter?
- Conflicts: can AI introduce conflicts? how to check
- MENA-specific: LBBA, UAE Legal Affairs Department, KSA Ministry of Justice guidance (where available)

**Week 12 — AI Disclosure Obligations**
- When to disclose AI use to clients
- How to frame AI assistance in engagement letters and retainer agreements
- Court disclosure: emerging rules on AI-assisted briefs (US, UK, DIFC)
- Building your firm's AI-use policy: a starter template
- Final exercise: draft a firm AI-use policy and an AI-disclosure clause for your engagement letter

## Assessment and certification

- Each module has a short self-assessment quiz (5–10 questions)
- Weeks 6, 9, and 12 have portfolio exercises that are peer-reviewed or mentor-reviewed
- Completion certificate issued upon finishing all 12 modules and passing the Week 12 final exercise
- CPD/CLE credit: HAQQ is pursuing CLE credit recognition with select bar associations; check current status in-platform

## Caveats

- Law changes. Jurisdiction-specific content in this curriculum should be verified against current primary sources for client-matter use.
- This curriculum teaches the use of AI tools; it does not replace legal education or professional qualification.
- Ethical rules vary by jurisdiction; the Week 11 module provides a framework, not jurisdiction-specific advice on bar obligations.

## Related skills

- [[academy-justinian-tutor]]
- [[academy-legal-ai-skills-catalog]]
- [[academy-students-program]]
- [[academy-ai-feature-explainer]]
