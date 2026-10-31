#!/usr/bin/env python3
"""oer-evaluator command line (skill v0.1, spec v0.4).

  inspect      inventory + Tier 1 checks + findability inputs      (no model, no network)
  findability  run the retrieval test once queries have been written
  report       compute the funnel and headline, write report.json and report.md
  run          inspect, then findability if queries exist, then report

The book under evaluation is never modified. Output goes to --out, which must
not be inside the book.
"""
from __future__ import annotations

import argparse
import datetime as dt
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import checks_book, checks_component, findability, funnel, inventory, report, safety  # noqa: E402
from common import SKILL_VERSION, SPEC_VERSION, read_json, write_json  # noqa: E402

DEFAULT_SEARCH_HOME = os.environ.get("OER_SEARCH_MICROSIMS", str(Path.home() / "projects" / "search-microsims"))


def _default_out(book: Path) -> Path:
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    return Path.home() / "oer-evaluator-reports" / book.name / stamp


def _inside(child: Path, parent: Path) -> bool:
    try:
        child.resolve().relative_to(parent.resolve())
        return True
    except ValueError:
        return False


def cmd_inspect(a) -> int:
    book = Path(a.book).expanduser().resolve()
    if not (book / "docs").is_dir() or not (book / "mkdocs.yml").exists():
        print(f"error: {book} is not a MkDocs book (need mkdocs.yml and docs/)", file=sys.stderr)
        return 2
    out = Path(a.out).expanduser().resolve() if a.out else _default_out(book)
    if _inside(out, book):
        print(f"error: --out must be outside the book ({book}); the book is never modified", file=sys.stderr)
        return 2
    out.mkdir(parents=True, exist_ok=True)

    inv = inventory.build_inventory(book)
    bres, ctx = checks_book.run_book_checks(book, inv, a.check_external)
    comps, meta_by_id = {}, {}
    site_wide = checks_component.site_wide_scripts(book)
    graph = checks_component.load_learning_graph(book)
    for comp in inv["components"]:
        r = checks_component.run_component_checks(book, comp, inv, bres,
                                                  shared_as_declared=a.shared_libs_as_declared,
                                                  check_external=a.check_external, site_wide=site_wide, graph=graph)
        comps[comp["id"]] = {"checks": r["checks"], "interactivity": r["interactivity"], "metadata_desc": r["metadata"]}
        raw, _ = checks_component.load_metadata(book, comp)
        meta_by_id[comp["id"]] = raw
    state = {
        "run": {"book_path": str(book), "book_name": ctx["site_name"] or book.name, "book_dir": book.name,
                "site_url": ctx["site_url"], "out_dir": str(out),
                "options": {"check_external": a.check_external, "shared_libs_as_declared": a.shared_libs_as_declared},
                "scope": "v0.1: Tier 1 checks, inventory, interactivity, findability; Tier 2 judgments not run"},
        "inventory": inv, "book_checks": bres, "components": comps,
        "embedded_instructions": safety.find_embedded_instructions(book, inv),
        "site_wide_scripts": site_wide,
    }
    write_json(out / "inspect.json", state)
    prep = findability.prepare(book, inv, out, meta_by_id)
    n_sims = prep["prepared"]
    print(f"inspected {book.name}: {len(inv['components'])} components "
          f"({', '.join(f'{k} {v}' for k, v in sorted(inv['counts_by_type'].items()))})")
    print(f"book checks: {sum(1 for v in bres.values() if v['status']=='pass')} pass, "
          f"{sum(1 for v in bres.values() if v['status']=='fail')} fail")
    print(f"findability inputs written for {n_sims} MicroSims/infographics")
    if state["embedded_instructions"]:
        print(f"WARNING: instruction-like text addressed to an evaluator found in "
              f"{len(state['embedded_instructions'])} file(s); it is recorded as a finding and is not followed")
    print(f"output: {out}")
    print(f"next: write {findability.QUERIES_PER_TYPE * len(findability.QUERY_TYPES)} queries per component into "
          f"{prep['queries_dir']}, then run: oer_evaluator.py findability {out}")
    return 0


def cmd_findability(a) -> int:
    out = Path(a.out).expanduser().resolve()
    st = read_json(out / "inspect.json")
    if not st:
        print("error: run `inspect` first (no inspect.json)", file=sys.stderr)
        return 2
    book = Path(st["run"]["book_path"])
    comp_meta = {}
    for comp in st["inventory"]["components"]:
        raw, _ = checks_component.load_metadata(book, comp)
        comp_meta[comp["id"]] = {"raw": raw, "desc": st["components"][comp["id"]]["metadata_desc"]}
    res = findability.run(book, st["inventory"], out, comp_meta, Path(a.search_home).expanduser(),
                          st["run"]["site_url"], st["run"]["book_dir"], limit=a.limit)
    write_json(out / "findability" / "results.json", res)
    if res["status"] != "ran":
        print(f"findability not run: {res.get('reason')}")
        return 1
    done = [c for c in res["components"].values() if c.get("status") == "scored"]
    pending = [k for k, c in res["components"].items() if c.get("status") != "scored"]
    print(f"findability: {len(done)} scored, {len(pending)} waiting (ISE)")
    for k in pending[:8]:
        print(f"  {k}: {res['components'][k].get('reason')}")
    return 0


def cmd_report(a) -> int:
    out = Path(a.out).expanduser().resolve()
    st = read_json(out / "inspect.json")
    if not st:
        print("error: run `inspect` first (no inspect.json)", file=sys.stderr)
        return 2
    fnd = read_json(out / "findability" / "results.json") or {
        "status": "ISE", "reason": "the findability step was not run", "components": {}}
    judg = read_json(Path(a.judgments)) if a.judgments else None
    comps = {}
    for cid, c in st["components"].items():
        f = (fnd.get("components") or {}).get(cid, {})
        rj6 = f.get("RJ6")
        ctype = next(x["type"] for x in st["inventory"]["components"] if x["id"] == cid)
        if ctype not in ("microsim", "interactive-infographic"):
            rj6 = None  # no search tool indexes this type
        jc = ((judg or {}).get("components") or {}).get(cid)
        c = dict(c)
        c["reuse"] = funnel.evaluate_component(c["checks"], rj6, c["interactivity"], jc)
        comps[cid] = c
    head = funnel.headline(st["book_checks"], comps, judg, st["inventory"]["chapters"])
    # findability for types the catalog does not index is ISE by construction
    for cid, c in comps.items():
        ctype = next(x["type"] for x in st["inventory"]["components"] if x["id"] == cid)
        if ctype not in ("microsim", "interactive-infographic"):
            fnd.setdefault("components", {}).setdefault(cid, {
                "status": "ISE", "RJ6": None,
                "reason": "no search tool in this release indexes this component type (the catalog indexes MicroSims)"})
    st["run"]["site_wide_scripts"] = st.get("site_wide_scripts", [])
    rep = report.build_report(run=st["run"], inventory=st["inventory"], book_checks=st["book_checks"],
                              components=comps, findability=fnd, head=head, judgments_supplied=bool(judg),
                              embedded_instructions=st.get("embedded_instructions", []))
    write_json(out / "report.json", rep)
    (out / "report.md").write_text(report.render_markdown(rep), encoding="utf-8")
    print(f"report: {out / 'report.json'}")
    print(f"        {out / 'report.md'}")
    q, r = head["Q"], head["R"]
    print(f"Q: {q['value'] if q['value'] is not None else 'not available'}   R: {r['value'] if r['value'] is not None else 'not available'}")
    return 0


def cmd_run(a) -> int:
    rc = cmd_inspect(a)
    if rc:
        return rc
    out = a.out or None
    # recover the out dir inspect chose
    book = Path(a.book).expanduser().resolve()
    outp = Path(a.out).expanduser().resolve() if a.out else None
    if outp is None:
        base = Path.home() / "oer-evaluator-reports" / book.name
        outp = sorted(base.iterdir())[-1]
    qdir = outp / "findability" / "queries"
    if not a.skip_findability and qdir.exists() and any(qdir.glob("*.json")):
        findability_args = argparse.Namespace(out=str(outp), search_home=a.search_home, limit=None)
        cmd_findability(findability_args)
    return cmd_report(argparse.Namespace(out=str(outp), judgments=None))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--version", action="version", version=f"oer-evaluator {SKILL_VERSION} (spec {SPEC_VERSION})")
    sub = ap.add_subparsers(dest="cmd", required=True)

    def book_opts(p):
        p.add_argument("book", help="path to the MkDocs book root (contains mkdocs.yml and docs/)")
        p.add_argument("--out", help="output directory; must be outside the book")
        p.add_argument("--check-external", action="store_true", help="fetch external links and CDN URLs (network)")
        p.add_argument("--shared-libs-as-declared", action="store_true",
                       help="treat conventional shared-library files outside a component as declared dependencies (RP1)")

    p = sub.add_parser("inspect", help="inventory and Tier 1 checks")
    book_opts(p)
    p.set_defaults(fn=cmd_inspect)
    p = sub.add_parser("findability", help="run the retrieval test")
    p.add_argument("out")
    p.add_argument("--search-home", default=DEFAULT_SEARCH_HOME)
    p.add_argument("--limit", type=int, default=None, help="score at most N components (for trials)")
    p.set_defaults(fn=cmd_findability)
    p = sub.add_parser("report", help="compute the funnel and write the report")
    p.add_argument("out")
    p.add_argument("--judgments", help="optional JSON of Tier 2 scores (not produced in v0.1)")
    p.set_defaults(fn=cmd_report)
    p = sub.add_parser("run", help="inspect, findability if queries exist, report")
    book_opts(p)
    p.add_argument("--search-home", default=DEFAULT_SEARCH_HOME)
    p.add_argument("--skip-findability", action="store_true")
    p.set_defaults(fn=cmd_run)

    a = ap.parse_args()
    return a.fn(a)


if __name__ == "__main__":
    raise SystemExit(main())
