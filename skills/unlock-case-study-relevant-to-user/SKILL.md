---
name: unlock-case-study-relevant-to-user
description: Use when surfacing a relevant use case or success story to a user who is exploring the platform, approaching an upgrade decision, or showing signs of disengagement. Selects and presents a case study matched to the user's detected persona (role, industry, jurisdiction) to demonstrate concrete value and reduce hesitation. Invoked at empty-state moments and before upgrade prompts to show social proof specific to the user's context.
license: MIT
metadata: " id: unlock.case-study-relevant-to-user category: unlock jurisdictions: [__multi__] priority: P2 intent: [case-study, social-proof, personalization, conversion] related: [unlock-contextual-upsell, unlock-empty-state-suggestions, unlock-cross-product-bridge] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'unlock'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Case Study — Relevant to User

## What it does

This skill surfaces a case study or use-case story that matches the current user's profile — their role, industry, jurisdiction, and task context. Case studies demonstrate that people like the user have already succeeded with the platform, reducing the activation energy for new users and providing social proof at conversion moments.

## When this applies

- **Empty state** — user opens a new chat with no prior context; surface a case study alongside starter suggestions
- **Pre-upgrade** — before showing an upgrade prompt ([[unlock-contextual-upsell]]), prime with a relevant case study showing what Pro users achieve
- **Disengagement signal** — user has been inactive for > 3 minutes, or has typed and deleted multiple messages (hesitation signal)
- **Onboarding flow** — after the user states their role and jurisdiction, immediately surface a matching case study
- **Feature discovery** — when the user first encounters a new feature, show a concrete example of another user using it successfully

## Behavior

### Profile matching logic
The skill reads the user's known profile attributes and selects from the case study library:

| Attribute | Source | Match target |
|---|---|---|
| Role | Onboarding self-identification | `in-house-counsel`, `private-practice`, `compliance-officer`, `entrepreneur`, `legal-ops` |
| Industry | HubSpot CRM or self-declared | `fintech`, `real-estate`, `technology`, `hospitality`, `manufacturing`, `ngo` |
| Jurisdiction | IP geolocation + self-declared | `UAE`, `KSA`, `LB`, `EG`, `DIFC`, `ADGM`, `UK`, `FR`, `US` |
| Task context | Current conversation | `nda-drafting`, `due-diligence`, `employment`, `ip`, `corporate` |

### Matching algorithm
1. Score each case study against the user's profile on 4 dimensions
2. Weight: task_context (40%) + jurisdiction (30%) + industry (20%) + role (10%)
3. Return the highest-scoring case study
4. If tie: prefer the most recently added case study (freshness)
5. If no match above threshold (score < 0.5): return the generic "legal professional" default

### Case study format

A case study shown to the user should be concise and concrete — never longer than 4–5 sentences:

```
[Persona] — a [role] at a [industry] firm in [jurisdiction] — used Louis to [task].
In [time], they [specific achievement]. The result: [outcome in concrete terms].

"[Short testimonial quote if available]"

[Try it] [Learn more]
```

**Good example**:
> A compliance officer at a UAE fintech used Louis to run KYC checks across 40 counterparties before a Series B close. In 2 hours, Louis screened all 40 against UN, OFAC, and EU lists and flagged 2 for enhanced due diligence. The team avoided a deal delay that would have cost 3 days of legal hours.

**Bad example** (too generic):
> A lawyer used Louis to help with legal work. It saved time and was useful.

### Jurisdictional personalization
For MENA users specifically, case studies should reflect local context:
- KSA users: reference MOC registry, ZATCA compliance, SAIP trademark
- UAE users: reference DED checks, DIFC/ADGM structures, CBUAE compliance
- Lebanon users: reference commercial register, BDL circulars, bilingual Arabic/French documents
- DIFC/ADGM users: reference English common-law drafting, DIAC arbitration, free-zone structures

## Case study library categories

Maintain a curated library with at minimum one case study per intersection of:
- Role × jurisdiction (e.g., "in-house counsel × UAE")
- Task type × industry (e.g., "NDA drafting × fintech")
- Feature × outcome (e.g., "sanctions screening × due diligence acceleration")

Minimum 20 case studies in library at launch; expand with each product update.

## Do not

- Do not invent case study details — all case studies must be based on real or composite real user experiences
- Do not surface a case study that required a product tier the current user cannot access (e.g., enterprise feature for a free-tier user)
- Do not repeat the same case study in the same session
- Do not show more than one case study at a time — choice overload reduces conversion
- Do not show a case study with a testimonial quote that has not been verified with the user who gave it

## Examples (good vs problematic)

| Scenario | Good | Problematic |
|---|---|---|
| UAE in-house counsel, new session | Show: "In-house counsel at Dubai REIT used Louis for SPA review..." | Show: "A lawyer in New York used Louis for US securities work..." |
| KSA compliance officer | Show: "Compliance team screened 50 Saudi entities via MOC + OFAC in 1 hour" | Show: Generic "save time" claim with no specifics |
| Upgrade prompt context | Show case study first → then upgrade prompt | Show upgrade prompt first → then case study (kills conversion) |

## Measurement

Track per case study:
- **Click-through rate** (user clicks "Try it" or "Learn more")
- **Conversion lift** (did showing this case study before an upgrade prompt improve conversion vs control?)
- **Relevance rating** (optional thumbs up/down on case study shown)

## Related skills

- [[unlock-contextual-upsell]] — the upgrade prompt this case study primes
- [[unlock-empty-state-suggestions]] — shown alongside this at empty-state moments
- [[unlock-cross-product-bridge]] — bridges between product tiers; case studies support the bridge
