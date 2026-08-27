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

## codearranger — claude-legal (U.S. state + federal civil-practice layer)

- Source: https://github.com/GalacticPlayground/claude-law (the `claude-legal`
  marketplace; checked out locally at `~/projects/claude-law`). Ported
  here: `us-mi-legal-corpus`, `us-az-legal-corpus`, `us-ca-legal-corpus`,
  `us-co-legal-corpus`, `us-in-legal-corpus`, `us-ny-legal-corpus`,
  `us-oh-legal-corpus`, `us-or-legal-corpus`, `us-tn-legal-corpus`,
  `us-wa-legal-corpus`, and `us-federal-debt-corpus` (skills only).
- License: MIT
- Contributes: a per-state civil-practice layer for **nine states** plus a
  federal consumer-credit layer:
  - Michigan (29 `mi-*`), Arizona (28 `az-*`), California (21 `ca-*`),
    Colorado (22 `co-*`), Indiana (23 `in-*`), New York (35 `ny-*`),
    Ohio (30 `oh-*`), Oregon (21 `or-*`), Tennessee (31 `tn-*`),
    Washington (32 `wa-*`).
  - Each state ships venue skills (e.g. Wayne/Third, Oakland/Sixth,
    36th District, King County District/Superior, Maricopa/Pima, the
    NYC Civil/Housing/Commercial courts), statewide court-rule document
    formatting, and drafting/motion/hearing/deadline/filing/pro-se/
    post-judgment procedural skills, plus subject-matter bundles
    (consumer-debt, family-law, landlord-tenant, personal-injury,
    employment, commercial-disputes where the state justifies them).
  - Each state carries a verbatim court-rules corpus + a curated state-code
    index under its `<st>-law-references` skill.
  - Federal consumer-credit layer (5 FCRA/consumer-report skills from
    `us-federal-debt-corpus`): `consumer-report-ordering`,
    `consumer-credit-disputes`, `consumer-report-accuracy`,
    `consumer-harm-documentation`, `consumer-credit-monitoring`.
- Owner-map values: `mi-legal`, `az-legal`, `ca-legal`, `co-legal`,
  `in-legal`, `ny-legal`, `oh-legal`, `or-legal`, `tn-legal`, `wa-legal`,
  and `federal-debt`.

### Thin-adaptation note

Each upstream state plugin symlinked three federal corpora
(`federal-debt-laws/`, `federal-bankruptcy/`, `ucc-model/`) in from the shared
`us-federal-debt-corpus` plugin, plus shipped redundant full-state-code
verbatim dumps. In **hermes-the-firm** those are NOT bundled:

- Federal/UCC primary-law text (FDCPA, FCRA, Reg-F, TILA, ECOA, Title 11,
  model UCC) is served by this repo's existing open-us-law corpus via the
  `us-statute-lookup` skill (federal = USC + CFR, complete + human-verified).
- Full state-code verbatim dumps are likewise covered by the open-us-law
  corpus (every state code COMPLETE + verified).
- Each `<st>-law-references` skill carries a `references/federal-layer.md`
  routing note describing exactly how each federal citation resolves.

See `skills/mi-law-references/references/federal-layer.md` (and the
state-specific equivalents) for the resolution table.

---

## Copyright notices and license texts

Per the MIT License condition ("the above copyright notice and this
permission notice shall be included in all copies or substantial portions
of the Software") and Apache-2.0 §4(a), the upstream copyright notices are
reproduced verbatim below.

### MIT projects — full permission notice (applies to each project listed)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

**Copyright lines:**

- HAQQ master-claude-for-legal: `Copyright (c) 2026 HAQQ Legal AI and contributors`
- HAQQ mini-claude-for-legal (Louis library): `Copyright (c) 2026 HAQQ Legal AI / Stephane Boghossian`
- beshkenadze/us-legal-tools: `Copyright (c) 2024 Aleksandr Beshkenadze <beshkenadze@gmail.com>`
- codearranger/claude-legal (`us-mi-legal-corpus`): `Copyright (c) 2026 codearranger`

### anthropics/claude-for-legal — Apache-2.0

`Copyright 2026 Anthropic PBC` per that repository's licensing headers; the
upstream ships no separate NOTICE file (verified at commit `4a6c651`, see
UPSTREAM.md). This distribution's own Apache-2.0 grant is in LICENSE.

### Vaquill open-us-law data — CC BY 4.0 carve-out

The bundled file `references/us-law-coverage.json` is generated from the
Vaquill open-us-law audited coverage manifest and remains under the
Creative Commons Attribution 4.0 International License (CC BY 4.0); it is
NOT sublicensed under this repository's Apache-2.0 grant.
Copyright (c) 2026 Vaquill AI — compilation and metadata only. The
underlying statutory text is public domain under the government-edicts
doctrine and carries no copyright.

Attribution: Vaquill, "open-us-law"
(https://github.com/vaquill/open-us-law;
https://huggingface.co/datasets/vaquill/open-us-law), licensed under
CC BY 4.0 — https://creativecommons.org/licenses/by/4.0/legalcode
