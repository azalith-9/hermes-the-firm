# Upstream tracking

This plugin rolls six upstream layers into one Hermes plugin:
[anthropics/claude-for-legal], a Claude Code plugin marketplace by
Anthropic, Apache License 2.0 (the twelve practice departments);
beshkenadze/us-legal-tools, MIT (the federal MCP research connectors);
Vaquill/open-us-law, data CC BY 4.0 (the audited statutory-corpus
coverage manifest); two HAQQ Legal AI skill packs, MIT
(master-claude-for-legal firm AI administration and
mini-claude-for-legal, the 982-skill Louis library); and
codearranger/claude-legal, MIT (ten state civil-practice floors plus
the federal consumer-credit layer).

- **Tracked versions:**
  - anthropics/claude-for-legal `main` @ `4a6c651` ("Update plugin content")
  — that upstream ships no NOTICE file (checked at the pinned commit);
  Apache-2.0 §4(d) therefore imposes no NOTICE-preservation obligation.
  Upstream copyright lines are reproduced in THIRD-PARTY-NOTICES.md.
  - beshkenadze/us-legal-tools (MIT) — the federal MCP connector layer
  - Vaquill/open-us-law (data CC BY 4.0) — the statutory coverage manifest
  - haqq-ai/master-claude-for-legal (MIT)
  - haqq-ai/mini-claude-for-legal (MIT, the Louis library)
  - codearranger/claude-legal, ten `us-<state>-legal-corpus` plugins
    + `us-federal-debt-corpus` skills (MIT)
- **Upstream repos:**
  - https://github.com/anthropics/claude-for-legal
  - https://github.com/beshkenadze/us-legal-tools
  - https://github.com/vaquill/open-us-law
  - https://github.com/haqq-ai/master-claude-for-legal
  - https://github.com/haqq-ai/mini-claude-for-legal
  - https://github.com/GalacticPlayground/claude-law
  - Licenses in THIRD-PARTY-NOTICES.md
- **License:** Apache-2.0 (Anthropic) + MIT (HAQQ, Beshkenadze,
  codearranger) + CC BY 4.0 (Vaquill data) — see LICENSE and
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
| beshkenadze us-legal-tools: 4 federal MCP connectors (eCFR, Federal Register, CourtListener, govinfo) | `skills/` (owner `federal-mcp`) + wiring catalog `references/federal-mcp-catalog.json`; the MCP servers run from npm at use time, not from this repo |
| Vaquill open-us-law: audited 51-jurisdiction coverage manifest | `references/us-law-coverage.json` + four primary-law skills (owner `primary-law`); the multi-GB statutory corpus stays external, installed separately |
| codearranger `us-<state>-legal-corpus` ×10 (az/ca/co/in/mi/ny/oh/or/tn/wa): state skills + court-rules corpus + curated state-code index; `us-federal-debt-corpus` consumer-credit skills | `skills/<st>-*` (owners `<st>-legal`); reference corpus under each `<st>-law-references/references/`; federal/UCC text thin-adapted to the open-us-law corpus — see THIRD-PARTY-NOTICES.md |

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
coverage per area, agent scheduling notes, all-sources-represented
(including UPSTREAM.md naming every upstream layer), and Louis YAML
validity.
