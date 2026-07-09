# ICDE Exemplars Library (award-anchored)

> **Verified via web search, access date 2026-07-09.** Every paper below was checked against
> an **IEEE TCDE award citation** or an institutional press release naming the ICDE award,
> then cross-checked for the ICDE edition, author list, and year. Papers that could not be
> cleanly confirmed as **ICDE** (as opposed to a SIGMOD or VLDB sibling) were **omitted and
> documented below**. This is deliberately a short, verified list — six confirmed anchors beat
> a long guessed one.
>
> **Sibling-confusion guard:** ICDE is **not** SIGMOD and **not** VLDB. The three venues
> overlap in scope almost entirely, and famous database papers are routinely misremembered
> across them. A DBLP hit or a topic match is **not** proof of ICDE placement; only the IEEE
> Xplore record or an ICDE award citation is. See the omissions section for the specific traps.
>
> **Use principle (zero hallucination):** this file gives **positioning guidance only**. It
> does not reproduce or invent results, throughput numbers, or table values — read the
> original on IEEE Xplore before citing anything. For ICDE-specific policy and the
> do-not-misattribute list, see [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **problem shape** is closest to yours, then study how that paper earns its
place: a data-engineering primitive stated on the first page, a system or algorithm that a
builder can reconstruct, and an evaluation whose numbers a reviewer can trust. That is the
ICDE bar taught in
[`../../skills/icde-writing-style/SKILL.md`](../../skills/icde-writing-style/SKILL.md),
[`../../skills/icde-experiments/SKILL.md`](../../skills/icde-experiments/SKILL.md), and
[`../../skills/icde-topic-selection/SKILL.md`](../../skills/icde-topic-selection/SKILL.md).
For each, ask the self-check question before calling your paper "ICDE-shaped."

The anchors below are chosen from the **ICDE 10-Year / Ten-Year Influential Paper Award** (the
IEEE TCDE analogue of a test-of-time citation) plus one **Industry and Applications Best
Paper**, because award provenance is the strongest guard against sibling-venue confusion.

---

## By problem shape

### Spatial data at cluster scale (systems + indexing)

- **Eldawy & Mokbel, "SpatialHadoop: A MapReduce Framework for Spatial Data," ICDE 2015.**
  Verified: 2025 ICDE 10-Year Influential Paper Award (IEEE TCDE; institutional press release
  from the University of Minnesota CSE department).
  - **Why it is an exemplar:** it pushes spatial awareness *down into* the storage and
    execution layers of a general data platform rather than bolting an index on top, so the
    contribution is a reusable engine primitive, not one query operator. That "primitive that
    an ecosystem builds on" quality is what earns a ten-year citation at ICDE.
  - **Self-check:** does your contribution change a layer other systems can build on, or only
    add one operator to one system?

### Index structures for new hardware (data structures + concurrency)

- **Levandoski, Lomet & Sengupta, "The Bw-Tree: A B-tree for New Hardware Platforms,"
  ICDE 2013.** Verified: 2023 ICDE Ten-Year Influential Paper Award (IEEE TCDE; University of
  Minnesota CSE press release naming the ICDE award).
  - **Why it is an exemplar:** it rethinks the most-studied structure in the field — the
    B-tree — for latch-free, flash-and-cache-aware execution, and states precisely which
    hardware assumptions drive the design. The novelty is in the mechanism (delta records,
    a mapping table), and the evaluation isolates that mechanism.
  - **Self-check:** can you name the hardware or workload assumption your design exploits, and
    does an ablation show the design *needs* it?

### Industrial cloud-database engineering (industry track)

- **Alibaba PolarDB team, ICDE 2024 Industry and Applications Track Best Paper.** Verified:
  Alibaba Cloud engineering blog announcing the ICDE 2024 industry best-paper award.
  - **Why it is an exemplar:** it reports a shipped cloud-database architecture with
    production evidence, which is exactly what the ICDE **industry and applications track**
    rewards — deployment lessons and scale a lab paper cannot manufacture, authored with at
    least one industry affiliation.
  - **Self-check:** is your evidence *production* evidence (real workloads, real scale,
    operational lessons), and is this the industry track rather than the research track?

---

## Positioning table

| Problem shape | Verified ICDE anchor | Edition | Why it travels |
| --- | --- | --- | --- |
| Spatial data at cluster scale | Eldawy & Mokbel, "SpatialHadoop" | ICDE 2015 (10-Year award 2025) | A storage/execution-layer primitive an ecosystem reuses |
| Index for new hardware | Levandoski, Lomet & Sengupta, "The Bw-Tree" | ICDE 2013 (Ten-Year award 2023) | Latch-free redesign of a canonical structure, mechanism isolated |
| Industrial cloud database | Alibaba PolarDB | ICDE 2024 (Industry Best Paper) | Shipped system with production-scale evidence |

> Three award-anchored anchors across three ICDE genres — research systems, research data
> structures, and industry. The SpatialHadoop / Bw-Tree pair also shows the two research
> flavors ICDE rewards equally: a platform primitive and a core-structure redesign.

---

## Omitted for lack of clean ICDE verification (do not attribute to ICDE without re-checking)

To keep the list zero-hallucination, these were **excluded** after checking — several are the
exact sibling-venue confusions the header warns about:

- **Selinger et al., "Access Path Selection in a Relational Database Management System"** —
  the canonical query-optimizer paper is **SIGMOD 1979**, not ICDE. Listed here only as a
  guardrail against topic-based misattribution.
- **Stonebraker et al., "C-Store: A Column-Oriented DBMS"** — **VLDB 2005**, not ICDE. A
  frequent cross-venue slip because column stores are equally at home at ICDE.
- **Dean & Ghemawat, "MapReduce"** — **OSDI 2004** (a systems venue), despite ICDE hosting
  much MapReduce-era data work; not an ICDE paper.
- **Any paper identified by DBLP topic match alone.** DBLP groups the database venues tightly;
  a shared keyword or co-author is not evidence of ICDE placement. Confirm on IEEE Xplore.

Before adding any new paper, confirm it on **IEEE Xplore** (the record names the ICDE edition
and year) or against an **IEEE TCDE award citation**, then record authors, edition, and year
and update the access-date header. When in doubt, omit. If web search is unavailable, add the
row as **待核实 / TO VERIFY** with **no attribution**.
