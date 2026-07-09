# SIGCOMM Exemplars Library (problem × system class)

> **Verified via web search, access date 2026-07-09.** Every paper below was checked against the **dblp
> SIGCOMM proceedings stream** (`dblp.org/db/conf/sigcomm/...`) and the **ACM Digital Library** to confirm
> it appeared in the **main ACM SIGCOMM conference proceedings** (not a workshop, not Computer
> Communication Review as a standalone editorial, and not a sibling venue) — matching edition year, author
> list, and page range. Papers that could not be cleanly confirmed as **SIGCOMM main-track** were
> **omitted and documented below**. This is deliberately a short, verified list (6 verified > 20 guessed).
>
> **Sibling-confusion guard:** SIGCOMM is **not** NSDI, MobiCom, CoNEXT, IMC, or SIGMETRICS, and it is
> **not** IEEE/ACM Transactions on Networking. Several famous networking results live in those venues, and
> some SIGCOMM-adjacent classics appeared only in CCR as editorial notes. A networking paper being
> famous does **not** make it a SIGCOMM main-track paper (see omissions).
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent throughput numbers, latency percentiles, or table values — read the original in the
> ACM DL before citing anything. For SIGCOMM-specific policy, scope, and the do-not-misattribute list, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **problem × system class** is closest to yours, then study how that paper earns the
SIGCOMM bar: a **networking problem stated as measured pain**, a **design principle** rather than a point
fix, and **evaluation that survives real traffic, real topology, or real deployment** (see
[`../../skills/sigcomm-writing-style/SKILL.md`](../../skills/sigcomm-writing-style/SKILL.md),
[`../../skills/sigcomm-topic-selection/SKILL.md`](../../skills/sigcomm-topic-selection/SKILL.md), and
[`../../skills/sigcomm-experiments/SKILL.md`](../../skills/sigcomm-experiments/SKILL.md)). Ask each row's
self-check question before claiming your paper is "SIGCOMM-shaped."

---

## By system class

### Distributed lookup / peer-to-peer substrate

- **Stoica, Morris, Karger, Kaashoek & Balakrishnan, "Chord: A Scalable Peer-to-Peer Lookup Service for
  Internet Applications," SIGCOMM 2001, pp. 149-160.**
  Verified: `dblp.org/db/conf/sigcomm/StoicaMKKB01`; ACM DL `10.1145/383059.383071`. Later an ACM SIGCOMM
  Test of Time award paper.
  - **Why it is an exemplar:** distills a whole class of systems (P2P storage, DNS-like lookup) into **one
    primitive** — consistent-hashing lookup with provable logarithmic routing state — so the *mechanism*,
    not one application, is the contribution. The model of a SIGCOMM abstraction that outlives its era.
  - **Self-check:** is your contribution a reusable networking primitive with a stated invariant, rather
    than a single tuned deployment?

### Enterprise network control (software-defined precursor)

- **Casado, Freedman, Pettit, Luo, McKeown & Shenker, "Ethane: Taking Control of the Enterprise,"
  SIGCOMM 2007.**
  Verified: `dblp.org/db/conf/sigcomm/sigcomm2007`; ACM DL SIGCOMM '07 proceedings.
  - **Why it is an exemplar:** reframes enterprise security and management as a **centralized
    policy-then-forwarding** architecture, and backs the architecture with a real campus deployment — the
    lineage that became software-defined networking. SIGCOMM rewards an architecture argument grounded in
    a running system.
  - **Self-check:** does your design make a **structural** claim about where control belongs, evidenced by
    a deployment rather than a diagram?

### Data-center network architecture

- **Greenberg, Hamilton, Jain, Kandula, Kim, Lahiri, Maltz, Patel & Sengupta, "VL2: A Scalable and
  Flexible Data Center Network," SIGCOMM 2009.**
  Verified: `dblp.org/db/conf/sigcomm/sigcomm2009`; ACM DL SIGCOMM '09 proceedings.
  - **Why it is an exemplar:** starts from **measured** data-center traffic and agility requirements, then
    designs a Clos-based fabric with valiant load balancing to meet them — problem measured first,
    architecture derived second. A template for the SIGCOMM "measurement motivates mechanism" arc.
  - **Self-check:** is your architecture justified by a **traffic characterization** you measured, not by
    an assumed workload?

### Data-center congestion control

- **Alizadeh, Greenberg, Maltz, Padhye, Patel, Prabhakar, Sengupta & Sridharan, "Data Center TCP
  (DCTCP)," SIGCOMM 2010, CCR 40(4).**
  Verified: `dblp.org/db/conf/sigcomm/sigcomm2010`; ACM DL `10.1145/1851182.1851192`. Later an ACM SIGCOMM
  Test of Time award paper.
  - **Why it is an exemplar:** uses the **ECN signal already in commodity switches** to react to the
    *extent* of congestion, not just its presence, cutting buffer occupancy while holding throughput. A
    minimal, deployable change validated on a real testbed — the SIGCOMM taste for elegant deltas over
    clean-slate rewrites.
  - **Self-check:** does your mechanism exploit an **existing deployed capability** and prove the win with
    switch-level measurement, rather than assume new hardware?

### Data-center flow scheduling / transport

- **Alizadeh, Yang, Sharif, Katti, McKeown, Prabhakar & Shenker, "pFabric: Minimal Near-Optimal
  Datacenter Transport," SIGCOMM 2013.**
  Verified: `dblp.org/db/conf/sigcomm/sigcomm2013`; ACM DL `10.1145/2486001.2486031`.
  - **Why it is an exemplar:** decouples **flow scheduling from rate control**, pushing priority into the
    fabric so simple endpoints approach optimal flow-completion time — reported at the **tail** (99th
    percentile) for short flows, not just the mean. The SIGCOMM reflex to report the distribution, not the
    average.
  - **Self-check:** do you separate the mechanism's **principle** from its knobs, and report **tail**
    behavior where tails are what hurt?

### Production fabric evolution (experience / longitudinal)

- **Singh, Ong, Agarwal, Anderson, Armistead, Bannon, Boving, ... Hölzle, Stuart & Vahdat, "Jupiter
  Rising: A Decade of Clos Topologies and Centralized Control in Google's Datacenter Network,"
  SIGCOMM 2015.**
  Verified: `dblp.org/db/conf/sigcomm/sigcomm2015`; ACM DL SIGCOMM '15 proceedings.
  - **Why it is an exemplar:** an **operator experience paper** — a decade of production data-center
    fabric generations, the decisions that held and the ones that did not. The genre SIGCOMM's **experience
    track** is for: lessons only a deployment at scale can teach.
  - **Self-check:** if this is an experience submission, does it deliver **generalizable lessons from real
    operation**, not a product brochure?

---

## By problem (each cell is a verified SIGCOMM paper above)

| Problem | Verified SIGCOMM exemplar | Edition : pages/DOI | System class |
| --- | --- | --- | --- |
| Scalable lookup primitive | Stoica et al., "Chord" | 2001 : 149-160 | P2P / DHT |
| Enterprise control architecture | Casado et al., "Ethane" | 2007 : SIGCOMM '07 | SDN precursor |
| Data-center fabric design | Greenberg et al., "VL2" | 2009 : SIGCOMM '09 | DC architecture |
| Data-center congestion | Alizadeh et al., "DCTCP" | 2010 : 10.1145/1851182.1851192 | DC transport |
| Near-optimal flow completion | Alizadeh et al., "pFabric" | 2013 : 10.1145/2486001.2486031 | DC scheduling |
| A decade of production fabric | Singh et al., "Jupiter Rising" | 2015 : SIGCOMM '15 | Experience / operations |

> Six verified papers across six problem × system-class cells. The DCTCP → pFabric pair also shows **a
> research line** (react to congestion extent → schedule flows in the fabric) within SIGCOMM, useful when
> positioning an incremental-but-principled data-center-transport contribution.

---

## Omitted for lack of clean SIGCOMM main-track verification (do not attribute without re-checking)

To keep the list zero-hallucination, the following were **excluded** after checking — several are exactly
the venue confusions the header warns about:

- **"OpenFlow: Enabling Innovation in Campus Networks" (McKeown et al., 2008)** — appeared in **ACM
  SIGCOMM Computer Communication Review** as an **editorial note**, not the SIGCOMM main-track
  proceedings. Landmark, but not a SIGCOMM conference paper. Listed here only as a guardrail.
- **"Hedera: Dynamic Flow Scheduling for Data Center Networks" (Al-Fares et al.)** — **NSDI 2010**, not
  SIGCOMM. A frequent misfile because it sits next to SIGCOMM data-center work. Omitted.
- **"Random Early Detection Gateways for Congestion Avoidance" (Floyd & Jacobson, 1993)** — **IEEE/ACM
  Transactions on Networking**, a *journal*, not the SIGCOMM proceedings. Omitted.
- **"BBR: Congestion-Based Congestion Control" (Cardwell et al., 2017)** — appeared in **Communications of
  the ACM** and as an IETF draft; no SIGCOMM main-track placement could be confirmed. Omitted to avoid
  venue misattribution.

Before adding any paper, confirm it on `dblp.org/db/conf/sigcomm/` and the ACM DL by matching the **SIGCOMM
edition** (the proceedings landing page names the ACM SIGCOMM conference for that year), then record author
list, year, and pages, and update the access-date header. Distinguish the **main-track proceedings** from
CCR editorial notes and from workshop tracks. When in doubt, omit. If web search is unavailable, add the
row as **待核实 / TO VERIFY** with **no attribution**.
