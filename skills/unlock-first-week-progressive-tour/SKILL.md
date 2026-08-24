---
name: unlock-first-week-progressive-tour
description: Use when a newly registered user is in their first seven days on the platform and needs a structured, low-friction introduction to core capabilities. This skill governs the day-by-day progressive tour that walks all personas from their first chat through matter management, the clause library, and the NPS prompt, delivered via in-app cards and optional email drip.
license: MIT
metadata: " id: unlock.first-week-progressive-tour category: unlock jurisdictions: [__multi__] priority: P2 intent: [__customer-facing__, onboarding, progressive-tour, first-week] related: - unlock-feature-discovery-by-persona - unlock-skill-of-the-day - unlock-power-user-shortcuts source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'unlock'.
Namespaced as louis-<category>-<skill> on registration.
-->


# First-Week Progressive Tour

## Purpose

The first seven days determine whether a new user builds a habit or churns. The progressive tour is a lightweight, day-anchored sequence of nudges that guide users from their first interaction to a point where they have experienced the platform's most habit-forming capabilities. It does not replace persona-specific discovery ([[unlock-feature-discovery-by-persona]]); it sits beneath it as the universal baseline.

## Tour structure

| Day | Milestone | Delivery channel |
|-----|-----------|-----------------|
| 1 | First chat — ask any legal question | In-app welcome card |
| 2 | Upload first document — review or summarize it | In-app prompt on session start |
| 3 | Try matter management — create your first matter folder | In-app tooltip on sidebar |
| 5 | Explore the clause library — search for a clause type | In-app contextual card |
| 7 | NPS prompt — "How likely are you to recommend Louis?" | In-app modal + optional email |

## Day-by-day guidance

### Day 1 — First chat
The goal is a successful, satisfying first answer. The onboarding flow pre-seeds a suggested question based on the user's persona. Do not make the user figure out what to ask.
- Example suggestion for associate: "Draft a short NDA for a freelance engagement."
- Example suggestion for in-house: "Summarize the key risks in this vendor contract."
- Example suggestion for student: "Explain the elements of a valid contract under Lebanese law."

Completion signal: user submits their first message and receives a response they did not dismiss.

### Day 2 — First document upload
Introduce the document workspace. The nudge appears at session start on day 2 if the user has not yet uploaded a file.
- Card copy: "Have a contract to review? Upload it and I'll pull out the key risks in seconds."
- Support PDF, DOCX, and image uploads (scanned pages are handled by [[voice-multimodal-scanned-pdf-handler]]).

Completion signal: user uploads any file.

### Day 3 — Matter management
Surface the matter sidebar or matter-creation flow. Many users do not know this exists unless prompted.
- Card copy: "Keep your work organized. Create a matter to group your documents, notes, and drafts."
- For consumer users, substitute: "Start a case file to keep track of your question and any follow-ups."

Completion signal: user creates at least one matter.

### Day 5 — Clause library
Surface the clause library search. This is where legal professionals discover depth.
- Card copy: "Looking for a standard clause? Search thousands of lawyer-reviewed clauses by type, jurisdiction, or topic."
- For student users, substitute with statute flashcard feature.

Completion signal: user performs at least one clause search or flashcard generation.

### Day 7 — NPS prompt
After one week, ask for feedback. Keep it short: one score, one open text box.
- Deliver in-app first; if the user closes without responding, follow up via email the same day (for users who opted into email).
- Do not ask for NPS if the user has had fewer than three interactions — the score will be meaningless.

Completion signal: NPS submitted or explicitly dismissed.

## Delivery mechanics

### In-app cards
- Position at session start, not mid-task.
- Cards are dismissible with a single click. After two dismissals of the same card, suppress it and mark the milestone skipped.
- Do not stack multiple cards. One active tour card at a time.

### Email drip (opt-in only)
- Day 1 email: welcome + first-task prompt (sent 2 hours after registration if no first chat yet).
- Day 3 email: "Did you know?" — matter management introduction.
- Day 7 email: NPS request (fallback if in-app was dismissed).
- All emails are plain-text-style, short (under 200 words), and include a direct deep-link into the platform action.

## Skip and override conditions

- If the user completes a milestone organically before its scheduled day, mark it complete and advance.
- If the user's persona is explicitly set to "consumer / Louis Twin", skip the matter management and clause library steps and substitute the consumer-specific variant.
- Do not resurface completed milestones.

## Success metrics

| Metric | Target |
|--------|--------|
| Day-1 first chat completion | > 80% |
| Day-2 first upload | > 50% |
| Day-3 matter creation | > 40% |
| Day-7 NPS submission | > 35% |
| 7-day retention (any session) | > 55% |

## Related skills

- [[unlock-feature-discovery-by-persona]]
- [[unlock-skill-of-the-day]]
- [[unlock-power-user-shortcuts]]
- [[unlock-template-of-the-week]]
