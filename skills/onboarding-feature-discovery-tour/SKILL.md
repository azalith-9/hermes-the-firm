---
name: onboarding-feature-discovery-tour
description: Use when a new user signs in to a legal AI assistant for the first time and the system must guide them through the product's core capabilities via a brief, optional, skippable modal tour. Defines the exact step sequence, each step's purpose and copy, the trigger conditions, the anti-patterns that break user trust (locking UI, repeating after dismissal), and how the tour integrates with the longer-arc progressive onboarding journey.
license: MIT
metadata: " id: onboarding.feature-discovery-tour category: onboarding priority: P1 intent: [onboarding, feature-discovery, tour, first-sign-in, UX, modal] related: [onboarding-b2c-vs-b2b-fork, onboarding-empty-state-prompts, onboarding-first-prompt-suggestion-by-persona, onboarding-persona-detection-questions, onboarding-template-of-the-day] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'onboarding'.
Registered as a flat plugin skill.
-->


# Onboarding — Feature Discovery Tour

## When this applies

The feature discovery tour is a **lightweight modal sequence** shown to users during their first sign-in. It is the synchronous, in-session orientation — distinct from the longer-arc progressive onboarding (see [[onboarding-template-of-the-day]] and the week-one progressive tour). Its goal is to give users enough context to take their first meaningful action within 60–90 seconds.

This skill defines when to show the tour, what each step contains, and how to do it without creating the friction patterns that make users abandon onboarding.

---

## Trigger Conditions

| Trigger | Show tour? | Notes |
|---------|-----------|-------|
| First sign-in (no prior session) | Yes (offer; skippable) | Default trigger |
| Re-activation after 7+ days inactive | Yes (abbreviated version) | Show only new-feature steps |
| New major feature launch | Yes (feature-specific mini-tour) | Trigger only for users who have not used the new feature |
| Returning user with completed tour | No | Do not repeat |
| Mid-session interruption | Never | Never trigger the tour while a user is actively working |

---

## Tour Steps — Modal Sequence

The tour is a **7-step modal sequence**. Each modal is skippable at any point. Progress indicator (1 of 7) is shown throughout.

### Step 1 — Welcome

**Modal title:** "Welcome to Louis."

**Body copy (consumer fork):**
> "Louis is your legal AI assistant. Ask about your rights, review a contract, or get a plain-language explanation of any legal situation. Louis provides legal information — for legal advice, you'll still want a qualified lawyer. Let's take a quick look at what you can do."

**Body copy (lawyer fork):**
> "Welcome to your legal workbench. Louis supports research, drafting, review, and multi-jurisdiction analysis. Your professional judgment drives every output. Let's show you what's available."

**CTA:** "Next →" / "Skip tour"

### Step 2 — Composer Demo

**Modal title:** "Start with a question."

**Body copy:**
> "Type anything — a question about your rights, a document to review, or a drafting task. Louis will figure out what you need."

**Interactive element (optional):** A pre-filled sample prompt that the user can click to see a simulated response: "What does this non-compete clause mean?"

**CTA:** "Next →" / "Try it now" (exits tour and opens the composer)

### Step 3 — Document Workspace

**Modal title:** "Understand any document."

**Body copy:**
> "Upload a contract, lease, or legal document. Louis reads every clause, flags what matters, and explains it in plain language."

**Visual:** Screenshot of the document workspace with a sample contract and annotated clause flagging

**Consumer fork addition:** "Always review key findings with a lawyer before signing."

**CTA:** "Next →"

### Step 4 — Skills Library

**Modal title:** "973 specialised skills."

**Body copy:**
> "Louis routes every request to the right specialised skill — contract drafting, employment law, company formation, dispute resolution, and more. Covering Lebanon, UAE, KSA, DIFC, ADGM, and beyond."

**Visual:** Skills library grid showing a sample of categories

**CTA:** "Next →"

### Step 5 — Customize

**Modal title:** "Make it yours."

**Body copy:**
> "Set your jurisdiction, role, and language preferences. For law firms, configure firm playbooks and matter templates."

**CTA:** "Next →" / "Customize now" (exits tour and opens settings)

### Step 6 — Drafting Board (Lawyer fork only — skip for consumer fork)

**Modal title:** "For complex matters: the Drafting Board."

**Body copy:**
> "Manage multi-step legal workflows — from first research to final draft. Assign documents to matters, track revisions, and deliver organised output."

**CTA:** "Next →"

### Step 7 — Ready

**Modal title:** "You're ready."

**Body copy (consumer fork):**
> "Start by asking a question, uploading a document, or choosing from the prompts below. Louis is here when you need it."

**Body copy (lawyer fork):**
> "Start by uploading a document for review, or jump into the drafting board for a new matter."

**CTAs:** "Start asking →" (opens composer) / "Upload a document" (opens doc workspace)

---

## Anti-Patterns

The following patterns actively harm user trust and must be avoided:

| Anti-pattern | Why it fails | What to do instead |
|---|---|---|
| Locking the UI behind the tour | Traps users; creates resentment | Always provide "Skip" on every step |
| Repeating the tour after the user dismissed it | Disrespects the user's choice | Store dismissal in user profile; never re-show on the same user |
| Showing the tour mid-task | Interrupts the user; destroys trust | Only show on session start, never mid-session |
| Making steps too long | Users stop reading; skip rate spikes | Each modal: 2–4 sentences max |
| No progress indicator | Users don't know how long the tour is | Always show step N of total |
| Auto-advancing without reading | Feels dismissive | Only advance on explicit click; no timers |

---

## Tour Analytics

Track these metrics to optimise the tour:
- **Skip rate per step**: where users bail out (high skip at step 2 → step 2 is too long or unclear)
- **Completion rate**: % of users who reach step 7
- **Post-tour action rate**: % of tour completers who take a meaningful action within 5 minutes
- **Tour-skip to first-action time**: how long users who skip the tour take to complete a first action vs those who completed it

A well-designed tour should have >60% completion or >80% of skippers still taking a first action within 10 minutes.

---

## Integration with Progressive Onboarding

The feature discovery tour is **step zero** of a longer onboarding arc. After the tour:
- [[onboarding-template-of-the-day]] activates for the first week (daily micro-prompts)
- [[onboarding-first-prompt-suggestion-by-persona]] provides the next prompt after the tour completes
- The week-one progressive tour (referenced as `unlock.first-week-progressive-tour`) surfaces features progressively as the user is ready for them — not all at once

---

## Related skills

- [[onboarding-b2c-vs-b2b-fork]]
- [[onboarding-empty-state-prompts]]
- [[onboarding-first-prompt-suggestion-by-persona]]
- [[onboarding-persona-detection-questions]]
- [[onboarding-template-of-the-day]]
