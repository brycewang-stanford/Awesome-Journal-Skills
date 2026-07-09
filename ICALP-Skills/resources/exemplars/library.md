# ICALP Exemplars Library (track × contribution shape)

> **Verified via web search, access date 2026-07-09.** Every paper below was checked against
> **dblp** (`db/conf/icalp/`), the **DROPS/LIPIcs** ICALP volume listings at Schloss Dagstuhl, and
> the announcing institution's own news page, to confirm it appeared at the **EATCS International
> Colloquium on Automata, Languages, and Programming (ICALP)** — matching title, authors, year, and
> track. Each is an ICALP **Best Paper** or **Best Student Paper** awardee, so the list also models
> what the two program committees reward. Papers that could not be cleanly confirmed as ICALP (as
> opposed to STOC, FOCS, SODA, LICS, or a journal) were **omitted and documented below**. It is
> deliberately a short, verified list (6 verified > 20 guessed).
>
> **Sibling-confusion guard:** ICALP is **not** STOC, **not** FOCS, **not** SODA, and **not** LICS.
> Many canonical TCS results appeared at those venues instead; a famous author or a familiar theorem
> name does **not** prove an ICALP placement. Each row was checked to be an ICALP edition and track
> specifically (see omissions).
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent theorem statements, bounds, or constants — read the original on DROPS/dblp
> before citing anything. For ICALP-specific policy, scope, and the two-track model, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **track × contribution shape** is closest to yours, then study how that paper
states a **precise problem in a clean model**, proves a **theorem whose statement is legible in the
abstract**, and positions its **improvement against the prior bound** — the ICALP bar (see
[`../../skills/icalp-writing-style/SKILL.md`](../../skills/icalp-writing-style/SKILL.md),
[`../../skills/icalp-topic-selection/SKILL.md`](../../skills/icalp-topic-selection/SKILL.md), and
[`../../skills/icalp-experiments/SKILL.md`](../../skills/icalp-experiments/SKILL.md)). For each, ask
the self-check question before claiming your paper is "ICALP-shaped."

ICALP splits into **Track A (Algorithms, Complexity and Games)** and **Track B (Automata, Logic,
Semantics and Theory of Programming)**. The exemplars are grouped by track so the routing decision in
`icalp-topic-selection` stays concrete.

---

## Track A — Algorithms, Complexity and Games

### Approximation algorithm — network design

- **Bosch-Calvo, Grandoni & Jabal Ameli, "A 4/3 Approximation for 2-Vertex-Connectivity,"
  ICALP 2023 (Track A Best Paper).** Verified: ICALP 2023 awards page (`icalp2023.cs.upb.de/awards`)
  and IDSIA/USI news; dblp/DROPS `LIPIcs.ICALP.2023`.
  - **Why it is an exemplar:** it improves a *named approximation ratio* for a classic network-design
    problem — the archetypal Track A contribution, where the headline is a better provable constant
    and the technique (a structured local-improvement argument) is the payoff.
  - **Self-check:** is your result a provable improvement on a stated bound for a problem the
    community already tracks, rather than a heuristic evaluated empirically?

### Parallel / sublinear algorithms — combinatorial optimization

- **Blikstad, "Sublinear-round Parallel Matroid Intersection," ICALP 2022 (Track A Best Student
  Paper).** Verified: ICALP 2022 awards; dblp/DROPS `LIPIcs.ICALP.2022`.
  - **Why it is an exemplar:** it advances the **round complexity** of a fundamental problem in a
    clean model of parallel computation — a single, crisp complexity-measure improvement, the kind of
    result Track A student awards reward.
  - **Self-check:** does your paper move a well-defined complexity measure (rounds, queries, time) in
    a standard model, with the model fixed before the theorem?

### Complexity — lower bounds

- **Bun & Thaler, "Dual Lower Bounds for Approximate Degree and Markov-Bernstein Inequalities,"
  ICALP 2013 (Track A Best Paper).** Verified: Harvard Privacy Tools news; dblp ICALP 2013.
  - **Why it is an exemplar:** a **lower-bound** contribution — proving a limitation via a dual
    witness — showing Track A is as much about hardness/impossibility as about faster algorithms.
  - **Self-check:** if your contribution is a lower bound, is the model and the complexity measure
    stated precisely enough that the bound is unambiguous and comparable to prior work?

### Randomized algorithms — approximate counting

- **Guo & Jerrum, "A Polynomial-Time Approximation Algorithm for All-Terminal Network Reliability,"
  ICALP 2018 (Best Paper).** Verified: Edinburgh LFCS and Kiel Dependable Systems news; dblp ICALP
  2018.
  - **Why it is an exemplar:** it resolves the tractability of a long-standing **approximate counting**
    question with an FPRAS — a result whose significance is legible from one sentence, and whose method
    (a novel sampling argument) travels.
  - **Self-check:** does your abstract let a non-specialist see *what* became tractable and *by how
    much*, without reading the proof?

---

## Track B — Automata, Logic, Semantics and Theory of Programming

### Logic + complexity — decision procedures

- **Chistikov, Mansutti & Starchak, "Integer Linear-Exponential Programming in NP by Quantifier
  Elimination," ICALP 2024 (Track B Best Paper).** Verified: IMDEA Software and Warwick DCS news;
  dblp/DROPS `LIPIcs.ICALP.2024`.
  - **Why it is an exemplar:** it pins the **complexity of a logical theory** via quantifier
    elimination — the signature Track B move, where the contribution is the exact complexity of
    deciding a formalism, not an algorithm's runtime on data.
  - **Self-check:** is your result about the decidability/complexity of a logic, language, or calculus,
    with the fragment defined precisely?

### Automata / verification — infinite-state systems

- **Künnemann, Mazowiecki, Schütze, Sinclair-Banks & Węgrzycki, "Coverability in VASS Revisited:
  Improving Rackoff's Bound to Obtain Conditional Optimality," ICALP 2023 (Track B Best Paper).**
  Verified: ICALP 2023 awards page; DROPS `LIPIcs.ICALP.2023.131`.
  - **Why it is an exemplar:** it sharpens a classical bound (Rackoff's) for **coverability in vector
    addition systems** and ties it to a conditional lower bound — Track B verification theory at its
    center, uniting an upper and a matching conditional bound.
  - **Self-check:** does your paper close, or conditionally close, a gap for a well-studied model of
    computation (Petri nets/VASS, pushdown, timed systems)?

### Automata / databases — regular languages under updates

- **Amarilli, Jachiet & Paperman, "Dynamic Membership for Regular Languages," ICALP 2021 (Track B
  Best Paper).** Verified: dblp/DROPS `LIPIcs.ICALP.2021`; ICALP 2021 report (EATCS bulletin).
  - **Why it is an exemplar:** it gives a **fine-grained classification** of how hard membership stays
    under updates, keyed to the algebraic structure of the language — the Track B taste for a complete
    dichotomy/characterization rather than a single data point.
  - **Self-check:** does your result classify an entire family (a dichotomy, a trichotomy, a complete
    characterization) rather than settling one instance?

---

## Track ↔ exemplar (verified rows)

| Track | Contribution shape | Verified ICALP exemplar | Edition |
| --- | --- | --- | --- |
| A | Approximation ratio | Bosch-Calvo, Grandoni & Jabal Ameli, "4/3 for 2-Vertex-Connectivity" | 2023 |
| A | Round/complexity measure | Blikstad, "Sublinear-round Parallel Matroid Intersection" | 2022 |
| A | Lower bound | Bun & Thaler, "Dual Lower Bounds for Approximate Degree..." | 2013 |
| A | Approximate counting (FPRAS) | Guo & Jerrum, "...All-Terminal Network Reliability" | 2018 |
| B | Logic decision complexity | Chistikov, Mansutti & Starchak, "Integer Linear-Exponential Programming..." | 2024 |
| B | Infinite-state verification | Künnemann et al., "Coverability in VASS Revisited" | 2023 |
| B | Regular-language classification | Amarilli, Jachiet & Paperman, "Dynamic Membership for Regular Languages" | 2021 |

> Seven verified papers across the two tracks and seven contribution shapes. The Track A rows show
> the venue's range from faster algorithms to hardness; the Track B rows show its range from logic to
> automata to language theory.

---

## Omitted for lack of clean ICALP verification (do not attribute to ICALP without re-checking)

To keep the list zero-hallucination, several famous TCS results were **excluded** after checking —
some are exactly the sibling-venue confusions the header warns about:

- **The PCP theorem (Arora-Safra; Arora-Lund-Motwani-Sudan-Szegedy)** — the founding papers are
  **FOCS 1992**, not ICALP. A classic sibling-venue trap.
- **"PRIMES is in P" (Agrawal-Kayal-Saxena)** — published in the *Annals of Mathematics* (a journal),
  not ICALP. Omitted.
- **Smoothed analysis of the simplex method (Spielman-Teng)** — **STOC 2001** / *JACM*, not ICALP.
- **Reingold, "Undirected connectivity in log-space"** — **STOC 2005** / *JACM*, not ICALP.

Before adding any paper, confirm it on **dblp** and **DROPS/LIPIcs** by matching the venue string to
an ICALP edition **and** the correct track (not STOC, FOCS, SODA, LICS, or a journal), then record
authors, year, and the DROPS DOI, and update the access-date header. When in doubt, omit. If web
search is unavailable, add the row as **待核实 / TO VERIFY** with **no attribution**.
