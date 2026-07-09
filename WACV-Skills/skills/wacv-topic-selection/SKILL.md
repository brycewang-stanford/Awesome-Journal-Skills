---
name: wacv-topic-selection
description: Use when deciding whether a project belongs at WACV or should route elsewhere, covering WACV's applications-first identity within the CVF's CVPR/ICCV/ECCV/WACV calendar, the Applications-vs-Algorithms track choice, whether the two-round winter timing fits your schedule, and routing to CVPR, ICCV, ECCV, 3DV, or a journal.
---

# WACV Topic Selection

WACV is the **applications-first winter member** of the Computer Vision Foundation's
four-venue calendar (CVPR in June, ICCV/ECCV alternating in autumn, WACV in winter). This
skill decides *whether* to send a paper here — and, if so, *which track* — before other
skills decide *how*. Facts are the WACV 2026/2027 cycles as read on 2026-07-09.

## The core question

Ask two things in order. First: **is the contribution about applying computer vision to a
real problem, or advancing vision method for its own sake?** WACV's name — *Applications of
Computer Vision* — is a genuine editorial stance, and its Applications track exists to
review systems that work under real constraints. Second: **does the winter, two-round
calendar fit your timeline better than waiting for a single-deadline sibling?** A paper that
is nearly ready in mid-summer can enter WACV Round 1 and, if close, be invited to revise —
rather than sitting until the next CVPR cycle.

## Routing across the CVF calendar (from WACV's seat)

| You have… | WACV-shaped if… | Route elsewhere if… |
|---|---|---|
| A vision system for a real domain (agriculture, medical, retail, robotics) under real constraints | The constraint (power, data scarcity, in-the-wild robustness) is the contribution | It is a generic method with an arbitrary demo domain → CVPR/ICCV/ECCV |
| A new architecture / algorithm | It advances a vision mechanism and you want the winter slot and the R&R net | It is a field-defining method aimed at the largest audience → CVPR |
| A benchmark / re-evaluation of a deployed task | It corrects how a real task is measured or constrained | It is a broad foundation-model benchmark → a larger venue |
| A 3D / geometry contribution | It is applied and constraint-driven | It is core 3D reconstruction method → 3DV or CVPR |
| A theory / learning result with a vision demo | *(rarely WACV)* | The claim is statistical/learning-theoretic → NeurIPS/ICML/AISTATS |

WACV is not a "CVPR reject bin." It is a real venue with its own applications identity, a
respectable acceptance profile, and a review model designed to *improve* papers across two
rounds rather than gate them once.

## Choosing the track

Once WACV is the answer, the track is the next decision, and it changes how you write the
first page:

- **Applications track** — reviewed on **systems-level innovation, novelty of the
  application domain, and comparative assessment** under real-world constraints (low-power
  inference, data scarcity, robustness in the wild). Choose this when the value is that the
  system *works under a named constraint*, not that the math is new.
- **Algorithms track** — reviewed on **algorithmic novelty and quantified evaluation against
  current alternatives**. Choose this when you introduce a genuinely new method or
  architecture and can show matched-baseline wins.

Authors pick **one primary track**. If a paper seems to fit both, choose the track where the
contribution is stronger, and frame the first page to argue for that lens — a mis-tracked
paper draws the wrong review question and heads for Revise and Resubmit.

## A quick self-test

```text
Is the deployment constraint the point?           yes → Applications track, WACV strong
Is a new vision mechanism the point?              yes → Algorithms track (WACV) or CVPR/ICCV/ECCV
Is vision only the demo for a learning claim?     yes → route to NeurIPS/ICML/AISTATS
Do you want a revision path if you're close?      yes → WACV Round 1 fits
Is the claim about a non-vision modality's math?  yes → not WACV
```

## Reverify each cycle

- The two-track structure and each track's review criteria.
- WACV's place and timing in the CVF calendar and the two-round dates.
- Whether the winter cycle's deadlines actually beat your next sibling-venue option.

## Output format

```text
[Verdict] WACV / route to <CVPR|ICCV|ECCV|3DV|journal|other>
[Why] <one line: applications-under-constraint vs method-for-its-own-sake>
[Track if WACV] Applications / Algorithms — because <criterion match>
[Timing] winter two-round fits: yes/no
[Risk] <the reviewer question this framing must pre-empt>
```
