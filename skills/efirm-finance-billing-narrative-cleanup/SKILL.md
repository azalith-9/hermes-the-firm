---
name: efirm-finance-billing-narrative-cleanup
description: Use when reviewing and cleaning up time-entry narratives before they are assembled into an invoice. Flags block-billing, insufficient activity description, privilege leaks, grammar issues, and attorney-identification failures. Produces a cleaned narrative with a diff showing every change, paired with the invoice-generator workflow. Applies to any jurisdiction and any client type; client-specific billing guidelines can be loaded as context.
license: MIT
metadata: " id: efirm-finance.billing-narrative-cleanup category: efirm-finance jurisdictions: [__multi__] priority: P1 intent: [billing, narrative, time entry, invoice cleanup, billing guidelines, block billing] related: [efirm-finance-invoice-generator-from-time-entries, efirm-finance-afa-quote-builder, efirm-finance-budget-vs-actual-matter] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'efirm-finance'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Billing Narrative Cleanup

A time-entry narrative is the justification for every hour billed. Vague narratives invite client write-downs, billing disputes, and discovery-related privilege problems. Specific, well-structured narratives reduce write-off risk, pass client billing audits, and demonstrate value. This skill reviews narratives before invoicing and produces a cleaned version with a diff.

## When to use this

- Before assembling a monthly or matter-close invoice
- As part of a periodic billing audit (random sample of entries)
- When a specific client has triggered a billing dispute and narratives need to be reviewed retrospectively
- When onboarding new timekeepers who need training on narrative standards

## What to Review — Seven Checks

### 1. Block Billing Detection

Block billing bundles multiple activities into a single time entry (e.g., "Review file, draft letter, conference with client — 4.5 hours"). Most in-house counsel guidelines and court cost assessment standards prohibit block billing because it prevents evaluation of whether each component was reasonably necessary.

**Flag pattern**: a single entry with more than one activity verb ("review...," "draft...," "attend...") where activities are not clearly inseparable.

**Fix**: split into separate entries, or restructure as "Review of correspondence and draft of response letter" if the activities are logically continuous.

**Example:**
- BAD: "Review file, attend call with client, draft response to opposition, research damages issues. 3.5h"
- BETTER:
  - "Review of matter file in preparation for client call re discovery schedule. 0.5h"
  - "Telephone conference with client re discovery schedule and upcoming depositions. 0.5h"
  - "Draft response letter to opposition counsel re discovery objections. 1.5h"
  - "Research on damages quantification under UAE Civil Code for preparation of expert brief. 1.0h"

### 2. Insufficient Activity Description

Narratives that fail to identify what was actually done are write-down bait.

**Common inadequate descriptions:**
- "Review file" — which file? What was the purpose of the review?
- "Research" — research on what issue? For what purpose?
- "Internal meeting" — with whom? On what subject?
- "Correspondence" — with whom? About what?
- "Work on matter" — this is not a description

**Standard for an adequate narrative:**
- Action verb (reviewed, drafted, attended, analyzed, researched)
- Object (the document, party, issue, or proceeding)
- Purpose or context (in connection with X, for Y purpose, re Z)

**Examples:**
- WEAK: "Review of correspondence."
- BETTER: "Review of correspondence from opposing counsel re proposed discovery schedule modifications and preparation of summary for partner."
- WEAK: "Research."
- BETTER: "Research on KSA Labor Law Article 80 grounds for summary dismissal in connection with employee termination file [Client/Matter]."

### 3. Privilege Protection

Time-entry narratives can inadvertently reveal privileged attorney-client communications or attorney work product if they describe the substance of legal advice given or litigation strategy contemplated.

**Problematic descriptions:**
- "Advise client that claim is weak and settlement should be considered" — reveals the substance of legal advice; privileged; should not appear in an invoice sent to the client (and certainly not on any invoice that might be seen by opposing counsel in a fee dispute)
- "Draft memo on weaknesses in our position" — reveals litigation strategy; work product

**Better approach:**
- "Prepare written analysis of litigation risk and strategic options for partner review" (neutral; does not reveal the substance of the advice)
- "Draft internal legal memorandum re case assessment"

**Rule**: the narrative should describe the nature of the legal work, not its substantive content.

### 4. Grammar, Spelling, and Formatting

Basic quality issue: invoices with typos or grammatical errors undermine professional credibility.

- Capitalize proper nouns (party names, court names, agreement titles)
- Consistent capitalization of matter/file references
- No abbreviations that are not client-understood (avoid firm-internal codes)
- Active voice preferred ("Drafted response letter" rather than "Response letter was drafted")
- Consistent tense (past tense for completed activities)

### 5. Attorney / Timekeeper Identification

Most billing systems require the attorney's initials or name on the time entry, but the narrative itself should make clear who performed what work where multiple timekeepers interact.

In a narrative for a partner reviewing work product:
- "Review and revision of first draft associate memorandum on security agreement structure [Assoc: ABC]" — identifies who did the drafting and who did the review

### 6. Opposing Counsel Names

Some clients have billing guidelines that require opposing counsel to be referred to by firm name only (not individual names), for conflict and relationship management reasons. Flag any entries where an opposing counsel's individual name appears; redact to firm name as needed.

### 7. Length Within Firm Style

Some firms require brief (one-line) entries; others accept multi-sentence descriptions for complex activities. Review against the applicable client billing guidelines or firm style guide.

## Output Format

### Input entry
```
Timekeeper: [Name] | Date: [Date] | Hours: 2.5
Original: "Review file, research, draft memo."
```

### Cleaned entry
```
Timekeeper: [Name] | Date: [Date] | Hours: 2.5
Cleaned: "Review of client correspondence and prior advice in preparation for 
         drafting. Research on UAE Federal Decree-Law 33/2021 notice-period
         provisions. Draft internal memorandum on termination procedure for
         review by partner."
```

### Diff
```
CHANGE: "Review file" → "Review of client correspondence and prior advice 
         in preparation for drafting"
CHANGE: "research" → "Research on UAE Federal Decree-Law 33/2021 notice-period
         provisions"  
CHANGE: "draft memo" → "Draft internal memorandum on termination procedure for
         review by partner"
REASON: Block billing split into three sequential activities; each activity
        made specific and contextualized.
```

## Integration with Invoice Pipeline

This skill is upstream of [[efirm-finance-invoice-generator-from-time-entries]]. The sequence is:

1. Export raw time entries from matter management system
2. Run billing narrative cleanup (this skill)
3. Partner reviews cleaned entries and approves any significant rewrites
4. Pass cleaned entries to invoice generator

If the client has specific billing guidelines (uploaded to context), those guidelines are applied as additional rules during cleanup.

## Common Patterns that Require Rewriting

| Original narrative | Problem | Fixed version |
|---|---|---|
| "Review file — 2.5h" | Too vague | "Review of [specific document/correspondence] in connection with [issue/purpose] — 2.5h" |
| "Emails — 1.0h" | No context | "Review and response to client email re [subject]; review opposing counsel email re [subject] — 1.0h" |
| "Research — 3.0h" | Completely undefined | "Legal research on [jurisdiction] [issue] for preparation of [document/advice] — 3.0h" |
| "Team meeting — 0.5h" | Block without context | "Team meeting with [partner/associate] to discuss case strategy and review of discovery responses — 0.5h" |
| "Call — 0.3h" | No parties or subject | "Telephone conference with [client] re [issue] — 0.3h" |

## Related skills

- [[efirm-finance-invoice-generator-from-time-entries]]
- [[efirm-finance-afa-quote-builder]]
- [[efirm-finance-budget-vs-actual-matter]]
