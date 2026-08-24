---
name: us-citation-verify
description: >-
  Verify a claimed US legal citation against primary law in the local open-us-law corpus — catch hallucinated cites, wrong section numbers, repealed provisions, and quotes that don't match the text. Use before filing, sending, or relying on any draft that cites US statutes.
---

<!--
HERMES PORT NOTE
Generated for hermes-the-firm from the open-us-law corpus (Vaquill, data CC BY 4.0). Coverage claims are read from the
corpus's own coverage manifest at port time and recorded in
references/us-law-coverage.json — never hand-asserted.
-->

# US Citation Verification (open-us-law corpus)

Round-trip every US citation in a draft against the actual statutory text.
Companion to `firm-admin:citation-verifier` (which handles document-scope
verification); this one goes to primary law.

## Procedure

1. Extract every citation: statutes, code sections, court rules.
2. For each, resolve jurisdiction + citation scheme (the coverage file
   records each jurisdiction's scheme, e.g. Michigan `act.section`).
3. Pull the cited section from the corpus. Compare:
   - does the section number exist?
   - does the quoted text match verbatim?
   - is the section `in_force`, or repealed/renumbered?
   - does the proposition the draft claims actually match the text?
4. Mark every cite VERIFIED / MISMATCH / NOT FOUND / OUT-OF-COVERAGE.
5. `NOT FOUND` in a `partial`-coverage jurisdiction is inconclusive, not
   a refutation — say so and point at the official source.
6. Report a table: cite | verdict | actual text/status | fix needed.

## Hard rules

- A fabricated cite that survives because the corpus lacks coverage must
  still be flagged UNVERIFIED — absence of evidence here is not clearance.
- Case law is NOT in this corpus; flag case citations as unverified by
  this tool rather than guessing.
