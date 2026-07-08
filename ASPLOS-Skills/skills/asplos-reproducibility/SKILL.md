---
name: asplos-reproducibility
description: Use when hardening an ASPLOS paper's results for independent repetition — pinning simulator versions and configs, recording kernel/firmware/BIOS state, packaging FPGA bitstreams and RTL, documenting hardware dependencies an evaluator may lack, and writing availability statements that match what the ACM badges will later require.
---

# ASPLOS Reproducibility

Systems results decay fast: a kernel update, a microcode revision, or a silently
changed simulator default can move numbers by more than the paper's claimed margin.
Reproducibility work at ASPLOS is therefore **state capture** — recording the full
machine, model, and toolchain state behind every figure — done while the experiments
run, not reconstructed at camera-ready time. It also front-loads artifact
evaluation: the badge criteria (`asplos-artifact-evaluation`) are exactly a demand
that this state capture exists and works.

## The state ledger

Maintain one ledger row per experimental platform, committed alongside results:

| Layer | Capture | Why it moves numbers |
|---|---|---|
| Silicon | CPU model + stepping, memory config/topology, device (e.g. CXL expander) firmware | Steppings differ in errata and prefetch behavior |
| Firmware/BIOS | Microcode revision; SMT, turbo, prefetcher, C-state, NUMA settings | Any one knob can swamp a 10% effect |
| OS | Kernel version + full config, relevant sysctls, mitigations state | Speculation mitigations alone shift syscall-heavy results |
| Toolchain | Compiler + flags, libraries, runtime versions | -O level and allocator choice are classic silent variables |
| Simulator | Exact commit, all config files, region/checkpoint method, warm-up length | Defaults change across releases without notice |
| FPGA | Board, toolchain version, constraints, bitstream hash, achieved clock | Re-synthesis at a different clock is a different experiment |
| Workloads | Suite versions, input sets, trace provenance and preprocessing | "SPEC" without input class is unrepeatable |
| Randomness | Seeds for any stochastic component + run counts | Needed for the dispersion numbers to mean anything |

## Scripted capture beats remembered capture

Run at the start of every measurement session; store output next to the data:

```bash
#!/bin/sh
# state-capture.sh — commit this file and its output with each result set
uname -a; cat /proc/cmdline
grep -m1 'model name' /proc/cpuinfo; grep microcode /proc/cpuinfo | sort -u
cat /sys/devices/system/cpu/vulnerabilities/* 2>/dev/null | sort -u
cat /sys/devices/system/cpu/smt/control 2>/dev/null
numactl --hardware 2>/dev/null | head -5
cc --version | head -1
git -C "$SIM_DIR" rev-parse HEAD 2>/dev/null   # simulator commit
sha256sum "$BITSTREAM" 2>/dev/null              # FPGA bitstream identity
```

## The hardware-access problem, named honestly

ASPLOS artifacts often need hardware an independent evaluator will not have. The
honest pattern is a **three-tier availability statement** drafted at submission
time:

1. **Repeatable anywhere:** simulator experiments and analysis scripts — full
   configs and one command per figure.
2. **Repeatable with named hardware:** the exact platform requirements (board,
   expander, CPU family), plus what to expect if the evaluator's part differs.
3. **Not independently repeatable:** results on lab-only or pre-production
   hardware — say so, and provide either supervised access, raw logs with the
   analysis pipeline, or a scaled-down proxy. Silence here reads as concealment;
   a stated limitation reads as engineering.

## Claim-preservation, not number-worship

State which conclusions should survive environmental drift and which are
environment-specific: "the ordering of policies is stable across kernels 6.6-6.9;
absolute runtimes are not." This single sentence pattern prevents the most common
failed-reproduction dispute — an evaluator matching your ordering but not your
absolute numbers and calling it a failure.

## Timing across the ASPLOS cycle

- **Before September 9:** ledger current; capture script in the repo; availability
  tiers drafted (they inform the paper's own text).
- **Response window:** the ledger is your defense when a reviewer doubts a number —
  you can state the exact conditions instead of hand-waving.
- **Major Revision:** re-run under the *captured* original state where possible;
  where the environment has drifted, disclose the drift in the change note.
- **After acceptance:** the ledger becomes the Artifact Appendix's dependency
  section nearly verbatim; AE calendars for 2027 were 待核实 at pack-check time, so
  confirm dates when notified.

## One command per figure

The internal gold standard that makes everything downstream cheap: every figure
and table in the paper regenerates from a single committed command that reads
raw results and emits the exact plot. It catches stale-figure bugs before
submission, turns response-window questions into lookups, and becomes the
Reproducible-badge run script with a rename. Institute it at the first result,
when it costs minutes — retrofitting it at camera-ready costs days.

## Trace and dataset provenance

Workload inputs decay independently of code. For each trace or dataset, record
origin (public suite version, generated-by script + seed, or production source),
preprocessing steps as scripts rather than prose, and a checksum of the exact
bytes used. Production traces that cannot be released need a characterization
(rate, skew, working-set curves) plus a matched synthetic generator committed to
the repo — this is also the anonymity-safe form for submission, since a raw
trace can identify its owner.

## When numbers drift between submission and revision

The Major Revision window arrives months after the original runs, and
environments drift. Protocol:

1. Re-run a **sentinel subset** (three representative experiments) under the
   captured original state before starting revision work; if the sentinels
   reproduce, extend confidently.
2. If they do not, bisect the ledger — kernel, microcode, simulator commit —
   until the moved variable is found; the ledger exists for exactly this moment.
3. Disclose in the change note which results were re-collected and under what
   changed conditions, and re-state the claim-preservation sentence for the new
   environment. Silent regeneration of all numbers invites a reviewer to ask
   which version was real.

## Output format

```text
[Ledger coverage] platforms with complete rows: N/N · gaps listed
[Capture automation] script committed + outputs stored with data: Y/N
[Simulator pinning] commit + configs + region method + warm-up recorded: Y/N
[Availability tiers] anywhere / named-hardware / not-repeatable — each populated
[Claim preservation] drift-stable vs environment-specific conclusions stated: Y/N
[Badge readiness] which badges the current package could already earn
```
