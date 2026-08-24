---
name: us-regulations-status
description: >-
  Check whether a US state or federal administrative-regulations question can be answered from the local open-us-law snapshot, and route to the right fallback when it cannot.
---

<!--
HERMES PORT NOTE
Generated for hermes-the-firm from the open-us-law corpus (Vaquill, data CC BY 4.0). Coverage claims are read from the
corpus's own coverage manifest at port time and recorded in
references/us-law-coverage.json — never hand-asserted.
-->

# US Regulations Coverage Status

State administrative codes are the weakest part of the corpus: only a
subset of states ship regulations (and Michigan is NOT among them in
current snapshots). Federal regulations come from eCFR builds.

## Procedure

1. Read the corpus manifest/index (or `references/us-law-coverage.json`
   plus the snapshot's own index) for the jurisdiction.
2. If regulations for that jurisdiction are present: proceed like
   `us-statute-lookup`, citing title/part/section and noting the
   snapshot date — agency material amends fast.
3. If absent: say so plainly, then offer the honest paths:
   - the state's official admin-code portal (listed in coverage JSON
     where known),
   - federal questions: the eCFR online (always current),
   - installing the next open-us-law snapshot if it adds the corpus.
4. Never approximate a regulation from training memory and present it
   as the current text.
