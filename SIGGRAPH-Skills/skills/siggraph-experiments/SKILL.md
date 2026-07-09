---
name: siggraph-experiments
description: Use when designing or auditing the evaluation of a SIGGRAPH / TOG paper, covering head-to-head comparisons against the strongest prior method, ablations, performance/timing reporting with hardware, image/geometry quality metrics, perceptual and user studies, and matching the evidence to the graphics claim shape.
---

# SIGGRAPH Experiments

SIGGRAPH acceptance turns on **evidence proportional to a graphics claim**: a technique that claims
to be faster must be timed against a real baseline on stated hardware; one that claims higher
quality must be compared, quantitatively and visually, against the strongest prior method. This
skill matches evaluation to claim shape and pre-empts the domain-expert reviewer's first
objections. Anchor policy to `resources/official-source-map.md`.

## Match evidence to the claim

| Claim shape | Evidence the reviewer expects | Common failure |
|---|---|---|
| "Higher quality" | Head-to-head vs SOTA with a metric (PSNR/SSIM/LPIPS/FLIP; Hausdorff/normal error for geometry) + side-by-side visuals + video | Only one's own results shown; no baseline |
| "Faster / real-time" | Wall-clock vs baseline at **equal quality**, with GPU/CPU, driver, resolution | Timing at unequal quality; no hardware stated |
| "More general / robust" | Results across a broad, non-cherry-picked scene set incl. hard cases | Works only on the paper's three easy inputs |
| "New capability" | Demonstrations prior methods provably cannot produce | Capability asserted, not shown against a method that fails |
| "Perceptually better" | A user/perceptual study with enough participants and a valid protocol | "Looks better" with no study |

## The comparison is the evaluation

In graphics, the head-to-head comparison against the **strongest** prior method is not optional:

- **Reproduce baselines faithfully.** Use authors' code and recommended settings; if you must
  reimplement, say so and match their reported numbers where possible. A weakened baseline is the
  objection that sinks the paper.
- **Equalize conditions.** Same scene, viewpoint, lighting, sample/time budget. When you give
  yourself or the baseline an advantage, disclose it.
- **Show the comparison both ways** — a metric table *and* a visual side-by-side (still + video);
  numbers and pixels persuade different reviewers.
- **Include the cases where you lose.** Bounding your method's regime is credibility, not weakness.

## Metrics, honestly

- **Images:** PSNR/SSIM for fidelity, LPIPS/FLIP for perceptual difference; state the reference and
  the region of interest. No single metric is sufficient — report several and show the images.
- **Geometry:** Hausdorff / mean surface distance, normal/curvature error, element quality; state
  the alignment and units.
- **Simulation/animation:** energy/momentum behavior, stability under time-step, constraint
  residuals; a plot over time, not a single frame.
- **Report variance** where results are stochastic (multiple seeds/runs), and **never** compare at
  unequal sample counts or resolutions without saying so.

## Performance and timing are first-class

Timings are claims a reviewer will check:

- Report **hardware** (GPU/CPU model, memory, driver), **resolution/scene size**, and **settings**
  for every timing.
- Break down where time goes (preprocess vs per-frame vs per-sample) so the claim is auditable.
- Compare speed **at matched quality** — "faster" at lower quality is not faster.

## Perceptual and user studies

When the claim is about perceived quality or usability:

- Pre-register the protocol; report participant count, task, stimuli, and the statistic (with a
  correction for multiple comparisons where relevant).
- Use a valid design (two-alternative forced choice, ranking, or a calibrated scale); report effect
  size and confidence intervals, not just significance.
- Put stimuli and raw responses in the supplemental for reproducibility.

## Ablations isolate the contribution

- Turn off each component in turn and show the quality/speed cost — this proves the contribution is
  the part you claim, not an incidental engineering detail.
- For learning-based methods, ablate architecture, loss terms, and data; run a **contamination
  check** so test scenes are not in training.
- Key ablation rows go in the body; the full grid goes to the supplemental (see
  `siggraph-supplementary`).

## Anti-patterns

- No comparison to the obvious strongest baseline.
- Timings with no hardware, or "faster" at unequal quality.
- A single cherry-picked scene standing in for generality.
- One metric asserted as quality with no images shown.
- A perceptual claim with no study, or a study with too few participants to support it.

## Output format

```text
[Claim -> evidence] each claim matched to comparison/metric/timing/study? yes/no
[Baselines] strongest prior method compared, faithfully, at equal conditions? yes/no
[Metrics] appropriate metrics + visuals/video for each quality claim? yes/no
[Timing] hardware/resolution/settings reported, matched-quality? yes/no
[Ablations] each component isolated; contamination checked (if learned)? yes/no
[Gaps] <ordered, with the reviewer objection each closes>
```
