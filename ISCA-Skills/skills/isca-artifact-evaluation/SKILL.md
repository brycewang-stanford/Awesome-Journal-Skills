---
name: isca-artifact-evaluation
description: Use when preparing an accepted ISCA paper's artifact for evaluation under the ACM Review and Badging policy — scoping which results are reproducible within evaluator budgets, packaging simulator-heavy workflows others can run, writing the evaluator-facing appendix, and earning badges that print on the paper.
---

# ISCA Artifact Evaluation

The verified 2026 arrangement: authors of **accepted** papers could voluntarily
submit artifacts, assessed under the **ACM Artifact Review and Badging** policy,
with earned badges printed on the paper and attached as ACM Digital Library
metadata — and with no effect on the acceptance decision itself. The conference
framed AE as a recent, deliberate import into the architecture community
(following ASPLOS from 2020 and MICRO from 2021). Voluntary does not mean
optional in practice: badges are becoming the community's default trust signal,
and an architecture paper without them increasingly gets asked why.

## Decide scope first: which claims does the artifact defend?

Architecture artifacts fail most often from over-promising. Before packaging,
split the paper's results three ways and say so in the artifact documentation:

| Tier | Contents | Evaluator experience |
|---|---|---|
| **Reproduce** | Headline figure(s) + key ablation, runnable on evaluator-accessible machines within hours | Runs it, matches within stated tolerance |
| **Regenerate-with-resources** | Full sweeps needing cluster-days; scripts and configs complete, cost stated honestly | Inspects, spot-runs a slice |
| **Inspect-only** | Anything needing hardware evaluators won't have (FPGA boards, silicon, internal traces) | Reads code + recorded raw outputs; verifies the pipeline from raw to figure |

Declaring tier boundaries up front converts "couldn't run everything" from a
failure into the documented plan. Never gate the Reproduce tier on proprietary
inputs — substitute an open workload subset and show it preserves the trend.

## Simulator-heavy artifacts: the specific frictions

- **Wall-clock honesty.** Cycle-level simulation of full suites is
  CPU-months; evaluators have days. Ship reduced-input or single-region variants
  of the headline experiment, with the full-run manifests alongside. State
  expected runtimes per step, measured, not guessed.
- **Build fragility.** Simulator trees with local patches break on new
  toolchains. Ship a container image with everything pre-built, *and* the
  from-source path for evaluators who distrust images.
- **Tolerance statement.** Define "match": bit-identical stats for
  deterministic runs; a stated percentage band where sampling or threading
  varies. An evaluator staring at 33.7% vs the paper's 34% needs the band in
  writing.
- **Third-party licenses.** SPEC-class suites cannot be redistributed; ship
  build recipes plus checksums, and include one freely redistributable workload
  so the pipeline is exercisable end to end regardless.

## The package an evaluator can drive blind

```text
artifact/
  README.md          # claims-to-experiments map; runtimes; tolerance bands
  INSTALL.md         # container route + source route, both tested cold
  run_all.sh         # Reproduce tier end to end, one command
  experiments/
    f07-headline/    # regen.sh + manifest.ini per figure (from
    f09-ablation/    #   isca-reproducibility — same manifests, reused)
  expected/          # our raw outputs + final CSVs, for diffing
  workloads/         # free subset included; licensed suite: recipe + checksums
  LICENSE
```

The README's first section is a **claims table**: paper claim → figure → command
→ expected output → tolerance. Evaluators grade against exactly this table;
making them reverse-engineer the mapping from the paper costs goodwill and,
frequently, a badge.

```bash
# Cold-start rehearsal — run on a machine that has never seen the project
docker load < artifact-image.tar.gz
docker run --rm -it artifact:v1 bash -lc './run_all.sh --tier reproduce'
diff <(csvcut -c workload,ipc results/f07.csv) \
     <(csvcut -c workload,ipc expected/f07.csv)   # within README tolerance?
```

Have a group member *outside the project* do this rehearsal before submission;
every question they ask is a missing README paragraph.

## The badge set under ACM's policy

The ACM Review and Badging framework distinguishes availability badging (the
artifact is permanently retrievable from an archival location) from functional
and results-oriented badging (the artifact works as documented; the paper's
results can be obtained with it). Practical mapping:

- **Availability** is cheap and unconditional: deposit the evaluated snapshot
  with a DOI-issuing archive (a lab GitHub alone is not archival). Do this even
  if you pursue nothing else.
- **Functionality** rides on documentation and the cold-start test.
- **Results reproduction** rides on the Reproduce tier's design: modest
  runtime, clear tolerance, deterministic where possible.

Which badges ISCA 2027 requests, the AE calendar, and the committee's platform
offerings (cloud credits, provided machines) are per-edition decisions — 待核实
against the 2027 AE page when it exists.

## Working with evaluators

Architecture AE is conventionally collaborative and iterative: evaluators hit a
wall, authors fix and resubmit within the AE window. Budget author-days for this
in the post-acceptance calendar (`isca-workflow`), respond within a day while
the evaluator's context is warm, and version every fix (`artifact:v1.1`,
changelog in the README) so the final badge attaches to an identifiable object.

## Timing and division of labor

AE happens in the same weeks as camera-ready preparation and talk writing.
Assign the artifact to someone who ran the original experiments — packaging is
recall-heavy — and start from the submission-time snapshot that
`isca-reproducibility` froze in November, not from the current dev tree, which
has drifted.

## Submission gate

- [ ] Claims table complete: every badge-relevant figure mapped to a command
- [ ] Cold-start rehearsal passed by a non-author on a clean machine
- [ ] Runtimes measured and stated per step; tolerance bands written
- [ ] Container + source routes both build
- [ ] Licensed workloads handled by recipe; free subset runs end to end
- [ ] Archival deposit made; DOI in the camera-ready's artifact statement

Venue facts verified 2026-07-08 (`../../resources/official-source-map.md`);
badge definitions follow ACM's published badging policy — check the version the
2027 AE chairs cite.
