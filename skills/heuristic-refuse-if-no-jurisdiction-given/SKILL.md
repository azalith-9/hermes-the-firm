---
name: heuristic-refuse-if-no-jurisdiction-given
description: Use when a user submits a drafting, review, or legal advice request without specifying the applicable jurisdiction. Defines the decision rule — when to ask (hard ask for drafting and specific advice) versus when to assume and flag (general knowledge questions) — and provides the standard prompt for eliciting jurisdiction from the user. This is a P0 quality gate that prevents defective legal outputs grounded in the wrong governing law.
license: MIT
metadata: " id: heuristic.refuse-if-no-jurisdiction-given category: heuristic priority: P0 intent: [__core__, jurisdiction, quality-gate, clarification, routing] related: [heuristic-always-state-jurisdiction-first, router-jurisdiction-detector, conversation-clarifying-questions, heuristic-governing-law-must-match-forum] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'heuristic'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Refuse-or-Assume Rule for Missing Jurisdiction

## When this applies

Every time a drafting, review, or specific advice request arrives and the jurisdiction is not specified, this heuristic governs the response. It prevents the platform from generating a legal output grounded in an assumed jurisdiction that may be wrong.

The rule has two branches: **hard ask** (pause; do not proceed without jurisdiction) and **soft assume + flag** (proceed with a general or multi-jurisdiction answer, but flag the assumption).

## Branch 1 — Hard ask (do not assume)

For these request types, stop and ask for the jurisdiction before proceeding:

### Drafting any contract or legal instrument
A contract draft must reflect the governing law of the instrument. The wrong governing law affects capacity requirements, formal validity (written form? notarization? registration?), mandatory default rules, and interpretation standards. Drafting a UAE LLC shareholders agreement under an assumed Lebanese governing law would produce a defective document.

### Advice about specific legal rights ("Can I sue?", "What's the deadline?", "Is this enforceable?")
Specific legal-rights questions require a jurisdiction-specific answer. The limitation period for a contract claim is 10 years in Lebanon, 15 years under UAE federal law (general), and 6 years in DIFC. Answering "you have 3 years" to a claim question without knowing the jurisdiction is not neutral — it is actively wrong for most scenarios.

### Criminal or regulatory exposure questions
Penalties, elements of offenses, enforcement agencies, and defenses all differ by jurisdiction. Do not advise on regulatory exposure without knowing the regulatory jurisdiction.

### Employment-related drafting or advice
Employment law is jurisdiction-specific and often has mandatory provisions that cannot be contracted out of. UAE Labor Law, KSA Labor Law, Lebanese Labor Code, and DIFC Employment Law are materially different instruments.

## Branch 2 — Soft assume + flag (acceptable for general questions)

For these request types, it is acceptable to provide a general or comparative answer while flagging the assumption:

### General legal-knowledge questions
"What is force majeure?" / "What does consideration mean in contract law?" — these can be answered with a legal-concept explanation, noting which legal traditions the answer draws from.

### Comparative or "how does X differ?" questions
"How does NDA enforcement differ between common law and civil law?" — pick 3–5 jurisdictions and structure the answer comparatively. Flag that the user should confirm the relevant jurisdiction(s) for their specific matter.

### Legal vocabulary / terminology questions
"What does *rescission* mean?" or "What is a promissory note?" — definitional questions do not require jurisdiction-specific answers, though noting civil-law vs common-law distinctions adds value.

## The ask pattern

When the hard-ask branch applies, use this standard prompt:

> *"Before I draft / review / advise on this, I need to know the applicable jurisdiction. My coverage for you includes:*
>
> - *Lebanon (Beirut courts / Lebanese law)*
> - *UAE onshore (Dubai courts / UAE federal law)*
> - *UAE — DIFC (DIFC Courts / DIFC law)*
> - *UAE — ADGM (ADGM Courts / ADGM law)*
> - *KSA (Saudi courts / KSA law)*
> - *Other GCC (Qatar / Bahrain / Kuwait / Oman)*
> - *International — please specify the seat of arbitration (DIAC, ICC, LCIA, ADCCAC)*
> - *France / EU*
> - *UK*
> - *Other (please specify)*
>
> *Which applies here?"*

Adapt the list to the context — a consumer question about a lease does not need the arbitration-seat options. A cross-border corporate transaction may need all of them.

## Inferring jurisdiction from context

Some contextual signals allow safe inference without a hard ask:

| Signal | Safe inference |
|---|---|
| User's Louis profile jurisdiction set to UAE; question about a UAE employment contract | Assume UAE; flag assumption in the response |
| User pastes a contract with "Governed by the laws of England and Wales" | England and Wales is clearly stated; proceed |
| User mentions "Dubai Marina apartment lease" | UAE is the probable jurisdiction; confirm before drafting |
| User asks about "DIFC court enforcement" | DIFC jurisdiction is explicitly stated in the question |
| User's prior messages in this session established the matter is in KSA | KSA is established context; proceed |

Even when inferring from context, state the assumed jurisdiction in the response (per [[heuristic-always-state-jurisdiction-first]]) so the user can correct if wrong.

## Interaction with the jurisdiction detector

The [[router-jurisdiction-detector]] automatically attempts to detect jurisdiction from context signals before a skill fires. If the detector has successfully identified the jurisdiction with high confidence, this heuristic does not need to fire — the jurisdiction is already known. If the detector returns low confidence or no detection, this heuristic governs.

## Anti-patterns

| Anti-pattern | Why it fails |
|---|---|
| Assume the user's profile jurisdiction for every question | User may be asking about a counterparty in a different jurisdiction, or a matter in a third jurisdiction |
| Give a "generally speaking" answer and bury the jurisdiction caveat | User acts on the general answer; specific jurisdiction rules are different; practitioner error |
| Ask for jurisdiction for every question including simple vocabulary questions | Creates friction; users find it annoying and stop using the product |
| Ask for jurisdiction and then produce a generic answer anyway | Pointless friction; if you asked, use the answer |

## Related skills

- [[heuristic-always-state-jurisdiction-first]]
- [[router-jurisdiction-detector]]
- [[conversation-clarifying-questions]]
- [[heuristic-governing-law-must-match-forum]]
