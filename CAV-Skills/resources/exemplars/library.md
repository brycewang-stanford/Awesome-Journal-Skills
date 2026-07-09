# CAV Exemplars Library (contribution shape × method)

> **Verified via web search, access date 2026-07-09.** Every paper below was checked against
> **dblp** and the **Springer LNCS** book pages to confirm it appeared at the **International
> Conference on Computer Aided Verification (CAV)** — matching title, author list, year, and LNCS
> volume. Papers that could not be cleanly confirmed as CAV (as opposed to TACAS, FMCAD, VMCAI,
> POPL, or PLDI) were **omitted and documented below**. It is deliberately a short, verified list
> (5 verified > 15 guessed).
>
> **Sibling-confusion guard:** CAV is **not** TACAS, **not** FMCAD, **not** VMCAI, and **not** a
> PL venue (POPL/PLDI). Several canonical verification tools and techniques were introduced at
> those venues instead; a famous author or a familiar tool name does **not** prove CAV. Each row
> was checked to be a CAV edition specifically (see omissions).
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent results, benchmark numbers, or runtimes — read the original on Springer LNCS
> before citing anything. For CAV-specific policy, categories, and the cycle model, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **contribution shape × method** is closest to yours, then study how that paper
states a **verification problem the community recognizes**, backs it with **evidence proportional
to the claim** (a soundness argument, a fair benchmark comparison, or a usable tool), and makes its
scope and limits explicit — the CAV bar (see
[`../../skills/cav-writing-style/SKILL.md`](../../skills/cav-writing-style/SKILL.md),
[`../../skills/cav-topic-selection/SKILL.md`](../../skills/cav-topic-selection/SKILL.md), and
[`../../skills/cav-experiments/SKILL.md`](../../skills/cav-experiments/SKILL.md)). For each, ask the
self-check question before claiming your paper is "CAV-shaped."

CAV's four submission categories map onto these shapes: a new **technique/algorithm** is a Regular
Paper; a **usable tool** on standard benchmarks is a Short Tool Paper; a verification **applied to
a real system** is a Short Application Paper or an Industrial Experience Report.

---

## By contribution shape

### Verification technique / algorithm — abstraction

- **Clarke, Grumberg, Jha, Lu & Veith, "Counterexample-Guided Abstraction Refinement," CAV 2000**
  (LNCS 1855, pp. 154-169). Verified: dblp `rec/conf/cav/ClarkeGJLV00`; Springer LNCS 1855.
  Introduced **CEGAR** — automatically refining a predicate abstraction using spurious
  counterexamples.
  - **Why it is an exemplar:** it turns an intractable state-explosion problem into an automatable
    loop with a clear soundness story, and the technique travels across model checkers rather than
    being tied to one tool. A durable *algorithmic* contribution, the archetypal CAV Regular Paper.
  - **Self-check:** is your contribution a general technique with a stated soundness/completeness
    property, evaluated to show it scales past what the prior method could handle?

### Verification technique / algorithm — SAT/SMT-based model checking

- **McMillan, "Interpolation and SAT-Based Model Checking," CAV 2003** (LNCS 2725, pp. 1-13).
  Verified: dblp `rec/conf/cav/McMillan03`; Springer LNCS 2725. Introduced **Craig-interpolation**
  based unbounded model checking over a SAT backend.
  - **Why it is an exemplar:** it connects a proof-theoretic idea (interpolants) to a scalable
    verification algorithm and demonstrates the gain on **industrial hardware benchmarks** against a
    named prior method — technique plus honest, comparative evidence.
  - **Self-check:** does your algorithm rest on a precise formal idea, and is the empirical gain
    shown against the right baseline on benchmarks the community accepts?

### Tool paper — SMT solver

- **Barrett, Conway, Deters, Hadarean, Jovanović, King, Reynolds & Tinelli, "CVC4," CAV 2011**
  (LNCS 6806, pp. 171-177). Verified: dblp `rec/conf/cav/BarrettCDHJKRT11`; Springer LNCS 6806.
  A widely used open-source SMT solver.
  - **Why it is an exemplar:** the model **Short Tool Paper** — a real, engineered, reusable solver
    described so others can use and build on it, with architecture and SMT-LIB support foregrounded
    over novelty claims. Tool papers are *not* anonymized at CAV precisely because the tool's
    identity is the point.
  - **Self-check:** is your tool downloadable, documented, and evaluated on standard benchmarks, and
    does the paper explain the design decisions a user or extender needs — not just a new idea?

### New application domain — neural-network verification (technique)

- **Katz, Barrett, Dill, Julian & Kochenderfer, "Reluplex: An Efficient SMT Solver for Verifying
  Deep Neural Networks," CAV 2017** (LNCS 10426). Verified: dblp `rec/conf/cav/KatzBDJK17`;
  Springer LNCS 10426. Extended the simplex method to reason about ReLU networks.
  - **Why it is an exemplar:** it opened **neural-network verification** as a CAV subarea by casting
    a new, high-stakes problem as an SMT question with a genuine algorithmic contribution — showing
    that "foundations of verification" keep absorbing new domains.
  - **Self-check:** does your paper bring a real, hard verification problem into scope with a
    technique that is more than an off-the-shelf solver call, and does it show feasibility on
    realistic instances?

### Tool paper — reusable framework following a technique

- **Katz, Huang, Ibeling, Julian, Lazarus, Lim, Shah, Thakoor, Wu, Zeljić, Dill, Kochenderfer &
  Barrett, "The Marabou Framework for Verification and Analysis of Deep Neural Networks," CAV 2019**
  (LNCS 11561). Verified: dblp `rec/conf/cav/KatzHIJLLSTWZDK19`; Springer LNCS 11561.
  - **Why it is an exemplar:** it turns the Reluplex line into a **reusable, extensible framework** —
    the tool-paper follow-up that lets a whole community run and extend the technique, with the
    engineering (APIs, activation functions, topologies) as the contribution.
  - **Self-check:** if your work extends a prior technique into usable infrastructure, does the tool
    paper document reuse and extension points, not merely re-report the earlier result?

---

## Contribution-shape ↔ exemplar (verified rows)

| Contribution shape | Verified CAV exemplar | Edition | Method |
| --- | --- | --- | --- |
| Technique / algorithm (abstraction) | Clarke, Grumberg, Jha, Lu & Veith, "CEGAR" | CAV 2000 | Predicate-abstraction refinement |
| Technique / algorithm (SAT/SMT) | McMillan, "Interpolation and SAT-Based Model Checking" | CAV 2003 | Craig interpolation |
| Tool paper (SMT solver) | Barrett et al., "CVC4" | CAV 2011 | Solver engineering |
| New application domain | Katz et al., "Reluplex" | CAV 2017 | SMT for ReLU networks |
| Tool paper (framework) | Katz et al., "Marabou" | CAV 2019 | NN-verification framework |

> Five verified papers across five contribution shapes. Two are **Regular-Paper**-style techniques,
> two are **Tool Papers**, and one opens a new application domain — mirroring how CAV's category
> structure rewards both foundational algorithms and the usable tools that carry them.

---

## Omitted for lack of clean CAV verification (do not attribute to CAV without re-checking)

To keep the list zero-hallucination, the following were **excluded** after checking — several are
exactly the sibling-venue confusions the header warns about:

- **"Z3: An Efficient SMT Solver" (de Moura & Bjørner)** — verified to be **TACAS 2008**, *not*
  CAV, despite being the most-cited SMT-solver tool paper. A direct sibling-venue trap; listed only
  as a guardrail (CAV and TACAS are distinct even when both sit under FLoC/ETAPS ecosystems).
- **"Symbolic Model Checking without BDDs" / Bounded Model Checking (Biere, Cimatti, Clarke, Zhu)**
  — **TACAS 1999**, not CAV. Omitted.
- **"SAT-Based Model Checking without Unrolling" (IC3 / PDR; Bradley)** — **VMCAI 2011**, not CAV.
  A frequent misattribution; omitted.
- **"A Tool for Checking ANSI-C Programs" (CBMC; Clarke, Kroening, Lerda)** — **TACAS 2004**, not
  CAV. Omitted.
- **"Lazy Abstraction" (Henzinger, Jhala, Majumdar, Sutre)** — **POPL 2002**, a PL venue, not CAV.
  Omitted.

Before adding any paper, confirm it on **dblp** and **Springer LNCS** by matching the venue string
to a CAV edition (not TACAS, FMCAD, VMCAI, POPL, or PLDI), then record authors, year, and LNCS
volume/pages, and update the access-date header. When in doubt, omit. If web search is unavailable,
add the row as **待核实 / TO VERIFY** with **no attribution**.
