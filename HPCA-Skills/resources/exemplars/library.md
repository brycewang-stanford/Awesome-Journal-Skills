# HPCA Exemplars Library (contribution shapes)

> **Verified via web search of the IEEE-CS TCCA HPCA Test of Time Award pages and
> cross-checked against the dblp HPCA series index, access date 2026-07-09.** Every
> paper below is a named **HPCA Test of Time Award** winner (the TCCA award for past
> HPCA papers whose influence is still felt ~18-22 years after publication). Each row
> was checked to be an **HPCA** paper — matching title, authors, and year against
> `dblp.org/db/conf/hpca/` — not a paper from a sibling venue. It is deliberately a
> short, verified list (6 verified > 15 guessed).
>
> **Sibling-confusion guard:** HPCA is **not** ISCA, MICRO, or ASPLOS. Several famous
> architecture ideas were published at those venues; a topic being "architecture" does
> **not** make a paper HPCA. Runahead execution, for instance, has an HPCA 2003 paper
> *and* a separate ISCA lineage — attribute the specific paper you cite, not the idea.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**.
> It does not reproduce or invent speedup numbers, table values, or claims — read the
> original on IEEE Xplore before citing anything. For HPCA-specific policy and the
> do-not-misattribute list, see [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **contribution shape** is closest to yours, then study how that
paper puts a **mechanism-to-behavior claim on the first page**, with a **measured
motivation** and **evidence matched to the instrument** — the HPCA bar (see
[`../../skills/hpca-writing-style/SKILL.md`](../../skills/hpca-writing-style/SKILL.md),
[`../../skills/hpca-topic-selection/SKILL.md`](../../skills/hpca-topic-selection/SKILL.md),
and [`../../skills/hpca-experiments/SKILL.md`](../../skills/hpca-experiments/SKILL.md)).
For each, ask the self-check question before claiming your paper is "HPCA-shaped."

---

## By contribution shape

### A reusable structure that replaces a per-case design (prefetching / microarchitecture)

- **Nesbit & Smith, "Data Cache Prefetching Using a Global History Buffer," HPCA 2004.**
  HPCA Test of Time Award 2024. Verified against `dblp.org/db/conf/hpca/hpca2004`.
  - **Why it is an exemplar:** replaces ad-hoc prefetch tables with a **general index
    structure (the global history buffer)** that many prefetching schemes can reuse —
    the contribution is a mechanism that *travels*, not one tuned predictor.
  - **Self-check:** is your contribution a reusable structure with a stated cost, or a
    single point design that happens to win on one workload?

### A measured cost that motivates a new control loop (power / thermal management)

- **Brooks & Martonosi, "Dynamic Thermal Management for High-Performance
  Microprocessors," HPCA 2001.** HPCA Test of Time Award 2021. Verified against
  `dblp.org/db/conf/hpca/hpca2001`.
  - **Why it is an exemplar:** frames **temperature as a first-class design
    constraint** and proposes runtime mechanisms to hold it — a motivation-driven
    control contribution that opened a subfield, the HPCA sweet spot where a measured
    problem justifies a mechanism.
  - **Self-check:** does your paper measure the problem before proposing the fix, so the
    mechanism answers a quantified cost rather than an assumed one?

### Relaxing a single design assumption for an efficiency win (energy / DVFS)

- **Semeraro, Magklis, Balasubramonian, Albonesi, Dwarkadas & Scott, "Energy-Efficient
  Processor Design Using Multiple Clock Domains with Dynamic Voltage and Frequency
  Scaling," HPCA 2002.** HPCA Test of Time Award 2022. Verified against
  `dblp.org/db/conf/hpca/hpca2002`.
  - **Why it is an exemplar:** weakens the **single-global-clock assumption** into
    multiple independently scaled domains, then shows the energy payoff — the
    contribution is an explicit relaxation of a structural assumption, exactly the move
    HPCA rewards.
  - **Self-check:** can you name the assumption your design relaxes, and pair the
    relaxation with a measured efficiency payoff?

### A model plus a mechanism it justifies (on-chip networks)

- **Peh & Dally, "A Delay Model and Speculative Architecture for Pipelined Routers,"
  HPCA 2001.** HPCA Test of Time Award 2020. Verified against
  `dblp.org/db/conf/hpca/hpca2001`.
  - **Why it is an exemplar:** pairs an **analytical delay model** with a speculative
    router microarchitecture the model motivates — theory and machine in one paper, so
    the design choice is explained, not just measured.
  - **Self-check:** does your paper offer a model that predicts *why* the mechanism
    helps, rather than only a benchmark bar chart?

### Characterization that becomes a predictive tool (multicore / shared resources)

- **Chandra, Guo, Kim & Solihin, "Predicting Inter-Thread Cache Contention on a Chip
  Multi-Processor Architecture," HPCA 2005.** HPCA Test of Time Award 2023. Verified
  against `dblp.org/db/conf/hpca/hpca2005`.
  - **Why it is an exemplar:** turns an observed multicore pathology (shared-cache
    contention) into **predictive models** usable for scheduling — the contribution is a
    tool derived from careful characterization, the `hpca-topic-selection` signal that
    measurement is central, not decorative.
  - **Self-check:** does your characterization yield something *predictive or
    actionable*, rather than stopping at "we observed X"?

### A hardware primitive that makes a security guarantee affordable (secure architecture)

- **Gassend, Suh, Clarke, van Dijk & Devadas, "Caches and Hash Trees for Efficient
  Memory Integrity Verification," HPCA 2003.** HPCA Test of Time Award 2025. Verified
  against `dblp.org/db/conf/hpca/hpca2003`.
  - **Why it is an exemplar:** makes memory-integrity verification **practical** by
    caching hash-tree nodes — the contribution is an architectural primitive that turns
    an expensive guarantee into an affordable one, bridging security and performance.
  - **Self-check:** does your primitive make a previously impractical guarantee cheap
    enough to adopt, with the overhead measured on the machine?

---

## By contribution shape (index)

| Contribution shape | Verified HPCA exemplar | Edition | ToT year |
| --- | --- | --- | --- |
| Reusable structure (prefetching) | Nesbit & Smith, "Data Cache Prefetching Using a Global History Buffer" | HPCA 2004 | 2024 |
| Measured cost → control loop (thermal) | Brooks & Martonosi, "Dynamic Thermal Management for High-Performance Microprocessors" | HPCA 2001 | 2021 |
| Relaxed assumption → efficiency (DVFS) | Semeraro et al., "Multiple Clock Domains with DVFS" | HPCA 2002 | 2022 |
| Model + mechanism (on-chip networks) | Peh & Dally, "A Delay Model and Speculative Architecture for Pipelined Routers" | HPCA 2001 | 2020 |
| Characterization → predictor (multicore) | Chandra et al., "Predicting Inter-Thread Cache Contention" | HPCA 2005 | 2023 |
| Primitive → affordable guarantee (security) | Gassend et al., "Caches and Hash Trees for Efficient Memory Integrity Verification" | HPCA 2003 | 2025 |

> Six verified papers across six contribution shapes. The two HPCA 2001 winners (Brooks
> & Martonosi; Peh & Dally) show that a single edition can seat both a control-loop and a
> model-plus-mechanism contribution — useful when positioning where your paper's center
> of gravity sits.

---

## Before adding any new paper

- Confirm it on `dblp.org/db/conf/hpca/` by matching the **edition to the year** (the
  dblp page names the "IEEE International Symposium on High-Performance Computer
  Architecture"), then record author list, year, and title, and update the access-date
  header.
- Prefer **HPCA Test of Time Award** winners from the TCCA award pages as anchors; they
  are already vetted for HPCA placement and long-term impact.
- When in doubt, omit. If web search is unavailable, add the row as **待核实 / TO
  VERIFY** with **no attribution** — never guess a venue, and never blur an idea's
  lineage across HPCA/ISCA/MICRO/ASPLOS.
