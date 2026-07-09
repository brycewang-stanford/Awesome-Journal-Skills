---
name: hpca-experiments
description: Use when auditing an HPCA evaluation: declaring the fidelity contract (simulator, configuration, workloads, sampled regions, validation), matching each claim to its instrument, capturing real-silicon machine state, tuning baselines honestly, and reporting per-workload distributions rather than a single mean.
---

# HPCA Experiments

Use this to stress-test an HPCA evaluation before the July gate. Architecture
reviews are won and lost on methodology: a mechanism can be sound and still be
rejected if the numbers cannot be trusted against their instrument.

## Declare the fidelity contract

Every HPCA evaluation rests on a contract the paper must state explicitly:

- **Tool and version.** Which simulator (and commit), or which real machine.
- **Fidelity scope.** What the model captures and what it abstracts — an in-order
  functional model and a cycle-level OoO model make different claims believable.
- **Configuration.** Core width, cache hierarchy, memory/DRAM timing model,
  interconnect — the parameters a reviewer needs to reproduce the setup.
- **Workloads and regions.** The suite, the inputs, and how regions were sampled
  (e.g., SimPoint-style sampling) rather than run to completion.
- **Validation.** What the timing models were validated against, with the error.

A number outside its contract is unreviewable; a contract stated up front pre-empts
half the methodology objections.

## Match each claim to its instrument

| Claim type | Credible instrument | Not credible from |
|---|---|---|
| Cycle-level speedup | Validated cycle-level simulator | A functional/trace model with no timing |
| Energy/power | Modeled power tool with stated assumptions, or measured silicon | Hand-waved "should save energy" |
| Real-world behavior | Silicon with captured governor/turbo/SMT/NUMA state | A simulator alone, presented as measurement |
| Area/cost | Synthesis or a cited model | An unsupported "small overhead" |

Do not let a claim borrow credibility from an instrument that cannot support it.

## Capture machine state for silicon

Every real-hardware number needs host provenance: frequency governor, turbo, SMT,
NUMA policy, kernel and firmware versions, plus **trial counts and dispersion**.
A single run on an unpinned machine is noise dressed as a result.

## Tune baselines honestly

The most common HPCA methodology objection is an under-tuned baseline. Give prior
mechanisms their best reasonable configuration, sweep the parameters that matter, and
report where your mechanism is **neutral or loses** — a paper that only ever wins is
less believable, not more.

## Report the distribution

Report **per-workload results**, not only a geomean. Mark the workloads where the
mechanism helps, is neutral, and hurts, and explain the losses. Sensitivity studies
(cache size, core count, bandwidth) belong in the paper or appendix, because the
first reviewer question is "does this hold off your chosen point?"

## Pre-submission audit

```text
1. Is the fidelity contract stated in full (tool, scope, config, workloads, validation)?
2. Does each headline claim name a credible instrument for its type?
3. Are silicon numbers accompanied by machine state, trials, and dispersion?
4. Are baselines tuned to their best config, with a sweep, not a single point?
5. Are results per-workload with neutral/loss cases marked and explained?
6. Do sensitivity studies show the result survives off the chosen operating point?
```

## Output format

```text
[Fidelity contract] complete / partial / missing
[Instrument match] claims matched / total claims
[Silicon provenance] state+trials+dispersion captured? (Y/N/NA)
[Baseline tuning] best-config + sweep? (Y/N)
[Distribution] per-workload with losses explained? (Y/N)
[Top methodology risks] <ordered>
```

Methodology expectations shift by cycle — reopen the current CFP and recent HPCA
program norms before treating any convention here as fixed.
