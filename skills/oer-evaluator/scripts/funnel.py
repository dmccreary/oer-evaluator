"""Four-stage reuse process, reuse value, and the Q and R headline numbers
(spec Sections 3 and 4).

The formulas are implemented in full so a later release can feed them Tier 2
judgments. In v0.1 those judgments are not run, so most outputs here are
"pending" or "not available" rather than numbers. Nothing is estimated.
"""
from __future__ import annotations

from statistics import mean

TIER2_FOR_STAGE = {2: ["RJ2"], 3: ["J1", "J7"], 4: ["RJ1", "RJ4"]}
DET_STAGE2 = ["RP1", "RP2", "RP3", "RP4", "RP6"]


def _status(checks: dict, key: str) -> str:
    return (checks.get(key) or {}).get("status", "ISE")


def reuse_value(rj1: float, rj4: float, rj6: float) -> float:
    """reuse value = mean(RJ1, RJ4) x (RJ6 / 3), on the 0-3 scale (decision D11)."""
    return round(mean([rj1, rj4]) * (rj6 / 3.0), 4)


def evaluate_component(checks: dict, rj6: int | None, level: str, judgments: dict | None = None) -> dict:
    j = judgments or {}
    interactive = level in ("L1", "L2")

    # Stage 1: findable
    if rj6 is None:
        s1 = ("ISE", "findability was not tested for this component")
    elif rj6 == 0:
        s1 = ("fail", "RJ6 scored 0: the component is not found by the search tool")
    else:
        s1 = ("pass", f"RJ6 = {rj6}")

    # Stage 2: portable (deterministic checks, then RJ2)
    statuses = {k: _status(checks, k) for k in DET_STAGE2}
    failed = [k for k, v in statuses.items() if v == "fail"]
    unknown = [k for k, v in statuses.items() if v == "ISE"]
    if failed:
        s2 = ("fail", "failed " + ", ".join(failed))
    elif unknown:
        s2 = ("ISE", "could not determine " + ", ".join(unknown))
    elif "RJ2" in j:
        s2 = ("pass", "deterministic checks pass and RJ2 = %s" % j["RJ2"]) if j["RJ2"] >= 2 else ("fail", f"RJ2 = {j['RJ2']} (below 2)")
    else:
        s2 = ("pending", "deterministic checks pass; RJ2 (context independence) not run")

    # Stage 3: sound
    need = ["J1"] + (["J7"] if interactive else [])
    if any(k not in j for k in need):
        miss = [k for k in need if k not in j]
        s3 = ("pending", "not run: " + ", ".join(miss))
    elif any(j[k] < 2 for k in need):
        s3 = ("fail", "below 2: " + ", ".join(f"{k}={j[k]}" for k in need if j[k] < 2))
    else:
        s3 = ("pass", ", ".join(f"{k}={j[k]}" for k in need))

    # Stage 4: worth reusing (scored, never a gate)
    if all(k in j for k in ("RJ1", "RJ4")):
        s4 = ("scored", f"RJ1={j['RJ1']}, RJ4={j['RJ4']}")
    else:
        s4 = ("pending", "not run: " + ", ".join(k for k in ("RJ1", "RJ4") if k not in j))

    stages = {1: s1, 2: s2, 3: s3, 4: s4}
    reached = 0
    for n in (1, 2, 3):
        if stages[n][0] == "pass":
            reached = n
        else:
            break
    stopped_at = next((n for n in (1, 2, 3) if stages[n][0] != "pass"), None)
    if any(stages[n][0] == "fail" for n in (1, 2, 3)):
        reuse_ready = False
    elif all(stages[n][0] == "pass" for n in (1, 2, 3)):
        reuse_ready = True
    else:
        reuse_ready = None

    value = value_wo = None
    if reuse_ready is False:
        value = 0.0
    if reuse_ready is True and s4[0] == "scored" and rj6 is not None:
        value = reuse_value(j["RJ1"], j["RJ4"], rj6)
    if s4[0] == "scored" and s2[0] == "pass" and s3[0] == "pass":
        value_wo = round(mean([j["RJ1"], j["RJ4"]]), 4)  # as if findability were fully fixed
    return {
        "stages": {str(n): {"status": st, "detail": d} for n, (st, d) in stages.items()},
        "stage_reached": reached, "stopped_at": stopped_at,
        "reuse_ready": reuse_ready, "reuse_value": value, "value_without_findability": value_wo,
        "pending": sorted({k for n in (2, 3, 4) for k in TIER2_FOR_STAGE[n] if k not in j and (k != "J7" or interactive)}),
    }


def headline(book_checks: dict, components: dict, judgments: dict | None, chapters: list[dict]) -> dict:
    """Q and R plus the detail that sits beside them."""
    applicable = [c for c in book_checks.values() if c["status"] != "N/A"]
    passed = [k for k, c in book_checks.items() if c["status"] == "pass"]
    reasons_q, reasons_r = [], []

    # ---- Q ----
    jud = (judgments or {}).get("chapters") or {}
    q_ind = ["J1", "J2", "J3", "J4", "J5", "J6", "J7", "J8", "J10", "J11"]
    weights = {c["dir"]: c.get("weight", 0) for c in chapters}
    means = {}
    for ind in q_ind:
        num = den = 0.0
        for d, scores in jud.items():
            v = scores.get(ind)
            w = weights.get(d, 0)
            if isinstance(v, (int, float)) and w > 0:
                num += v * w
                den += w
        if den > 0:
            means[ind] = round(num / den, 4)
    if means:
        q = {"value": round(mean(means.values()), 3), "status": "computed", "indicator_means": means,
             "provisional": True, "unvalidated": True,
             "note": "Computed from Tier 2 scores that have not passed V1 and V2."}
    else:
        q = {"value": None, "status": "not_available",
             "reason": "The Tier 2 judgment indicators (J1-J8, J10, J11) are not run in v0.1, so Q cannot be computed. It is not estimated."}

    # ---- R ----
    vals = {cid: c["reuse"]["reuse_value"] for cid, c in components.items()}
    known = [v for v in vals.values() if v is not None]
    unknown = [cid for cid, v in vals.items() if v is None]
    ready = {True: 0, False: 0, None: 0}
    for c in components.values():
        ready[c["reuse"]["reuse_ready"]] += 1
    if components and not unknown:
        r = {"value": round(mean(known), 3), "status": "computed", "provisional": True,
             "note": "Unweighted mean over every inventoried component; non-reuse-ready components count as 0."}
    else:
        r = {"value": None, "status": "not_available",
             "reason": ("Reuse value needs RJ1 (topic generality) and RJ4 (substance), and reuse-readiness needs RJ2 and J1, "
                        "none of which run in v0.1. R is not estimated."),
             "known_zero": sum(1 for v in known if v == 0.0), "unknown": len(unknown), "components": len(components)}

    level_counts = {"L0": 0, "L1": 0, "L2": 0}
    for c in components.values():
        level_counts[c["interactivity"]] = level_counts.get(c["interactivity"], 0) + 1
    return {
        "Q": q, "R": r,
        "beside_Q": {"completeness_checks_passed": len(passed), "completeness_checks_applicable": len(applicable),
                     "passed": passed,
                     "failed": [k for k, c in book_checks.items() if c["status"] == "fail"],
                     "not_determined": [k for k, c in book_checks.items() if c["status"] == "ISE"]},
        "beside_R": {"reuse_ready": {"yes": ready[True], "no": ready[False], "not_yet_determined": ready[None]},
                     "interactivity_levels": level_counts,
                     "instrumented_components": level_counts.get("L2", 0), "components": len(components)},
        "provisional": True,
        "provisional_because": ["Tier 2 judgments are not run in v0.1", "findability scores may be ISE"],
    }
