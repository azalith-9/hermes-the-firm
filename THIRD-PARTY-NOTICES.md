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
