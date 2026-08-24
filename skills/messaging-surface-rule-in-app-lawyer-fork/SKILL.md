---
name: messaging-surface-rule-in-app-lawyer-fork
description: Use when writing or reviewing in-app copy, onboarding messages, feature tooltips, upsell prompts, or system notifications displayed to users who have been identified or self-declared as licensed legal professionals. The lawyer fork of in-app messaging uses professional framing, productivity claims, and feature positioning appropriate for a practitioner audience — distinct from the consumer fork. Applied by messaging-compliance-checker for any in-app asset tagged to the professional persona.
license: MIT
metadata: " id: messaging.surface-rule.in-app-lawyer-fork category: messaging jurisdictions: [__multi__] priority: P2 intent: [messaging, in-app, lawyer, professional, UX-copy, onboarding] related: [messaging-compliance-checker, messaging-allowed-claims-lawyer, messaging-banned-claims-lawyer, messaging-surface-rule-in-app-non-lawyer-fork, onboarding-b2c-vs-b2b-fork] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'messaging'.
Registered as a flat plugin skill.
-->


# Messaging — Surface Rule: In-App Lawyer Fork

## When this applies

Once a user has been classified as a **legal professional** (via persona quiz, email domain, LinkedIn import, or manual declaration during onboarding — see [[onboarding-b2c-vs-b2b-fork]]), all in-app copy shown to that user follows the lawyer-fork rules defined here. This covers:

- Welcome and onboarding screens (post-persona detection)
- Feature discovery tooltips and walkthroughs
- Empty-state prompts in the drafting board, document workspace, and skills library
- Upsell and plan-upgrade prompts
- System notifications and status messages
- Error messages and escalation prompts
- Settings page descriptions

The lawyer fork is **not** a relaxation of compliance requirements — it is a different voice, a different vocabulary, and a different value frame. Banned claims for lawyers still apply in full per [[messaging-banned-claims-lawyer]].

---

## Behavior — The Professional Voice

In-app copy in the lawyer fork assumes the user:
- Holds a law degree and is practicing or has recently practiced
- Understands legal concepts and does not need them explained from scratch
- Has high expectations of accuracy, jurisdictional coverage, and citation quality
- Is evaluating the product against their existing workflow and billing model
- Cares about professional responsibility and will not use a tool that creates malpractice risk

Copy must reflect these assumptions. Do not over-explain basic legal concepts. Do not use consumer-style "we make law easy!" messaging. Do not imply the user is not competent.

---

## Copy Rules by In-App Location

### Onboarding / Welcome Screen

| Element | Lawyer fork rule |
|---------|-----------------|
| Welcome headline | Professional register: "Welcome to your legal workbench." / "Your AI-powered research and drafting partner." |
| Sub-copy | State coverage and capability: "Multi-jurisdiction coverage across LB, KSA, UAE, DIFC, ADGM, UK, and more." |
| First action prompt | Task-oriented: "Start with a document review" / "Draft your first contract" / "Research a legal question" |
| Disclaimer | Brief but present: "Louis assists with legal research and drafting; lawyer review and judgment remain essential." |

### Feature Tooltips and Discovery

- Lead with the task the feature enables, not the technology behind it
- "Review this contract against standard market terms — Louis flags deviations." (not "AI-powered contract analysis")
- Reference jurisdiction-specific capabilities where relevant: "KSA employment contracts — including Saudization compliance"
- Use professional vocabulary: "liability cap", "indemnification", "governing law", "non-compete enforceability" — assume the user understands these

### Drafting Board Empty State

- "Start a new matter — Louis will draft the first pass." (not "Get started with your legal work!")
- "Assign documents to this matter, set the jurisdiction and party positions, and Louis generates a workflow."

### Upsell / Plan Upgrade Prompts

- Frame around professional capability expansion, not cost savings
- "Upgrade to Pro for eFirm features: firm playbooks, matter templates, and team assignment."
- "Your current plan includes single-jurisdiction research. Pro unlocks multi-jurisdiction comparison across LB, KSA, UAE, DIFC, ADGM, and UK."
- Never use "save money" framing in lawyer-fork upgrade prompts — the professional audience responds to capability, not cost

### Error and Escalation Messages

- Professional register: "This analysis is based on publicly available legal sources. For binding legal opinions or court filings, verify against primary sources."
- Do not use apologetic consumer-style error messages ("Oh no! Something went wrong.")
- Use precise, actionable language: "Document type not recognized — please select the applicable jurisdiction and contract category."

---

## Banned Patterns in Lawyer Fork

These patterns are blocked specifically for the lawyer fork (in addition to the general banned claims):

- Consumer-style excitement: "You're going to love this!" (wrong register)
- Over-simplification: "Legal made easy!" (condescending to a professional)
- Displacement framing: "Handle this without an associate" (see [[messaging-banned-claims-lawyer]])
- Fee-threat language: "Save on legal costs" (attacks the lawyer's billing model)
- Competence challenges: "Louis does this better than manual review" (threatening to professional identity)

---

## Examples

**Strong lawyer-fork in-app copy:**
> "Your NDA is ready for review. Louis flagged 3 deviations from DIFC market standard and suggested revisions. You retain full editorial control."

**Weak in-app copy (avoid on lawyer fork):**
> "Wow, Louis just wrote your NDA! Check it out!"

**Strong empty-state prompt:**
> "No documents in this matter yet. Upload a contract or generate a first draft — specify jurisdiction, parties, and key commercial terms."

**Weak empty-state (avoid):**
> "Get started! Louis makes contracts easy."

---

## Related skills

- [[messaging-compliance-checker]]
- [[messaging-allowed-claims-lawyer]]
- [[messaging-banned-claims-lawyer]]
- [[messaging-surface-rule-in-app-non-lawyer-fork]]
- [[onboarding-b2c-vs-b2b-fork]]
- [[onboarding-persona-detection-questions]]
