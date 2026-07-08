---
name: kdd-artifact-evaluation
description: Use when packaging code, datasets, configs, and deployment evidence for a KDD paper, where the repository cited in the submission is the only artifact reviewers can reach because rebuttals ban links. Covers anonymized repo construction, scale-claim harnesses, ADS evidence without production data, and post-acceptance release.
---

# KDD Artifact Evaluation

Use this while the submission is being assembled — not after. KDD's review mechanics
create one hard constraint that reorders all artifact work: **the rebuttal phase does
not allow hyperlinks**, so the anonymized repository referenced inside the submitted
PDF is the complete and final artifact channel for the whole review. There is no
"we'll share code if reviewers ask"; asking happens in a phase where you cannot answer
with a link.

## Artifact strategy by track

| Track | Primary artifact | What reviewers actually probe | Non-shippable core, and its substitute |
|---|---|---|---|
| Research | Anonymized code + configs + data loaders | Can the headline table be regenerated? Does the scale claim have a runnable path? | Massive datasets → downsampled slice + full-scale download script |
| ADS | Measurement definitions + pipeline skeleton | Are post-launch metrics precisely defined? Is the eval window stated? | Production data/code → metric spec, schema, synthetic replay generator |
| Datasets & Benchmarks | The dataset itself + loaders + baseline harness | License, provenance, documentation, versioning | Nothing — the artifact is the paper |

## Building the anonymized repository

- Create a **fresh** repository, never a scrubbed clone: git history, CI configs,
  issue templates, and `.git` metadata leak identity that no README edit removes.
- Sweep for: usernames in paths, institutional cluster names, cloud bucket names,
  internal package registries, license headers, notebook execution metadata, and
  dataset names that only one company uses.
- Cite the repository in the paper body (and optionally the abstract); after the
  deadline this reference is unchangeable, so double-check the URL resolves logged out.
- Structure for a 10-minute reviewer, because that is the realistic inspection budget:

```bash
anonymous-artifact/
├── README.md            # 1 screen: claim -> command -> expected output table
├── env/                 # lockfile or container spec, exact versions
├── configs/             # one config per reported table/figure row
├── data/
│   ├── get_data.sh      # public downloads, checksums
│   └── sample/          # small slice so the pipeline runs in minutes
├── run.sh               # regenerates the smallest headline result end-to-end
└── results/expected/    # committed reference outputs for diffing
# smoke-test on a clean machine:
docker run --rm -v $PWD:/w -w /w python:3.11 bash -c "pip install -r env/requirements.txt && bash run.sh --sample"
```

## Scale claims need scale artifacts

KDD reviewers read "scales to billions of edges" as a checkable claim, not marketing:

- Ship the throughput/memory harness, not only accuracy scripts; a scalability figure
  without its benchmark script is the least-trusted plot in the paper.
- Record hardware, dataset cardinalities (rows/edges/events), and wall-clock per run in
  a machine-readable manifest, so the repo answers "on what?" precisely.
- Where the full-scale run needs a cluster no reviewer has, provide the mid-scale run
  that completes on one machine plus the exact extrapolation logic the paper uses.

## ADS evidence packaging without leaking production

The ADS track requires quantified post-launch performance, but production data almost
never ships. Reviewers accept that trade when the package contains:

- Exact metric definitions (numerator, denominator, unit, aggregation window) for
  every post-launch number in the paper.
- The measurement design: A/B split or pre/post window, traffic share, duration, and
  what guardrail metrics were tracked.
- A synthetic or replayed data generator that exercises the same pipeline shape, so
  the method is runnable even though the evidence is observational.
- An honesty note distinguishing measured production numbers from simulated ones —
  mixing them silently is a rejection pattern.

## After acceptance

- Replace the anonymous mirror with the public, licensed, citable repository; the
  camera-ready must carry the durable link (see `kdd-camera-ready`).
- Prefer an archival deposit (DOI-stamped release) over a bare git URL for the version
  that the proceedings reference.
- Check the current cycle for artifact-badging or code-availability initiatives before
  assuming none exists (待核实 — such programs change year to year).

## Vignette: packaging a billion-edge graph paper

A Research Track paper claims its sampler trains GNNs on a 3B-edge graph on one
machine. What the artifact must contain for that claim to survive contact with a
skeptical reviewer:

- `get_data.sh` that downloads the *public* 3B-edge graph (or constructs it from
  public parts) with checksums — a scale claim on an unfetchable graph is attested,
  not rerunnable, and should be labeled accordingly (`kdd-reproducibility`).
- A `--scale small|medium|full` switch: `small` finishes on a laptop in minutes and
  validates the pipeline; `medium` reproduces one main-table row on a single GPU
  overnight; `full` documents the exact hardware used for the headline.
- The peak-memory tracker wired into every run, because the paper's "one machine"
  claim is really a memory claim.
- `results/expected/` with per-scale reference outputs, so a reviewer's partial rerun
  has something to diff against.

What it must not contain: the 40GB of intermediate artifacts (regenerable), the
authors' cluster submission scripts (identity leak), or a README promising "full
instructions after acceptance" — that sentence tells reviewers the artifact is
theater.

## Common artifact failures at this venue

| Failure | Why it is fatal at KDD specifically |
|---|---|
| Repo created but never cited in the PDF | The link ban makes it undiscoverable during rebuttal |
| Git history preserved from the lab repo | Identity leak → desk-level anonymity problem |
| Accuracy scripts only, no efficiency harness | The paper's scale/efficiency axis becomes unverifiable |
| Sample data missing, full data gated | Reviewer's 10-minute budget ends at the download wall |
| ADS package with raw production extracts | Confidentiality violation risk transferred to reviewers |

## Output format

```text
[Artifact channel] repo cited in PDF: yes/no (if no: unrecoverable after deadline)
[Track register] research-repro / ads-deployment-evidence / dataset-release
[Regeneration level] one-command sample / scripted / descriptive only
[Scale evidence] throughput+memory harness: present / missing
[Anonymity sweep] <paths/history/metadata findings>
[Post-acceptance plan] <public repo, license, archival DOI>
```
