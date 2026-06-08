# *Operations Research* Exemplars Library (method × topic)

> **Verified via web search, access date 2026-06-08.** Every paper below was checked to confirm it
> actually appeared in **_Operations Research_** — the flagship methodology journal of **INFORMS** (the
> Institute for Operations Research and the Management Sciences; ISSN 0030-364X / 1526-5463) — with year
> and volume/issue, against INFORMS PubsOnline (`pubsonline.informs.org/doi/10.1287/opre...`) and the
> corroborating RePEc/IDEAS record for the journal (`ideas.repec.org/a/inm/oropre/...`), with Google
> Scholar lookups carrying the journal name. Papers that could not be fully verified **as _Operations
> Research_** were **omitted** — this is deliberately a short, clean list, not a long, uncertain one.
>
> **Sibling-journal guard.** *Operations Research* is **not** *Management Science*, *Mathematics of
> Operations Research*, *Manufacturing & Service Operations Management* (M&SOM), *INFORMS Journal on
> Computing*, *Operations Research Letters*, or *Mathematical Programming*. Several famous "OR" results
> live in those venues; the [Omitted](#omitted-for-lack-of-full-verification-do-not-attribute-to-operations-research)
> section records the traps checked and rejected. INFORMS publishes several of these siblings, so a
> `10.1287/...` DOI alone does **not** prove *Operations Research* — confirm the `opre` stem.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent theorems, bounds, constants, or computational numbers — read the original on
> INFORMS PubsOnline before citing any result. For *Operations Research*-specific scope, length tiers,
> the equation-free-introduction rule, and house style, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **method × decision problem** is closest to yours, then study how that paper turns an
operational question into a **rigorous, provable OR/MS methodological contribution** — the *Operations
Research* bar (see [`../../skills/ors-topic-selection/SKILL.md`](../../skills/ors-topic-selection/SKILL.md),
[`../../skills/ors-theory-development/SKILL.md`](../../skills/ors-theory-development/SKILL.md), and
[`../../skills/ors-methods/SKILL.md`](../../skills/ors-methods/SKILL.md)). For each, ask the self-check
question before claiming your paper is "*Operations Research*-shaped."

---

## By method

### Tractable robust optimization (deterministic optimization / robustness)

- **Bertsimas & Sim, "The Price of Robustness," _Operations Research_ 2004, 52(1):35–53.**
  Verified: `pubsonline.informs.org/doi/10.1287/opre.1030.0065`; RePEc `inm/oropre/v52y2004i1p35-53`.
  - **Why it is an exemplar:** controls the conservatism of a robust solution with a budget parameter so
    the robust counterpart **stays a linear program** and extends to discrete optimization, with
    probabilistic guarantees on constraint violation. The
    [`ors-theory-development`](../../skills/ors-theory-development/SKILL.md) move of choosing a model whose
    *structure* (here, LP-representable uncertainty) is exactly what enables tractability and theorems —
    and the [`ors-literature-positioning`](../../skills/ors-literature-positioning/SKILL.md) "precise
    delta": the tractability/conservatism trade-off stated against prior ellipsoidal robust models.
  - **Self-check:** does your formulation preserve a tractable structure (LP/conic/convex) *and* carry a
    provable guarantee, rather than buy robustness with an intractable counterpart?

### Heavy-traffic / many-server asymptotics (stochastic models / queueing)

- **Halfin & Whitt, "Heavy-Traffic Limits for Queues with Many Exponential Servers," _Operations Research_ 1981, 29(3):567–588.**
  Verified: `pubsonline.informs.org/doi/10.1287/opre.29.3.567`; RePEc `inm/oropre/v29y1981i3p567-588`.
  - **Why it is an exemplar:** identifies the scaling (now the **Halfin–Whitt / QED regime**) in which the
    probability of delay converges to a constant strictly between 0 and 1, via a weak-convergence /
    diffusion-limit argument — the [`ors-methods`](../../skills/ors-methods/SKILL.md) heavy-traffic
    machinery (functional CLT, state-space collapse) establishing an asymptotic performance law.
  - **Self-check:** does your stochastic model isolate the *regime* (scaling of arrival rate vs. servers)
    in which a clean limit and a usable approximation emerge, with the limit proved, not asserted?

### Approximate dynamic programming for large-scale stochastic decisions (MDP / ADP)

- **Topaloglu & Powell, "A Distributed Decision-Making Structure for Dynamic Resource Allocation Using Nonlinear Functional Approximations," _Operations Research_ 2005, 53(2):281–297.**
  Verified: `pubsonline.informs.org/doi/10.1287/opre.1040.0166`; RePEc `inm/oropre/v53y2005i2p281-297`.
  - **Why it is an exemplar:** attacks a high-dimensional dynamic resource-allocation MDP with separable
    nonlinear value-function approximations and a distributed learning structure — the
    [`ors-theory-development`](../../skills/ors-theory-development/SKILL.md) MDP/ADP path (state, decision,
    value approximation) paired with the [`ors-data-analysis`](../../skills/ors-data-analysis/SKILL.md)
    obligation to show the approximation scales against credible baselines.
  - **Self-check:** is your approximation architecture justified (structure exploited, error/quality
    argued), and is its scaling demonstrated on instances large enough to matter?

### Lagrangian relaxation on a combinatorial structure (network / discrete optimization)

- **Held & Karp, "The Traveling-Salesman Problem and Minimum Spanning Trees," _Operations Research_ 1970, 18(6):1138–1162.**
  Verified: `pubsonline.informs.org/doi/10.1287/opre.18.6.1138`; RePEc `inm/oropre/v18y1970i6p1138-1162`.
  - **Why it is an exemplar:** exposes the **1-tree** structure inside the symmetric TSP and uses
    Lagrangian relaxation / subgradient ascent to produce strong bounds — the canonical
    [`ors-methods`](../../skills/ors-methods/SKILL.md) duality-and-relaxation technique, where finding the
    right combinatorial structure ([`ors-theory-development`](../../skills/ors-theory-development/SKILL.md))
    is what unlocks the bound.
  - **Self-check:** have you found the relaxation/structure that yields a *provably valid bound* and drives
    the algorithm, rather than a heuristic with no certificate?

### Simulation metamodeling with intrinsic + extrinsic uncertainty (simulation)

- **Ankenman, Nelson & Staum, "Stochastic Kriging for Simulation Metamodeling," _Operations Research_ 2010, 58(2):371–382.**
  Verified: `pubsonline.informs.org/doi/10.1287/opre.1090.0754`; RePEc `inm/oropre/v58y2010i2p371-382`.
  - **Why it is an exemplar:** extends kriging to stochastic simulation by separately modeling the
    **intrinsic** noise of each replication and the **extrinsic** uncertainty about the response surface —
    the [`ors-methods`](../../skills/ors-methods/SKILL.md) simulation-output discipline (consistent
    estimator, quantified error) feeding the [`ors-data-analysis`](../../skills/ors-data-analysis/SKILL.md)
    requirement to report variance and replication budgets honestly.
  - **Self-check:** does your simulation method separate sampling noise from model uncertainty and
    quantify both, instead of fitting a deterministic surface to noisy output?

### Distributionally robust / data-driven decisions (optimization under ambiguity)

- **Bertsimas & Sim, "The Price of Robustness," _Operations Research_ 2004, 52(1):35–53.** *(cross-listed
  above)* — read alongside the robust-optimization line as the LP-representable anchor before reaching for
  heavier conic or distributionally robust formulations, so the
  [`ors-literature-positioning`](../../skills/ors-literature-positioning/SKILL.md) delta against it is
  precise.

---

## By topic (each cell is a verified _Operations Research_ paper above)

| Topic (decision problem) | Verified _Operations Research_ exemplar | Year / vol(issue) | Method |
| --- | --- | --- | --- |
| Optimization under uncertainty | Bertsimas & Sim, "The Price of Robustness" | 2004, 52(1) | Tractable (LP-representable) robust optimization |
| Service systems / call centers | Halfin & Whitt, "Heavy-Traffic Limits for Queues with Many Exponential Servers" | 1981, 29(3) | Many-server heavy-traffic / diffusion limit |
| Dynamic resource allocation | Topaloglu & Powell, "A Distributed Decision-Making Structure…" | 2005, 53(2) | Approximate dynamic programming (value-function approximation) |
| Routing / network optimization | Held & Karp, "The Traveling-Salesman Problem and Minimum Spanning Trees" | 1970, 18(6) | Lagrangian relaxation on a 1-tree structure |
| Simulation analysis | Ankenman, Nelson & Staum, "Stochastic Kriging for Simulation Metamodeling" | 2010, 58(2) | Stochastic-kriging metamodel |

---

## Omitted for lack of full verification (do not attribute to _Operations Research_ without re-checking)

To keep the list zero-hallucination, these strong candidates were **excluded** after web-checking — each
is a real, important paper, but **not in _Operations Research_** (the sibling-journal traps the brief
warned of):

- **Ben-Tal & Nemirovski, "Robust Solutions of Uncertain Linear Programs" (1999)** — verified to be in
  **_Operations Research Letters_** 25(1):1–13, **not _Operations Research_**. A foundational robust-LP
  paper whose venue is the *Letters*, a distinct INFORMS-adjacent Elsevier journal.
- **Cachon & Lariviere, "Supply Chain Coordination with Revenue-Sharing Contracts: Strengths and
  Limitations" (2005)** — verified in **_Management Science_** 51(1):30–44 (INFORMS, `inm/ormnsc`,
  DOI `10.1287/mnsc.1040.0215`), **not _Operations Research_**. Same publisher, different journal — the
  `mnsc` stem, not `opre`.
- **Gittins, "Bandit Processes and Dynamic Allocation Indices" (1979)** — verified in the **_Journal of
  the Royal Statistical Society, Series B_** 41(2):148–177, **not _Operations Research_**. The
  index-policy classic underlying much OR scheduling work lives in JRSS-B.
- **Karmarkar, "A New Polynomial-Time Algorithm for Linear Programming" (1984)** — verified in
  **_Combinatorica_** 4:373–395, **not _Operations Research_**. The interior-point breakthrough is a
  *Combinatorica* paper (with an earlier STOC version).

Before adding any new paper to this library, confirm it on `pubsonline.informs.org` with the **`opre`**
DOI stem and the volume/issue (or the RePEc `inm/oropre` record), and update the access-date header.
When in doubt, **omit**.
