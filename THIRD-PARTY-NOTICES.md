# Third-party notices

hermes-the-firm bundles mechanically-ported content from three upstream
projects. Each skill carries an HTML port note naming its provenance;
`references/owner-map.json` is the machine-readable index.

## anthropics/claude-for-legal

- Source: https://github.com/anthropics/claude-for-legal
- License: Apache License 2.0 (see LICENSE)
- Contributes: the twelve practice departments (skills, watcher agents,
  practice-profile templates), shared company-profile/dashboard templates.
- Owner-map values: `<area>` (e.g. `litigation-legal`).

## HAQQ Legal AI — master-claude-for-legal

- Source: https://github.com/haqq-ai/master-claude-for-legal (as distributed
  by HAQQ Legal AI; MIT licensed)
- License: MIT
- Contributes: firm-admin skills (`citation-verifier`, `meeting-brief`,
  `nda-triage`, `status-synthesis`, `version-diff`,
  `firm-admin-tabular-review`), reference docs in
  `references/firm-admin/`, governance templates in
  `templates/firm-admin-*`.
- Owner-map value: `firm-admin`.

## HAQQ Legal AI — mini-claude-for-legal

- Source: https://github.com/haqq-ai/mini-claude-for-legal (the open-source
  Louis skill library; MIT licensed)
- License: MIT
- Contributes: 982 deep-knowledge skills across 47 categories with a
  MENA-first jurisdictional lens.
- Owner-map values: `louis/<category>`.

## beshkenadze — us-legal-tools

- Source: https://github.com/beshkenadze/us-legal-tools
- License: MIT
- Contributes: the federal MCP layer. Skills generated here carry wiring
  instructions for that project's MCP servers (`@us-legal-tools/*-sdk/mcp`);
  the servers themselves run from npm at use time, not from this repo.
- Owner-map value: `federal-mcp`.

## Vaquill — open-us-law

- Source: https://github.com/vaquill/open-us-law; dataset at
  https://huggingface.co/datasets/vaquill/open-us-law
- License: code per upstream repo; **data CC BY 4.0**
- Contributes: `references/us-law-coverage.json` (generated from the
  project's audited coverage manifest) and four primary-law skills.
  The corpus itself is multi-GB and stays external — install separately
  (see the `us-statute-lookup` skill); nothing corpus-sized is bundled.
- Owner-map value: `primary-law`.
