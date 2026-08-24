---
name: onboarding-persona-detection-questions
description: Use when a new user must be guided through a brief onboarding quiz to determine their persona for a legal AI assistant. Defines the exact 3–4 quiz questions, the valid answer options, the mapping from answers to personas, and the anti-patterns that cause quiz abandonment. The quiz output feeds the B2C vs B2B fork, the starter prompt selection, and the persona setting in the user profile. Never ask more than 4 questions; always offer a skip path.
license: MIT
metadata: " id: onboarding.persona-detection-questions category: onboarding priority: P0 intent: [onboarding, persona, quiz, detection, B2C, B2B, routing] related: [onboarding-b2c-vs-b2b-fork, onboarding-first-prompt-suggestion-by-persona, onboarding-empty-state-prompts, onboarding-feature-discovery-tour] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'onboarding'.
Registered as a flat plugin skill.
-->


# Onboarding — Persona Detection Questions

## When this applies

The persona detection quiz runs when:
1. A new user has completed sign-up and no high-confidence automatic signals have determined their persona (see [[onboarding-b2c-vs-b2b-fork]])
2. A returning user explicitly requests to re-take the quiz
3. After 7 days of using the product without completing the quiz (re-surface prompt)

The quiz is **optional and skippable** at every step. Completing it unlocks persona-appropriate defaults, but the product is fully functional without quiz completion. Never make the quiz a mandatory gate.

---

## The Questions

### Question 1 — Role (Required)

**Question text:** "What best describes your role?"

| Option | Mapped persona |
|--------|---------------|
| Lawyer / Solicitor / Advocate | → `associate` (refined by Q4) |
| In-house counsel / Legal ops | → `in-house-counsel` |
| Law student | → `law-student` |
| Business owner / Founder / Manager | → `sme-founder` |
| Other / Individual / Not sure | → `louis-twin` (consumer default) |

**Arabic options (for MENA locale):**
- محامي / مستشار قانوني → lawyer path
- مستشار قانوني داخلي → in-house path
- طالب قانون → law-student path
- صاحب عمل / مؤسس → sme-founder path
- أخرى → louis-twin

### Question 2 — Primary Jurisdiction (Required)

**Question text:** "Which jurisdiction do you work in most often?"

| Option | Notes |
|--------|-------|
| Lebanon (LB) | |
| Saudi Arabia (KSA) | |
| UAE — onshore | |
| UAE — DIFC | |
| UAE — ADGM | |
| Other GCC (Qatar QFC, Bahrain, Kuwait, Oman) | |
| Egypt | |
| France / OHADA | |
| UK | |
| US | |
| Multiple / International | Triggers multi-jurisdiction feature set |
| Not sure | Default to UAE |

**Why this matters:** Jurisdiction selection drives which knowledge bases are loaded, which default governing law appears in drafting tools, and which jurisdiction-specific disclaimers surface in high-stakes interactions.

### Question 3 — Primary Use Case (Required)

**Question text:** "What will you use Louis for most?"

| Option | Feature emphasis |
|--------|-----------------|
| Drafting documents / contracts | Drafting board + template library |
| Reviewing / analysing documents | Document workspace + review tools |
| Legal research | Research features + citation tools |
| Learning / studying law | Justinian / educational features |
| Understanding my own situation | Consumer-oriented information tools |

### Question 4 — Firm or Organisation Size (Conditional — shown only if Q1 = Lawyer)

**Question text:** "How large is your firm or legal team?"

| Option | Persona refinement | Features pitched |
|--------|-------------------|-----------------|
| Solo practitioner | `associate` — solo mode | Individual Pro tier; personal playbooks |
| Small firm (2–10 lawyers) | `associate` | eFirm Starter; team features |
| Medium firm (11–100 lawyers) | `partner` | eFirm Business; team management; analytics |
| Large firm (100+ lawyers) | `partner` | Enterprise; custom deployment |
| In-house (any team size) | `in-house-counsel` | Compliance tools; vendor management |

---

## Persona Output Mapping

| Q1 result | Q4 result | Persona assigned |
|-----------|-----------|-----------------|
| Lawyer | Solo | `associate` |
| Lawyer | Small firm | `associate` |
| Lawyer | Medium/Large firm | `partner` |
| Lawyer | (skipped) | `associate` |
| In-house counsel | — | `in-house-counsel` |
| Law student | — | `law-student` |
| Business owner | — | `sme-founder` |
| Other / skip | — | `louis-twin` |

### Automatic inference (no quiz)

These signals override or pre-empt the quiz result:
- Email domain `@firmname.com` → start with `associate` assumption; quiz if possible
- LinkedIn import: title contains "lawyer" / "avocat" / "محامي" / "solicitor" / "counsel" → lawyer path
- Corporate card payment → likely B2B; quiz with B2B defaults pre-selected
- Referral from law firm partnership page → B2B; Q4 may be pre-filled by the referral URL

---

## Anti-Patterns

| Anti-pattern | Why it fails | Fix |
|---|---|---|
| More than 4 questions | Drop-off rate increases sharply after question 3; after 4 it's significant | Cap at 4 questions; move nice-to-have questions to settings page |
| No "Skip" option | Users feel trapped; some abandon entirely | Provide "Skip" at every question; "Skip all" at the start |
| Sensitive or irrelevant questions | Gender, income, age, nationality → irrelevant to product persona and feel invasive | Never ask; remove if discovered in any variant |
| Mandatory quiz before first use | Treats onboarding as a barrier, not a guide | Allow direct product access; quiz is optional |
| Long question text | Users don't read; tap the first option | Each question ≤ 10 words; each option ≤ 4 words |
| No progress indicator | Users don't know how many questions remain | Show "Q1 of 4" or a progress bar |

---

## Output and Storage

On quiz completion or skip:

1. **Persona set in user profile:** persisted in the user's account; displayed in Settings as current persona
2. **Jurisdiction preference set:** used as default in drafting and research features
3. **B2C / B2B fork determined:** persona drives fork per [[onboarding-b2c-vs-b2b-fork]]
4. **Starter prompts loaded:** [[onboarding-first-prompt-suggestion-by-persona]] uses the persona output
5. **Router context updated:** the skill router reads persona preference for routing decisions

On skip (no quiz completion):
- Persona defaults to `louis-twin` (B2C)
- Jurisdiction defaults to "Not set" (user is prompted on first jurisdiction-requiring task)
- Quiz re-surface prompt set for 7 days after first sign-in

---

## Re-Taking the Quiz

Users can re-take the quiz from:
- **Settings → Profile → Update my persona**
- **In-app prompt after 7 days** (if skipped initially)
- **Chat command:** "Change my persona" or "I'm actually a lawyer" → surface quiz or direct toggle

After re-taking, the new persona result overwrites the old one immediately. The user's existing chats and documents are not affected; only the defaults change going forward.

---

## Related skills

- [[onboarding-b2c-vs-b2b-fork]]
- [[onboarding-first-prompt-suggestion-by-persona]]
- [[onboarding-empty-state-prompts]]
- [[onboarding-feature-discovery-tour]]
