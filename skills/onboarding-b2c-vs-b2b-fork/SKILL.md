---
name: onboarding-b2c-vs-b2b-fork
description: Use when a new user begins onboarding for a legal AI assistant and the system must determine whether to serve them as a consumer (B2C) or as a legal professional (B2B) — and fork the entire experience accordingly. Defines the detection signals, the fork logic, the persona assigned to each path, and the override mechanism. This skill is the gateway to all persona-specific onboarding, messaging, feature access, and pricing presentation.
license: MIT
metadata: " id: onboarding.B2C-vs-B2B-fork category: onboarding priority: P0 intent: [onboarding, persona, B2C, B2B, fork, detection, routing] related: [onboarding-persona-detection-questions, onboarding-first-prompt-suggestion-by-persona, messaging-bridge-line, messaging-surface-rule-in-app-lawyer-fork, messaging-surface-rule-in-app-non-lawyer-fork] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'onboarding'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Onboarding — B2C vs B2B Fork

## When this applies

This skill runs at or immediately after sign-up for every new user. Its output is a binary classification — **B2C (consumer)** or **B2B (professional)** — which determines:

- Which persona the user is assigned
- Which in-app messaging fork they see ([[messaging-surface-rule-in-app-non-lawyer-fork]] or [[messaging-surface-rule-in-app-lawyer-fork]])
- Which starter prompts are surfaced ([[onboarding-first-prompt-suggestion-by-persona]])
- Which pricing tier and features are pitched
- What disclaimer language is displayed prominently
- Whether eFirm or enterprise features are shown

The fork is not permanent — users can override it at any time. But the default must be set correctly from the first interaction.

---

## Inputs / Signals

The fork is determined by accumulating signals from multiple sources. No single signal is determinative; higher-confidence signals outweigh weaker ones.

### High-confidence signals (any one sufficient)

| Signal | B2C indicator | B2B indicator |
|--------|--------------|--------------|
| Email domain | Free domain (@gmail, @yahoo, @hotmail, @icloud, or consumer ISP) | Corporate domain (@firmname.com, @legalpartners.com, @corp.com) |
| Sign-up form field | "Firm name" left blank | "Firm name" filled |
| Persona quiz | "Business owner", "Student", "Individual" selected | "Lawyer", "In-house counsel", "Legal ops" selected |
| LinkedIn import | Title contains no legal keywords | Title contains "lawyer", "attorney", "advocate", "avocat", "محامي", "counsel", "solicitor", "partner" |

### Medium-confidence signals (combine two or more)

| Signal | B2C indicator | B2B indicator |
|--------|--------------|--------------|
| First prompt content | Consumer situation ("my lease", "I got fired", "starting a side business") | Professional task ("review this MSA", "draft an NDA for client", "compare non-compete law") |
| Payment method | Personal card (consumer name) | Corporate card or invoice billing |
| Referral source | Consumer influencer link, organic search | Law firm partnership link, CLE registration, conference badge scan |
| Device / platform | Mobile first, iOS | Desktop first, enterprise SSO |

### Low-confidence signals (inform but do not determine)

- Time of day / session length
- Browser language and locale
- Geographic IP (firm-heavy cities: Dubai DIFC, Riyadh KAFD, Beirut Hamra, London EC4)

---

## Fork Logic

```
IF high-confidence B2B signal → assign B2B fork
ELSE IF high-confidence B2C signal → assign B2C fork  
ELSE IF 2+ medium-confidence B2B signals → assign B2B fork
ELSE IF 2+ medium-confidence B2C signals → assign B2C fork
ELSE → assign B2C fork (default) + surface persona quiz after first session
```

**Default is B2C.** The consumer fork is more protective (stronger UPL disclaimers, plain-language framing, "talk to a lawyer" prompts). Assigning a lawyer to the consumer fork is a minor inconvenience they can override; assigning a consumer to the lawyer fork is a product safety and UPL risk.

---

## B2C Fork Configuration

When the user is classified as B2C:

| Parameter | Setting |
|-----------|---------|
| Persona | `louis-twin` (consumer default) |
| Tone | Empathetic, plain English, situational |
| Disclaimer | Prominent "legal information, not legal advice" on every high-stakes interaction |
| Starter prompts | Consumer personas: employment, housing, family, business start-up, wills |
| Features shown | Consumer-tier capabilities; eFirm and enterprise features hidden |
| Pricing presented | Free tier + consumer paid tiers |
| "Talk to a lawyer" triggers | Active — displayed on complex or urgent legal situations |
| Skills available | Consumer-relevant subset (not full professional library) |

---

## B2B Fork Configuration

When the user is classified as B2B, fork further by sub-role:

| Detected role | Persona assigned | Additional features |
|---------------|-----------------|---------------------|
| Lawyer + small firm (≤10 lawyers) | `associate` | eFirm features pitched; matter management shown |
| Lawyer + medium-large firm | `partner` | eFirm features; team management; usage analytics |
| In-house counsel | `in-house-counsel` | Enterprise compliance tools; policy drafting; vendor contract workflows |
| Legal ops | `in-house-counsel` (default) | Workflow automation features; reporting |
| Lawyer (unknown firm size) | `associate` (default) | Standard professional features |

B2B fork settings:
- Tone: professional, citation-heavy, task-oriented
- Disclaimer: brief professional-responsibility framing ("lawyer review required for client-facing output")
- Starter prompts: professional tasks (contract review, NDA drafting, jurisdiction comparison)
- Full skills library accessible
- Pricing: Pro / Business / Enterprise tiers
- eFirm features: available and pitched at onboarding

---

## Persona Quiz

If the automated fork is not high-confidence, surface the persona detection quiz per [[onboarding-persona-detection-questions]]. The quiz:
- Takes ≤ 60 seconds (3–4 questions)
- Is optional with a "Skip" path (defaults to B2C)
- Overwrites the automated classification if completed
- Is re-surfaced after 7 days if the user skipped initially

---

## Override Mechanisms

Users can override the fork at any time:

1. **/customize** — settings page with explicit persona selector
2. **Re-take persona quiz** — available from the settings page
3. **Manual fork selection** — explicit "I'm a lawyer / I'm not a lawyer" toggle in account settings
4. **Support channel** — users can request a fork change via support

After override, re-run the fork logic and persist the user's explicit choice. Do not re-detect automatically after an explicit override — treat the user's choice as authoritative.

---

## Re-Evaluation After First 5 Prompts

Regardless of initial classification, after the user's first 5 prompts, re-evaluate signals:
- If a B2C-classified user is consistently using professional legal terminology and task framing → surface gentle "Are you a legal professional?" prompt
- If a B2B-classified user is consistently using consumer-style prompts → offer consumer persona switch
- Do not switch silently; prompt the user and get confirmation before re-forking

---

## Critical Principles

- **Fluidity over locking**: the fork is a default, not a cage. Users move between professional and personal use; the system should adapt.
- **Consumer safety first**: when in doubt, use the more protective consumer fork
- **Signal accumulation**: re-evaluate the classification as more signals arrive; do not treat sign-up signals as permanently definitive

---

## Related skills

- [[onboarding-persona-detection-questions]]
- [[onboarding-first-prompt-suggestion-by-persona]]
- [[onboarding-empty-state-prompts]]
- [[messaging-surface-rule-in-app-lawyer-fork]]
- [[messaging-surface-rule-in-app-non-lawyer-fork]]
- [[messaging-bridge-line]]
