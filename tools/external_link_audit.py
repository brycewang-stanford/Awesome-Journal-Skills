#!/usr/bin/env python3
"""Liveness audit for the external URLs cited across first-party markdown.

The repository audit (``tools/audit_repo.py``) already guarantees that every
*local* relative link resolves on disk. This companion tool covers the other
half of link hygiene that a curated directory cares about: the *external* URLs
— official journal homepages, publisher pages, submission portals — must not
404. A dead "Official" link in an awesome-list is a real, user-facing defect.

This tool is deliberately a *report*, not a CI gate: it needs the network, and
many academic publishers answer bots with 403/429 (a block, not a dead page),
so a strict pass/fail would be noise. Classification:

  DEAD        final status 404 or 410 — actionable, the page is gone.
  REDIRECT    permanent 3xx whose final URL differs materially — review and
              repoint to the canonical URL.
  BLOCKED     401/403/429 — the host refuses bots; almost never a real defect.
  UNREACHABLE 000/timeout/5xx — transient or network-side; re-run before acting.
  OK          2xx.

Infrastructure hosts (GitHub, shields.io badges, the project's own site) are
skipped by default; they are stable and dominate the URL list.

Usage:
  python3 tools/external_link_audit.py                 # check all, show actionable
  python3 tools/external_link_audit.py --include-infra # also check github/shields
  python3 tools/external_link_audit.py --only DEAD     # filter classes
  python3 tools/external_link_audit.py --json
  python3 tools/external_link_audit.py --refresh       # ignore the on-disk cache

Results are cached under tools/.cache/external_links.json (gitignored) so that
re-runs only re-check URLs whose verdict was inconclusive (BLOCKED/UNREACHABLE)
or that are new since the last run.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CACHE_PATH = ROOT / "tools" / ".cache" / "external_links.json"
SUMMARY_CONTRACT = "external-link-cache-summary-v2"

IMPORTED_ROOTS = {
    "AER-Skills",
    "AER-skills",
    "Nature-Skills",
    "nature-skills",
    "nature-paper-skills",
    "claude-scholar",
    "codex-claude-academic-skills",
}

# Stable infrastructure hosts: not journal/publisher targets, and they dominate
# the URL list (badges, repo links). Skipped unless --include-infra is passed.
INFRA_HOSTS = {
    "github.com",
    "raw.githubusercontent.com",
    "img.shields.io",
    "awesome.re",
    "copaper.ai",
    "www.copaper.ai",
    "shields.io",
}

# Stop at whitespace, markdown/HTML delimiters, backticks, emphasis markers, and
# any non-ASCII char (CJK text or full-width punctuation that abuts a URL in the
# Chinese source maps marks where the URL actually ends). NOTE: a bare ``)`` is
# *not* a hard stop — Wikipedia disambiguation URLs such as ``Mind_(journal)``
# legitimately contain it; trailing parens are reconciled by balance in
# ``normalize``. Opening ``[`` remains a hard stop so adjacent Markdown links
# such as ``...package=meta)/[metafor](...)`` do not merge into one URL. Known
# limitation: URLs whose path contains literal CJK (e.g. some baike.baidu.com
# /item/ links) are truncated at the first CJK char.
URL_RE = re.compile(r"https?://[\x21-\x7e]+")
_STOP_CHARS = set(" \t\n<>\"'[]}|`*")
TRAILING = ".,;:!?*`"


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def is_first_party(path: Path) -> bool:
    parts = path.relative_to(ROOT).parts
    # ``.maintenance/`` holds internal agent working notes, not published
    # content; dead links there are not user-facing defects.
    if not parts or parts[0] in IMPORTED_ROOTS or parts[0] == ".maintenance":
        return False
    return ".git" not in parts


def first_party_markdown() -> list[Path]:
    return sorted(p for p in ROOT.rglob("*.md") if is_first_party(p))


def host_of(url: str) -> str:
    m = re.match(r"https?://([^/]+)", url)
    return m.group(1).lower() if m else ""


def normalize(url: str) -> str:
    url = url.strip()
    # Cut at the first delimiter that cannot be part of a real URL here
    # (backtick, emphasis marker, closing bracket, CJK punctuation).
    for i, ch in enumerate(url):
        if ch in _STOP_CHARS:
            url = url[:i]
            break
    url = url.rstrip(TRAILING)
    # Adjacent Markdown links sometimes leave ``)/`` after the real URL once
    # the following ``[`` is cut away: ``[meta](...=meta)/[metafor](...)``.
    if url.endswith(")/") and url.count("(") < url.count(")"):
        url = url[:-1]
    # Strip only *unbalanced* trailing parens/brackets (markdown link wrappers),
    # keeping balanced ones that belong to the URL (Wikipedia disambiguation).
    while url and url[-1] in ")]}>":
        closer = url[-1]
        opener = {")": "(", "]": "[", "}": "{", ">": "<"}[closer]
        if url.count(opener) >= url.count(closer):
            break
        url = url[:-1]
    return url


def collect_urls(include_infra: bool) -> dict[str, list[str]]:
    """Map each external URL to the sorted files that cite it."""
    refs: dict[str, set[str]] = defaultdict(set)
    for path in first_party_markdown():
        text = path.read_text(encoding="utf-8", errors="replace")
        for raw in URL_RE.findall(text):
            url = normalize(raw)
            if not url:
                continue
            if not include_infra and host_of(url) in INFRA_HOSTS:
                continue
            refs[url].add(rel(path))
    return {url: sorted(files) for url, files in sorted(refs.items())}


def curl_status(url: str, timeout: int) -> tuple[str, str]:
    """Return (http_code, final_url). http_code '000' means no response."""
    try:
        out = subprocess.run(
            [
                "curl", "-s", "-o", "/dev/null",
                "-w", "%{http_code} %{url_effective}",
                "-L", "--max-time", str(timeout),
                "-A", "Mozilla/5.0 (compatible; AJS-link-audit/1.0)",
                url,
            ],
            capture_output=True,
            text=True,
            timeout=timeout + 5,
        )
    except Exception:
        return "000", url
    parts = out.stdout.strip().split(" ", 1)
    code = parts[0] if parts else "000"
    final = parts[1] if len(parts) > 1 else url
    return code, final


def classify(code: str, url: str, final: str) -> str:
    if code in {"404", "410"}:
        return "DEAD"
    if code.startswith("2"):
        # Materially different final host => worth repointing.
        if host_of(final) and host_of(final) != host_of(url):
            return "REDIRECT"
        return "OK"
    if code in {"401", "403", "429"}:
        return "BLOCKED"
    return "UNREACHABLE"


def load_cache() -> dict:
    if CACHE_PATH.exists():
        try:
            return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def save_cache(cache: dict) -> None:
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    CACHE_PATH.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")


def cache_summary(refs: dict[str, list[str]], include_infra: bool) -> dict:
    """Summarize the on-disk verdict cache without making network requests."""
    cache = load_cache()
    classes = ("OK", "DEAD", "REDIRECT", "BLOCKED", "UNREACHABLE", "UNCHECKED")
    counts = {cls: 0 for cls in classes}
    checked = 0
    current_cache_entries = 0
    for url in refs:
        if url in cache:
            current_cache_entries += 1
        cached_class = str(cache.get(url, {}).get("class", ""))
        if cached_class in counts and cached_class != "UNCHECKED":
            counts[cached_class] += 1
            checked += 1
        else:
            counts["UNCHECKED"] += 1
    actionable = counts["DEAD"] + counts["REDIRECT"]
    inconclusive = counts["BLOCKED"] + counts["UNREACHABLE"]
    if not CACHE_PATH.exists():
        status = "no-cache"
    elif actionable:
        status = "actionable-review"
    elif inconclusive or counts["UNCHECKED"]:
        status = "advisory-review"
    else:
        status = "cached-ok"
    summary = {
        "contract": SUMMARY_CONTRACT,
        "status": status,
        "include_infra": include_infra,
        "cache_path": rel(CACHE_PATH),
        "cache_present": CACHE_PATH.exists(),
        "cache_entry_count": len(cache),
        "current_cache_entry_count": current_cache_entries,
        "orphaned_cache_entry_count": len(set(cache) - set(refs)),
        "url_count": len(refs),
        "checked_count": checked,
        "unchecked_count": counts["UNCHECKED"],
        "actionable_count": actionable,
        "inconclusive_count": inconclusive,
        "counts": counts,
    }
    summary["fingerprint"] = json.dumps(
        {
            "contract": summary["contract"],
            "status": summary["status"],
            "include_infra": summary["include_infra"],
            "cache_entry_count": summary["cache_entry_count"],
            "current_cache_entry_count": summary["current_cache_entry_count"],
            "orphaned_cache_entry_count": summary["orphaned_cache_entry_count"],
            "url_count": summary["url_count"],
            "checked_count": summary["checked_count"],
            "unchecked_count": summary["unchecked_count"],
            "actionable_count": summary["actionable_count"],
            "inconclusive_count": summary["inconclusive_count"],
            "counts": summary["counts"],
        },
        ensure_ascii=False,
        sort_keys=True,
    )
    summary["fingerprint"] = hashlib.sha256(summary["fingerprint"].encode("utf-8")).hexdigest()[:12]
    return summary


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--include-infra", action="store_true", help="also check github/shields/etc.")
    ap.add_argument("--only", action="append", default=[], help="only show these classes (DEAD/REDIRECT/BLOCKED/UNREACHABLE/OK)")
    ap.add_argument("--timeout", type=int, default=20)
    ap.add_argument("--workers", type=int, default=12)
    ap.add_argument("--limit", type=int, default=0, help="check at most N urls (0 = all)")
    ap.add_argument("--refresh", action="store_true", help="ignore cached verdicts")
    ap.add_argument("--cache-summary", action="store_true", help="summarize cached verdicts without network requests")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)

    refs = collect_urls(args.include_infra)
    urls = list(refs)
    if args.limit:
        urls = urls[: args.limit]
        refs = {url: refs[url] for url in urls}

    if args.cache_summary:
        summary = cache_summary(refs, args.include_infra)
        if args.json:
            print(json.dumps(summary, ensure_ascii=False, indent=2))
        else:
            counts = summary["counts"]
            print(f"External-link cache summary — {summary['url_count']} unique URL(s)")
            print(
                "  "
                + " · ".join(
                    f"{cls}={counts.get(cls, 0)}"
                    for cls in ("OK", "DEAD", "REDIRECT", "BLOCKED", "UNREACHABLE", "UNCHECKED")
                )
            )
            print(
                f"Coverage: {summary['current_cache_entry_count']}/{summary['url_count']} current URL(s) have cache rows; "
                f"{summary['cache_entry_count']} total cache row(s); "
                f"{summary['orphaned_cache_entry_count']} orphaned"
            )
            print(
                f"Status: {summary['status']}; cache: "
                f"{'present' if summary['cache_present'] else 'missing'}; "
                f"sha256 {summary['fingerprint']}"
            )
        return 0

    cache = {} if args.refresh else load_cache()
    # Re-use only confident verdicts; always re-check inconclusive ones.
    todo = [
        u for u in urls
        if cache.get(u, {}).get("class") not in {"OK", "DEAD", "REDIRECT"}
    ]

    def work(url: str) -> tuple[str, dict]:
        code, final = curl_status(url, args.timeout)
        return url, {"code": code, "final": final, "class": classify(code, url, final)}

    if todo:
        print(f"Checking {len(todo)} url(s) (cached: {len(urls) - len(todo)})...", file=sys.stderr)
        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            for url, verdict in pool.map(work, todo):
                cache[url] = verdict
        save_cache(cache)

    results = []
    for url in urls:
        v = cache.get(url, {"code": "000", "final": url, "class": "UNREACHABLE"})
        results.append({"url": url, **v, "files": refs[url]})

    counts: dict[str, int] = defaultdict(int)
    for r in results:
        counts[r["class"]] += 1

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return 0

    print(f"External-link audit — {len(results)} unique URL(s) across first-party markdown")
    print("  " + " · ".join(f"{cls}={counts.get(cls,0)}" for cls in ("OK", "DEAD", "REDIRECT", "BLOCKED", "UNREACHABLE")))
    show_classes = set(args.only) if args.only else {"DEAD", "REDIRECT"}
    shown = [r for r in results if r["class"] in show_classes]
    if shown:
        print(f"\nShowing {len(shown)} url(s) in classes: {', '.join(sorted(show_classes))}\n")
    for r in sorted(shown, key=lambda r: (r["class"], r["url"])):
        print(f"[{r['class']}] {r['code']}  {r['url']}")
        if r["class"] == "REDIRECT":
            print(f"      -> {r['final']}")
        for f in r["files"][:6]:
            print(f"      · {f}")
        if len(r["files"]) > 6:
            print(f"      · (+{len(r['files']) - 6} more)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
