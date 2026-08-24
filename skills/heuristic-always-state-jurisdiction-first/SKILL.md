---
name: heuristic-always-state-jurisdiction-first
description: Use this heuristic when generating any substantive legal answer, opinion, analysis, or document draft. Requires that the applicable jurisdiction be stated explicitly in the first sentence of any legal response. This is a P0 core quality rule for the Louis platform — failing to state jurisdiction makes a legal answer trivially wrong for some readers and is the single most common failure mode in multi-jurisdiction AI legal assistance.
license: MIT
metadata: " id: heuristic.always-state-jurisdiction-first category: heuristic priority: P0 intent: [__core__, jurisdiction, legal-accuracy, output-quality] related: [heuristic-refuse-if-no-jurisdiction-given, router-jurisdiction-detector, heuristic-governing-law-must-match-forum, heuristic-shariah-compliance-check-when-relevant] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'heuristic'.
Registered as a flat plugin skill.
-->


# Always State Jurisdiction First

## When this applies

This heuristic applies to every substantive legal answer — whether in chat, in a document draft, in a review output, or in a research summary. It is a P0 quality rule: no exceptions on substantive legal content.

It does **not** apply to:
- Pure procedural questions about the Louis platform itself ("how do I export a document?").
- Conversational acknowledgments ("Sure, I can help with that — give me a moment.").
- Purely factual non-legal questions.

## The rule

**State the applicable jurisdiction in the first sentence of every substantive legal answer.**

The jurisdiction statement must:
1. Name the specific jurisdiction (not just a region).
2. Appear at the start — not buried in paragraph 3.
3. Be accurate — do not guess if the user has not provided jurisdiction (see [[heuristic-refuse-if-no-jurisdiction-given]]).

## Correct patterns

```
✅ "Under UAE federal law (specifically the Commercial Companies Law as amended), a limited liability company requires a minimum of two shareholders."

✅ "In Lebanon, under the Code of Obligations and Contracts (COC), the general limitation period for contractual claims is ten years."

✅ "Under DIFC law (DIFC Contract Law DIFC Law No. 6 of 2004 and its amendments), consideration is required for a binding agreement — unlike civil-law systems."

✅ "Across MENA, the answer varies by jurisdiction. Let me cover the four most common positions: UAE federal, KSA, Lebanon, and DIFC/ADGM."
```

## Incorrect patterns

```
🚫 "The contract is enforceable if both parties have capacity and the object is lawful." 
   [NO — which jurisdiction's capacity rules? Which definition of lawful object?]

🚫 "Generally, you have three years to bring a claim."
   [NO — 3 years is the tort limitation in LB and UAE federal civil code; it is 6 years in DIFC/ADGM; it is case-type-specific in KSA.]

🚫 "Employment contracts require written form."
   [NO — written form requirements differ materially between UAE, KSA, Lebanon, and DIFC.]
```

## Why this rule exists

Legal rules are jurisdiction-specific. Even fundamental concepts — capacity, consideration, limitation periods, enforceability of penalty clauses, arbitration opt-out rules — differ substantially between civil-law jurisdictions (LB, UAE onshore, KSA, EG, FR) and common-law jurisdictions (DIFC, ADGM, UK). A legally accurate answer for UAE federal law may be wrong for DIFC, and vice versa.

Skipping the jurisdiction creates an output that is:
- Trivially wrong for some subset of readers.
- Potentially dangerous if acted upon without professional verification.
- Impossible to quality-check without re-asking the jurisdiction question.

## Multi-jurisdiction pattern

When the user's question spans multiple jurisdictions, or when the jurisdiction is contextually broad (e.g., "GCC"), structure the answer jurisdicition-by-jurisdiction:

> *"The position on force majeure varies across MENA. Here is the framework in the four jurisdictions most commonly relevant to Louis users:*
>
> *UAE federal: [position].*
> *KSA: [position].*
> *Lebanon: [position].*
> *DIFC/ADGM: [position as common-law jurisdictions]."*

This structure is preferred over mixing jurisdictions in undifferentiated prose.

## How this interacts with other heuristics

- If the jurisdiction is unknown and cannot be safely inferred, apply [[heuristic-refuse-if-no-jurisdiction-given]] before invoking this heuristic.
- If the jurisdiction is known but involves a KSA or Islamic finance context, pair with [[heuristic-shariah-compliance-check-when-relevant]].
- For choice of forum and governing law clause review, pair with [[heuristic-governing-law-must-match-forum]].
- For routing the user's request to the correct jurisdiction-specific skill, see [[router-jurisdiction-detector]].

## Related skills

- [[heuristic-refuse-if-no-jurisdiction-given]]
- [[router-jurisdiction-detector]]
- [[heuristic-governing-law-must-match-forum]]
- [[heuristic-shariah-compliance-check-when-relevant]]
