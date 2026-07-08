# OSDI Exemplars Library (system class × era)

> **Verified via web search against dblp and USENIX proceedings pages, access date
> 2026-07-08.** Every paper below was confirmed to have appeared at **OSDI
> specifically** — matching the dblp `conf/osdi/` record or the `usenix.org` proceedings
> page, with authors, edition, and (where available) page range. Papers that could not
> be cleanly pinned to OSDI were **excluded and documented below**, because the systems
> canon scatters across OSDI, SOSP, NSDI, and ATC and memory routinely misfiles them.
>
> **Sibling-confusion guard:** OSDI is a **USENIX** venue. A famous paper being "a
> classic systems paper" proves nothing about its venue: GFS is SOSP, Raft is ATC,
> Firecracker is NSDI. Verify on `dblp.org/db/conf/osdi/` or the `usenix.org` page
> before attributing anything to OSDI.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**.
> It does not reproduce results, speedup numbers, or table values — USENIX proceedings
> are open access, so download the free PDF from `usenix.org` and read the original
> before citing anything. For current policy see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row closest to your system class, then study how that paper (a) names an
**abstraction or mechanism** rather than an implementation effort, (b) argues from a
**built and measured artifact**, and (c) states what the design **trades away** — the
three moves `osdi-writing-style` and `osdi-topic-selection` test for. Ask each row's
self-check question before claiming your draft is "OSDI-shaped."

---

## The verified five

### Data-parallel programming abstraction (2004)

- **Dean & Ghemawat, "MapReduce: Simplified Data Processing on Large Clusters,"
  OSDI '04 (6th), pp. 137–150.** Verified: dblp `conf/osdi/DeanG04`.
  - **Why it is an exemplar:** collapses a whole class of cluster programs into two
    user-supplied functions and pushes fault tolerance, partitioning, and scheduling
    into the runtime. The contribution is the **programming abstraction plus the
    machinery that makes it survive failures at scale**, argued from production use.
  - **Self-check:** can you state your interface in one sentence and name what the
    runtime silently handles on the programmer's behalf?

### Distributed structured storage (2006)

- **Chang, Dean, Ghemawat, Hsieh, Wallach, Burrows, Chandra, Fikes & Gruber,
  "Bigtable: A Distributed Storage System for Structured Data," OSDI '06 (7th).**
  Verified: dblp/USENIX; recognized among OSDI '06 best papers (SIGOPS Hall of Fame
  listing).
  - **Why it is an exemplar:** a deliberately **narrow data model** (sorted sparse
    map) chosen so the system can scale; the paper is explicit about what it refuses
    to provide (full relational semantics) and why.
  - **Self-check:** does your paper defend what the system does *not* do as a design
    decision rather than hiding it as a limitation?

### Globally distributed transactions (2012)

- **Corbett et al., "Spanner: Google's Globally-Distributed Database," OSDI '12
  (10th).** Verified: `usenix.org/conference/osdi12/technical-sessions/presentation/corbett`.
  - **Why it is an exemplar:** derives external-consistency guarantees from an
    unconventional primitive (clock-uncertainty intervals) and quantifies the
    primitive's real behavior. Mechanism, guarantee, and measurement are one story.
  - **Self-check:** is there one enabling primitive whose measured properties carry
    your correctness or performance claim?

### Machine-learning systems (2016)

- **Abadi et al., "TensorFlow: A System for Large-Scale Machine Learning," OSDI '16
  (12th).** Verified: `usenix.org/conference/osdi16/technical-sessions/presentation/abadi`.
  - **Why it is an exemplar:** frames ML execution as a **systems problem** — dataflow
    graphs mapped onto heterogeneous hardware — and evaluates as a system (throughput,
    scaling), not as a model-accuracy paper. The template for OSDI's ML-systems lane.
  - **Self-check:** if the learned model were swapped out, would your contribution
    still stand as a systems result?

### LLM inference serving (2022)

- **Yu, Jeong, Kim, Kim & Chun, "Orca: A Distributed Serving System for
  Transformer-Based Generative Models," OSDI '22 (16th), pp. 521–538.** Verified:
  dblp `conf/osdi/YuJKKC22`.
  - **Why it is an exemplar:** identifies a scheduling granularity mismatch
    (request-level batching vs iteration-level generation) and rebuilds the serving
    loop around the right granularity. A small, sharp insight scaled into a system.
  - **Self-check:** can you name the single mismatch your design corrects, in one
    sentence a reviewer could repeat?

---

## By system class

| System class | Verified OSDI exemplar | Edition | The reusable move |
| --- | --- | --- | --- |
| Programming abstraction / runtime | MapReduce (Dean & Ghemawat) | OSDI '04 | Two-function interface, fault tolerance in the runtime |
| Storage system | Bigtable (Chang et al.) | OSDI '06 | Narrow data model defended as a scaling decision |
| Distributed database / consistency | Spanner (Corbett et al.) | OSDI '12 | One measured primitive carries the guarantee |
| ML systems | TensorFlow (Abadi et al.) | OSDI '16 | ML execution evaluated as a system, not a model |
| Inference serving | Orca (Yu et al.) | OSDI '22 | Fix a granularity mismatch in the scheduling loop |

> Five verified papers across five system classes and eighteen years — also a lineage:
> MapReduce-era cluster abstractions lead to Bigtable/Spanner storage, which lead to
> the TensorFlow/Orca ML-systems lane that dominates recent OSDI programs.

---

## Excluded — sibling-venue traps (do not attribute to OSDI)

Checked and excluded during verification; each is a canonical misfiling risk:

- **"The Google File System" (Ghemawat, Gobioff & Leung)** — **SOSP 2003** (ACM), not
  OSDI, despite being the direct ancestor of the Bigtable/MapReduce line above.
- **"In Search of an Understandable Consensus Algorithm" (Raft; Ongaro & Ousterhout)**
  — **USENIX ATC 2014**, not OSDI.
- **"ZooKeeper: Wait-free Coordination for Internet-scale Systems" (Hunt et al.)** —
  **USENIX ATC 2010**, not OSDI.
- **"Firecracker: Lightweight Virtualization for Serverless Applications" (Agache et
  al.)** — **NSDI 2020**, not OSDI.
- **"Efficient Memory Management for Large Language Model Serving with PagedAttention"
  (vLLM; Kwon et al.)** — **SOSP 2023**, not OSDI, even though it cites and extends
  Orca (OSDI '22).

Before adding any paper here, resolve it on `dblp.org/db/conf/osdi/` (record key
`conf/osdi/...`) **and** open its `usenix.org` proceedings page — USENIX proceedings
are open access, so the check costs one click. Record authors, edition, pages, and
update the access-date header. When in doubt, omit; if verification tooling is
unavailable, add the row as **待核实** with no venue attribution.
