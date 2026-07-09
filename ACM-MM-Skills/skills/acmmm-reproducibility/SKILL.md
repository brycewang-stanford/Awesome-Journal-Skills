---
name: acmmm-reproducibility
description: Use when strengthening the reproducibility of an ACM MM (ACM Multimedia) paper or preparing for the ACM MM Reproducibility track and ACM artifact badging — capturing environments, media/data access, seeds, and multimodal pipelines so an independent reviewer can rebuild results and reach Artifacts Evaluated or Results Reproduced badges.
---

# ACM MM Reproducibility

Use this to make an ACM Multimedia result rebuildable — both for main-track credibility and
for the dedicated **Reproducibility track**, which routes artifacts through ACM's
badging pipeline. Multimedia adds a wrinkle: the data is often video, audio, or interactive
media, and "run the code" is not enough if a reviewer cannot obtain or render the media.

## What reproducibility means here

ACM's artifact model distinguishes availability, evaluation, and reproduction. Map your goal
to the badge you are actually pursuing:

| Badge (ACM terminology) | What it asserts | What you must ship |
|---|---|---|
| Artifacts Available | The artifact is publicly, permanently retrievable | A DOI/archived repository with the code and media pointers |
| Artifacts Evaluated (Functional/Reusable) | Reviewers ran it and it works / is reusable | Build + run instructions, environment, documentation |
| Results Reproduced | An independent team reproduced the paper's results | A pipeline that regenerates the reported numbers/media |

Confirm the exact badge set offered for the current cycle on the Reproducibility-track call;
ACM's badge names and criteria evolve.

## The multimodal reproducibility ledger

Keep a single record that ties each reported result to the code, data, and config that
produced it:

```text
result: Table 2, row "full model"
  code commit: <hash>
  config: configs/full.yaml
  data: <dataset name + version + anonymous mirror for review>
  media preprocessing: <fps, sample rate, caption source>
  seed(s): <list>
  hardware: <GPU/CPU, hours>
  expected output: results/table2_full.json
```

## Media and data access

- Provide an **anonymous, working** path to the data during double-blind review — a mirror
  that a reviewer can actually download, not a placeholder.
- State the **license** and any consent/usage terms; user-generated media often cannot be
  redistributed, so document how a reviewer obtains it.
- Pin **preprocessing**: frame rate, resampling, transcription source, and alignment — small
  differences here silently break multimodal results.

## Determinism where it is achievable

- Fix and log seeds; note where nondeterminism is irreducible (e.g., some GPU kernels) and
  report variance instead of pretending to bit-exactness.
- Version the environment (container or lockfile) and record hardware, since media models are
  often memory- and throughput-sensitive.

## Reproducibility-track readiness pass

- The Reproducibility and Open Source tracks are **single-blind**, so the artifact carries
  its real identity — but the *main-track* review artifact must still be anonymous.
- Package for a stranger: a reviewer with your README and nothing else should build, run, and
  hit an expected-output check within a bounded time.
- Include a smoke check (see [`../../resources/code/README.md`](../../resources/code/README.md))
  that verifies structure and media rendering before you submit.

## Where multimodal pipelines silently break

Multimedia reproduction fails in places pure-code reproduction does not:

- **Codec and container drift** — a video re-encoded with a different codec changes pixel values
  and breaks frame-exact results; pin the decode path.
- **Sample-rate and resampling** — audio resampled by a different library shifts features; record
  the exact resampler and rate.
- **Caption/transcript source** — if captions come from an ASR system or a platform, name the
  version; a different transcript is a different input.
- **Frame sampling** — "every k-th frame" depends on the container's frame rate; state fps and
  the sampling rule.

A reproduction package that omits these looks complete but regenerates different numbers, which
is worse than an honest gap.

## Anonymous review vs. public artifact

The review artifact and the release artifact have different rules, and conflating them causes
anonymity leaks or dead links:

- **During review** (double-blind tracks): anonymous repository, anonymous data mirror, no author
  names in code comments, media metadata, or commit history.
- **At release** (camera-ready): the public, de-anonymized repository with a permanent archive
  (DOI), the license, and the final media — replacing, not merely supplementing, the anonymous
  mirror.

## Output format

```text
[Badge target] Available / Evaluated / Results Reproduced
[Ledger] complete / gaps: <which results lack a trace>
[Data access] anonymous + licensed / broken or unlicensed
[Media preprocessing] pinned / underspecified
[Determinism] seeds+env logged / gaps
[Track blinding] correct for chosen track / mismatch
[Top fixes] <ordered>
```
