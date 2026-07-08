---
name: sigmod-reproducibility
description: Use when hardening the reproducibility story of a SIGMOD submission, covering PACMMOD's expectation that code, data, scripts, and notebooks be shared, experiment provenance from config to figure, dataset and workload disclosure, variance reporting for systems numbers, and alignment with later ARI badging.
---

# SIGMOD Reproducibility

PACMMOD's author guidelines state the culture plainly: sharing research
artifacts should be the norm, and papers are expected to make code, data,
scripts, and notebooks available where possible — encouraged rather than
mandatory for acceptance, but reviewers read availability as a credibility
signal. This skill covers reproducibility *as engineered into the paper*;
the post-acceptance badge process lives in `sigmod-artifact-evaluation`.

## Provenance chain, not vibes

A database paper's result is a function of code version, configuration,
dataset, workload, and hardware. Reproducibility means the paper pins all
five for every number it prints.

| Layer | Must be recoverable from paper + artifact | Where it usually hides |
|---|---|---|
| Code version | Commit or tag behind each experiment | "latest" at submission time |
| Configuration | Buffer sizes, thread counts, compaction/GC settings, flags | Defaults nobody recorded |
| Dataset | Source, version, generator seed, scale factor | "standard benchmark data" |
| Workload | Query mix, arrival pattern, skew parameters, warm/cold state | The harness script |
| Hardware | CPU model, cores, RAM, storage class, network, OS/kernel | A single sentence, if any |

The practical test: could a competent stranger fill this whole table from
your materials? Every empty cell is a review question waiting to be asked in
the feedback phase.

## Systems numbers need distributions

Throughput and latency are noisy. The SIGMOD-credible floor:

- Repeated runs with the repetition count stated; medians or means with a
  spread measure, never a single lucky run.
- Latency reported at named percentiles (p50/p95/p99), since tail behavior
  is often the actual contribution.
- Warm-up policy stated: what was cached, JIT-compiled, or pre-compacted
  before measurement started.
- Cross-run controls named: same machine, isolated tenancy, pinned cores,
  disabled turbo — whatever was actually done, said explicitly.

## Fairness to baselines is reproducibility too

The most contested numbers in a data-systems paper are the competitor's.
Record and disclose: which version of each baseline, who tuned it and how,
which of its features were enabled, and whether its authors' recommended
configuration was used. An artifact that reproduces *your* system but ships
an untuned strawman baseline reproduces the wrong thing.

## Repro debt ledger

Track gaps while writing rather than reconstructing at deadline:

```text
# repro-ledger.md (kept in the paper repo)
| Paper item | Script | Data pinned | Config pinned | Runs/variance | Status |
|-----------|--------|-------------|---------------|---------------|--------|
| Fig 6     | exp/f6.sh | yes (sf=100, seed 41) | yes | 5 runs, p50/p99 | OK |
| Fig 7     | exp/f7.sh | yes | NO — flags undocumented | 1 run | DEBT |
| Tab 2     | manual | partial | yes | n/a | DEBT: script it |
```

Rule: nothing with status DEBT appears in the submitted PDF. The ledger later
becomes the ARI claims map almost verbatim.

## Pinning, mechanically

The cheapest insurance is captured at run time, not reconstructed later:

```bash
# stamped into every experiment's log directory by the harness
git -C "$ENGINE_DIR" rev-parse HEAD          > meta/engine.commit
"$ENGINE" --dump-effective-config             > meta/config.effective
sha256sum data/*.bin                          > meta/datasets.sha256
lscpu; free -h; uname -r; nvme list          >> meta/hardware.txt
echo "$WORKLOAD_SEED $QUERY_MIX $SKEW"        > meta/workload.params
```

Five commands, and the provenance table fills itself for every figure. The
`--dump-effective-config` line matters most: defaults you never set are
still part of the experiment, and engines change defaults between versions.

## Data you cannot publish

Industrial collaborations often involve proprietary workloads. The accepted
pattern at SIGMOD: characterize the private data (sizes, distributions, skew,
schema shape), provide a public or synthetic stand-in that exhibits the same
phenomena, run headline experiments on both, and say which conclusions are
supported by the public path alone. A paper whose every claim requires
private data cannot be badged and will be read skeptically.

## Multi-round consistency

Because SIGMOD reviewing spans rounds, reproducibility discipline has a
second job: your own revision. Reviewers may demand new experiments with a
one-month window — regenerating the whole evaluation under a new flag is only
survivable if the original runs were scripted, seeded, and logged. Teams that
hand-ran their plots discover this during the revision, at the worst time.

## What reviewers can check without running anything

Even reviewers who never open the artifact test reproducibility passively:
do the numbers in the abstract, the results section, and the conclusion
agree; do figure axes and caption units match the prose; does the claimed
hardware plausibly fit the claimed dataset in memory; do percentages in
tables sum sensibly. Internal inconsistency is read as evidence that the
pipeline is hand-operated — and it usually is. A final numeric-consistency
pass over the PDF is reproducibility work, not copyediting.

## Output format

```text
[Sharing posture] full artifact / partial / withheld with stated reason
[Provenance table] complete cells vs. gaps, per figure and table
[Variance floor] repetitions, spread measures, percentile reporting
[Baseline fairness] versions, tuning provenance, config disclosure
[Private-data plan] public stand-in coverage of headline claims
[Debt ledger] items that must close before the round deadline
```
