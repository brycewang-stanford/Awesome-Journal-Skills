# MICRO Exemplars Library (mechanism × era)

> **Verified via web search, access date 2026-07-08.** Every row below was confirmed
> against the **ACM Digital Library or dblp record** for an IEEE/ACM International
> Symposium on Microarchitecture proceedings volume — matching title, authors, year,
> pages, and DOI. Selection is biased toward papers with **independent award
> validation** (MICRO Test of Time, per the SIGMICRO ToT pages) so that "exemplar"
> status is the community's judgment, not this file's. Five verified rows beat
> twenty guessed ones.
>
> **Sibling-attribution guard:** MICRO, ISCA, HPCA, and ASPLOS publish adjacent work
> and their classics are routinely mis-shelved. Notable traps checked and excluded
> below. A paper "everyone knows is a MICRO paper" is not a citation — the DOI
> record is.
>
> **Zero-hallucination rule:** this library gives positioning shapes only. Numbers,
> table values, and mechanism details must be re-read from the actual papers before
> being cited anywhere.

---

## How to use this library

Find the row whose *contribution shape* matches your project, then imitate the
shape — how the paper couples a characterization to a mechanism to a cost story —
not the topic. Cross-reference
[`../../skills/micro-topic-selection/SKILL.md`](../../skills/micro-topic-selection/SKILL.md)
(fit tests), [`../../skills/micro-writing-style/SKILL.md`](../../skills/micro-writing-style/SKILL.md)
(the four-beat argument), and
[`../../skills/micro-experiments/SKILL.md`](../../skills/micro-experiments/SKILL.md)
(instrument ladder).

## The five verified exemplars

### 1. The predictor paper — Yeh & Patt, "Two-Level Adaptive Training Branch Prediction," MICRO 1991 (24th), pp. 51–61

- Verified: dblp `conf/micro/YehP91`; ACM DL DOI `10.1145/123465.123475`.
- **Shape:** observe that run-time history contains structure static schemes miss →
  a two-level table organization exploiting it → accuracy evaluated against the
  prior predictor taxonomy. The archetype of "small structure, large consequence"
  — speculation quality bounds the whole pipeline.
- **Self-check:** does your mechanism's benefit come from *information the hardware
  already sees* but currently discards?

### 2. The policy paper — Qureshi & Patt, "Utility-Based Cache Partitioning," MICRO 2006 (39th), pp. 423–432

- Verified: ACM DL DOI `10.1109/MICRO.2006.49`; MICRO Test of Time 2024 (SIGMICRO
  ToT page).
- **Shape:** define a measurable quantity (marginal utility of cache ways per
  workload) → build cheap monitoring hardware to estimate it online → a runtime
  policy with explicit low-overhead accounting. The subtitle itself
  ("low-overhead, high-performance, runtime") is the MICRO value system in six
  words.
- **Self-check:** can your policy's decision input be measured by hardware you can
  size in KB?

### 3. The modeling-tool paper — Muralimanohar, Balasubramonian & Jouppi, "Optimizing NUCA Organizations and Wiring Alternatives for Large Caches with CACTI 6.0," MICRO 2007 (40th), pp. 3–14

- Verified: ACM DL DOI `10.1109/MICRO.2007.30`; MICRO Test of Time 2025 (one of two
  awardees, per SIGMICRO).
- **Shape:** the community's design questions outgrew its estimation tools → extend
  the tool (interconnect-aware large-cache modeling) → demonstrate design
  conclusions the old tool could not reach. Proof that MICRO publishes
  *infrastructure* when it changes what everyone else can evaluate.
- **Self-check:** would three other groups' next papers use your tool?

### 4. The power-methodology paper — Li, Ahn, Strong, Brockman, Tullsen & Jouppi, "McPAT: An Integrated Power, Area, and Timing Modeling Framework for Multicore and Manycore Architectures," MICRO 2009 (42nd), pp. 469–480

- Verified: ACM DL DOI `10.1145/1669112.1669172`.
- **Shape:** unify previously separate estimation concerns (power + area + timing)
  behind one interface usable with performance simulators. Together with CACTI it
  defines the evaluation culture this pack teaches in `micro-experiments`: power
  numbers at MICRO are *modeled*, versioned, and named.
- **Self-check:** are your own power/area claims produced by a tool you could cite
  at this level of specificity?

### 5. The accelerator paper — Chen, Luo, Liu, Zhang, He, Wang, Li, Chen, Xu, Sun & Temam, "DaDianNao: A Machine-Learning Supercomputer," MICRO 2014 (47th), pp. 609–622

- Verified: ACM DL DOI `10.1109/MICRO.2014.58`.
- **Shape:** identify the structural bottleneck (off-chip weight traffic) → commit
  the architecture to on-chip storage distributed with compute (eDRAM tiles) →
  evaluate as a *system* with area/power modeling. The template for the accelerator
  wave that followed: the novelty is a **memory-hierarchy decision**, defended
  quantitatively — not a claim that the workload matters.
- **Self-check:** if a reviewer deletes your accelerator's dataflow choice and
  keeps the arithmetic units, does your speedup survive? (If yes, the dataflow is
  not the contribution.)

## Mechanism × era matrix

| Era | Exemplar | Structure touched | Enduring lesson |
|---|---|---|---|
| 1991 | Two-level branch prediction | Fetch-stage predictor tables | History the hardware discards is headroom |
| 2006 | Utility-based cache partitioning | Shared LLC allocation | Measure utility online, act cheaply |
| 2007 | CACTI 6.0 / NUCA | Modeling infrastructure | Tools that move the community are MICRO papers |
| 2009 | McPAT | Power/area/timing models | Cost claims need named, versioned instruments |
| 2014 | DaDianNao | Accelerator memory hierarchy | Locality arguments beat FLOPS arguments |

## Checked and excluded (do not cite these as MICRO papers)

- **"Flipping Bits in Memory Without Accessing Them" (Rowhammer)** — ISCA 2014,
  not MICRO. The most common misattribution in memory-systems drafts.
- **Wattch (power modeling)** — ISCA 2000, not MICRO; McPAT/CACTI are the MICRO
  entries in that lineage.
- **DianNao (the predecessor accelerator)** — ASPLOS 2014; only **Da**DianNao is
  the MICRO paper. Same group, same year, different venue — a perfect trap.
- **"Simultaneous Multithreading: Maximizing On-Chip Parallelism"** — ISCA 1995.

## Adding a row

Confirm on dblp (`conf/micro/...`) or the ACM DL/IEEE Xplore proceedings entry:
title, full author list, edition ordinal, pages, DOI. Prefer papers with ToT or
Hall-of-Fame-adjacent validation. If verification fails through every access path,
add the candidate under a **待核实** heading with no attribution and no shape
claims until confirmed.
