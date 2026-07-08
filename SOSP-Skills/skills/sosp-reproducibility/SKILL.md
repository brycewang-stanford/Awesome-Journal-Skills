---
name: sosp-reproducibility
description: Use when hardening the reproducibility of a SOSP paper's results before submission — pinning the OS-level environment, recording hardware and topology, making every figure regenerable from logged runs, separating measurement noise from effect size, and preparing the ground for post-acceptance artifact evaluation.
---

# SOSP Reproducibility

Use this while experiments are being designed and run — months before the SOSP
deadline, not during artifact evaluation. At SOSP the artifact process happens after
acceptance (see `sosp-artifact-evaluation`), which means reproducibility discipline has
a different job pre-submission: it protects **you**. Reviewers probe numbers during a
three-month review cycle and a response phase in which new experiments are forbidden;
the only defensible paper is one whose every number can be traced to a logged,
re-runnable measurement of a pinned system.

## The OS-research twist: your system changes the platform

An operating-systems artifact often *is* the environment — a modified kernel, a new
scheduler, an interposed I/O path. That collapses the usual app/platform separation and
creates specific hazards:

- A rebased kernel patch series can silently change baseline behavior; record the exact
  base commit and the full patch stack for every run, including baseline runs.
- Firmware, microcode, and mitigations (for example, speculative-execution mitigations)
  can dominate syscall-heavy microbenchmarks; log them and hold them constant across
  system and baseline.
- Frequency scaling, turbo states, and NUMA placement move tail latencies by tens of
  percent; fix the policy, and record it rather than assuming defaults.

## Capture the environment mechanically

Hand-written "Experimental Setup" sections drift from reality. Generate the facts:

```bash
#!/usr/bin/env bash
# capture-env.sh — run on every experiment node, archive with the run's results
{
  uname -a; cat /etc/os-release | head -2
  cat /proc/cmdline                          # mitigations, isolcpus, hugepages
  lscpu | grep -E 'Model name|Socket|NUMA|MHz'
  free -h | head -2; lsblk -d -o NAME,MODEL,ROTA,SIZE
  ip -br link; ethtool eth0 2>/dev/null | grep -E 'Speed|Duplex'
  git -C "$REPO" rev-parse HEAD; git -C "$REPO" status --porcelain
} > "env-$(hostname)-$(date +%Y%m%dT%H%M%S).txt"
```

Archive one such file per node per experiment batch, next to the raw results. When a
reviewer asks eleven weeks later whether the baseline ran with the same mitigations,
the answer is a file, not a memory.

## One command per figure

The standard that survives review pressure: every figure and table in the paper is
produced by a script that reads only archived raw logs. No spreadsheet steps, no
hand-transcribed numbers. This is also what makes the response phase survivable — you
can re-check any reviewer-doubted number against raw data without re-running anything,
which is the only kind of "checking" the response rules allow.

| Discipline | Pre-submission payoff | Post-acceptance payoff |
|---|---|---|
| Raw logs archived per run, immutable | Response-phase answers under the no-new-data rule | AE claims map writes itself |
| Figure scripts read logs only | No PDF/data divergence between drafts | Evaluators regenerate your plots |
| Environment capture per node per batch | Detects config drift between system and baseline runs | `hardware/` directory is done |
| Run manifest (who, when, which commit, which config) | Attribution when a number looks off | Provenance for the archival artifact |

## Variance is a first-class result

Systems effects live in distributions. Reproducibility at SOSP includes making the
noise floor explicit:

- Report repetitions and the spread (percentiles or CIs), especially for tail-latency
  claims — a p99 from one run of one trial is folklore, not a measurement.
- Distinguish sources: run-to-run jitter, node-to-node hardware variation, and
  time-of-day effects on shared testbeds. If experiments ran on a shared cluster,
  say so and quantify what that cost in variance.
- Decide the warm-up policy (discard first N iterations? cold-start included?) once,
  document it, and apply it uniformly; asymmetric warm-up between system and baseline
  is a classic self-inflicted review wound.

## Traces and workloads you cannot publish

Production traces make SOSP evaluations compelling and reproductions hard. The honest
pattern: characterize the private trace in the paper (size, arrival statistics, skew,
whatever drives the result), release a synthetic generator matched to those statistics,
and show at least one headline experiment where synthetic and real traces agree in
trend. Flag in the paper which results are re-runnable and which are documented-only —
the same tiering the artifact evaluation will ask for later.

## Output format

```text
[Repro posture] traceable / partially / folklore
[Environment] capture automated? mitigations+kernel pinned for baseline too?
[Figure pipeline] all one-command? exceptions: <list>
[Variance] repetitions, spread reported, warm-up policy uniform?
[Private data] trace characterization + generator plan
[Gap list] <ordered fixes before the freeze>
```
