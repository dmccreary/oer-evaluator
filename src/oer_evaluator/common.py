"""Shared helpers for the oer-evaluator scripts.

Standard library only, so every deterministic step runs anywhere. The one
optional heavy dependency (sentence-transformers) is confined to findability.py.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

SPEC_VERSION = "0.4"
SKILL_VERSION = "0.1.0"
REPORT_SCHEMA = "oer-evaluator-report/v1"

# Scaffold text that means "this field was never filled in".
PLACEHOLDER_PATTERNS = [
    r"describe the intended reader",
    r"list the assumed prior knowledge",
    r"^\s*\.\.\.\s*$",
    r"lorem ipsum",
    r"a title under",
    r"\btodo\b",
    r"your (text|description|title) here",
]

# Boilerplate learning-objective openings, taken from the author's
# search-microsims find-duplicate-microsims.py (quality_score).
BOILERPLATE_OBJECTIVE_PREFIXES = (
    "understand the key concepts",
    "explore ",
    "apply knowledge of",
    "test understanding of",
    # a fourth line of the same auto-generated template, seen in real books
    "experiment with parameters",
)

# Placeholder sim ids copied into every book by design (same list as
# search-microsims find-duplicate-microsims.py).
PLACEHOLDER_SIM_IDS = ("template", "sample-arch", "sim-template")
PLACEHOLDER_TITLE_MARKERS = ("a title under", "template", "lorem ipsum")


def safe_resolve(path: Path) -> Path | None:
    """Path.resolve() that returns None for paths the OS rejects (for example a
    very long string that was parsed as a link target)."""
    try:
        return Path(path).resolve()
    except (OSError, ValueError, RuntimeError):
        return None


def safe_exists(path: Path) -> bool:
    try:
        return Path(path).exists()
    except (OSError, ValueError):
        return False


def read_text(path: Path, limit: int = 2_000_000) -> str:
    try:
        return Path(path).read_text(encoding="utf-8", errors="replace")[:limit]
    except OSError:
        return ""


def read_json(path: Path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8", errors="replace"))
    except (OSError, ValueError):
        return None


def write_json(path: Path, obj) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def slug(s: str) -> str:
    s = re.sub(r"[^A-Za-z0-9]+", "-", s.strip().lower()).strip("-")
    return s[:80] or "item"


def safe_id(component_id: str) -> str:
    """Filesystem-safe form of a component id."""
    return re.sub(r"[^A-Za-z0-9._-]+", "__", component_id).strip("_")


def is_placeholder_text(text: str) -> bool:
    t = (text or "").strip()
    if not t:
        return True
    return any(re.search(p, t, re.I | re.M) for p in PLACEHOLDER_PATTERNS)


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Parse a leading '---' YAML block as flat key: value pairs (no YAML dep)."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    block = text[3:end].strip("\n")
    body = text[end + 4:].lstrip("\n")
    fm: dict = {}
    for line in block.split("\n"):
        m = re.match(r"^([A-Za-z0-9_.\-]+):\s*(.*)$", line)
        if m:
            fm[m.group(1)] = m.group(2).strip().strip("'\"")
    return fm, body


def strip_code_fences(text: str) -> str:
    """Remove fenced code blocks so examples inside them are not parsed."""
    return re.sub(r"^(```|~~~).*?^\1[^\n]*$", "", text, flags=re.S | re.M)


def sections(text: str, level_pattern: str = r"#{2,3}") -> dict[str, str]:
    """Map lowercased heading text -> body text up to the next heading."""
    out: dict[str, str] = {}
    parts = re.split(rf"^({level_pattern})\s+(.+?)\s*$", text, flags=re.M)
    # parts: [pre, hashes, title, body, hashes, title, body, ...]
    for i in range(1, len(parts) - 2, 3):
        out[parts[i + 1].strip().lower()] = parts[i + 2]
    return out


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", strip_code_fences(text)))


def mkdocs_scalar(mkdocs_text: str, key: str) -> str | None:
    """Top-level scalar from mkdocs.yml without a YAML parser (mkdocs.yml can
    contain python tags that break safe_load)."""
    m = re.search(rf"^{re.escape(key)}:\s*(.+?)\s*$", mkdocs_text, flags=re.M)
    if not m:
        return None
    v = m.group(1).strip()
    if v[:1] in "'\"" and v[-1:] == v[:1]:
        v = v[1:-1]
    return v or None


def result(status: str, value=None, evidence=None, method: str = "static", note: str | None = None,
           extra: dict | None = None) -> dict:
    """One check result. status: pass | fail | ISE | N/A | recorded."""
    r = {
        "status": status,
        "value": value,
        "evidence": evidence or [],
        "method": method,
        "note": note,
    }
    if extra:
        r["extra"] = extra
    return r


def ev(location: str, detail: str = "", quote: str | None = None) -> dict:
    d = {"location": location, "detail": detail}
    if quote:
        d["quote"] = quote[:240]
    return d
