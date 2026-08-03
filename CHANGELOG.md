# Changelog

All notable changes to this repository. Versions apply to the plugin packs, which are
released together — every first-party pack carries the same version so that
`/plugin install` never leaves a user with a mixed-vintage set.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); this
project uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] — 2026-08-03

First stable release. The catalogue, the audits and the cross-journal capability layer
are considered stable enough to depend on; all 299 first-party packs move from `0.1.0`
(and assorted `0.2.0` / `0.3.0`) to a single `1.0.0`.

### Added

- **Venue index covering the whole repository.** `venue-index.tsv` grew from 289 rows
  (depth packs only) to **743 venues** by indexing the discipline bundles' per-venue
  profiles, which previously existed only as prose and so could not be shortlisted or
  ranked. Cross-tier duplicates are resolved by name/acronym identity, not by slug.
- **Richer, retrieval-ready index columns.** `scope_keywords` (TF-IDF over each venue's
  own scope prose), `coverage`, `venue_type`, `profile_path`, and `ranking_labels` —
  the last recorded only where the pack's own text asserts a label, never inferred.
- **`ladder.tsv`** — a 1,725-edge venue-adjacency graph built from the venues each
  pack names as siblings or alternatives, so the resubmission ladder starts from
  evidence rather than improvisation.
- **A measurable floor under journal matching.**
  `shared-resources/journal-selection/eval/` ships a 1,738-paper gold set harvested
  from the packs' own verified exemplar libraries, plus a deterministic harness that
  scores the candidate-generation step (recall@k, MRR, per-discipline breakdown). CI
  enforces a recall floor, so an index regression fails the build.
- **`rt-venue-reframe`** — turns a manuscript framed for one venue into one framed for
  another, diffing contribution claim, introduction arc, evidence bar, house style and
  policy across both venues' packs.
- **`rt-desk-reject-risk`** — scores a draft against the target venue's *own*
  documented desk-reject triggers (456 of 743 venues publish them) and returns a
  cost-ranked fix list.
- **`CATALOG.md` + `catalog.json`** — a browsable and a machine-readable index of every
  venue with its install target, generated from the same index the matcher reads.
- **`.maintenance/FRESHNESS.md` + `tools/freshness_audit.py`** — makes the
  "grounded in official sources" claim auditable by deriving each pack's
  `last_verified` date from its own source-map prose, with age gates available in CI.

### Changed

- All first-party pack versions normalised to `1.0.0` across `plugin.json`, each pack's
  `marketplace.json`, and the root marketplace, via the new `tools/set_version.py`.
- `rt-journal-match` and `rt-workflow` updated for the wider index, the ladder, and the
  two new steps in the lifecycle.
- `tools/gen_venue_index.py` rewritten; shared classification and text-extraction logic
  factored into `tools/venue_lib.py`.

### Fixed

- Chinese venue display names no longer carry the `《刊名》投稿（slug）` boilerplate.
- CJK keyword extraction no longer emits cross-boundary fragments in place of words.
- Parenthetical acronyms are matched against the venue's own name before being treated
  as an alias — previously "Anesthesiology (ASA)" made every venue mentioning the
  American Sociological Association look adjacent to it.

### Notes

- The venue index still holds **no volatile facts** by design. Fees, acceptance rates,
  turnaround and page limits live in each pack's `resources/official-source-map.md` and
  are read at match time.
- `tier` remains an indicative bucket, not a ranking or a bibliometric claim.

## [0.1.0] — 2026-05 to 2026-07

Initial public development: 299 packs and 4,152 skills across 522 journals and 155+
CS/AI conferences, the nine discipline breadth bundles, the cross-journal
`Research-Toolkit-Skills`, the `shared-resources/` capability layer, and the repository
audit suite (`tools/run_checks.py`) wired into CI.
