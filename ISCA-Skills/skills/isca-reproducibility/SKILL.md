---
name: isca-reproducibility
description: Use when making an ISCA paper's results regenerable — pinning simulator versions and local patches, archiving per-figure configuration manifests, recording workload provenance and sampling seeds, quantifying run-to-run variation on real hardware, and keeping the environment resurrectable through the February window.
---

# ISCA Reproducibility

In architecture, "reproducible" means someone else — or you, three months later,
mid-rebuttal — can regenerate every reported number from recorded state. Because
most ISCA numbers come out of simulators, reproducibility here is largely
*configuration archaeology*: the result is a function of tool commit, local
patches, model parameters, workload build, region selection, and warm-up policy,
and losing any one of those breaks the chain. The venue reinforces this culture
with post-acceptance artifact evaluation under ACM badging
(`isca-artifact-evaluation`); this skill covers the discipline that must exist
*before* any AE form is filled.

## The result chain, and what to pin at each link

| Link | What drifts silently | Pin it by |
|---|---|---|
| Simulator | Version-to-version behavior changes; forgotten local edits | Exact commit hash + `git diff` of local patches archived with results |
| Machine model | Config files edited during exploration | One immutable config per experiment family; configs referenced by hash |
| Workloads | Compiler/flags/inputs change binaries | Archive binaries or lockfile the build; record input sets by checksum |
| Regions & warm-up | Re-generated sampling points differ | Store the region/checkpoint files themselves, plus the generator seed |
| Post-processing | "Quick" notebook edits change aggregation | Scripted stats path from raw output to figure, in the repo |
| Real-hardware runs | Frequency scaling, thermal state, background load | Record governor, SMT/turbo state, kernel; report dispersion over trials |

## One manifest per published number

Adopt the rule that every figure and table in the paper has a manifest and a
regeneration command. This is the same manifest format `isca-experiments`
specifies for methodology writing — one artifact serves both purposes.

```bash
results/
  f07-headline/
    manifest.ini          # instrument, model, measurement, workloads
    regen.sh              # rebuild -> run -> aggregate -> plot, no hands
    raw/                  # simulator stats as emitted (never edited)
    derived/f07.csv       # scripted aggregation output
    f07.pdf               # exactly the file included in the paper
# The submission-freeze ritual:
git tag isca27-submitted && \
  sha256sum results/*/f*.pdf paper/fig/*.pdf | sort | uniq -c -w64 | \
  awk '$1!=2 {print "FIGURE MISMATCH:", $0}'   # every paper figure must
                                               # hash-match a regenerated one
```

The freeze ritual catches the classic disaster: a figure in the PDF produced by
a config that no longer exists because exploration continued after the plot was
made.

## Nondeterminism gets measured, not ignored

- **Deterministic simulators:** verify determinism once (same commit + config +
  workload → bit-identical stats) and record that check; if a threading mode
  breaks it, either use the deterministic mode for reported numbers or report
  dispersion.
- **Real hardware:** never a single trial. Report median and spread across ≥5
  runs, with the machine-state record (governor, turbo, SMT, kernel, isolation
  measures). Reviewers increasingly ask; artifact evaluators always do.
- **Sampled simulation:** the sampling procedure and seed are part of the
  result. Different SimPoint runs are different experiments — archive the chosen
  regions, don't regenerate them.

## Paper-side reporting

The paper must let a skeptical reader reconstruct the setup without the
artifact: a full configuration table (structures, sizes, latencies, DRAM
timing), the workload list with inputs and build flags summarized, the region/
warm-up policy, and a variability statement wherever hardware was measured. Under
double-blind rules the repository link, if given, must be fully anonymized
(verified 2026 rule — see `isca-submission`); the common pattern is an
anonymized-mirror link at submission, replaced by the real archival link in the
camera-ready.

## Resurrectability: the February requirement

The 2026 cycle's rebuttal/revision window (Feb 16 - Mar 6) arrived three months
after submission. Teams whose environment had rotted — simulator tree no longer
building, cluster images recycled, workload binaries lost — entered the window
unable to run the experiments that would have saved the paper. Protocol:

1. At submission: container or environment image built and stored; `regen.sh`
   for at least the headline figure verified *from the image*, not from a dev
   machine.
2. Window-open minus one week (early February): resurrection drill — boot the
   image, regenerate one figure end to end, confirm hash match.
3. Keep one team member's environment untouched between November and March; do
   not upgrade the shared toolchain mid-wait.

## Habits that make all of this cheap

- Results directories are append-only; a changed config is a *new* experiment
  ID, never an edit in place.
- The plotting path takes experiment IDs, not file paths typed by hand.
- A `METHODS.md` in the repo grows in real time — every methodological choice
  (why these regions, why this warm-up, why this DRAM model) written down when
  made, because November-you will not remember July-you's reasoning.
- Weekly: `regen.sh` for the current headline figure runs green in CI or by
  hand. Regeneration that only works on deadline eve doesn't work.

## Pre-submission reproducibility gate

- [ ] Every paper figure hash-matches a scripted regeneration
- [ ] Simulator commit + local patch diff archived alongside results
- [ ] Workload binaries/inputs archived or deterministically rebuildable
- [ ] Region/checkpoint files stored; sampling seeds recorded
- [ ] Hardware numbers carry trial counts and dispersion
- [ ] Environment image built, stored, and drill-tested
- [ ] Anonymized artifact link (if any) resolves and contains no identity

## Where each practice pays off later

| Practice | Pays off at... |
|---|---|
| Per-figure manifests + `regen.sh` | Methodology section writing, rebuttal experiments, AE claims table |
| Submission-tag freeze ritual | Camera-ready number verification, artifact snapshot selection |
| Environment image + drill | The February window's first 48 hours |
| Hardware-state records | Reviewer variance questions, Functional-badge documentation |
| `METHODS.md` running log | Every "why did we choose X" question from reviewers and evaluators |

Venue facts (AE program, badging, double-blind link rule) verified 2026-07-08 in
`../../resources/official-source-map.md`; the engineering protocol above is
community best practice, applicable regardless of cycle.
