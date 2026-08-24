---
name: plain-language-letters
description: >
  Reference: DEPRECATED — use `/client-letter` for routine correspondence or
  `/status client` for substantive updates. Split into two more focused skills
  during the v2 rebuild. Kept as a redirect for migration.
user-invocable: false
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from anthropics/claude-for-legal (plugin 'legal-clinic', Apache-2.0) by tools_dev/port_upstream.py.
Tool names, config paths, and /legal-clinic:{skill} invocations were
rewritten to Hermes equivalents. Hand adjustments are tracked in
tools_dev/MANUAL_FIXUPS.md — do not hand-edit regenerated sections.
-->


# [DEPRECATED] Plain-Language Letters → see `/client-letter` and `/status client`

This skill was split during the v2 rebuild:

- **Routine correspondence** (appointment confirms, document requests, brief
  "we filed it" updates) → `skills/client-letter/` — use `/client-letter [type]`

- **Substantive client status updates** → `skills/status/` in client-facing
  mode — use `/status client`

Both apply the plain-language standards (reading level, no jargon) from PRACTICE.md.

See the respective SKILL.md files for full workflows.
