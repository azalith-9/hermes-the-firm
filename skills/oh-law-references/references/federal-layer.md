# Federal and UCC text — served by the firm's open-us-law corpus

In the upstream `claude-legal` plugin this skill physically hosted three
federal corpora as symlinks into the shared `us-federal-debt-corpus` plugin:

- `federal-debt-laws/` — FDCPA, FCRA, TILA, ECOA, Reg-F, Reg-Z, etc.
- `federal-bankruptcy/` — Title 11 U.S.C. chapters 1/3/5/7/11/12/13/15
- `ucc-model/` — Model UCC Articles 1/2/3/9

In **hermes-the-firm** those corpora are not bundled (thin-adaptation
decision when this state layer was rolled in). The same primary-law text is
served by the firm's **open-us-law corpus**, COMPLETE and human-verified for
both **federal** (USC + CFR, 274,600 sections) and this state's code.

## How to get the text

Use the **`us-statute-lookup`** skill, which reads the local open-us-law
parquet corpus and returns verbatim, current statute/regulation text. Every
federal-debt citation in this layer resolves there by citation:

- **FDCPA** — 15 U.S.C. § 1692 (`15 USC 1692`)
- **FCRA** — 15 U.S.C. § 1681 (`15 USC 1681`)
- **Reg-F** — 12 CFR 1006 (CFR is in the federal corpus)
- **TILA** — 15 U.S.C. § 1601; **ECOA** — 15 U.S.C. § 1691
- **UCC / chain of title** — this state's enacted UCC; model-UCC text is
  also reachable through the corpus

State primary law is authoritative there too. The curated topical index in
`oh-statutes-debt/` remains for quick orientation; verify current text via the corpus.

> Never paraphrase a federal or state statute when you can quote it from
> the corpus. This file is a routing note, not the law.
