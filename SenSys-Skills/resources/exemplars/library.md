# SenSys Exemplars Library (topic × contribution)

> **Verified via web search + dblp/ACM DL, access date 2026-07-09.** Every paper below was
> confirmed on the **dblp SenSys index** (`dblp.org/db/conf/sensys`) and/or the **ACM Digital
> Library** to have appeared at the **ACM Conference on Embedded Networked Sensor Systems
> (SenSys)** — matching edition number, year, author list, and DOI — and each also sits on the
> **SenSys Test-of-Time roll** (`sensys.acm.org/tot/`), which is by construction SenSys-only.
> Papers that could not be cleanly confirmed as SenSys were omitted (see the guard below). A
> short verified list beats a long guessed one.
>
> **Sibling-confusion guard:** SenSys is **not** MobiCom, **not** NSDI/SIGCOMM, and — even
> after the 2026 merger absorbed them — the *pre-2026* IPSN and IoTDI papers are their own dblp
> venues (`conf/ipsn`, `conf/iotdi`), not SenSys. A famous sensor-networks result is often
> misfiled: directed diffusion is **MobiCom 2000**, TAG/TinyDB core results are **OSDI/SIGMOD**,
> and Glossy is **IPSN 2011** — none are SenSys. Confirm the dblp key says `conf/sensys` before
> attributing.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does
> not reproduce or invent energy numbers, packet-reception ratios, or table values — read the
> original on the ACM DL before citing anything. For SenSys policy and scope see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **contribution type** is closest to yours, then study how the paper puts a
**buildable mechanism** and its **measured behavior on real hardware** at the center — the
SenSys bar (see [`../../skills/sensys-writing-style/SKILL.md`](../../skills/sensys-writing-style/SKILL.md),
[`../../skills/sensys-topic-selection/SKILL.md`](../../skills/sensys-topic-selection/SKILL.md),
and [`../../skills/sensys-experiments/SKILL.md`](../../skills/sensys-experiments/SKILL.md)). Ask
the self-check before claiming your paper is "SenSys-shaped." Each is decades-durable, which is
exactly why it is a Test-of-Time exemplar — a modern paper should hit the same evidence bar on
current silicon and (post-merger) may add an on-device-AI dimension.

---

## By contribution

### Network service on constrained nodes (data collection / routing)

- **Gnawali, Fonseca, Jamieson, Moss & Levis, "Collection Tree Protocol," SenSys 2009 (7th).**
  Verified: `dl.acm.org/doi/10.1145/1644038.1644040`; SenSys Test-of-Time award.
  - **Why it is an exemplar:** two named principles (datapath validation, adaptive beaconing)
    turned into a **reusable, widely deployed service** measured across many testbeds — a
    mechanism that travels, not a one-network tuning. It became the field's baseline for years.
  - **Self-check:** is your contribution a **reusable service or mechanism** with a stated
    operating principle, evaluated on more than one testbed, rather than a single deployment?

### Low-power link layer (energy-centric systems design)

- **Polastre, Hill & Culler, "Versatile Low Power Media Access for Wireless Sensor Networks"
  (B-MAC), SenSys 2004 (2nd).** Verified: SenSys Test-of-Time award; SenSys 2004 proceedings.
  - **Why it is an exemplar:** designs a MAC around the **energy budget of a duty-cycled node**
    and exposes tunable interfaces, showing energy/latency trade-offs measured on real motes —
    the SenSys move of making **power the first-class metric**, not throughput alone.
  - **Self-check:** does your design treat **energy as the objective** and report it with a
    named measurement method, or does energy appear only as an afterthought paragraph?

### Time synchronization primitive (distributed embedded systems)

- **Maróti, Kusy, Simon & Lédeczi, "The Flooding Time Synchronization Protocol" (FTSP),
  SenSys 2004 (2nd).** Verified: `dl.acm.org/doi/10.1145/1031495.1031501`; Test-of-Time award.
  - **Why it is an exemplar:** isolates a **primitive every sensing deployment needs** (µs-scale
    synchronization) and proves it robust to node/link failure on hardware — a crisp systems
    contribution with a clearly bounded claim.
  - **Self-check:** does your paper deliver a **named primitive** with a bounded, measured
    guarantee under realistic failure, rather than an end-to-end app whose wins are diffuse?

### Embedded programming abstraction (memory-constrained software)

- **Dunkels, Schmidt, Voigt & Ali, "Protothreads: Simplifying Event-Driven Programming of
  Memory-Constrained Embedded Systems," SenSys 2006 (4th).** Verified: SenSys Test-of-Time award.
  - **Why it is an exemplar:** a **programming abstraction** whose payoff is measured in **bytes
    of RAM and lines of code** on real microcontrollers — evidence in the units the platform
    actually constrains, the SenSys software-systems flavor.
  - **Self-check:** if your contribution is software, is its benefit measured in the platform's
    scarce resources (RAM, flash, cycles, energy), not only in developer convenience?

### Mobile / opportunistic sensing + inference (sensing-to-semantics)

- **Hemminki, Nurmi & Tarkoma, "Accelerometer-Based Transportation Mode Detection on
  Smartphones," SenSys 2013 (11th).** Verified: SenSys Test-of-Time award; SenSys 2013 proceedings.
  - **Why it is an exemplar:** turns a **commodity sensor stream into a semantic label** with an
    inference pipeline evaluated against real ground truth — the lineage that, post-merger,
    connects directly to on-device / embedded-AI submissions.
  - **Self-check:** is your inference validated against **honest, provenance-documented ground
    truth** collected in realistic conditions, with the sensing and model constraints reported?

---

## By topic (each cell is a verified SenSys paper above)

| Topic | Verified SenSys exemplar | Edition / year | Contribution type |
| --- | --- | --- | --- |
| Data collection / routing | Gnawali et al., "Collection Tree Protocol" | 7th / 2009 | Reusable network service |
| Low-power MAC / energy | Polastre, Hill & Culler, "B-MAC" | 2nd / 2004 | Energy-first link layer |
| Time synchronization | Maróti et al., "FTSP" | 2nd / 2004 | Distributed primitive |
| Embedded software abstraction | Dunkels et al., "Protothreads" | 4th / 2006 | Memory-constrained abstraction |
| Mobile sensing + inference | Hemminki, Nurmi & Tarkoma, "Transportation Mode Detection" | 11th / 2013 | Sensing-to-semantics pipeline |

> Five verified Test-of-Time papers across five contribution types. B-MAC → FTSP → CTP also
> traces a **research arc** (energy-aware link → synchronization → collection service) built up
> at SenSys over the 2000s — useful when positioning a principled increment on a prior primitive.

---

## Omitted for lack of clean SenSys verification (do not attribute without re-checking)

Kept off the list to preserve zero-hallucination; several are exactly the misfilings the header
warns about:

- **"Directed Diffusion" (Intanagonwiwat, Govindan & Estrin)** — a foundational sensor-networks
  paper, but it appeared at **MobiCom 2000**, not SenSys. Listed only as a guardrail.
- **Glossy (Ferrari, Zimmerling, Thiele & Saukh)** — canonical low-power flooding, but **IPSN
  2011**. Post-2026 the *community* is merged into SenSys; the *2011 paper's venue is still
  IPSN* (`conf/ipsn`). Do not relabel it SenSys.
- **TAG / TinyDB (Madden et al.)** — the core results are **OSDI 2002 / SIGMOD / TODS**, not
  SenSys. Omitted.

Before adding any paper, confirm it on `dblp.org/db/conf/sensys` (the key must read
`conf/sensys` and the edition/year must match) or on the ACM DL SenSys proceedings, then record
authors, year, edition, and DOI and update the access-date header. When in doubt, omit. If web
search is unavailable, add the row as **待核实 / TO VERIFY** with **no attribution**.
