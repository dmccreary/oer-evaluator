#!/usr/bin/env python3
"""Run the deterministic `inspect` step of the OER Evaluator over many MkDocs textbooks.

This is the code behind the 101-book census in papers/openbook-qr-score. It

  1. finds every directory under --root that looks like a MkDocs textbook
     (has mkdocs.yml and a docs/chapters folder with at least --min-chapters entries),
  2. runs `oer_evaluator.py inspect` on each one, with a per-book time limit,
  3. writes one <out>/<book>/inspect.json per book plus <out>/<book>.log,
  4. writes <out>/census-index.json recording what ran, what failed and how long it took.

No model and no network are used. The books are never modified.

    python3 src/census/run_census.py --root ~/Documents/ws --out ~/oer-census
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

EVALUATOR = Path(__file__).resolve().parent.parent / "oer_evaluator" / "oer_evaluator.py"


def find_books(root: Path, min_chapters: int) -> list[Path]:
    books = []
    for d in sorted(p for p in root.iterdir() if p.is_dir()):
        chapters = d / "docs" / "chapters"
        if (d / "mkdocs.yml").is_file() and chapters.is_dir() and len(list(chapters.iterdir())) >= min_chapters:
            books.append(d)
    return books


def inspect_one(book: Path, out: Path, limit_s: int) -> dict:
    book_out = out / book.name
    log = out / f"{book.name}.log"
    started = time.time()
    try:
        with log.open("w", encoding="utf-8") as fh:
            proc = subprocess.run(
                [sys.executable, str(EVALUATOR), "inspect", str(book), "--out", str(book_out)],
                stdout=fh, stderr=subprocess.STDOUT, timeout=limit_s,
            )
        status = "ok" if proc.returncode == 0 and (book_out / "inspect.json").is_file() else f"exit {proc.returncode}"
    except subprocess.TimeoutExpired:
        status = f"timeout after {limit_s}s"
    return {"book": book.name, "status": status, "seconds": round(time.time() - started, 2)}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", required=True, help="folder that contains the book folders")
    ap.add_argument("--out", required=True, help="output folder (must be outside every book)")
    ap.add_argument("--min-chapters", type=int, default=5, help="skip books with fewer chapter folders (default 5)")
    ap.add_argument("--limit-seconds", type=int, default=150, help="time limit per book (default 150)")
    ap.add_argument("--jobs", type=int, default=1, help="books to inspect in parallel (default 1)")
    ap.add_argument("--only", nargs="*", help="inspect only these book folder names")
    a = ap.parse_args()

    root, out = Path(a.root).expanduser().resolve(), Path(a.out).expanduser().resolve()
    out.mkdir(parents=True, exist_ok=True)
    books = find_books(root, a.min_chapters)
    if a.only:
        books = [b for b in books if b.name in set(a.only)]
    if not books:
        print(f"No MkDocs textbooks found under {root}", file=sys.stderr)
        return 1
    print(f"Inspecting {len(books)} books from {root} into {out} ({a.jobs} at a time)")

    started = time.time()
    with ThreadPoolExecutor(max_workers=max(1, a.jobs)) as pool:
        results = list(pool.map(lambda b: inspect_one(b, out, a.limit_seconds), books))
    failed = [r for r in results if r["status"] != "ok"]
    for r in failed:
        print(f"  FAILED {r['book']}: {r['status']}")

    index = {"root": str(root), "min_chapters": a.min_chapters, "books": len(books), "failed": len(failed),
             "total_seconds": round(time.time() - started, 1), "results": results}
    (out / "census-index.json").write_text(json.dumps(index, indent=2), encoding="utf-8")
    print(f"Done: {len(books) - len(failed)} ok, {len(failed)} failed, {index['total_seconds']} s total")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
