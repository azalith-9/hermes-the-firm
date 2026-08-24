---
name: strategy-messaging-bible
description: Use when writing copy for any Louis-facing surface — marketing pages, onboarding flows, sales collateral, social media, or in-product messaging. Defines the core brand pillars (comfort UI, MENA-first, jurisdiction-aware, bilingual native, transparent skill router) and governs tagline selection and surface-specific messaging rules. Internal use only.
license: MIT
metadata: " id: strategy.messaging-bible category: strategy jurisdictions: [__multi__] priority: P3 intent: [__internal__] related: [strategy-customers, strategy-competitors, strategy-growth-strategy, site-use-case-router] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'strategy'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Strategy — Messaging Bible

## Purpose

This skill is the canonical reference for all Louis brand messaging. Every piece of copy — marketing, onboarding, email, social, in-product — should be consistent with the pillars and rules defined here.

## Core brand pillars

### 1. Comfort UI

**What it means:** Louis is designed for lawyers who are AI-skeptical or AI-naive. The interface does not assume technical fluency. Interactions are guided, not open-ended. The name "Louis" (a human name, not a product acronym) is a deliberate choice to lower the psychological barrier to AI adoption in a conservative professional sector.

**In copy:** Use language that normalises AI assistance without overpromising autonomy. Avoid tech jargon ("LLM", "embedding", "vector search"). Prefer: "Louis reads the contract and flags what matters."

---

### 2. MENA-first

**What it means:** Louis was built for MENA legal professionals. It understands UAE Federal Decree-Laws, KSA Royal Decrees, DIFC/ADGM common law, Lebanese civil law, and Egyptian commercial law. This is not a US/UK tool with MENA added on — it was designed for MENA from day one.

**In copy:** Lead with jurisdiction specificity. Not "legal AI" — "legal AI for UAE law", "legal AI built for KSA practitioners." Name specific laws and frameworks when addressing practice-area audiences.

---

### 3. Jurisdiction-aware

**What it means:** Louis knows which legal system governs a task. It does not conflate UAE Federal law with DIFC law, or KSA Sharia-based commercial principles with civil-law norms. Jurisdiction awareness is explicit and auditable.

**In copy:** "Louis knows whether you're working under UAE Federal Law or DIFC Law — and adjusts accordingly." Use jurisdiction-specific examples in all vertical pages.

---

### 4. Bilingual native

**What it means:** Arabic is not a translation layer — it is a first-class working language. Documents can be drafted, reviewed, and researched in Arabic. Output is bilingual when the matter requires it.

**In copy:** Always mention Arabic when addressing MENA audiences. This is the single strongest differentiator from all US/UK competitors. Example: "Draft your employment contract in Arabic and English — simultaneously."

---

### 5. Transparent skill router

**What it means:** When Louis executes a task, the active skill is visible to the user. This is a trust and compliance differentiator: lawyers and supervising partners can see exactly what capability was used and apply their professional judgment accordingly.

**In copy:** "Louis shows its work." Or: "Know exactly which AI capability is running — Louis is transparent by design." Resonates with bar-rule compliance concerns (see [[safety-bar-rule-1-1-competence-AI]]).

## Tagline candidates by surface

| Surface | Tagline candidate |
|---|---|
| Homepage hero | "Legal AI built for MENA." |
| Sub-hero | "Draft, review, and research in Arabic and English — jurisdiction-aware, always." |
| Onboarding | "Meet Louis. Your bilingual MENA legal assistant." |
| Tools landing page | "Free legal tools for MENA practitioners." |
| Investor deck | "The first legal AI built for the MENA legal market." |
| LinkedIn ad | "UAE law. KSA law. DIFC law. Louis knows the difference." |

Surface-specific tagline rules are defined in more detail in the surface-rule companion (formerly `[[messaging.surface-rule]]`).

## Messaging anti-patterns

- **Do not:** "AI-powered legal platform" — generic; any LegalTech company could say this
- **Do not:** "Revolutionising legal" — overused; signals nothing
- **Do not:** "Your AI lawyer" — legally problematic; implies UPL (unauthorised practice of law)
- **Do not:** Promise specific accuracy percentages unless backed by verifiable benchmarks
- **Do not:** Describe Louis as a "chatbot" — it is a skill-based legal assistant with transparent routing

## Tone and voice

| Attribute | Description |
|---|---|
| **Professional** | Not casual, not stiff. Peer-to-peer, lawyer to lawyer. |
| **Precise** | No vague claims. Specifics (jurisdiction, statute, time-saving metric) outperform generalities. |
| **Confident, not arrogant** | Louis is the MENA specialist. State it plainly. Do not hedge. |
| **Respectful of the profession** | Never position Louis as replacing lawyers. It amplifies them. |
| **Bilingual aware** | Arabic copy should not be literal translations of English copy; adapt for register. |

## Related skills

- [[strategy-customers]]
- [[strategy-competitors]]
- [[strategy-growth-strategy]]
- [[site-use-case-router]]
