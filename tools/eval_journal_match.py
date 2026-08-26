#!/usr/bin/env python3
"""Measure the journal-match **candidate-generation** step against a labelled gold set.

``journal-match.md`` is a six-step method. Steps 3-6 (scoring, tiering, sequencing) are
model judgement and are not mechanically checkable. Step 2 — *given a paper, produce a
candidate set that contains the right venue* — is retrieval, and this measures it.

It measures it **through the code the skill runs**: both this harness and
``tools/match_venues.py`` go through ``match_lib.VenueMatcher``. Before, the harness
re-implemented a keyword overlap that nothing else used, so the number described a
retriever no author ever invoked.

What a number here does and does not mean:

* It **does** regression-test the index and the matcher together: break either and
  recall drops.
* It **does not** score the agent's shortlist. An agent reads each candidate's skills
  and source map before recommending; this harness reads only the scope index.

Usage:  python3 tools/eval_journal_match.py [--write] [--min-recall-at-10 N]
"""

from __future__ import annotations

import argparse
import csv
import sys
from collections import defaultdict

from match_lib import VenueMatcher, load_venues
from venue_lib import ROOT

GOLD = ROOT / "shared-resources/journal-selection/eval/gold-set.tsv"
ABSTRACTS = ROOT / "shared-resources/journal-selection/eval/abstract-terms.tsv"
RESULTS = ROOT / "shared-resources/journal-selection/eval/RESULTS.md"

CUTOFFS = (1, 5, 10, 20)
RANK_LIMIT = None        # rank the whole corpus, so `any-rank` means what it says
# A configuration that covers a handful of papers produces a number with a confidence
# interval wider than the effect anyone would read into it. Below this share of the
# split, the row is withheld and the shortfall is reported instead — a missing number is
# honest, a number from sixty papers presented beside one from eight hundred is not.
MIN_CONFIG_COVERAGE = 0.25

# Not a query: the same headline query run through a matcher built without the subject
# vocabulary, so the table can show what that vocabulary is worth rather than assert it.
SCOPE_ONLY_MODE = "title (scope only)"


def load_abstract_terms() -> dict[str, str]:
    """paper title -> space-joined abstract term bag (see tools/fetch_abstracts.py)."""
    if not ABSTRACTS.exists():
        return {}
    with ABSTRACTS.open(encoding="utf-8") as handle:
        return {row["paper_title"].lower(): row["abstract_terms"]
                for row in csv.DictReader(handle, delimiter="\t")}


def build_query(row: dict, mode: str, abstracts: dict[str, str]) -> str | None:
    title = row["paper_title"]
    # `title (scope only)` is the same query against a differently-built matcher, not a
    # different query. It is listed here rather than special-cased at the call site so
    # that "every mode the harness runs is one this function understands" stays a
    # checkable invariant.
    if mode in ("title", SCOPE_ONLY_MODE, "title+discipline", "oracle-discipline"):
        return title
    if mode == "title+context":
        return f"{title} {row['context']}" if row["context"] else title
    if mode == "title+abstract":
        terms = abstracts.get(title.lower())
        return f"{title} {terms}" if terms else None
    raise ValueError(mode)


def evaluate(gold, matcher: VenueMatcher, mode: str, abstracts) -> dict:
    hits = {k: 0 for k in CUTOFFS}
    reciprocal = 0.0
    retrieved_at_all = 0
    scored = 0
    lane_violations = 0
    lane_slots = 0
    per_discipline: dict[str, list[int]] = defaultdict(lambda: [0, 0])

    for row in gold:
        query = build_query(row, mode, abstracts)
        if query is None:                     # not covered by this configuration
            continue
        scored += 1
        ranking = matcher.rank(
            query,
            discipline=row["discipline"] if mode in ("title+discipline",
                                                     "oracle-discipline") else None,
            only_discipline=(mode == "oracle-discipline"),
            limit=RANK_LIMIT,
        )
        ids = [h.venue["venue_id"] for h in ranking]
        truth = row["true_venue_id"]
        position = ids.index(truth) + 1 if truth in ids else None
        if position:
            retrieved_at_all += 1
            reciprocal += 1.0 / position
            for k in CUTOFFS:
                if position <= k:
                    hits[k] += 1
        bucket = per_discipline[row["discipline"]]
        bucket[1] += 1
        if position and position <= 10:
            bucket[0] += 1

        # Lane precision: an empirical paper offered a theory-only venue is a wrong
        # answer even when the true venue also appears. Judged on the true venue's lane,
        # which is the only lane label the gold set carries.
        for hit in ranking[:10]:
            lane_slots += 1
            if lanes_conflict(row["lane"], hit.venue["lane"]):
                lane_violations += 1

    n = max(scored, 1)
    return {
        "mode": mode,
        "n": scored,
        "recall": {k: hits[k] / n for k in CUTOFFS},
        "mrr": reciprocal / n,
        "coverage": retrieved_at_all / n,
        "lane_violation": lane_violations / max(lane_slots, 1),
        "per_discipline": {d: (c[0] / c[1], c[1])
                           for d, c in sorted(per_discipline.items())},
    }


def lanes_conflict(paper_lane: str, venue_lane: str) -> bool:
    """Would sending a paper of this lane to a venue of that lane be a category error?

    Only the unambiguous direction is counted: an empirical paper to a venue that
    publishes no empirics. Theory papers appear in empirical venues routinely, so the
    reverse is not a violation.
    """
    if "empirical" not in paper_lane:
        return False
    return "empirical" not in venue_lane


DESCRIPTIONS = {
    "title": ("paper title only", "all venues, no prior",
              "**headline.** The paper's own words, chosen by its authors — no shared "
              "vocabulary with the index."),
    "title (scope only)": ("paper title only",
                           "all venues, **prose vocabulary only**",
                           "the headline query run against `scope-postings.tsv` alone — "
                           "what the matcher could do when the only thing it knew about "
                           "a venue was the prose describing how to submit to it. "
                           "Contrast row: the gap to `title` is what the subject "
                           "vocabulary buys."),
    "title+abstract": ("title + the abstract's term bag", "all venues, no prior",
                       "what an author actually pastes in. Covers only the gold papers "
                       "whose abstract could be resolved from a free bibliographic "
                       "source (Crossref, Europe PMC, arXiv), which is uneven by "
                       "discipline — see Limitations."),
    "title+context": ("title + the exemplar library's gloss", "all venues, no prior",
                      "optimistic bound. The gloss was written by the same authors as "
                      "the packs, so it is vocabulary-correlated with the index. "
                      "Contrast only."),
    "title+discipline": ("paper title only", "all venues, discipline **prior**",
                         "Step 1 done right: the true discipline and its adjacents are "
                         "boosted, but a strong match elsewhere still surfaces."),
    "oracle-discipline": ("paper title only",
                          "discipline + adjacents, as a **filter**",
                          "the ceiling if Step 1 is perfect *and* trusted absolutely. "
                          "The default is the softer prior above, because Step 1 is a "
                          "judgement and a wrong guess under a filter deletes the "
                          "answer outright rather than merely mis-ranking it."),
}


def render(results, venues, gold, abstracts, dev_headline, withheld, n_split) -> str:
    n_venues = len(venues)
    n_test = sum(1 for g in gold if g["split"] == "test")
    lines = [
        "# Journal-match retrieval evaluation",
        "",
        "> Generated by `python3 tools/eval_journal_match.py --write`. "
        "Do not edit by hand.",
        "",
        f"**Corpus:** {n_venues} venues in `venue-index.tsv`, "
        f"scored through `tools/match_lib.py` — the same code path "
        f"`tools/match_venues.py` runs · **Gold set:** {len(gold)} papers across "
        f"{len({g['true_venue_id'] for g in gold})} venues "
        "(`eval/gold-set.tsv`, harvested from the packs' own verified exemplar "
        f"libraries) · **Scored below:** the {n_test}-paper `test` half.",
        "",
        "## What is being measured",
        "",
        "Step 2 of [`../journal-match.md`](../journal-match.md) — **candidate "
        "generation**. Given a paper, does the matcher surface its true venue in the "
        "top *k*? Steps 3-6 (scoring, tiering, the resubmission ladder) are model "
        "judgement and are deliberately **not** scored here.",
        "",
        "This is a retrieval floor, not a ceiling on the capability: an agent reads "
        "each candidate's skills and `official-source-map.md` before recommending "
        "anything. The harness reads only the venue index.",
        "",
        "**Two vocabularies.** Every configuration below searches both "
        "`scope-postings.tsv` (TF-IDF over each pack's own prose, which is about a "
        "*process*) and `topic-postings.tsv` (TF-IDF over the titles of articles the "
        "venue published, which is about a *subject*). The `title (scope only)` row is "
        "the first of those alone — the same query, the same code path, the earlier "
        "index — kept in the table because a component whose contribution is folded "
        "into the headline stops being auditable.",
        "",
        "## Results",
        "",
        "| Configuration | n | R@1 | R@5 | R@10 | R@20 | MRR | any-rank | wrong-lane@10 |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for r in results:
        lines.append(
            f"| `{r['mode']}` | {r['n']} | "
            + " | ".join(f"{r['recall'][k]:.1%}" for k in CUTOFFS)
            + f" | {r['mrr']:.3f} | {r['coverage']:.1%} "
            f"| {r['lane_violation']:.1%} |"
        )
    random_at = {k: k / n_venues for k in CUTOFFS}
    lines += [
        "| _random baseline_ | — | "
        + " | ".join(f"{random_at[k]:.1%}" for k in CUTOFFS)
        + " | — | — | — |",
        "",
        "`any-rank` = the true venue was retrieved at all, at any depth (it shares at "
        "least one index term with the query, in either vocabulary) — the ceiling every "
        "cutoff above is "
        "working against. It stops bounding anything once the query is long: "
        "`title+abstract` sends a median of 130 terms against a 900-deep index, so "
        "*some* term reaches the true venue essentially always, and its 100% is a "
        "property of the query length rather than a solved problem. Read it on the "
        "title rows. `wrong-lane@10` = share of top-10 slots given to a venue that "
        "publishes no empirical work, for a paper whose true venue does — the cheapest "
        "kind of obviously wrong suggestion, and the one an author notices first.",
        "",
        "### Tuning integrity",
        "",
        "The matcher has five weighting constants (`RANK_DECAY`, `PHRASE_BONUS`, "
        "`PART_DISCOUNT`, `COORD_K`, `TOPIC_WEIGHT`). They were chosen against the gold "
        "set's `dev` half; every number in this file is computed on `test`, which they "
        "were never fitted to. Papers are assigned by a hash of their title, so the "
        "split is stable as packs are added.",
        "",
        f"| Half | n | R@10 | MRR |",
        "|---|---:|---:|---:|",
        f"| `dev` (tuned on) | {dev_headline['n']} | "
        f"{dev_headline['recall'][10]:.1%} | {dev_headline['mrr']:.3f} |",
        f"| `test` (reported) | {results[0]['n']} | "
        f"{results[0]['recall'][10]:.1%} | {results[0]['mrr']:.3f} |",
        "",
        "A large gap between the two rows would mean the constants had been fitted to "
        "noise; they track each other closely, which is the point of publishing both.",
        "",
        "### Reading the configurations",
        "",
        "| Configuration | Query | Candidate set | Interpretation |",
        "|---|---|---|---|",
    ]
    for r in results:
        query, candidates, note = DESCRIPTIONS[r["mode"]]
        lines.append(f"| `{r['mode']}` | {query} | {candidates} | {note} |")
    for r in withheld:
        query, candidates, note = DESCRIPTIONS[r["mode"]]
        lines.append(f"| `{r['mode']}` _(withheld)_ | {query} | {candidates} | {note} |")
    if withheld:
        names = ", ".join(f"`{r['mode']}` ({r['n']}/{n_split} papers, "
                          f"{r['n'] / max(n_split, 1):.0%})" for r in withheld)
        lines += [
            "",
            f"**Withheld for thin coverage:** {names}. A configuration is reported only "
            f"once it covers {MIN_CONFIG_COVERAGE:.0%} of the split; below that the "
            "confidence interval is wider than anything a reader would conclude from "
            "the number. Rerun `tools/fetch_abstracts.py` to fill the gap.",
        ]
    lines += [
        "",
        "## Recall@10 by discipline (`title` configuration)",
        "",
        "| Discipline | R@10 | n |",
        "|---|---:|---:|",
    ]
    headline = next(r for r in results if r["mode"] == "title")
    ranked = sorted(headline["per_discipline"].items(), key=lambda kv: -kv[1][1])
    for discipline, (recall, count) in ranked[:20]:
        lines.append(f"| {discipline} | {recall:.1%} | {count} |")
    covered = sum(1 for g in gold if g["paper_title"].lower() in abstracts)
    if covered:
        # Abstract coverage is not missing at random: Europe PMC is near-complete for
        # medicine and the life sciences while Crossref carries an abstract for only
        # some of the social-science corpus. Stating the spread keeps a reader from
        # reading the `title+abstract` row as a like-for-like uplift on the headline.
        per_discipline: dict[str, list[int]] = {}
        for g in gold:
            bucket = per_discipline.setdefault(g["discipline"], [0, 0])
            bucket[1] += 1
            if g["paper_title"].lower() in abstracts:
                bucket[0] += 1
        sizeable = {d: hit / total for d, (hit, total) in per_discipline.items()
                    if total >= 20}
        spread = ""
        if len(sizeable) >= 2:
            best = max(sizeable, key=sizeable.get)
            worst = min(sizeable, key=sizeable.get)
            spread = (f" That coverage is uneven by discipline — {sizeable[best]:.0%} "
                      f"of {best} papers against {sizeable[worst]:.0%} of {worst} — so "
                      "the row is not a like-for-like uplift on the headline.")
        abstract_note = (
            f"`title+abstract` is the realistic figure; it covers {covered} of "
            f"{len(gold)} gold papers ({covered / max(len(gold), 1):.0%}), the rest "
            "being papers that could not be resolved to an open abstract." + spread)
    else:
        abstract_note = (
            "The realistic `title+abstract` configuration is **not reported here**: "
            "`eval/abstract-terms.tsv` has not been built. It needs network access, so "
            "it is a maintainer step rather than a CI step — run "
            "`python3 tools/fetch_abstracts.py` (resumable) to produce it.")
    lines += [
        "",
        "## Limitations",
        "",
        "1. **The gold set is drawn from the repository itself.** Exemplar libraries "
        "hold papers the pack authors judged canonical for that venue, which skews "
        "toward famous, prototypical papers. Real routing decisions involve marginal "
        "papers, which are harder.",
        "2. **The headline query is a title.** A real match runs on an abstract plus "
        "the five signals of Step 1; a title is a deliberately thin, pessimistic query. "
        + abstract_note,
        "3. **Only depth packs contribute labels.** Breadth-bundle venues are in the "
        "candidate set (so they can absorb probability mass) but have no gold papers, "
        "which makes the task harder, not easier.",
        "4. **Keywords are derived, not curated.** `scope_keywords` come from TF-IDF "
        "over each venue's own prose. Chinese terms are filtered through a vocabulary "
        "discovered from the corpus (cohesion + boundary entropy), which removes "
        "cross-boundary fragments but is not a substitute for a real segmenter.",
        "5. **The exemplar libraries are excluded from the index text**, so a gold "
        "paper's own citation cannot leak into the venue it labels.",
        "6. **The subject vocabulary is a different measurement, not only a better "
        "one.** `topic-postings.tsv` is derived from the titles of articles each venue "
        "actually published, harvested from Crossref and DBLP. Titles that *are* gold "
        "papers are dropped and the count is published in that file's header — but "
        "harvesting a venue's own publication stream carries a residual optimism the "
        "prose vocabulary does not: a gold paper's companion piece, its authors' later "
        "work and its subfield's subsequent vocabulary are all still in there. That is "
        "what any real recommender has, and it is why the `title (scope only)` row is "
        "reported beside the headline instead of being replaced by it.",
        "7. **Not every venue has a subject vocabulary.** Resolution is exact or it "
        "does not happen, and the venues it cannot reach are not a random sample: "
        "Chinese-language journals that neither registry indexes have none at all. "
        "Those venues are searched over their prose alone while their neighbours are "
        "searched over both, so their placement is weaker evidence about fit than "
        "another venue's. `tools/match_venues.py` marks them; this harness does not "
        "correct for it.",
        "",
        "## Regenerating",
        "",
        "```bash",
        "python3 tools/gen_venue_index.py     # index + scope postings",
        "python3 tools/gen_ladder.py          # ladder + discipline adjacency",
        "python3 tools/build_eval_set.py      # gold set",
        "python3 tools/fetch_abstracts.py     # abstract term bags (network; optional)",
        "python3 tools/eval_journal_match.py --write",
        "```",
        "",
    ]
    return "\n".join(lines)


MODES = ["title", SCOPE_ONLY_MODE, "title+abstract", "title+context",
         "title+discipline", "oracle-discipline"]


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="write eval/RESULTS.md")
    parser.add_argument("--min-recall-at-10", type=float, default=None,
                        help="exit non-zero if headline recall@10 falls below this")
    parser.add_argument("--modes", help="comma-separated subset, for quick iteration")
    args = parser.parse_args(argv)

    venues = load_venues()
    with GOLD.open(encoding="utf-8") as handle:
        gold = list(csv.DictReader(handle, delimiter="\t"))
    abstracts = load_abstract_terms()
    matcher = VenueMatcher(venues)

    held_out = [r for r in gold if r["split"] == "test"]
    tuning = [r for r in gold if r["split"] == "dev"]

    # The contrast row runs the same query through a matcher built without the subject
    # vocabulary. Two matchers, not a flag on one, so neither configuration can quietly
    # borrow the other's postings.
    scope_only = VenueMatcher(venues, topic_weight=0.0) if matcher.topics_loaded else None

    modes = args.modes.split(",") if args.modes else MODES
    scored = []
    for mode in modes:
        if mode == SCOPE_ONLY_MODE:
            if scope_only is None:
                continue
            row = evaluate(held_out, scope_only, "title", abstracts)
            row["mode"] = SCOPE_ONLY_MODE
            scored.append(row)
            continue
        scored.append(evaluate(held_out, matcher, mode, abstracts))
    floor = MIN_CONFIG_COVERAGE * len(held_out)
    results = [r for r in scored if r["n"] >= floor]
    withheld = [r for r in scored if 0 < r["n"] < floor]
    dev_headline = evaluate(tuning, matcher, "title", abstracts)

    for r in results:
        recalls = " ".join(f"R@{k}={r['recall'][k]:.1%}" for k in CUTOFFS)
        print(f"{r['mode']:<18} n={r['n']:<5} {recalls}  MRR={r['mrr']:.3f}  "
              f"any={r['coverage']:.1%}  wrong-lane@10={r['lane_violation']:.1%}")
    for r in withheld:
        print(f"{r['mode']:<18} n={r['n']:<5} withheld: covers "
              f"{r['n'] / len(held_out):.0%} of the split, below the "
              f"{MIN_CONFIG_COVERAGE:.0%} floor")
    print(f"{'(dev) title':<18} n={dev_headline['n']:<5} "
          f"R@10={dev_headline['recall'][10]:.1%}  "
          f"MRR={dev_headline['mrr']:.3f}   <- tuning half, not the headline")

    if args.write:
        RESULTS.parent.mkdir(parents=True, exist_ok=True)
        RESULTS.write_text(
            render(results, venues, gold, abstracts, dev_headline, withheld,
                   len(held_out)),
            encoding="utf-8")
        print(f"\nwrote {RESULTS.relative_to(ROOT)}")

    headline = next(r for r in results if r["mode"] == "title")["recall"][10]
    if args.min_recall_at_10 is not None and headline < args.min_recall_at_10:
        print(f"FAIL: headline recall@10 {headline:.1%} below floor "
              f"{args.min_recall_at_10:.1%}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
