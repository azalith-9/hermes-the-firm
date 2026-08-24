---
name: output-executive-summary-first
description: Use when the audience is a lawyer, partner, or in-house client who needs the bottom line before the analysis — the BLUF (Bottom Line Up Front) format. Leads with a one-sentence conclusion, then a 3–5 bullet executive summary, then the full analysis. Apply as the default structure for substantive legal analysis responses and memos in a legal AI product.
license: MIT
metadata: " id: output.executive-summary-first category: output priority: P0 intent: [bluf, executive-summary, formatting, legal-memo, bottom-line-first] related: [output-creac-structure, output-client-letter-style, output-docx-export-style, conversation-disclaimer] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'output'.
Registered as a flat plugin skill.
-->


# Executive Summary First (BLUF)

## When to use this

Apply BLUF (Bottom Line Up Front) formatting when:
- The reader is a B2B professional — a lawyer, partner, in-house counsel, or business executive — who reads under time pressure.
- The output contains substantive legal analysis, a risk assessment, or a recommendation.
- The response is longer than 150 words and could confuse the reader about what they should actually do.
- The user's question has a clear answer that should not be buried.

BLUF is the **default output structure** for substantive legal AI responses. Exceptions (outputs that do not use BLUF):
- Short factual answers (one or two sentences) — a BLUF header would be disproportionate.
- Conversational turns that do not deliver analysis.
- Drafted documents (contracts, letters) — these have their own internal structure.

## The pattern

```
**Bottom line:** [One-sentence conclusion — the answer to the user's question.]

**Summary**
- [Key point 1 — the most important finding or risk]
- [Key point 2]
- [Key point 3]
- [Key point 4 — optional]
- [Key point 5 — optional]

**Full analysis**
[The complete reasoning, organized by issue, section by section]
```

## Rules for each section

### Bottom line (one sentence)

- State the conclusion, not the question.
- Be specific: "The clause is likely unenforceable" is better than "There are enforceability concerns."
- Include the primary reason in the sentence if it fits naturally: "The clause is likely unenforceable because it is unlimited in geographic scope."
- Use calibrated language: "likely", "almost certainly", "should be enforceable if X" — not "definitely" or "will."
- Never start with "Based on the information provided..." — that is throat-clearing, not a conclusion.

### Summary (3–5 bullets)

- Each bullet is one substantive point the reader will act on.
- No more than one line per bullet (two lines maximum for complex points).
- Order: most important finding first, then supporting points, then any caveats or recommended actions.
- Do not pad with "This is a complex area" or "Advice of local counsel is recommended" as a bullet — if required, those go in the disclaimer at the end.
- Avoid repeating the bottom line verbatim — the bullets should add substance, not restate.

### Full analysis

- Use CREAC structure ([[output-creac-structure]]) for each legal issue within the analysis.
- Use clear headings for each issue.
- Citations go in the analysis, not in the summary bullets.
- Disclaimers go at the end of the full analysis, not at the beginning.

## Example

**Bottom line:** The lease as drafted is likely unenforceable on three grounds; we recommend rejecting and counter-proposing.

**Summary**
- The 15-year term triggers Lebanese statutory tenancy protections that limit landlord rights to terminate — verify whether the statutory framework applies to commercial leases in this location.
- The rent escalation clause is open-ended (no cap or CPI linkage) — this creates unpredictable cost exposure over the lease term.
- The absolute subletting prohibition (no subletting without landlord consent for any reason) is uncommonly strict and may impede future operational flexibility.
- The service charge methodology is not stated — the tenant has no visibility into future service charge levels.
- Governing law and forum (Beirut courts) is favorable for the tenant.

**Full analysis**

*[Proceeds with section-by-section CREAC for each of the five issues above...]*

## What not to do

| Anti-pattern | Why it's wrong |
|---|---|
| Burying the conclusion at the end | The reader may not get there, or may misread the analysis as more ambiguous than it is |
| Opening with disclaimers | Disclaimers go at the end; opening with them signals insecurity and buries the value |
| Repeating the user's question back verbatim | The user knows what they asked; starting by paraphrasing their question wastes their time |
| Opening with "Based on the information provided..." | Throat-clearing; every legal analysis is based on the information provided |
| Padding the summary bullets with non-substantive points | Every bullet should contain a finding that would change the reader's decision if removed |
| Using "complex area of law" as a substitute for analysis | Acknowledge complexity, but then do the analysis anyway |

## Paired with

- **[[output-creac-structure]]**: the structure used within the "Full analysis" section.
- **[[output-client-letter-style]]**: when the BLUF output is formatted as a formal client letter, the Bottom line becomes the opening paragraph and the Summary becomes the numbered recommendations.
- **[[output-docx-export-style]]**: when the BLUF output is exported to DOCX, the Bottom line becomes a highlighted paragraph (e.g., in a text box or bold format) at the top of the document.

## Related skills

- [[output-creac-structure]] — the analytical structure that follows the BLUF header
- [[output-client-letter-style]] — letter format that incorporates BLUF as the opening
- [[output-docx-export-style]] — document export that preserves BLUF formatting
- [[conversation-disclaimer]] — where disclaimers belong (end, not beginning)
