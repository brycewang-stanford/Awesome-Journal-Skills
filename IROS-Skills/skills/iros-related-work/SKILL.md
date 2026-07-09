---
name: iros-related-work
description: Use when positioning an IROS submission against robotics-systems literature across ICRA, IROS, RSS, CoRL, RA-L, and T-RO, covering the lanes embodied-systems reviewers check, concurrent arXiv work, prior-version overlap, IEEE Xplore archival status, and keeping self-citations anonymous under the double-anonymous cycle.
---

# IROS Related Work

Use this to audit novelty and eligibility. Reopen the current CFP for dual-submission, anonymity, and
prior-publication rules before advising authors. At IROS the question a reviewer asks is not only "is
this new?" but "does the paper know the nearest *systems* it resembles and say what it does
differently?"

## Positioning checks

- Separate a **systems contribution** from a component tweak: a new integration, a new capability under a
  constraint, a new reliability level, or a deployment insight — not merely a swapped module.
- Cover the robotics-systems lanes, not just the one nearest your method; a manipulation paper still owes
  the perception and planning neighbors it builds on.
- Treat **IEEE Xplore proceedings, RA-L, and T-RO** as archival; position against them honestly rather
  than around them.
- Cite arXiv and prior workshop versions so **double-anonymous review survives** — never point a reviewer
  to an identity-revealing page or repository.
- Explain overlap with any prior or concurrent version of your own work, and do not submit duplicate
  archival material.

## The lanes robotics reviewers check

| Lane | Typical sources | What IROS reviewers check |
|---|---|---|
| Conference systems | ICRA, prior IROS, RSS, CoRL | Whether the nearest deployed system is compared or explicitly distinguished |
| Robotics journals | RA-L, T-RO, T-ASE, IJRR, Autonomous Robots | Whether mature, revised results are acknowledged, not dodged |
| Perception/learning | CVPR/ICCV, NeurIPS/ICML when a component derives from them | Whether a borrowed component is credited and evaluated in the robotics setting |
| Field/application | Domain venues (field robotics, medical, aerial) | Whether deployment realities and prior fielded systems are cited |

A bibliography citing only your own subfield tells a reviewer the paper may be re-deriving a neighboring
system's idea — a recognizable IROS weakness no amount of demo polish repairs.

## Concurrent-work judgment calls

- Independently concurrent arXiv work: cite neutrally, state the technical difference, and avoid
  priority claims a reviewer cannot verify.
- Your own workshop version: usually non-archival and citable, but verify against the current CFP and
  phrase the citation so anonymity holds.
- When unsure whether a venue counts as archival for dual-submission, declare the overlap in the
  submission form rather than gambling on an editor's read.

## Positioning vignette

Imagine the paper presents a lidar-inertial state estimator that runs on an embedded computer. Its
nearest neighbors: a prior IROS lidar-odometry system it extends, an RA-L fusion method with a heavier
compute footprint, and a CVPR learned-odometry component it borrows a front end from. The novelty
sentence should name all three contrasts — tighter fusion than the IROS predecessor, a smaller compute
budget than the RA-L method, and the learned front end credited and re-evaluated on real field data.

```text
Novelty sentence template:
  "Unlike <nearest system> which <limitation>, our system <capability>
   under <embodiment constraint>, evidenced by <embodied result>."
```

## Output format

```text
[Eligibility] clear / needs declaration / risky
[Closest lanes] <conference/journal/perception/field>
[Nearest 3 systems] <system -> distinction>
[Archival-overlap risk] <none/issues>
[Novelty sentence] <IROS-ready systems contrast>
```
