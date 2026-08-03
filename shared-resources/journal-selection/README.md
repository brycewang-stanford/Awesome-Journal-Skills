# Journal-Selection — cross-journal matching capability

A venue-neutral capability layer that turns *"where should I send this paper?"* into a
ranked, reasoned shortlist across the whole repository. Complements the per-journal packs
(which answer *"how do I clear this venue's bar?"*) with the missing front-door question
*"which venue?"*.

## Contents

| File | What it gives an agent |
|---|---|
| [`journal-match.md`](journal-match.md) | The matching methodology: profile the paper (discipline / method / contribution / setting / ambition) → shortlist candidates from the index → score on Fit × acceptance-odds × turnaround × cost/policy × audience → return a reach/match/safe shortlist + a resubmission ladder. Reads volatile facts live from each pack's source-map. |
| [`venue-index.tsv`](venue-index.tsv) | **Stable** index of **743 venues** — every venue the repository covers, whether as a depth pack or as a profile inside a discipline bundle. |
| [`ladder.tsv`](ladder.tsv) | **1,725 adjacency edges** for the resubmission ladder: which venues each pack names as siblings or alternatives, with a mention count and a same-discipline flag. Candidate adjacency, not a ranking. |
| [`eval/`](eval/README.md) | A 1,738-paper gold set and a harness that scores the candidate-generation step, so an index regression shows up as a failing number rather than a quietly worse recommendation. |

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
| `scope_keywords` | terms derived by TF-IDF from each venue's own scope prose. **Derived, not curated** — a hit is a reason to open the profile, not a fit judgement. |
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
2. It filters [`venue-index.tsv`](venue-index.tsv) by discipline / lane / region /
   venue_type, narrows on `scope_keywords`, then opens each candidate's `source_map`
   (depth) or `profile_path` (breadth) for the real judgement and the live facts.
3. After a reject, it seeds the downgrade ladder from [`ladder.tsv`](ladder.tsv) and
   hands the chosen rung to `rt-venue-reframe` for the rewrite plan.

## Regenerating

```bash
python3 tools/gen_venue_index.py              # venue-index.tsv
python3 tools/gen_ladder.py                   # ladder.tsv        (reads the index)
python3 tools/build_eval_set.py               # eval/gold-set.tsv (reads the index)
python3 tools/eval_journal_match.py --write   # eval/RESULTS.md
python3 tools/gen_catalog.py                  # CATALOG.md + catalog.json
```

Order matters — the ladder, the gold set and the catalog all read the index. Each
generator also takes `--check`, which CI uses to fail on a stale committed file.

To reclassify a venue, edit the `DISC` / `TIER` / `THEORY` / `CHINA` maps in
[`tools/venue_lib.py`](../../tools/venue_lib.py) and regenerate — never hand-edit the
generated TSVs.

---
*Part of the cross-journal capability layer alongside
[`../empirical-methods/`](../empirical-methods/). Discipline/tier are curated annotations;
fit and all volatile facts defer to each pack's own skills and source-map.*
