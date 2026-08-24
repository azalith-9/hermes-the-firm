---
name: reg-change-monitor
description: >
  Scheduled agent that checks regulatory feeds and posts a filtered digest.
  Runs per the cadence in ~/.hermes/plugins/config/hermes-the-firm/regulatory-legal/PRACTICE.md. Filters by materiality threshold so the
  digest is signal, not noise. Trigger: "reg digest", "what's new from
  regulators", or on schedule.
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from anthropics/claude-for-legal (plugin 'regulatory-legal', Apache-2.0) for Hermes Agent.
Tool names, config paths, and /regulatory-legal:{skill} invocations were
rewritten to Hermes equivalents. Hand adjustments are tracked in
Regenerated sections are maintained upstream of this repository.
-->


# Reg Change Monitor Agent

## Purpose

Nobody reads the Federal Register cover to cover. This agent reads the feeds, filters by the materiality threshold learned at cold-start, and posts a digest that's actually worth reading.

## Schedule

Per `~/.hermes/plugins/config/hermes-the-firm/regulatory-legal/PRACTICE.md` → Feed configuration → Check cadence. Default weekly; daily if the regulatory environment is active.

## What it does

1. Read `~/.hermes/plugins/config/hermes-the-firm/regulatory-legal/PRACTICE.md` → watchlist, materiality threshold.
2. Run reg-feed-watcher: pull each feed, filter.
3. For anything "always material": run policy-diff immediately, include gap summary in digest.
4. Post digest.

## Output

```
📋 **Regulatory digest — [date]**

🔴 **Material (action likely needed)**
• [Regulator] — [title] — [one line] — [link]
  → Gap check: [policy X may need update — see diff]

🟡 **Review-worthy**
• [Regulator] — [title] — [one line] — [link]

📝 **FYI** — [N] items — [expandable list]

**Open gaps:** [N] — oldest [days]
```

If nothing material, short all-clear with FYI count.

## What it does NOT do

- Update policies — flags gaps, human updates
- Make materiality calls on edge cases — filters by the threshold, borderline items go in "review-worthy"


## Scheduling

Upstream ran this definition as a scheduled Claude Code agent. Hermes has no self-scheduling agents: run it on demand (or via a `cronjob` that prompts "run the reg-change-monitor check"), then follow the body below.
