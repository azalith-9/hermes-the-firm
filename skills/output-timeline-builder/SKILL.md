---
name: output-timeline-builder
description: Use when the agent must reconstruct or project a chronological timeline of events for litigation, M&A, regulatory proceedings, contract performance, or statute-of-limitations analysis. Formats events in date-ordered lists with optional annotations, deadline flags, and multi-track parallel display. Triggers on any question involving a sequence of events, breach timeline, deal milestones, or deadline mapping.
license: MIT
metadata: " id: output.timeline-builder category: output intent: ['__format__', 'timeline', 'chronology', 'litigation', 'M&A', 'deadlines'] related: - output-table-of-comparisons - output-irac-structure - draft-litigation-complaint - heuristic-numbers-and-dates-double-check priority: P1 source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'output'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Timeline Builder

A timeline is one of the most powerful analytical tools in legal practice — it turns a pile of documents, emails, and testimony into a narrative that either supports or undermines a legal position. In litigation, the timeline is often the first analytical product prepared. In M&A, it tracks deal milestones and regulatory windows. In contract disputes, it maps performance against obligations. This skill governs how the agent builds, formats, and annotates legal timelines.

## When to use this

Build a timeline when:
- Reconstructing the facts for a litigation chronology or witness statement
- Mapping M&A deal milestones (discovery → NDA → DD → term sheet → definitive agreement → signing → closing → post-closing)
- Tracking regulatory filing windows and approval deadlines
- Analysing contract performance and alleged breach
- Computing limitation periods — what happened when, and is the claim in time?
- Preparing a board presentation or case summary for a client

## Standard format — compact list

The default format is a date-stamped event list, ISO date format (YYYY-MM-DD):

```
2024-01-15  Discovery call between Acme and Globex
2024-02-20  NDA executed (Mutual NDA, English/Arabic)
2024-04-10  Due diligence commenced — data room opened
2024-05-22  Term sheet signed
2024-07-30  Definitive agreement signed — SPA
2024-08-15  MOFCOM / regulatory filing submitted (UAE: MoCI notification)
2024-10-01  Regulatory clearance obtained
2024-10-15  Closing conditions satisfied
2024-10-22  Closing — consideration transferred
2024-11-01  Earnout period commences (12-month)
2025-10-31  Earnout period ends
```

Use ISO date format consistently. If only month/year is known, write `2024-07` and note the precision: `[month and year only — exact date not established]`.

## Variant: annotated timeline

Add a source column and a legal-significance column for litigation purposes:

```
Date         Event                                        Document / Source            Legal significance
2024-02-20   NDA executed                                 NDA (Ex. A-001)              Confidentiality obligations arise
2024-04-10   DD data room opened                          Data room log (Ex. B-003)    Constructive disclosure of [item]
2024-07-30   SPA signed                                   SPA (Ex. A-002)              Representations and warranties as at this date
2024-10-22   Closing                                      Closing statement (Ex. C-01) Condition precedent deadline trigger
2024-11-15   Alleged breach discovered by Buyer           Email Doe→Smith (Ex. D-007)  Limitation clock starts (UAE: 1 year from knowledge, Civil Code art 487 analog)
```

The Document column creates the evidentiary chain. The Legal significance column is the lawyer's value-add.

## Variant: deadline tracker with severity flags

For matters with multiple upcoming deadlines:

```
Deadline        Days remaining  Event                               Priority
2026-05-20      6               Response to DFSA request due        🔴 CRITICAL
2026-05-28      14              Reply brief due — DIFC CFI          🔴 CRITICAL
2026-06-10      27              Annual regulatory renewal filing    🟡 HIGH
2026-07-01      48              Option exercise window closes       🟡 HIGH
2026-09-30      139             Statute of limitations — claim X    🟢 MONITOR
```

Severity flags:
- 🔴 CRITICAL — imminent, failure creates irreversible harm or contempt risk
- 🟡 HIGH — within 30 days, requires active management
- 🟢 MONITOR — important but sufficient lead time

## Variant: multi-track timeline

For complex matters with parallel workstreams (e.g., regulatory approval + financing + diligence running simultaneously):

```
Date         Track: Regulatory          Track: Financing            Track: Diligence
2024-08-01   MoCI filing submitted       —                           Legal DD commenced
2024-08-15   —                          Facility agreement signed    Technical DD commenced
2024-09-01   Waiting period begins       —                           DD issues list issued
2024-09-30   —                          Conditions precedent met     DD responses received
2024-10-01   Clearance obtained          —                           DD sign-off
2024-10-22   [Closing]                  [Closing]                   [Closing]
```

Use the multi-track format when a key question is whether two tracks will converge in time (e.g., "will regulatory clearance arrive before the financing longstop?").

## Limitation periods — MENA reference

When building timelines for limitation analysis, the applicable periods under key MENA legal systems:

| Jurisdiction | General limitation | Contract claims | Tort claims | Notes |
|---|---|---|---|---|
| UAE (federal) | 15 years (Civil Code) | 15 years general; 1 year for specific commercial claims | 3 years from knowledge | UAE Civil Transactions Law governs; shorter periods for specific sectors |
| DIFC | 6 years (DIFC Limitation Law) | 6 years | 6 years | Common-law-style accrual rules |
| ADGM | 6 years | 6 years | 6 years | English Limitation Act 1980 as adapted |
| KSA | No single general period; varies by type | Commercial: 5 years (Commercial Court Law) | Variable | Hijri calendar affects computation |
| Lebanon | 10 years general (Civil Code) | 10 years general; shorter for specific categories | 3 years | Civil law accrual rules |
| Egypt | 15 years general | 15 years; 7 years commercial | 3 years from knowledge | Civil Code art 374 |

**Always verify the specific limitation period for the specific cause of action — these general periods have many exceptions.**

## Dates and calendar notes

**Hijri dates:** Saudi and some UAE regulatory instruments use Hijri dates. When including these on a timeline, always add the Gregorian equivalent: `1443H-07-12 (12 February 2022)`. Conversion should be done against the official Umm al-Qura calendar.

**Date precision:** if a date is approximate or disputed, flag it: `~2024-03` or `2024-03 [disputed — see testimony of Witness X]`.

**Time zones:** for cross-border transactions, note the applicable time zone for deadline events: `2024-10-22 17:00 GST (UTC+4) — UAE closing`.

## Dates integrity check

Timeline dates are high-stakes. Always apply [[heuristic-numbers-and-dates-double-check]]:
- Check that dates are internally consistent (no event precedes its cause)
- Verify that stated deadlines align with the contract or court order
- Flag any gap in the timeline that suggests missing documents or disputed facts

## Related skills

- [[output-table-of-comparisons]]
- [[output-irac-structure]]
- [[draft-litigation-complaint]]
- [[draft-witness-statement]]
- [[heuristic-numbers-and-dates-double-check]]
- [[output-source-attribution-block]]
