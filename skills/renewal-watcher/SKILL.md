---
name: renewal-watcher
description: >
  Scheduled agent that checks the renewal register and posts what's coming up.
  Runs weekly by default. Posts to the channel named in `~/.hermes/plugins/config/hermes-the-firm/commercial-legal/PRACTICE.md` → House style
  → Renewal alerts. Trigger phrases: "what's renewing", "check renewals",
  "renewal report", or on schedule.
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from anthropics/claude-for-legal (plugin 'commercial-legal', Apache-2.0) for Hermes Agent.
Tool names, config paths, and /commercial-legal:{skill} invocations were
rewritten to Hermes equivalents. Hand adjustments are tracked in
Regenerated sections are maintained upstream of this repository.
-->


# Renewal Watcher Agent

## Purpose

The renewal register only helps if someone reads it. This agent reads it for you, weekly, and tells the channel what's coming up before the cancel-by windows close.

## Schedule

Weekly, Monday morning. Configurable — if the contracts volume is high, daily is fine; if low, monthly.

## What it does

1. Read `~/.hermes/plugins/config/hermes-the-firm/commercial-legal/PRACTICE.md` to get the alert destination (Slack channel or email list).
2. Load the renewal-tracker skill, run Mode 2 (next 90 days).
3. If there are 🔴 items (cancel-by in 0–13 days), post them immediately regardless of schedule.
4. If the [CLM] is connected and the register hasn't been synced in >30 days, run Mode 3 to refresh.
5. Post the report to the destination.

## Output format

```
📅 **Renewals — week of [date]**

🔴 **Cancel-by in 0–13 days**
• [Counterparty] — cancel by **[date]** ([annual $]) — owner: [business owner]

🟠 **Cancel-by in 14–44 days**
• [Counterparty] — cancel by [date] ([annual $])
• ...

🟡 **Cancel-by in 45–89 days**
• [N] agreements — [link to full register]

**Flagged:** [any with uncapped renewal pricing or notes worth raising]
```

If nothing is due in the next 90 days, post a short all-clear rather than nothing — so people know the agent ran.

## What this agent does NOT do

- Cancel contracts
- Decide whether to renew
- Ping business owners directly — the channel post tags them, they decide what to do
- Modify the register — it reads and reports; additions come from reviews


## Scheduling

Upstream ran this definition as a scheduled Claude Code agent. Hermes has no self-scheduling agents: run it on demand (or via a `cronjob` that prompts "run the renewal-watcher check"), then follow the body below.
