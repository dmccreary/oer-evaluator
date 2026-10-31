"""Tier 1 book-level checks P1-P13 (spec Section 5).

Every check returns {status, value, evidence, method, note}. status is
pass | fail | ISE (could not be determined) | N/A. A check never guesses:
when evidence cannot be found the result is fail or ISE, with the locations
that were searched.
"""
from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote

from common import (ev, is_placeholder_text, mkdocs_scalar, parse_frontmatter, read_text,
                    result, safe_exists, safe_resolve, sections, strip_code_fences)

CC_PATTERNS = [
    (r"CC[\s-]*BY[\s-]*NC[\s-]*SA[\s-]*(\d\.\d)", "CC-BY-NC-SA-{v}"),
    (r"CC[\s-]*BY[\s-]*NC[\s-]*ND[\s-]*(\d\.\d)", "CC-BY-NC-ND-{v}"),
    (r"CC[\s-]*BY[\s-]*NC[\s-]*(\d\.\d)", "CC-BY-NC-{v}"),
    (r"CC[\s-]*BY[\s-]*SA[\s-]*(\d\.\d)", "CC-BY-SA-{v}"),
    (r"CC[\s-]*BY[\s-]*ND[\s-]*(\d\.\d)", "CC-BY-ND-{v}"),
    (r"CC[\s-]*BY[\s-]*(\d\.\d)", "CC-BY-{v}"),
    (r"CC0", "CC0-1.0"),
    (r"Attribution-NonCommercial-ShareAlike\s*(\d\.\d)", "CC-BY-NC-SA-{v}"),
    (r"Attribution-NonCommercial-NoDerivatives\s*(\d\.\d)", "CC-BY-NC-ND-{v}"),
    (r"Attribution-NonCommercial\s*(\d\.\d)", "CC-BY-NC-{v}"),
    (r"Attribution-ShareAlike\s*(\d\.\d)", "CC-BY-SA-{v}"),
    (r"Attribution\s*(\d\.\d)\s*International", "CC-BY-{v}"),
    (r"\bMIT License\b", "MIT"),
    (r"Apache License,? Version 2\.0", "Apache-2.0"),
]


def normalize_license(text: str) -> str | None:
    for pat, fmt in CC_PATTERNS:
        m = re.search(pat, text or "", flags=re.I)
        if m:
            return fmt.format(v=m.group(1)) if "{v}" in fmt and m.groups() else fmt
    return None


def _md_files(docs: Path) -> list[Path]:
    out = []
    for p in sorted(docs.rglob("*.md")):
        rel = p.relative_to(docs).as_posix()
        if rel.startswith(("prompts/",)) or re.search(r"image-prompts?.*\.md$|cover-prompt\.md$|TODO\.md$", rel):
            continue
        out.append(p)
    return out


def book_context(book: Path) -> dict:
    mk = read_text(book / "mkdocs.yml")
    return {
        "book": book,
        "docs": book / "docs",
        "mkdocs_text": mk,
        "site_url": mkdocs_scalar(mk, "site_url"),
        "site_name": mkdocs_scalar(mk, "site_name") or book.name,
        "site_author": mkdocs_scalar(mk, "site_author"),
        "copyright": mkdocs_scalar(mk, "copyright"),
    }


def p1_license(ctx) -> dict:
    book, docs = ctx["book"], ctx["docs"]
    searched = []
    for label, text in (
        ("mkdocs.yml copyright", ctx["copyright"] or ""),
        ("docs/license.md", read_text(docs / "license.md")),
        ("LICENSE", read_text(book / "LICENSE")),
        ("LICENSE.md", read_text(book / "LICENSE.md")),
    ):
        searched.append(label)
        lic = normalize_license(text)
        if lic:
            nc = "-NC" in lic
            nd = "-ND" in lic
            note = None
            if nc or nd:
                note = "Declared and identifiable, but the NonCommercial/NoDerivatives term restricts some reuse."
            return result("pass", lic, [ev(label, f"license identified as {lic}")], note=note)
    return result("fail", None, [ev(", ".join(searched), "no recognizable license text found")])


def p2_creators(ctx) -> dict:
    names, evid = [], []
    if ctx["site_author"]:
        names.append(ctx["site_author"])
        evid.append(ev("mkdocs.yml site_author", ctx["site_author"]))
    about = read_text(ctx["docs"] / "about.md")
    sec = sections(about, r"#{1,3}")
    for title, body in sec.items():
        if title in ("author", "authors", "creator", "creators", "about the author"):
            line = next((l.strip() for l in body.split("\n") if l.strip()), "")
            if line and not is_placeholder_text(line):
                names.append(line)
                evid.append(ev("docs/about.md", f"## {title}", line))
    names = list(dict.fromkeys(n for n in names if n))
    if names:
        return result("pass", names, evid)
    return result("fail", None, [ev("mkdocs.yml, docs/about.md", "no author or creator found")])


def p3_sponsor(ctx) -> dict:
    pat = re.compile(r"(sponsored by|funded by|supported by|funding(?: provided)? by|publisher:)\s*([^\n.<]{3,100})", re.I)
    for label, path in (("mkdocs.yml", ctx["book"] / "mkdocs.yml"), ("docs/about.md", ctx["docs"] / "about.md"),
                        ("docs/index.md", ctx["docs"] / "index.md"), ("docs/license.md", ctx["docs"] / "license.md")):
        m = pat.search(read_text(path))
        if m:
            return result("pass", m.group(2).strip(), [ev(label, m.group(0).strip())],
                          note="Recorded as a signal. Prestige is never scored (decision D3).")
    return result("fail", None, [ev("mkdocs.yml, docs/about.md, docs/index.md, docs/license.md", "no sponsor or publisher statement found")])


OBJ_HEADING = re.compile(r"learning (objectives?|outcomes?|goals?)|objectives", re.I)
OBJ_PHRASE = re.compile(
    r"(by the end of (this|the) (chapter|lesson|unit|module|course)[^.\n]{0,80}?(you|students|learners)[^.\n]{0,30}?(will|should|'ll|be able))"
    r"|(students? (will|should) be able to)|(learners? (will|should) be able to)", re.I)


def p4_objectives(ctx, chapters: list[dict]) -> dict:
    docs = ctx["docs"]
    evid = []
    course = []
    cd = read_text(docs / "course-description.md")
    for title, body in sections(cd, r"#{2,3}").items():
        if re.search(r"learning (outcomes|objectives)", title):
            for l in body.split("\n"):
                m = re.match(r"^\s*[-*]\s+(?:\*\*[^*]+\*\*:?\s*)?(.+)$", l)
                if m and not is_placeholder_text(m.group(1)):
                    course.append(m.group(1).strip())
    if course:
        evid.append(ev("docs/course-description.md", f"{len(course)} course-level outcomes"))
    per_chapter = {}
    for ch in chapters:
        if not ch.get("index_path"):
            continue
        text = strip_code_fences(read_text(ctx["book"] / ch["index_path"]))
        found = None
        for title, body in sections(text, r"#{2,3}").items():
            if OBJ_HEADING.search(title) and re.search(r"^\s*([-*]|\d+\.)\s+\S", body, flags=re.M):
                found = f"heading '{title}'"
                break
        if not found:
            m = OBJ_PHRASE.search(text)
            if m:
                found = f"phrase: {m.group(0)[:80]}"
        per_chapter[ch["dir"]] = found
        if found:
            evid.append(ev(ch["index_path"], found))
    n = len(per_chapter)
    k = sum(1 for v in per_chapter.values() if v)
    value = {"course_level": len(course), "chapters_with_objectives": k, "chapters": n,
             "missing": [d for d, v in per_chapter.items() if not v]}
    # Pass when the course states outcomes, or every chapter states its own.
    ok = len(course) > 0 or (n > 0 and k == n)
    if not course and n == 0:
        return result("fail", value, [ev("docs/course-description.md, docs/chapters/", "no objectives found")])
    note = None
    if ok and course and n and k < n:
        note = f"Course-level outcomes exist, but {n - k} of {n} chapters state no objectives of their own."
    return result("pass" if ok else "fail", value, evid[:40], note=note)


def _section_text(path: Path, pattern: str) -> tuple[str, str] | None:
    for title, body in sections(read_text(path), r"#{1,3}").items():
        if re.search(pattern, title):
            b = body.strip()
            if b and not is_placeholder_text(b):
                return title, b
    return None


def p5_learners(ctx) -> dict:
    for rel in ("course-description.md", "about.md"):
        hit = _section_text(ctx["docs"] / rel, r"^audience|intended (reader|audience)|who (this|the) (book|course) is for")
        if hit:
            return result("pass", hit[1][:300], [ev(f"docs/{rel}", f"## {hit[0]}", hit[1][:120])])
    return result("fail", None, [ev("docs/course-description.md, docs/about.md", "no audience statement, or only scaffold text")])


def p6_prereqs(ctx, chapters: list[dict]) -> dict:
    evid = []
    book_level = _section_text(ctx["docs"] / "course-description.md", r"^prerequisites?")
    if book_level:
        evid.append(ev("docs/course-description.md", "## Prerequisites", book_level[1][:120]))
    with_pr = 0
    for ch in chapters:
        if ch.get("index_path") and _section_text(ctx["book"] / ch["index_path"], r"^prerequisites?"):
            with_pr += 1
    if with_pr:
        evid.append(ev("docs/chapters/*/index.md", f"{with_pr} of {len(chapters)} chapters have a Prerequisites section"))
    if book_level or with_pr:
        return result("pass", {"course_level": bool(book_level), "chapters_with_prerequisites": with_pr, "chapters": len(chapters)}, evid)
    return result("fail", None, [ev("docs/course-description.md, docs/chapters/*/index.md", "no prerequisites found")])


def p7_instructions(ctx) -> dict:
    pat = r"how to use|using this (book|textbook|course)|how to read|getting started|how to navigate"
    for rel in ("about.md", "index.md"):
        hit = _section_text(ctx["docs"] / rel, pat)
        if hit:
            return result("pass", True, [ev(f"docs/{rel}", f"## {hit[0]}")])
    return result("fail", False, [ev("docs/about.md, docs/index.md", "no 'how to use' section found")])


def p8_accessibility(ctx) -> dict:
    docs = ctx["docs"]
    if (docs / "accessibility.md").exists():
        return result("pass", True, [ev("docs/accessibility.md", "dedicated page")])
    for rel in ("about.md", "index.md", "license.md", "contact.md", "course-description.md"):
        text = read_text(docs / rel)
        m = re.search(r".{0,60}accessib.{0,80}", text, flags=re.I)
        if m:
            return result("pass", True, [ev(f"docs/{rel}", "mentions accessibility", m.group(0))])
    m = re.search(r".{0,40}accessib.{0,60}", ctx["mkdocs_text"], flags=re.I)
    if m:
        return result("pass", True, [ev("mkdocs.yml", "mentions accessibility", m.group(0))])
    return result("fail", False, [ev("docs/*.md, mkdocs.yml", "no accessibility statement found")])


def p9_tech_requirements(ctx) -> dict:
    pat = re.compile(r"(technical|system|software|hardware)\s+requirements|supported browsers?|browser requirements|what you.?ll need|you will need", re.I)
    for rel in ("about.md", "index.md", "course-description.md", "faq.md"):
        text = read_text(ctx["docs"] / rel)
        m = pat.search(text)
        if m:
            line = text[max(0, m.start() - 20): m.end() + 80].replace("\n", " ")
            return result("pass", True, [ev(f"docs/{rel}", "technical requirements wording", line)])
    return result("fail", False, [ev("docs/about.md, docs/index.md, docs/course-description.md, docs/faq.md", "no technical requirements statement found")])


def p10_references(ctx, chapters: list[dict]) -> dict:
    docs = ctx["docs"]
    def count_items(p: Path) -> int:
        return len(re.findall(r"^\s*(?:\d+\.|[-*])\s+\S", strip_code_fences(read_text(p)), flags=re.M))
    per = {}
    book_refs = docs / "references.md"
    total = 0
    if book_refs.exists():
        n = count_items(book_refs)
        per["docs/references.md"] = n
        total += n
    for ch in chapters:
        p = ctx["book"] / "docs" / "chapters" / ch["dir"] / "references.md"
        if p.exists():
            n = count_items(p)
            per[f"docs/chapters/{ch['dir']}/references.md"] = n
            total += n
    evid = [ev(k, f"{v} reference entries") for k, v in list(per.items())[:40]]
    if total > 0:
        return result("pass", {"total": total, "files": len(per)}, evid)
    return result("fail", {"total": 0, "files": 0}, [ev("docs/references.md, docs/chapters/*/references.md", "no reference lists found")])


LINK_RE = re.compile(r"(?<!\!)\[[^\]]*\]\(\s*<?([^)\s>]+)")
IMG_RE = re.compile(r"!\[[^\]]*\]\(\s*<?([^)\s>]+)")
HTMLREF_RE = re.compile(r"<(?:a|img|iframe|source|script|link)\b[^>]*?\b(?:href|src)=[\"']([^\"']+)[\"']", re.I)


def _resolve_internal(md: Path, docs: Path, ref: str) -> tuple[bool, str]:
    ref = unquote(ref.split("#")[0].split("?")[0])
    if not ref:
        return True, ""
    if len(ref) > 400:
        return False, ref[:80]
    base = docs if ref.startswith("/") else md.parent
    target = safe_resolve(base / ref.lstrip("/"))
    if target is None:
        return False, ref[:80]
    candidates = [target]
    if target.suffix == "":
        candidates += [target / "index.md", target.with_suffix(".md"), target / "index.html"]
    return any(safe_exists(c) for c in candidates), str(target)


def p11_links(ctx, check_external: bool = False) -> dict:
    docs = ctx["docs"]
    internal_total = internal_ok = 0
    external = []
    broken = []
    for md in _md_files(docs):
        text = strip_code_fences(read_text(md))
        refs = LINK_RE.findall(text) + IMG_RE.findall(text) + HTMLREF_RE.findall(text)
        for ref in refs:
            if ref.startswith(("mailto:", "tel:", "javascript:", "#", "data:")) or "{{" in ref or "{%" in ref:
                continue
            if re.match(r"^[a-z][a-z0-9+.-]*://", ref, re.I):
                external.append((md.relative_to(ctx["book"]).as_posix(), ref))
                continue
            internal_total += 1
            ok, tgt = _resolve_internal(md, docs, ref)
            if ok:
                internal_ok += 1
            else:
                broken.append(ev(md.relative_to(ctx["book"]).as_posix(), f"unresolved link: {ref}"))
    pct = round(100.0 * internal_ok / internal_total, 1) if internal_total else 100.0
    value = {"internal_total": internal_total, "internal_resolved": internal_ok,
             "internal_percent": pct, "external_total": len(external),
             "external_checked": False, "external_resolved": None}
    note = "External links were not checked (offline). Pass --check-external to test them."
    if check_external and external:
        from net import head_ok
        ok_n = 0
        urls = sorted({u for _, u in external})
        res = {u: head_ok(u) for u in urls[:300]}
        for _, u in external:
            if res.get(u):
                ok_n += 1
        value.update({"external_checked": True, "external_resolved": ok_n})
        for loc, u in external:
            if u in res and not res[u] and len(broken) < 200:
                broken.append(ev(loc, f"external link did not resolve: {u}"))
        note = None
    status = "pass" if internal_ok == internal_total and (not value["external_checked"] or value["external_resolved"] == len(external)) else "fail"
    return result(status, value, broken[:200], method="static" if not check_external else "network", note=note)


def p12_practice(ctx, chapters: list[dict]) -> dict:
    per, evid = {}, []
    for ch in chapters:
        qp = ctx["docs"] / "chapters" / ch["dir"] / "quiz.md"
        if not qp.exists():
            per[ch["dir"]] = 0
            continue
        text = strip_code_fences(read_text(qp))
        n = len(re.findall(r"^#{3,5}\s*\d+[.)]\s+\S", text, flags=re.M))
        if n == 0:
            n = len(re.findall(r"^\?\?\?\s+question", text, flags=re.M))
        if n == 0:
            n = len(re.findall(r"^\s*\d+\.\s+\*\*", text, flags=re.M))
        per[ch["dir"]] = n
        evid.append(ev(f"docs/chapters/{ch['dir']}/quiz.md", f"{n} questions"))
    missing = [d for d, n in per.items() if n == 0]
    value = {"per_chapter": per, "chapters": len(per), "chapters_without_items": missing,
             "total_items": sum(per.values())}
    if not per:
        return result("fail", value, [ev("docs/chapters/", "no chapters found")])
    return result("pass" if not missing else "fail", value, evid[:60])


def p13_alt_text(ctx) -> dict:
    total = with_alt = 0
    missing = []
    for md in _md_files(ctx["docs"]):
        text = strip_code_fences(read_text(md))
        for m in re.finditer(r"!\[([^\]]*)\]\(\s*<?([^)\s>]+)", text):
            total += 1
            if m.group(1).strip():
                with_alt += 1
            elif len(missing) < 200:
                missing.append(ev(md.relative_to(ctx["book"]).as_posix(), f"image without alt text: {m.group(2)}"))
        for m in re.finditer(r"<img\b[^>]*>", text, flags=re.I):
            total += 1
            tag = m.group(0)
            alt = re.search(r"\balt=[\"']([^\"']*)[\"']", tag, flags=re.I)
            if alt and alt.group(1).strip():
                with_alt += 1
            elif len(missing) < 200:
                src = re.search(r"\bsrc=[\"']([^\"']+)", tag, flags=re.I)
                missing.append(ev(md.relative_to(ctx["book"]).as_posix(), f"<img> without alt text: {src.group(1) if src else '?'}"))
    pct = round(100.0 * with_alt / total, 1) if total else 100.0
    value = {"images": total, "with_alt": with_alt, "percent": pct}
    if total == 0:
        return result("N/A", value, [ev("docs/**/*.md", "no images found")])
    return result("pass" if with_alt == total else "fail", value, missing)


def run_book_checks(book: Path, inventory: dict, check_external: bool = False) -> dict:
    ctx = book_context(book)
    chapters = inventory["chapters"]
    return {
        "P1": p1_license(ctx), "P2": p2_creators(ctx), "P3": p3_sponsor(ctx),
        "P4": p4_objectives(ctx, chapters), "P5": p5_learners(ctx),
        "P6": p6_prereqs(ctx, chapters), "P7": p7_instructions(ctx),
        "P8": p8_accessibility(ctx), "P9": p9_tech_requirements(ctx),
        "P10": p10_references(ctx, chapters), "P11": p11_links(ctx, check_external),
        "P12": p12_practice(ctx, chapters), "P13": p13_alt_text(ctx),
    }, ctx
