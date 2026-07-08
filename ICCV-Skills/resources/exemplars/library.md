# ICCV Exemplars Library (era × contribution type)

> **Verified via web search on 2026-07-08.** Every row below was checked to have appeared
> at the **IEEE/CVF International Conference on Computer Vision (ICCV)** specifically —
> against dblp `conf/iccv` records, CVF open-access paper pages, and (for award facts)
> the PAMI-TC awards page — not merely "a top vision venue." Papers whose ICCV placement
> could not be cleanly confirmed were left out; the guard list at the bottom exists
> because the vision big three (CVPR/ICCV/ECCV) are the most misattributed venues in
> machine-learning bibliographies.
>
> **Zero-hallucination use principle:** this library provides positioning patterns only.
> It states no benchmark numbers, no architecture details beyond the one-line mechanism,
> and nothing you should cite without opening the paper itself on CVF open access or
> IEEE Xplore.

---

## How to use this library

Because ICCV is biennial, its exemplars double as a time-lapse of what the venue's
juries considered field-defining, era by era. Find the row nearest your contribution
type, then ask the row's question of your own draft. Pair with
[`../../skills/iccv-topic-selection/SKILL.md`](../../skills/iccv-topic-selection/SKILL.md)
(the Marr Prize lineage as a taste signal) and
[`../../skills/iccv-related-work/SKILL.md`](../../skills/iccv-related-work/SKILL.md)
(venue-attribution hygiene).

## The verified rows

### Local features era — Lowe, "Object Recognition from Local Scale-Invariant Features," ICCV 1999

Verified: dblp `conf/iccv/Lowe99` (Proceedings of the Seventh IEEE International
Conference on Computer Vision, pp. 1150–1157). The SIFT lineage's conference debut: a
*representation* (scale-invariant local features) framed by the capability it unlocks
(recognition in clutter and occlusion).
**Ask of your draft:** does the paper sell the reusable representation, or only the
end-task score?

### Instance segmentation — He, Gkioxari, Dollár, Girshick, "Mask R-CNN," ICCV 2017 (Marr Prize)

Verified: ICCV 2017 best-paper award coverage and CVF open access ICCV 2017 listing. A
minimal extension of an existing detector family that created a new standard task
interface; its award shows ICCV rewards *clean generality*, not maximal novelty
theater.
**Ask of your draft:** is the mechanism simple enough that every lab can adopt it by
the next cycle?

### Unpaired translation — Zhu, Park, Isola, Efros, "Unpaired Image-to-Image Translation Using Cycle-Consistent Adversarial Networks" (CycleGAN), ICCV 2017

Verified: CVF open access ICCV 2017 paper page; authors' project page states ICCV 2017.
Reframed a data requirement (paired supervision) as the thing to eliminate — the
contribution is the *removed assumption*, made trainable by a cycle constraint.
**Ask of your draft:** can you name the assumption you delete, and what enforces
consistency once it is gone?

### Backbone architecture — Liu, Lin, Cao, Hu, Wei, Zhang, Lin, Guo, "Swin Transformer: Hierarchical Vision Transformer using Shifted Windows," ICCV 2021 (Marr Prize)

Verified: Marr Prize 2021 announcements (USTC/press) and CVF open access ICCV 2021
listing. A general-purpose backbone argued through breadth: one design evaluated
across classification, detection, and segmentation.
**Ask of your draft:** if you claim generality, does the evidence span tasks the way a
backbone paper's must?

### Controllable generation — Zhang, Rao, Agrawala, "Adding Conditional Control to Text-to-Image Diffusion Models" (ControlNet), ICCV 2023 (Marr Prize)

Verified: ICCV 2023 best-paper announcements and CVF open access ICCV 2023 listing. A
mechanism for steering frozen pretrained generators — the foundation-model-era pattern
of contributing *around* a large model rather than retraining one.
**Ask of your draft:** does your method respect the frozen-backbone reality of current
practice, and show what control it adds at what cost?

### Promptable segmentation at scale — Kirillov et al., "Segment Anything," ICCV 2023

Verified: CVF open access ICCV 2023 paper page
(`openaccess.thecvf.com/content/ICCV2023/html/Kirillov_Segment_Anything_ICCV_2023_paper.html`).
Task + model + dataset shipped as one artifact; the release itself became field
infrastructure — the modern ceiling for what `iccv-artifact-evaluation` calls the
release runway.
**Ask of your draft:** if the dataset or model is the contribution, is the release
plan engineered to the same standard as the method?

### Physical construction from text — Pun, Deng, R. Liu, Ramanan, C. Liu, Zhu, "Generating Physically Stable and Buildable Brick Structures from Text" (BrickGPT), ICCV 2025 (Marr Prize)

Verified: ICCV 2025 award announcements (official account and CMU coverage). The most
recent Marr Prize: generation constrained by *physical feasibility* — a reminder that
the venue's top award often goes to a new capability with a checkable correctness
criterion, not to a leaderboard increment.
**Ask of your draft:** what external criterion (physics, geometry, human use) would
prove your outputs right or wrong?

## Era × type matrix

| Era | Contribution type | Exemplar | Cycle |
| --- | --- | --- | --- |
| Classical | Representation | Lowe, scale-invariant local features | 1999 |
| Deep detection | Task-interface method | Mask R-CNN | 2017 |
| GAN | Assumption-removal method | CycleGAN | 2017 |
| Transformer | General backbone | Swin Transformer | 2021 |
| Foundation-model | Control mechanism | ControlNet | 2023 |
| Foundation-model | Task+model+data artifact | Segment Anything | 2023 |
| Generative-physical | Constrained generation | BrickGPT | 2025 |

## Do-not-misattribute guard list

Confusable landmarks that are **not** ICCV papers — never cite them as ICCV, and use
them to spot-check any machine-generated bibliography:

- **ResNet** — CVPR 2016. **YOLO** — CVPR 2016. **Latent diffusion (Stable
  Diffusion's paper)** — CVPR 2022.
- **NeRF** — ECCV 2020.
- **ViT** ("An Image is Worth 16×16 Words") — ICLR 2021.
- **Faster R-CNN** — NeurIPS 2015 (its predecessor Fast R-CNN *is* ICCV 2015 — the
  R-CNN family spans three venues, which is exactly how misattributions start).
- **U-Net** — MICCAI 2015.

## Maintenance recipe

To add a row: confirm the paper on CVF open access under an `ICCV<year>` path or in a
dblp `conf/iccv` record (title, authors, year); for award claims, check the PAMI-TC
awards page; then state the mechanism in one line and write the row's self-check
question. Update the access date in the header. If verification is ambiguous between
siblings, put the paper on the guard list instead — a wrong exemplar does more damage
here than a missing one. If web access is unavailable, add nothing.
