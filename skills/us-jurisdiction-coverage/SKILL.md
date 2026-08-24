---
name: us-jurisdiction-coverage
description: >-
  Check what US jurisdictions and corpora the local open-us-law snapshot actually covers before answering a US-law question — verified-complete vs thin vs absent, per corpus type. Use to route questions honestly instead of answering past the data.
---

<!--
HERMES PORT NOTE
Generated for hermes-the-firm from the open-us-law corpus (Vaquill, data CC BY 4.0). Coverage claims are read from the
corpus's own coverage manifest at port time and recorded in
references/us-law-coverage.json — never hand-asserted.
-->

# US Jurisdiction Coverage Check

Reads `references/us-law-coverage.json` (generated from the open-us-law
project's own audited manifest) and reports what can be answered from
primary law locally.

## Procedure

1. Load the coverage JSON. Per jurisdiction it carries:
   `coverage_status` (complete/thin/partial/broken),
   `coverage_verified` (human-audited), `dump_ready`,
   `section_count`, `citation_scheme`, `official_source`.
2. For the user's question, report:
   - statutes: verified? complete?
   - regulations: NOT generally covered yet (only a handful of states;
     federal via eCFR snapshots) — treat regulation questions as
     out-of-corpus unless the snapshot says otherwise.
   - court rules: covered for most states; case law: NOT covered.
3. Give the verdict in plain terms: ANSWERABLE FROM CORPUS /
   PARTIALLY (with what caveat) / NOT IN CORPUS (official source listed).

## Example verdict (illustrative)

Michigan workers' comp: MCL 418 (Workers' Disability Compensation Act)
is inside the Michigan statutory code, which ships COMPLETE and human-
VERIFIED — so statute-level questions are answerable from the corpus,
with agency regulations and case law flagged as outside it.
