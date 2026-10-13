"""Optional network helpers. Only imported when --check-external is passed."""
from __future__ import annotations
import urllib.request


def head_ok(url: str, timeout: float = 8.0) -> bool:
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, method=method, headers={"User-Agent": "oer-evaluator/0.1"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return 200 <= r.status < 400
        except Exception:
            continue
    return False
