# IPSN Exemplars Library (contribution shape × track)

> **Verified via web search, access date 2026-07-09.** Every paper below was checked against
> **dblp**, the **ACM Digital Library**, and/or **IEEE Xplore** to confirm it appeared at the
> **ACM/IEEE International Conference on Information Processing in Sensor Networks (IPSN)** —
> matching title, author list, year, and venue string. Papers that could not be cleanly confirmed
> as IPSN (as opposed to SenSys, MobiCom, MobiSys, NSDI, or a journal) were **omitted and
> documented below**. It is deliberately a short, verified list (3 verified > 15 guessed).
>
> **Sibling-confusion guard:** IPSN is **not** SenSys, **not** MobiCom/MobiSys, **not** NSDI, and
> **not** a signal-processing journal. Many canonical sensor-network tools were introduced at those
> venues instead; a famous author or a familiar mote/tool name does **not** prove IPSN. Each row was
> checked to be an IPSN edition specifically (see omissions).
>
> **Merger note:** IPSN merged into **SenSys (Embedded AI and Sensing Systems)** from 2025-2026, so
> new work in this lineage is submitted to SenSys — but these historical IPSN papers still model the
> bar. See [`../official-source-map.md`](../official-source-map.md).
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent results, numbers, or table values — read the original on ACM DL / IEEE Xplore
> before citing anything.

---

## How to use this library

Pick the row whose **contribution shape × track** is closest to yours, then study how that paper
states a **real sensing problem**, backs it with **evidence proportional to the claim** (real
platforms, ground truth, energy/accuracy budgets), and — for the IP track — grounds it in
**estimation or information-processing theory**. Match the bar in
[`../../skills/ipsn-writing-style/SKILL.md`](../../skills/ipsn-writing-style/SKILL.md),
[`../../skills/ipsn-topic-selection/SKILL.md`](../../skills/ipsn-topic-selection/SKILL.md), and
[`../../skills/ipsn-experiments/SKILL.md`](../../skills/ipsn-experiments/SKILL.md). For each, ask
the self-check question before claiming your paper is "IPSN-shaped."

---

## By contribution shape × track

### IP track — information-processing theory for sensing

- **Bajwa, Haupt, Sayeed & Nowak, "Compressive Wireless Sensing," IPSN 2006** (Nashville, TN).
  Verified: author copy (`nowak.ece.wisc.edu/ipsn06a.pdf`) + ACM DL / dblp. Introduced
  **compressive wireless sensing**: a fusion center recovers a spatial signal field from a small
  number of random projections delivered by distributed nodes, with an analysis of the
  power/distortion/latency trade-off as a function of node count.
  - **Why it is an exemplar:** it is a pure **Information Processing** contribution — a sensing
    *theory* with a communication/energy consequence, not a systems build. It shows the IP track's
    signature: an estimator or coding result whose payoff is measured in bits, joules, and error.
  - **Self-check:** does your IP-track claim rest on an information-processing argument (estimation
    bound, sparsity, coding, inference) that would survive on a different radio or platform?

### SPOTS track — a sensor platform others adopt

- **Polastre, Szewczyk & Culler, "Telos: Enabling Ultra-Low Power Wireless Research," IPSN 2005**
  (Los Angeles; the 4th IPSN, SPOTS track). Verified: ACM DL (`doi 10.5555/1147685.1147744`) /
  dblp. Introduced the **Telos mote** — an MSP430 + IEEE 802.15.4 (Chipcon) platform designed from
  scratch for minimal power, usability, and robustness.
  - **Why it is an exemplar:** the canonical **SPOTS** paper — a hardware/software *platform*
    delivered as a reusable artifact and justified by measured power and design trade-offs, not by a
    single application result. The contribution is a tool a third party could build on.
  - **Self-check:** is your SPOTS contribution a platform/tool a stranger could pick up and use, and
    is it justified by measurement (power, timing, robustness) rather than one demo?

### Deployment — a real cyber-physical instrumentation result

- **Kim, Pakzad, Culler, Demmel, Fenves, Glaser & Turon, "Health Monitoring of Civil
  Infrastructures Using Wireless Sensor Networks," IPSN 2007** (the 6th IPSN), pp. 254-263,
  DOI 10.1145/1236360.1236395. Verified: ACM DL / IEEE Xplore. A **64-node WSN deployed on the
  Golden Gate Bridge**, collecting synchronized ambient vibration data across a long multi-hop
  network — the largest structural-health-monitoring WSN of its time.
  - **Why it is an exemplar:** it shows IPSN's **real-deployment** contribution shape — a physical
    system instrumented against real-world ground truth (a bridge), where the hard problems are
    synchronization, yield, and reliable multi-hop collection, and the evidence is the deployment
    itself.
  - **Self-check:** if your paper is a deployment, does it report the physical-world hardships
    honestly (synchronization error, packet yield, hop count, energy) and measure against real
    ground truth rather than a lab surrogate?

---

## Contribution-shape ↔ exemplar (verified rows)

| Track / shape | Verified IPSN exemplar | Edition | Core idea |
| --- | --- | --- | --- |
| IP — sensing theory | Bajwa, Haupt, Sayeed & Nowak, "Compressive Wireless Sensing" | IPSN 2006 | Compressive sensing over a WSN; power/distortion/latency trade-off |
| SPOTS — platform | Polastre, Szewczyk & Culler, "Telos" | IPSN 2005 | Ultra-low-power mote platform (MSP430 + 802.15.4) |
| Deployment | Kim et al., "Health Monitoring of Civil Infrastructures..." | IPSN 2007 | 64-node Golden Gate Bridge structural-health-monitoring WSN |

> Three verified papers across IPSN's three native modes — an **IP-track theory** result, a
> **SPOTS-track platform**, and a **real deployment**. Together they show why IPSN kept two tracks:
> the questions "is the estimator sound?" and "is the platform reusable?" are judged differently.

---

## Omitted for lack of clean IPSN verification (do not attribute to IPSN without re-checking)

To keep the list zero-hallucination, the following were **excluded** after checking — several are
exactly the sibling-venue confusions the header warns about:

- **"The Flooding Time Synchronization Protocol" (Maróti et al.)** — verified to be **SenSys 2004**,
  *not* IPSN. A classic sensor-network paper at the sibling venue; listed only as a guardrail.
- **"The Cricket Location-Support System" (Priyantha, Chakraborty & Balakrishnan)** — **MobiCom
  2000**, not IPSN. Omitted despite being canonical localization.
- **"Collection Tree Protocol" (Gnawali et al.)** — **SenSys 2009**, not IPSN. Omitted.
- **Radio-interferometric localization / "RIPS" (Marótі et al.)** — **SenSys 2005**, not IPSN.
  Omitted; a direct SenSys-vs-IPSN trap.

Before adding any paper, confirm it on **dblp** and **ACM DL / IEEE Xplore** by matching the venue
string to an **IPSN** edition (not SenSys, MobiCom, MobiSys, NSDI, or a journal), then record
authors, year, and DOI/pages, and update the access-date header. Note the track (IP or SPOTS) where
the edition recorded it. When in doubt, omit. If web search is unavailable, add the row as
**待核实 / TO VERIFY** with **no attribution**.
