---
name: nsdi-artifact-evaluation
description: Use when preparing an accepted NSDI paper's artifact for badge evaluation — packaging code, traces, and testbed recipes for the AEC, choosing which badges to pursue, choosing among Artifacts Available / Functional / Results Reproduced, meeting Zenodo-style permanence expectations, hitting the per-cycle artifact deadlines, and timing public release to stay eligible for the Community Award.
---

# NSDI Artifact Evaluation

Artifact evaluation at NSDI is post-acceptance and opt-in: accepted authors package
what the paper is made of, an Artifact Evaluation Committee tries it, and earned
badges travel with the paper. Mechanics below follow the NSDI '27 Call for Artifacts
as re-verified on 2026-11-24; reread the live page after acceptance.

## What the '27 call establishes

- Evaluation is **open to all accepted papers**, optional, and starts only **after**
  acceptance decisions — it does not influence acceptance (yet; the call says the AEC
  may one day advise the PC).
- **Three separate badges**; a paper may earn one, two, or all three:
  **Artifacts Available** (permanently and publicly retrievable — Zenodo with a DOI
  encouraged; institutional and third-party repositories also valid), **Artifacts
  Functional** (documentation, completeness, exercisability), and **Results
  Reproduced** (the AEC independently obtains the paper's main results within
  tolerance).
- **Authors choose** which badges the AEC should consider at artifact-submission
  time, and cannot change the URL/archive or badge selection after the deadline.
- Two-step submission on per-cycle AE HotCRP sites (`nsdi27springae` /
  `nsdi27fallae`): register the accepted paper's abstract, PDF, topics and conflicts,
  then submit a stable URL or archive.
- '27 timeline: spring cycle artifacts due **August 7, 2026** (11:59 PM US PDT),
  decisions **October 13, 2026**, final papers October 20, 2026; fall cycle artifacts
  due **December 18, 2026** (11:59 PM US PST), decisions **February 19, 2027**, final
  papers March 4, 2027. The gap between a fall acceptance (December 8) and the artifact
  deadline is ten days — start packaging while the paper is under review, as the call
  itself advises.
- Evaluation is **single-blind**: evaluators know the authors, not vice versa — keep
  analytics and tracking off artifact sites during the window.

## Choose badges like claims

The badge menu is a claims menu; over-claiming wastes AEC goodwill exactly as
over-claiming in the paper wastes reviewer goodwill.

| You can honestly promise | Pursue | Do not pursue |
|---|---|---|
| The bits are public forever (DOI'd archive) | Available | — |
| An evaluator can build and run the core on documented hardware | + functionality-level badge | results claims tied to your production traces |
| Headline figures regenerate within characterized variance on accessible hardware | + reproduction-level badge | anything requiring your private fleet |

The networked-systems complication: results badges collide with topology dependence.
If p99.9 numbers need 80 nodes and a specific RTT matrix, ship a **documented
downscaled configuration** with expected outputs at that scale, and say explicitly
which paper trends survive downscaling and which do not (`nsdi-reproducibility`).

## The Community Award changes your timeline

NSDI's Community Award goes to the best paper whose **code and/or dataset is made
publicly available by the final-papers deadline**. Note the trigger: not badge
completion — *public release by camera-ready time*. Teams that treat openness as a
post-AE cleanup task silently exit the running. If the artifact will be public
anyway, make it public early enough to count (`nsdi-camera-ready`).

## Package for a stranger with a deadline

AEC members evaluate many artifacts on volunteer time. The artifact that wins is the
one where the first fifteen minutes succeed:

```text
artifact/
  README.md            # claims -> badge(s) sought; hardware/software needs up front
  GETTING_STARTED.md   # <=30 min smoke path: build, tiny topology, one sanity result
  CLAIMS.md            # paper claim -> experiment -> script -> expected output ± variance
  setup/               # topology recipes: containers/CloudLab profile/VM configs
  traces/              # shippable traces or synthetic generators + fidelity notes
  experiments/<id>/    # one runnable unit per paper experiment (run.sh + provenance)
  figures/Makefile     # regenerate paper figures from logs (fresh or shipped)
LICENSE                # explicit license; unlicensed code is not "available"
```

NSDI-specific packaging notes:

- **State the variance.** Tail-latency reproduction is stochastic; publish the spread
  you observed so the evaluator can tell noise from failure.
- **Solve the testbed problem for them**: a public-testbed profile (e.g., CloudLab)
  or an emulated topology beats instructions that assume your lab's switches.
- **Trace substitutions documented**: where production data cannot ship, the synthetic
  stand-in's construction and its fidelity limits are part of the artifact, not a
  footnote.
- **Kernel/NIC settings pinned** — the classic source of "works for authors only."

## Dry-run protocol before submission

The single highest-yield hour: a lab member who did not build the artifact follows
`GETTING_STARTED.md` on a machine you did not prepare.

1. Fresh VM or container, no lab dotfiles, no cached dependencies.
2. Stopwatch on: record where the reader stalls, every undocumented assumption, and
   the wall-clock to first sanity result.
3. Fix the artifact, not the reader — each stall becomes a README line or a setup
   script, then re-run with a second novice if anything structural changed.

## Process notes

- By artifact-submission time you provide a stable URL or uploaded archive; from
  there, treat the artifact as frozen except through communication with the AEC.
- Evaluation is typically interactive at systems venues — expect clarification
  questions and budget author time during the window rather than vacationing through
  it.
- Badges recognize the artifact; they change neither the paper's acceptance nor its
  12-page body. Badged papers are encouraged to add an **Artifact Appendix of up to two
  pages** (NSDI '27 call); the badges themselves appear on the final paper —
  final-paper packaging follows `nsdi-camera-ready` and the live instructions.

## Common failure modes at systems AECs

- The build assumes the authors' distribution/toolchain; pin everything or ship the
  container.
- Scripts hardcode the lab's hostnames, interface names, or IP ranges.
- Expected outputs given as exact numbers with no variance band — evaluators "fail"
  runs that are actually fine.
- The trace download link requires the authors' institutional login.
- The README's experiment names do not match the paper's section numbers, forcing
  the evaluator to reverse-map claims.

## Output format

```text
[Badge plan] sought badges + honest basis for each
[Fifteen-minute test] GETTING_STARTED verified on a clean machine? time observed
[Scale strategy] downscale config + surviving-trends statement present?
[Trace shippability] per-dataset: ship / substitute / withhold (documented)
[Community Award] public release date vs final-papers deadline
[Gaps] ordered fixes before artifact submission
```
