#!/usr/bin/env python3
"""Machine-readable submission rules: parse, validate, and compile them.

A pack's ``resources/official-source-map.md`` is the single source of truth for a
venue's volatile facts. Until now those facts were prose only, so nothing could check a
manuscript against them deterministically. A source map may now also carry one fenced
block of the form::

    ```json
    {
      "schema": "ajs-preflight-rules/1",
      "venue": "The Journal of Finance",
      "verified": "2026-11-23",
      "rules": {
        "main_text_pages_max": {"value": 60, "source": "https://afajof.org/submissions/",
                                "note": "Internet Appendix not counted"},
        "review_mode": {"value": "single-blind", "source": "https://..."}
      }
    }
    ```

A numeric limit the venue words as guidance ("about 300 characters", "preferably no
more than") carries ``"soft": true``; preflight then reports a breach as FLAG, not FAIL.

The block is a *compiled view of the prose*, never a second copy that can drift on its
own, and ``--check`` enforces that in three ways:

1. every numeric value in the block appears as a number in the surrounding prose;
2. every ``source`` URL in the block is also cited in the surrounding prose;
3. ``verified`` equals the date the freshness parser reads from the prose without the
   block — so a block cannot claim a re-check the map does not record.

``--write`` compiles every block into ``shared-resources/submission-readiness/
venue-rules.json``, which ``tools/preflight.py`` reads (and which is vendored into the
Research Toolkit pack so preflight works from a plain plugin install).

Stdlib only. ``python3 tools/venue_rules.py --check`` is part of ``run_checks.py``.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import re
import sys
from pathlib import Path

from venue_lib import ROOT, read

OUT = ROOT / "shared-resources" / "submission-readiness" / "venue-rules.json"
INDEX = ROOT / "shared-resources" / "journal-selection" / "venue-index.tsv"
SCHEMA = "ajs-preflight-rules/1"

# Controlled vocabulary. A rule key outside this set is a typo until proven otherwise;
# preflight only knows how to test these.
NUMERIC_KEYS = {
    "main_text_pages_max",      # pages, excluding references/appendix unless note says otherwise
    "main_text_words_max",      # words in the main text
    "total_words_max",          # words including everything the venue counts
    "abstract_words_max",       # words (English) in the abstract
    "abstract_chars_max",       # characters (CJK venues state abstract length in 字)
    "main_text_chars_max",      # characters (CJK venues)
    "keywords_min",
    "keywords_max",
    "references_max",
    "exhibits_max",             # tables + figures in the main text
    "title_words_max",
    "title_chars_max",
    "words_per_exhibit",        # each main-text exhibit lowers the word cap by this much (AEA)
}
ENUM_KEYS = {
    "review_mode": {"double-blind", "single-blind", "open", "triple-blind"},
    "cover_letter": {"required", "optional", "discouraged"},
    "abstract_format": {"structured", "unstructured", "either"},
    "significance_stars": {"prohibited", "discouraged", "allowed"},
}
BOOL_KEYS = {
    "jel_codes_required",
    "keywords_required",
    "anonymized_supplement_required",
    "page_limit_includes_references",
}
TEXT_KEYS = {
    "submission_fee", "apc", "template", "reference_style", "portal",
    "data_code_policy", "language", "file_format", "supplement_policy",
    "preprint_policy", "llm_policy",
}
# required_statements: must be IN the manuscript at first submission.
# separate_upload_statements: required, but uploaded as their own file or form field —
#   putting them in the manuscript can break anonymity, so preflight only reminds.
# conditional_statements: required only if a condition holds (e.g. AI was used).
LIST_KEYS = {"required_statements", "separate_upload_statements", "conditional_statements"}
STATEMENTS = {
    "data_availability", "code_availability", "conflict_of_interest", "funding",
    "ethics_approval", "informed_consent", "ai_use_disclosure", "author_contributions",
    "trial_registration", "reporting_guideline", "limitations", "broader_impact",
    "reproducibility_checklist", "significance_statement", "acknowledgments",
    "disclosure_statement", "jel_codes", "keywords", "structured_abstract",
    "highlights", "graphical_abstract", "key_points", "lay_summary",
}
ALL_KEYS = NUMERIC_KEYS | set(ENUM_KEYS) | BOOL_KEYS | TEXT_KEYS | LIST_KEYS

FENCE = re.compile(r"```json[ \t]*\n(.*?)\n```", re.S)
URL = re.compile(r"https?://[^\s|)>\]`\"'<]+")
ISO = re.compile(r"^20[0-9]{2}-[0-9]{2}-[0-9]{2}$")


def find_block(text: str) -> tuple[dict | None, str, str | None]:
    """(rules, prose_without_block, error). ``rules`` is None when the map has no block."""
    for m in FENCE.finditer(text):
        body = m.group(1)
        if SCHEMA not in body:
            continue
        prose = text[: m.start()] + text[m.end():]
        try:
            return json.loads(body), prose, None
        except json.JSONDecodeError as exc:
            return None, prose, f"rules block is not valid JSON: {exc}"
    return None, text, None


def _norm_url(u: str) -> str:
    return u.rstrip(".,;:*_").rstrip("/").lower()


def _numbers_in(text: str) -> set[str]:
    # "3,000" and "3000" are the same limit; strip thousands separators before matching.
    return {n.replace(",", "") for n in re.findall(r"\d[\d,]*", text)}


def validate(pack: str, block: dict, prose: str, today: dt.date) -> list[str]:
    from freshness_audit import last_verified  # local import: freshness imports venue_lib too

    errs: list[str] = []
    if block.get("schema") != SCHEMA:
        errs.append(f"schema must be {SCHEMA!r}")
    if not isinstance(block.get("venue"), str) or not block["venue"].strip():
        errs.append("missing 'venue' name")
    verified = block.get("verified", "")
    if not (isinstance(verified, str) and ISO.match(verified)):
        errs.append("'verified' must be an ISO date")
    else:
        prose_date, _ = last_verified(prose, today)
        if prose_date is None or prose_date.isoformat() != verified:
            errs.append(
                f"'verified' is {verified} but the prose records "
                f"{prose_date.isoformat() if prose_date else 'no date'} — re-date the prose "
                "(e.g. 're-verified YYYY-MM-DD') in the same edit")
    rules = block.get("rules")
    if not isinstance(rules, dict) or not rules:
        errs.append("'rules' must be a non-empty object")
        return errs
    prose_urls = {_norm_url(u) for u in URL.findall(prose)}
    prose_numbers = _numbers_in(prose)
    for key, rule in rules.items():
        where = f"rules.{key}"
        if key not in ALL_KEYS:
            errs.append(f"{where}: unknown key (allowed: {', '.join(sorted(ALL_KEYS))})")
            continue
        if not isinstance(rule, dict) or "value" not in rule:
            errs.append(f"{where}: must be an object with 'value'")
            continue
        value, source = rule["value"], rule.get("source")
        if "soft" in rule and (not isinstance(rule["soft"], bool) or key not in NUMERIC_KEYS):
            errs.append(f"{where}: 'soft' must be true/false and only on a numeric limit")
        if value is None:
            continue  # explicitly unknown: allowed, preflight reports UNKNOWN
        if not (isinstance(source, str) and source.startswith("http")):
            errs.append(f"{where}: a non-null value needs an http(s) 'source'")
        elif _norm_url(source) not in prose_urls:
            errs.append(f"{where}: source {source} is not cited in the source map's prose")
        if key in NUMERIC_KEYS:
            if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
                errs.append(f"{where}: value must be a positive integer")
            elif str(value) not in prose_numbers:
                errs.append(f"{where}: {value} does not appear in the prose — the block "
                            "may only restate what the map already says")
        elif key in ENUM_KEYS:
            if value not in ENUM_KEYS[key]:
                errs.append(f"{where}: {value!r} not in {sorted(ENUM_KEYS[key])}")
        elif key in BOOL_KEYS:
            if not isinstance(value, bool):
                errs.append(f"{where}: value must be true/false")
        elif key in LIST_KEYS:
            if not isinstance(value, list) or not all(isinstance(v, str) for v in value):
                errs.append(f"{where}: value must be a list of strings")
            else:
                bad = [v for v in value if v not in STATEMENTS]
                if bad:
                    errs.append(f"{where}: unknown statement(s) {bad} "
                                f"(allowed: {', '.join(sorted(STATEMENTS))})")
        elif key in TEXT_KEYS:
            if not isinstance(value, str) or not value.strip():
                errs.append(f"{where}: value must be a non-empty string")
    return errs


def _aliases() -> dict[str, list[str]]:
    """pack_dir -> venue_id/display names from the venue index, for name lookup."""
    out: dict[str, list[str]] = {}
    if not INDEX.exists():
        return out
    with INDEX.open(encoding="utf-8") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            if row.get("coverage") == "depth" and row.get("pack_dir"):
                out.setdefault(row["pack_dir"], []).extend(
                    [row["venue_id"], row["display_name"]])
    return out


def collect(today: dt.date) -> tuple[dict, list[str]]:
    compiled: dict[str, dict] = {}
    problems: list[str] = []
    aliases = _aliases()
    for source_map in sorted(ROOT.glob("*/resources/official-source-map.md")):
        pack = source_map.parent.parent
        block, prose, err = find_block(read(source_map))
        if err:
            problems.append(f"{pack.name}: {err}")
            continue
        if block is None:
            continue
        errs = validate(pack.name, block, prose, today)
        problems.extend(f"{pack.name}: {e}" for e in errs)
        if errs:
            continue
        plugin = pack / ".claude-plugin" / "plugin.json"
        plugin_name = json.loads(read(plugin)).get("name", "") if plugin.exists() else ""
        names = [block["venue"], pack.name, plugin_name, *aliases.get(pack.name, [])]
        seen: list[str] = []
        for n in names:
            if n and n not in seen:
                seen.append(n)
        compiled[pack.name] = {
            "venue": block["venue"],
            "aliases": seen,
            "verified": block["verified"],
            "source_map": f"{pack.name}/resources/official-source-map.md",
            "rules": block["rules"],
        }
    return compiled, problems


def render(compiled: dict) -> str:
    payload = {
        "schema": "ajs-venue-rules/1",
        "generated_by": "python3 tools/venue_rules.py --write",
        "note": ("Compiled from the JSON rules block in each pack's official-source-map.md. "
                 "Do not edit by hand; edit the source map and regenerate."),
        "venues": compiled,
    }
    return json.dumps(payload, ensure_ascii=False, indent=1, sort_keys=True) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--write", action="store_true", help="regenerate venue-rules.json")
    ap.add_argument("--check", action="store_true",
                    help="exit 1 if any block is invalid or venue-rules.json is stale")
    ap.add_argument("--pack", help="validate one pack directory only (for authoring)")
    args = ap.parse_args()
    today = dt.date.today()

    if args.pack:
        path = ROOT / args.pack / "resources" / "official-source-map.md"
        block, prose, err = find_block(read(path))
        if err or block is None:
            print(err or f"{args.pack}: no rules block found", file=sys.stderr)
            return 1
        errs = validate(args.pack, block, prose, today)
        for e in errs:
            print(f"{args.pack}: {e}", file=sys.stderr)
        if not errs:
            print(f"OK: {args.pack} rules block valid ({len(block['rules'])} rules)")
        return 1 if errs else 0

    compiled, problems = collect(today)
    for p in problems:
        print(f"ERROR: {p}", file=sys.stderr)
    text = render(compiled)
    if args.write:
        OUT.write_text(text, encoding="utf-8")
        print(f"wrote {OUT.relative_to(ROOT)} ({len(compiled)} venues)")
    if args.check:
        current = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if current != text:
            print("ERROR: venue-rules.json is stale; run python3 tools/venue_rules.py --write",
                  file=sys.stderr)
            return 1
        if not problems:
            print(f"OK: venue rules current ({len(compiled)} venues with a rules block)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
