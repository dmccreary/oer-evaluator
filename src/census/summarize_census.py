#!/usr/bin/env python3
"""Summarize a census made by run_census.py.

Reads <census-dir>/*/inspect.json and prints the statistics quoted in the paper
(papers/openbook-qr-score, "Scripted census of 101 textbooks"):

  * how many of the 13 book-level checks (P1..P13) each book passed, and the distribution,
  * the pass count for each check,
  * the share of internal links that resolve (check P11),
  * how many components were inventoried, by type.

With --csv it also writes the per-book table used for the census histogram figure
(columns: book, checks_passed, checks_total, components, p11_internal_percent).

    python3 src/census/summarize_census.py ~/oer-census --csv papers/openbook-qr-score/figures/census-book-checks.csv
"""
from __future__ import annotations

import argparse
import csv
import json
import statistics as st
import sys
from collections import Counter
from pathlib import Path


def load(census: Path) -> list[dict]:
    rows = []
    for f in sorted(census.glob("*/inspect.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        checks = d["book_checks"]
        p11 = checks.get("P11", {}).get("value")
        rows.append({
            "book": d["run"]["book_dir"],
            "checks": {k: v["status"] for k, v in checks.items()},
            "passed": sum(1 for v in checks.values() if v["status"] == "pass"),
            "total": len(checks),
            "component_types": Counter(c["type"] for c in d["inventory"]["components"]),
            "p11_pct": p11.get("internal_percent") if isinstance(p11, dict) else None,
        })
    return rows


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("census", help="folder written by run_census.py")
    ap.add_argument("--csv", help="write the per-book table to this CSV path")
    a = ap.parse_args()

    rows = load(Path(a.census).expanduser())
    if not rows:
        print("No inspect.json files found.", file=sys.stderr)
        return 1
    n = len(rows)
    passed = [r["passed"] for r in rows]
    print(f"Books: {n}   checks per book: {sorted({r['total'] for r in rows})}")
    print(f"Checks passed per book: mean {st.mean(passed):.1f}, median {st.median(passed):g}, min {min(passed)}, max {max(passed)}")
    print(f"Books passing 5 or fewer: {sum(1 for p in passed if p <= 5)};  passing 10 or more: {sum(1 for p in passed if p >= 10)}")
    print("Distribution (checks passed: books):", dict(sorted(Counter(passed).items())))

    print("\nPer-check results (pass / fail / N/A):")
    names = sorted({k for r in rows for k in r["checks"]}, key=lambda k: int(k[1:]))
    for k in names:
        c = Counter(r["checks"].get(k) for r in rows)
        print(f"  {k:<4} pass {c['pass']:>3}  fail {c['fail']:>3}  N/A {c['N/A']:>3}")

    pct = [r["p11_pct"] for r in rows if r["p11_pct"] is not None]
    if pct:
        print(f"\nInternal links resolved (P11): median {st.median(pct):.1f}%, min {min(pct):.1f}%, "
              f"books at 100%: {sum(1 for p in pct if p >= 100)}, books at 99% or more: {sum(1 for p in pct if p >= 99)}")

    types = Counter()
    for r in rows:
        types.update(r["component_types"])
    print(f"\nComponents inventoried: {sum(types.values())}  {dict(types.most_common())}")

    if a.csv:
        with open(a.csv, "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(["book", "checks_passed", "checks_total", "components", "p11_internal_percent"])
            for r in rows:
                w.writerow([r["book"], r["passed"], r["total"], sum(r["component_types"].values()),
                            "" if r["p11_pct"] is None else r["p11_pct"]])
        print(f"\nWrote {a.csv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
