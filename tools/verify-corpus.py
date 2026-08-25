#!/usr/bin/env python3
"""Verify a downloaded open-us-law corpus against its SHA256SUMS.json manifest.

Public, generic version: verifies whatever parquet files are present in the
data directory against the manifest the Vaquill repo ships. No hardcoded
jurisdictions — if you downloaded Michigan and federal statutes, it checks
Michigan and federal statutes. Optionally spot-checks that a citation you
care about actually resolves in the downloaded files.

Usage:
    # verify everything in <this-repo>/data/ (the default: the plugin's
    # own data folder — the same place the download commands below put it)
    python3 tools/verify-corpus.py

    # verify a specific directory
    python3 tools/verify-corpus.py --data-dir ~/my-law-data/

    # also confirm specific citations resolve (substring match on the
    # 'citation' column of *_statutes.parquet files)
    python3 tools/verify-corpus.py --cite "MCL 418" --cite "12101"

Exit code 0 = all hashes OK; 1 = mismatch or missing file. Designed for
scripts as well as humans.
"""
import argparse
import hashlib
import json
import os
import sys

DEFAULT_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
MANIFEST = "SHA256SUMS.json"


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def verify_hashes(data_dir):
    """Check every local parquet against the manifest. Returns (ok, checked_count)."""
    manifest_path = os.path.join(data_dir, MANIFEST)
    if not os.path.exists(manifest_path):
        print(f"MISSING {MANIFEST} in {data_dir} — re-download with `hf download`")
        return False, 0

    entries = json.load(open(manifest_path))
    expected = {e["file"]: e for e in entries}

    ok, checked = True, 0
    for name in sorted(expected):
        path = os.path.join(data_dir, name)
        if not name.endswith(".parquet"):
            continue  # only data files matter here
        if not os.path.exists(path):
            continue  # not downloaded — fine, selective pulls are the point
        exp = expected[name]["sha256"]
        got = sha256_of(path)
        match = got == exp
        ok &= match
        checked += 1
        size_mb = os.path.getsize(path) / 1e6
        status = "OK " if match else "BAD"
        detail = f"{got[:12]} expected {exp[:12]}" if not match else f"{got[:12]} ({size_mb:.1f} MB)"
        print(f"{status} {name}  sha256={detail}")

    if checked == 0:
        print(f"\nNo downloaded parquet files found in {data_dir}.")
        print("Pull some first — see README.md, 'Stocking the vault'.")
        return False, 0
    return ok, checked


def check_citations(data_dir, cites):
    """Spot-check that citations resolve in downloaded statute files."""
    try:
        import pyarrow.parquet as pq
    except ImportError:
        print("\n(citation spot-check skipped: pyarrow not installed — "
              "`pip install pyarrow` to enable)")
        return True

    statute_files = sorted(
        f for f in os.listdir(data_dir)
        if f.endswith(".parquet") and "statutes" in f
    )
    if not statute_files:
        print("\n(no statute files downloaded — citation check skipped)")
        return True

    all_found = True
    for fname in statute_files:
        table = pq.read_table(os.path.join(data_dir, fname))
        cols = [c.lower() for c in table.column_names]
        text_col = next((c for c in ("citation", "citation_short", "section_number") if c in cols), None)
        if not text_col:
            continue
        idx = table.column_names[cols.index(text_col)]
        vals = [str(v) for v in table.column(idx).to_pylist()]
        for cite in cites:
            hits = sum(1 for v in vals if cite.lower() in v.lower())
            found = hits > 0
            all_found &= found
            mark = "FOUND" if found else "NOT FOUND"
            print(f"{mark}: '{cite}' -> {hits} sections in {fname}")
    return all_found


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--data-dir", default=DEFAULT_DATA_DIR,
                    help=f"data directory containing parquet files + {MANIFEST} "
                         f"(default: {DEFAULT_DATA_DIR})")
    ap.add_argument("--cite", action="append", default=[],
                    help="citation to spot-check in statute files (repeatable)")
    args = ap.parse_args()

    data_dir = os.path.expanduser(args.data_dir)
    if not os.path.isdir(data_dir):
        print(f"No such directory: {data_dir}")
        sys.exit(1)

    print(f"Verifying corpus in {data_dir}\n")
    hashes_ok, n = verify_hashes(data_dir)
    if n:
        summary = f"\n{n} file{'s' if n != 1 else ''} verified against {MANIFEST}"
        summary += " — ALL HASHES OK" if hashes_ok else " — HASH MISMATCH(S). Re-download before citing."
        print(summary)

    cites_ok = True
    if args.cite:
        print()
        cites_ok = check_citations(data_dir, args.cite)

    sys.exit(0 if (hashes_ok and cites_ok) else 1)


if __name__ == "__main__":
    main()
