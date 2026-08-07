# Changelog

All notable changes to this repository. Versions apply to the plugin packs, which are
released together — every first-party pack carries the same version so that
`/plugin install` never leaves a user with a mixed-vintage set.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); this
project uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] — 2026-08-08

Journal selection stops being a method an agent improvises over a TSV and becomes a
command with a measured error rate. Recall@10 for the true venue, from a bare title,
goes from **27.7% to 40.5%** on a newly held-out half of the gold set.

### Added

- **`tools/match_venues.py`** — step 2 of the journal-match method, executable.
  Ranks all 743 venues against a paper's title and abstract, prints where to read each
  candidate and which terms it matched, and takes `--discipline` (a **prior**, not a
  filter), `--only-discipline`, `--lane` / `--region` / `--venue-type` / `--coverage`,
  `--exclude` for venues that already rejected the paper, and `--json`.
- **`tools/match_lib.py`** — the shared retrieval layer. `match_venues.py` and
  `eval_journal_match.py` both go through it, so the published number now describes the
  code an author actually runs. Previously the harness re-implemented its own keyword
  overlap that nothing else used.
- **`scope-postings.tsv`** — a 300-term-deep inverted index behind the matcher. The
  human-readable `venue-index.tsv` keeps its 40 terms per venue; the term a given paper
  shares with its venue is usually not in the top forty, which was the single largest
  cause of misses.
- **`discipline-adjacency.tsv`** — which disciplines routinely stand in for one another,
  collapsed from the venue graph. A labour paper now reaches general economics and
  public economics automatically instead of relying on the agent to remember to widen.
- **`rt-ladder-ev` + `tools/ladder_ev.py`** — cost a submission *sequence*, not a venue:
  expected months, P(placed), P(ladder exhausted), with a sensitivity band, because
  `p_accept` is a judgement and not a measurement. The sequence is what spends a year.
- **`rt-venue-integrity`** — the escape hatch for the coverage-honesty rule. When the
  right venue is outside the index, a source-by-source verification protocol (indexing,
  publisher, editorial board, fees, retractions) with each finding attributed to a
  primary source. It ships no predatory list and applies no label; it reports checks.
- **`paper-profile.md`** — the five signals of step 1, written once and read by every
  downstream skill instead of each re-deriving them from the manuscript and quietly
  disagreeing.
- **A dev/test split on the gold set**, assigned by a hash of each paper's title. The
  matcher's four weighting constants are tuned on `dev`; every figure in
  `eval/RESULTS.md` is computed on `test`, and both halves are printed side by side.
- **`tools/fetch_abstracts.py`** — resolves gold papers against OpenAlex and commits a
  sorted, stopword-filtered **term bag** per abstract (not the abstract), for the
  realistic `title+abstract` configuration. Network-dependent and therefore never run by
  CI; resumable, and it refuses to record a rate-limit response as "no abstract found".
- **A wrong-lane precision metric** — the share of top-10 slots given to a venue that
  publishes no empirical work, for a paper whose true venue does. Recall alone said
  nothing about the obviously wrong suggestions an author notices first.

### Changed

- **Scope text now covers every skill in a pack**, not only the four "fit" skills. A
  methods skill names the designs a venue accepts and a review-process skill names what
  its referees ask about; both were being discarded. The exemplar library remains
  excluded, since it is the label source for the eval.
- **Chinese scope terms are filtered through a vocabulary discovered from the corpus**
  (recurrence + internal cohesion + boundary entropy) instead of storing every generated
  n-gram. TF-IDF ranks terms; it cannot tell a word from a fragment, and fragments
  scored *well* precisely because they were rare — `融学院主`, sliced out of `金融学院主办`,
  was indexed as though it were a term.
- **Skill slugs, URLs and submission-process boilerplate no longer reach the index.**
  `qje-identification` and `neurips-submission` are the most TF-IDF-distinctive strings
  in a pack and are worthless for matching; they were taking roughly half of every
  English pack's keyword budget.
- **The retrieval floor in CI rises from 22% to 36%**, measured on the held-out half.
- **The quality scorecard's toolkit size band** widens from 5–10 to 5–14 skills. The
  upper bound had been set to the toolkit's size at the time plus one, so the first
  genuine additions to the lifecycle registered as sprawl.

### Fixed

- **Two alias-collision bugs in the resubmission-ladder graph.** Venue aliases were
  counted with a plain substring search, so *TAR* matched inside **STAR**D and every
  radiology pack looked adjacent to The Accounting Review, while *ISS* matched inside
  **ISS**N and half the economics packs looked adjacent to ACM ISS. Latin aliases now
  require non-alphanumeric boundaries: **218 spurious edges removed** (1,725 → 1,507),
  and the share of same-discipline edges rose from 51% to 59%.
- **A configuration that covers too little of the eval split is now withheld** rather
  than published beside one that covers all of it.

### Corrections to 1.0.0

- 1.0.0 stated that "CJK keyword extraction no longer emits cross-boundary fragments in
  place of words." That was an overclaim. The change it referred to was a scoring bonus
  for longer n-grams, which makes fragments *rarer* in the ranking but cannot exclude
  them — `融学院主` was still in the shipped index. The vocabulary filter described above
  is what actually excludes them.

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
