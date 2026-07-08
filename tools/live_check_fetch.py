#!/usr/bin/env python3
"""Fetch the live-check target pages from an environment with journal egress.

The repo's build sandboxes sit behind an egress policy that denies CONNECT to
most journal/publisher domains, so unresolved source-map facts cannot be
re-verified from there. GitHub Actions runners CAN reach those domains, so the
`live-check` workflow runs this script and the fetched page text lands in the
job log for a maintainer (or agent reading the log via API) to act on.

Deliberately a *report*: it fetches, extracts readable text, and prints. It
never edits files, never fails the build on a blocked page, and is only ever
run on manual dispatch. Source-map updates stay a human/agent editing step.

Usage:
  python3 tools/live_check_fetch.py                       # default list
  python3 tools/live_check_fetch.py --list PATH           # custom list
  python3 tools/live_check_fetch.py --max-chars 4000      # more context
"""

from __future__ import annotations

import argparse
import html
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LIST = ROOT / ".maintenance" / "LIVE-CHECK-URLS.txt"

UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
)

TAG_RE = re.compile(r"<(script|style|noscript)[^>]*>.*?</\1>", re.S | re.I)
HTML_RE = re.compile(r"<[^>]+>")
WS_RE = re.compile(r"[ \t]+")
NL_RE = re.compile(r"\n{3,}")


def to_text(raw: bytes) -> str:
    body = raw.decode("utf-8", errors="replace")
    body = TAG_RE.sub(" ", body)
    body = HTML_RE.sub("\n", body)
    body = html.unescape(body)
    body = WS_RE.sub(" ", body)
    lines = [ln.strip() for ln in body.splitlines()]
    return NL_RE.sub("\n\n", "\n".join(ln for ln in lines if ln))


def fetch(url: str, timeout: int) -> tuple[int, str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en,zh;q=0.8"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.status, to_text(resp.read())


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--list", default=str(DEFAULT_LIST), help="target list file")
    ap.add_argument("--timeout", type=int, default=30)
    ap.add_argument("--max-chars", type=int, default=6000, help="text budget per page")
    args = ap.parse_args()

    targets: list[tuple[str, str]] = []
    for line in Path(args.list).read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        url, _, hint = (part.strip() for part in line.partition("|"))
        targets.append((url, hint))

    blocked = 0
    for url, hint in targets:
        print(f"\n{'=' * 78}\nURL: {url}\nLOOK FOR: {hint or '(unspecified)'}\n{'-' * 78}")
        try:
            status, text = fetch(url, args.timeout)
        except Exception as exc:  # noqa: BLE001 — report-only tool
            blocked += 1
            print(f"FETCH FAILED: {exc}")
            continue
        print(f"HTTP {status} · {len(text)} chars of extracted text")
        print(text[: args.max_chars])
        if len(text) > args.max_chars:
            print(f"... [truncated at {args.max_chars} chars]")

    print(f"\n{'=' * 78}\nDone: {len(targets)} targets, {blocked} failed/blocked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
