# IROS Exemplars Library (topic × system)

> **Verified via web search, access date 2026-07-09.** Every paper below was checked against its
> **IEEE Xplore / ACM Digital Library proceedings record** to confirm it appeared in the **IEEE/RSJ
> International Conference on Intelligent Robots and Systems (IROS)** — matching the DOI to the IROS
> edition, plus author list, year, host city, and page range. Papers that could not be cleanly confirmed
> as **IROS** (as opposed to ICRA, RSS, CoRL, RA-L, or a journal) were **omitted and documented below**.
> It is deliberately a short, verified list (5 verified > 20 guessed).
>
> **Sibling-confusion guard:** IROS is **not** ICRA, RSS, CoRL, or RA-L, and it is not a journal.
> Several famous robotics papers people "remember as IROS" actually live in those venues — a
> `10.1109/IROS.*` DOI is the only proof, and a `10.1109/ROBOT.*` or `10.1109/ICRA.*` DOI is the ICRA
> tell (see omissions). Each row below carries an IROS DOI checked individually.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent results, ablation numbers, or trajectory-error figures — read the original in IEEE
> Xplore before citing anything. For IROS-specific policy and the do-not-misattribute list, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **topic × system** is closest to yours, then study how that paper puts a **working
robotic capability on the first page** — a system that runs, on stated hardware, evaluated on a real or
standardized dataset with error metrics — the IROS bar (see
[`../../skills/iros-writing-style/SKILL.md`](../../skills/iros-writing-style/SKILL.md),
[`../../skills/iros-topic-selection/SKILL.md`](../../skills/iros-topic-selection/SKILL.md), and
[`../../skills/iros-experiments/SKILL.md`](../../skills/iros-experiments/SKILL.md)). For each, ask the
self-check question before claiming your paper is "IROS-shaped."

---

## By system

### Standardized evaluation / dataset (perception + SLAM tooling)

- **Sturm, Engelhard, Endres, Burgard & Cremers, "A Benchmark for the Evaluation of RGB-D SLAM
  Systems," IROS 2012, Vilamoura, pp. 573-580.** Verified: DOI `10.1109/IROS.2012.6385773`.
  - **Why it is an exemplar:** the contribution is **infrastructure** — motion-capture ground truth plus
    a defined error metric (absolute trajectory error) that let a whole community compare SLAM systems on
    equal terms. IROS rewards tooling that other robotics work is forced to adopt.
  - **Self-check:** does your benchmark define the metric *and* the protocol precisely enough that a
    competitor cannot game it, and is the ground truth independently trustworthy?

### Volumetric mapping for on-board planning (representation)

- **Oleynikova, Taylor, Fehr, Nieto & Siegwart, "Voxblox: Incremental 3D Euclidean Signed Distance
  Fields for On-Board MAV Planning," IROS 2017, Vancouver.** Verified: DOI `10.1109/IROS.2017.8202315`.
  - **Why it is an exemplar:** it earns its place by running **on-board, in real time, on one CPU core**,
    and by tying the map representation directly to what a trajectory optimizer needs. The system
    constraint (compute budget on a flying robot) *is* the contribution's frame.
  - **Self-check:** is your representation justified by an embodied constraint (onboard compute, latency,
    memory) rather than by offline accuracy alone?

### Lidar odometry on a ground vehicle (state estimation under an embodiment)

- **Shan & Englot, "LeGO-LOAM: Lightweight and Ground-Optimized Lidar Odometry and Mapping on Variable
  Terrain," IROS 2018, Madrid, pp. 4758-4765.** Verified: DOI `10.1109/IROS.2018.8594299`.
  - **Why it is an exemplar:** it exploits a **specific embodiment assumption** — a ground plane — to run
    six-DoF estimation on a low-power embedded computer. The paper is honest that the assumption both
    buys the speed and bounds the applicability.
  - **Self-check:** does your method name the embodiment assumption it exploits, and show the payoff and
    the limit of leaning on it?

### Range-image semantic segmentation (learning inside a perception stack)

- **Milioto, Vizzo, Behley & Stachniss, "RangeNet++: Fast and Accurate LiDAR Semantic Segmentation,"
  IROS 2019, Macau, pp. 4213-4220.** Verified: DOI `10.1109/IROS40897.2019.8967762`.
  - **Why it is an exemplar:** a learned component (a segmentation network) is presented as a **module
    that meets a frame-rate budget** and feeds a downstream robotics pipeline — not as a leaderboard
    entry. Speed and integration carry equal weight to accuracy.
  - **Self-check:** is your learned component evaluated at the latency the robot actually imposes, and is
    its output shown to serve a downstream task?

### Tightly-coupled sensor fusion (factor-graph state estimation)

- **Shan, Englot, Meyers, Wang, Ratti & Rus, "LIO-SAM: Tightly-coupled Lidar Inertial Odometry via
  Smoothing and Mapping," IROS 2020, Las Vegas, pp. 5135-5142.** Verified: DOI
  `10.1109/IROS45743.2020.9341176`.
  - **Why it is an exemplar:** it fuses lidar and IMU in a **factor graph** and validates on multiple
    field datasets from real platforms — the IROS pattern of a system evaluated across environments, not
    one hero run.
  - **Self-check:** does your estimator show robustness across several real sequences and platforms
    rather than a single curated trajectory?

---

## By topic (each cell is a verified IROS paper above)

| Topic | Verified IROS exemplar | Edition / pages | System |
| --- | --- | --- | --- |
| Evaluation infrastructure | Sturm et al., "A Benchmark for RGB-D SLAM Systems" | 2012 / 573-580 | Mocap ground truth + ATE metric |
| Onboard volumetric mapping | Oleynikova et al., "Voxblox" | 2017 | Incremental ESDF from TSDF |
| Ground-vehicle lidar odometry | Shan & Englot, "LeGO-LOAM" | 2018 / 4758-4765 | Ground-optimized LOAM |
| Lidar semantic segmentation | Milioto et al., "RangeNet++" | 2019 / 4213-4220 | Range-image CNN + kNN cleanup |
| Lidar-inertial fusion | Shan et al., "LIO-SAM" | 2020 / 5135-5142 | Factor-graph LIO |

> Five verified papers across five system cells. The LeGO-LOAM → LIO-SAM pair also shows **a research
> line** (ground-optimized lidar odometry → tightly-coupled lidar-inertial fusion) by an overlapping
> author group within IROS, useful when positioning an incremental-but-deployed systems contribution.

---

## Omitted for lack of clean IROS verification (do not attribute to IROS without re-checking)

To keep the list zero-hallucination, the following were **excluded** after checking — several are exactly
the sibling-venue confusions the header warns about:

- **Zhang & Singh, "LOAM: Lidar Odometry and Mapping in Real-time"** — the canonical LOAM paper is
  **RSS 2014**, **not IROS**. Its IROS-edition descendants (LeGO-LOAM, LIO-SAM) are above; the original
  is not an IROS paper.
- **Hess, Kohler, Rapp & Andor, "Real-Time Loop Closure in 2D LIDAR SLAM" (Cartographer)** — **ICRA
  2016** (`10.1109/ICRA.2016.7487258`), **not IROS**. A direct DOI trap: the `ICRA.2016` string is the
  tell.
- **Mur-Artal, Montiel & Tardós, "ORB-SLAM"** — published in **IEEE Transactions on Robotics (T-RO),
  2015**, a journal, **not the IROS conference**. Omitted.
- **Hornung, Wurm, Bennewitz, Stachniss & Burgard, "OctoMap"** — the archival OctoMap paper is in the
  **Autonomous Robots journal (2013)**; it grew from a workshop, and no clean IROS main-conference
  placement was confirmed. Omitted.
- **Mahler et al., "Dex-Net 2.0"** — **RSS 2017**, **not IROS**. Omitted to avoid venue misattribution.

Before adding any new paper, confirm it in IEEE Xplore or the ACM DL by matching the **DOI to the IROS
edition** (the record names "IEEE/RSJ International Conference on Intelligent Robots and Systems"), then
record author list, year, host city, and pages, and update the access-date header. When in doubt, omit.
If web search is unavailable, add the row as **待核实 / TO VERIFY** with **no attribution**.
