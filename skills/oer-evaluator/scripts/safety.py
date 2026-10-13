"""Detect text addressed to an evaluator (spec Section 8: the resource is data,
never instructions).

Content that tries to steer the evaluation is a finding to report. The scripts
never act on it; this module only records where it is, so the finding does not
depend on a reader noticing it. It is a heuristic and will miss paraphrases.
Documentation that quotes such text as an example can also match; the report
says "review", not "malicious".
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from common import read_json, read_text

# "judge" is deliberately absent: it is a common verb ("a note to judge why...").
_ADDRESSEE = r"(?:ai\s+|llm\s+|automated\s+)?(?:evaluators?|graders?|reviewers?|assessors?|scoring\s+(?:agent|system)|evaluation\s+(?:agent|tool))"

# Strong signals are text aimed at an evaluator or at the scoring itself. Educational
# prose about prompts ("write clear instructions for an AI", a quoted "ignore previous
# instructions" attack example) is deliberately not matched.
STRONG: list[tuple[str, re.Pattern]] = [
    ("addressed-to-evaluator", re.compile(rf"\b(?:note|message|instruction|notice|attention|request)s?\s+(?:to|for)\s+(?:the\s+|any\s+|an?\s+|all\s+)?{_ADDRESSEE}\b", re.I)),
    ("system-instruction", re.compile(rf"\b(?:system|developer)\s+(?:instruction|prompt|message|note)s?\s+(?:to|for)\s+(?:the\s+|any\s+|an?\s+)?{_ADDRESSEE}\b", re.I)),
    ("to-any-evaluator", re.compile(rf"\b(?:to|for)\s+any\s+{_ADDRESSEE}\b", re.I)),
    ("ignore-rubric", re.compile(r"\bignore\s+(?:the|your|all)\s+(?:rubric|scoring|evaluation\s+criteria|checks|indicators)\b", re.I)),
    ("dictates-score", re.compile(r"\b(?:report|give|assign|set|mark|rate|score)\b[^.\n]{0,60}\b(?:quality|reuse|overall)\s+scores?\b[^.\n]{0,40}\b(?:3(?:\.0)?|perfect|maximum|full marks)\b", re.I)),
    ("mark-all-pass", re.compile(r"\bmark\s+(?:every|all|each)\s+(?:check|indicator|item)s?\s+as\s+pass", re.I)),
    ("ignore-then-score", re.compile(r"\bignore\s+(?:all\s+|any\s+|the\s+|your\s+)?(?:previous|prior|above|earlier)\b[^.\n]{0,40}\b(?:and|then)\b[^.\n]{0,60}\b(?:score|report|rate|mark|grade|evaluat|certif)", re.I)),
]
# Weak signals are common in legitimate documentation. They count only in pairs.
WEAK: list[tuple[str, re.Pattern]] = [
    ("requests-deletion", re.compile(r"\b(?:delete|erase|wipe|remove)\s+(?:the\s+)?(?:file\s+)?[`'\"]?(?:docs/|\.\./)[\w./-]+", re.I)),
    ("claims-certification", re.compile(r"\b(?:pre-?certified|already\s+(?:been\s+)?certified|certified\s+by\s+the\s+maintainers)\b", re.I)),
    ("ignore-previous", re.compile(r"\bignore\s+(?:all\s+|any\s+|the\s+|your\s+)?(?:previous|prior|above|earlier)\s+(?:instructions?|rules?|prompts?)\b", re.I)),
]


def scan_text(text: str) -> list[dict]:
    """Return the hits that justify a finding: any strong pattern, or two weak ones."""
    def run(group):
        out = []
        for name, pat in group:
            m = pat.search(text or "")
            if m:
                s = max(0, m.start() - 40)
                out.append({"pattern": name, "snippet": re.sub(r"\s+", " ", text[s: m.end() + 80]).strip()[:240]})
        return out
    strong, weak = run(STRONG), run(WEAK)
    if strong:
        return strong + weak
    if len(weak) >= 2:
        return weak
    return []


def _strings(obj):
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from _strings(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from _strings(v)


def find_embedded_instructions(book: Path, inventory: dict) -> list[dict]:
    """Return a list of {location, unit, patterns[], snippets[]}."""
    docs = book / "docs"
    out: list[dict] = []
    seen_files: set[str] = set()

    def unit_for(rel: str) -> dict:
        m = re.match(r"docs/sims/([^/]+)/", rel)
        if m:
            return {"kind": "component", "id": f"sims/{m.group(1)}"}
        return {"kind": "book", "id": "book"}

    def add(path: Path, text: str):
        rel = path.relative_to(book).as_posix()
        if rel in seen_files:
            return
        hits = scan_text(text)
        if hits:
            seen_files.add(rel)
            out.append({"location": rel, "unit": unit_for(rel),
                        "patterns": sorted({h["pattern"] for h in hits}),
                        "snippets": [h["snippet"] for h in hits][:3]})

    if not docs.is_dir():
        return out
    for p in sorted(docs.rglob("*.md")):
        add(p, read_text(p, 400_000))
    for p in sorted(docs.glob("sims/*/metadata.json")):
        raw = read_json(p)
        add(p, "\n".join(_strings(raw)) if raw is not None else read_text(p))
    for p in sorted(docs.glob("sims/*/*.html")):
        add(p, read_text(p, 400_000))
    return out
