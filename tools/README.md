# Maintenance Tools

These scripts are dependency-free Python tools for repository maintenance. They
are designed to run on a fresh clone of the repository, with no virtualenv and
nothing to install.

**Python 3.9 or newer.** Every tool and the whole unit suite are verified on 3.9,
and CI runs the hard gate on both 3.9 and current Python so the floor stays real —
stdlib-only is worth little if the scripts quietly need last year's syntax.

## Hard Gates

| Tool | Purpose | Typical command |
|------|---------|-----------------|
| [`run_checks.py`](run_checks.py) | Runs the standard local hard gates: the unit suite, a Python syntax check, repository invariants, pack conformance, and the clone audit, plus the generator `--check` runs, the freshness and conference-cycle gates, the subject-vocabulary index check, the retrieval floor and a whitespace check. By default it also runs report-only source-map and root-card audits. CI uses `--skip-reports` so warnings stay advisory and the hard gate stays fast. | `python3 tools/run_checks.py` |
| [`tests/`](tests/) | Offline unit tests for the tools themselves — the text layer (`venue_lib`), the retrieval layer (`match_lib`), the ladder arithmetic (`ladder_ev`), the abstract harvester's declined-vs-absent rule (`fetch_abstracts`), the freshness parser, the ladder's alias matcher, the eval harness's split and coverage rules, the venue-topic resolver's exact-match rules, the documented-count reconciliation, and the hero-asset guard. Stdlib `unittest`, no network, under a second. They build their own fixtures rather than reading the committed index: a test that reads generated data cannot tell "the code is right" from "the code and the committed output are wrong in the same way", which is precisely the gap the `--check` generators leave. | `python3 -m unittest discover -s tools/tests -t tools` |
| [`audit_repo.py`](audit_repo.py) | Validates repository invariants: skill counts, pack counts, root marketplace coverage, root journal entries, plugin metadata, required source maps, frontmatter, local Markdown links, and external-import policy. | `python3 tools/audit_repo.py` |
| [`clone_audit.py`](clone_audit.py) | Finds likely find-replace skill clones. CI reports near-clones at 0.75 and fails only at 0.90. | `python3 tools/clone_audit.py --threshold 0.75 --fail-threshold 0.90 --top 20` |

## Report-Only Tools

These tools exit 0 by default when they report warnings, and still exit non-zero
for argument or runtime errors. Use `--strict` only when a focused cleanup batch
should fail on warnings.

| Tool | Purpose | Typical command |
|------|---------|-----------------|
| [`source_map_audit.py`](source_map_audit.py) | Reports first-party `resources/official-source-map.md` files with missing source URLs, missing visible check dates, thin content, and heavy unresolved-flag loads. | `python3 tools/source_map_audit.py` |
| [`root_entry_audit.py`](root_entry_audit.py) | Reports progress and source-anchor gaps for the 200 root journal-entry cards. | `python3 tools/root_entry_audit.py` |
| [`quality_scorecard.py`](quality_scorecard.py) | Two measurements per pack. **Conformance** is pass/fail and is the gate: both READMEs, a resources README, a source anchor, worked examples, exemplars, a code library or a stated reason there is none, a skill count inside its role's band, every description saying when to use the skill and naming its venue, and every skill carrying a worked block. `--require-conformance` makes it a failing build, and `run_checks.py` runs it that way. **Backlog score** (0-100) ranks what is left to do using only dimensions that still vary across packs: source-map currency, unresolved-fact load, the depth of the pack's *thinnest* skill, how far that skill sits below the pack's own average, and execution-bridge wiring where the bridge's stack is the discipline's stack. That last denominator has two conditions, and it used to have one: a pack needs a code library *and* a discipline whose empirical work runs on StatsPAI/Stata (`venue_lib.uses_econometric_execution`). Shipping code was enough until August 2026, which put 90 AI conferences and 10 Chinese CS journals in the denominator and docked them up to ten points for not wiring a DiD/IV/RDD stack to PyTorch and EDA work — they were, between them, every unwired pack in the repository, which is how the mis-scoping surfaced. It is a ranking, not a standard. The two were one number until August 2026, when five of its six dimensions sat at maximum for 299 of 299 packs and the "quality score" was arithmetically `94 + freshness`; the table now prints its own dimension saturation so the next flatlining dimension is visible before it stops measuring. Roles are distinguished throughout — single-venue `depth` packs, compressed AI-conference `conference` packs, large `breadth` bundles, and the cross-journal `toolkit` — each with its own substance target and structural band. The `unit` and `thin` columns are cross-language: Latin/technical tokens count as one unit and two CJK characters count as one unit. `--top N` shows the packs with the most work left; `--show-skills` names the thinnest files inside each; `--json` for diffing the trajectory over time. | `python3 tools/quality_scorecard.py --top 20 --show-skills` |
| [`external_link_audit.py`](external_link_audit.py) | Reports liveness for external official/publisher/submission URLs cited in first-party Markdown. It is network-dependent and advisory: 404/410 are actionable, while 401/403/429 and timeouts usually need manual recheck. Results are cached under `tools/.cache/`; `--cache-summary --json` reads that cache and URL inventory without making network requests, including current cache coverage and orphaned cache rows. `--write` regenerates `.maintenance/DEAD-LINKS.md`, the actionable half as a queue with each citing file named. URL extraction handles non-ASCII paths (a citation with a Chinese path used to be truncated at the first non-Latin byte and reported dead) and skips elided template URLs such as `https://arxiv.org/abs/...`. | `python3 tools/external_link_audit.py` |
| [`live_check_fetch.py`](live_check_fetch.py) | Fetches the `.maintenance/LIVE-CHECK-URLS.txt` target pages and prints readable page text for source-map re-verification. The build sandbox's egress policy denies most journal/publisher domains, so this is meant to run on a GitHub Actions runner (via the `live-check` workflow) where those domains are reachable; the fetched text lands in the job log for a maintainer or agent to act on. Report-only: never edits files or fails the build. | `python3 tools/live_check_fetch.py` |

## Updating the inventory tripwires

`audit_repo.py` hard-codes the expected skill/pack/root-entry counts so accidental
bulk deletions fail CI. When you intentionally add or remove packs, refresh the
three `EXPECTED_*` constants (and the README badges) in the same commit:

```bash
python3 tools/audit_repo.py --counts   # prints the live numbers to copy in
```

## Generators

All generators accept `--check`, which exits non-zero when the committed output
differs from a fresh build. `run_checks.py` runs them that way, so a new pack cannot
silently leave the matcher, the ladder, the eval or the catalog behind. Shared
classification and text-extraction logic lives in [`venue_lib.py`](venue_lib.py) —
edit the `DISC` / `TIER` / `THEORY` / `CHINA` maps there to reclassify a venue, never
the generated files.

Run them in this order; each reads the one above it.

| Tool | Purpose | Typical command |
|------|---------|-----------------|
| [`gen_venue_index.py`](gen_venue_index.py) | Regenerates `shared-resources/journal-selection/venue-index.tsv` — the stable index of all 744 venues (290 depth packs + 454 breadth-bundle profiles, cross-tier duplicates resolved by name/acronym identity) — **and** `scope-postings.tsv`, the 900-term-deep inverted index the matcher searches. Emits stable fields only (coverage / type / discipline / tier / lane / region / derived `scope_keywords` / pointers) — never volatile fees or acceptance, which stay in each pack's `official-source-map.md`. `ranking_labels` records only labels a pack's own text asserts. | `python3 tools/gen_venue_index.py` |
| [`gen_ladder.py`](gen_ladder.py) | Regenerates `ladder.tsv`, the venue-adjacency graph behind the resubmission ladder, from the venues each pack names as siblings or alternatives, plus `discipline-adjacency.tsv`, the same graph collapsed by discipline (which widens the matcher's discipline prior). Candidate adjacency, not a ranking. | `python3 tools/gen_ladder.py` |
| [`build_eval_set.py`](build_eval_set.py) | Harvests the `(paper → venue)` gold set from the depth packs' verified exemplar libraries into `eval/gold-set.tsv`, assigning each paper to a `dev` or `test` split by a hash of its title. | `python3 tools/build_eval_set.py` |
| [`fetch_abstracts.py`](fetch_abstracts.py) | Resolves gold papers against Crossref, then Europe PMC, then arXiv, and stores a sorted, stopword-filtered **term bag** per abstract (not the abstract) in `eval/abstract-terms.tsv`, powering the realistic `title+abstract` configuration. No single free source covers this gold set: Crossref is broad but only where the publisher deposited an abstract, Europe PMC is near-complete for medicine and the life sciences, arXiv reaches the CS and physics preprints that Crossref misses. OpenAlex has the best coverage of the four and now **bills per request**, so it is opt-in via `--source all`. The invariant that matters: a source that *declines* (401/402/403/429/5xx/timeout) has said nothing about the paper and is never cached as a miss — folding a decline into "no abstract" is how a throttled run quietly produces a small, biased corpus that looks complete. **Network-dependent, so it is never run by CI** — its output is committed and CI reads the file. Resumable: rerun to fill gaps. | `python3 tools/fetch_abstracts.py` |
| [`fetch_venue_topics.py`](fetch_venue_topics.py) | Builds the **subject** half of the venue vocabulary: `venue-sources.tsv` (which bibliographic source each venue resolved to, and by which rule) and `topic-postings.tsv` (a ranked TF-IDF vocabulary per venue over the titles of articles it actually published). It exists because the scope index is derived from prose about a *process* while a query is about a *subject*, so a venue whose scope terms are all review mechanics was unreachable from any paper title. Free sources by venue type — Crossref for journals, DBLP for conference series — with OpenAlex opt-in on the same reasoning as `fetch_abstracts.py` (it bills per request). Resolution is **exact after normalisation or it does not happen**: a fuzzy venue match does not degrade a ranking, it fills a venue's vocabulary with another venue's subjects, and the rule that fired is recorded per row so a wrong mapping is reviewable. Gold-set titles are dropped from the harvest and the count is published in the postings header. **Network-dependent, so CI never runs the harvest** — `--check` is offline and only verifies that the committed postings still describe the current venue ordering. | `python3 tools/fetch_venue_topics.py --resolve --harvest` |
| [`eval_journal_match.py`](eval_journal_match.py) | Scores the matcher's candidate-generation step against that gold set (recall@k, MRR, wrong-lane precision, per-discipline) and writes `eval/RESULTS.md`. It goes through `match_lib.py`, so it measures the code `match_venues.py` runs rather than a private re-implementation. Reported on the held-out `test` half; `--min-recall-at-10` is the CI floor that turns an index or matcher regression into a failing build. | `python3 tools/eval_journal_match.py --write` |
| [`gen_catalog.py`](gen_catalog.py) | Regenerates the browsable `CATALOG.md` and machine-readable `catalog.json` — every venue by discipline with its install target. | `python3 tools/gen_catalog.py` |
| [`freshness_audit.py`](freshness_audit.py) | Regenerates `.maintenance/FRESHNESS.md` by **parsing** each source map's own access/verification dates (no second copy to drift). `--max-age-days` / `--max-unknown` turn it into a gate; the weekly CI job runs it advisory. | `python3 tools/freshness_audit.py --write` |
| [`cycle_audit.py`](cycle_audit.py) | Regenerates `.maintenance/CYCLE-CURRENCY.md`: for each of the 90 conference packs, **which edition** its source map describes. Freshness and currency are different properties for a conference, and only one of them was being checked — a conference's page caps, chairs, tracks and review phases belong to one edition (AAAI-26, CCS 2027) and are replaced wholesale by the next call, so a pack can be re-read last month, be accurate, and still describe a cycle that closed before the reader arrived. That is what issue #3 reported. The edition label is **parsed** from the pack's own prose, anchored to the venue's acronym (aliases in `venue_lib.CONFERENCE_ALIASES`) so "CCS 2027" reads as an edition and a copyright year does not. Four states: `current`, `due` (this year's edition, no stated date still ahead — a live check, not an error), `stale` (a past edition; `--max-stale 0` is the hard gate in `run_checks.py`), and `retired` (the map itself says the venue stopped running, as `IPSN-Skills` does — a last edition in the past is then correct). Like the freshness dashboard, it stores only stable fields so CI can byte-check it. | `python3 tools/cycle_audit.py --write` |
| [`set_version.py`](set_version.py) | Writes one version across every manifest a pack owns plus the root marketplace — the four places `audit_repo.py` requires to agree. | `python3 tools/set_version.py --set 1.0.0` |

## Author-Facing Tools

Unlike everything above, these are run *by an agent while helping an author*, not by a
maintainer. They read only committed data and make no network calls.

| Tool | Purpose | Typical command |
|------|---------|-----------------|
| [`match_venues.py`](match_venues.py) | Step 2 of the journal-match method: rank the 744 indexed venues against a paper's title and abstract. `--discipline` is a prior (widened by `discipline-adjacency.tsv`), not a filter; `--only-discipline` hard-filters, `--exclude` drops venues that already rejected the paper, `--json` pipes. Prints where to read each candidate and which terms it matched, so a nonsense hit is visible as one, and warns when the leading candidates rest on one or two words or when nothing in the named discipline matched at all. Retrieval only — the recommendation still comes from reading each venue's pack. | `python3 tools/match_venues.py --title "..." --abstract "..." --discipline finance` |
| [`ladder_ev.py`](ladder_ev.py) | Step 6: cost a submission *sequence*. Given each rung's `p_accept` and months-to-decision, returns expected months, P(placed), P(ladder exhausted), and a sensitivity band — because `p_accept` is a judgement, not a measurement. | `python3 tools/ladder_ev.py --rung "A:0.06:4.5" --rung "B:0.2:3.0"` |
| [`match_lib.py`](match_lib.py) | Not a CLI: the shared retrieval layer both `match_venues.py` and `eval_journal_match.py` go through. The weighting constants live here and are tuned on the gold set's `dev` half only. | — |

## Asset Rendering (Node)

Unlike the Python maintenance scripts above, [`render_posters.mjs`](render_posters.mjs)
is a Node + Playwright helper for regenerating poster/social images from an HTML
deck. It screenshots every `<article class="poster" id="poster-NN">` in the deck
to PNG at native 1080×1920, saved at 2× (2160×3840), and is meant to be re-run
after editing the HTML to refresh the exported PNGs.

```bash
node tools/render_posters.mjs                       # default AJS Xiaohongshu deck
node tools/render_posters.mjs <deck.html>           # custom HTML, PNGs next to it
node tools/render_posters.mjs <deck.html> <outDir>  # custom output dir
```

Requires a global Playwright (`npm i -g playwright`); the script resolves it from
the global module root automatically. If no Chromium is cached, run
`npx playwright install chromium` once.

## Python Syntax Check

Run this after editing any script in this directory:

```bash
python3 -m py_compile tools/*.py
```
