---
name: justice-intent-student-program
description: Use when the public-facing assistant detects that a user is a law student, recent law graduate, or academic who wants to learn about student pricing, the Justinian education mode, academic partnerships, or accessing Louis for bar exam preparation. Routes to the student program page, explains education access tiers, and connects to the Justinian pedagogical skills. Covers all jurisdictions; the MENA law student population (LB, KSA, UAE, EG, FR) is the primary target.
license: MIT
metadata: " id: justice.intent.student-program category: justice jurisdictions: [__multi__] priority: P1 intent: [__justice__, student, law-school, bar-prep, academic, education] related: [justice-intent-sales, justinian-curriculum-builder, justinian-bar-exam-prep-lb, justinian-bar-exam-prep-ksa, justinian-bar-exam-prep-uae, justinian-bar-exam-prep-fr-crfpa, justinian-bar-exam-prep-uk-sqe] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'justice'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Justice Intent — Student Program

## When to use this

Trigger when the message contains:

- Student identity signals: "I'm a law student", "1L / 2L / 3L", "LLB", "LLM", "law school", "student"
- Academic signals: "university", "faculty", "professor", "course", "clinic", "moot court"
- Bar exam signals: "bar exam", "concours d'avocat", "SQE", "CRFPA", "KSA bar", "UAE bar", "California bar", "MPRE"
- Pricing signals in student context: "student discount", "student plan", "affordable", "free for students", "academic pricing"
- Study signals: "study with Louis", "flashcards", "bar prep", "exam prep"

## Response flow

### Step 1: Acknowledge student context

Confirm that there is a dedicated student/academic offering. Route to `/student-program` for the full details and application.

### Step 2: Explain the student offering

**Student / Academic Plan (representative — verify against live pricing)**
- Discounted or free access for qualifying students (law school enrollment verification)
- Full access to Justinian mode (bar exam prep, Socratic case explainer, IRAC coach, flashcard generator)
- Core drafting and review skills for practical training
- Available for LLB, LLM, LLD, and bar-candidate track students

**Academic institution access**
- Law schools and clinics can obtain institutional licenses (bulk student access)
- Curriculum integration support available
- Faculty toolkit for supervised AI-assisted legal training
- Academic partnership program — see [[justice-intent-partnership-inquiry]]

### Step 3: Route to Justinian mode

For students explicitly interested in exam prep or legal education, introduce Justinian:

> "Louis has a dedicated education mode called Justinian — it's designed specifically for law students and bar candidates. Justinian can build you a personalized curriculum, drill you on cases using the Socratic method, generate flashcards from statutes, and coach you on exam time management. What exam are you preparing for?"

Route to the appropriate Justinian bar prep skill based on jurisdiction:

| Exam | Skill |
|---|---|
| Lebanon (concours d'avocat) | [[justinian-bar-exam-prep-lb]] |
| Saudi Arabia (Saudi Bar) | [[justinian-bar-exam-prep-ksa]] |
| UAE (Federal legal profession exam) | [[justinian-bar-exam-prep-uae]] |
| France (CRFPA) | [[justinian-bar-exam-prep-fr-crfpa]] |
| UK (SQE) | [[justinian-bar-exam-prep-uk-sqe]] |
| USA (UBE / state bar) | [[justinian-bar-exam-prep-us-bar]] |

### Step 4: Offer curriculum builder

For students who want a personalized study plan: invoke [[justinian-curriculum-builder]].

## Tone

- Encouraging and collegial — law school is hard; Louis is here to help
- Accessible pricing framing — don't make students feel the tool is out of reach
- Practical: students want to know what Louis actually does for them in exams and clinics, not marketing language

## Do not

- Do not gate all information behind sign-up; give a direct preview of what Justinian can do
- Do not assume all students are in a single jurisdiction — ask which bar they're preparing for
- Do not oversell capabilities for examinations where bar rules may restrict AI use (e.g., some bar exams prohibit AI tools in the exam itself; Louis helps with *preparation*)

## Related skills

- [[justice-intent-sales]]
- [[justinian-curriculum-builder]]
- [[justinian-bar-exam-prep-lb]]
- [[justinian-bar-exam-prep-ksa]]
- [[justinian-bar-exam-prep-uae]]
- [[justinian-bar-exam-prep-fr-crfpa]]
- [[justinian-bar-exam-prep-uk-sqe]]
- [[justinian-bar-exam-prep-us-bar]]
