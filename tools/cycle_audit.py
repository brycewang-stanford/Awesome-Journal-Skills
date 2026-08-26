#!/usr/bin/env python3
"""Audit whether each conference pack still describes an edition that has not yet met.

`freshness_audit.py` answers "when was this source map last re-read?". For a journal
that is the whole question: a masthead, a word cap and a submission policy belong to a
standing publication, and re-reading them is what keeps them true.

A conference is not a standing publication. Its facts belong to one **edition** —
AAAI-26, ICML 2026, CCS 2027 — and every one of them (page cap, chairs, tracks, review
phases, deadlines) is replaced wholesale when the next call goes out. So a conference
pack has a second way to be wrong that the freshness dashboard cannot see: it can be
re-read last month, report its dates accurately, and still describe a cycle that closed
before the reader arrived. That is not a hypothetical failure mode — it is what issue #3
reported about `AAAI-Skills`, whose source map was 65 days old and entirely about
AAAI-26 while the AAAI-27 cycle had already opened, run and closed its deadline.

What this reads
---------------
The edition label the source map writes for its own venue, anchored to the venue's
acronym so that "CCS 2027" is read as an edition and a stray year in a copyright line is
not. Aliases for venues that do not write their pack's directory name (`ACM-CCS-Skills`
writes "CCS") live in `venue_lib.CONFERENCE_ALIASES`, next to the rest of the venue
classification. Nothing is stamped into the packs: the label is parsed from the prose
that already carries it, for the same reason `freshness_audit.py` parses its dates —
a second copy of a fact is a fact free to drift.

The four states
---------------
``current``  — the newest edition named is a future calendar year, or a month-dated
               event for this year's edition is still ahead. Nothing to do.
``due``      — the newest edition named is *this* calendar year and no stated date for
               it is still in the future. The edition may have met and it may not; the
               file does not say. A human or a live check has to look.
``stale``    — the newest edition named is a past calendar year. The meeting happened;
               the pack is describing a closed cycle. Actionable without ambiguity.
``retired``  — the source map itself states the venue stopped running, merged into
               another conference, or held a final edition. A last edition in the past
               is then correct, not stale. `IPSN-Skills` is the case that forced this
               state to exist: IPSN 2024 was the twenty-third and last edition before
               the series folded into SenSys, so the "outdated" label is the true one.

``due`` is deliberately not an error. Whether NeurIPS 2026 has met depends on a month
this file may never state, and a check that guesses would either cry wolf every autumn
or stay silent every spring. It reports; `--max-stale` is the part that can fail a build.

Outputs `.maintenance/CYCLE-CURRENCY.md`, holding only **stable** data (the parsed
edition years, not a status) so the dashboard can be byte-checked in CI while the
verdicts are recomputed against the current date at audit time.

Usage:
    python3 tools/cycle_audit.py                  # report
    python3 tools/cycle_audit.py --write          # regenerate the dashboard
    python3 tools/cycle_audit.py --check          # dashboard up to date?
    python3 tools/cycle_audit.py --max-stale 0    # gate
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from collections import Counter

from venue_lib import CONFERENCE_ALIASES, CONFERENCE_DEPTH_PACKS, ROOT, read

OUT = ROOT / ".maintenance" / "CYCLE-CURRENCY.md"

# An edition label is the venue's own name, optionally carrying a co-hosted partner
# ("IJCAI-ECAI 2026"), then the year — two digits or four. The separator set is narrow
# on purpose: a space, a hyphen, an en dash or the apostrophe of "Sec '26". Anything
# looser starts reading "IJCAI submissions closed in 2026" as an edition label.
_EDITION = r"(?:[-–][A-Z][A-Za-z&]{1,11})?[\s'’\-–]{0,3}(\d{4}|\d{2})\b"

# The label has to *begin* at the venue's name, not merely contain it. Several acronyms
# in this corpus are suffixes of another venue's: ACL of EACL, VLDB of PVLDB, and the
# aliased short forms (CCS, MM, S&P) are shorter still. Without this guard,
# `ACL-Skills` was reported as anchored to **ACL 2027** on the strength of one line
# about the **EACL 2027** commitment deadline — the pack has no 2027 fact in it, and the
# one check meant to notice that a conference pack describes a closed cycle was reading
# a different conference's calendar as evidence that it did not.
#
# A preceding *letter or digit* disqualifies; a hyphen or space does not, because a
# co-hosted edition genuinely writes the partner first ("IJCAI-ECAI 2026" is an ECAI
# edition) and `-27` is how AAAI writes its own.
_NAME_START = r"(?<![A-Za-z0-9])"

MONTHS = {
    "january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6,
    "july": 7, "august": 8, "september": 9, "october": 10, "november": 11,
    "december": 12, "jan": 1, "feb": 2, "mar": 3, "apr": 4, "jun": 6, "jul": 7,
    "aug": 8, "sep": 9, "sept": 9, "oct": 10, "nov": 11, "dec": 12,
}
MONTH_YEAR = re.compile(
    r"\b(" + "|".join(sorted(MONTHS, key=len, reverse=True)) + r")\b"
    r"[^\n]{0,18}?\b(20\d{2})\b",
    re.I,
)

# A retirement claim. Sharing a sentence with the venue's name is not enough — the two
# shapes that proved it are both in this corpus. `OOPSLA-Skills` says two *review
# outcomes* "were merged into" one, and `USENIX-Security-Skills` cites a page confirming
# USENIX **ATC** "was discontinued", in a sentence that goes on to name USENIX Security.
# So the claim has to follow the venue's own name closely enough to be about it, which
# both true retirements in the corpus do ("IPSN merged into…", "IPSN and IoTDI stopped
# running…") and neither impostor does.
RETIRED_PHRASE = (
    r"(?:merged into|merge[sd]? with|folded into|stopped running|no longer (?:runs|run|"
    r"held|takes place|a standalone)|discontinued|ceased|final edition|last edition|"
    r"last held)"
)
RETIRED_GAP = 40

# Editions outside this window are a typo, an ISSN or a history note, not a cycle.
YEAR_FLOOR, YEAR_CEILING = 2015, 2035


def aliases_for(pack: str) -> tuple[str, ...]:
    """The names a pack's venue may use for itself in its own source map."""
    return CONFERENCE_ALIASES.get(pack, (pack[: -len("-Skills")],))


# Neither a URL nor an inline code span is a claim. `https://aistats.org/aistats2027/`
# contains the venue's name followed by a year, and a source map citing it to record that
# the page **404s** would otherwise be read as announcing a 2027 edition — the newest-year
# rule then reports the pack as current on the strength of a page that does not exist.
# Stripping the scheme does not help: `aistats.org/aistats2027/` still matches. What
# actually separates the two is that prose asserts and a quoted literal does not, so both
# forms are removed and only prose is read.
URL = re.compile(r"<?https?://\S+")
CODE_SPAN = re.compile(r"`[^`\n]*`")


def edition_years(text: str, names: tuple[str, ...]) -> list[int]:
    """Every plausible edition year the *prose* states for this venue, ascending."""
    text = CODE_SPAN.sub(" ", URL.sub(" ", text))
    years: set[int] = set()
    for name in names:
        pattern = re.compile(_NAME_START + re.escape(name) + _EDITION, re.I)
        for match in pattern.finditer(text):
            raw = match.group(1)
            year = int(raw) if len(raw) == 4 else 2000 + int(raw)
            if YEAR_FLOOR <= year <= YEAR_CEILING:
                years.add(year)
    return sorted(years)


def latest_stated_month(text: str, year: int) -> int | None:
    """Latest month the text names alongside `year`, or None if it names none.

    Used only to separate "this year's edition is still ahead" from "this year's
    edition may already have met" — never to date anything.
    """
    months = [
        MONTHS[m.group(1).lower()]
        for m in MONTH_YEAR.finditer(text)
        if int(m.group(2)) == year
    ]
    return max(months) if months else None


def is_retired(text: str, names: tuple[str, ...]) -> bool:
    """Does the source map state that *this* venue stopped running?"""
    for name in names:
        pattern = re.compile(
            _NAME_START + re.escape(name) + r"[^.\n]{0," + str(RETIRED_GAP) + r"}?"
            + RETIRED_PHRASE,
            re.I,
        )
        if pattern.search(text):
            return True
    return False


def collect() -> list[dict]:
    records: list[dict] = []
    for pack in sorted(CONFERENCE_DEPTH_PACKS):
        source_map = ROOT / pack / "resources" / "official-source-map.md"
        if not source_map.exists():
            records.append({
                "pack": pack, "alias": aliases_for(pack)[0], "edition": None,
                "month": None, "retired": False, "note": "no source map",
            })
            continue
        text = read(source_map)
        names = aliases_for(pack)
        years = edition_years(text, names)
        newest = years[-1] if years else None
        records.append({
            "pack": pack,
            "alias": names[0],
            "edition": newest,
            "month": latest_stated_month(text, newest) if newest else None,
            "retired": is_retired(text, names),
            "note": "" if newest else "no edition label found",
        })
    return records


def status_of(record: dict, today: dt.date) -> str:
    edition = record["edition"]
    # A venue with an edition still ahead of it has not stopped running, whatever the
    # prose says — so the retirement reading only applies once the last edition named
    # is in the past. This is the second guard on the same misreading, and it holds
    # even for a phrasing the first one has never seen.
    if record["retired"] and edition is not None and edition <= today.year:
        return "retired"
    if edition is None:
        return "unknown"
    if edition > today.year:
        return "current"
    if edition < today.year:
        return "stale"
    month = record["month"]
    if month is not None and month >= today.month:
        return "current"
    return "due"


def render(records: list[dict]) -> str:
    """The dashboard. Stable fields only — the status is computed when it is read."""
    lines = [
        "# Conference cycle currency",
        "",
        "> Generated by `python3 tools/cycle_audit.py --write`. Do not edit by hand.",
        "",
        "A conference pack's facts belong to one **edition**, not to a standing "
        "masthead. `.maintenance/FRESHNESS.md` records when each source map was last "
        "re-read; this records **which edition it was re-read about**, which is the "
        "half that goes wrong silently — a pack can be a month old, accurate, and "
        "entirely about a cycle that has already closed.",
        "",
        "The `edition` column is the newest year the source map states for its own "
        "venue, and `month` the latest month it names alongside that year (blank where "
        "it names none). Both are parsed from the pack's own prose. **Status is not "
        "stored here** — it depends on today's date, and this file has to stay "
        "byte-stable for CI. Run the tool to see it.",
        "",
        f"**{len(records)} conference packs.**",
        "",
        "| Pack | Venue writes | Edition | Month | Retired | Note |",
        "|---|---|---:|---:|---|---|",
    ]
    for record in sorted(records, key=lambda r: (r["edition"] or 0, r["pack"])):
        lines.append(
            f"| {record['pack']} | {record['alias']} | "
            f"{record['edition'] or '—'} | {record['month'] or '—'} | "
            f"{'yes' if record['retired'] else 'no'} | {record['note'] or '—'} |"
        )
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="write the dashboard")
    parser.add_argument("--check", action="store_true",
                        help="fail if the committed dashboard is stale")
    parser.add_argument("--max-stale", type=int, default=None,
                        help="fail if more than N packs describe a past edition")
    parser.add_argument("--today", default=None,
                        help="override today's date (YYYY-MM-DD) for reproducible runs")
    parser.add_argument("--strict", action="store_true",
                        help="fail on any 'due' or 'unknown' pack as well")
    args = parser.parse_args(argv)

    if args.today:
        try:
            today = dt.date.fromisoformat(args.today)
        except ValueError:
            print(f"FAIL: --today must be YYYY-MM-DD, got {args.today!r}",
                  file=sys.stderr)
            return 1
    else:
        today = dt.date.today()

    records = collect()
    text = render(records)

    if args.check:
        current = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if current != text:
            print(f"FAIL: {OUT.relative_to(ROOT)} is stale — run "
                  "`python3 tools/cycle_audit.py --write`", file=sys.stderr)
            return 1
        print(f"OK: cycle dashboard current ({len(records)} conference packs)")

    if args.write:
        OUT.write_text(text, encoding="utf-8")
        print(f"wrote {OUT.relative_to(ROOT)} ({len(records)} conference packs)")

    by_status: dict[str, list[dict]] = {}
    for record in records:
        by_status.setdefault(status_of(record, today), []).append(record)

    counts = Counter({k: len(v) for k, v in by_status.items()})
    print(f"Cycle audit scanned {len(records)} conference packs as of {today}.")
    print("  " + " · ".join(
        f"{counts.get(state, 0)} {state}"
        for state in ("current", "due", "stale", "retired", "unknown")
    ))

    for state, heading in (
        ("stale", "Describing an edition that has already met"),
        ("due", "This year's edition, no future date stated — needs a live check"),
        ("unknown", "No edition label found in the source map"),
    ):
        rows = by_status.get(state, [])
        if not rows:
            continue
        print(f"\n{heading}:")
        for record in sorted(rows, key=lambda r: (r["edition"] or 0, r["pack"])):
            print(f"  {record['pack']:<32} {record['alias']} "
                  f"{record['edition'] or '—'}")

    failures = 0
    stale = by_status.get("stale", [])
    if args.max_stale is not None and len(stale) > args.max_stale:
        failures += 1
        print(f"\nFAIL: {len(stale)} pack(s) describe a past edition "
              f"(limit {args.max_stale}).", file=sys.stderr)
    if args.strict:
        loose = by_status.get("due", []) + by_status.get("unknown", [])
        if loose:
            failures += 1
            print(f"FAIL: {len(loose)} pack(s) due or unlabelled.", file=sys.stderr)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
