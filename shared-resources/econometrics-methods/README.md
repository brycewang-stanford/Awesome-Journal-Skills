# Econometrics Methods Resource

Shared resources for econometric theory, methods, simulation, and replication
packages. This is distinct from the empirical causal-inference code kit:
use it when the paper's contribution is a new estimator, test, inference method,
identification result, or computational econometrics workflow.

## What to Use

- `simulation-and-replication-checklist.md` - design and packaging checklist for
  Monte Carlo, empirical illustrations, and replication materials.
- `code/check_simulation_package.py` - dependency-free smoke checker for a local
  econometrics simulation or replication package.

## Scope

Use this kit to audit:

- simulation design, seeds, DGPs, baselines, and failure diagnostics;
- empirical illustrations that demonstrate applied value;
- proof/simulation/estimator code that supports a methods paper;
- replication-package README, software, commands, and output mapping.

Venue-specific rules still live in each pack's `resources/official-source-map.md`
and must be reopened before final advice.
