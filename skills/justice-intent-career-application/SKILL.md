---
name: justice-intent-career-application
description: Use when a user expresses interest in working at HAQQ/Louis, asks about open positions, wants to submit a CV, or inquires about internships. Routes the conversation to the careers portal or appropriate contact, captures role interest and background context, and maintains the HAQQ brand voice for talent interactions. Distinct from the A2J legal aid routing and commercial sales flows — this is a talent acquisition intent.
license: MIT
metadata: " id: justice.intent.career-application category: justice jurisdictions: [__multi__] priority: P1 intent: [__justice__, career, hiring, job-application, talent, internship] related: [justice-intent-book-call, justice-intent-changelog-status, justice-human-handoff] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'justice'.
Registered as a flat plugin skill.
-->


# Justice Intent — Career Application

## When this applies

This intent fires when a user's message signals that they want to join the HAQQ/Louis team — as an employee, contractor, intern, advisor, or partner. It is a **talent acquisition routing flow**.

---

## Context: HAQQ's access-to-justice mission

The "Justice" category in Louis covers HAQQ's accessibility wing — the product and mission work that makes legal services accessible to underserved populations: low-income legal aid, pro bono routing, refugee support, tenant rights, and criminal-defense pro-se support. Career applicants to HAQQ are often motivated by this mission, and the talent routing should reinforce it.

Framing for talent interactions: Louis is building the **legal AI platform for MENA and the world's underserved** — this resonates with lawyers, engineers, legal ops professionals, and mission-driven individuals who want their work to matter.

---

## Detection patterns

### Strong signals
- "I want to work at HAQQ / Louis"
- "Do you have any open positions?"
- "I'd like to apply for a job"
- "Can I send my CV / resume?"
- "Is HAQQ hiring?"
- "I'm interested in an internship"
- "How do I join the team?"

### Moderate signals (confirm before routing)
- "I'm a lawyer interested in your platform" — could be a customer, not an applicant; clarify
- "I'd like to contribute to the open-source project" — distinguish: open-source contributor vs. employee
- "I'm building something similar, can we connect?" — partnership intent, not career

---

## Behavior

### Step 1: Acknowledge warmly and confirm intent
"It sounds like you're interested in joining the HAQQ team — is that right, or were you looking for something else?"

If confirmed as career intent, proceed.

### Step 2: Capture role interest and background
Ask 1–2 quick questions (don't over-interview at this stage):

| Question | Purpose |
|---|---|
| "What kind of role interests you — engineering, legal, operations, business development, or something else?" | Route to correct team/contact |
| "Where are you based?" | Relevant for remote vs. in-person; MENA talent especially relevant |

Optional (if they volunteer):
- Years of experience / seniority
- Specific skills (Arabic + legal, LLM engineering, legal ops, growth marketing)
- Whether they're available immediately or longer-term

### Step 3: Route to careers channel
- Primary: **careers page** (e.g., `haqq.ai/careers` or equivalent)
- Secondary: **email** — `careers@haqq.ai` or equivalent (ask user to include their role interest and attach CV)
- For open-source contributors: GitHub repository (mini-hermes-the-firm) + contributor guide

### Step 4: Reinforce the mission
Close with a brief mission-aligned statement:
"HAQQ is building the legal AI platform for MENA — combining Arabic-first AI with deep jurisdictional knowledge to make legal services accessible to everyone. If that excites you, we'd love to hear from you."

---

## Role categories (as of 2024–2025 HAQQ team stage)

| Category | Typical roles | What HAQQ looks for |
|---|---|---|
| Legal | Lawyers (MENA jurisdictions), legal researchers, legal ops | Arabic + French; MENA jurisdiction experience; AI-curious; entrepreneurial |
| Engineering | LLM engineers, full-stack, backend, devops | LLM/prompt engineering; TypeScript/Node; legal domain interest |
| Product | Product managers, designers | Legal workflow understanding; user-centric design |
| Business development | Sales, partnerships, enterprise | MENA network; legal market relationships |
| Operations | Operations, finance, HR | Startup experience; MENA-based preferred |
| Content / knowledge | Legal content writers, knowledge engineers | Arabic legal writing; jurisdiction research |

---

## Open-source contributor path

If the user is interested in contributing to `mini-hermes-the-firm` (the open-source project) rather than joining as an employee:
- Point to GitHub repository
- Explain contribution process: issue triage, skill enrichment, pull requests
- Note that exceptional contributors may be invited to collaborate more deeply

---

## Do not

- Do not promise specific roles, salary ranges, or timelines — route to the official channel
- Do not screen or evaluate the applicant (that is the recruiter's role)
- Do not share internal team information or org charts
- Do not treat a career inquiry as a sales opportunity — the user is not buying

---

## Related skills

- [[justice-intent-book-call]]
- [[justice-intent-changelog-status]]
- [[justice-human-handoff]]
