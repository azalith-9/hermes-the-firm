---
name: dataroom-watcher
description: >
  Monitors the VDR for new document uploads and posts closing checklist status
  on schedule. Flags new uploads that match high-priority categories. Trigger:
  "what's new in the data room", "VDR updates", or on schedule.
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from anthropics/claude-for-legal (plugin 'corporate-legal', Apache-2.0) by tools_dev/port_upstream.py.
Tool names, config paths, and /corporate-legal:{skill} invocations were
rewritten to Hermes equivalents. Hand adjustments are tracked in
tools_dev/MANUAL_FIXUPS.md — do not hand-edit regenerated sections.
-->


# Dataroom Watcher Agent

## Purpose

VDRs get updated at 11pm the night before a call. This agent watches for new uploads and tells the team what came in. Also runs the closing checklist status on the configured cadence.

## Schedule

Daily during active diligence. Checklist status per `~/.hermes/plugins/config/hermes-the-firm/corporate-legal/PRACTICE.md` → Deal team briefing cadence.

## Integrations

Posting to Slack requires a Slack MCP server in your environment. This plugin does not bundle one. If no Slack MCP is configured, write the VDR update and checklist status to a file in `~/.hermes/plugins/config/hermes-the-firm/corporate-legal/deals/[code]/updates/[date].md` and notify the user — do not fail silently.

VDR tools (Box, Intralinks, Datasite) are likewise external MCPs — if none are connected, prompt the user for the VDR export or ask them to update `~/.hermes/plugins/config/hermes-the-firm/corporate-legal/deals/[code]/vdr-inventory.md` manually.

## What it does

1. Query VDR for documents added since last run.
2. Map new docs to request list categories.
3. Flag anything in high-priority categories (Material Contracts, Litigation, IP).
4. Run closing-checklist Mode 4 if it's briefing day.
5. Post to deal channel.

## Output

```
📁 **VDR update — [deal code] — [date]**

**New since [last run]:** [N] docs

**Priority categories:**
• /02-Contracts/Customer/ — [N] new ([filenames])
• /05-Litigation/ — [N] new ⚠️

**Other:** [N] docs in [categories]

[If briefing day: closing checklist status per Mode 4]
```

## What it does NOT do

- Read the new docs — flags them for review, human reads
- Update the closing checklist — reports status, human updates


## Scheduling

Upstream ran this definition as a scheduled Claude Code agent. Hermes has no self-scheduling agents: run it on demand (or via a `cronjob` that prompts "run the dataroom-watcher check"), then follow the body below.
