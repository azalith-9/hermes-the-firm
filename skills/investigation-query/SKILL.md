---
name: investigation-query
description: >
  Ask questions against an open investigation log — what witnesses said, where
  accounts conflict, what gaps exist, what the strongest evidence is on each
  issue. Use when the attorney needs to query the investigation record without
  re-reading every entry.
argument-hint: "[matter name] [question]"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from anthropics/claude-for-legal (plugin 'employment-legal', Apache-2.0) for Hermes Agent.
Tool names, config paths, and /employment-legal:{skill} invocations were
rewritten to Hermes equivalents. Hand adjustments are tracked in
Regenerated sections are maintained upstream of this repository.
-->


# /investigation-query

Answers questions against the investigation log — what witnesses said,
where accounts conflict, what gaps exist, what the strongest evidence is
on each issue.

## Instructions

1. Load the `internal-investigation` reference skill and run Mode 3 (Query).
2. Always cite log entry IDs in the answer.
3. If the log contains nothing relevant to the question, say so explicitly —
   "I have not seen any information on [topic] in this investigation log
   ([N] entries reviewed)" — and offer to flag it as a gap.

## Examples

```
hermes-the-firm:investigation-query [matter name]
What did the respondent say about the December team dinner?
```

```
hermes-the-firm:investigation-query [matter name]
Where do the complainant's and respondent's accounts conflict?
```

```
hermes-the-firm:investigation-query [matter name]
What do we still need?
```

> Detailed log-query process, citation rules, and gap-flagging templates live
> in the `internal-investigation` reference skill — load it before doing
> substantive work.
