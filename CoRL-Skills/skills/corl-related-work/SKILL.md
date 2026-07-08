---
name: corl-related-work
description: Use when positioning a CoRL paper against the literature — the robot-learning lineage across CoRL/RSS/ICRA, the ML-methods stream from NeurIPS/ICLR/ICML, the fast-moving VLA and foundation-model wave, classical robotics baselines, concurrent arXiv work, and PMLR citation hygiene including the year-offset trap.
---

# CoRL Related Work

Robot learning is a confluence field: any given CoRL paper inherits from at least
three literatures moving at different speeds. Reviewers here are typically expert
in one lane and conversant in the rest — so a related-work section that covers
only the authors' home lane reads as blinkered to a third of the pool.

## The three lanes, plus two overlays

| Lane | What reviewers check | Typical miss |
|---|---|---|
| Robot-learning lineage (CoRL, RSS, ICRA/IROS learning papers) | Do you know the last 2–3 years of the *task family* you claim? | Citing only your lab's chain of prior work |
| ML methods (NeurIPS/ICLR/ICML) | Is the algorithmic idea actually new, or a known method re-embodied? | Renaming an established technique with a robotics word |
| Classical robotics (planning, control, estimation) | Does a non-learning baseline solve your task? Why learn at all? | Dismissing model-based methods without citation or comparison |
| Overlay: foundation-model / VLA wave | Position relative to the current generation of pretrained robot policies | Comparing against a wave that is two generations stale |
| Overlay: concurrent arXiv | Preprint culture is aggressive here; overlap appears mid-review | Silence on a widely known concurrent preprint |

Practical breadth check: your citation list should contain entries from at least
two recent CoRL volumes, at least one ML venue, and at least one classical
robotics source — or an explicit reason why a lane is genuinely empty.

## Handling velocity: the field moves during your review

Between the late-May CoRL deadline and September decisions, the arXiv state of
your subfield will change. Norms to apply:

- Work that appeared publicly *after* your submission cannot be held against
  your novelty; if a reviewer raises it, note the dates factually in the rebuttal
  and offer a comparison in revision if it is genuinely relevant.
- Work that was on arXiv well *before* the deadline is fair game even without a
  venue stamp — this community treats known preprints as citable context. Sweep
  arXiv thoroughly in deadline month; "it wasn't published yet" does not excuse
  missing a preprint your reviewers all saw on social media.
- For close concurrent work, add a labeled paragraph ("Concurrent work") that
  differentiates on approach and evidence rather than priority claims.

## Positioning moves that work at this venue

- **Differentiate on evidence regime, not just method.** "Prior work
  demonstrates X in simulation; we provide the first real-robot evaluation with
  a measured transfer gap" is a legitimate and well-received axis here.
- **Name the assumption you remove.** "Existing approaches assume known object
  poses; we operate from raw RGB" — a robotics-meaningful delta beats an
  architecture tweak in this pool's eyes.
- **Give the task-family history one honest sentence of state-of-the-art**,
  including the best non-learning result. Erasing the classical solution to make
  the learning look necessary is a detectable and damaging move.
- **Baselines follow citations**: any method you describe as closest related
  work should appear in your tables, or the text should say why it cannot
  (`corl-experiments` covers fairness mechanics).

## PMLR citation hygiene — including the year-offset trap

CoRL proceedings publish through PMLR, and two mechanical errors recur:

1. **The year offset.** PMLR volumes sometimes carry a publication year after
   the conference year — e.g., the CoRL **2021** best paper (Chen et al.,
   in-hand re-orientation) is `PMLR v164, 2022`, and SayCan from CoRL **2022**
   appears with 2023 pagination metadata. Cite the conference edition in prose
   ("at CoRL 2021") even when the BibTeX year says otherwise, and keep the pair
   consistent across your references.
2. **Venue misattribution.** Neighboring PMLR volumes belong to different
   conferences; copying a BibTeX entry from a random site routinely mislabels a
   CoRL paper as appearing at another venue or vice versa. Resolve every robot
   learning citation against the volume index (v205 = CoRL 2022, v229 = 2023,
   v270 = 2024, v305 = 2025).

```bibtex
@inproceedings{chen2022inhand,
  title     = {A System for General In-Hand Object Re-Orientation},
  author    = {Chen, Tao and Xu, Jie and Agrawal, Pulkit},
  booktitle = {Proceedings of the 5th Conference on Robot Learning (CoRL 2021)},
  series    = {Proceedings of Machine Learning Research},
  volume    = {164},
  pages     = {297--307},
  year      = {2022},   % PMLR publication year != conference year — keep both visible
  publisher = {PMLR}
}
```

Prefer arXiv-to-PMLR upgrade passes before camera-ready: many robot-learning
papers you cited as preprints during writing will have acquired proceedings
entries by October.

## Double-anonymous self-citation

- Cite your own prior work in the third person, exactly as you would a
  stranger's; the giveaway is not the citation but the possessive framing
  ("building on our platform [12]").
- If the paper visibly extends a system with a recognizable name, do not
  amputate the citation — anonymity through omission breaks the scholarly
  record; third-person distance is the sanctioned tool.
- Watch transitive leaks: citing an unreleased internal report, a thesis, or a
  dataset only your lab could hold identifies you as surely as a name.

## Section-audit checklist

```text
[ ] All three lanes represented (or absence argued), plus VLA-wave currency
[ ] ≥2 recent CoRL volumes cited within the claimed task family
[ ] Best classical/non-learning approach acknowledged, compared or excused
[ ] Concurrent-work paragraph drafted if a known preprint is close
[ ] Every "closest work" citation appears in the experiments, or is excused
[ ] PMLR volume/year pairs verified against volume indexes; no misattribution
[ ] Self-citations third-person; no possessive framing; no transitive leaks
```

Verify volume anchors and any new proceedings arrangements at
https://proceedings.mlr.press/ and the live corl.org pages; this file's anchors
were checked 2026-07-08.
