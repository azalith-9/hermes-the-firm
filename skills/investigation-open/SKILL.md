---
name: investigation-open
description: >
  Open a new internal investigation matter — runs intake, generates the sources
  checklist, and creates the persistent investigation log. Use when a complaint
  or allegation comes in and the attorney needs to stand up a privileged
  investigation workspace.
argument-hint: "[brief description of the allegation]"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from anthropics/claude-for-legal (plugin 'employment-legal', Apache-2.0) for Hermes Agent.
Tool names, config paths, and /employment-legal:{skill} invocations were
rewritten to Hermes equivalents. Hand adjustments are tracked in
Regenerated sections are maintained upstream of this repository.
-->


# /investigation-open

Opens a new investigation matter — runs intake, generates the sources
checklist, and creates the persistent investigation log.

## Instructions

1. Load `~/.hermes/plugins/config/hermes-the-firm/employment-legal/PRACTICE.md`.
2. Load the `internal-investigation` reference skill and run Mode 1 (Open).
3. If a matter with the same slug already exists, warn before overwriting.

## Examples

```
hermes-the-firm:investigation-open
Harassment complaint filed against a manager in the Austin office.
```

```
hermes-the-firm:investigation-open
(skill will ask for details)
```

> Detailed intake, privilege-formation requirements, sources checklist, and log
> templates live in the `internal-investigation` reference skill — load it
> before doing substantive work.
