---
name: conext-experiments
description: Use when designing or auditing the evaluation of an ACM CoNEXT paper — matching evidence to claim shape with real testbeds and deployments, honest and tuned baselines, measurement statistics and uncertainty, trace and config provenance, and contamination-aware ablations for ML-for-networking work.
---

# CoNEXT Experiments

Build the evaluation a networking reviewer will actually interrogate. CoNEXT's evidence culture is
**systems-and-measurement**: claims are backed on the **real target platform** — a testbed,
deployment, or trace — with honest baselines and reported uncertainty, not simulation standing in
for hardware or a single number with no variance. Because a one-shot major revision is decided on a
list of **minimum necessary changes**, an evaluation gap you leave now often becomes a mandatory fix
under a tight window later.

## Match evidence to claim shape

| Claim shape | Evidence CoNEXT expects |
|---|---|
| A mechanism is faster/cheaper on real hardware | A run on the **real target** (switch, NIC, kernel, testbed) under its real constraints, vs. a tuned baseline, with effect sizes |
| A phenomenon exists in the wild | A **measurement campaign** with documented vantage points, capture dates, and a reproducible extraction methodology |
| An architecture scales | **Scalability evidence** (real deployment or faithful emulation) across the relevant range, not a point claim |
| An operator intervention helps | Evidence at **operationally relevant scale**, with the counterfactual measured or bounded |
| A learned component adds value | An **ablation** isolating the learned part from the mechanism, plus a contamination check |

## Real testbeds and deployments over simulation

- **Evaluate on the platform the paper is about.** If the claim is about switch behavior, run it on
  the switch (or a faithful hardware testbed); if about a protocol on real paths, use a testbed or
  trace-driven replay. Simulation-only systems claims are a classic CoNEXT revision risk.
- **Describe the testbed so it can be rebuilt:** topology, hardware models, firmware/OS versions,
  link rates, buffer depths, and background traffic. A reviewer who cannot picture the setup cannot
  trust the numbers.
- **State what is emulated vs. real**, and why the emulation is faithful for the claim.

## Honest, tuned baselines

- Compare against the **strongest reasonable baseline**, tuned with an equal, documented budget —
  not a strawman default. "The baseline is not tuned/fair" is one of the most common CoNEXT
  push-backs.
- Report the baseline's configuration alongside yours so the comparison is auditable.
- Where a fair baseline does not exist, say so and justify the comparison you made.

## Measurement statistics and uncertainty

- Report **multiple runs** and **variability** (confidence intervals, percentiles/CDFs for latency,
  not just means). Tail behavior is often the point in networking.
- Use **corrected comparisons** when testing many conditions; a measurement reviewer notices
  uncorrected multiple testing.
- Prefer **effect sizes and distributions** over a single bar; a CDF that shows the whole
  distribution pre-empts questions a mean hides.

## Trace and config provenance (pin it now)

- Record **capture vantage points and dates**, the **extraction/anonymization methodology**, and the
  **exact configs** used. These cannot be reconstructed after the fact — pin them at collection time.
- For anything derived from operator or third-party data, document the **access terms** and what can
  be released (this interacts with double-anonymity and reproducibility).
- Keep the raw-to-result pipeline scripted so the numbers in the paper regenerate from the trace.

## Contamination-aware ML-for-networking ablations

If the paper uses a learner or LLM on networking data:

- **Isolate the learned component** with an ablation (e.g., replace it with a heuristic) so the
  reviewer sees its marginal value over the mechanism.
- **Guard against contamination/leakage:** ensure test paths/traces/time windows are disjoint from
  training, and that a temporal split reflects real deployment.
- **Pin model identifiers and dates** and cache raw model outputs; a package that needs live API
  calls re-samples rather than reproduces (see [`conext-reproducibility`](../conext-reproducibility/SKILL.md)).
- Apply the **model-swap test**: if the networking lesson does not survive swapping the model, the
  paper may belong at an ML venue (see [`conext-topic-selection`](../conext-topic-selection/SKILL.md)).

## Pre-submission evaluation audit

```text
[Claim coverage]   every claim has a matching measurement on the real target? yes/no
[Platform realism] real hardware/testbed/trace, or simulation standing in? note each
[Baselines]        strongest reasonable, equally tuned, config reported? yes/no
[Uncertainty]      multiple runs, CIs/CDFs, corrected comparisons? yes/no
[Provenance]       vantage points, dates, configs, firmware/OS pinned? yes/no
[ML checks]        ablation + contamination guard + model-swap survives? n/a or yes/no
```

## Output format

```text
[Evaluation status] solid / gaps
[Claim-evidence matrix] <claim -> measurement + platform + baseline + uncertainty>
[Platform] real target used? emulation justified?
[Provenance] traces/configs/firmware pinned for reproducibility
[Revision risk] <the gap most likely to become a minimum-necessary change>
```
