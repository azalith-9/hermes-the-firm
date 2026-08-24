---
name: us-statute-lookup
description: >-
  Look up US primary law — state statutes, the US Code, state constitutions, and court rules — in the local open-us-law corpus. Use when an answer needs the actual statutory text, not a summary: verify what a statute says, quote a section verbatim, or check current force status before relying on either.
---

<!--
HERMES PORT NOTE
Generated for hermes-the-firm from the open-us-law corpus (Vaquill, data CC BY 4.0). Coverage claims are read from the
corpus's own coverage manifest at port time and recorded in
references/us-law-coverage.json — never hand-asserted.
-->

# US Statute Lookup (open-us-law corpus)

You have access to a structured corpus of US primary law: ~3M sections of
state statutes (all 50 states + territories + USC), constitutions, court
rules, and partial state/federal regulations, normalized to one parquet
schema with `act_status` (`in_force`, `repealed`, ...) and deterministic
citations.

## Data location

The corpus is NOT bundled with this plugin (it is multi-GB). Check these
locations, in order:

1. `$OPEN_US_LAW_DIR` environment variable
2. `~/data/open-us-law/` (parquet files named `us_< jurisdiction>_<corpus>.parquet`)
3. If absent: tell the user how to fetch it —
   `huggingface.co/datasets/vaquill/open-us-law` or the R2 mirror at
   `oss-data-us.vaquill.ai` (see that project's README). Do not fabricate
   statute text from memory instead; say the corpus is not installed and
   offer to install it.

## Procedure

1. Identify the jurisdiction (state code) and the statute at issue.
2. Check `references/us-law-coverage.json` (next to this file) BEFORE
   trusting any answer from the corpus: is this jurisdiction
   `coverage_verified: true`? Is `coverage_status` `complete`, or only
   `thin`/`partial`? A missing statute in a `partial` jurisdiction means
   "may exist but not be ingested", NOT "does not exist".
3. Load the matching parquet (`pandas`/`polars`/DuckDB all read it).
4. Search by citation pattern first (deterministic), full-text second.
5. Quote the exact section text with its citation and `act_status`.
6. Every answer states: jurisdiction, citation, status as of the corpus
   snapshot date, and whether the jurisdiction's coverage is verified.

## Hard rules

- Never paraphrase a statute when you can quote it.
- Never present corpus text as legal advice; it is the raw law.
- Statutes change. The corpus is a dated snapshot. Flag anything
  time-sensitive (deadlines, amounts, procedures) for verification
  against the official source listed in the coverage file.
