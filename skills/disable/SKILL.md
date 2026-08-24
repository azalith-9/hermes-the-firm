---
name: disable
description: >
  Disable a community skill installed through the hub without removing its
  files. Use when the user wants to temporarily quiet a community skill
  ("disable [skill]"), stop its hooks from firing while keeping its config,
  or re-enable a previously disabled skill.
argument-hint: "[skill name]"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from anthropics/claude-for-legal (plugin 'legal-builder-hub', Apache-2.0) for Hermes Agent.
Tool names, config paths, and /legal-builder-hub:{skill} invocations were
rewritten to Hermes equivalents. Hand adjustments are tracked in
Regenerated sections are maintained upstream of this repository.
-->


# /disable

Run the `disable` workflow from the skill-manager reference skill against the
named skill.

What disable does:

- Renames the skill's `SKILL.md` to `SKILL.md.disabled` so the agent no longer
  discovers it as an active skill. Files, references, templates, and config
  stay in place.
- If the skill ships hooks in `hooks/hooks.json`, also rename that file to
  `hooks.json.disabled` so no automatic triggers fire while the skill is
  disabled.
- Logs the action to
  `~/.hermes/plugins/config/hermes-the-firm/legal-builder-hub/install-log.yaml`.

Safety rules:

1. **Only disable community skills installed through this hub.** Same check
   as uninstall — consult the install log and PRACTICE.md installed table.
2. **Never disable a first-party plugin's skill.** Off-limits.
3. **Confirm before renaming.** Show the paths, get explicit `yes`.

Re-enable by running the command again with the same skill name — the
skill-manager workflow recognizes a disabled skill and flips the rename back.

> Detailed uninstall, disable, and re-enable workflows live in the
> `skill-manager` reference skill — load it before doing substantive work.
