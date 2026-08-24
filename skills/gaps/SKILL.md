---
name: gaps
description: Open gaps tracker — what's flagged and not yet closed. Use when the user asks "what gaps are open", "gap tracker", "remediation status", or wants to close (--close GAP-ID) or risk-accept (--accept GAP-ID) a tracked gap.
argument-hint: "[optional: --close GAP-ID | --accept GAP-ID]"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from anthropics/claude-for-legal (plugin 'regulatory-legal', Apache-2.0) for Hermes Agent.
Tool names, config paths, and /regulatory-legal:{skill} invocations were
rewritten to Hermes equivalents. Hand adjustments are tracked in
Regenerated sections are maintained upstream of this repository.
-->


# /gaps

1. Read the gap tracker at `~/.hermes/plugins/config/hermes-the-firm/regulatory-legal/gap-tracker.yaml`.
2. If `--close`: mark gap closed with resolution note.
3. If `--accept`: record the risk-acceptance rationale and acceptor, status → risk-accepted.
4. Otherwise: report open gaps by age and materiality.

> Detailed tracker schema, status-report format, owner-notification logic (per-send confirmation, no exceptions), reminder cadence, the close/risk-accept modes, and the consequential-action gate live in the **gap-surfacer** reference skill — load it before doing substantive work.
