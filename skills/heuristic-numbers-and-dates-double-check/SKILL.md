---
name: heuristic-numbers-and-dates-double-check
description: Use as a mandatory post-draft quality pass on any legal document or advice output. Requires a dedicated review of every number and date in the output — statute article numbers, case citations, deadlines, limitation periods, currency amounts, percentages, and Hijri/Gregorian dates. AI legal drafting errors are most visible and most damaging when they involve incorrect numbers; this heuristic prevents those failures. Applies universally across all jurisdictions and document types.
license: MIT
metadata: " id: heuristic.numbers-and-dates-double-check category: heuristic priority: P0 intent: [__core__, quality-control, numbers, dates, accuracy, post-draft] related: [heuristic-statute-of-limitations-flag, heuristic-party-names-consistency, router-confidence-scorer, heuristic-always-state-jurisdiction-first] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'heuristic'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Double-Check Numbers and Dates

## When this applies

This heuristic runs as a post-draft pass on every substantive legal output: contract drafts, review memos, advice letters, litigation analysis, regulatory summaries. Numbers and dates are the most failure-prone category in AI-generated legal text, and errors in this category are the most damaging — they directly affect legal rights, deadlines, and financial obligations.

Apply this pass after drafting and before delivering any output to the user.

## What to check

### 1. Statute and regulatory article numbers

- **Do not invent article numbers.** If the applicable article is not known with certainty, state the concept and note that the exact article number should be verified.
- If an article number was provided in the user's input or a reliable source, reproduce it exactly.
- Common failure mode: hallucinated article numbers that resemble real ones (e.g., "Art. 347 COC" when the correct article is Art. 349).
- **MENA context**: article numbers in Lebanese, UAE, KSA, and Egyptian codes are frequently cited in practice; errors here undermine credibility immediately.

### 2. Case citations

- For any case citation, verify: year, docket or reference number, court, paragraph pin-cite (if used).
- Do not invent case citations. A fictional case citation in a legal memo is a serious professional error.
- If only the case name and general principle are known, state the principle without a fabricated citation: "The general principle from X case (verify citation with a legal database) is…"
- **MENA context**: DIFC and ADGM judgments use specific reference formats (e.g., "CFI-2024-XXXXX"). KSA court decisions are often not publicly cited by docket number. Lebanese Court of Cassation decisions are cited by chamber and date.

### 3. Deadlines, notice periods, and limitation periods

- Deadlines embedded in legal advice must be verified against current law. Limitation periods change by legislation; notice periods differ by contract and statute.
- Specify: (a) the period, (b) the start date (accrual event), (c) the end date, and (d) whether the period is calendar days or business days.
- Flag immediately if a limitation period is within 6 months (see [[heuristic-statute-of-limitations-flag]]).
- **MENA context**: MENA jurisdictions mix calendar-day and business-day conventions. UAE commercial contracts often use business days; UAE court deadlines often use calendar days. KSA may use Hijri calendar for official deadlines — confirm the calendar being used.

### 4. Currency amounts

- Specify the currency with its ISO code (USD, AED, SAR, LBP, EGP, EUR, GBP). Do not rely on symbols alone, especially in bilingual documents.
- Do not drop zeros. AED 1,000,000 and AED 1,000 are very different numbers; a dropped zero is a contract defect.
- Check that amounts are consistently expressed across the document (amount in figures = amount in words = amount in schedules).
- **MENA context**: Lebanon's Lebanese pound (LBP) has been subject to multiple exchange rates; specify which rate applies if relevant. KSA transactions may reference SAR and USD simultaneously; confirm which is controlling.

### 5. Dates (calendar and Hijri/Gregorian)

- Check all dates for internal consistency (e.g., a contract executed on 1 January cannot reference events that happen on 15 December of the same year as having already occurred).
- In KSA documents, dates are often stated in both Hijri and Gregorian calendars. Verify that both match. Conversion errors between calendars are common — use a verified converter.
- In UAE, official government documents may use Hijri; commercial contracts use Gregorian. If the document is for a UAE government entity, check whether the execution date and effective date should be expressed in Hijri.
- **Execution vs effective date**: many documents are executed on one date but become effective on another. Both must be stated; they must be logically consistent.

### 6. Percentages and rates

- Interest rates, profit rates (for Islamic finance structures), ownership stakes, and tax rates must be stated accurately.
- In KSA and UAE Islamic finance: conventional interest rates do not appear; profit rates and rental yields should be stated as percentages and verified against the transaction documents.
- Ownership stakes in company structures must add up to 100%. A cap table with stakes totaling 99% or 101% is a drafting error.

## The checking tactic

After producing a draft, run a dedicated "numbers and dates only" review pass:

1. **List every number and date** in the output — scan systematically, clause by clause.
2. **For each item**: confirm it is intentional, verify (or flag for verification) against source material.
3. **Flag uncertainties**: if a number was not provided by the user and was generated by inference, state it explicitly: "Note: the limitation period stated above (3 years) is based on general UAE Civil Code provisions; verify against the specific contract type and current law."
4. **Consistency check**: for multi-document transactions, verify that amounts, dates, and references are consistent across all documents.

## Lebanon example (civil-law deadlines)

Lebanon's Code of Obligations and Contracts (COC) provides indicative limitation periods:

| Claim type | Period | Reference |
|---|---|---|
| Tort | 3 years | Art. 257 COC |
| Commercial contracts (general) | 10 years | Art. 349 COC |

These periods are jurisdiction-specific and subject to legislative change. **Verify against current law** rather than relying on these as authoritative. Shorter periods may apply to specific claim types (insurance: 2 years; maritime: 1 year; wage claims: 1 year).

The principle is the same for all MENA jurisdictions: always verify rather than recall.

## Failure modes

| Failure | Impact |
|---|---|
| Incorrect limitation period stated | User may miss filing deadline; case may be time-barred |
| Fabricated article number cited | Embarrassment; advice relying on non-existent provision |
| Currency amount with dropped zero | Contract defect; potential financial loss |
| Hijri/Gregorian conversion error | Incorrect effective dates; missed deadlines |
| Wrong percentage for ownership stake | Corporate structure documents are legally defective |

## Related skills

- [[heuristic-statute-of-limitations-flag]]
- [[heuristic-party-names-consistency]]
- [[router-confidence-scorer]]
- [[heuristic-always-state-jurisdiction-first]]
