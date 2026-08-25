# Upstream tracking

This plugin is a port of [anthropics/claude-for-legal], a Claude Code
plugin marketplace by Anthropic, Apache License 2.0 — rolled together with
two HAQQ Legal AI skill packs (MIT) into one Hermes plugin.

- **Tracked versions:**
  - anthropics/claude-for-legal `main` @ `4a6c651` ("Update plugin content")
  — that upstream ships no NOTICE file (checked at the pinned commit);
  Apache-2.0 §4(d) therefore imposes no NOTICE-preservation obligation.
  Upstream copyright lines are reproduced in THIRD-PARTY-NOTICES.md.
  - haqq-ai/master-claude-for-legal (MIT)
  - haqq-ai/mini-claude-for-legal (MIT, the Louis library)
- **Upstream repos:**
  - https://github.com/anthropics/claude-for-legal
  - https://github.com/haqq-ai/master-claude-for-legal
  - https://github.com/haqq-ai/mini-claude-for-legal
  - Licenses in THIRD-PARTY-NOTICES.md
- **License:** Apache-2.0 (Anthropic) + MIT (HAQQ) — see LICENSE and
  THIRD-PARTY-NOTICES.md

## What is ported

| Upstream | Here |
|---|---|
| 12 first-party plugin skill trees (`<area>/skills/*/SKILL.md` + references) | `skills/<flat-name>/` |
| 10 scheduled agents (`<area>/agents/*.md`) | skills with a Scheduling section; leave-tracker merged as a reference doc |
| Practice-profile templates (`<area>/CLAUDE.md`) | `templates/<area>-PRACTICE.md` |
| Shared templates (`references/company-profile-template.md`, `dashboard-template.md`) | `references/` (rewritten) |
| Per-plugin `.mcp.json` connector declarations | `references/upstream-mcp.json` (provenance only) |
| master-claude-for-legal: 6 skills + 15 refs + 3 governance templates | `skills/` + `references/firm-admin/` + `templates/firm-admin-*` |
| mini-claude-for-legal: 982 skills in 47 categories (Louis library) | `skills/<category-prefixed-flat>/`, owner `louis/<category>` |

Not ported: `external_plugins/cocounsel-legal` (vendor-maintained) and
`managed-agent-cookbooks/` (targets Claude Code's managed-agent runtime;
see the port-decision notes in our internal toolchain).

## Re-syncing from a new upstream release

Re-syncs run through our internal port toolchain, which is not part
of this public distribution. Public verification after any re-sync:

```bash
python3 -m pytest tests/ -q
```

(A full per-skill validation sweep runs at release time.)

Regeneration rebuilds `skills/`, `templates/`, `references/*.json`,
and shared reference files wholesale; hand edits there will be lost.

`tests/test_port.py` is the regression gate: leak patterns, frontmatter/
dir name equality, dangling `hermes-the-firm:<skill>` refs, template
coverage per area, agent scheduling notes, all-three-sources-present,
and Louis YAML validity.
