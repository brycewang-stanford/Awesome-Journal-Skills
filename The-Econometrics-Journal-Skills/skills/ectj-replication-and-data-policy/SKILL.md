---
name: ectj-replication-and-data-policy
description: Use when preparing The Econometrics Journal replication files, README, software versions, data documentation, seeds, proprietary-data exemptions, and OUP Supporting Information package after conditional acceptance or before submission risk review.
---

# EctJ Replication And Data Policy

Use this before submission for planning and after conditional acceptance for packaging.
Reopen the RES replication policy before final delivery.

## Package checklist

- Prepare a README that explains file contents, execution order, software, package versions,
  expected outputs, runtime, and system requirements.
- Include data or clear access instructions with complete variable documentation. If using
  proprietary formats, provide ASCII alternatives when required.
- Include all code needed to reproduce tables, figures, simulations, appendices, and
  supplementary results; set random seeds.
- Explain usage restrictions, confidential data, or exemption requests at first submission if
  current policy requires early disclosure.
- Expect accepted packages to appear as OUP Supporting Information when permitted.
- Treat non-compliance as publication risk; the RES policy says the board may refuse
  publication for non-compliance.

## Methods-paper package pattern

For an EctJ methods paper, the replication package should let a referee rerun the claim hierarchy:

1. `00_setup` records software versions, seeds, paths, and package checks.
2. `01_simulation` recreates the minimal Monte Carlo tables used in the paper.
3. `02_application` recreates the empirical illustration or diagnostic example.
4. `03_figures_tables` exports exactly the exhibits in the manuscript and supplement.
5. `README` states expected runtime, hardware assumptions, and which files are slow or optional.

If the proof is symbolic rather than computational, still include any scripts used for figures, numerical
examples, or robustness checks. Do not leave code that changes a published number outside the package.

## Acceptance-risk audit

Run this audit before treating the package as ready:

- Match every numbered table, figure, simulation panel, and appendix exhibit to a producing script.
- Record the exact software stack, solver options, random seeds, BLAS or parallel settings, and any
  non-default package versions that can change Monte Carlo output.
- Separate slow exhaustive simulations from the short smoke run a referee can execute quickly; both should
  write comparable output names.
- For restricted data, provide the legal access path, synthetic or public-use substitute when possible,
  and the reason the substitute cannot reproduce confidential quantities exactly.
- Check that manuscript labels, supplement labels, file names, and README names agree after final
  revisions. A stale label is evidence that the package was not rerun.

For EctJ, the package should make the method credible, not merely archived. A referee should be able to
see which computation supports the leading-case theory, which computation supports practical use, and
which files are optional robustness material.

## Monte Carlo determinism checks

Simulation-heavy EctJ papers fail reproduction for reasons pure-empirics packages never face.
Verify each before delivery:

- One named seed per experiment, set inside the script rather than at the console; the RES policy
  explicitly expects seeds to be set for simulations.
- Parallel runs use a reproducible RNG-stream scheme (one substream per replication), because
  thread scheduling otherwise reorders draws and shifts the third digit of rejection rates.
- Record solver tolerances and optimizer starting values; a Monte Carlo that mostly converges
  must log which replications failed and how they were handled.
- Rerun the smoke version on a clean machine and diff against the shipped output; illustrative
  bar: simulated sizes should match to the digits printed in the paper.

## Calibration: what a posted EctJ package looks like

Accepted packages appear alongside the article as OUP Supporting Information. Typical shape,
hedged where journal practice varies: a top-level README, a master script per claim layer
(simulation, application, exhibits), pinned software versions, and data or documented access
instructions with ASCII fallbacks for proprietary formats. Exact file-format and size constraints
on the OUP side can change; confirm against the journal's current author guidelines before the
final upload.

## Output format

```text
[Replication status] ready / needs fixes / blocked
[Contents] <data/code/README/software/seeds>
[Restricted-data issue] <none, access path, or exemption request>
[Reproduction command] <master script or workflow>
[Publication risk] <low/medium/high and why>
```
