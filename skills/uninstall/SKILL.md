---
name: uninstall
description: >
  Uninstall a community skill that was installed via the hub. Confirms before
  deleting files, refuses to touch first-party plugin skills, and logs every
  action. Use when the user wants to fully remove a community skill
  ("uninstall [skill]", "remove this skill") rather than just disable it.
argument-hint: "[skill name]"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from anthropics/claude-for-legal (plugin 'legal-builder-hub', Apache-2.0) for Hermes Agent.
Tool names, config paths, and /legal-builder-hub:{skill} invocations were
rewritten to Hermes equivalents. Hand adjustments are tracked in
Regenerated sections are maintained upstream of this repository.
-->


# /uninstall

Run the `uninstall` workflow from the skill-manager reference skill against
the named skill.

Safety rules:

1. **Only uninstall community skills installed through this hub.** Check
   `~/.hermes/plugins/config/hermes-the-firm/legal-builder-hub/install-log.yaml`
   and the PRACTICE.md installed starter pack table. If the skill is not recorded
   there, refuse and tell the user.
2. **Never uninstall a first-party plugin's skill.** The 12 core plugins that
   ship with hermes-the-firm are off-limits from this command. If the named
   skill resolves to a path inside one of those plugins, refuse.
3. **Confirm before removing files.** Show the user every path that will be
   deleted. Proceed only on explicit `yes`.
4. **Log the uninstall.** Append to `install-log.yaml` with action `uninstall`
   and timestamp so the audit trail is intact.

If the user wants to stop a skill from running but keep the files (e.g., for
later re-enable, or to preserve configuration), suggest `hermes-the-firm:disable`
instead.

> Detailed uninstall, disable, and re-enable workflows live in the
> `skill-manager` reference skill — load it before doing substantive work.
