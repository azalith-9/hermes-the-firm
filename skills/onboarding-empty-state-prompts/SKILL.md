---
name: onboarding-empty-state-prompts
description: Use when a user encounters an empty state in a legal AI assistant — a screen with no prior content, no chats, no documents, no projects — and the system must provide an actionable, persona-appropriate prompt rather than a dead end. Covers the specific prompt language, CTA patterns, and personalization signals for every major empty-state screen. Eliminates "no data" dead-ends and converts them into the user's next productive action.
license: MIT
metadata: " id: onboarding.empty-state-prompts category: onboarding priority: P0 intent: [onboarding, empty-state, prompts, UX, engagement, retention] related: [onboarding-first-prompt-suggestion-by-persona, onboarding-persona-detection-questions, onboarding-b2c-vs-b2b-fork, onboarding-feature-discovery-tour] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'onboarding'.
Registered as a flat plugin skill.
-->


# Onboarding — Empty-State Prompts

## When this applies

An **empty state** is any screen or section in the product that has no user-generated content yet: no chats, no documents, no projects, no recent activity. Empty states are high-risk UX moments — a user who sees a blank screen with no guidance will drop off. This skill converts every empty state into an invitation to take the next productive action.

Empty states fall into two types:
1. **First-time empty**: the user has never used this area of the product
2. **Return-visit empty**: the user has used the product but has no recent activity in this area (cleared history, new device, returning after a long absence)

Both types need actionable prompts. The second type benefits from additional context awareness ("Welcome back…").

---

## Behavior — The Empty-State Pattern

Every empty state must follow this pattern:
1. **Acknowledge the state briefly** (optional — skip if the UI design makes the empty state self-explanatory)
2. **Provide a specific, actionable next step** — not a vague "get started" directive
3. **Make the action easy** — clickable chips, pre-filled example prompts, or direct CTAs
4. **Never leave the user with nothing to do**

Empty states should **never** be negative or apologetic ("No data found", "Nothing here yet"). They should be forward-looking and inviting.

---

## Prompt by Screen

### /home (no recent chats)

**Default prompt:**
> "Let's start. Draft an NDA, review a contract, or ask a legal question — Louis is ready."

**Clickable chips:**
- "Draft an NDA"
- "Review a contract"
- "Ask about my rights"
- "Help me start a business"

**Returning user variant:**
> "Welcome back. Pick up where you left off — or start something new."

### /assistant (new chat, blank composer)

Surface persona-appropriate starter prompts from [[onboarding-first-prompt-suggestion-by-persona]].

**For consumer (louis-twin) persona:**
- "I got a contract to sign — can you explain it?"
- "I want to know my rights as a tenant in [jurisdiction]"
- "Help me start a freelance business — what do I need?"

**For lawyer persona:**
- "Review this MSA from a vendor-side perspective"
- "Draft a mutual NDA for a joint venture under UAE law"
- "Compare non-compete enforceability in LB, KSA, and UAE"

### /projects (no projects)

**Default prompt:**
> "Create a project to organise documents and chats by matter. Keep everything related to a client or transaction in one place."

**CTA button:** "New Project"

**Example project names to show as clickable:** "Vendor Agreement — Q2", "Employment Dispute", "Company Formation LB"

### /doc-workspace (no documents in current project)

**Default prompt:**
> "Upload a contract or legal document — Louis will analyse it, flag key issues, and explain every clause."

**CTAs:**
- "Upload document"
- "Use the demo contract (Acme MSA)"
- "Paste contract text"

**Sub-prompt (lawyer fork):**
> "Or generate a first draft — specify the document type, parties, jurisdiction, and key commercial terms."

### /drafting-board (empty board, no matters)

**Default prompt:**
> "Start a new matter and Louis will map out a multi-step legal workflow — research, drafting, review, and delivery."

**CTA:** "New matter"

**Example matter types to show:** "NDA negotiation", "Employment contract review", "Corporate restructuring"

### /skills (no recent skills or route tests)

**Default prompt:**
> "Louis routes every request to specialised skills. Use the route-tester to see which skill handles any message — and explore the full library."

**CTA:** "Open route-tester"

**Second CTA:** "Browse skills library"

---

## Personalization Layers

### Persona-aware

- The specific prompt chips and CTA text adapt to the user's persona (B2C vs B2B, and sub-role within B2B)
- Persona is read from [[onboarding-persona-detection-questions]] output
- If persona is unknown (first visit, no quiz), use the consumer-default prompts for /home and /assistant

### Time-of-day-aware

| Time window | Tone adjustment |
|-------------|----------------|
| Morning (6am–11am) | "Start your day with…" / "Ready to get ahead of today's work?" |
| Afternoon (11am–5pm) | Neutral; task-focused |
| Evening (5pm–10pm) | "Wrapping up the day?" / "Quick review before you close?" |
| Late night (10pm+) | Neutral; no social-pressure urgency language |

### Recency-aware (returning user)

- If the user has prior chats or projects: "Welcome back. Continue with [last matter name]?" with a clickable link
- If the user has been inactive > 7 days: "It's been a while — here's what Louis can help with today." + fresh prompt chips
- Do not use guilting language ("You haven't used Louis in 14 days") — use inviting language only

### Jurisdiction-aware

Where jurisdiction is known from the user profile or prior prompts:
- Localise the example chips: "Know your rights in [UAE / Lebanon / KSA]" rather than generic "[jurisdiction]"
- Surface jurisdiction-relevant templates in document-workspace empty states

---

## Anti-Patterns to Avoid

| Anti-pattern | Replace with |
|---|---|
| "No data found" | "Create your first [project / document / chat] here" |
| "Nothing here yet" | A specific invitation to create something |
| "Get started!" (no next step) | A concrete, clickable action |
| Locking the empty state behind a tutorial | Always give the user something to do now |
| Pure decorative empty state (illustration only, no text) | Add at least one actionable CTA |

---

## Related skills

- [[onboarding-first-prompt-suggestion-by-persona]]
- [[onboarding-persona-detection-questions]]
- [[onboarding-b2c-vs-b2b-fork]]
- [[onboarding-feature-discovery-tour]]
- [[messaging-surface-rule-in-app-non-lawyer-fork]]
- [[messaging-surface-rule-in-app-lawyer-fork]]
