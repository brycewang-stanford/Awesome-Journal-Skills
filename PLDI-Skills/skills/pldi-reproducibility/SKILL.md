---
name: pldi-reproducibility
description: Use when hardening a PLDI paper's measurements against the SIGPLAN Empirical Evaluation Guidelines — warmup and steady-state discipline, variance and confidence reporting, principled benchmark choice, pinned toolchains, cross-platform validity, and a measurement log that survives artifact evaluation.
---

# PLDI Reproducibility

PLDI's methodological yardstick is written down: the SIGPLAN Empirical Evaluation
Guidelines and their one-page checklist (Blackburn, Hauswirth, Berger, Hicks,
Krishnamurthi, 2018; sigplan.org/Resources/EmpiricalEvaluation/, read 2026-07-08).
Reviewers and artifact evaluators both reach for it. This skill turns the
checklist into compiler-bench practice; `pldi-experiments` covers what to measure,
this covers whether anyone can trust and repeat the measurement.

## Checklist, translated to PL systems

| Guideline item | What it means for a compiler/runtime paper |
|---|---|
| Clearly stated claims | "1.17x geomean on suite S vs baseline B at -O2" — never "significant speedups" |
| Suitable comparison | The strongest sensible baseline configuration, tuned as its authors intend |
| Principled benchmark choice | The suite is justified; exclusions are listed with reasons, not silently dropped |
| Adequate data analysis | Repetitions, variance, and an aggregation rule (geomean for ratios) stated in the paper |

## The measurement sins PLDI reviewers hunt

- **No warmup discipline.** JIT-compiled and cache-sensitive workloads need
  documented warmup iterations before timed runs; AOT binaries still need
  file-cache and frequency-scaling control. Say which regime you measured —
  steady-state and cold-start are different claims.
- **Single-run numbers.** Report repetitions (dozens, not three), dispersion
  (confidence intervals or at least min/max), and never present a 2% delta
  inside the noise band as an improvement.
- **One machine, universal claim.** A locality optimization can invert between
  microarchitectures. Two platforms with differing cache hierarchies is the
  floor for a general performance claim; otherwise scope the claim to the
  measured machine.
- **Unpinned toolchains.** "GCC" is not a baseline; "GCC 14.2, -O2, glibc 2.39,
  Ubuntu 24.04, governor=performance" is.
- **Benchmark survivorship.** Excluding the programs your technique fails on,
  without saying so, is the most damaging silent choice in a PL evaluation.

## A protocol worth writing down

Keep the protocol in the repository, executed by machine, so paper and artifact
cannot diverge:

```bash
# protocol.sh — executed, not described
set -euo pipefail
lscpu > results/env/cpu.txt; uname -a > results/env/os.txt
cc --version > results/env/toolchain.txt
for b in $(cat benchmarks/suite.list); do
  for i in $(seq 1 5);  do ./run.sh "$b" >/dev/null; done      # warmup
  for i in $(seq 1 30); do ./run.sh "$b" >> "results/raw/$b.csv"; done
done
python3 scripts/aggregate.py --stat geomean --ci 95 results/raw/
```

Log the environment beside the numbers: CPU model, frequency-scaling governor,
ASLR setting, load conditions. When a reviewer's rerun differs from yours, the
environment log is what turns a dispute into a diagnosis.

## Compile-time and memory are claims too

If the paper claims low compile-time overhead or memory neutrality, those numbers
need the same repetitions-and-variance treatment as speedups. A "under 3%
overhead" sentence backed by one timed build is the soft spot response-phase
reviewers press hardest.

## Tie-in to badges

Everything above lands in the artifact (`pldi-artifact-evaluation`): the executed
protocol becomes `reproduce_all.sh`, the environment log becomes `results/env/`,
and the suite-choice justification becomes `benchmarks/README`. Reproducibility
retrofitted after acceptance always shows.

## Output format

```text
[Guidelines pass] claims / comparison / benchmark choice / analysis — each ok?
[Warmup regime] documented? steady-state vs cold-start stated?
[Variance] runs per data point, CI method, noise floor vs claimed delta
[Platforms] n machines; claim scoped accordingly?
[Pinning + log] toolchain versions, flags, environment captured in repo?
```
