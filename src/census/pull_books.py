#!/usr/bin/env python3
"""Bring every candidate book repository up to date with `git pull --ff-only`, and record what happened.

Run this before run_census.py so the census describes the latest published versions.
It never merges, rebases or creates worktrees: `--ff-only` either fast-forwards a clean
history or refuses. A repository that refuses (diverged history, no upstream, offline,
authentication needed) is reported and left exactly as it was.

For every candidate it writes one row to <out> (default pull-log.csv):
    book, branch, head_before, head_after, dirty, status
where `dirty` is yes when the working tree has uncommitted changes (a pull can still succeed).

    python3 src/census/pull_books.py --root ~/Documents/ws --out pull-log.csv --jobs 4
"""
from __future__ import annotations

import argparse
import csv
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from run_census import find_books  # noqa: E402

ENV = {**os.environ, "GIT_TERMINAL_PROMPT": "0"}   # never wait for a password prompt


def git(repo: Path, *args: str, timeout: int = 90) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True, timeout=timeout, env=ENV)


def pull_one(repo: Path, timeout: int) -> dict:
    row = {"book": repo.name, "branch": "", "head_before": "", "head_after": "", "dirty": "", "status": ""}
    try:
        if git(repo, "rev-parse", "--is-inside-work-tree").returncode != 0:
            row["status"] = "not a git repository"
            return row
        row["branch"] = git(repo, "rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
        row["head_before"] = git(repo, "rev-parse", "--short", "HEAD").stdout.strip()
        row["dirty"] = "yes" if git(repo, "status", "--porcelain", "--untracked-files=no").stdout.strip() else "no"
        if git(repo, "rev-parse", "--abbrev-ref", "@{upstream}").returncode != 0:
            row["status"] = "no upstream branch"
            return row
        p = git(repo, "pull", "--ff-only", "--quiet", timeout=timeout)
        row["head_after"] = git(repo, "rev-parse", "--short", "HEAD").stdout.strip()
        if p.returncode == 0:
            row["status"] = "up to date" if row["head_after"] == row["head_before"] else "updated"
        else:
            row["status"] = "refused: " + (p.stderr.strip().splitlines() or ["unknown error"])[-1][:120]
    except subprocess.TimeoutExpired:
        row["status"] = f"timeout after {timeout}s"
    return row


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", required=True)
    ap.add_argument("--out", default="pull-log.csv")
    ap.add_argument("--min-chapters", type=int, default=1, help="pull every book with at least this many chapter entries (default 1, a superset of the census)")
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--timeout", type=int, default=90, help="seconds allowed for each pull")
    a = ap.parse_args()

    repos = find_books(Path(a.root).expanduser().resolve(), a.min_chapters)
    print(f"Pulling {len(repos)} repositories under {a.root} ({a.jobs} at a time)")
    with ThreadPoolExecutor(max_workers=max(1, a.jobs)) as pool:
        rows = list(pool.map(lambda r: pull_one(r, a.timeout), repos))
    with open(a.out, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["book", "branch", "head_before", "head_after", "dirty", "status"])
        w.writeheader()
        w.writerows(rows)
    counts: dict[str, int] = {}
    for r in rows:
        key = r["status"].split(":")[0]
        counts[key] = counts.get(key, 0) + 1
    print("Result:", counts)
    for r in rows:
        if r["status"].startswith(("refused", "timeout", "not a git")):
            print(f"  {r['book']}: {r['status']}")
    print(f"Wrote {a.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
