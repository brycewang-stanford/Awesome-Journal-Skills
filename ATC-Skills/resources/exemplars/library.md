# ATC Exemplars Library (contribution shape × systems area)

> **Verified via web search, access date 2026-07-09.** Every paper below was checked against
> **dblp**, the **ACM Digital Library**, and the **USENIX ATC technical-sessions / proceedings
> pages** to confirm it appeared at the **USENIX Annual Technical Conference (USENIX ATC)** — the
> venue now continued as the **ACM SIGOPS Annual Technical Conference** — matching title, author
> list, year, and venue string. Papers that could not be cleanly confirmed as ATC (as opposed to
> OSDI, SOSP, NSDI, EuroSys, or FAST) were **omitted and documented below**. It is deliberately a
> short, verified list (5 verified > 15 guessed).
>
> **Sibling-confusion guard:** ATC is **not** OSDI, **not** SOSP, **not** NSDI, **not** EuroSys,
> and **not** FAST. Many landmark systems papers were introduced at those venues instead; a famous
> systems name or a familiar system does **not** prove ATC. Each row was checked to be a USENIX ATC
> edition specifically (see omissions).
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent throughput numbers, speedups, or table values — read the original on the
> USENIX/ACM DL page before citing anything. For ATC-specific policy, scope, the two-round review,
> and the SIGOPS transition, see [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **contribution shape × systems area** is closest to yours, then study how that
paper states a **systems problem practitioners recognize**, backs it with **measured evidence on a
real implementation** (end-to-end plus microbenchmarks), and is honest about where the design costs
show up — the ATC bar (see
[`../../skills/atc-writing-style/SKILL.md`](../../skills/atc-writing-style/SKILL.md),
[`../../skills/atc-topic-selection/SKILL.md`](../../skills/atc-topic-selection/SKILL.md), and
[`../../skills/atc-experiments/SKILL.md`](../../skills/atc-experiments/SKILL.md)). For each, ask the
self-check question before claiming your paper is "ATC-shaped." Several rows are USENIX ATC **Best
Paper** honorees, so they also model the ceiling at this venue.

---

## By contribution shape

### Systems software / new OS artifact — virtualization

- **Kivity, Laor, Costa, Enberg, Har'El, Marti & Zolotarov, "OSv—Optimizing the Operating System
  for Virtual Machines," USENIX ATC 2014.** Verified: usenix.org `atc14` technical-sessions page;
  ACM DL `10.5555/2643634.2643642`; dblp. A guest OS designed to run a single application inside a
  cloud VM, shedding the assumptions a general-purpose OS makes.
  - **Why it is an exemplar:** it takes a concrete deployment reality (one app per VM in the cloud)
    and delivers a **built, runnable system** whose design choices are justified by measurement, not
    novelty for its own sake — the classic ATC "system you can run." The contribution is an artifact
    others adopt.
  - **Self-check:** does your paper deliver a working system whose design is driven by a real
    deployment constraint, evaluated with real workloads rather than a proof-of-concept demo?

### Systems architecture — networking / virtualization boundary

- **Niu, Xu, Cheng, Su, Xiong, Wang, Han & Winstein, "NetKernel: Making Network Stack Part of the
  Virtualized Infrastructure," USENIX ATC 2020.** Verified: usenix.org `atc20` presentation page;
  ACM DL `10.5555/3489146.3489156`; dblp. Decouples the network stack from the guest VM and offers
  it as an independent, operator-managed module.
  - **Why it is an exemplar:** it re-draws a **system boundary** (where the network stack lives) and
    argues the case with an implementation plus measurements of what the new boundary costs and
    saves. An architectural contribution with practical payoff for operators — squarely ATC.
  - **Self-check:** if your contribution is "move this responsibility across a boundary," do you
    show the win *and* pay the honest cost (added indirection, compatibility) with numbers?

### Technique + implementation — storage / file systems

- **Hu, Kim, Zhang, Kaminsky, Fried, Katz-Bassett, et al. — "TxFS: Leveraging File-System Crash
  Consistency to Provide ACID Transactions," USENIX ATC 2018 (Best Paper).** Verified: USENIX ATC
  '18 best-paper announcement (UT Austin news); ACM DL; dblp. Builds transactional semantics on top
  of a journaling file system's existing crash-consistency machinery.
  - **Why it is an exemplar:** it finds leverage in a mechanism the system **already has** (the
    journal) rather than bolting on a new subsystem, and validates the guarantee with a working
    implementation. Minimal, insightful, and evaluated — the ATC storage sweet spot.
  - **Self-check:** does your technique reuse an existing mechanism to deliver a stronger guarantee,
    with correctness and performance both measured on a real system?

### Technique + tool — dynamic binary translation / hypervisors

- **Spink, Wagstaff & Franke, "A Retargetable System-Level DBT Hypervisor," USENIX ATC 2019 (Best
  Paper).** Verified: Edinburgh ICSA best-paper announcement; the ACM DL special issue on the ATC
  2019 award papers; dblp. A dynamic-binary-translation hypervisor whose guest and host
  architectures are retargetable rather than hard-wired.
  - **Why it is an exemplar:** it turns a normally one-off engineering effort (a per-architecture
    DBT hypervisor) into a **general, retargetable mechanism**, then shows it works across targets.
    Depth of systems engineering with a generalizing idea — an ATC hallmark.
  - **Self-check:** is your engineering contribution a *reusable mechanism* others could retarget or
    extend, not a single hand-built instance?

### Automated method + tool — distributed-systems verification

- **Yao, Tao, Gu, Nieh, Jana & Ryan — "DistAI: Data-Driven Automated Invariant Learning for
  Distributed Protocols," USENIX ATC 2021 (Best Paper).** Verified: Columbia SSL best-paper
  announcement; ACM DL; dblp. Learns candidate invariants from simulation data to help
  automatically verify distributed protocols.
  - **Why it is an exemplar:** it attacks a hard, practitioner-relevant problem (getting invariants
    for distributed-protocol verification) with an **automated tool** evaluated on real protocols —
    showing ATC's appetite for tooling that makes a painful task tractable.
  - **Self-check:** does your tool automate something practitioners currently do by hand, and is it
    evaluated on real targets with an honest account of where it fails?

---

## Contribution-shape ↔ exemplar (verified rows)

| Contribution shape | Verified ATC exemplar | Edition | Area |
| --- | --- | --- | --- |
| New OS artifact | Kivity et al., "OSv" | USENIX ATC 2014 | Virtualization |
| Systems architecture | Niu et al., "NetKernel" | USENIX ATC 2020 | Networking |
| Technique + implementation | "TxFS" (Best Paper) | USENIX ATC 2018 | Storage / FS |
| Technique + tool | Spink, Wagstaff & Franke, "Retargetable DBT Hypervisor" (Best Paper) | USENIX ATC 2019 | Virtualization / DBT |
| Automated method + tool | Yao et al., "DistAI" (Best Paper) | USENIX ATC 2021 | Distributed / verification |

> Five verified papers across five contribution shapes and five systems areas — a snapshot of ATC's
> breadth, from a whole guest OS to an invariant-learning tool. Three are Best Paper honorees.

---

## Omitted for lack of clean ATC verification (do not attribute to ATC without re-checking)

To keep the list zero-hallucination, the following were **excluded** after checking — several are
exactly the sibling-venue confusions the header warns about:

- **"Scaling Memcache at Facebook" (Nishtala et al.)** — verified to be **NSDI 2013**, *not* ATC,
  despite being a canonical practical-systems paper. A direct sibling-venue trap; listed only as a
  guardrail.
- **"The Google File System" (Ghemawat, Gobioff & Leung)** — **SOSP 2003**, not ATC. Omitted.
- **"MapReduce: Simplified Data Processing on Large Clusters" (Dean & Ghemawat)** — **OSDI 2004**,
  not ATC. Omitted.
- **"Disco: Running Commodity Operating Systems on Scalable Multiprocessors" (Bugnion, Devine &
  Rosenblum)** — **SOSP 1997** (and a TOCS journal version), a SIGOPS Hall of Fame paper, but *not*
  an ATC placement. A frequent virtualization-history misattribution; omitted.

Before adding any paper, confirm it on **dblp** and the **USENIX/ACM DL** by matching the venue
string to a USENIX ATC edition (not OSDI, SOSP, NSDI, EuroSys, or FAST), then record authors, year,
and DOI/pages, and update the access-date header. When in doubt, omit. If web search is
unavailable, add the row as **待核实 / TO VERIFY** with **no attribution**. Note that from 2026 the
venue string becomes **ACM SIGOPS Annual Technical Conference**; pre-2026 editions carry the
**USENIX** string.
