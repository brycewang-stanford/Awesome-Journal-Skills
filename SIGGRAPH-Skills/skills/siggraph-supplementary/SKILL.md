---
name: siggraph-supplementary
description: Use when planning the SIGGRAPH / TOG supplemental package, especially the results video that reviewers weight heavily, plus comparison galleries, additional results, code and data, and appendices, and when deciding what evidence must live in the 7-page body versus the supplemental material.
---

# SIGGRAPH Supplementary

At SIGGRAPH the supplemental material — above all the **results video** — is not an appendix, it is
primary evidence. Motion, temporal coherence, interaction latency, and rendering artifacts simply
do not survive as still figures, and reviewers watch the video to judge them. This skill governs
the split between the reviewed body and the supplemental, and the craft of the video itself.
Anchor format rules to `resources/official-source-map.md`.

## The decision-criticality rule

The body is capped (Conference/dual-track: **<= 7 pages excluding references and two figures-only
pages**). The supplemental is generous. But **nothing that decides acceptance may depend on the
reviewer opening the supplemental** — a reviewer might weight the body most. So:

| Evidence | Where it lives |
|---|---|
| The core claim, method, and headline comparison | Body (the 7 pages) |
| The teaser and the key result figures | Body |
| Temporal/interactive results (animation, simulation, real-time) | **Video** — irreplaceable |
| Extended comparison galleries, more scenes, more ablations | Supplemental (additional results) |
| Derivations, proofs, parameter tables, network details | Appendix in supplemental |
| Code, trained weights, scenes/meshes, data | Supplemental (and camera-ready archive) |

Rule of thumb: if a reviewer must *see it move* to believe the claim, it is a video; if it merely
strengthens a claim the body already makes, it is supplemental; if losing it would change the
decision, it belongs in the body.

## The results video is a deliverable, not a screen recording

Reviewers form their impression of a graphics result in the first thirty seconds of the video.
Build it deliberately:

- **Open with the headline result**, side-by-side with the strongest prior method, on a scene the
  reader recognizes.
- **Show motion and temporal coherence** — flicker, popping, and instability are exactly what a
  static figure hides and a reviewer is hunting for. Do not cut away from a hard case.
- **Include failure cases.** A reviewer who finds an artifact you concealed distrusts everything;
  one who sees you show it trusts the rest.
- **Label everything on screen** — method name, scene, resolution, frames per second, and timing —
  because the video is watched without the paper in hand.
- **Keep comparisons fair:** same viewpoint, same lighting, same runtime budget; note where a
  baseline was given an advantage.
- **Respect rights and length:** you must hold permissions for every frame at submission; keep to
  the portal's size/length limits and a standard codec (H.264/MP4 is safest).

## Comparison galleries and additional results

Graphics reviewers expect breadth beyond the body's few figures:

- An **HTML comparison viewer** (image sliders / flip-books) lets a reviewer A/B your result
  against baselines at full resolution — far more convincing than downsized paper figures.
- Provide the **full scene set** you evaluated on, not only the cherry-picked ones, so the reviewer
  can check generality.
- Include **more ablation rows** than fit the body, each pinned to the paper's ablation table.

## Package layout

```text
supplemental/
  video.mp4              # results video, labeled, rights-cleared, <= portal limit
  comparisons/index.html # full-res A/B viewer vs each baseline
  additional_results/    # extra scenes, extra ablations, keyed to body figures
  appendix.pdf           # derivations, proofs, parameter/network tables
  code/                  # source + build (see siggraph-reproducibility)
  assets/                # scenes, meshes, textures, weights (or stable links)
  README.txt             # what each item is; which body claim it supports
```

## Anti-patterns

- A results video that is a muted slideshow of the paper's figures — it shows nothing new.
- Hiding the decisive comparison in supplemental while the body over-claims without it.
- An unlabeled video the reviewer cannot interpret without the PDF.
- Cherry-picked scenes with the failure set quietly omitted.
- Missing permissions on a single video frame — an ethics/production block.

## Output format

```text
[Body vs supplemental] each claim placed by decision-criticality? yes/no
[Results video] opens on headline+baseline? shows motion? failures included? labeled? rights cleared?
[Comparisons] full-res A/B viewer vs baselines present? full scene set included?
[Additional results] extra ablations/scenes keyed to body figures? yes/no
[Appendix] derivations/params moved out of the 7-page body? yes/no
[Fixes] <ordered>
```
