# ITCS Resources

Action-oriented resources for the ITCS skill pack. The `skills/` give advice; this directory
lets an agent model an ITCS-shaped paper, benchmark against verified exemplars, and prepare a
lightweight double-blind LIPIcs submission whose central claims are fully proved.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before-to-after abstract/introduction rewrite for a **new-model** theory paper, executing the ITCS "innovation-first" arc. Illustrative fictional paper; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against real, verified ITCS/ICS papers across conceptual-contribution shapes, and avoid sibling-venue confusion with STOC, FOCS, SODA, CCC, and TCC. |
| [`official-source-map.md`](official-source-map.md) | Confirm the current-cycle ITCS deadline, format, review model, LIPIcs publication, and conceptual-novelty ethos before giving submission-ready advice. |
| [`external_tools.md`](external_tools.md) | Open the official ITCS, HotCRP, LIPIcs/DROPS, and preprint surfaces, plus the cross-check sources for when the gateway blocks a direct fetch. |
| [`code/README.md`](code/README.md) | Understand why this pure-theory pack ships **no code kit**, and the proof-checkability passes that replace an artifact/reproducibility package. |

## Scope Note

This is a **pure-theory** conference pack whose papers publish **open access in LIPIcs**
(Schloss Dagstuhl), not an empirical-CS, ML-conference, or economics pack. There is **no
artifact-evaluation track, no reproducibility package, and no experiments requirement**. Do not
import the OpenReview/PMLR machinery, the ACM/IEEE artifact-badging kit, or the
Stata/DiD/IV/RDD econometrics tooling. ITCS "evidence" is a **complete, checkable proof** and a
**new idea worth the community's attention**, carried through a lightweight double-blind,
**no-rebuttal** review.

## Suggested Workflow

1. Route and frame with
   [`../skills/itcs-topic-selection`](../skills/itcs-topic-selection/SKILL.md) and
   [`../skills/itcs-writing-style`](../skills/itcs-writing-style/SKILL.md) — deciding ITCS vs.
   STOC/FOCS/SODA on the *novelty axis* before writing is the highest-leverage move.
2. Prove and package with
   [`../skills/itcs-reproducibility`](../skills/itcs-reproducibility/SKILL.md),
   [`../skills/itcs-supplementary`](../skills/itcs-supplementary/SKILL.md), and — only if an
   illustrative simulation genuinely helps —
   [`../skills/itcs-experiments`](../skills/itcs-experiments/SKILL.md).
3. Benchmark against [`exemplars/library.md`](exemplars/library.md), then confirm the live cycle
   in [`official-source-map.md`](official-source-map.md) and
   [`external_tools.md`](external_tools.md) before the HotCRP audit in
   [`../skills/itcs-submission`](../skills/itcs-submission/SKILL.md).
