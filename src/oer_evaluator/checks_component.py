"""Tier 1 component-level checks RP1-RP9 (spec Section 5).

Static analysis only. Nothing here runs a browser, so RP2 is reported with
method "static" and a note saying a render would confirm it.
"""
from __future__ import annotations

import re
from pathlib import Path

from common import (BOILERPLATE_OBJECTIVE_PREFIXES, ev, is_placeholder_text, parse_frontmatter,
                    read_json, read_text, result, safe_exists, safe_resolve, strip_code_fences)
from checks_book import normalize_license
from safety import scan_text

# ---- metadata -------------------------------------------------------------
# Same field paths as search-microsims src/normalize_metadata.py, so RP5 sees
# a record the way the catalog does.
_SCALAR = {
    "title": ["title", "dublinCore.title", "dublin_core.title", "dc.title", "DC.title", "name"],
    "description": ["description", "dublinCore.description", "dublin_core.description", "dc.description", "DC.description"],
    "creator": ["creator", "author", "dublinCore.creator", "dublin_core.creator", "dc.creator", "DC.creator"],
    "gradeLevel": ["gradeLevel", "educational.gradeLevel", "educational.grade_level"],
    "topic": ["topic", "educational.topic"],
}
_LIST = {
    "subjects": ["subjects", "subject", "educational.subjectArea", "educational.subject_area",
                 "dublinCore.subject", "dublin_core.subject", "dc.subject", "DC.subject"],
    "learningObjectives": ["learningObjectives", "learningObjective", "learning_objective",
                           "educational.learningObjectives", "educational.learning_objectives"],
}
_LEVEL_SYNONYMS = ["gradeLevel", "educationalLevel", "educational.gradeLevel", "educational.educationalLevel",
                   "audience", "coverage", "educational.audience"]
_VERSION_PATHS = ["version", "technical.version", "dublinCore.version", "dc.version"]
_LICENSE_PATHS = ["license", "rights", "dublinCore.rights", "dublin_core.rights", "dc.rights", "DC.rights",
                  "dublinCore.license", "copyright"]


def _get_nested(raw, dotted):
    v = raw
    for part in dotted.split("."):
        if not isinstance(v, dict):
            return None
        v = v.get(part)
        if v is None:
            return None
    return v


def _first(raw, paths):
    for p in paths:
        v = raw.get(p)
        if v in (None, "", [], {}) and "." in p:
            v = _get_nested(raw, p)
        if v not in (None, "", [], {}):
            return p, v
    return None, None


def _lookup_source(raw: dict) -> dict:
    wrapped = raw.get("microsim")
    if isinstance(wrapped, dict):
        return {**wrapped, **{k: v for k, v in raw.items() if k != "microsim"}}
    return raw


def load_metadata(book: Path, comp: dict) -> tuple[dict | None, str | None]:
    """Return (raw metadata dict, source label) for a component, or (None, None)."""
    t = comp["type"]
    if t in ("microsim", "interactive-infographic"):
        p = book / comp["path"] / "metadata.json"
        raw = read_json(p)
        if isinstance(raw, dict):
            return raw, str(p.relative_to(book))
        return None, None
    if t in ("section",):
        fm, _ = parse_frontmatter(read_text(book / comp["path"]))
        return (fm or None), (comp["path"] + " (frontmatter)") if fm else None
    if t == "static-figure" and comp["path"].count("/") >= 1 and (book / comp["path"]).is_dir():
        raw = read_json(book / comp["path"] / "metadata.json")
        if isinstance(raw, dict):
            return raw, f"{comp['path']}/metadata.json"
    return None, None


def describe_metadata(raw: dict | None) -> dict:
    """Group fields for RP5 and record which look generic."""
    if not raw:
        return {"present": {}, "missing_required": ["title", "description", "subject", "learningObjectives"],
                "generic": [], "level_key": None, "raw_available": False}
    src = _lookup_source(raw)
    out = {}
    for k, paths in _SCALAR.items():
        _, v = _first(src, paths)
        if isinstance(v, list):
            v = ", ".join(str(x) for x in v)
        out[k] = v
    for k, paths in _LIST.items():
        _, v = _first(src, paths)
        if v is not None and not isinstance(v, list):
            v = [v]
        out[k] = v
    lk, lv = _first(src, _LEVEL_SYNONYMS)
    out["level"] = lv if not isinstance(lv, list) else ", ".join(map(str, lv))
    out["level_key"] = lk
    _, ver = _first(src, _VERSION_PATHS)
    out["version"] = ver
    present = {k: v for k, v in out.items() if v not in (None, "", [], {}) and k != "level_key"}
    required = {"title": out.get("title"), "description": out.get("description"),
                "subject": out.get("subjects"), "learningObjectives": out.get("learningObjectives")}
    missing = [k for k, v in required.items() if v in (None, "", [], {}) or (isinstance(v, str) and is_placeholder_text(v))]
    generic = []
    desc = out.get("description")
    if isinstance(desc, str) and desc and (len(desc.strip()) < 40 or "<iframe" in desc.lower()):
        generic.append("description")
    objs = out.get("learningObjectives") or []
    if objs:
        boiler = sum(1 for o in objs if isinstance(o, str) and o.lower().startswith(BOILERPLATE_OBJECTIVE_PREFIXES))
        if boiler / len(objs) >= 0.5:  # a template fills most of the list even when one line differs
            generic.append("learningObjectives")
    if isinstance(out.get("title"), str) and is_placeholder_text(out["title"]):
        generic.append("title")
    # A field that is text addressed to an evaluator is not a real description.
    instruction_fields = []
    for fld, val in (("title", out.get("title")), ("description", out.get("description")),
                     ("learningObjectives", " ".join(map(str, out.get("learningObjectives") or []))),
                     ("subject", " ".join(map(str, out.get("subjects") or [])))):
        if isinstance(val, str) and val and scan_text(val):
            instruction_fields.append(fld)
            if fld not in generic:
                generic.append(fld)
    return {"present": present, "missing_required": missing, "generic": generic,
            "instruction_like_fields": instruction_fields,
            "level_key": lk, "raw_available": True,
            "normalized": {k: out.get(k) for k in ("title", "description", "subjects", "learningObjectives",
                                                  "gradeLevel", "topic", "creator", "level", "version")}}


# ---- HTML / JS analysis ------------------------------------------------------
_HTML_REF = re.compile(
    r"<(script|link|img|iframe|source|object|embed|video|audio)\b[^>]*?\b(?:src|href|data)\s*=\s*[\"']([^\"']+)[\"']", re.I)
_CSS_URL = re.compile(r"url\(\s*[\"']?([^)\"']+)[\"']?\s*\)|@import\s+[\"']([^\"']+)[\"']", re.I)
_JS_STR = re.compile(r"[\"'`]((?:https?:)?//[^\"'`\s]+\.(?:js|css|json|csv)(?:\?[^\"'`\s]*)?|(?:\.{1,2}/|/)?[\w\-./]+\.(?:json|csv|tsv|png|jpe?g|gif|svg|webp|mp3|mp4|wav|html|js|css|glb|wasm|geojson))[\"'`]", re.I)
_PIN = re.compile(r"(@\d+(?:\.\d+){0,2}(?![\w.]*latest))|(/\d+\.\d+(?:\.\d+)?/)|([-.@]v?\d+\.\d+(?:\.\d+)?(?:\.min)?\.(?:js|css))|(\bv\d+(?:\.\d+)+)", re.I)
_FONT_HOSTS = ("fonts.googleapis.com", "fonts.gstatic.com")
_SHARED_LIB_HINT = re.compile(r"(^|/)(shared-libs?|js|css|lib|libs|vendor|assets)/", re.I)


def _is_external(ref: str) -> bool:
    return bool(re.match(r"^(https?:)?//", ref, re.I))


def _html_files(d: Path) -> list[Path]:
    return sorted(d.glob("*.html"))


def _js_files(d: Path) -> list[Path]:
    return [p for p in sorted(d.glob("*.js")) if p.stat().st_size < 600_000]


def analyze_package(sim_dir: Path) -> dict:
    """Collect every local and external reference a sim package makes."""
    local_refs: list[dict] = []
    external: list[dict] = []
    files_read = []
    docs = []
    for f in _html_files(sim_dir):
        docs.append((f, "html", read_text(f)))
    for f in _js_files(sim_dir):
        docs.append((f, "js", read_text(f)))
    for f in sorted(sim_dir.glob("*.css")):
        docs.append((f, "css", read_text(f)))
    for f, kind, text in docs:
        files_read.append(f.name)
        refs: list[tuple[str, str]] = []
        if kind == "html":
            for tag, ref in _HTML_REF.findall(text):
                if tag.lower() == "link" and False:
                    continue
                refs.append((tag.lower(), ref))
            for m in _CSS_URL.finditer(text):
                refs.append(("css", m.group(1) or m.group(2)))
        elif kind == "css":
            for m in _CSS_URL.finditer(text):
                refs.append(("css", m.group(1) or m.group(2)))
        else:
            for m in _JS_STR.finditer(strip_js_comments(text)):
                refs.append(("js-string", m.group(1)))
        for tag, ref in refs:
            ref = ref.strip()
            if not ref or ref.startswith(("data:", "#", "javascript:", "mailto:", "blob:")):
                continue
            if _is_external(ref):
                external.append({"ref": ref, "from": f.name, "tag": tag})
            else:
                base = sim_dir  # JS and HTML both execute at the page URL
                if kind in ("css",):
                    base = f.parent
                clean = ref.split("#")[0].split("?")[0]
                target = safe_resolve(base / clean) if (not clean.startswith("/") and len(clean) < 400) else None
                local_refs.append({"ref": ref, "from": f.name, "tag": tag,
                                   "target": str(target) if target else None,
                                   "root_relative": clean.startswith("/")})
    return {"local": local_refs, "external": external, "files": files_read}


def strip_js_comments(text: str) -> str:
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    return re.sub(r"(?m)^\s*//.*$", "", text)


def _classify_local(sim_dir: Path, refs: list[dict]) -> tuple[list, list, list]:
    inside_missing, outside, ok = [], [], []
    root = sim_dir.resolve()
    for r in refs:
        if r["root_relative"] or not r["target"]:
            outside.append({**r, "exists": None, "reason": "root-relative path depends on the host site"})
            continue
        t = Path(r["target"])
        try:
            t.relative_to(root)
            inside = True
        except ValueError:
            inside = False
        exists = t.exists()
        if inside and not exists:
            inside_missing.append({**r, "exists": False})
        elif not inside:
            outside.append({**r, "exists": exists, "reason": "resolves outside the component directory"})
        else:
            ok.append(r)
    return inside_missing, outside, ok



# ---- site-wide scripts (mkdocs.yml extra_javascript) and event delivery --------------
_SEND = re.compile(r"navigator\.sendBeacon|new\s+XMLHttpRequest|\.open\(\s*[\"']POST|fetch\([^)]{0,200}?method\s*:\s*[\"']POST|\$\.post\(|axios\.post", re.S | re.I)


def site_wide_scripts(book: Path) -> list[dict]:
    """Scripts that mkdocs.yml loads on every page, classified by what their code does.
    A quiz can be instrumented by one of these without any code in the quiz itself."""
    mk = read_text(book / "mkdocs.yml")
    m = re.search(r"^extra_javascript:\s*\n((?:[ \t]+.*\n?|[ \t]*\n)+)", mk, re.M)
    out = []
    if not m:
        return out
    for entry in re.findall(r"^\s*-\s*(?:path:\s*)?[\"']?([^\s\"'#]+\.js)[\"']?", m.group(1), re.M):
        if _is_external(entry):
            continue
        p = book / "docs" / entry
        if not p.exists():
            continue
        code = strip_js_comments(read_text(p, 400_000))
        roles = []
        if re.search(r"(?:window\.)?\b(?:LRSSim|LRSLite|LRS)\s*=", code):
            roles.append("xapi-runtime")
        # A quiz emitter reads the rendered quiz markup and emits an answer. The
        # runtime and viewer files mention 'answered' but do not parse a quiz.
        reads_dom = re.search(r"querySelector(?:All)?\s*\(|getElementsBy", code)
        reads_quiz = re.search(r"\bdetails\b", code, re.I) and re.search(r"\bquiz|\bquestion\b", code, re.I)
        emits = re.search(r"\banswered\b|\.answer\s*\(", code) and re.search(r"\b(?:LRSSim|LRS|lrs)\b", code)
        if reads_dom and reads_quiz and emits and "xapi-runtime" not in roles:
            roles.append("quiz-emitter")
        out.append({"path": f"docs/{entry}", "entry": entry, "roles": roles, "sends": bool(_SEND.search(code))})
    return out


def delivery(book: Path, comp: dict, site_wide: list[dict]) -> dict:
    """Does any code in the files that run this component send events off the page?
    Static evidence only: 'not found' is not proof that nothing is delivered."""
    files: dict[str, str] = {}
    t = comp["type"]
    if t in ("microsim", "interactive-infographic"):
        d = book / comp["path"]
        for f in list(_html_files(d)) + _js_files(d):
            files[f"{comp['path']}/{f.name}"] = read_text(f, 400_000)
        main = read_text(d / "main.html")
        for src in re.findall(r"<script[^>]+src=[\"']([^\"']*(?:lrs|xapi)[^\"']*)[\"']", main, re.I):
            if _is_external(src):
                continue
            p = (d / src.split("?")[0]).resolve()
            if p.exists():
                try:
                    files[str(p.relative_to(book.resolve()))] = read_text(p, 400_000)
                except ValueError:
                    files[str(p)] = read_text(p, 400_000)
    for s in site_wide:
        if s["roles"]:
            files[s["path"]] = read_text(book / s["path"], 400_000)
    matched = [name for name, txt in files.items() if _SEND.search(strip_js_comments(txt) if name.endswith(".js") else txt)]
    return {"send_code_found": bool(matched), "matched_in": matched[:6], "files_checked": sorted(files)[:12],
            "note": None if matched else "No code that sends events off the page was found in the files checked. Statements may be kept in memory only."}

def interactivity(book: Path, comp: dict, site_wide: list[dict] | None = None) -> dict:
    """RP8: interactivity level by reading code, never by trusting status flags."""
    t = comp["type"]
    if t in ("microsim", "interactive-infographic"):
        d = book / comp["path"]
        texts = {p.name: read_text(p) for p in list(_html_files(d)) + _js_files(d)}
        loads = [n for n, tx in texts.items() if re.search(r"<script[^>]+src=[\"'][^\"']*lrs-sim", tx, re.I)]
        creates = [n for n, tx in texts.items() if re.search(r"\bLRSSim\s*\.\s*create\s*\(", strip_js_comments(tx))]
        other = [n for n, tx in texts.items() if re.search(r"new\s+TinCan\b|ADL\.XAPIWrapper|\bxapiwrapper\b", strip_js_comments(tx), re.I)]
        if (loads and creates) or other:
            return {"level": "L2", "method": "static",
                    "evidence": [ev(f"{comp['path']}/{n}", "loads the LRS runtime") for n in loads] +
                                [ev(f"{comp['path']}/{n}", "calls LRSSim.create") for n in creates] +
                                [ev(f"{comp['path']}/{n}", "uses an xAPI client library") for n in other],
                    "creates_in": creates, "note": None}
        partial = None
        if loads and not creates:
            partial = "loads lrs-sim.js but never calls LRSSim.create, so it emits nothing"
        elif creates and not loads:
            partial = "calls LRSSim.create but does not load lrs-sim.js in this package"
        handler = re.compile(r"addEventListener|\bonclick\s*=|\bonchange\s*=|\boninput\s*=|mousePressed|mouseClicked|mouseDragged|keyPressed|createButton|createSlider|createSelect|createCheckbox|createInput|createRadio|<button\b|<input\b|<select\b|\.on\(\s*[\"']click", re.I)
        hits = [n for n, tx in texts.items() if handler.search(strip_js_comments(tx) if n.endswith(".js") else tx)]
        if hits:
            return {"level": "L1", "method": "static", "evidence": [ev(f"{comp['path']}/{n}", "interaction handlers") for n in hits[:6]],
                    "creates_in": [], "note": partial}
        return {"level": "L1", "method": "static", "evidence": [],
                "creates_in": [], "note": (partial + "; " if partial else "") + "typed as a MicroSim (at least L1); no interaction handlers were found"}
    if t == "quiz":
        text = read_text(book / comp["path"])
        if re.search(r"^\?\?\?\s+question|<details", text, flags=re.M):
            emitters = [s for s in (site_wide or []) if "quiz-emitter" in s["roles"]]
            if emitters and re.search(r"^\?\?\?\s+question", text, flags=re.M):
                return {"level": "L2", "method": "static",
                        "evidence": [ev("mkdocs.yml", f"extra_javascript loads {e['entry']} on every page; it emits an 'answered' statement per quiz question")
                                     for e in emitters] + [ev(comp["path"], "quiz uses the question markup the emitter reads")],
                        "creates_in": [], "site_wide": [e["path"] for e in emitters],
                        "note": "Instrumented by a site-wide script, not by code in the quiz."}
            return {"level": "L1", "method": "static", "evidence": [ev(comp["path"], "answers revealed on demand")],
                    "creates_in": [], "note": None}
        return {"level": "L0", "method": "static", "evidence": [], "creates_in": [], "note": None}
    return {"level": "L0", "method": "static", "evidence": [], "creates_in": [], "note": None}


# ---- individual checks ---------------------------------------------------------
def rp1_self_contained(book, comp, pkg, shared_as_declared: bool) -> dict:
    if comp["type"] in ("microsim", "interactive-infographic"):
        d = book / comp["path"]
        missing, outside, _ = _classify_local(d, pkg["local"])
        shared_only = bool(outside) and all(_SHARED_LIB_HINT.search(o["ref"]) for o in outside)
        if shared_as_declared and shared_only:
            outside_blocking = []
        else:
            outside_blocking = outside
        evid = [ev(f"{comp['path']}/{o['from']}", f"requires a file outside the component: {o['ref']}") for o in outside]
        evid += [ev(f"{comp['path']}/{m['from']}", f"missing file inside the component: {m['ref']}") for m in missing]
        value = {"outside_files": sorted({o["ref"] for o in outside}),
                 "missing_files": sorted({m["ref"] for m in missing}),
                 "shared_library_only": shared_only}
        if not outside_blocking and not missing:
            return result("pass", value, evid, note="Shared libraries treated as declared (policy flag)." if shared_as_declared and shared_only else None)
        note = None
        if shared_only and not missing:
            note = ("Every outside file is a conventional shared library. Copying the component alone breaks it, "
                    "though embedding the hosted page by iframe still works. Rerun with --shared-libs-as-declared to treat these as declared.")
        return result("fail", value, evid[:60], note=note)
    if comp["type"] == "static-figure":
        p = book / comp["path"]
        return result("pass" if p.exists() else "fail", {"files": [comp["path"]]}, [ev(comp["path"], "single asset" if p.is_file() else "poster directory")])
    # markdown components: embedded assets must live under the file's directory.
    # An iframe of another inventoried component (a MicroSim) is composition, not
    # a packaging defect, so it is recorded as a component dependency instead.
    p = book / comp["path"]
    text = strip_code_fences(read_text(p))
    if comp["type"] == "faq-pair":
        text = comp.get("answer_text", "")
    asset_refs = re.findall(r"!\[[^\]]*\]\(\s*<?([^)\s>]+)", text)
    asset_refs += re.findall(r"<(?:img|script)[^>]+src=[\"']([^\"']+)", text, flags=re.I)
    iframe_refs = re.findall(r"<iframe[^>]+src=[\"']([^\"']+)", text, flags=re.I)
    root = p.parent.resolve()
    outside, deps_ok, deps_missing = [], [], []
    for r in asset_refs:
        if _is_external(r) or r.startswith(("data:", "#")):
            continue
        t_ = safe_resolve(p.parent / r.split("#")[0].split("?")[0]) if len(r) < 400 else None
        if t_ is None:
            continue
        try:
            t_.relative_to(root)
        except ValueError:
            outside.append(r)
    for r in iframe_refs:
        if _is_external(r) or r.startswith(("data:", "#")) or len(r) >= 400:
            continue
        t_ = safe_resolve(p.parent / r.split("#")[0].split("?")[0])
        if t_ is None:
            continue
        if re.search(r"/docs/(sims|posters)/", t_.as_posix()):
            (deps_ok if safe_exists(t_) else deps_missing).append(r)
        else:
            try:
                t_.relative_to(root)
            except ValueError:
                outside.append(r)
    value = {"outside_files": sorted(set(outside)),
             "component_dependencies": sorted(set(deps_ok)),
             "component_dependencies_missing": sorted(set(deps_missing))}
    evid = [ev(comp["path"], f"embeds an asset outside its directory: {o}") for o in sorted(set(outside))[:30]]
    note = None
    if deps_ok or deps_missing:
        note = (f"Embeds {len(set(deps_ok))} other components by iframe"
                + (f" and {len(set(deps_missing))} that do not exist yet (see P11)" if deps_missing else "")
                + ". These are bundle relationships, not packaging defects.")
    return result("fail" if outside else "pass", value, evid, note=note)


def rp2_renders_standalone(book, comp, pkg) -> dict:
    if comp["type"] not in ("microsim", "interactive-infographic"):
        return result("N/A", None, [], note="Applies to HTML components. Markdown host-feature dependence is not scored in v0.1.")
    d = book / comp["path"]
    main = d / "main.html"
    if not main.exists():
        return result("fail", None, [ev(comp["path"], "no main.html to open on its own")], method="static")
    text = read_text(main)
    problems = []
    if not re.search(r"<html\b", text, re.I) or not re.search(r"<body\b", text, re.I):
        problems.append("main.html is not a complete HTML document")
    for r in pkg["local"]:
        if r["root_relative"] or not r["target"]:
            problems.append(f"root-relative reference depends on the host site: {r['ref']}")
        elif not Path(r["target"]).exists():
            problems.append(f"unresolved reference: {r['ref']} (in {r['from']})")
    problems = list(dict.fromkeys(problems))
    return result("fail" if problems else "pass", {"problems": problems},
                  [ev(f"{comp['path']}/main.html", p) for p in problems[:30]], method="static",
                  note="Static analysis only. A headless render would confirm it.")


def rp3_dependencies(book, comp, pkg, check_external: bool) -> dict:
    if comp["type"] not in ("microsim", "interactive-infographic"):
        return result("N/A", None, [], note="Applies to HTML components.")
    ext = {}
    for e in pkg["external"]:
        ext.setdefault(e["ref"], e["from"])
    items, evid = [], []
    unpinned = 0
    for url, frm in ext.items():
        host = re.sub(r"^(https?:)?//", "", url).split("/")[0]
        if host in _FONT_HOSTS:
            items.append({"url": url, "pinned": None, "exempt": "font service"})
            continue
        pinned = bool(_PIN.search(url)) and "latest" not in url.lower()
        if not pinned:
            unpinned += 1
            evid.append(ev(f"{comp['path']}/{frm}", f"external dependency not pinned to a version: {url}"))
        items.append({"url": url, "pinned": pinned})
    value = {"external": len(items), "unpinned": unpinned, "resolved_checked": False, "resolved": None, "items": items[:40]}
    if check_external and items:
        from net import head_ok
        res = {i["url"]: head_ok(("https:" + i["url"]) if i["url"].startswith("//") else i["url"]) for i in items[:40]}
        value["resolved_checked"] = True
        value["resolved"] = sum(1 for v in res.values() if v)
        for u, ok in res.items():
            if not ok:
                evid.append(ev(comp["path"], f"external dependency did not resolve: {u}"))
        bad = unpinned or value["resolved"] < len(res)
        return result("fail" if bad else "pass", value, evid, method="network")
    return result("fail" if unpinned else "pass", value, evid, method="static",
                  note="Pinning was checked from the URLs. Whether each URL resolves was not checked (offline); pass --check-external." if items else "No external dependencies.")


def rp4_license(book, comp, raw, book_p1) -> dict:
    if raw:
        src = _lookup_source(raw)
        k, v = _first(src, _LICENSE_PATHS)
        if v:
            text = v if isinstance(v, str) else str(v)
            lic = normalize_license(text) or text.strip()[:60]
            return result("pass", lic, [ev(f"{comp['path']} metadata", f"declared in '{k}'", text)], note="declared on the component")
    if book_p1.get("status") == "pass":
        return result("pass", book_p1["value"], [ev("book license (P1)", "inherited from the book")], note="inherited from the book")
    return result("fail", None, [ev(comp["path"], "no license on the component and none declared for the book")])


def rp5_metadata(book, comp, raw, source) -> tuple[dict, dict]:
    desc = describe_metadata(raw)
    has_container = comp["type"] in ("microsim", "interactive-infographic", "section") or raw is not None
    if comp["type"] == "faq-pair" and comp.get("question"):
        desc["present"]["title"] = comp["question"]
        desc["missing_required"] = [m for m in desc["missing_required"] if m != "title"]
    missing = desc["missing_required"]
    value = {
        "required_search_fields": {"present": [f for f in ("title", "description", "subject", "learningObjectives") if f not in missing],
                                  "missing": missing, "generic": desc["generic"]},
        "recommended_search_field": {"level": desc["present"].get("level"), "key": desc["level_key"]},
        "attribution_fields": {"creator": desc["present"].get("creator"), "version": desc["present"].get("version")},
        "source": source, "metadata_container": has_container,
    }
    evid = [ev(source or comp["path"], f"required search field missing: {m}") for m in missing]
    evid += [ev(source or comp["path"], f"required search field present but generic: {g}") for g in desc["generic"]
             if g not in desc.get("instruction_like_fields", [])]
    evid += [ev(source or comp["path"], f"required search field contains text addressed to an evaluator: {g}")
             for g in desc.get("instruction_like_fields", [])]
    note = None
    if not has_container:
        note = "This component type has no machine-readable metadata container."
    if not desc["present"].get("level"):
        note = (note + " " if note else "") + "No level field (gradeLevel, educationalLevel, audience, coverage)."
    elif desc["level_key"] not in ("gradeLevel", "educational.gradeLevel"):
        note = (note + " " if note else "") + f"Level is in '{desc['level_key']}', which the catalog's WHAT text does not read (it reads gradeLevel)."
    return result("pass" if not missing else "fail", value, evid, note=note), desc


def rp6_editable(book, comp, pkg) -> dict:
    t = comp["type"]
    if t in ("microsim", "interactive-infographic"):
        d = book / comp["path"]
        js = [p for p in d.glob("*.js")]
        readable = [p for p in js if ".min." not in p.name and p.stat().st_size < 600_000]
        inline = 0
        main = d / "main.html"
        if main.exists():
            inline = sum(len(m) for m in re.findall(r"<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>", read_text(main), flags=re.S | re.I))
        minified_only = bool(js) and not readable
        if readable or inline > 200:
            return result("pass", True, [ev(f"{comp['path']}/{p.name}", "readable source") for p in readable[:5]]
                          or [ev(f"{comp['path']}/main.html", f"{inline} characters of inline script")])
        if minified_only:
            return result("fail", False, [ev(comp["path"], "only minified JavaScript")])
        return result("fail", False, [ev(comp["path"], "no readable script source found")])
    if t == "static-figure":
        p = book / comp["path"]
        if p.is_dir():
            sources = [f.name for f in p.iterdir() if f.suffix.lower() in (".svg", ".drawio", ".pptx", ".psd", ".ai")]
            return result("pass" if sources else "fail", bool(sources),
                          [ev(f"{comp['path']}/{s}", "editable source") for s in sources] or
                          [ev(comp["path"], "raster output only; no editable source found")])
        suf = p.suffix.lower()
        if suf == ".svg":
            return result("pass", True, [ev(comp["path"], "SVG is editable")])
        return result("fail", False, [ev(comp["path"], f"{suf} raster image with no editable source alongside")])
    return result("pass", True, [ev(comp["path"], "Markdown source")])


def _links(text: str) -> list[str]:
    t = strip_code_fences(text)
    out = re.findall(r"(?<!\!)\[[^\]]*\]\(\s*<?([^)\s>]+)", t)
    out += re.findall(r"<(?:a|iframe)[^>]+(?:href|src)=[\"']([^\"']+)", t, flags=re.I)
    return out


def rp7_companions(book, comp, inventory) -> dict:
    t = comp["type"]
    chapters = {c["dir"]: c for c in inventory["chapters"]}
    if t in ("microsim", "interactive-infographic"):
        sid = comp["id"].split("/", 1)[1]
        idx = book / comp["path"] / "index.md"
        recorded = []
        for l in _links(read_text(idx)):
            if l.endswith("quiz.md") or re.search(r"/quiz(/|\.md)?$", l):
                recorded.append(l)
        # candidates: chapters that embed this sim, and their quizzes
        cands = []
        for ch in inventory["chapters"]:
            md = book / ch["index_path"] if ch.get("index_path") else None
            if md and re.search(rf"sims/{re.escape(sid)}/", read_text(md)) and ch["has_quiz"]:
                cands.append(f"docs/chapters/{ch['dir']}/quiz.md")
        if recorded:
            return result("pass", recorded, [ev(f"{comp['path']}/index.md", f"links to {r}") for r in recorded])
        if cands:
            return result("fail", None, [ev(c, "chapter quiz exists for a chapter that embeds this MicroSim, but the MicroSim does not name it") for c in cands],
                          note="Candidate companions are inferred from chapter embedding, not recorded by the component.")
        return result("N/A", None, [], note="No quiz found that pairs with this MicroSim.")
    if t == "quiz":
        text = read_text(book / comp["path"])
        sims = [l for l in _links(text) if "sims/" in l]
        ch = chapters.get(comp.get("chapter", ""))
        cands = []
        if ch and ch.get("index_path"):
            cands = sorted(set(re.findall(r"sims/([A-Za-z0-9_.-]+)/", read_text(book / ch["index_path"]))))
        if sims:
            return result("pass", sims, [ev(comp["path"], f"links to {s}") for s in sims[:10]])
        if cands:
            return result("fail", None, [ev(f"docs/chapters/{comp.get('chapter')}/index.md", f"embeds MicroSim '{c}' but the quiz does not name it") for c in cands[:10]],
                          note="Candidate companions are inferred from chapter embedding, not recorded by the component.")
        return result("N/A", None, [], note="No MicroSim found that pairs with this quiz.")
    return result("N/A", None, [], note="Bundle companions apply to MicroSims and quizzes.")


def _resolve_identifier(name: str, text: str, depth: int = 0):
    """Resolve NAME to a string or number literal through simple assignments,
    following at most two hops (c = PAGE_CONCEPT; PAGE_CONCEPT = 353)."""
    m = re.search(rf"\b{re.escape(name)}\s*=\s*(?:[\"']([^\"']+)[\"']|(\d+)\b|([A-Za-z_]\w*)\s*[;,\n])", text)
    if not m:
        return None
    if m.group(1):
        return m.group(1)
    if m.group(2):
        return m.group(2)
    if m.group(3) and depth < 2 and m.group(3) not in ("null", "undefined", "true", "false"):
        return _resolve_identifier(m.group(3), text, depth + 1)
    return None


def rp9_concepts(book, comp, level_info, graph=None) -> dict:
    """Concept ids passed to the LRS runtime. A `concept` option on
    LRSSim.create, lrs.item, lrs.question or lrs.button is the mapping; its
    values are listed when they can be resolved to a string or number literal
    and flagged as computed otherwise. Nothing is guessed."""
    if level_info["level"] != "L2":
        return result("N/A", None, [], note="Applies to level L2 components.")
    if comp["type"] == "quiz":
        qt = strip_code_fences(read_text(book / comp["path"]))
        n_q = len(re.findall(r"^#{3,5}\s*\d+[.)]\s+\S", qt, flags=re.M)) or len(re.findall(r"^\?\?\?\s+question", qt, flags=re.M))
        n_c = len(re.findall(r"\*\*Concept Tested:?\*\*", qt))
        from common import slug as _slug
        labels = re.findall(r"\*\*Concept Tested:?\*\*\s*([^\n]+)", qt)
        value = {"questions": n_q, "with_concept_tested": n_c, "source": "Concept Tested labels, slugged by the site-wide emitter"}
        if graph is not None:
            hit = [l for l in labels if _slug(l.strip()) in graph["slugs"]]
            value["learning_graph"] = {"checked": True, "labels": len(labels), "matched": len(hit),
                                       "unmatched": [l.strip() for l in labels if l not in hit][:20]}
            note = "The emitter derives the concept id by slugging the label; only labels that equal a learning-graph label join the rollup."
        else:
            value["learning_graph"] = {"checked": False, "reason": "no learning graph found"}
            note = "The emitter derives the concept id from the label. No learning graph was found to check it against."
        ok = n_q > 0 and n_c >= n_q
        return result("pass" if ok else "fail", value,
                      [ev(comp["path"], f"{n_c} of {n_q} questions carry a Concept Tested label")], note=note)
    d = book / comp["path"]
    ids: set[str] = set()
    option_found = False
    computed = False
    evid = []
    names = list(dict.fromkeys(level_info["creates_in"] + [p.name for p in _js_files(d)]))
    for name in names:
        text = strip_js_comments(read_text(d / name))
        if "LRSSim" not in text and not re.search(r"\blrs\.(item|question|button)", text):
            continue
        before = (len(ids), option_found, computed)
        for m in re.finditer(r"\bconcept\s*:\s*([^,}\n]+)", text):
            option_found = True
            expr = m.group(1).strip().rstrip(";")
            if re.match(r"^[\"'][^\"']+[\"']$", expr):
                ids.add(expr.strip("\"'"))
            elif re.match(r"^\d+$", expr):
                ids.add(expr)
            else:
                base = re.match(r"[A-Za-z_]\w*", expr)
                if base and "(" not in expr and "[" not in expr:
                    lit = _resolve_identifier(base.group(0), text)
                    if lit is not None:
                        ids.add(lit)
                    else:
                        computed = True
                else:
                    computed = True
        for blk in re.finditer(r"\b\w*(?:CONCEPTS?|[Cc]oncepts?Map)\w*\s*=\s*\{(.*?)\}", text, flags=re.S):
            for v in re.findall(r":\s*(?:[\"']([^\"']+)[\"']|(\d+)\b)", blk.group(1)):
                ids.add(v[0] or v[1])
        if (len(ids), option_found, computed) != before:
            evid.append(ev(f"{comp['path']}/{name}", "concept option passed to the LRS runtime"))
    if option_found or ids:
        value = {"concept_ids": sorted(ids)[:60], "computed_values": computed,
                 "learning_graph": match_concepts(sorted(ids), graph)}
        notes = []
        if computed:
            notes.append("Some concept values are computed in code and could not be listed.")
        lg = value["learning_graph"]
        if lg.get("checked") and lg["unmatched"]:
            notes.append(f"{len(lg['unmatched'])} of {len(ids)} listed concept ids do not join this book's learning graph, "
                         "so the concept rollup may drop their statements.")
        return result("pass", value, evid[:6], note=" ".join(notes) or None)
    return result("fail", None, [ev(comp["path"], "events are emitted but no concept option was found")])



# ---- learning-graph join (RP9) -------------------------------------------------------
def load_learning_graph(book: Path) -> dict | None:
    """Concept ids and label slugs from docs/learning-graph/learning-graph.{json,csv}."""
    from common import slug
    base = book / "docs" / "learning-graph"
    ids, slugs = set(), set()
    j = read_json(base / "learning-graph.json")
    nodes = (j.get("nodes") if isinstance(j, dict) else j) if j else None
    if isinstance(nodes, list):
        for n in nodes:
            if isinstance(n, dict):
                if n.get("id") is not None:
                    ids.add(str(n["id"]))
                if isinstance(n.get("label"), str):
                    slugs.add(slug(n["label"]))
    elif (base / "learning-graph.csv").exists():
        import csv
        with open(base / "learning-graph.csv", newline="", encoding="utf-8", errors="replace") as f:
            for row in csv.DictReader(f):
                if row.get("ConceptID"):
                    ids.add(str(row["ConceptID"]).strip())
                if row.get("ConceptLabel"):
                    slugs.add(slug(row["ConceptLabel"]))
    if not ids and not slugs:
        return None
    return {"ids": ids, "slugs": slugs, "count": max(len(ids), len(slugs))}


def match_concepts(concept_ids: list[str], graph: dict | None) -> dict:
    """Which emitted concept ids join the learning graph. Numeric ids and
    '<book>-<id>' forms match a ConceptID; slugs match a slugged label."""
    from common import slug
    if graph is None:
        return {"checked": False, "reason": "no learning graph found at docs/learning-graph/"}
    matched, unmatched = [], []
    for cid in concept_ids:
        s = str(cid)
        tail = re.search(r"-(\d+)$", s)
        if s in graph["ids"] or (tail and tail.group(1) in graph["ids"]) or slug(s) in graph["slugs"]:
            matched.append(s)
        else:
            unmatched.append(s)
    return {"checked": True, "graph_concepts": graph["count"], "matched": matched, "unmatched": unmatched}

def run_component_checks(book: Path, comp: dict, inventory: dict, book_checks: dict,
                         shared_as_declared: bool = False, check_external: bool = False,
                         site_wide: list[dict] | None = None, graph: dict | None = None) -> dict:
    t = comp["type"]
    pkg = analyze_package(book / comp["path"]) if t in ("microsim", "interactive-infographic") else {"local": [], "external": [], "files": []}
    raw, source = load_metadata(book, comp)
    lvl = interactivity(book, comp, site_wide)
    rp5, desc = rp5_metadata(book, comp, raw, source)
    checks = {
        "RP1": rp1_self_contained(book, comp, pkg, shared_as_declared),
        "RP2": rp2_renders_standalone(book, comp, pkg),
        "RP3": rp3_dependencies(book, comp, pkg, check_external),
        "RP4": rp4_license(book, comp, raw, book_checks["P1"]),
        "RP5": rp5,
        "RP6": rp6_editable(book, comp, pkg),
        "RP7": rp7_companions(book, comp, inventory),
        "RP8": result("recorded", lvl["level"], lvl["evidence"], method=lvl["method"], note=lvl["note"],
                      extra={"delivery": delivery(book, comp, site_wide or [])} if lvl["level"] == "L2" else None),
        "RP9": rp9_concepts(book, comp, lvl, graph),
    }
    return {"checks": checks, "interactivity": lvl["level"], "metadata": desc}
