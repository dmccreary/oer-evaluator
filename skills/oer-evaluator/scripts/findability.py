"""RJ6 findability: the retrieval test (spec Section 6, decision D11).

Three steps, so the language-model part stays separate and auditable:

  prepare   write a content digest per component (never its metadata)
  [agent]   write 12 queries per component from that digest
  run       embed the component's metadata with the catalog's own WHAT text,
            rank it against the author's search-microsims catalog, and score
            RJ6 from the strong-hit and hit rates

Hit definitions are the search service's own calibrated bands:
  strong hit  rank <= 3  and WHAT score >= 0.75   (the 'reuse' band)
  hit         rank <= 10 and WHAT score >= 0.60   (at least the 'template' band)
"""
from __future__ import annotations

import importlib.util
import json
import re
import sys
from pathlib import Path

from common import read_json, read_text, safe_id, strip_code_fences, write_json

QUERY_TYPES = ["topic", "topic_level", "objective", "format"]
QUERIES_PER_TYPE = 3
STRONG_RANK, STRONG_SCORE = 3, 0.75
HIT_RANK, HIT_SCORE = 10, 0.60
TWIN_THRESHOLD = 0.90          # duplicate-cluster threshold in the catalog
RATE_FOR_3, RATE_FOR_2 = 0.75, 0.50

QUERY_GUIDE = {
    "topic": "Topic only. Example: 'Topic: repeated division method for binary conversion'",
    "topic_level": "Topic plus level. Example: 'Topic: ... | Grade Level: undergraduate'",
    "objective": "Phrased as a learning objective. Example: 'Learning Objectives: Students will apply ...'",
    "format": "Seeking a kind of resource. Example: 'Title: interactive simulation that lets students step through ...'",
}


# ---- score mapping (pure, unit-tested) -------------------------------------------
def score_rj6(*, metadata_present: bool, required_fields_present: bool, specific: bool,
              n_queries: int, hits: int, strong: int) -> dict:
    """Map retrieval results to the 0-3 RJ6 score using the anchors in spec Section 7."""
    if not metadata_present:
        return {"score": 0, "reason": "metadata absent"}
    if n_queries <= 0:
        return {"score": None, "reason": "no valid queries"}
    strong_rate = strong / n_queries
    hit_rate = hits / n_queries
    if required_fields_present and specific and strong_rate >= RATE_FOR_3:
        return {"score": 3, "reason": f"strong hit on {strong}/{n_queries} queries with specific search fields"}
    if required_fields_present and hit_rate >= RATE_FOR_2:
        return {"score": 2, "reason": f"hit on {hits}/{n_queries} queries with required search fields present"}
    if hits >= 1:
        why = f"hit on {hits}/{n_queries} queries"
        if not required_fields_present:
            why += "; capped at 1 because a required search field is missing"
        elif strong_rate >= RATE_FOR_3 and not specific:
            why += "; search fields are present but generic"
        return {"score": 1, "reason": why}
    return {"score": 0, "reason": f"no hit in {n_queries} queries"}


# ---- content digests ---------------------------------------------------------------
def _visible_text(html: str) -> str:
    html = re.sub(r"<(script|style)\b.*?</\1>", " ", html, flags=re.S | re.I)
    html = re.sub(r"<!--.*?-->", " ", html, flags=re.S)
    html = re.sub(r"<[^>]+>", " ", html)
    return re.sub(r"\s+", " ", html).strip()


def _leading_comment(js: str, limit: int = 1200) -> str:
    m = re.match(r"\s*/\*(.*?)\*/", js, flags=re.S)
    if m:
        return re.sub(r"\s*\n\s*\*?\s*", " ", m.group(1)).strip()[:limit]
    lines = []
    for l in js.split("\n"):
        s = l.strip()
        if s.startswith("//"):
            lines.append(s[2:].strip())
        elif lines or s:
            break
    return " ".join(lines)[:limit]


def content_digest(book: Path, comp: dict, meta: dict | None) -> dict:
    d = book / comp["path"]
    parts = {}
    idx = read_text(d / "index.md")
    body = re.sub(r"^---.*?\n---\n", "", idx, count=1, flags=re.S)
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    body = re.sub(r"<iframe[^>]*>.*?</iframe>", "", body, flags=re.S | re.I)
    body = re.sub(r"^#\s+.+$", "", body, count=1, flags=re.M)  # the H1 is the title, i.e. metadata
    parts["lesson_page"] = strip_code_fences(body).strip()[:5000]
    parts["page_text"] = _visible_text(read_text(d / "main.html"))[:1500]
    js = ""
    for f in sorted(d.glob("*.js")):
        if ".min." in f.name or f.stat().st_size > 600_000:
            continue
        js = _leading_comment(read_text(f))
        if js:
            break
    parts["source_comment"] = js
    avoid = []
    if meta:
        for k in ("title", "name"):
            if isinstance(meta.get(k), str):
                avoid.append(meta[k].strip())
        desc = meta.get("description")
        if isinstance(desc, str) and desc.strip():
            avoid.append(desc.strip())
    avoid.append(comp.get("title", ""))
    return {"id": comp["id"], "type": comp["type"], "content": parts,
            "avoid_phrases": [a for a in dict.fromkeys(avoid) if a]}


def prepare(book: Path, inventory: dict, out_dir: Path, metadata_by_id: dict) -> dict:
    inputs_dir = out_dir / "findability" / "inputs"
    (out_dir / "findability" / "queries").mkdir(parents=True, exist_ok=True)
    listed = []
    for comp in inventory["components"]:
        if comp["type"] not in ("microsim", "interactive-infographic"):
            continue
        raw = metadata_by_id.get(comp["id"])
        digest = content_digest(book, comp, raw)
        digest["query_spec"] = {
            "queries_per_type": QUERIES_PER_TYPE, "types": QUERY_TYPES, "guide": QUERY_GUIDE,
            "write_to": str(out_dir / "findability" / "queries" / f"{safe_id(comp['id'])}.json"),
            "rules": [
                "Write queries from the content above, as a different author searching for this kind of resource would.",
                "Never copy the title, the description, or any phrase listed in avoid_phrases.",
                "Use the search service's query format: 'Field: value | Field: value'.",
                "Write exactly 3 queries for each of the 4 types, 12 in total.",
            ]}
        write_json(inputs_dir / f"{safe_id(comp['id'])}.json", digest)
        listed.append(comp["id"])
    write_json(out_dir / "findability" / "manifest.json",
               {"components": listed, "expected_queries_per_component": QUERIES_PER_TYPE * len(QUERY_TYPES)})
    return {"prepared": len(listed), "inputs_dir": str(inputs_dir),
            "queries_dir": str(out_dir / "findability" / "queries")}


# ---- query validation ----------------------------------------------------------------
def validate_queries(payload, avoid_phrases: list[str]) -> tuple[list[dict], list[str]]:
    problems: list[str] = []
    if not isinstance(payload, dict) or not isinstance(payload.get("queries"), list):
        return [], ["queries file must be an object with a 'queries' list"]
    valid, per_type = [], {t: 0 for t in QUERY_TYPES}
    avoid_lc = [a.lower() for a in avoid_phrases if len(a) >= 4]
    for i, q in enumerate(payload["queries"]):
        text = (q.get("text") if isinstance(q, dict) else None) or ""
        qtype = q.get("type") if isinstance(q, dict) else None
        if qtype not in QUERY_TYPES:
            problems.append(f"query {i}: type must be one of {QUERY_TYPES}")
            continue
        text = text.strip()
        if not text or len(text) > 500:
            problems.append(f"query {i}: empty or longer than 500 characters")
            continue
        low = text.lower()
        echoed = next((a for a in avoid_lc if a in low), None)
        if echoed:
            problems.append(f"query {i}: copies metadata text ('{echoed[:40]}')")
            continue
        # also reject any 8-word run lifted from an avoided phrase (description)
        words = re.findall(r"\w+", low)
        lifted = False
        for a in avoid_lc:
            aw = re.findall(r"\w+", a)
            for s in range(0, max(0, len(aw) - 7)):
                if " ".join(aw[s:s + 8]) in " ".join(words):
                    lifted = True
                    break
            if lifted:
                break
        if lifted:
            problems.append(f"query {i}: lifts an 8-word run from the metadata")
            continue
        per_type[qtype] += 1
        valid.append({"type": qtype, "text": text})
    for t, n in per_type.items():
        if n != QUERIES_PER_TYPE:
            problems.append(f"type '{t}': {n} valid queries, expected {QUERIES_PER_TYPE}")
    return valid, problems


# ---- search runner --------------------------------------------------------------------
def _load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, str(path))
    mod = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(path.parent))
    spec.loader.exec_module(mod)
    return mod


def _label_free(text: str) -> str:
    return re.sub(r"\b(Title|Topic|Subjects?|Grade Level|Learning Objectives?|Cognitive Level|Action)\s*:", " ", text)


def run(book: Path, inventory: dict, out_dir: Path, comp_meta: dict, search_home: Path,
        site_url: str | None, book_name: str, limit: int | None = None) -> dict:
    """comp_meta: {component id: {"raw": dict|None, "desc": describe_metadata(...)}}"""
    base = {"status": "ISE", "catalog": None, "components": {}}
    try:
        import numpy as np
    except ImportError:
        base["reason"] = "numpy is not installed"
        return base
    src = search_home / "src"
    needed = [src / "normalize_metadata.py", src / "embeddings" / "generate-embeddings.py",
              src / "find-similar-templates" / "find-similar-templates.py"]
    missing = [str(p) for p in needed if not p.exists()]
    if missing:
        base["reason"] = "search-microsims not found: " + ", ".join(missing)
        return base
    try:
        norm = _load_module("oe_normalize_metadata", needed[0])
        gen = _load_module("oe_generate_embeddings", needed[1])
        fst = _load_module("oe_find_similar_templates", needed[2])
    except Exception as e:  # missing sentence-transformers etc.
        base["reason"] = f"could not import the search service: {type(e).__name__}: {e}"
        return base
    try:
        model = fst.load_model()
        emb, urls, what_matrix, _ = fst.load_embeddings()
        catalog_data = fst.load_microsims_data()
    except Exception as e:
        base["reason"] = f"could not load the model or catalog: {type(e).__name__}: {e}"
        return base

    meta = emb.get("metadata", {})
    prefix = (site_url or "").rstrip("/")
    keep = [i for i, u in enumerate(urls)
            if not (prefix and u.startswith(prefix + "/")) and f"/{book_name}/" not in u]
    cand_urls = [urls[i] for i in keep]
    cand_mat = what_matrix[keep]
    cand_text = []
    for u in cand_urls:
        rec = catalog_data.get(u, {})
        objs = rec.get("learningObjectives") or []
        cand_text.append(" ".join(str(x) for x in [rec.get("title", ""), rec.get("description", ""),
                                                  rec.get("topic", ""), rec.get("subject", ""),
                                                  " ".join(objs) if isinstance(objs, list) else objs]))

    # embed this book's components exactly as the catalog embeds a record
    comp_ids, comp_texts, comp_has_meta = [], [], {}
    for comp in inventory["components"]:
        if comp["type"] not in ("microsim", "interactive-infographic"):
            continue
        info = comp_meta.get(comp["id"], {})
        raw = info.get("raw")
        if not raw:
            comp_has_meta[comp["id"]] = False
            continue
        rec = norm.normalize_metadata(raw)
        rec.setdefault("_source", {"repo": book_name, "sim": comp["id"].split("/", 1)[-1]})
        text = gen.create_what_text(rec)
        comp_has_meta[comp["id"]] = bool(text.strip())
        if text.strip():
            comp_ids.append(comp["id"])
            comp_texts.append(text)
    vecs = model.encode(comp_texts, convert_to_numpy=True, normalize_embeddings=True) if comp_texts else np.zeros((0, cand_mat.shape[1]))
    pool_mat = np.vstack([cand_mat, vecs]) if len(comp_ids) else cand_mat
    pool_ids = cand_urls + [f"book::{c}" for c in comp_ids]
    pool_text = cand_text + [t for t in comp_texts]
    pool_index = {pid: i for i, pid in enumerate(pool_ids)}

    kw = None
    try:
        from sklearn.feature_extraction.text import TfidfVectorizer
        vec = TfidfVectorizer(stop_words="english", sublinear_tf=True)
        kw_mat = vec.fit_transform(pool_text)
        kw = (vec, kw_mat)
    except Exception:
        kw = None

    results = {}
    done = 0
    for comp in inventory["components"]:
        if comp["type"] not in ("microsim", "interactive-infographic"):
            continue
        cid = comp["id"]
        if limit is not None and done >= limit:
            break
        info = comp_meta.get(cid, {})
        desc = info.get("desc", {})
        if not comp_has_meta.get(cid):
            sc = score_rj6(metadata_present=False, required_fields_present=False, specific=False,
                           n_queries=0, hits=0, strong=0)
            results[cid] = {"status": "scored", "RJ6": sc["score"], "reason": sc["reason"], "queries": [], "rates": None}
            done += 1
            continue
        qpath = out_dir / "findability" / "queries" / f"{safe_id(cid)}.json"
        inp = read_json(out_dir / "findability" / "inputs" / f"{safe_id(cid)}.json") or {}
        if not qpath.exists():
            results[cid] = {"status": "ISE", "RJ6": None, "reason": f"queries not yet written: {qpath.name}", "queries": []}
            continue
        valid, problems = validate_queries(read_json(qpath), inp.get("avoid_phrases", []))
        if len(valid) != QUERIES_PER_TYPE * len(QUERY_TYPES):
            results[cid] = {"status": "ISE", "RJ6": None, "problems": problems,
                            "reason": f"{len(valid)} valid queries of {QUERIES_PER_TYPE * len(QUERY_TYPES)}; rewrite the rejected ones", "queries": []}
            continue
        ci = pool_index[f"book::{cid}"]
        cvec = pool_mat[ci]
        twin_sims = pool_mat @ cvec
        excluded = twin_sims >= TWIN_THRESHOLD
        excluded[ci] = False
        n_twins = int(excluded.sum())
        twin_ids = [pool_ids[k].replace("book::", "") for k in np.where(excluded)[0][:5]]
        qv = model.encode([q["text"] for q in valid], convert_to_numpy=True, normalize_embeddings=True)
        sims = pool_mat @ qv.T                      # pool x queries
        sims[excluded, :] = -1.0
        qrows = []
        hits = strong = kw_hits = rank_hits = rank_strongs = 0
        for j, q in enumerate(valid):
            s = sims[:, j]
            score = float(s[ci])
            rank = int(1 + (s > score).sum())
            top = int(np.argmax(s))
            is_strong = rank <= STRONG_RANK and score >= STRONG_SCORE
            is_hit = rank <= HIT_RANK and score >= HIT_SCORE
            hits += is_hit
            strong += is_strong
            rank_hits += rank <= HIT_RANK
            rank_strongs += rank <= STRONG_RANK
            row = {"type": q["type"], "text": q["text"], "rank": rank, "what_score": round(score, 4),
                   "hit": bool(is_hit), "strong_hit": bool(is_strong),
                   "best_other": None if top == ci else {"id": pool_ids[top].replace("book::", ""),
                                                         "what_score": round(float(s[top]), 4)}}
            if kw:
                qvec = kw[0].transform([_label_free(q["text"])])
                ks = (kw[1] @ qvec.T).toarray().ravel()
                ks[excluded] = -1.0
                kscore = float(ks[ci])
                krank = int(1 + (ks > kscore).sum()) if kscore > 0 else None
                row["keyword_rank"] = krank
                kw_hits += bool(krank and krank <= HIT_RANK)
            qrows.append(row)
        n = len(qrows)
        sc = score_rj6(metadata_present=True,
                       required_fields_present=not desc.get("missing_required", ["x"]),
                       specific=not desc.get("generic"),
                       n_queries=n, hits=int(hits), strong=int(strong))
        by_type = {}
        for t in QUERY_TYPES:
            rows = [r for r in qrows if r["type"] == t]
            by_type[t] = {"hits": sum(r["hit"] for r in rows), "of": len(rows)}
        results[cid] = {
            "status": "scored", "RJ6": sc["score"], "reason": sc["reason"],
            "rates": {"hit": round(hits / n, 3), "strong_hit": round(strong / n, 3),
                      "keyword_hit": round(kw_hits / n, 3) if kw else None,
                      # pilot diagnostics: the same ranks without the WHAT-score floor
                      "rank_only_hit": round(rank_hits / n, 3), "rank_only_strong_hit": round(rank_strongs / n, 3)},
            "by_query_type": by_type, "twins_removed": n_twins, "twin_ids": twin_ids, "queries": qrows,
            "diagnostic": ("found by embedding but missed by keyword: metadata may lack the vocabulary authors use"
                           if kw and hits and kw_hits < hits / 2 else None),
        }
        done += 1

    base.update({
        "status": "ran",
        "catalog": {
            "search_home": str(search_home), "model": meta.get("model"), "schema": meta.get("schema"),
            "count": meta.get("count"), "generated_at": meta.get("generated_at"),
            "candidates_after_excluding_this_book": len(cand_urls),
            "this_book_components_in_pool": len(comp_ids),
            "bands": {"reuse": fst.REUSE_THRESHOLD, "template": fst.TEMPLATE_THRESHOLD},
            "keyword_diagnostic": "tf-idf stand-in (ItemsJS not run)" if kw else "not run (scikit-learn unavailable)",
        },
        "components": results,
    })
    return base
