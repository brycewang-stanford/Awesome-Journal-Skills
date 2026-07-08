# ASPLOS Exemplars Library (Influential Paper Award lineage)

> **Verified via web search, access date 2026-07-08.** Every row below traces to the
> **ACM SIGARCH/SIGPLAN/SIGOPS ASPLOS Influential Paper Award** — the venue's own
> ten-year-hindsight judgment of which ASPLOS papers mattered — as posted on
> `sigarch.org` and the `asplos-conference.org` award pages. The award has been
> presented annually since ASPLOS 2011 to papers from ten or more conferences earlier,
> which makes it the cleanest possible exemplar filter: not "famous systems papers"
> but papers the three sponsoring communities certified as ASPLOS papers with lasting
> influence.
>
> **Venue-attribution guard:** the architecture/systems space is dense with sibling
> venues (ISCA, MICRO, HPCA, SOSP, OSDI, PLDI). A famous accelerator or OS paper is
> *not* an ASPLOS paper until its proceedings entry says so. Confirm any addition on
> the ACM DL ASPLOS series page (https://dl.acm.org/conference/asplos) before citing
> it as an ASPLOS exemplar — award pages give title/year; the DL gives the DOI.
>
> **Zero-hallucination rule:** this file records positioning lessons only. It states
> no speedup numbers, benchmark scores, or design constants from the papers — read
> the originals on ACM DL before citing any result.

---

## How to use this library

Each exemplar earned the award for a different *shape* of ASPLOS contribution. Match
your project to the closest shape, then ask the self-check question. If none of the
five shapes fits, revisit
[`../../skills/asplos-topic-selection/SKILL.md`](../../skills/asplos-topic-selection/SKILL.md)
before writing — the paper may belong at a single-community venue instead.

## Five award-verified shapes

### 1. The accelerator that respects the memory system

- **"DianNao: a small-footprint high-throughput accelerator for ubiquitous
  machine-learning"** — Tianshi Chen, Zidong Du, Ninghui Sun, Jia Wang, Chengyong Wu,
  Yunji Chen, Olivier Temam. ASPLOS 2014; **2024 Influential Paper Award** (source:
  ASPLOS 2024 award page).
  - **Shape:** domain-specific hardware whose contribution is explicitly cross-layer —
    the design is argued from workload structure and memory-transfer behavior, not
    from a datapath alone.
  - **Self-check:** does your accelerator paper explain what the *software* looks like
    and where the data movement goes, or only what the ALUs do? The latter is an
    ISCA/MICRO shape.

### 2. The scheduler that treats the datacenter as the machine

- **"Paragon: QoS-Aware Scheduling for Heterogeneous Datacenters"** — Christina
  Delimitrou, Christos Kozyrakis. ASPLOS 2013; **2024 Influential Paper Award**.
  - **Shape:** a runtime/OS-layer mechanism justified by architectural heterogeneity
    and interference — the hardware diversity is the premise, the systems layer is the
    contribution.
  - **Self-check:** if the hardware were homogeneous, would your mechanism still be
    interesting? If yes, it may be a pure-systems (SOSP/OSDI/EuroSys) paper.

### 3. The virtualization mechanism that redraws a hardware/software boundary

- **"ELI: bare-metal performance for I/O virtualization"** — Abel Gordon, Nadav Amit,
  Nadav Har'El, Muli Ben-Yehuda, Alex Landau, Assaf Schuster, Dan Tsafrir.
  ASPLOS 2012; **2024 Influential Paper Award**.
  - **Shape:** takes an interface everyone assumed fixed (interrupt delivery through
    the hypervisor) and shows a different split of responsibilities between hardware
    and software recovers the lost performance.
  - **Self-check:** can you name the boundary your design moves, and who was paying
    the cost before it moved?

### 4. The workload study that recalibrates the hardware community

- **"Clearing the Clouds: a study of emerging scale-out workloads on modern
  hardware"** — Michael Ferdman, Almutaz Adileh, Onur Kocberber, Stavros Volos,
  Mohammad Alisafaee, Djordje Jevdjic, Cansu Kaynak, Adrian Daniel Popescu, Anastasia
  Ailamaki, Babak Falsafi. ASPLOS 2012; **2023 Influential Paper Award**.
  - **Shape:** measurement as contribution — careful characterization of real
    workloads against real microarchitecture, with conclusions that redirect design
    effort. Proof that ASPLOS accepts evidence papers when the methodology is
    architecture-grade.
  - **Self-check:** does your characterization identify *which hardware structures*
    are mis-provisioned, or does it stop at application-level throughput?

### 5. The allocator that made memory management a multiprocessor problem

- **"Hoard: A Scalable Memory Allocator for Multithreaded Applications"** — Emery
  Berger, Kathryn McKinley, Robert Blumofe, Paul Wilson. ASPLOS 2000; **2019
  Influential Paper Award** (source: SIGARCH award page).
  - **Shape:** a language-runtime component (the allocator) redesigned around
    architectural realities (false sharing, per-processor contention) — the PL/OS/
    architecture triangle in one artifact.
  - **Self-check:** does your runtime mechanism name the architectural phenomenon it
    is designed against, and measure it directly?

## Shape × layer summary

| Award year | Paper (ASPLOS year) | Primary layer pairing | Contribution shape |
| --- | --- | --- | --- |
| 2024 | DianNao (2014) | Architecture × workload/software | Domain accelerator argued from data movement |
| 2024 | Paragon (2013) | OS/runtime × heterogeneous hardware | QoS scheduling over architectural diversity |
| 2024 | ELI (2012) | Hypervisor × hardware interface | Boundary redraw for I/O virtualization |
| 2023 | Clearing the Clouds (2012) | Measurement × microarchitecture | Workload characterization that redirects design |
| 2019 | Hoard (2000) | Language runtime × multiprocessor | Allocator built against false sharing |

## Award-listed but not row-verified here (confirm before citing)

The 2025 award recognized **"PowerNap: Eliminating Server Idle Power" (ASPLOS 2009)**
and **"Unikernels: Library Operating Systems for the Cloud" (ASPLOS 2013)**, and the
2022 award recognized **"Learning from mistakes: a comprehensive study on real world
concurrency bug characteristics" (ASPLOS 2008)** — titles and years were verified on
SIGARCH postings, but full author lists were not re-read at check time, so they are
kept out of the shape rows. Confirm authors on ACM DL before quoting (待核实).

## Adding a new exemplar

1. Find the paper on the ACM DL ASPLOS series page and record the DOI, edition
   ordinal, full author list, and page range.
2. Prefer papers with hindsight validation — Influential Paper Award winners, or at
   minimum heavily-built-upon artifacts — over last year's best-paper picks.
3. State the *shape* (which layers the paper couples and how), not its numbers.
4. Update the access-date header. If the award page and the DL disagree, the DL entry
   controls the bibliographic facts. When verification fails, add the row as
   待核实 with no author attribution.
