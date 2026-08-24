---
name: investigation-add
description: >
  Add data to an open investigation — documents, interview notes, or
  observations. Processes batches against the documented pull criteria,
  surfaces significant items, and logs everything reviewed for coverage
  verification. Use when new evidence, interview notes, or document
  productions come in for an open investigation.
argument-hint: "[matter name or slug, then paste or attach data]"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from anthropics/claude-for-legal (plugin 'employment-legal', Apache-2.0) for Hermes Agent.
Tool names, config paths, and /employment-legal:{skill} invocations were
rewritten to Hermes equivalents. Hand adjustments are tracked in
Regenerated sections are maintained upstream of this repository.
-->


# /investigation-add

Adds data to an open investigation log. Processes document batches using
documented pull criteria, surfaces significant items, logs everything
reviewed for coverage verification.

## Instructions

1. Load `~/.hermes/plugins/config/hermes-the-firm/employment-legal/PRACTICE.md`.
2. Load the `internal-investigation` reference skill and run Mode 2 (Add data).
3. After processing, show the surface ratio and list of surfaced items.
4. Prompt to update the sources checklist if the data covers a checklist item.

## Examples

```
hermes-the-firm:investigation-add [matter name]
[paste interview notes]
```

```
hermes-the-firm:investigation-add [matter name]
[attach email export]
```

> Detailed needle-finding process, log entry format, surface-ratio rules, and
> sources-checklist tracking live in the `internal-investigation` reference
> skill — load it before doing substantive work.
