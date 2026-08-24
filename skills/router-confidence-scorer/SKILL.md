---
name: router-confidence-scorer
description: Use before delivering any substantive legal answer to score the model's own confidence in the proposed response. Produces a 0.0–1.0 confidence score and routes the request to one of four handling modes — proceed, hedge, cite-or-bust, or escalate — based on jurisdiction coverage, recency requirements, specificity of the claim, and stakes. The anti-hallucination gate for all legal AI output.
license: MIT
metadata: " id: router.confidence-scorer category: router priority: P0 intent: [__router__] related: [router-escalation, router-complexity-grader, router-tool-selector, router-intent-detection] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'router'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Confidence Scorer

## Purpose

The Confidence Scorer prevents hallucination of legal substance. Legal AI assistants face a specific failure mode: confident-sounding assertions about statute numbers, case citations, regulatory thresholds, and procedural deadlines that are subtly or entirely wrong. In legal practice, this is not a cosmetic error — a missed deadline or incorrect statute reference can cause irreversible harm.

This skill runs before any substantive legal answer is delivered and gates the output through one of four handling modes based on a self-assessed confidence score.

## When to Run

Run on every response that contains:
- A statute or article reference (specific number)
- A case citation
- A regulatory threshold or deadline (a specific number of days, percentage, or amount)
- A claim about what a law "requires" or "prohibits"
- A comparison between jurisdictions on a specific legal point
- Any statement about recent developments or amendments (anything within the last 18 months)

Do not run the full scorer for: greetings, routing decisions, document drafting of boilerplate, or pure summarization where the source document is provided.

## Inputs to Evaluate

When scoring, consider all four dimensions simultaneously:

### Dimension 1 — Jurisdiction Coverage

Training coverage varies by jurisdiction. Apply this calibration:

| Jurisdiction | Training coverage level | Confidence adjustment |
|---|---|---|
| UK (E&W), US federal, France, Germany, EU | Strong | No adjustment |
| UAE (federal + DIFC + ADGM) | Strong | No adjustment |
| KSA | Good | Slight downward adjustment for recent regulatory changes |
| Lebanon, Egypt | Moderate | Downward adjustment for recent developments |
| Jordan, Kuwait, Bahrain, Oman, Qatar | Moderate | Downward adjustment |
| OHADA jurisdictions | Weaker | Significant downward adjustment |
| Other MENA or niche jurisdictions | Variable | Significant downward adjustment |

If the jurisdiction is one where training coverage is weaker, reduce confidence by 0.1–0.2 before applying other adjustments.

### Dimension 2 — Recency Requirement

Legal rules change. Assess whether the response requires current (post-training) information:

- **Static principles** (consideration, offer and acceptance, general corporate law principles): no recency concern
- **Statute text that has not changed in decades**: low recency concern
- **Regulatory thresholds, deadlines, and prescribed amounts**: high recency concern — these change frequently
- **Recent enactments or amendments** (within 18 months of training cutoff): very high recency concern
- **Case law developments**: moderate to high depending on area

If recency matters and the answer depends on potentially-outdated information, reduce confidence significantly.

### Dimension 3 — Specificity

- A general statement ("UAE employment law requires a notice period") → lower specificity, lower risk of error
- A specific statement ("Article 43 of UAE Federal Law No. 33 of 2021 requires 30 days' notice for contracts of over 5 years") → high specificity, high risk of hallucinated article number or incorrect duration

As specificity increases, confidence must be verified against a reliable source. If you cannot verify, do not assert.

### Dimension 4 — Stakes

Not all errors are equally consequential:

| Stakes level | Examples | Escalation threshold |
|---|---|---|
| High | Litigation deadline, criminal exposure, imminent regulatory sanction, property rights | Escalate at confidence < 0.6 |
| Medium | Contract term advice, negotiation positioning | Hedge at confidence < 0.75 |
| Low | Background research, educational explanation, boilerplate generation | Proceed at confidence ≥ 0.5 |

## Scoring and Handling Modes

After evaluating all four dimensions, assign a final score from 0.0 to 1.0 and map to a handling mode:

### `proceed` — Confidence ≥ 0.85

The response is based on well-established, jurisdiction-appropriate, current law. Deliver the answer as drafted. No hedging language required unless the user's situation has complexity that warrants a disclaimer.

### `hedge` — Confidence 0.60–0.84

The response is likely correct but there is meaningful uncertainty. Apply hedging language throughout:
- "In most cases…" not "The law requires…"
- "Typically…" not "Always…"
- "Generally under [jurisdiction] law…" not "Under [jurisdiction] law…"
- "This may vary depending on recent amendments — verify against current legislation"

Link to [[conversation-uncertainty-language]] for the standard hedging vocabulary.

### `cite-or-bust` — Confidence < 0.60 on a specific fact

The specific fact (article number, case citation, regulatory threshold) cannot be asserted without verification. Two options:

1. **Trigger a tool call**: if [[router-tool-selector]] indicates that `tool.web-search-orchestrator` or `tool.legal-data-hunter` is available and the request complexity is `medium` or above, run a verification search before answering
2. **Refuse to assert**: if tools are not available or the stakes are low, write `[citation needed — please verify this reference against current [jurisdiction] law]` rather than guessing

**Anti-hallucination rule**: Never invent a statute number, article number, case name, party name, or regulatory deadline. If you cannot verify, write the placeholder. A placeholder is honest; a hallucinated citation is harmful.

### `escalate` — Confidence < 0.40 on a high-stakes question

The question is high-stakes (see Dimension 4) and the model's confidence is below the threshold for any independent answer. Route to [[router-escalation]] with a summary of:
- What the user is asking
- Why confidence is insufficient
- What a human lawyer or specialist should investigate

Never send a low-confidence, high-stakes answer — even with heavy hedging — without offering an escalation path.

## Output

Emit a JSON object before generating the answer:

```json
{
  "confidence": 0.0-1.0,
  "mode": "proceed|hedge|cite-or-bust|escalate",
  "jurisdiction_coverage": "strong|good|moderate|weak",
  "recency_risk": "none|low|moderate|high",
  "specificity": "general|moderate|high",
  "stakes": "high|medium|low",
  "reasoning": "<one sentence explaining the score>"
}
```

If mode is `hedge`, the response body must use appropriate hedging language throughout.
If mode is `cite-or-bust`, insert `[citation needed — please verify]` wherever an unverified specific claim appears.
If mode is `escalate`, do not attempt to answer the substantive question; route per [[router-escalation]] immediately.

## Anti-Hallucination Rule (Absolute)

**Never invent statute numbers, article numbers, case citations, or party names.**

If you know the general framework but cannot verify the specific article:
- Write: "Under the UAE Federal Law on Commercial Companies [exact article number to be verified]..."
- Do NOT write: "Under Article 47 of the UAE Federal Law on Commercial Companies..." if you are not certain

A citation that is confidently wrong is worse than no citation at all. Courts, counterparties, and clients will rely on citations. Incorrect citations cause real harm.

## Related Skills

- [[router-escalation]]
- [[router-complexity-grader]]
- [[router-tool-selector]]
- [[router-intent-detection]]
- [[conversation-uncertainty-language]]
