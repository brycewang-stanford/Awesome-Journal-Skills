---
name: infocom-reproducibility
description: Use when strengthening IEEE INFOCOM reproducibility even though the venue runs no formal artifact-evaluation track, covering pinned simulator setups, released code and datasets where possible, complete proofs and parameters within the page budget, IEEE reproducibility-badge options, and consistency between what the paper claims and what a reader could rebuild.
---

# INFOCOM Reproducibility

Use this before submission and again before camera-ready. INFOCOM has **no formal
artifact-evaluation track** (as of 2026-07-09; 待核实 whether a cycle adds one), so reproducibility
is a matter of **credibility, not a badge you are forced to earn**. The goal is that a competent
networking reader could rebuild your evidence and reach your conclusions from the paper plus any
material you choose to release — which, at a large venue with no rebuttal, is how you convert a
skeptical reviewer.

## Evidence map

- Map each theorem, algorithm, and reported number to a **verifiable location** — a proof (in the
  body or a tight in-budget appendix), a simulator configuration, or a released script/dataset.
- For analytical results, give enough of the assumptions, derivation, and parameters that a reader
  could re-derive or check the bound. A theorem whose proof is "omitted for space" with no pointer
  is a weakness a reviewer cannot rebut for you.
- For simulation/measurement, report the simulator and version, topology and traffic model, seeds,
  number of runs, and the parameters — enough to re-run.
- **Releasing code/data is optional but persuasive.** Where you can, deposit the simulator scripts,
  the trace, and the plotting code in a public archive; where you cannot (proprietary traces,
  privacy), say so and why.
- Keep the paper and any released material **consistent**: a number in the PDF that no released
  script or stated configuration produces reads as carelessness.

## What "reproducible" means without a badge track

| Claim in the paper | Weak reproducibility answer | INFOCOM-persuasive answer |
|---|---|---|
| "We prove Theorem 1" | "Proof omitted for space" (no pointer) | Proof sketch in body + full proof in the in-budget appendix or a stated report |
| "We simulate at scale" | "ns-3 simulation" (no setup) | Named simulator + version, topology/traffic, seeds, runs, CIs; scripts if releasable |
| "On a real trace" | "a real dataset" (unnamed) | The trace's source and access, preprocessing, and inclusion criteria |
| "Our policy beats X" | Point estimates only | Seeded runs with CIs; released config so the comparison can be re-run |

Because there is no artifact evaluator and (traditionally) no rebuttal, "trust us" does not scale —
convert every hand-wave into a stated configuration or a released file.

## Provenance and setup pinning

```text
[Analysis]   list assumptions; give full proofs (in-budget appendix or a cited technical report);
             state all parameters used in the theorems
[Simulation] name and version the simulator; pin topology, traffic model, seeds, run count;
             archive the scripts and configs if releasable
[Measurement] record the trace source and dates; document preprocessing, filtering, and confounds
[Compute]    state hardware and runtime so a reader can size a reproduction
[Randomness] log seeds for stochastic steps; say what is and is not deterministic
```

## IEEE reproducibility options (optional, post-decision)

- IEEE offers reproducibility avenues (e.g., **IEEE DataPort** for datasets, and code/data badges
  on some IEEE venues) that authors may use to deposit artifacts with a DOI. INFOCOM does not
  mandate them; treat them as a way to strengthen a released package, and confirm the current
  cycle's specifics (**待核实**).
- A public repository with an OSI-approved license and a one-screen README makes a released
  simulator far more credible than a bare tarball.

## Degrees of reproducibility (state the one you achieved)

- **Turnkey:** one documented command re-runs the simulation and regenerates the key figures.
- **Scripted:** scripts exist but need documented manual steps or external trace access.
- **Descriptive:** the paper states assumptions, setup, and parameters precisely enough to rebuild.

For an analytical INFOCOM paper, *descriptive plus a full proof* is often the honest bar; for a
simulation-heavy paper, aim *scripted or turnkey* so a reviewer's doubt about a number has a public
answer.

## Consistency and camera-ready pass

- Before submission: every scored number traces to a proof, a stated configuration, or a releasable
  script; released material (if any) is double-blind (no owner strings or identifying repo).
- Before camera-ready: if you release code/data, swap any anonymized link for a permanent,
  licensed, DOI-issuing archive, and make the paper's statements match it.

## Output format

```text
[Claim inventory] <claim -> proof | configuration | released script>
[Proof completeness] full / sketched-with-pointer / omitted-no-pointer
[Simulation provenance] <simulator+version / topology / seeds / runs / CIs present?>
[Release plan] none / code / data / both, with license and archive
[Reproducibility level] turnkey / scripted / descriptive, stated honestly
[Fixes] <paper additions + release additions before the deadline>
```
