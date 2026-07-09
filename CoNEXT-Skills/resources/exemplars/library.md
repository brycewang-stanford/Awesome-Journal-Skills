# ACM CoNEXT Exemplars Library (contribution shape × method)

> **Verified via web search, access date 2026-07-09.** Every paper below was checked against
> **dblp** and the **ACM Digital Library** to confirm it appeared at the **ACM International
> Conference on emerging Networking EXperiments and Technologies (CoNEXT)** — matching title,
> author list, year, and venue string — and each is a documented **CoNEXT Best Paper** honoree.
> Papers that could not be cleanly confirmed as CoNEXT (as opposed to SIGCOMM, NSDI, IMC,
> SIGMETRICS, or MobiCom) were **omitted and documented below**. It is deliberately a short,
> verified list (5 verified > 15 guessed).
>
> **Sibling-confusion guard:** CoNEXT is **not** SIGCOMM, **not** NSDI, **not** IMC, and **not** a
> journal like ToN. Many networking classics were introduced at those venues instead; a famous
> author or a familiar system name does **not** prove CoNEXT. Each row was checked to be a CoNEXT
> edition specifically (see omissions).
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent results, throughput numbers, or table figures — read the original on ACM DL
> before citing anything. For CoNEXT-specific policy, scope, and the two-cycle PACMNET model, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **contribution shape × method** is closest to yours, then study how that paper
states a **networking problem practitioners recognize**, backs it with **evidence proportional to
the claim** (a testbed run, a deployment, a measurement campaign), and names its **limitations and
threats** — the CoNEXT bar (see
[`../../skills/conext-writing-style/SKILL.md`](../../skills/conext-writing-style/SKILL.md),
[`../../skills/conext-topic-selection/SKILL.md`](../../skills/conext-topic-selection/SKILL.md), and
[`../../skills/conext-experiments/SKILL.md`](../../skills/conext-experiments/SKILL.md)). For each,
ask the self-check question before claiming your paper is "CoNEXT-shaped."

All rows below are CoNEXT **Best Paper** honorees, so they also model what the venue rewards at the
top of the distribution across systems, measurement, architecture, and wireless.

---

## By contribution shape

### Systems + programmable data plane — stateful packet processing

- **Scholz et al. / Chiesa et al., "Millions of Low-latency State Insertions on ASIC Switches,"
  CoNEXT 2023** (PACMNET; DOI 10.1145/3629144). Verified: ACM DL PACMNET / dblp; **CoNEXT 2023 Best
  Paper** (KTH NSLab). Builds a key-value data structure that supports very high-rate state
  insertion on commodity ASIC switches for stateful in-network processing.
  - **Why it is an exemplar:** a hardware-constrained systems contribution delivered as a
    **runnable mechanism on real switch silicon**, not a simulation — the classic CoNEXT "systems
    idea evaluated on the real target." The contribution is a mechanism others can adopt.
  - **Self-check:** is your systems claim evaluated on the real platform (switch, NIC, kernel,
    testbed) it targets, against the constraints that platform actually imposes?

### Internet measurement — protocol performance in the wild

- **Nawrocki, Fotouhi Tehrani, Hiesgen, Mücke, Schmidt & Wählisch, "On the Interplay between TLS
  Certificates and QUIC Performance," CoNEXT 2022.** Verified: ACM DL / dblp; **CoNEXT 2022 Best
  Paper**. Measures how certificate sizes and TLS behavior shape QUIC's early performance across
  real servers.
  - **Why it is an exemplar:** it takes a widely deployed protocol interaction that folklore
    hand-waves and **measures it at Internet scale**, turning a suspicion into quantified effect —
    the CoNEXT measurement mode. The lesson is about real deployments, not a lab artifact.
  - **Self-check:** does your measurement change what the community believes about real protocol
    behavior, with a methodology and vantage points a reviewer could scrutinize and reproduce?

### Network architecture — inter-domain routing at deployment scale

- **Krähenbühl, Tabaeiaghdaei, Gloor, Kwon, Perrig, Hausheer & Roos, "Deployment and Scalability of
  an Inter-Domain Multi-Path Routing Infrastructure," CoNEXT 2021** (SCION line). Verified: ACM DL /
  dblp; **CoNEXT 2021 Best Paper**. Reports the engineering and scalability of a running
  inter-domain multi-path routing deployment.
  - **Why it is an exemplar:** it advances a **clean-slate architecture by showing it deployed and
    scaling**, not merely proposed — CoNEXT prizes the "we built it and ran it" evidence that
    architecture papers often lack.
  - **Self-check:** does your architecture paper carry deployment or scalability evidence a skeptic
    would accept, or is it a design with only simulation behind it (an NSDI/HotNets re-route
    signal)?

### Traffic engineering + measurement — operator-scale systems

- **Pujol, Poese, Zerwas, Smaragdakis & Feldmann, "Steering Hyper-Giants' Traffic at Scale,"
  CoNEXT 2019.** Verified: ACM DL / dblp; **CoNEXT 2019 Best Paper**. Studies and steers the
  traffic of large content providers ("hyper-giants") as seen from a major network.
  - **Why it is an exemplar:** it combines **operational measurement with a systems intervention**
    at the scale of a real carrier — the kind of "here is how the Internet actually delivers
    content, and here is what an operator can do" contribution CoNEXT rewards.
  - **Self-check:** is your evidence drawn from a real network at operationally relevant scale, and
    does your intervention connect to something an operator could deploy?

### Wireless / mobile systems — low-power networking

- **Chen, Ghaderi, Rubenstein & Zussman, "Maximizing Broadcast Throughput Under Ultra-Low-Power
  Constraints," CoNEXT 2016** (DOI 10.1145/2999572.3004861). Verified: ACM DL / dblp; **CoNEXT
  2016 Best Paper** (Columbia WiMNet). Optimizes broadcast throughput for energy-harvesting,
  ultra-low-power wireless nodes.
  - **Why it is an exemplar:** it pairs a **crisp analytical model with a real hardware
    constraint** (energy harvesting) and validates on a testbed — the CoNEXT wireless mode where
    theory earns its keep by respecting a deployable device.
  - **Self-check:** if your model or protocol assumes an idealized device, does the paper show it
    survives the real constraints (energy, radio, mobility) of the hardware it targets?

---

## Contribution-shape ↔ exemplar (verified rows)

| Contribution shape | Verified CoNEXT exemplar | Edition | Method |
| --- | --- | --- | --- |
| Systems + data plane | "Millions of Low-latency State Insertions on ASIC Switches" | CoNEXT 2023 | Switch-hardware systems |
| Internet measurement | "...TLS Certificates and QUIC Performance" | CoNEXT 2022 | Internet-scale measurement |
| Network architecture | "...Inter-Domain Multi-Path Routing Infrastructure" (SCION) | CoNEXT 2021 | Deployment + scalability |
| Traffic engineering | "Steering Hyper-Giants' Traffic at Scale" | CoNEXT 2019 | Operational measurement + systems |
| Wireless / low-power | "Maximizing Broadcast Throughput Under Ultra-Low-Power Constraints" | CoNEXT 2016 | Model + testbed |

> Five verified CoNEXT Best Papers across five contribution shapes — spanning the venue's range
> from switch silicon to Internet-scale measurement to clean-slate architecture to wireless.

---

## Omitted for lack of clean CoNEXT verification (do not attribute to CoNEXT without re-checking)

To keep the list zero-hallucination, the following were **excluded** after checking — several are
exactly the sibling-venue confusions the header warns about:

- **Founding congestion-control and data-center-transport papers (e.g., the DCTCP line)** —
  verified as **SIGCOMM**, not CoNEXT; omitted despite being networking canon.
- **The canonical software-defined-networking and OpenFlow origin papers** — **SIGCOMM/HotNets**
  and CCR, not CoNEXT placements; omitted.
- **Large Internet-topology and CDN-measurement classics** — many are **IMC** or **SIGCOMM**
  papers; a measurement flavor does not make a paper CoNEXT. Omitted unless individually verified.
- **CoNEXT workshop, Student Workshop, and Companion papers** — these appear in the CoNEXT
  *Companion* proceedings, not the main PACMNET track; do not cite them as main-conference CoNEXT
  papers.

Before adding any paper, confirm it on **dblp** and **ACM DL** by matching the venue string to a
CoNEXT edition (not SIGCOMM, NSDI, IMC, SIGMETRICS, or MobiCom), then record authors, year, and
DOI/pages, and update the access-date header. When in doubt, omit. If web search is unavailable,
add the row as **待核实 / TO VERIFY** with **no attribution**.
