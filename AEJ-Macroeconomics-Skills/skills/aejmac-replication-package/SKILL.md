---
name: aejmac-replication-package
description: Use when assembling the data, code, and documentation package for an American Economic Journal: Macroeconomics (AEJ: Macro) manuscript to pass the AEA Data and Code Availability Policy and the AEA Data Editor's pre-publication reproducibility check. Covers macro specifics (simulation/calibration code, restricted-access data); it does not write the analysis itself.
---

# Replication Package (aejmac-replication-package)

## When to trigger

- A paper is heading toward conditional acceptance and the AEA Data Editor check is next
- You have simulation/calibration code but have never packaged it for a reviewer to run
- The data include a restricted/proprietary source (confidential micro data, licensed series)
- You want to build the package *as you go* rather than scrambling at acceptance

## The AEA reproducibility regime (verified 2026-06; re-confirm on the official AEA pages)

- Governed by the **AEA Data and Code Availability Policy**. Conditionally accepted papers undergo a review by the **AEA Data Editor** (Lars Vilhuber) **before publication**, including **reproducibility checks** and verification of the information provided.
- Deposit in the **AEA Data and Code Repository on openICPSR** (use is strongly encouraged; other trusted repositories may be allowed with Data Editor approval). Materials are posted with the article.
- **Code scope is broad** — and this is the macro-critical point: the policy covers data cleaning **and** "estimation, **simulation**, model solution, and **visualization**" code. For AEJ: Macro, the **DSGE/HANK solver, the calibration/estimation routines, and the simulation code must all be in the package**, not only the regression scripts.
- **Restricted-access data:** exceptions exist for confidential / copyrighted / agreement-restricted data; authors must preserve materials 5+ years, provide reasonable replication assistance, **make the code public even when the data cannot be**, and disclose data sources. State any such request to the Data Editor.
- **Field experiments** must be registered in the **AEA RCT Registry**.

## Building a macro-grade package

### Directory & master script
- A clear tree: `/data` (raw + analysis), `/code`, `/output` (tables + figures), `/docs`.
- One **master script** (`run_all`) that regenerates **every table and figure** from raw inputs in order, including the model solution and simulation steps.
- A **README** following the AEA template: data sources and access, software + versions, hardware, expected runtime, and a map from each exhibit to the script that makes it.

### Macro-specific reproducibility
- **Pin the toolchain**: Stata version + `ssc`/`net` package versions; R `renv.lock`; Python `requirements.txt`/`conda env`; Julia `Project.toml`/`Manifest.toml`; **Dynare version** for DSGE.
- **Seeds** set and reported for every simulation, bootstrap, and randomization step.
- **Long-running computations** (global solutions, large HANK simulations, MCMC): provide a way to verify without a supercomputer — ship intermediate/cached outputs and a reduced-scale switch, and document expected full runtime.
- **Numerical accuracy artifacts**: include the diagnostics (Euler errors, grid checks) so the Data Editor can confirm the solution, not just rerun it.

### Data documentation
- For each source: provider, exact extract/vintage, access date, license, and whether it is public or restricted.
- Real-time vs. revised macro vintages (e.g., ALFRED): document which you used.
- Restricted data: a clear access path and a public code subset that runs on synthetic/sample data where possible.

## Checklist

- [ ] openICPSR (AEA Data and Code Repository) deposit planned; README on the AEA template
- [ ] Master `run_all` regenerates every exhibit incl. model solution + simulation
- [ ] Simulation, calibration/estimation, and solver code all included (not just regressions)
- [ ] Toolchain pinned (Stata/R/Python/Julia/Dynare versions); seeds set and reported
- [ ] Long-running steps: cached outputs + reduced-scale switch + runtime documented
- [ ] Restricted data: exception request stated; code public; access path documented; 5-year retention noted
- [ ] Every data source documented (provider, vintage, access date, license)
- [ ] Field experiments registered in the AEA RCT Registry

## Anti-patterns

- Packaging only the regression scripts and omitting the DSGE solver / simulation code
- "Results available on request" instead of a deposited, runnable package
- Unpinned package versions, so the Data Editor cannot reproduce the numbers
- Unseeded simulations that do not reproduce
- A multi-day computation with no reduced-scale path or cached intermediates
- Discovering a data-license problem at acceptance instead of flagging it early

## Output format

```
【Repository】openICPSR (AEA Data and Code Repository) deposit ready? [Y/N]
【Master script】run_all regenerates all exhibits incl. model+simulation? [Y/N]
【Code scope】solver + calibration/estimation + simulation + cleaning all included? [Y/N]
【Toolchain + seeds】versions pinned; seeds reported? [Y/N]
【Restricted data】exception stated; code public; access path documented? [Y/N / NA]
【Long runs】cached outputs + reduced-scale switch + runtime noted? [Y/N / NA]
【Next step】aejmac-referee-strategy
```
