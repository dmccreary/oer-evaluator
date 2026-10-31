"""Component inventory (spec Section 4) and chapter weights (Section 7).

Detection follows the packaging conventions documented in the author's
microsim-generator, faq-generator and quiz-generator skills:

  MicroSim / interactive infographic  docs/sims/<id>/{main.html,index.md,metadata.json}
  static figure                       docs/posters/<slug>/ or images referenced from chapters
  FAQ pair                            docs/faq.md, one '###' question per pair
  chapter quiz                        docs/chapters/<dir>/quiz.md
  glossary                            docs/glossary.md

Types with no packaging convention (worked example, instructor material) are
listed as not detected, never guessed.
"""
from __future__ import annotations

import re
from pathlib import Path

from common import (PLACEHOLDER_SIM_IDS, PLACEHOLDER_TITLE_MARKERS, parse_frontmatter,
                    read_json, read_text, safe_exists, safe_resolve, sections, slug, strip_code_fences, word_count)

IMAGE_EXT = (".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp")


def _concepts_covered(index_text: str) -> tuple[int | None, str]:
    """Count rows of the 'Concepts Covered' section. Handles the table format
    (book-chapter-generator v1.0.0+) and the older numbered list."""
    secs = sections(index_text, r"#{2,3}")
    body = None
    for title, text in secs.items():
        if title.startswith("concepts covered"):
            body = text
            break
    if body is None:
        return None, "missing"
    rows = [l for l in body.split("\n") if l.strip().startswith("|")]
    if rows:
        data = [r for r in rows
                if not re.match(r"^\s*\|\s*:?-{2,}", r)
                and not re.match(r"^\s*\|\s*Concept\s*\|", r, re.I)]
        return len(data), "table"
    numbered = re.findall(r"^\s*\d+\.\s+\S", body, flags=re.M)
    if numbered:
        return len(numbered), "numbered-list"
    bullets = re.findall(r"^\s*[-*]\s+\S", body, flags=re.M)
    if bullets:
        return len(bullets), "bullet-list"
    return 0, "empty"


def _is_placeholder_sim(sim_dir: Path, title: str) -> bool:
    sid = sim_dir.name.lower()
    if sid in PLACEHOLDER_SIM_IDS or sid.startswith("template-"):
        return True
    t = (title or "").strip().lower()
    return any(m in t for m in PLACEHOLDER_TITLE_MARKERS)


def _sim_title(sim_dir: Path) -> str:
    meta = read_json(sim_dir / "metadata.json")
    if isinstance(meta, dict):
        for k in ("title", "name"):
            if isinstance(meta.get(k), str) and meta[k].strip():
                return meta[k].strip()
        micro = meta.get("microsim")
        if isinstance(micro, dict):
            dc = micro.get("dublinCore") or {}
            if isinstance(dc.get("title"), str):
                return dc["title"]
    fm, body = parse_frontmatter(read_text(sim_dir / "index.md"))
    return fm.get("title", "") or sim_dir.name


def build_inventory(book: Path) -> dict:
    docs = book / "docs"
    components: list[dict] = []
    chapters: list[dict] = []
    notes: list[str] = []

    # ---- chapters, quizzes, weights ------------------------------------
    chap_root = docs / "chapters"
    chapter_dirs = sorted(p for p in chap_root.iterdir() if p.is_dir()) if chap_root.is_dir() else []
    any_concept_table = False
    for cdir in chapter_dirs:
        idx = cdir / "index.md"
        text = read_text(idx)
        fm, body = parse_frontmatter(text)
        n_concepts, fmt = _concepts_covered(text)
        if n_concepts is not None:
            any_concept_table = True
        quiz = cdir / "quiz.md"
        refs = cdir / "references.md"
        chapters.append({
            "id": f"chapters/{cdir.name}",
            "dir": cdir.name,
            "title": fm.get("title") or (re.search(r"^#\s+(.+)$", body, flags=re.M) or [None, cdir.name])[1],
            "index_path": str(idx.relative_to(book)) if idx.exists() else None,
            "concept_count": n_concepts,
            "concept_format": fmt,
            "word_count": word_count(body),
            "has_quiz": quiz.exists(),
            "has_references": refs.exists(),
        })
        if idx.exists():
            components.append({
                "id": f"chapters/{cdir.name}", "type": "section",
                "path": str(idx.relative_to(book)), "title": chapters[-1]["title"],
                "chapter": cdir.name,
            })
        if quiz.exists():
            components.append({
                "id": f"chapters/{cdir.name}/quiz", "type": "quiz",
                "path": str(quiz.relative_to(book)),
                "title": f"Quiz: {chapters[-1]['title']}", "chapter": cdir.name,
            })

    # chapter weights: concepts if every content chapter has a table/list, else words
    scale = "none"
    if chapters:
        if all(c["concept_count"] is not None for c in chapters):
            scale = "concepts"
        else:
            scale = "words"
    for c in chapters:
        if scale == "concepts":
            c["weight"] = c["concept_count"]
        elif scale == "words":
            c["weight"] = c["word_count"]
        else:
            c["weight"] = 0
        # A chapter that lists no concepts (front matter) carries no weight.
        if scale == "concepts" and not c["concept_count"]:
            c["weight"] = 0
    if scale == "words" and any_concept_table:
        notes.append("Some chapters have Concepts Covered tables and some do not; word count is used for every chapter so weights are never mixed across scales.")

    # ---- MicroSims and interactive infographics ------------------------
    sims_root = docs / "sims"
    if sims_root.is_dir():
        for sdir in sorted(p for p in sims_root.iterdir() if p.is_dir()):
            has_main = (sdir / "main.html").exists()
            has_idx = (sdir / "index.md").exists()
            has_js = any(sdir.glob("*.js"))
            if not (has_main or (has_idx and has_js)):
                continue  # shared-libs, assets, etc.
            title = _sim_title(sdir)
            if _is_placeholder_sim(sdir, title):
                notes.append(f"Excluded scaffold sim '{sdir.name}' (placeholder, not a learning component).")
                continue
            meta = read_json(sdir / "metadata.json") or {}
            diagram_type = ""
            if isinstance(meta, dict):
                diagram_type = str(meta.get("diagram_type", "")).lower()
            is_infographic = (sdir / "data.json").exists() or "overlay" in diagram_type
            components.append({
                "id": f"sims/{sdir.name}",
                "type": "interactive-infographic" if is_infographic else "microsim",
                "path": str(sdir.relative_to(book)),
                "title": title,
                "has_metadata_json": (sdir / "metadata.json").exists(),
            })

    # ---- static posters -------------------------------------------------
    poster_root = docs / "posters"
    if poster_root.is_dir():
        for pdir in sorted(p for p in poster_root.iterdir() if p.is_dir()):
            components.append({
                "id": f"posters/{pdir.name}", "type": "static-figure",
                "path": str(pdir.relative_to(book)), "title": pdir.name,
            })

    # ---- figures referenced from chapter markdown ----------------------
    seen_imgs: set[str] = set()
    if chap_root.is_dir():
        for md in sorted(chap_root.rglob("*.md")):
            text = strip_code_fences(read_text(md))
            refs = re.findall(r"!\[[^\]]*\]\(\s*<?([^)\s>]+)", text)
            refs += re.findall(r"<img[^>]+src=[\"']([^\"']+)[\"']", text, flags=re.I)
            for ref in refs:
                if re.match(r"^[a-z]+://", ref) or ref.startswith(("data:", "#")):
                    continue
                ref = ref.split("#")[0].split("?")[0]
                if not ref.lower().endswith(IMAGE_EXT):
                    continue
                if len(ref) > 400:
                    continue
                target = safe_resolve(md.parent / ref) if not ref.startswith("/") else safe_resolve(docs / ref.lstrip("/"))
                if target is None:
                    continue
                try:
                    rel = target.relative_to(docs.resolve())
                except ValueError:
                    continue
                relp = rel.as_posix()
                if not safe_exists(target) or relp in seen_imgs:
                    continue
                if relp.startswith(("sims/", "posters/")):
                    continue  # belongs to a sim or poster component
                seen_imgs.add(relp)
                components.append({
                    "id": f"figure:{relp}", "type": "static-figure",
                    "path": f"docs/{relp}", "title": Path(relp).name,
                    "referenced_from": str(md.relative_to(book)),
                })

    # ---- FAQ pairs ------------------------------------------------------
    faq = docs / "faq.md"
    faq_pairs = 0
    if faq.exists():
        text = strip_code_fences(read_text(faq))
        parts = re.split(r"^###\s+(.+?)\s*$", text, flags=re.M)
        used: dict[str, int] = {}
        for i in range(1, len(parts) - 1, 2):
            q = parts[i].strip()
            a = parts[i + 1]
            a = re.split(r"^##\s", a, maxsplit=1, flags=re.M)[0].strip()
            base = slug(q)
            used[base] = used.get(base, 0) + 1
            cid = f"faq#{base}" + (f"-{used[base]}" if used[base] > 1 else "")
            components.append({
                "id": cid, "type": "faq-pair", "path": "docs/faq.md",
                "title": q, "question": q, "answer_words": word_count(a),
                "answer_text": a[:4000],
            })
            faq_pairs += 1

    # ---- glossary -------------------------------------------------------
    gloss = docs / "glossary.md"
    if gloss.exists():
        gtext = strip_code_fences(read_text(gloss))
        terms = re.findall(r"^#{3,4}\s+\S", gtext, flags=re.M)
        components.append({
            "id": "glossary", "type": "glossary", "path": "docs/glossary.md",
            "title": "Glossary", "term_count": len(terms),
        })

    counts: dict[str, int] = {}
    for c in components:
        counts[c["type"]] = counts.get(c["type"], 0) + 1

    return {
        "components": components,
        "counts_by_type": counts,
        "chapters": chapters,
        "chapter_weight_scale": scale,
        "faq_pair_count": faq_pairs,
        "not_detected_types": [
            {"type": "worked-example", "reason": "no packaging convention; needs LLM enumeration with human confirmation"},
            {"type": "instructor-material", "reason": "no packaging convention; needs LLM enumeration with human confirmation"},
            {"type": "quiz-for-one-microsim", "reason": "no file convention (spec Section 4); found only through RP7 links"},
        ],
        "notes": notes,
    }
