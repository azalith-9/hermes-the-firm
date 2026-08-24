---
name: session
description: >
  Run a focused N-question study session on a subject — MBE, essay, or
  flashcards. Tracks performance and updates the study plan. Use when the
  user says "run me 10 questions on [subject]", "do a session on [subject]",
  "let's do 5 cards on [subject]", or wants to drill a fixed number of
  questions and have the plan adapt.
argument-hint: "<subject> <n> [--mbe | --essay | --flashcards]"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from anthropics/claude-for-legal (plugin 'law-student', Apache-2.0) for Hermes Agent.
Tool names, config paths, and /law-student:{skill} invocations were
rewritten to Hermes equivalents. Hand adjustments are tracked in
Regenerated sections are maintained upstream of this repository.
-->


# /session

1. Parse `$ARGUMENTS` — subject and N. If missing, ask:
   > What subject, and how many questions? (e.g., `Evidence 10` or `Contracts 5 --essay`.)
2. Load `~/.hermes/plugins/config/hermes-the-firm/law-student/PRACTICE.md` → jurisdiction, exam format, weak subjects.
3. Load `~/.hermes/plugins/config/hermes-the-firm/law-student/study-plan.yaml` if it exists. Read `session_history` for this subject to weight subtopics toward where the student has been weak.
4. Route by method flag:
   - `--mbe` (default for bar prep subjects): load `bar-prep-questions` skill, run N MBE-style questions. Apply jurisdiction handling (see that skill's `## Jurisdiction handling`). Label each `[UBE/majority]` or `[state-specific]`.
   - `--essay`: load `bar-prep-questions`, run N essay prompts. Grade per essay-mode rubric.
   - `--flashcards`: load `flashcards` skill, run N cards in `--drill` mode.
5. Run N questions one at a time. After each, explain right/wrong and flag rule-body when jurisdictions diverge.
6. At session end, write session results:
   - If `study-plan.yaml` exists: append to `session_history` per the schema in the `study-plan` skill.
   - If not: write to `~/.hermes/plugins/config/hermes-the-firm/law-student/session-history.yaml`.
7. Report:
   - Score: X/N (percentage)
   - Missed: list with subtopic tags
   - Weak subtopics this session
   - Pattern vs. prior sessions on this subject (if history has 2+ prior)
   - What the plan now recommends next
