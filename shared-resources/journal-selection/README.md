# Journal-Selection — cross-journal matching capability

A venue-neutral capability layer that turns *"where should I send this paper?"* into a
ranked, reasoned shortlist across the whole repository. Complements the per-journal packs
(which answer *"how do I clear this venue's bar?"*) with the missing front-door question
*"which venue?"*.

## Contents

| File | What it gives an agent |
|---|---|
| [`journal-match.md`](journal-match.md) | The matching methodology: profile the paper (discipline / method / contribution / setting / ambition) → shortlist candidates with `tools/match_venues.py` → score on Fit × acceptance-odds × turnaround × cost/policy × audience → return a reach/match/safe shortlist + a costed resubmission ladder. Reads volatile facts live from each pack's source-map. |
| [`worked-example.md`](worked-example.md) | One paper through all six steps with the tool output pasted verbatim — including a plausible-looking candidate that is wrong, and a ladder comparison whose probability difference turns out not to survive its own sensitivity band. |
| [`paper-profile.md`](paper-profile.md) | The five signals, written down **once** in a small YAML block and read by every downstream toolkit skill, so they stop re-deriving the paper and disagreeing about it. |
| [`venue-index.tsv`](venue-index.tsv) | **Stable** index of **743 venues** — every venue the repository covers, whether as a depth pack or as a profile inside a discipline bundle. Human-readable: 40 scope terms per venue. |
| [`scope-postings.tsv`](scope-postings.tsv) | The retrieval index behind the matcher: the same ranked vocabulary, 300 terms deep, inverted. Generated; not meant to be read. |
| [`ladder.tsv`](ladder.tsv) | **1,507 adjacency edges** for the resubmission ladder: which venues each pack names as siblings or alternatives, with a mention count and a same-discipline flag. Candidate adjacency, not a ranking. |
| [`discipline-adjacency.tsv`](discipline-adjacency.tsv) | Which disciplines routinely stand in for one another, collapsed from the venue graph. Widens the matcher's discipline prior so a labour paper still reaches general economics. |
| [`eval/`](eval/README.md) | A 1,738-paper gold set, split into a tuning half and a held-out half, and a harness that scores the candidate-generation step — so an index regression shows up as a failing number rather than a quietly worse recommendation. |

## Running it

```bash
python3 tools/match_venues.py --title "..." --abstract "..." \
        --discipline economics/labor --lane empirical --top 15   # step 2
python3 tools/ladder_ev.py --rung "Venue A:0.06:4.5" --rung "Venue B:0.2:3.0"
                                                                 # step 6
```

Step 2 is a command rather than an instruction to read a TSV by eye, for three reasons:
it is reproducible, it searches the full 300-term vocabulary instead of the 40 published
per venue, and **the evaluation scores the same code path**, so the published number
describes what an author actually runs.

The matcher **retrieves**; the agent recommends. Every result names where to read more,
and the terms it matched on, so a nonsense hit is visible as one.

## The index schema

| Column | Notes |
|---|---|
| `venue_id` | stable slug; the join key for `ladder.tsv` and the gold set |
| `display_name` | human-readable venue name |
| `coverage` | `depth` (own pack, live-checked source map) or `breadth` (one profile skill inside a bundle) |
| `venue_type` | `journal` / `conference` |
| `discipline`, `region`, `lane` | the primary filters — `lane` is `empirical` / `theory` / `review` / `qualitative` |
| `tier` | an **indicative bucket** (`top-5 econ`, `FT50 / UTD24`, `field`), never a ranking |
| `ranking_labels` | indexing labels (FT50, UTD24, CSSCI, CCF A …) recorded **only where the pack's own text asserts them**. Nothing bibliometric is inferred, and an empty cell means "not asserted here", not "not indexed". |
| `scope_keywords` | the 40 most venue-distinctive terms, by TF-IDF over the venue's own scope prose. **Derived, not curated** — a hit is a reason to open the profile, not a fit judgement. Chinese terms are filtered through a vocabulary discovered from the corpus (cohesion + boundary entropy) so that cross-boundary fragments never reach the index. |
| `pack_dir`, `profile_path`, `source_map` | where to read more |

## Design principle (no fact duplication / no drift)

The index holds only **stable** attributes. Everything volatile — APC/fees, acceptance
and desk-reject rates, turnaround, page limits, data-and-code policy — stays in each
pack's `resources/official-source-map.md`, which the live-check campaign keeps current.
The matcher reads those at match time. This keeps a single source of truth and avoids
the journal-match layer drifting out of date.

The same rule governs freshness metadata: [`.maintenance/FRESHNESS.md`](../../.maintenance/FRESHNESS.md)
derives each pack's `last_verified` date by **parsing the source map's own prose**
rather than storing a second copy free to drift (`python3 tools/freshness_audit.py`).

## How to use

1. An agent (or a pack's `*-workflow` router) facing a "which journal?" question loads
   [`journal-match.md`](journal-match.md) and follows the six steps. The triggerable
   entry point is `rt-journal-match` in `Research-Toolkit-Skills`.
2. It writes the [paper profile](paper-profile.md) once, runs
   `tools/match_venues.py`, then opens each candidate's `source_map` (depth) or
   `profile_path` (breadth) for the real judgement and the live facts.
3. After a reject, it seeds the downgrade ladder from [`ladder.tsv`](ladder.tsv), prices
   it with `tools/ladder_ev.py` (`rt-ladder-ev`), and hands the chosen rung to
   `rt-venue-reframe` for the rewrite plan.
4. If the right venue turns out to be **outside** the index, it says so and routes to
   `rt-venue-integrity` rather than forcing a poor fit.

## Regenerating

```bash
python3 tools/gen_venue_index.py              # venue-index.tsv + scope-postings.tsv
python3 tools/gen_ladder.py                   # ladder.tsv + discipline-adjacency.tsv
python3 tools/build_eval_set.py               # eval/gold-set.tsv (reads the index)
python3 tools/fetch_abstracts.py              # eval/abstract-terms.tsv (network; optional)
python3 tools/eval_journal_match.py --write   # eval/RESULTS.md
python3 tools/gen_catalog.py                  # CATALOG.md + catalog.json
```

Order matters — the ladder, the gold set and the catalog all read the index. Each
generator except `fetch_abstracts.py` takes `--check`, which CI uses to fail on a stale
committed file. `fetch_abstracts.py` needs the network and is therefore run by hand; CI
reads its committed output and never fetches.

To reclassify a venue, edit the `DISC` / `TIER` / `THEORY` / `CHINA` maps in
[`tools/venue_lib.py`](../../tools/venue_lib.py) and regenerate — never hand-edit the
generated TSVs.

---
*Part of the cross-journal capability layer alongside
[`../empirical-methods/`](../empirical-methods/). Discipline/tier are curated annotations;
fit and all volatile facts defer to each pack's own skills and source-map.*
