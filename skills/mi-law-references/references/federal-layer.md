# Federal and UCC text — served by the firm's open-us-law corpus

In the upstream `claude-legal` plugin this skill physically hosted three
federal corpora as symlinks into the shared `us-federal-debt-corpus` plugin:

- `federal-debt-laws/` — FDCPA, FCRA, TILA, ECOA, Reg-F, Reg-Z, etc.
- `federal-bankruptcy/` — Title 11 U.S.C. chapters 1/3/5/7/11/12/13/15
- `ucc-model/` — Model UCC Articles 1/2/3/9

In **hermes-the-firm** those corpora are not bundled (per the thin-adaptation
decision when this Michigan layer was rolled in). The same primary-law text is
served by the firm's **open-us-law corpus**, which ships COMPLETE and
human-verified for both **federal** (USC + CFR, 274,600 sections) and
**Michigan** (MCL, 40,658 sections).

## How to get the text

Use the **`us-statute-lookup`** skill. It reads the local open-us-law parquet
corpus and returns verbatim, current statute/regulation text with an
`act_status`. Every federal-debt citation in this Michigan layer resolves there
by its citation:

- **FDCPA** — 15 U.S.C. § 1692 (lookup `federal` / `15 USC 1692`)
- **FCRA** — 15 U.S.C. § 1681 (`15 USC 1681`)
- **Reg-F** — 12 CFR 1006 (CFR is in the federal corpus)
- **TILA** — 15 U.S.C. § 1601; **ECOA** — 15 U.S.C. § 1691
- **UCC / chain of title** — Michigan enacted UCC Article 9 at MCL 440.9;
  model-UCC text is also reachable through the corpus

For Michigan primary law the corpus is authoritative too:
`us-statute-lookup` returns current MCL wording (MCL 600 RJA, MCL 445 RCPA /
MCPA, MCL 722 child custody, MCL 554 landlord-tenant, etc.). The curated
MI-specific topical index in `../mi-law-references/references/mi-statutes-debt/`
remains for quick orientation; verify the current text via the corpus.

> Never paraphrase a federal or state statute when you can quote it from the
> corpus. This file is a routing note, not the law.
