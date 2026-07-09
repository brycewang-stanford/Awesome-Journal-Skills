---
name: siggraph-reproducibility
description: Use when building the reproducibility story for a SIGGRAPH / TOG paper, covering deterministic result regeneration, scene/mesh/weight provenance, hardware and timing disclosure, floating-point and GPU non-determinism, and a code/data release that a reader or a Graphics Replicability Stamp volunteer can actually run.
---

# SIGGRAPH Reproducibility

In computer graphics, reproducibility means a reader can **regenerate your figures and timings**,
not merely re-derive your equations. SIGGRAPH's culture rewards this heavily — the community runs
its own replicability stamps (see `siggraph-artifact-evaluation`) — but the review itself is
decided on the paper and its supplemental video, so reproducibility is something you *build into*
the work from the start, not bolt on at camera-ready. Anchor policy to
`resources/official-source-map.md`.

## Reproducibility here is result-reproducibility

A graphics result is an image, a mesh, a frame sequence, or a timing on specific hardware. Each
class has its own failure mode:

- **Rendered images** depend on scene assets, sampler seeds, and the renderer's floating-point
  path — two "correct" runs can differ by pixels.
- **Geometry/mesh outputs** depend on the exact input mesh and its scale/orientation conventions.
- **Simulations** depend on time-step, solver tolerances, and RNG seeding.
- **Learning-based results** depend on released weights and inference data, not just source code.
- **Timings** — a first-class SIGGRAPH claim — depend on GPU/CPU, driver, and resolution.

If you cannot say exactly what a result depends on, you cannot make it reproducible.

## Pin provenance at creation time

These cannot be reconstructed after the fact:

- **Scenes and assets:** record the source and version of every scene, mesh, texture, and BRDF;
  ship them or give a stable download. A method evaluated on unshareable assets is unreproducible
  by construction — say so and provide a shareable proxy scene.
- **Seeds and configs:** log the seed, sample count, resolution, and every hyperparameter behind
  each figure. Store the config *with* the output, not in your memory.
- **Hardware and software stack:** GPU model, driver, CUDA/compiler versions, OS. Graphics timings
  are meaningless without them.
- **Model artifacts:** for learning-based work, pin the training data snapshot, the released
  weights' hash, and the inference command.

## Handle non-determinism honestly

Do not claim bit-exact reproduction you cannot deliver:

- **Declare the tolerance.** State whether a result is bit-exact, or matched within a metric
  (PSNR/SSIM/LPIPS/Hausdorff) and threshold, and bundle the reference output to compare against.
- **Seed the stochastic path** — Monte Carlo integration, stochastic simulation, dropout — and
  document the residual drift from GPU reductions or non-associative float math.
- **Separate deterministic and stochastic figures** so a reader knows which they can reproduce
  exactly and which only in distribution.

## The release a reader can run

```text
[README]      what it is; one command to build; one command to reproduce a headline figure;
              expected runtime and hardware
[Build]       pinned (Docker/conda/CMake) with exact GPU/driver/compiler versions
[Assets]      scenes/meshes/textures/weights bundled or stably linked
[repro/]      a script per headline figure: config in, image/metric/frame out, ref bundled
[MAPPING]     paper figure/table -> script -> expected output + tolerance
[LICENSE]     OSI-approved, so results can be reused and stamped
```

## Reproducibility vs. anonymity

SIGGRAPH Technical Papers review has historically been **single-blind** (reviewers see authors),
so the anonymization tax that ML/SE venues pay at review time is usually lighter here — **but
confirm the current cycle's blinding policy** (**待核实** for exact 2026 wording). If a cycle does
require anonymized review, strip owner strings, lab names, and identifying URLs from the code and
supplemental before upload, and swap in a de-anonymized permanent archive at camera-ready.

## Anti-patterns

- Reporting a timing with no hardware, or a quality number with no metric and no reference image.
- Shipping code without the scenes/meshes/weights it needs — it compiles but reproduces nothing.
- Claiming reproduction while leaving the sampler unseeded.
- Deferring the whole release to camera-ready, when provenance had to be pinned during the work.
- Treating "available upon request" as a release — it is a scored weakness, not a neutral choice.

## Output format

```text
[Result classes] images / meshes / simulation / learned / timings present
[Provenance] scenes+assets pinned? seeds+configs logged? hardware stack recorded? yes/no
[Determinism] tolerance stated + reference outputs bundled? yes/no
[Release] build + repro scripts + figure->script mapping present? yes/no
[Blinding] cycle policy confirmed (single-blind vs anonymized)? action if anonymized
[Gaps] <ordered, with what must be pinned before it is lost>
```
