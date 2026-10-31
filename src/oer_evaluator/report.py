"""Build report.json (the contract with the improvement planner) and report.md."""
from __future__ import annotations

import datetime as dt

from common import REPORT_SCHEMA, SKILL_VERSION, SPEC_VERSION

JUDGMENT_IDS = ["J1", "J2", "J3", "J4", "J5", "J6", "J7", "J8", "J10", "J11",
                "RJ1", "RJ2", "RJ3", "RJ4", "RJ5", "RJ7"]


def build_findings(book_checks: dict, components: dict, inv_by_id: dict, findability: dict) -> list[dict]:
    """Flat list of deterministic findings the planner can consume."""
    out = []
    for cid, res in book_checks.items():
        if res["status"] in ("fail", "ISE"):
            out.append({"check": cid, "level": "book", "unit": {"kind": "book", "id": "book"},
                        "status": res["status"], "value": res["value"],
                        "evidence": res["evidence"][:25], "note": res.get("note")})
    for comp_id, c in components.items():
        t = inv_by_id[comp_id]["type"]
        for k, res in c["checks"].items():
            if res["status"] in ("fail", "ISE"):
                out.append({"check": k, "level": "component",
                            "unit": {"kind": "component", "type": t, "id": comp_id},
                            "status": res["status"], "value": res["value"],
                            "evidence": res["evidence"][:12], "note": res.get("note")})
        f = (findability.get("components") or {}).get(comp_id)
        if f and f.get("RJ6") is not None and f["RJ6"] <= 1:
            out.append({"check": "RJ6", "level": "component",
                        "unit": {"kind": "component", "type": t, "id": comp_id},
                        "status": "fail" if f["RJ6"] == 0 else "partial", "value": f["RJ6"],
                        "evidence": [{"location": comp_id, "detail": f.get("reason", "")}],
                        "note": f.get("diagnostic")})
        if f and f.get("twins_removed"):
            out.append({"check": "duplicate-cluster", "level": "component",
                        "unit": {"kind": "component", "type": t, "id": comp_id},
                        "status": "info", "value": f["twins_removed"],
                        "evidence": [{"location": comp_id, "detail": f"{f['twins_removed']} catalog entries teach the same concept (WHAT similarity >= 0.90)"}],
                        "note": "Consider keeping the highest-quality member and embedding it."})
        d = ((c["checks"].get("RP8") or {}).get("extra") or {}).get("delivery")
        if d and not d["send_code_found"]:
            out.append({"check": "events-delivery", "level": "component",
                        "unit": {"kind": "component", "type": t, "id": comp_id},
                        "status": "info", "value": "no send code found",
                        "evidence": [{"location": f, "detail": "checked for code that sends events off the page"} for f in d["files_checked"][:6]],
                        "note": d["note"]})
        if t == "static-figure" and c["interactivity"] == "L0":
            out.append({"check": "RP8", "level": "component", "kind": "opportunity",
                        "unit": {"kind": "component", "type": t, "id": comp_id},
                        "status": "opportunity", "value": "L0", "evidence": [],
                        "note": "Static figure. Could be made interactive and instrumented."})
    return out


def build_report(*, run: dict, inventory: dict, book_checks: dict, components: dict,
                 findability: dict, head: dict, judgments_supplied: bool,
                 embedded_instructions: list | None = None) -> dict:
    inv_by_id = {c["id"]: c for c in inventory["components"]}
    comp_out = {}
    for cid, c in components.items():
        f = (findability.get("components") or {}).get(cid, {})
        comp_out[cid] = {
            "type": inv_by_id[cid]["type"], "path": inv_by_id[cid]["path"], "title": inv_by_id[cid].get("title"),
            "interactivity": c["interactivity"],
            "checks": c["checks"],
            "RJ6": {"score": f.get("RJ6"), "status": f.get("status", "ISE"),
                    "reason": f.get("reason") or findability.get("reason") or "findability was not run",
                    "rates": f.get("rates"), "by_query_type": f.get("by_query_type"),
                    "twins_removed": f.get("twins_removed"), "diagnostic": f.get("diagnostic"),
                    "queries": f.get("queries", [])},
            "reuse": c["reuse"],
        }
    return {
        "schema": REPORT_SCHEMA, "spec_version": SPEC_VERSION, "skill_version": SKILL_VERSION,
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "run": run,
        "headline": head,
        "book": {"checks": book_checks,
                 "chapters": inventory["chapters"], "chapter_weight_scale": inventory["chapter_weight_scale"]},
        "inventory": {"counts_by_type": inventory["counts_by_type"], "not_detected_types": inventory["not_detected_types"],
                      "notes": inventory["notes"]},
        "components": comp_out,
        "judgments": {k: ("supplied" if judgments_supplied else "not_run") for k in JUDGMENT_IDS},
        "signals": {"sponsor": book_checks.get("P3", {}).get("value"),
                    "embedded_instructions": embedded_instructions or [],
                    "site_wide_scripts": run.get("site_wide_scripts", [])},
        "findability": {k: v for k, v in findability.items() if k != "components"},
        "findings": build_findings(book_checks, components, inv_by_id, findability)
                    + [{"check": "embedded-instructions", "level": e["unit"]["kind"], "unit": e["unit"],
                        "status": "finding", "value": e["patterns"],
                        "evidence": [{"location": e["location"], "detail": "text addressed to an evaluator", "quote": s}
                                     for s in e["snippets"]],
                        "note": "Treated as data and not followed. Review it with the contributor; documentation that quotes an example can also match."}
                       for e in (embedded_instructions or [])],
        "limitations": [
            "Tier 2 judgment indicators (J1-J11, RJ1-RJ5, RJ7) are not run in v0.1. Q and R are therefore not available.",
            "RP2 is a static check. No page was rendered.",
            "External links and CDN URLs were not fetched unless --check-external was used.",
            "The keyword diagnostic is a TF-IDF stand-in, not ItemsJS.",
            "Worked examples and instructor materials have no packaging convention and are not inventoried.",
            "Findability was tested only for MicroSims and interactive infographics, the types the search catalog indexes.",
        ],
    }


def _fmt(v, n=90):
    s = str(v)
    return s if len(s) <= n else s[: n - 1] + "…"


def render_markdown(rep: dict) -> str:
    h = rep["headline"]
    L = []
    L.append(f"# OER Evaluator report: {rep['run']['book_name']}")
    L.append("")
    L.append(f"Spec v{rep['spec_version']} · skill v{rep['skill_version']} · {rep['generated_at']}")
    L.append("")
    L.append("## Headline")
    L.append("")
    L.append("| Number | Value | Why |")
    L.append("|---|---|---|")
    for key, name in (("Q", "Q, overall quality"), ("R", "R, reusable content")):
        x = h[key]
        L.append(f"| {name} | {x['value'] if x['value'] is not None else 'not available'} | {_fmt(x.get('reason') or x.get('note') or '', 200)} |")
    bq, br = h["beside_Q"], h["beside_R"]
    L.append("")
    L.append(f"- **Completeness checks passed:** {bq['completeness_checks_passed']} of {bq['completeness_checks_applicable']} "
             f"(failed: {', '.join(bq['failed']) or 'none'}).")
    rr = br["reuse_ready"]
    L.append(f"- **Reuse-ready components:** {rr['yes']} yes, {rr['no']} definitely not, {rr['not_yet_determined']} not yet determined, of {br['components']}.")
    lv = br["interactivity_levels"]
    L.append(f"- **Interactivity:** L0 {lv.get('L0', 0)}, L1 {lv.get('L1', 0)}, L2 (instrumented) {lv.get('L2', 0)}.")
    L.append(f"- **Provisional:** yes. {'; '.join(h['provisional_because'])}.")
    L.append("")
    L.append("## Book-level checks")
    L.append("")
    L.append("| Check | Status | Value |")
    L.append("|---|---|---|")
    for k, v in rep["book"]["checks"].items():
        L.append(f"| {k} | {v['status']} | {_fmt(v['value'], 110)} |")
    L.append("")
    L.append("## Inventory")
    L.append("")
    for t, n in sorted(rep["inventory"]["counts_by_type"].items()):
        L.append(f"- {t}: {n}")
    for n in rep["inventory"]["notes"]:
        L.append(f"- note: {n}")
    L.append("")
    sims = {cid: c for cid, c in rep["components"].items() if c["type"] in ("microsim", "interactive-infographic")}
    if sims:
        L.append("## MicroSims and infographics")
        L.append("")
        L.append("| Component | Level | RP1 | RP2 | RP3 | RP4 | RP5 | RP6 | RP7 | RP9 | RJ6 | Stage | Ready |")
        L.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
        for cid, c in sorted(sims.items()):
            ck = c["checks"]
            s = lambda k: ck[k]["status"].replace("N/A", "n/a")
            rj6 = c["RJ6"]["score"]
            ru = c["reuse"]["reuse_ready"]
            L.append(f"| {cid} | {c['interactivity']} | {s('RP1')} | {s('RP2')} | {s('RP3')} | {s('RP4')} | {s('RP5')} | {s('RP6')} | {s('RP7')} | {s('RP9')} "
                     f"| {rj6 if rj6 is not None else 'ISE'} | {c['reuse']['stage_reached']} | {'yes' if ru else ('no' if ru is False else '?')} |")
        L.append("")
    fnd = rep["findability"]
    L.append("## Findability test")
    L.append("")
    if fnd.get("status") == "ran":
        cat = fnd["catalog"]
        L.append(f"Catalog: {cat['count']} entries, model {cat['model']}, generated {cat['generated_at']}, "
                 f"{cat['candidates_after_excluding_this_book']} candidates after excluding this book. "
                 f"Bands: reuse >= {cat['bands']['reuse']}, template >= {cat['bands']['template']}. Keyword: {cat['keyword_diagnostic']}.")
    else:
        L.append(f"Not run: {fnd.get('reason', 'findability step was skipped')}. Every RJ6 is ISE (insufficient evidence).")
    L.append("")
    ei = rep["signals"].get("embedded_instructions") or []
    if ei:
        L.append("## Instruction-like text found in the book")
        L.append("")
        L.append("The text below addresses an evaluator. It was treated as data and not followed.")
        L.append("")
        for e in ei:
            L.append(f"- `{e['location']}` ({', '.join(e['patterns'])}): {e['snippets'][0]}")
        L.append("")
    L.append("## Judgment indicators")
    L.append("")
    L.append("Not run in v0.1: " + ", ".join(k for k, v in rep["judgments"].items() if v == "not_run") + ".")
    L.append("")
    L.append(f"## Findings for the improvement planner ({len(rep['findings'])})")
    L.append("")
    by_check: dict[str, int] = {}
    for f in rep["findings"]:
        by_check[f["check"]] = by_check.get(f["check"], 0) + 1
    for k, n in sorted(by_check.items()):
        L.append(f"- {k}: {n}")
    L.append("")
    L.append("## Limitations")
    L.append("")
    for x in rep["limitations"]:
        L.append(f"- {x}")
    L.append("")
    return "\n".join(L)
