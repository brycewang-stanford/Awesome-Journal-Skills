# Maintenance Tools

These scripts are dependency-free Python tools for repository maintenance. They
are designed to run on a fresh clone of the repository.

## Hard Gates

| Tool | Purpose | Typical command |
|------|---------|-----------------|
| [`run_checks.py`](run_checks.py) | Runs the standard local hard gates: Python syntax check, repository count tripwires, quality floor, and clone audit, plus a whitespace check. By default it also runs report-only source-map and root-card audits. CI uses `--skip-reports` so warnings stay advisory and the hard gate stays fast. | `python3 tools/run_checks.py` |
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
| [`quality_scorecard.py`](quality_scorecard.py) | Scores every first-party pack 0–100 on objective quality dimensions. It distinguishes single-venue `depth` packs, compressed AI-conference `conference` packs, and large `breadth` bundles: depth packs get credit for code/worked examples/exemplars, conference packs use a shorter skill-body target, and breadth bundles get credit for routers, rosters/source maps, worked routing cases, and selection patterns. The `unit` column is cross-language: Latin/technical tokens count as one unit and two CJK characters count as one unit. Venue-cue checks use pack names plus common skill-directory prefixes such as `jbf`, `ectj`, or `red`. `code=n/a` means the pack's resources explicitly explain why runnable econometric code is not discipline-appropriate. `--top N` shows the lowest scorers; `--show-skills` names the thinnest files inside each displayed pack; `--json` for diffing the trajectory over time; `--min-score` can gate a focused cleanup. | `python3 tools/quality_scorecard.py --top 20 --show-skills` |
| [`external_link_audit.py`](external_link_audit.py) | Reports liveness for external official/publisher/submission URLs cited in first-party Markdown. It is network-dependent and advisory: 404/410 are actionable, while 401/403/429 and timeouts usually need manual recheck. Results are cached under `tools/.cache/`; `--cache-summary --json` reads that cache and URL inventory without making network requests, including current cache coverage and orphaned cache rows. | `python3 tools/external_link_audit.py` |
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
| [`gen_venue_index.py`](gen_venue_index.py) | Regenerates `shared-resources/journal-selection/venue-index.tsv` — the stable index of all 743 venues (289 depth packs + 454 breadth-bundle profiles, cross-tier duplicates resolved by name/acronym identity). Emits stable fields only (coverage / type / discipline / tier / lane / region / derived `scope_keywords` / pointers) — never volatile fees or acceptance, which stay in each pack's `official-source-map.md`. `ranking_labels` records only labels a pack's own text asserts. | `python3 tools/gen_venue_index.py` |
| [`gen_ladder.py`](gen_ladder.py) | Regenerates `ladder.tsv`, the venue-adjacency graph behind the resubmission ladder, from the venues each pack names as siblings or alternatives. Candidate adjacency, not a ranking. | `python3 tools/gen_ladder.py` |
| [`build_eval_set.py`](build_eval_set.py) | Harvests the `(paper → venue)` gold set from the depth packs' verified exemplar libraries into `eval/gold-set.tsv`. | `python3 tools/build_eval_set.py` |
| [`eval_journal_match.py`](eval_journal_match.py) | Scores the matcher's candidate-generation step against that gold set (recall@k, MRR, per-discipline) and writes `eval/RESULTS.md`. `--min-recall-at-10` is the CI floor that turns an index regression into a failing build. | `python3 tools/eval_journal_match.py --write` |
| [`gen_catalog.py`](gen_catalog.py) | Regenerates the browsable `CATALOG.md` and machine-readable `catalog.json` — every venue by discipline with its install target. | `python3 tools/gen_catalog.py` |
| [`freshness_audit.py`](freshness_audit.py) | Regenerates `.maintenance/FRESHNESS.md` by **parsing** each source map's own access/verification dates (no second copy to drift). `--max-age-days` / `--max-unknown` turn it into a gate; the weekly CI job runs it advisory. | `python3 tools/freshness_audit.py --write` |
| [`set_version.py`](set_version.py) | Writes one version across every manifest a pack owns plus the root marketplace — the four places `audit_repo.py` requires to agree. | `python3 tools/set_version.py --set 1.0.0` |

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
