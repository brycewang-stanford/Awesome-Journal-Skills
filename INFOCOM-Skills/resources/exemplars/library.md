# IEEE INFOCOM Exemplars Library (contribution shape × method)

> **Verified via web search, access date 2026-07-09.** Every paper below was checked against
> **dblp** (`db/conf/infocom`) and IEEE Xplore / IEEE INFOCOM award pages to confirm it appeared at
> **IEEE INFOCOM** — matching title, author list, year, and venue string. Papers that could not be
> cleanly confirmed as INFOCOM (as opposed to SIGCOMM, NSDI, MobiCom, an IEEE journal, or IEEE
> Trans. Information Theory) were **omitted and documented below**. It is deliberately a short,
> verified list (4 verified > 15 guessed).
>
> **Sibling-confusion guard:** INFOCOM is **not** SIGCOMM, **not** NSDI, **not** MobiCom, and
> **not** an IEEE journal. Several canonical networking results were published at those venues
> instead; a famous author or a familiar topic does **not** prove an INFOCOM placement. Each row was
> checked to be an INFOCOM edition specifically (see omissions).
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent results, bounds, or numbers — read the original on IEEE Xplore before citing
> anything. For INFOCOM-specific policy, scope, and the cycle model, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **contribution shape × method** is closest to yours, then study how that paper
states a **networking problem and system model**, backs it with **evidence proportional to the
claim** (a proof, a seeded simulation, or a measurement), and pre-empts the objection it cannot
rebut — the INFOCOM bar (see
[`../../skills/infocom-writing-style/SKILL.md`](../../skills/infocom-writing-style/SKILL.md),
[`../../skills/infocom-topic-selection/SKILL.md`](../../skills/infocom-topic-selection/SKILL.md),
and [`../../skills/infocom-experiments/SKILL.md`](../../skills/infocom-experiments/SKILL.md)). For
each, ask the self-check question before claiming your paper is "INFOCOM-shaped."

Several rows are **IEEE INFOCOM Test of Time Paper Award** honorees, so they also model what
"influence a decade later" looks like at this venue.

---

## By contribution shape

### Analytical — switch scheduling / matching

- **McKeown, Anantharam & Walrand, "Achieving 100% Throughput in an Input-Queued Switch,"
  IEEE INFOCOM 1996, pp. 296-302** (DOI 10.1109/INFCOM.1996.497906). Verified: dblp
  `db/conf/infocom/infocom1996-1.html`. Showed that a maximum-weight-matching scheduling policy
  achieves 100% throughput for input-queued switches.
  - **Why it is an exemplar:** a clean **model** (input-queued switch, virtual output queues) yields
    a **provable throughput guarantee**, then the algorithm follows from the analysis — the classic
    INFOCOM "formulate, prove, and it changes what you build." The contribution is a mechanism and a
    bound, not a one-off measurement.
  - **Self-check:** does your model produce a result (a bound, a stability region, an algorithm) that
    a network designer would act on, and are its assumptions stated and defended?

### Wireless + optimization — caching at the edge

- **Golrezaei, Shanmugam, Dimakis, Molisch & Caire, "FemtoCaching: Wireless Video Content Delivery
  through Distributed Caching Helpers," IEEE INFOCOM 2012.** Verified: INFOCOM Test of Time 2024
  honoree (INFOCOM awards page); dblp. Formulated distributed caching by "helper" nodes as an
  optimization for wireless video delivery.
  - **Why it is an exemplar:** it marries a **wireless system** with an **optimization formulation**
    and an algorithm with guarantees — the INFOCOM blend of modeling and networking that a
    systems-only venue might route elsewhere. Its decade-later citations show durable impact.
  - **Self-check:** if your paper couples a wireless setting with an optimization, does the
    formulation yield an algorithm with a guarantee, evaluated at realistic scale?

### Mobile systems — computation offloading

- **Kosta, Aucinas, Hui, Mortier & Zhang, "ThinkAir: Dynamic Resource Allocation and Parallel
  Execution in the Cloud for Mobile Code Offloading," IEEE INFOCOM 2012.** Verified: INFOCOM Test of
  Time 2024 honoree; dblp. A framework for offloading mobile computation to the cloud with dynamic
  resource allocation.
  - **Why it is an exemplar:** a **built system** with a real design and evaluation that still reads
    as INFOCOM because the resource-allocation mechanism is the contribution — showing INFOCOM's
    systems wing alongside its analytical one.
  - **Self-check:** is your systems contribution a mechanism others can reuse, evaluated on a real
    implementation rather than a toy, and legible to a reviewer who leans analytical?

### Analytical — freshness / Age of Information

- **Sun, Uysal-Biyikoglu, Yates, Koksal & Shroff, "Update or Wait: How to Keep Your Data Fresh,"
  IEEE INFOCOM (2015/2016 — 待核实 exact edition; INFOCOM Test of Time 2026 honoree).** Verified as
  an INFOCOM paper via the INFOCOM Test of Time 2026 award citation; confirm the exact edition on
  dblp before citing. Introduced principles for optimizing Age of Information (data freshness) in
  networked systems.
  - **Why it is an exemplar:** it defines and **optimizes a metric** (AoI) with clean analysis, then
    shows the counter-intuitive "sometimes wait before updating" result — a formulation-first
    contribution that seeded a research area, exactly the INFOCOM analytical mode.
  - **Self-check:** does your paper formalize a networking quantity and derive a policy whose
    insight a practitioner would not have guessed?

---

## Contribution-shape ↔ exemplar (verified rows)

| Contribution shape | Verified INFOCOM exemplar | Edition | Method |
| --- | --- | --- | --- |
| Analytical / scheduling | McKeown, Anantharam & Walrand, "Achieving 100% Throughput..." | INFOCOM 1996 | Model + max-weight matching proof |
| Wireless + optimization | Golrezaei et al., "FemtoCaching" | INFOCOM 2012 | Optimization + algorithm |
| Mobile systems | Kosta et al., "ThinkAir" | INFOCOM 2012 | Built system + evaluation |
| Analytical / freshness | Sun et al., "Update or Wait" | INFOCOM 2015/2016 (待核实) | AoI analysis + policy |

> Four verified papers across four contribution shapes. The 1996 switch result and the AoI paper
> show INFOCOM's analytical spine; FemtoCaching and ThinkAir show its wireless and systems wings —
> all first-class here.

---

## Omitted for lack of clean INFOCOM verification (do not attribute to INFOCOM without re-checking)

To keep the list zero-hallucination, the following were **excluded** after checking — several are
exactly the sibling-venue confusions the header warns about:

- **Gupta & Kumar, "The Capacity of Wireless Networks"** — verified to be **IEEE Transactions on
  Information Theory (2000)**, a journal, *not* INFOCOM. A frequent misattribution; listed only as a
  guardrail.
- **Bianchi, "Performance Analysis of the IEEE 802.11 Distributed Coordination Function"** — **IEEE
  JSAC (2000)**, a journal, not INFOCOM. Omitted.
- **Dina Katabi's "seeing through walls" Wi-Fi sensing line** — the INFOCOM **Achievement Award**
  honors her body of work, but the wall-sensing papers themselves appeared at **SIGCOMM/NSDI**, not
  INFOCOM. Do not cite them as INFOCOM placements.
- **Any well-known SIGCOMM/NSDI/MobiCom system** — surface similarity to INFOCOM's systems wing is
  not proof; confirm the venue string.

Before adding any paper, confirm it on **dblp** (`db/conf/infocom`) and **IEEE Xplore** by matching
the venue string to an INFOCOM edition (not SIGCOMM, NSDI, MobiCom, JSAC, ToN, or Trans. Info.
Theory), then record authors, year, and DOI/pages, and update the access-date header. When in
doubt, omit. If web search is unavailable, add the row as **待核实 / TO VERIFY** with **no
attribution**.
