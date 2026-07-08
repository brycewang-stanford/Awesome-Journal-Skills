# ICRA Exemplars Library (topic × era)

> **Verified via web search, access date 2026-07-08.** Every paper below was checked
> against IEEE Xplore / ACM Digital Library proceedings records (DOI, venue string,
> city, pages) to confirm it appeared in the **IEEE International Conference on
> Robotics and Automation** specifically. Deliberately short: 5 verified beats 15
> guessed.
>
> **Sibling-confusion guard:** robotics classics scatter across ICRA, IROS, RSS,
> CoRL, ISER, and the journals T-RO / IJRR / RA-L — and many works exist in *both* a
> conference and a journal version. Famous traps checked and excluded below: LOAM is
> **RSS 2014**, ORB-SLAM's archival home is **T-RO**, and the KITTI benchmark paper
> is **CVPR 2012**. An "everyone knows it's ICRA" feeling is not verification.
>
> **Use principle (zero hallucination):** this library gives design positioning
> only. It does not restate results, numbers, or claims beyond what identifies the
> paper — read the original on IEEE Xplore before citing anything technical.

---

## How to use this library

Find the row nearest your paper's topic and era, then study how that paper's first
page states a **robot task, a physical difficulty, and a checkable contribution** —
the bar described in [`../../skills/icra-writing-style/SKILL.md`](../../skills/icra-writing-style/SKILL.md)
and evidenced per [`../../skills/icra-experiments/SKILL.md`](../../skills/icra-experiments/SKILL.md).
Each entry ends with a self-check question to ask of your own draft.

## Verified exemplars

### Sampling-based motion planning (classical era)

- **Kuffner & LaValle, "RRT-Connect: An Efficient Approach to Single-Query Path
  Planning," ICRA 2000, San Francisco, pp. 995-1001.**
  Verified: DOI `10.1109/ROBOT.2000.844730` (Proceedings 2000 ICRA "Millennium
  Conference").
  - **Why it is an exemplar:** a compact algorithmic idea — two trees grown toward
    each other with a greedy connect heuristic — stated so cleanly it became
    infrastructure. The paper form to study when your contribution is one sharp
    algorithm rather than a system.
  - **Self-check:** can your algorithm be specified completely in pseudo-code that
    fits half a column, and does the paper say exactly that much?

### Trajectory optimization for manipulation

- **Ratliff, Zucker, Bagnell & Srinivasa, "CHOMP: Gradient Optimization Techniques
  for Efficient Motion Planning," ICRA 2009, pp. 489-494.**
  Verified: CMU Robotics Institute publication record and proceedings listings;
  journal successor in IJRR 2013 (cite the version you mean).
  - **Why it is an exemplar:** repositions planning as covariant gradient
    optimization over trajectories — a reframing contribution whose value is argued
    on robot platforms, not just benchmarks. Also a model of the
    conference-paper-then-journal-expansion arc this pack recommends for
    derivation-heavy work.
  - **Self-check:** if your paper reframes a known problem, does it demonstrate the
    payoff of the reframing on hardware the community recognizes?

### Fiducials / perception infrastructure

- **Olson, "AprilTag: A Robust and Flexible Visual Fiducial System," ICRA 2011,
  Shanghai, pp. 3400-3407.**
  Verified: April Robotics Laboratory (U. Michigan) publication record and DL
  listings.
  - **Why it is an exemplar:** an unglamorous tool paper — a tag family and
    detector — accepted because it measured itself rigorously (occlusion, warping,
    distortion robustness) and shipped as usable infrastructure. Proof that ICRA
    rewards tools the field adopts, an encouraging precedent for dataset/benchmark
    submissions.
  - **Self-check:** does your tool paper quantify robustness on the axes users will
    actually stress, and is the artifact release ready on day one?

### SLAM at production quality

- **Hess, Kohler, Rapp & Andor, "Real-Time Loop Closure in 2D LIDAR SLAM,"
  ICRA 2016, Stockholm, pp. 1271-1278.**
  Verified: DOI `10.1109/ICRA.2016.7487258`.
  - **Why it is an exemplar:** the paper behind the Cartographer system — an
    engineering-forward contribution (real-time loop closure via branch-and-bound
    scan matching) whose experimental section compares against established methods
    on public data and whose code release amplified its impact. The template for
    systems papers per [`../../skills/icra-artifact-evaluation/SKILL.md`](../../skills/icra-artifact-evaluation/SKILL.md).
  - **Self-check:** does your systems paper prove competitiveness against named
    established approaches, not just self-baselines?

### Robot learning on hardware (modern era)

- **Nair, McGrew, Andrychowicz, Zaremba & Abbeel, "Overcoming Exploration in
  Reinforcement Learning with Demonstrations," ICRA 2018, Brisbane,
  pp. 6292-6299.**
  Verified: DOI `10.1109/ICRA.2018.8463162`.
  - **Why it is an exemplar:** a learning-method paper that earned its ICRA slot by
    grounding the RL contribution in robotics tasks (simulated manipulation with a
    physical-robot demonstration), showing how learning work is framed for a
    robotics reviewer pool rather than an ML one — the routing question in
    [`../../skills/icra-topic-selection/SKILL.md`](../../skills/icra-topic-selection/SKILL.md).
  - **Self-check:** if your paper is learning-first, does the robotics framing
    survive the embodiment test, or does it read as an ML paper wearing a gripper?

## Topic × era table

| Topic lane | Verified ICRA exemplar | Year / venue city / pages | Era lesson |
| --- | --- | --- | --- |
| Motion planning (algorithm) | RRT-Connect, Kuffner & LaValle | 2000 / San Francisco / 995-1001 | one sharp algorithm suffices |
| Trajectory optimization | CHOMP, Ratliff et al. | 2009 / Kobe cycle / 489-494 | reframing + hardware payoff |
| Perception infrastructure | AprilTag, Olson | 2011 / Shanghai / 3400-3407 | measured tools get adopted |
| SLAM / systems | Real-Time Loop Closure, Hess et al. | 2016 / Stockholm / 1271-1278 | systems need named rivals |
| Learning + demonstrations | Overcoming Exploration, Nair et al. | 2018 / Brisbane / 6292-6299 | learning framed for robotics |

## Checked and excluded (do not attribute to ICRA)

- **Zhang & Singh, "LOAM: Lidar Odometry and Mapping in Real-time"** — **RSS
  2014**, not ICRA. The most common lidar-SLAM misattribution.
- **Mur-Artal et al., "ORB-SLAM"** — archival home **IEEE T-RO (2015)**; do not
  cite the journal paper as an ICRA paper.
- **Geiger et al., "Are we ready for autonomous driving? The KITTI vision benchmark
  suite"** — **CVPR 2012**, despite its centrality to robotics.

Before adding a row, verify on IEEE Xplore that the DOI resolves to an ICRA
proceedings entry (`10.1109/ICRA.*` or legacy `10.1109/ROBOT.*`), record city,
pages, and access date, and when verification fails, either omit the paper or add
it as 待核实 with no attribution.
