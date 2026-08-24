---
name: expansion-kickoff
description: >
  Kick off international expansion planning for a new country — gathers intake,
  runs EOR vs. entity framing, drafts cross-functional questions, surfaces
  country-specific flags, and creates a persistent tracker. Use when someone
  says "we're hiring in [country]", "expansion to [country]", or "first hire
  in [country]".
argument-hint: "[country name]"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from anthropics/claude-for-legal (plugin 'employment-legal', Apache-2.0) for Hermes Agent.
Tool names, config paths, and /employment-legal:{skill} invocations were
rewritten to Hermes equivalents. Hand adjustments are tracked in
Regenerated sections are maintained upstream of this repository.
-->


# /expansion-kickoff

Starts an international expansion project for a new country — gathers intake,
runs EOR vs. entity framing, drafts cross-functional questions, surfaces
country-specific flags, and creates a persistent tracker.

## Instructions

1. Load `~/.hermes/plugins/config/hermes-the-firm/employment-legal/PRACTICE.md` → jurisdictional footprint, escalation table.
2. Load the `international-expansion` reference skill and run the full workflow.
3. If a tracker file already exists for this country (`~/.hermes/plugins/config/hermes-the-firm/employment-legal/expansion-[slug].yaml`),
   flag it: "An expansion tracker for [country] already exists. Use
   `hermes-the-firm:expansion-update [country]` to update it, or confirm
   you want to start over."
4. Create `~/.hermes/plugins/config/hermes-the-firm/employment-legal/expansion-[slug].yaml` on completion.

## Examples

```
hermes-the-firm:expansion-kickoff Germany
```

```
hermes-the-firm:expansion-kickoff
(skill will ask which country)
```

> Detailed EOR vs. entity framework, cross-functional questions, briefing
> templates, and tracker schema live in the `international-expansion`
> reference skill — load it before doing substantive work.
