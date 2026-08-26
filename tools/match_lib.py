#!/usr/bin/env python3
"""Step-2 candidate generation for journal-match: rank venues against a paper's text.

``journal-match.md`` step 2 used to read "filter `venue-index.tsv` by discipline, then
narrow on `scope_keywords`" — an instruction an agent carried out by eye, differently
every time, over a 570 KB file. That made the step unreproducible and made the eval a
measurement of something nobody actually ran.

This module is that step, executed the same way by ``tools/match_venues.py`` (what the
skill invokes) and ``tools/eval_journal_match.py`` (what CI scores). Improving retrieval
now means improving one function that both the product and the metric go through.

What it is not: a recommendation. It returns *candidates to read*. Fit, odds, cost and
audience are judged by the agent against each venue's own pack and source map — see
steps 3-6 of ``shared-resources/journal-selection/journal-match.md``.
"""

from __future__ import annotations

import csv
import math
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path

from venue_lib import ROOT, index_digest, tokenize

INDEX = ROOT / "shared-resources/journal-selection/venue-index.tsv"
POSTINGS = ROOT / "shared-resources/journal-selection/scope-postings.tsv"
TOPIC_POSTINGS = ROOT / "shared-resources/journal-selection/topic-postings.tsv"
ADJACENCY = ROOT / "shared-resources/journal-selection/discipline-adjacency.tsv"

# --- weighting ---------------------------------------------------------------------
# Chosen on the gold set's `dev` half only; the headline in eval/RESULTS.md is computed
# on `test`, which none of these were fitted to. All four sit on a plateau (dev R@10
# varies by 0.3 points across the top of the grid), so they are set to the reading that
# is easiest to justify rather than to the arithmetic maximum.

# A keyword's rank within its venue is evidence about that keyword, not about the venue:
# term 1 of 300 is what the venue is about, term 280 is something it once mentioned.
RANK_DECAY = 2.0
# A phrase keyword is *weaker* evidence than a rare single word, not stronger: TF-IDF
# bigrams drawn from prose are mostly incidental collocations ("recent work", "panel
# data"), whereas a rare unigram is usually a subject term. Setting this above 1.0 —
# the intuitive choice — cost 17 points of recall@10.
PHRASE_BONUS = 0.6
# The individual words inside a phrase keyword add almost nothing: if they carried the
# meaning they are already present as unigrams in their own right.
PART_DISCOUNT = 0.1
# Discipline is a prior, not a filter. Getting it wrong should cost a paper its ranking,
# not its only correct answer — a hard filter deletes the true venue outright, and Step 1
# profiling is a judgement call that will sometimes be wrong.
DISCIPLINE_BOOST = 2.2
ADJACENT_BOOST = 1.5
# Agreement across several distinct terms beats one lucky rare word. Without this, a
# design conference topped a minimum-wage paper's shortlist on the single word "design"
# while the labour-economics journals below it matched six terms each.
COORD_K = 4.0
# How hard to discount a term that is spread across unrelated disciplines. Inverse
# document frequency asks *how many venues* use a term; this asks *how many different
# subjects* do — which is a different question, and the one that separates a subject
# term from a homonym. "electrolyte" lives in one discipline and means something;
# "sensor" and "generation" live everywhere, and they are why a paper on a cytosolic DNA
# sensor was offered SenSys, IPSN and PerCom, and why "Hallmarks of Cancer: The Next
# Generation" was offered a natural-language-generation conference.
DISCIPLINE_SPREAD_ALPHA = 0.6
# How loudly the *subject* vocabulary speaks next to the *scope* vocabulary.
#
# `scope-postings.tsv` is derived from each pack's own prose, which is about a process:
# how to submit, how review works, what the format rules are. A paper title is about a
# subject. Asked to connect "Deep Contextualized Word Representations" to ACL through a
# vocabulary in which ACL is largely a set of anonymity rules, the matcher could not —
# 14% of dev papers reached their true venue at no depth at all.
#
# `topic-postings.tsv` (see `tools/fetch_venue_topics.py`) is the same venues' published
# article titles, which are in the register the query is in. Both are ranked TF-IDF lists
# built the same way, so weighting them equally is the reading that needs no argument —
# and on the gold set's `dev` half that is also where the curve is flat:
#
#     weight   0.0   0.25   0.5   0.75   1.0   1.5   2.0   3.0
#     R@10    46.9   58.3  59.5   59.7  58.5  57.4  56.2  53.8     (dev)
#
# Everything from 0.25 to 1.0 sits inside 1.4 points, so this is set to 1.0 rather than
# to the arithmetic maximum at 0.75 — the same rule the four constants above follow. It
# exists so the balance can be retuned without rebuilding either file, not because the
# number is interesting. What *is* interesting is the first column: nothing else in this
# module moves recall by ten points.
TOPIC_WEIGHT = 1.0


@dataclass
class Hit:
    venue: dict
    score: float
    terms: list[tuple[str, float]] = field(default_factory=list)

    def why(self, limit: int = 6) -> str:
        return ", ".join(t for t, _ in self.terms[:limit])


def load_venues(path: Path = INDEX) -> list[dict]:
    with path.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def load_adjacency(path: Path = ADJACENCY) -> dict[str, set[str]]:
    """discipline -> disciplines whose venues are named as alternatives to its own."""
    out: dict[str, set[str]] = defaultdict(set)
    if not path.exists():
        return out
    with path.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            out[row["discipline"]].add(row["adjacent_discipline"])
    return out


class IndexMismatch(RuntimeError):
    """The postings file does not describe the index that was loaded."""


class VenueMatcher:
    """Ranks venues against a paper's text over two vocabularies of the same shape.

    ``scope-postings.tsv`` says what the repository *knows* about a venue; it is derived
    from each pack's prose, which is about a process. ``topic-postings.tsv`` says what
    the venue *publishes about*; it is derived from the titles of its own articles,
    which is the register a query is in. Neither one is sufficient: the scope vocabulary
    carries the Chinese venues, the breadth bundles and everything a bibliographic API
    could not resolve, and the topic vocabulary carries the subject words no pack ever
    had a reason to write down. They are loaded and weighted identically and merged.

    The topic file is optional. Without it the matcher behaves exactly as it did before
    the file existed, which is what a fresh clone that has not run the (networked)
    harvest gets.
    """

    def __init__(self, venues: list[dict] | None = None,
                 postings_path: Path = POSTINGS,
                 adjacency: dict[str, set[str]] | None = None,
                 topics_path: Path | None = TOPIC_POSTINGS,
                 topic_weight: float = TOPIC_WEIGHT):
        self.venues = venues if venues is not None else load_venues()
        self.adjacency = adjacency if adjacency is not None else load_adjacency()
        self.postings: dict[str, list[tuple[int, float]]] = defaultdict(list)
        self.topics_loaded = False
        # Which venues the subject vocabulary actually reached. Not every venue has one:
        # a Chinese-language journal that neither Crossref nor DBLP indexes competes on
        # its scope prose alone, against neighbours that have both vocabularies. That is
        # a real asymmetry and the tools say so rather than hiding it — see
        # `match_venues.py`, which marks such a candidate in the shortlist.
        self.subject_venues: set[str] = set()
        self._merge(self._weighted_postings(postings_path))
        if topics_path is not None and topics_path.exists() and topic_weight:
            topics = self._weighted_postings(topics_path, scale=topic_weight)
            self._merge(topics)
            self.subject_venues = {self.venues[row]["venue_id"]
                                   for plist in topics.values() for row, _ in plist}
            self.topics_loaded = True

    # --- index loading ------------------------------------------------------

    def _merge(self, postings: dict[str, list[tuple[int, float]]]) -> None:
        for term, plist in postings.items():
            self.postings[term].extend(plist)

    def _weighted_postings(self, path: Path,
                           scale: float = 1.0) -> dict[str, list[tuple[int, float]]]:
        depth = 300
        declared_rows = None
        declared_digest = None
        raw: dict[str, list[tuple[int, int]]] = {}
        with path.open(encoding="utf-8") as handle:
            for line in handle:
                line = line.rstrip("\n")
                if not line:
                    continue
                if line.startswith("#"):
                    key, _, value = line[1:].partition("\t")
                    if key == "depth" and value.isdigit():
                        depth = int(value)
                    elif key == "venues" and value.isdigit():
                        declared_rows = int(value)
                    elif key == "digest":
                        declared_digest = value
                    continue
                term, _, refs = line.partition("\t")
                pairs = []
                for ref in refs.split(","):
                    row, _, rank = ref.partition(":")
                    pairs.append((int(row), int(rank)))
                raw[term] = pairs

        stale = ("regenerate with tools/fetch_venue_topics.py --harvest"
                 if path == TOPIC_POSTINGS else
                 "regenerate with tools/gen_venue_index.py")
        if declared_rows is not None and declared_rows != len(self.venues):
            raise IndexMismatch(
                f"{path.name} describes {declared_rows} venues but the index holds "
                f"{len(self.venues)} — {stale}")
        # The count alone would pass for a same-size reordering, and every posting would
        # then be attributed to the wrong venue — silently, and plausibly.
        if declared_digest:
            actual = index_digest([v["venue_id"] for v in self.venues])
            if actual != declared_digest:
                raise IndexMismatch(
                    f"{path.name} was built against a different venue ordering "
                    f"(digest {declared_digest}, index {actual}) — {stale}")

        n = max(len(self.venues), 1)
        postings: dict[str, list[tuple[int, float]]] = defaultdict(list)
        # Document frequency is computed from the postings themselves, so the weighting
        # never has to be kept in sync with a second file. It is computed per file, not
        # over the merge: a term's rarity among *published titles* is a different
        # measurement from its rarity among *editorial prose*, and averaging the two
        # would describe neither.
        for term, pairs in raw.items():
            idf = math.log(n / (1 + len(pairs)))
            if idf <= 0:
                continue
            phrase = PHRASE_BONUS if " " in term else 1.0
            for row, rank in pairs:
                weight = scale * idf * phrase / (1 + RANK_DECAY * rank / depth)
                postings[term].append((row, weight))
                if " " in term:
                    for part in term.split():
                        postings[part].append((row, weight * PART_DISCOUNT))

        self._discount_cross_discipline_terms(postings)
        return postings

    def _discount_cross_discipline_terms(
            self, postings: dict[str, list[tuple[int, float]]]) -> None:
        """Scale each term down by how many different disciplines lay claim to it.

        A term used by twenty venues inside one discipline is a subject term; a term
        used by twenty venues across twelve disciplines is a word the language happens
        to reuse. Both have the same document frequency, so IDF cannot tell them apart —
        the discount is on the *entropy* of the term's discipline distribution.
        """
        disciplines = [venue["discipline"] for venue in self.venues]
        for term, plist in postings.items():
            if len(plist) < 2:
                continue
            spread: Counter = Counter(disciplines[row] for row, _ in plist)
            total = sum(spread.values())
            entropy = -sum((c / total) * math.log(c / total) for c in spread.values())
            if entropy <= 0:
                continue
            factor = 1.0 / (1.0 + DISCIPLINE_SPREAD_ALPHA * entropy)
            postings[term] = [(row, weight * factor) for row, weight in plist]

    # --- querying -----------------------------------------------------------

    @staticmethod
    def query_terms(text: str) -> set[str]:
        words = tokenize(text)
        return set(words) | {f"{a} {b}" for a, b in zip(words, words[1:])}

    def rank(self, text: str, *, discipline: str | None = None,
             lane: str | None = None, region: str | None = None,
             venue_type: str | None = None, coverage: str | None = None,
             exclude: set[str] | None = None,
             only_discipline: bool = False,
             limit: int | None = None) -> list[Hit]:
        exclude = exclude or set()
        adjacent = self.adjacency.get(discipline, set()) if discipline else set()

        scores: Counter = Counter()
        contributions: dict[int, Counter] = defaultdict(Counter)
        for term in self.query_terms(text):
            for row, weight in self.postings.get(term, ()):
                scores[row] += weight
                contributions[row][term] += weight

        hits: list[Hit] = []
        for row, base in scores.items():
            venue = self.venues[row]
            if venue["venue_id"] in exclude:
                continue
            if lane and lane not in venue["lane"]:
                continue
            if region and venue["region"] != region:
                continue
            if venue_type and venue["venue_type"] != venue_type:
                continue
            if coverage and venue["coverage"] != coverage:
                continue
            matched = len(contributions[row])
            score = base * matched / (matched + COORD_K)
            if discipline:
                if venue["discipline"] == discipline:
                    score *= DISCIPLINE_BOOST
                elif venue["discipline"] in adjacent:
                    score *= ADJACENT_BOOST
                elif only_discipline:
                    continue
            hits.append(Hit(venue, score,
                            contributions[row].most_common(8)))

        # deterministic tie-break so a number is reproducible run to run
        hits.sort(key=lambda h: (-h.score, h.venue["venue_id"]))
        return hits[:limit] if limit else hits
