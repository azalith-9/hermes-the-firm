---
name: registry-sync
description: >
  Periodic check of watched registries for new and updated skills. Posts
  notifications per update preferences. Trigger: "sync registries", "anything
  new", or on schedule.
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from anthropics/claude-for-legal (plugin 'legal-builder-hub', Apache-2.0) by tools_dev/port_upstream.py.
Tool names, config paths, and /legal-builder-hub:{skill} invocations were
rewritten to Hermes equivalents. Hand adjustments are tracked in
tools_dev/MANUAL_FIXUPS.md — do not hand-edit regenerated sections.
-->


# Registry Sync Agent

## Purpose

The community ships skills. This agent notices.

## Schedule

Weekly by default.

## What it does

1. Read `~/.hermes/plugins/config/hermes-the-firm/legal-builder-hub/PRACTICE.md` → watched registries, installed skills, update preferences.
2. For each registry: fetch index, compare to last sync.
3. New skills: filter by practice profile match, note.
4. Updated skills: check against installed list, diff.
5. Post digest per preferences.

## Output

```
🧰 **Registry sync — [date]**

**Updates available for installed skills:**
• [skill] — [version] → [version] — [one-line changelog]

**New skills matching your profile:**
• [skill] from [registry] — [description]

[If auto-update on: "Applied N updates."]
```

## What it does NOT do

- Install anything without auto-update being explicitly enabled
- Recommend skills outside your practice profile (unless asked)


## Scheduling

Upstream ran this definition as a scheduled Claude Code agent. Hermes has no self-scheduling agents: run it on demand (or via a `cronjob` that prompts "run the registry-sync check"), then follow the body below.
