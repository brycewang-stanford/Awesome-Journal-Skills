# PODC Exemplars Library (contribution shape × model)

> **Verified via web search, access date 2026-07-09.** Every paper below was checked against
> **dblp** and the **ACM Digital Library** to confirm it appeared at the **ACM Symposium on
> Principles of Distributed Computing (PODC)** — matching title, author list, year, and venue
> string. Results that could not be cleanly confirmed as PODC (as opposed to DISC, SPAA, STOC,
> FOCS, or a journal such as JACM or *Distributed Computing*) were **omitted and documented below**.
> It is deliberately a short, verified list (5 verified > 15 guessed).
>
> **Sibling-confusion guard:** PODC is **not** DISC, **not** SPAA, **not** STOC/FOCS, and **not**
> PODS. Several canonical distributed-computing results were published *in journals* or at *DISC*,
> not at PODC; a famous author or a familiar theorem name does **not** prove a PODC placement. Each
> row was checked to be a PODC edition specifically (see omissions).
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent theorem statements, constants, or bounds — read the original on ACM DL / arXiv
> before citing anything. For PODC-specific policy, scope, and the cycle model, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **contribution shape × model** is closest to yours, then study how that paper
fixes a **precise distributed model** (network, timing, faults, cost measure), states a **result a
distributed-computing researcher recognizes as fundamental**, and backs it with a **proof** — the
PODC bar (see [`../../skills/podc-writing-style/SKILL.md`](../../skills/podc-writing-style/SKILL.md),
[`../../skills/podc-topic-selection/SKILL.md`](../../skills/podc-topic-selection/SKILL.md), and
[`../../skills/podc-experiments/SKILL.md`](../../skills/podc-experiments/SKILL.md)). For each, ask
the self-check question before claiming your paper is "PODC-shaped."

Several rows are **Dijkstra Prize** honorees (the joint PODC/DISC decade-of-impact award), so they
also model what "influence a decade later" looks like at this venue.

---

## By contribution shape

### New model / computational paradigm — population protocols

- **Angluin, Aspnes, Diamadi, Fischer & Peralta, "Computation in networks of passively mobile
  finite-state sensors," PODC 2004, pp. 290-299.** Verified: ACM DL / dblp. Introduced **population
  protocols** — anonymous finite-state agents that stably compute a predicate of their inputs via
  pairwise interactions. Later an **Edsger W. Dijkstra Prize** honoree.
  - **Why it is an exemplar:** it defines a **new, minimal model** and characterizes exactly what it
    can compute — a paradigm the community then built a subfield around. The contribution is the
    model plus its power/limits, not one algorithm.
  - **Self-check:** does your paper define a model whose computational power you then pin down, or is
    it one more algorithm inside an existing model?

### Foundational hierarchy — wait-free shared memory

- **Herlihy, "Impossibility and universality results for wait-free synchronization," PODC 1988,
  DOI 10.1145/62546.62593.** Verified: ACM DL / dblp. Established the **consensus-number hierarchy**:
  synchronization primitives are ranked by the number of processes among which they can solve
  wait-free consensus, with read/write registers at the bottom and universal objects at the top.
  - **Why it is an exemplar:** a single organizing idea (consensus number) that **classifies an
    entire design space** and proves both an impossibility (a low object cannot implement a high one)
    and a universality (a high-enough object implements everything). The archetypal PODC
    shared-memory result.
  - **Self-check:** does your result *organize* a space of objects or problems with a proven ranking,
    rather than adding a single construction whose place in the space is unclear?

### Necessary-and-sufficient conditions — failure detectors

- **Chandra, Hadzilacos & Toueg, "The weakest failure detector for solving consensus," PODC 1992,
  pp. 147-158, DOI 10.1145/135419.135451.** Verified: ACM DL / dblp. **Dijkstra Prize** honoree.
  Determined the **weakest** failure-detector information sufficient to solve consensus in an
  asynchronous crash-prone system, and proved it necessary.
  - **Why it is an exemplar:** it answers a question in the strong form the venue prizes — not "here
    is an algorithm using detector D" but "**D is exactly what is required**," a matching
    sufficiency-and-necessity result.
  - **Self-check:** can you state your assumption as *the weakest / tightest* one that suffices, with
    a lower bound showing nothing weaker works — or only as *an* assumption that happens to work?

### Impossibility technique — consensus lower bounds

- **Fischer, Lynch & Merritt, "Easy impossibility proofs for distributed consensus problems,"
  PODC 1985.** Verified: dblp / ACM DL. Gave **simpler proofs** of impossibility/lower-bound results
  for agreement in the presence of faults, distilling the proof technique itself.
  - **Why it is an exemplar:** the contribution is a **cleaner argument** for known impossibilities —
    PODC rewards a proof method others can reuse, not just a new theorem. It models the venue's taste
    for proofs that teach a technique.
  - **Self-check:** does your paper leave the community with a reusable proof *technique* (a valency
    argument, an indistinguishability argument, a covering argument), or only a one-off calculation?

### Locality lower bound — distributed graph algorithms

- **Kuhn, Moscibroda & Wattenhofer, "What cannot be computed locally!," PODC 2004, pp. 300-309.**
  Verified: ACM DL / dblp. Proved **locality lower bounds** — time/approximation trade-offs for
  local distributed algorithms on problems such as minimum vertex cover and maximal matching in the
  message-passing (LOCAL) model.
  - **Why it is an exemplar:** it establishes that **no local algorithm** can do better than a stated
    bound, framing a whole line of LOCAL/CONGEST lower-bound work. A model-and-cost-measure-precise
    negative result, the distributed-graph counterpart to the shared-memory impossibilities above.
  - **Self-check:** is your distributed-graph result tied to an explicit locality/round budget with a
    matching lower bound, or is it an algorithm whose optimality is left open?

---

## Contribution-shape ↔ exemplar (verified rows)

| Contribution shape | Verified PODC exemplar | Edition | Model / technique |
| --- | --- | --- | --- |
| New model / paradigm | Angluin, Aspnes, Diamadi, Fischer & Peralta | PODC 2004 | Population protocols |
| Foundational hierarchy | Herlihy, "...wait-free synchronization" | PODC 1988 | Consensus-number hierarchy (shared memory) |
| Necessary-and-sufficient | Chandra, Hadzilacos & Toueg | PODC 1992 | Weakest failure detector for consensus |
| Impossibility technique | Fischer, Lynch & Merritt | PODC 1985 | Simplified consensus impossibility proofs |
| Locality lower bound | Kuhn, Moscibroda & Wattenhofer | PODC 2004 | LOCAL-model distributed-graph lower bounds |

> Five verified papers across five contribution shapes, spanning PODC's two great model families —
> **shared memory** (wait-free hierarchy, failure detectors) and **message passing** (population
> protocols, consensus impossibility, LOCAL lower bounds). Note that PODC 2004 alone produced two of
> them (pp. 290-299 and 300-309), a reminder that a single program can define multiple subfields.

---

## Omitted for lack of clean PODC verification (do not attribute to PODC without re-checking)

To keep the list zero-hallucination, the following were **excluded** after checking — several are
exactly the venue confusions the header warns about:

- **Fischer, Lynch & Paterson, "Impossibility of Distributed Consensus with One Faulty Process"
  (the FLP result)** — the canonical citation is **JACM 32(2), 1985**, a *journal*, and its
  conference origin was **PODS 1983**, *not* PODC. A direct naming trap (PODS ≠ PODC); listed only
  as a guardrail. Cite the journal (or the PODS conference version) accurately, never as PODC.
- **Lamport, "Time, Clocks, and the Ordering of Events in a Distributed System"** — **CACM 21(7),
  1978**, a journal, not a PODC paper. Omitted.
- **Herlihy & Wing, "Linearizability: A Correctness Condition for Concurrent Objects"** — **ACM
  TOPLAS 12(3), 1990**, a journal. The PODC ecosystem uses it constantly, but it is not a PODC
  paper. Omitted.
- **Dwork, Lynch & Stockmeyer, "Consensus in the Presence of Partial Synchrony"** — the widely cited
  version is **JACM 35(2), 1988**; treat any PODC-vs-journal attribution carefully and cite the
  journal unless a specific PODC edition is confirmed on dblp. Omitted here to avoid misattribution.

Before adding any paper, confirm it on **dblp** and **ACM DL** by matching the venue string to a
**PODC** edition (not DISC, SPAA, STOC, FOCS, OPODIS, or a journal), then record authors, year, and
DOI/pages, and update the access-date header. When in doubt, omit. If web search is unavailable, add
the row as **待核实 / TO VERIFY** with **no attribution**.
