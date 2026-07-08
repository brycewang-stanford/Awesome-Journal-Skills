---
name: uai-reproducibility
description: Use when hardening reproducibility evidence for a UAI paper, including seeds, sampler convergence diagnostics, ELBO and calibration traces, dataset and hyperparameter disclosure, compute reporting, and honest code-availability statements, since UAI strongly encourages released code and data and reviews whether claims are convincingly backed.
---

# UAI Reproducibility

UAI's 2026 CFP did not impose a formal reproducibility checklist (one may appear later —
待核实 each cycle), but it strongly encouraged code and data availability and instructed
reviewers to judge whether claims are backed up convincingly. At this venue "convincing"
has a technical meaning: stochastic-inference results carry diagnostics, not just point
estimates. This skill turns that norm into an audit.

## The UAI-specific bar

Reproducibility questions at a probabilistic-inference venue go one level deeper than
"can I rerun the script":

- A sampler that reproduces the same posterior mean but different tail quantiles has not
  reproduced the paper — report and check the diagnostics that detect this (R-hat, ESS,
  divergent transitions where relevant).
- A variational result is reproducible when the ELBO trajectory and the selected
  restart are recoverable, not merely the final metric; multi-restart selection rules
  must be stated.
- Calibration claims reproduce only if the binning scheme, the split used for
  recalibration, and the α grid are all pinned down; empirical coverage moves with all
  three.
- Causal-discovery results depend on graph generation as much as on the algorithm:
  publish the SCM sampler, noise families, and intervention protocol.

## Determinism ledger

Record every randomness source once, in code, and cite it from the paper:

```python
# repro/ledger.py — imported by every experiment entry point
import json, platform, random, numpy as np

def fix_and_log(seed: int, path: str = "run_manifest.json"):
    random.seed(seed)
    np.random.seed(seed)
    manifest = {
        "seed": seed,
        "python": platform.python_version(),
        "numpy": np.__version__,
        "chains": 4, "warmup": 1000, "draws": 2000,   # sampler config lives here
        "elbo_restarts": 10, "restart_rule": "best final ELBO",
    }
    json.dump(manifest, open(path, "w"), indent=2)
    return manifest
```

The manifest style matters more than the specific fields: one machine-readable file per
run, checked into the artifact, lets a reviewer reconcile the paper's Table 3 with an
actual execution.

## Disclosure map

| What must be recoverable | Where it lives at UAI | Common omission |
|---|---|---|
| Model and assumption set | Main part, stated with each theorem/method | Assumptions distributed across three sections |
| Sampler / optimizer settings | Appendix (unlimited, same PDF) | "Default settings" without library version |
| Hyperparameter search space and selection rule | Appendix table | Only the winning configuration reported |
| Seeds and number of repeats | Appendix + artifact manifest | Single-run results with no variance |
| Dataset versions, splits, preprocessing | Appendix + loader script in ZIP | Preprocessing "as in [12]" where [12] is ambiguous |
| Compute (hardware, runtime, memory) | Appendix | Runtime reported only for the proposed method, not baselines |
| Code/data availability statement | Main part or appendix | Silence, which reviewers read as "unavailable" |

## Diagnostic quick reference

What "reported convincingly" tends to mean per inference family — as conventions of
the field, not venue mandates:

| Family | Minimum reported | Stronger version |
|---|---|---|
| MCMC | R-hat per parameter block, ESS, chain count/length | Rank plots; comparison against a long-run gold standard |
| Variational | Final ELBO, restart count and rule | ELBO traces; posterior-quality check on a tractable case |
| SMC / particle | Particle count, resampling scheme, ESS trajectory | Variance of the marginal-likelihood estimate over repeats |
| Conformal / intervals | Split sizes, α grid, empirical coverage | Conditional coverage slices; width distribution |
| Calibration | Binning scheme, ECE definition used | Reliability diagrams with confidence bands over seeds |
| Causal discovery | Graph generator, noise family, SHD/SID per seed | Sensitivity to assumption violations (unfaithfulness, confounding) |

If a row's "minimum" column is missing for your method family, expect the backing
criterion to absorb the damage.

## Honesty over completeness

- If code cannot be released (industrial constraints, licensed data), say so in the
  paper and compensate: fuller pseudocode, exact hyperparameters, synthetic surrogates
  for private datasets. The encouraged-not-mandatory wording gives room for honesty, not
  for vagueness.
- Report failure modes you observed — initializations that collapse, chains that need
  longer warmup on one dataset. Probabilistic-ML reviewers trust papers that know where
  their method breaks.
- Never let variance disappear in the retelling: if three of ten seeds underperform,
  the aggregate table must reflect it (mean ± sd over all ten, or a stated, principled
  selection rule).

## Where reproducibility evidence lives

Split by tier deliberately: the availability statement and diagnostic summaries in
the reviewed PDF (body or appendix), where they count toward backing; manifests,
loaders, and per-run logs in the ZIP, where they support spot-checks. Never leave the
only mention of seeds or repeat counts inside the optional archive — reviewers grade
what the PDF says.

## Pre-submission reproducibility drill

1. Clone your own artifact onto a machine that never ran the project; follow only the
   README.
2. Reproduce the smallest headline number end to end, including the diagnostic that
   validates it.
3. Diff the regenerated figure against the paper's; investigate any visible deviation
   before a reviewer does.
4. Grep the paper for every "we observe/we find/consistently" and confirm each maps to a
   logged run.
5. Write the availability statement last, describing what is actually in the ZIP — not
   what was planned in January.

## Output format

```text
[Repro grade] turnkey / recoverable with effort / under-specified
[Diagnostics reported] <R-hat/ESS/ELBO/coverage/SHD... as applicable>
[Determinism ledger] present / partial / absent
[Disclosure gaps] <items from the map still missing>
[Availability statement] drafted / needs honesty pass / missing
```
