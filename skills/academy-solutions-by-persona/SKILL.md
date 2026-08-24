---
name: academy-solutions-by-persona
description: Use when rendering a persona-tailored solution catalog or landing page for a specific user type — BigLaw partner, in-house counsel, solo practitioner, paralegal, law student, court clerk, journalist, or citizen with a legal question. Each persona gets a curated view of the most relevant Louis features, prompts, and entry points. Routes to this skill when user-type identification triggers a need for a contextualized product introduction rather than a generic feature tour.
license: MIT
metadata: " id: academy.solutions-by-persona category: academy jurisdictions: [__multi__] priority: P3 intent: [__customer-facing__, persona, onboarding, personalization] related: [academy-career-pitch, academy-ai-feature-explainer, academy-prompt-library-recommender, academy-use-case-explainer, academy-students-program] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'academy'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Solutions by Persona — Tailored Entry Points for Every User Type

## When to use this

Invoke when:
- A user's stated role or profile triggers a persona-specific onboarding path
- A marketing page needs persona-specific value propositions
- A sales conversation starts with "I'm a [role], what does Louis do for me?"
- A product tour needs to be calibrated to what the user actually does
- A returning user with a known role gets a new-feature notification

## Persona catalog

---

### Persona 1: BigLaw Partner / Senior Associate (Large Law Firm)

**Profile:** Billable-hour pressure, complex multi-jurisdictional matters, high volume of contract review and drafting, junior team to supervise.

**Primary pain points:**
- Every hour spent on standard-clause drafting is an hour not spent on client strategy
- Junior output quality is inconsistent; supervision takes time
- Cross-border matters require fast jurisdiction lookups the team may not have

**Top Louis entry points:**
- Risk Scanner — bulk-review counterparty drafts before assigning to junior
- Clause Library — standardize the firm's negotiating positions across matters
- Opposing Counsel Simulator — war-game the deal before negotiations begin
- Drafting Board — generate first-draft framework and have juniors refine

**Key message:** "Louis gives your team leverage. Your associates handle more with better baseline quality; you review final output, not raw drafts."

---

### Persona 2: In-House Counsel

**Profile:** Sole counsel or small legal team supporting a company. Volume of commercial contracts, limited specialist depth, time-pressured by business teams.

**Primary pain points:**
- Reviewing every vendor contract solo is unsustainable
- Business teams want instant answers; in-house lawyers cannot always be instant
- Non-standard jurisdictions (e.g., a MENA company contracting with an East African partner) create coverage gaps

**Top Louis entry points:**
- Contract Risk Scanner — triage incoming vendor contracts before reading in full
- Playbook integration — encode the company's standard positions so Louis applies them automatically
- Jurisdiction knowledge base — quick-reference answers to "what does UAE law say about X?"
- Document Workspace — collaborate with business stakeholders and track approvals

**Key message:** "Louis is the extra set of eyes that is always available. You direct the strategy; Louis handles the first-pass review and the boilerplate."

---

### Persona 3: Solo Practitioner

**Profile:** Single-lawyer practice, generalist or specialist, resource-constrained, client-direct.

**Primary pain points:**
- No junior to delegate to; every task lands on the same desk
- Cannot afford specialist subscription stacks
- Client communications and admin compete for the same hours as substantive legal work

**Top Louis entry points:**
- Document Library + Drafting Board — produce first drafts in minutes, not hours
- Risk Scanner — do a credible contract review without a second pair of eyes
- Client-facing plain-language tool — explain legal documents to clients without a lengthy email
- Prompt Library — pre-built prompts for the most common solo-practice tasks (retainer letters, demand letters, NDA drafts)

**Key message:** "Louis is your associate, your library, and your research tool — all in one. You do the legal judgment; Louis does the groundwork."

---

### Persona 4: Paralegal / Legal Operations

**Profile:** Supports a team of lawyers. High volume of administrative and quasi-legal tasks: document management, extraction, formatting, deadline tracking.

**Primary pain points:**
- Document extraction and summarization is repetitive and error-prone when done manually
- Lawyers expect consistent, well-formatted output; producing it takes more time than it should
- Limited legal knowledge makes it hard to know what to flag vs. what to pass through

**Top Louis entry points:**
- Contract extraction — pull parties, dates, key obligations, renewal dates from any document
- Document summary generator — plain-language summary for file management
- Consistency checker — ensure all defined terms are used correctly; flag cross-reference errors
- Checklist generator — produce a transaction closing checklist from a term sheet

**Key message:** "Louis handles the extraction, formatting, and consistency work automatically — so you spend your time on tasks that require human judgment."

---

### Persona 5: Law Student / Bar Candidate

**Profile:** Developing foundational legal reasoning skills; preparing for exams or bar admission; no live client matters.

**Primary pain points:**
- Abstract legal concepts are hard to internalize without application
- Case brief writing is slow; feedback is infrequent
- Bar exam pressure with limited coaching access

**Top Louis entry points:**
- Justinian tutor — IRAC coaching, case brief generation, bar exam question banks
- Moot court rehearsal — practice oral argument with a simulated bench
- Learn Legal with AI curriculum — structured 12-week path to practical AI proficiency
- Fact pattern builder — generate realistic scenarios to practice on

**Key message:** "Louis is your 24/7 study partner — Socratic, non-judgmental, and always available for one more practice question."

---

### Persona 6: Court Clerk / Judicial Support

**Profile:** Administrative and para-legal support for a court. High document volume, procedural accuracy requirements.

**Primary pain points:**
- Document routing and classification is manual and time-consuming
- Procedural deadline tracking across many cases
- Consistency of document formatting and citation style

**Top Louis entry points:**
- Document classification and routing
- Procedural deadline extractor
- Judgment summarization (for public-facing court communications)

**Note:** Court clerk use cases may involve restrictions on AI use in certain jurisdictions; verify local judicial AI policy before deployment.

---

### Persona 7: Journalist / Researcher Covering Legal Topics

**Profile:** Not a lawyer, but working with legal documents, court filings, or regulatory texts.

**Primary pain points:**
- Legal documents are difficult to read without specialized training
- Cannot afford a lawyer for every document review
- Need to understand what a document means, not get legal advice

**Top Louis entry points:**
- Plain-language explainer — "explain this contract clause in plain English"
- Document summarizer — "what are the key points of this court filing?"
- Jurisdiction explainer — "what does this regulation mean in practice?"

**Important:** outputs for non-lawyer users are explanations only, not legal advice. Always include the standard disclaimer.

---

### Persona 8: Citizen with a Legal Question

**Profile:** Individual without legal training, facing a legal situation (housing dispute, employment issue, consumer complaint, family matter).

**Primary pain points:**
- Lawyers are expensive; basic legal information is hard to find
- Legal documents they receive are incomprehensible
- Uncertainty about what their rights are

**Top Louis entry points:**
- Plain-language document explainer
- Know-your-rights information (jurisdiction-specific, general principles)
- Referral to lawyer / legal aid (for matters requiring professional advice)

**Important:** Louis provides legal information and tools, not legal advice. For any matter requiring legal action, users should be directed to a qualified lawyer. Outputs for this persona should always include a clear disclaimer and a referral path.

---

## Related skills

- [[academy-career-pitch]]
- [[academy-ai-feature-explainer]]
- [[academy-prompt-library-recommender]]
- [[academy-use-case-explainer]]
- [[academy-students-program]]
