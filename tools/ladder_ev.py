#!/usr/bin/env python3
"""Cost a submission ladder in months: expected time to acceptance, and where it goes.

    python3 tools/ladder_ev.py \
        --rung "Journal of Finance:0.06:4.5" \
        --rung "Review of Financial Studies:0.10:5.0" \
        --rung "Journal of Financial and Quantitative Analysis:0.22:3.5" \
        --rung "Journal of Banking and Finance:0.35:2.5"

Each rung is ``name:p_accept:months_to_decision``. Add ``--revision-months N`` for the
time an R&R adds at whichever rung accepts (default 4).

Why this exists: authors compare venues one at a time, and the thing that actually
costs them a year is the *sequence*. A ladder of three long-shot journals and a ladder
that starts one rung lower can differ by eighteen months in expected time-to-print, and
nothing in the repository made that difference visible.

**This is arithmetic, not a forecast.** ``p_accept`` is the author's judgement of this
paper's chance at this venue — not the venue's published acceptance rate, which is
computed over a submission pool this paper is not a random draw from. Because the inputs
are uncertain, the tool always prints a sensitivity band (``--band``, default ±40% on
every p) and says plainly when two ladders are not distinguishable.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass


@dataclass
class Rung:
    name: str
    p_accept: float
    months: float


def parse_rung(spec: str) -> Rung:
    parts = spec.rsplit(":", 2)
    if len(parts) != 3:
        raise argparse.ArgumentTypeError(
            f"expected name:p_accept:months, got {spec!r}")
    name, p_text, months_text = parts
    try:
        p_accept, months = float(p_text), float(months_text)
    except ValueError:
        raise argparse.ArgumentTypeError(f"p_accept and months must be numbers: {spec!r}")
    if not 0.0 <= p_accept <= 1.0:
        raise argparse.ArgumentTypeError(f"p_accept must be in [0,1]: {spec!r}")
    if months < 0:
        raise argparse.ArgumentTypeError(f"months must be >= 0: {spec!r}")
    return Rung(name.strip(), p_accept, months)


def evaluate(rungs: list[Rung], revision_months: float, scale: float = 1.0) -> dict:
    """Walk the ladder top-down, carrying the probability of still being unplaced."""
    reach = 1.0                 # P(the paper is still looking when this rung is tried)
    elapsed = 0.0               # months consumed by the time this rung decides
    expected_months = 0.0
    months_if_placed = 0.0
    p_placed = 0.0
    per_rung = []
    for rung in rungs:
        p = min(max(rung.p_accept * scale, 0.0), 1.0)
        elapsed += rung.months
        # Every rung costs its review time whether it accepts or rejects; the rung that
        # accepts also costs the revision round that precedes acceptance.
        expected_months += reach * (rung.months + p * revision_months)
        months_if_placed += reach * p * (elapsed + revision_months)
        per_rung.append({
            "name": rung.name,
            "p_reach": reach,
            "p_accept_here": reach * p,
            "months": rung.months,
            "months_elapsed": elapsed + revision_months,
        })
        p_placed += reach * p
        reach *= 1 - p
    return {
        "expected_months": expected_months,
        "months_if_placed": months_if_placed / p_placed if p_placed else float("nan"),
        "p_placed": p_placed,
        "p_exhausted": reach,
        "per_rung": per_rung,
    }


def band(low_value: float, high_value: float) -> str:
    lo, hi = sorted((low_value, high_value))
    return f"{lo:.1f}-{hi:.1f}"


def render(result: dict, low: dict, high: dict, rungs: list[Rung]) -> str:
    lines = [
        f"Ladder of {len(rungs)} rungs",
        "",
        f"  Time until the ladder resolves : {result['expected_months']:.1f} months "
        f"(band {band(low['expected_months'], high['expected_months'])})",
        f"  Time to print, if it places    : {result['months_if_placed']:.1f} months "
        f"(band {band(low['months_if_placed'], high['months_if_placed'])})",
        f"  P(placed somewhere on it)      : {result['p_placed']:.0%} "
        f"(band {low['p_placed']:.0%}-{high['p_placed']:.0%})",
        f"  P(ladder exhausted, unplaced)  : {result['p_exhausted']:.0%}",
        "",
        "  rung                                          reach   lands here   review   by",
    ]
    for row in result["per_rung"]:
        lines.append(
            f"  {row['name'][:42]:<42}  {row['p_reach']:>5.0%}   "
            f"{row['p_accept_here']:>9.0%}   {row['months']:>4.1f}m  "
            f"{row['months_elapsed']:>5.1f}m")
    lines += [
        "",
        "  reach = P(the paper is still unplaced when this rung is tried).",
        "  Band = every p_accept scaled by the sensitivity factor; if two ladders' bands",
        "  overlap, the comparison does not support choosing between them.",
    ]
    if result["p_exhausted"] > 0.25:
        lines += [
            "",
            f"  ⚠ {result['p_exhausted']:.0%} chance of running out of rungs. The ladder "
            "needs a credible floor —",
            "    a venue that will realistically take the paper — or it is not a plan.",
        ]
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--rung", action="append", type=parse_rung, default=[],
                        metavar="NAME:P:MONTHS", help="a rung, top of the ladder first")
    parser.add_argument("--revision-months", type=float, default=4.0,
                        help="months an R&R adds at the accepting venue (default 4)")
    parser.add_argument("--band", type=float, default=0.4,
                        help="sensitivity band on every p_accept (default 0.4 = ±40%%)")
    args = parser.parse_args(argv)

    if len(args.rung) < 2:
        parser.error("a ladder needs at least two rungs — that is the whole point")

    result = evaluate(args.rung, args.revision_months)
    low = evaluate(args.rung, args.revision_months, scale=1 - args.band)
    high = evaluate(args.rung, args.revision_months, scale=1 + args.band)
    print(render(result, low, high, args.rung))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
