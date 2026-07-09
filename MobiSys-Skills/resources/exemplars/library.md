# MobiSys Exemplars Library (topic × system class)

> **Verified via web search against the ACM Digital Library and dblp, access date
> 2026-07-09.** Every paper below was checked to have appeared at the **ACM International
> Conference on Mobile Systems, Applications, and Services (MobiSys)** — matching the dblp
> `conf/mobisys` record and the ACM DL proceedings volume to the stated edition, plus author
> list and year. Papers that could not be cleanly confirmed as **MobiSys** (as opposed to a
> sibling venue) were **omitted and documented below**. It is deliberately a short, verified
> list (5 verified > 15 guessed).
>
> **Sibling-confusion guard:** MobiSys is **not** MobiCom, SenSys, UbiComp/IMWUT, OSDI, or
> NSDI. Many famous mobile-and-systems papers live in those venues. Sharing the ACM SIGMOBILE
> umbrella with MobiCom and SenSys makes misattribution especially easy — a paper's fame in
> "mobile systems" does **not** prove it is a MobiSys paper. Each row below was checked to be a
> MobiSys edition specifically.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does
> not reproduce or invent results, latency/energy numbers, or table values — read the original
> on the ACM DL before citing anything. For MobiSys-specific policy and scope, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **topic × system class** is closest to yours, then study how that paper
puts a **mobile-system contribution on the first page**, states its **on-device evaluation**
(energy, latency, memory on real hardware), and ties every claim to a measurement — the
MobiSys bar (see
[`../../skills/mobisys-writing-style/SKILL.md`](../../skills/mobisys-writing-style/SKILL.md),
[`../../skills/mobisys-topic-selection/SKILL.md`](../../skills/mobisys-topic-selection/SKILL.md),
and [`../../skills/mobisys-experiments/SKILL.md`](../../skills/mobisys-experiments/SKILL.md)).
For each, ask the self-check before claiming your paper is "MobiSys-shaped."

---

## By system class

### Computation offload for energy (mobile runtime + program partitioning)

- **Cuervo, Balasubramanian, Cho, Wolman, Saroiu, Chandra & Bahl, "MAUI: Making Smartphones
  Last Longer with Code Offload," MobiSys 2010 (8th; San Francisco).**
  Verified via dblp `conf/mobisys` and the ACM DL MobiSys 2010 proceedings.
  - **Why it is an exemplar:** turns offload into a **fine-grained, energy-aware runtime
    decision** — which methods to run remotely, decided at run time against current
    connectivity — with energy measured on real phones. The contribution is a *system
    mechanism*, not a model, which is the MobiSys center of gravity.
  - **Self-check:** is your contribution a mobile-system mechanism whose payoff is measured in
    energy/latency on a real device, rather than an algorithm evaluated in simulation?

### On-phone acoustic sensing (mobile sensing service)

- **Lu, Pan, Lane, Choudhury & Campbell, "SoundSense: Scalable Sound Sensing for
  People-Centric Applications on Mobile Phones," MobiSys 2009 (7th; Kraków), pp. 165–178.**
  Verified via dblp `conf/mobisys/LuPLCC09` and the ACM DL.
  - **Why it is an exemplar:** a **general-purpose sensing pipeline that runs entirely on the
    phone** under resource limits, classifying sound with on-device learning and no back-end.
    The system, its footprint, and its on-device behavior are the result.
  - **Self-check:** does your sensing contribution run within the device's real compute/energy
    budget, and is that budget the thing you measure?

### Adaptive perception offload (interactive on-device pipeline)

- **Ra, Sheth, Mummert, Pillai, Wetherall & Govindan, "Odessa: Enabling Interactive Perception
  Applications on Mobile Devices," MobiSys 2011 (9th; Bethesda).**
  Verified via dblp `conf/mobisys/mobisys2011` and ACM DL DOI 10.1145/1999995.2000000.
  - **Why it is an exemplar:** shows that **offload and parallelism decisions must adapt at
    run time** for interactive perception, demonstrated across three applications on real
    devices — a systems finding about *when* to offload, not a vision model.
  - **Self-check:** is the contribution a runtime/systems decision proven by on-device
    latency-and-throughput measurement across conditions, not a static design?

### On-device deep-inference scheduling (resource-constrained ML serving)

- **Han, Shen, Philipose, Agarwal, Wolman & Krishnamurthy, "MCDNN: An Approximation-Based
  Execution Framework for Deep Stream Processing Under Resource Constraints," MobiSys 2016
  (14th).**
  Verified via the ACM DL MobiSys 2016 proceedings, DOI 10.1145/2906388.2906396.
  - **Why it is an exemplar:** frames on-device/cloud DNN serving as **approximate model
    scheduling** under battery, data, and cost budgets — an optimizing compiler and runtime
    scheduler. The systems problem, not the network architecture, is the paper.
  - **Self-check:** does your on-device ML paper contribute a *resource-management system*
    (scheduling, approximation, placement) rather than a better model?

### Mobile-GPU deep-learning runtime (continuous vision on the handset)

- **Huynh, Lee & Balan, "DeepMon: Mobile GPU-Based Deep Learning Framework for Continuous
  Vision Applications," MobiSys 2017 (15th), pp. 82–95.**
  Verified via dblp `conf/mobisys` and the ACM DL.
  - **Why it is an exemplar:** runs CNN/RNN inference **purely on the device's integrated
    GPU**, using inter-frame caching and decomposition to hit latency and energy targets —
    the classic MobiSys "make it run fast and cheap on the real chip" result.
  - **Self-check:** does your framework's win show up as on-device latency and energy on named
    hardware, with the accuracy trade-off reported honestly?

---

## By topic (each cell is a verified MobiSys paper above)

| Topic | Verified MobiSys exemplar | Edition / year | System class |
| --- | --- | --- | --- |
| Energy-aware code offload | Cuervo et al., "MAUI" | 8th / 2010 | Mobile runtime + partitioning |
| On-phone sensing service | Lu et al., "SoundSense" | 7th / 2009 | On-device sensing pipeline |
| Interactive perception | Ra et al., "Odessa" | 9th / 2011 | Adaptive offload/parallelism |
| On-device DNN serving | Han et al., "MCDNN" | 14th / 2016 | Approximate model scheduling |
| Mobile-GPU inference | Huynh et al., "DeepMon" | 15th / 2017 | On-device deep-learning runtime |

> Five verified papers across five system classes. MAUI → Odessa → MCDNN → DeepMon also traces
> **a research line** (offload for energy → adaptive offload → on-device deep-inference systems)
> within MobiSys, useful when positioning an incremental-but-principled systems contribution.

---

## Omitted for lack of clean MobiSys verification (do not attribute to MobiSys without re-checking)

To keep the list zero-hallucination, the following were **excluded** after checking — several
are exactly the sibling-venue confusions the header warns about:

- **"TaintDroid: An Information-Flow Tracking System for Realtime Privacy Monitoring on
  Smartphones"** — a famous smartphone-systems paper, but it appeared at **OSDI 2010**, not
  MobiSys. Omitted.
- **"CenceMe" (people-centric sensing)** — canonical mobile-sensing work, but published at
  **SenSys 2008**, a sibling SIGMOBILE venue, not MobiSys. A direct SIGMOBILE-umbrella trap.
- **"RADAR" / "See Through Walls with Wi-Fi!" / WiSee-style RF sensing** — these are
  **INFOCOM / SIGCOMM / MobiCom** wireless papers; RF-sensing fame is often misfiled as
  MobiSys. Omitted.
- **"The Case for VM-Based Cloudlets"** — foundational for mobile offload, but it appeared in
  **IEEE Pervasive Computing**, a journal, not MobiSys. Omitted.

Before adding any new paper, confirm it on the **ACM Digital Library** and **dblp** by
matching the `conf/mobisys` record and proceedings volume to the MobiSys edition (the volume
names "Mobile Systems, Applications, and Services"), then record author list, year, and pages,
and update the access-date header. When in doubt, omit. If web search is unavailable, add the
row as **待核实 / TO VERIFY** with **no attribution**.
