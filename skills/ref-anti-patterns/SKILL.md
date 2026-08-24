---
name: ref-anti-patterns
description: "Use as a reference guide listing the most common anti-patterns in legal AI use — behaviors that consistently produce low-quality outputs, create risk, or undermine the value of AI assistance. This is a meta-skill: it applies across all categories of legal AI work. Consult when a user appears to be making one of these mistakes, when output quality is unexpectedly poor, or when onboarding new users to the platform."
license: MIT
metadata: " id: ref.anti-patterns category: ref priority: P1 intent: [__ref__, anti-patterns, quality, legal-ai, best-practices] related: - ref-verification - ref-privilege-layers - ref-long-documents-50pp - ref-skill-authoring - heuristic-always-state-jurisdiction-first source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'ref'.
Registered as a flat plugin skill.
-->


# Reference — Anti-Patterns in Legal AI Use

## Scope

This reference catalogs the anti-patterns that most frequently degrade legal AI output quality, create compliance risk, or waste practitioner time. Each entry states the problem, explains why it occurs and what harm it causes, and gives the corrective action.

Use this reference:
- When reviewing AI output that seems lower quality than expected — check if an anti-pattern was used
- During onboarding of new legal team members to the platform
- When authoring or reviewing new skills — ensure the skill design does not permit or encourage any of these patterns

---

## Anti-Pattern 1 — Over-trusting AI outputs without verification

**The pattern:** Accepting AI-generated legal analysis, contract language, or citations and using them without checking the underlying sources.

**Why it happens:** AI outputs are fluent, structured, and authoritative-sounding. The cognitive effort of verification feels redundant after receiving a polished output.

**The harm:**
- Fabricated statute article numbers and case citations appear in filed pleadings, client memos, and contracts — creating professional liability for the lawyer
- Outdated law: AI training data has a cutoff; post-cutoff amendments are missed
- Jurisdiction errors: AI may correctly state the law for one jurisdiction and silently apply it to another

**Corrective action:**
- Apply [[ref-verification]] before sending any AI output to a client, court, or counterparty
- Every cited statute must be checked against the official source
- Every cited case must be verified to exist with the quoted proposition
- Treat AI outputs as a drafting aid, not a finished work product

---

## Anti-Pattern 2 — Sending privileged content to AI tools without redaction

**The pattern:** Pasting full client documents — emails, memos, litigation strategy documents — into a shared AI platform without considering privilege, confidentiality, or data protection implications.

**Why it happens:** Speed and convenience. Pasting the full document feels like the most efficient way to get a useful answer.

**The harm:**
- Attorney-client privilege may be waived if privileged communications are shared with a third-party AI provider (jurisdiction-specific — US, UK, and DIFC courts treat this differently; see [[ref-privilege-layers]])
- Client confidentiality obligations under applicable professional conduct rules (UAE Bar Association, KSA Ministry of Justice, DIFC Authority, SRA in UK) may be breached
- Data protection violations: sharing personal data of clients or third parties with an AI system without proper authorization and a DPA in place

**Corrective action:**
- Redact identifying information before submitting to any AI tool that is not covered by a firm DPA
- Maintain separate workflows for privileged / sensitive documents vs. research and drafting tasks
- Confirm that the AI platform provider has signed a DPA and that data processing is authorized under applicable data protection law
- For MENA clients: be aware that some jurisdictions have heightened sensitivity to cross-border data flows; confirm data residency of the AI platform

---

## Anti-Pattern 3 — Using AI as the lawyer (UPL risk)

**The pattern:** Providing AI-generated legal analysis or documents directly to clients as if they were lawyer-produced advice, or allowing AI to make legal decisions that require professional judgment.

**Why it happens:** The AI output often looks and reads like professional legal work. It is tempting to send it directly.

**The harm:**
- Unauthorized Practice of Law (UPL) risk: non-lawyers forwarding AI legal advice as legal advice may violate UPL rules in most jurisdictions
- Professional negligence: lawyers who outsource professional judgment to AI without exercising independent review may face liability for AI errors
- Regulatory risk: bar associations in UAE, KSA, Lebanon, Egypt, and DIFC/ADGM all regulate who may provide legal advice; AI tools do not have a law license

**Corrective action:**
- AI is a drafting and research tool; the lawyer exercises professional judgment and reviews and stands behind the output
- Every client communication must reflect the lawyer's independent review and conclusion
- For non-lawyers using AI: clearly frame all outputs as "for informational purposes only — consult qualified legal counsel"

---

## Anti-Pattern 4 — Skipping jurisdiction verification

**The pattern:** Running an analysis without specifying the jurisdiction, or accepting an AI analysis that silently defaults to US law (or another dominant-data-set jurisdiction).

**Why it happens:** The user may assume the AI knows the jurisdiction from context, or may not realize that the AI has defaulted to a different jurisdiction.

**The harm:**
- Wrong law applied: a UAE employment analysis written using US FMLA principles is not just unhelpful — it is actively misleading
- MENA jurisdictions are especially underrepresented in AI training data; without explicit direction, AI outputs frequently default to US or UK law even for clearly MENA-context queries

**Corrective action:**
- Always invoke [[heuristic-always-state-jurisdiction-first]] at the start of any substantive legal task
- If the output does not reference the correct jurisdiction's statutes and cases, stop and re-prompt with explicit jurisdiction instruction
- When the jurisdiction is uncertain, say so and ask the user before proceeding

---

## Anti-Pattern 5 — Pasting case citations without checking they exist

**The pattern:** Including AI-generated case citations in legal arguments, memos, or briefs without verifying they are real cases with the propositions attributed to them.

**Why it happens:** Case citations look authoritative and specific. They feel like a strong foundation for an argument.

**The harm:**
- Courts have sanctioned lawyers for filing briefs with fabricated AI citations (well-documented in US federal courts post-2023)
- Client embarrassment and firm reputational damage
- In MENA proceedings: citation of a non-existent judgment before a UAE or KSA court could constitute a serious professional misconduct violation

**Corrective action:**
- Every case citation must be verified before use: confirm the case exists, the court decided it, and the quoted proposition is accurate
- Use [[ref-verification]] as a mandatory checklist step
- For MENA cases: verify via official court websites (DIFC Courts, ADGM Judiciary) or subscription databases (LexisNexis MENA, Westlaw MENA); KSA and UAE onshore cases are not always publicly available

---

## Anti-Pattern 6 — Treating AI as a substitute for client conversation

**The pattern:** Using AI-generated analysis to answer client questions without first understanding the client's specific situation, context, and priorities.

**Why it happens:** AI can produce a plausible answer faster than a client intake call. It is tempting to skip the intake.

**The harm:**
- Generic analysis does not address the client's actual problem
- Material facts that would change the analysis are missed
- Client trust is undermined when the advice turns out to be irrelevant to their specific situation
- In MENA: cultural context, business relationship dynamics, and sector-specific constraints often affect the legal strategy in ways that cannot be inferred from a generic fact pattern

**Corrective action:**
- AI is most valuable after client intake, not before; use the intake to gather the specific facts, then use AI to analyze those facts
- Use [[conversation-clarifying-questions]] to capture necessary inputs before invoking substantive analysis skills
- The lawyer-client relationship is the product; AI is the production tool

---

## Anti-Pattern 7 — Long, unstructured prompts

**The pattern:** Sending AI a prompt that mixes multiple questions, includes background context buried in unformatted text, and asks for multiple outputs in a single instruction.

**Why it happens:** The user drafts the prompt as they think, rather than structuring it for optimal AI processing.

**The harm:**
- AI will address some questions and silently omit others
- Priority of instructions is unclear; the AI prioritizes based on position in the prompt, not importance to the user
- Output is a jumbled mix of answers that is harder to use than if the questions had been separated

**Corrective action:**
- One skill or task per prompt; if multiple outputs are needed, run them as separate prompts in sequence
- Place the most important instruction first (the AI anchors on early instructions more reliably)
- Use the skill's required inputs structure to front-load the necessary information
- Separate context (background facts) from instruction (what to do with the facts)

---

## Anti-Pattern 8 — Repeating the same prompt expecting different results

**The pattern:** Running the same prompt multiple times hoping that a different run will produce a better output, without changing the instructions or inputs.

**Why it happens:** The user is dissatisfied with the output but does not know how to improve the prompt.

**The harm:**
- Wasted tokens and time
- Slight variations in AI outputs are stochastic, not calibrated; repetition does not systematically improve quality

**Corrective action:**
- Diagnose why the output was unsatisfactory: wrong jurisdiction? missing input? misunderstood intent? wrong skill invoked?
- If the output is too general: add specifics (jurisdiction, party type, industry, specific clause to analyze)
- If the output used the wrong framework: explicitly correct it ("apply UAE Federal Law, not US law") and re-run
- If the output is too long: ask for a shorter version with a specific structure
- If an anti-pattern from this list was likely the cause: fix that first, then re-run

---

## How to use this reference

Consult this reference proactively:
- Before sending AI output to a client or court: run through anti-patterns 1, 5, and 3
- When setting up a new user: walk through all 8 patterns in the onboarding session
- When authoring new skills: ensure the skill template prompts users for jurisdiction (prevents anti-pattern 4) and instructs them to verify (prevents anti-patterns 1 and 5)

## Related skills

- [[ref-verification]]
- [[ref-privilege-layers]]
- [[ref-long-documents-50pp]]
- [[ref-skill-authoring]]
- [[heuristic-always-state-jurisdiction-first]]
- [[heuristic-no-us-style-boilerplate-in-civil-law-jx]]
