# ECCV Exemplars Library (topic × contribution type)

> **Verified via web search, access date 2026-07-08.** Every paper below was checked
> against **Springer LNCS proceedings records** (SpringerLink chapters/volumes or
> proceedings-cited page ranges) to confirm it appeared at the **European Conference
> on Computer Vision** specifically. Papers that could not be cleanly confirmed as
> ECCV main-conference work were **omitted and documented below**. Five verified
> rows beat fifteen guessed ones.
>
> **Big-three misattribution guard:** vision bibliographies constantly shuffle
> CVPR, ICCV, and ECCV. An LNCS-formatted PDF does not prove ECCV (workshops and
> other Springer venues use LNCS too), and a famous "vision paper" is as likely to
> live at a sibling venue — see the omissions list. Each row below names its
> Springer anchor.
>
> **Use principle (zero hallucination):** this file provides positioning patterns
> only. Reread the original before citing any number, and never quote results from
> this file. Policy facts live in [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row nearest your topic × contribution type, then study how the paper
earns flagship-venue attention: a reusable mechanism or resource, evidence that
outlived its submission cycle, and first-page clarity for a mixed vision panel
(see [`../../skills/eccv-topic-selection/SKILL.md`](../../skills/eccv-topic-selection/SKILL.md)
and [`../../skills/eccv-writing-style/SKILL.md`](../../skills/eccv-writing-style/SKILL.md)).
Each entry ends with a self-check question.

---

## Verified exemplars

### Dataset / benchmark contribution

- **Lin, Maire, Belongie, Hays, Perona, Ramanan, Dollár & Zitnick, "Microsoft COCO:
  Common Objects in Context," ECCV 2014.** Springer anchor: ECCV 2014 Part V,
  LNCS vol. 8693, pp. 740–755.
  - **Why it is an exemplar:** a dataset paper that defined a decade of detection
    and segmentation evaluation — the strongest proof that ECCV treats a
    well-built resource as a first-class contribution, not a workshop artifact.
  - **Self-check:** does your dataset paper specify collection, annotation, and
    evaluation protocol precisely enough to referee a decade of methods, and is
    hosting planned beyond one conference cycle?

### Practical detector / speed-accuracy engineering with an idea

- **Liu, Anguelov, Erhan, Szegedy, Reed, Fu & Berg, "SSD: Single Shot MultiBox
  Detector," ECCV 2016.** Springer anchor: ECCV 2016 (Amsterdam, Oct 11–14) Part I,
  pp. 21–37.
  - **Why it is an exemplar:** engineering-forward, but built on one isolable
    design idea (multi-scale default boxes, no proposal stage) that ablates
    cleanly — the difference between integration work and an ECCV paper.
  - **Self-check:** if you remove your paper's single named idea, does the
    performance story collapse? If nothing collapses, there is no idea yet.

### Loss / training-signal contribution

- **Johnson, Alahi & Fei-Fei, "Perceptual Losses for Real-Time Style Transfer and
  Super-Resolution," ECCV 2016.** Springer anchor: LNCS vol. 9906, chapter DOI
  10.1007/978-3-319-46475-6_43.
  - **Why it is an exemplar:** relocates the contribution from architecture to
    the *objective*, with speed as the measurable payoff — a template for papers
    whose novelty is what is optimized rather than what is built.
  - **Self-check:** is your contribution stated at the right layer (data, loss,
    architecture, inference), and do the ablations toggle exactly that layer?

### Representation shift

- **Mildenhall, Srinivasan, Tancik, Barron, Ramamoorthi & Ng, "NeRF: Representing
  Scenes as Neural Radiance Fields for View Synthesis," ECCV 2020.** Springer
  anchor: Computer Vision – ECCV 2020, pp. 405–421 (chapter DOI
  10.1007/978-3-030-58452-8_24).
  - **Why it is an exemplar:** replaces a data structure (discrete geometry) with
    a learned continuous field, spawning an entire subfield — the ceiling case of
    the durability test in `eccv-topic-selection`.
  - **Self-check:** does your paper change what the field optimizes over, or
    only how well one benchmark is scored?

### Well-engineered core-vision method (award lineage)

- **Teed & Deng, "RAFT: Recurrent All-Pairs Field Transforms for Optical Flow,"
  ECCV 2020 — Best Paper Award.** Springer anchor: ECCV 2020 (16th, Glasgow,
  Aug 23–28) Part II, pp. 402–419.
  - **Why it is an exemplar:** revisits a classical problem (optical flow) with a
    clean iterative architecture and dominant, carefully evaluated results —
    evidence that ECCV's top honors go to core-vision rigor, not only to trends.
  - **Self-check:** does your evaluation cover the classical protocol of the
    task in full, or only the slices where the method shines?

---

## Topic × contribution grid

| Topic | Verified ECCV exemplar | Edition / Springer anchor | Contribution type |
| --- | --- | --- | --- |
| Recognition infrastructure | Microsoft COCO | 2014 / LNCS 8693:740–755 | Dataset + evaluation protocol |
| Object detection | SSD | 2016 / Part I:21–37 | Single-idea practical method |
| Image synthesis | Perceptual Losses | 2016 / LNCS 9906, ch. 43 | Objective/loss design |
| Novel view synthesis | NeRF | 2020 / pp. 405–421 | Representation shift |
| Optical flow | RAFT | 2020 / Part II:402–419 | Core-vision method (Best Paper) |

> The 2014 → 2020 spread also shows the venue's even-year memory: each exemplar
> was still the reference point at the *following* ECCV, which is the durability
> bar `eccv-topic-selection` asks you to price in.

---

## Omitted for lack of clean ECCV verification (do not attribute without checking)

- **Carion et al., "End-to-End Object Detection with Transformers" (DETR)** —
  widely cited as ECCV 2020, but its Springer record was not cleanly confirmed in
  this verification pass. 待核实 before attributing; do not cite venue from memory.
- **He, Zhang, Ren & Sun, "Deep Residual Learning" (ResNet)** — **CVPR 2016**,
  not ECCV. (The related "Identity Mappings" paper is reputedly ECCV 2016 —
  verify on SpringerLink before using it.)
- **Mask R-CNN** — **ICCV 2017**. A standing big-three trap.
- **Faster R-CNN** — **NeurIPS 2015**, despite living in every vision bibliography.
- **U-Net** — **MICCAI 2015** (also Springer LNCS — format proves nothing).
- **ViT ("An Image is Worth 16×16 Words")** — **ICLR 2021**.

Before adding a row: find the paper's SpringerLink chapter or the proceedings
volume that names "European Conference on Computer Vision", record edition, LNCS
volume, and pages, and update the access-date header. If verification fails, add
it to this omissions list instead — never promote a guess.
