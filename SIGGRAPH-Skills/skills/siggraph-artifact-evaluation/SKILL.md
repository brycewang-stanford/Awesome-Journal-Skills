---
name: siggraph-artifact-evaluation
description: Use when pursuing the Graphics Replicability Stamp (GRSI) or Code Replicability in Computer Graphics (CRCG) recognition for an accepted SIGGRAPH / TOG paper, covering how graphics replicability differs from ACM artifact badging, what volunteers actually run, deterministic result reproduction, Software Heritage archiving, and the separate post-acceptance timing.
---

# SIGGRAPH Artifact Evaluation (Replicability Stamp)

SIGGRAPH does **not** run the ACM Artifact Review and Badging scheme that SIGSOFT and systems
venues use. The computer-graphics community's equivalent is a **community-run replicability
stamp**, earned *after* acceptance and independent of the review: the **Graphics Replicability
Stamp Initiative (GRSI, replicabilitystamp.org)** and the related **Code Replicability in Computer
Graphics (CRCG, replicability.graphics)**. The distinction matters: a stamp certifies that a
volunteer **rebuilt your code and reproduced your paper's results**, and archives that code for the
community. Facts below trace to `resources/official-source-map.md`; confirm the current GRSI
process before you package.

## What the stamp is (and is not)

| | Graphics Replicability Stamp (GRSI) | ACM Artifact Badges (other venues) |
|---|---|---|
| Who runs it | Volunteer researchers from the graphics community | The venue's artifact evaluation committee |
| What it certifies | Your code **replicates the paper's results** | Available / Functional / Reusable / Reproduced |
| When | Post-acceptance, on the initiative's own schedule | Post-acceptance, on the venue's AE deadline |
| Archiving | **Software Heritage** snapshot + long-term ID (since 2023) | DOI-issuing archive |
| Scope | Independent of SIGGRAPH's review; optional recognition | Tied to the venue's AE track |

The GRSI has recognized graphics code since **2016** and is supported across the field's venues
(ACM TOG, IEEE TVCG, Wiley CGF, Elsevier C&G, CAD/CAGD). **CRCG** has, since **July 2020**, focused
specifically on checking whether **SIGGRAPH papers' results are replicable**. Neither is required
for publication — but the stamp is the credible, checkable signal of a runnable contribution in
this community.

## What a volunteer actually does

Assume a graphics-literate volunteer clones your repository on their own machine and tries to
regenerate a headline result from your paper. They are checking **replicability of results**, not
just that the code compiles:

| Contribution type | What the volunteer reproduces | Common failure caught |
|---|---|---|
| A rendering technique | A converged image matching a paper figure, within tolerance | Non-deterministic output; missing scene assets |
| A geometry/mesh method | A processed mesh matching the reported statistics | Hard-coded absolute paths; unshipped input meshes |
| A simulation | A representative frame/sequence from the paper | Unseeded RNG; platform-specific solver drift |
| A learning-based method | A result from released weights, not retraining from scratch | Weights absent; inference needs undocumented data |

Design so the *first* headline result reproduces from a documented command on a clean checkout.

## Packaging plan for a replicable graphics artifact

```text
[Build]        a documented, pinned build (CMake/conda/Docker) that compiles on a clean machine;
               name exact compiler/CUDA/driver versions where GPU code is involved
[Assets]       ship (or give a stable download for) the scenes, meshes, textures, and weights the
               results need -- code without inputs cannot replicate a figure
[Determinism]  fix seeds; document tolerance for floating-point/GPU non-determinism; state which
               results are bit-exact vs perceptually-equal
[Mapping]      a table: paper figure/table -> command -> expected output image/metric/frame
[Timings]      report the hardware and the wall-clock the paper claims, so timings are checkable
[License]      an OSI-approved license so the code can be shared and reused
[Archive]      a Software Heritage snapshot (GRSI archives accepted code there) + a Zenodo DOI
```

## Determinism is the graphics-specific hard part

Reproducing an image is not reproducing a number. Plan for it:

- **State the comparison metric and tolerance.** Volunteers cannot judge "looks right" — give
  PSNR/SSIM/LPIPS or a diff threshold against a bundled reference image.
- **Pin the stochastic pieces.** Monte Carlo renderers, stochastic simulations, and GPU reductions
  drift; seed them and document the residual non-determinism.
- **Bundle reference outputs.** Include the exact images/frames the paper reports so a volunteer
  compares against ground truth, not a re-render of their own.
- **Separate "replicate the result" from "retrain the model."** For learning-based work, ship
  weights and an inference path; full retraining is rarely the replication target.

## Calibration

- The stamp is **post-acceptance and optional**; it is decided by the initiative's volunteers on
  their timeline, not by the SIGGRAPH committee, and not on the camera-ready deadline.
- GRSI and CRCG are related but distinct efforts; check each initiative's current submission
  instructions and supported-venue list before submitting your code.
- A stamp strengthens a paper's reach but is never a substitute for in-paper evidence — the review
  already happened without it.

## Output format

```text
[Target] Graphics Replicability Stamp (GRSI) / CRCG check / both
[Headline result] <figure/table the volunteer will reproduce>
[Clean-machine build] compiles + runs from documented command? yes/no
[Assets] scenes/meshes/weights shipped or stably linked? yes/no
[Determinism] seeds fixed + tolerance + reference outputs bundled? yes/no
[Claim mapping] <figure -> command -> expected output present?>
[Archive] Software Heritage snapshot + DOI + OSI license? yes/no
[Fixes before submitting code] <ordered>
```
