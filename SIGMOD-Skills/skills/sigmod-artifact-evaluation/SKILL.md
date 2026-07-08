---
name: sigmod-artifact-evaluation
description: Use when preparing a SIGMOD paper's code and data for the Availability & Reproducibility Initiative (ARI), covering the post-acceptance opt-in, HotCRP artifact registration, the Artifacts Available / Artifacts Evaluated / Results Reproduced badges, evaluator criteria, and the Best Artifact award path.
---

# SIGMOD Artifact Evaluation

SIGMOD runs a named, long-standing artifact program: the **Availability &
Reproducibility Initiative (ARI)** at `reproducibility.sigmod.org`. It is
optional, happens **after acceptance**, and is decoupled from the accept/
reject decision — but its badges are embedded into the paper's PDF in the ACM
Digital Library, so the payoff is permanent and public. Recent editions
registered artifacts through a dedicated HotCRP site (e.g.,
`sigmod25ari.hotcrp.com`); confirm the current edition's site and dates
before promising a timeline.

## The badge ladder

| Badge | What evaluators must confirm | Typical blocker |
|---|---|---|
| Artifacts Available | Code, data, scripts, notebooks reachable at a stable public location | Link rot; "email us for the dataset" |
| Artifacts Evaluated | Package is exercisable and well documented | Undocumented cluster assumptions |
| Results Reproduced | Key results of the paper independently regenerated | Figures that need hand-tuned steps |

Aim explicitly at one rung. A package engineered for Results Reproduced looks
different from one that merely publishes source: it names which figures and
tables constitute the "key results" and drives each one end to end.

## What ARI evaluators grade

The initiative's stated criteria are **coverage** (how much of the paper the
artifact backs), **ease of reproducibility** (how little effort a rerun
takes), **flexibility** (can parameters, workloads, and datasets be varied),
and **portability** (does it run beyond the authors' exact machine). Database
artifacts fail these in predictable ways:

- Coverage: the artifact rebuilds microbenchmarks but not the headline
  end-to-end comparison against the competing engine.
- Ease: a 40-step README where a driver script should be.
- Flexibility: scale factors and thread counts hard-coded into binaries.
- Portability: kernel-version, NUMA-layout, or GPU assumptions that only
  hold on the lab machine; no container or VM escape hatch.

## Hardware honesty

Data-management experiments often need big machines. ARI evaluations have
historically accommodated this via cloud credits or author-provided access in
some editions — but the current edition's policy must be checked, not
assumed. Regardless of policy:

- State minimum and recommended hardware in the README's first screen.
- Provide a reduced-scale mode (smaller scale factor, fewer threads) that
  preserves every qualitative trend, and say which absolute numbers will
  differ from the paper.
- Wall-clock estimates per experiment; evaluators budget time, and an
  unannounced 30-hour run is how evaluations stall.

## Packaging pattern that passes

```text
artifact/
  README.md          # claims map: Fig/Table -> script -> expected output
  LICENSE
  Dockerfile         # or VM image link; pinned OS + dependency versions
  data/fetch.sh      # pulls public datasets by checksum; sizes stated
  run_all.sh         # full reproduction, prints per-step ETA
  run_small.sh       # laptop-scale variant, trends preserved
  experiments/
    fig7_throughput/ # one directory per paper artifact, self-contained
    tab3_latency/
  plot/              # regenerates the exact PDF figures from raw logs
```

The claims map is the single highest-leverage file: a table from paper
artifact to command to expected output, with tolerances ("within 10% on
different hardware; ordering of systems preserved").

## Incentives beyond the badge

SIGMOD confers a **Best Artifact award** through the initiative, and
reproducibility reports from past editions are themselves published in the
ACM DL — meaning strong artifacts earn citable recognition. For an engine or
index paper, the artifact also becomes the de facto baseline implementation
future papers must compare against, which compounds citations for years.

## Questions evaluators ask that READMEs rarely answer

- Which exact figure numbers count as the paper's key results, and where is
  that stated?
- What should I see on screen when a run *succeeds* — and what does a known
  benign warning look like, so I don't abort a healthy run?
- How much disk does the full dataset expand to after decompression?
- Can steps be resumed after a failure, or does every retry start from
  data fetch?
- Which numbers are hardware-sensitive, and how much drift is acceptable
  before I should suspect a real problem?
- Who do I contact (anonymity no longer applies) if a step fails, and how
  fast do authors respond during the evaluation window?

Answer all six in the README's first two screens and the evaluation's most
common failure mode — silent stall and abandonment — mostly disappears.

## Sequencing with the paper lifecycle

1. During review: keep the anonymized package coherent (see
   `sigmod-supplementary`); it becomes the ARI seed.
2. At camera-ready: publish and tag the release matching published numbers
   (see `sigmod-camera-ready`).
3. At ARI registration: submit the tagged version via the edition's HotCRP,
   then leave it frozen — evaluate-time pushes create version skew.
4. After badging: keep the archive stable; the badge points at the DL
   record forever.

## Output format

```text
[Target badge] Available / Evaluated / Results Reproduced
[Claims map] Fig/Table -> script coverage, gaps listed
[Criteria audit] coverage / ease / flexibility / portability findings
[Hardware plan] full-scale needs, reduced-scale mode, runtimes
[Registration] ARI edition site + dates confirmed or 待核实
[Fix queue] ordered work before artifact submission
```
