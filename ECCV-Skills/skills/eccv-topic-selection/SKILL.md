---
name: eccv-topic-selection
description: Use when deciding whether a computer-vision project should target ECCV — weighing the two-year even-year cadence against CVPR, ICCV, WACV, BMVC, ACCV, NeurIPS, and journal routes, testing whether the work matches ECCV's breadth from geometry to vision-language, and reading the Koenderink Prize lineage as a durability signal.
---

# ECCV Topic Selection

Use this before committing a project to ECCV. The fit question has two
layers: *is this an ECCV-shaped paper* (scope, evidence, durability), and
*is the even-year calendar the right bet* — because choosing ECCV means the
next chance at this venue is two years away, and the same March deadline
usually competes with an ICCV or CVPR alternative for the identical result.

## Scope: what ECCV-shaped means

ECCV is a general vision flagship with a strong geometric and European
heritage: 3D reconstruction, SLAM/SfM, optical flow, recognition,
segmentation, video, generative models, vision-language, embodied and
applied vision all live in its LNCS volumes. The historical taste signal:
ECCV's proceedings carried COCO (2014), SSD and Perceptual Losses (2016),
and NeRF and RAFT (2020) — datasets, practical detectors, and
representation shifts, not just incremental leaderboard entries. ECVA's
**Koenderink Prize** honors a ten-year-old ECCV paper each edition; asking
"could this matter in ten years?" is a good severity filter for whether the
contribution is a mechanism or a configuration.

## The calendar layer

| Situation | Reading |
|---|---|
| Result ready by February of an even year | ECCV is live; decide vs the same-spring alternatives |
| Result ready in an odd year | ICCV (March) or CVPR (November) — holding a year for ECCV rarely beats publishing |
| Work is solid but not flagship-tier | BMVC or WACV now beats a two-year ECCV gamble |
| Contribution needs >14 LNCS pages of development | IJCV or TPAMI; conference length will amputate it |
| Learning contribution where vision is one testbed | NeurIPS/ICML/ICLR panels will value it more precisely |
| Dataset/benchmark contribution | Strong ECCV genre (COCO precedent) — but plan hosting beyond the cycle |

## Five questions before committing

1. **Breadth**: can the contribution be motivated to a mixed vision panel in
   one page, or does it need a subfield's shared context? (Narrow-deep work
   often fares better at a specialist venue or journal.)
2. **Durability**: will the claim survive from the March freeze to the
   September conference — and, for the venue's memory, to the next even
   year? (`eccv-experiments` staleness test.)
3. **Substrate independence**: is the win a mechanism, or a particular
   pretrained backbone's gift? Mechanism papers age across the biennial gap;
   substrate papers do not.
4. **Evidence budget**: can you fill 14 LNCS pages (figures included) with
   matched-substrate comparisons, isolating ablations, and honest failures
   by early March?
5. **Team exposure**: are all co-authors able to carry ECCV reviewer duty in
   April–June? The 2026 rules made co-author reviewing behavior a paper
   risk.

## Anti-fit signals

- The pitch depends on beating a SOTA number that three groups are visibly
  chasing — it will be stale by September.
- The core contribution is engineering integration without an isolable idea
  — strong WACV/demo material, weak flagship material.
- The paper's audience is one company's product context rather than the
  research community.

## Decision procedure

```text
1. Write the one-sentence contribution: "Given <input>, we <mechanism>,
   which yields <capability> that <prior family> cannot."
2. If the sentence needs a benchmark name to be interesting -> not ECCV.
3. Check the calendar table above for the earliest venue whose deadline
   the evidence budget can meet honestly.
4. If ECCV and another venue tie, price the option: ECCV slip = 2 years
   at this venue; CVPR slip = 1 year. Choose the venue whose slip you
   can afford.
5. Commit and hand the date chain to eccv-workflow.
```

## Output format

```text
[Fit verdict] ECCV-shaped / better at <venue> / needs maturation
[Scope test] <one-sentence contribution + mixed-panel motivation check>
[Calendar bet] <even-year timing vs alternatives, slip cost>
[Durability risks] <substrate dependence, SOTA-chase exposure>
[Commit decision] <venue + deadline + first falsifier experiment>
```
