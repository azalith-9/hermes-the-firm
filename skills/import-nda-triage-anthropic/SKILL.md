---
name: import-nda-triage-anthropic
description: Use when migrating an NDA triage skill originally built for the Anthropic the agent API into the mini-hermes-the-firm format. The adapter maps legacy NDA intake logic — mutual vs unilateral detection, risk-level scoring, accept/negotiate/reject routing, and expedited-review flags — into the standard skill model. Triggers on import of any Anthropic-native NDA screening or intake workflow.
license: MIT
metadata: " id: import.nda-triage-anthropic category: import jurisdictions: [__multi__] priority: P3 intent: [__import__, nda, triage, migration, anthropic, contract-intake] related: [import-nda-review-jamie-tso, import-contract-review-anthropic, review-nda-bilateral, draft-nda-unilateral] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'import'.
Registered as a flat plugin skill.
-->


# Import: NDA Triage (Anthropic)

## What it does

This import adapter migrates an **NDA triage skill** originally built for Anthropic's the agent API into the `mini-hermes-the-firm` standard format. NDA triage is the front door to an NDA review workflow: before spending legal-team time on a full review, the triage skill rapidly classifies an incoming NDA into one of three operational buckets — **accept as-is**, **negotiate**, or **reject** — and identifies the top risks that drove the classification.

The Anthropic-native triage skill may have been a rapid-fire system prompt, a classification chain, or a structured JSON-output prompt. This adapter normalises the shape and wires it into the Louis skill model.

## Import config

| Field | Source mapping | Default if absent |
|---|---|---|
| `triage_mode` | Legacy `mode` | `three-bucket` (accept / negotiate / reject) |
| `nda_type_detection` | Legacy `detect_type` boolean | `true` |
| `risk_flags_limit` | Legacy `max_flags` | `5` top flags |
| `expedited_flag` | Legacy `expedited` boolean | `true` |
| `output_format` | Legacy `format` | `triage_card` |
| `escalation_threshold` | Legacy `escalate_at` | `HIGH` |
| `jurisdiction` | Legacy `jurisdiction` | `__multi__` |

## Dry-run preview

```
IMPORT PREVIEW — nda-triage-anthropic
Source shape    : Anthropic NDA triage prompt
Mode            : three-bucket (accept / negotiate / reject)
Type detection  : enabled (mutual vs unilateral auto-detected)
Risk flags      : max 5 surfaced
Expedited flag  : enabled
Output          : triage_card
Escalation      : at HIGH risk level
```

## Triage decision logic (post-import)

```
NDA RECEIVED
      │
      ▼
Detect NDA type
  → Mutual: both parties disclose
  → Unilateral: only one party discloses (typically our client receives)
  → Hybrid: tiered or partial
      │
      ▼
Score against 5 core criteria (see below)
      │
      ▼
All criteria within standard range?
  Yes → ACCEPT (flag any cosmetic issues; no negotiation needed)
  One or more criteria outside range?
      ↓
  Risk level HIGH? → REJECT (or escalate to senior counsel)
  Risk level MEDIUM? → NEGOTIATE (specific redlines identified)
```

## Core triage criteria (5 checks)

| # | Check | Fail condition | Severity |
|---|---|---|---|
| 1 | **Confidential Information scope** | Over-broad (captures everything) or under-broad (excludes obvious sensitive items) | MEDIUM |
| 2 | **Term / duration** | Perpetual obligation with no sunset; or unreasonably short (< 2 years for tech deals) | MEDIUM |
| 3 | **Residuals clause** | Present without limitation — receiving party can use anything retained in memory | HIGH |
| 4 | **One-sided obligations** | Purportedly mutual but obligations materially asymmetric | MEDIUM |
| 5 | **Governing law / jurisdiction** | Non-neutral or unenforceable in the relevant operating jurisdiction | HIGH |

## Triage card output

```
NDA TRIAGE CARD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Type          : Mutual / Unilateral
Counterparty  : [name]
Date received : [date]
Triage result : ACCEPT / NEGOTIATE / REJECT
Risk level    : HIGH / MEDIUM / LOW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Top flags (max 5):
  1. [flag — severity — brief rationale]
  2. ...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Recommended next step:
  [Accept with notes / Redline and return / Escalate to senior counsel]
```

## MENA-specific triage notes

- **UAE**: government contracts may require Arabic as the official language of the NDA; flag if the document is English-only.
- **KSA**: side letters or addenda may be required to address Shariah-compliance concerns around penalty provisions.
- **DIFC / ADGM**: check that the DIFC/ADGM governing-law clause is actually valid — parties must have a legitimate connection to the jurisdiction.
- **Lebanon**: economic instability means USD payment obligations and FX-related provisions in any NDA with financial terms warrant extra scrutiny.

## Failure modes

| Error | Likely cause | Resolution |
|---|---|---|
| `type_not_detected` | No mutual/unilateral marker in source | Default to `mutual`; flag for manual confirmation |
| `criteria_not_mapped` | Legacy used different check names | Auto-map to nearest of 5 standard criteria |
| `triage_card_not_generated` | Legacy output was free-form | Wrap in triage card template post-import |
| `expedited_never_triggered` | Legacy had no expedite logic | Apply HIGH-risk escalation rule |

## Related skills

- [[import-nda-review-jamie-tso]]
- [[import-contract-review-anthropic]]
- [[review-nda-bilateral]]
- [[draft-nda-unilateral]]
- [[import-legal-risk-assessment-anthropic]]
