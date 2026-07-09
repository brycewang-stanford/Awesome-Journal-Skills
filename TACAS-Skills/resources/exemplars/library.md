# TACAS Exemplars Library (category × contribution)

> **Verified via web search, access date 2026-07-09.** Every paper below was checked against
> **dblp** and the **Springer LNCS** landing pages to confirm it appeared at **TACAS — the
> International Conference on Tools and Algorithms for the Construction and Analysis of Systems**
> (an ETAPS conference) — matching title, authors, year, and the LNCS volume. Papers that could not
> be cleanly confirmed as **TACAS** (as opposed to CAV, VMCAI, FMCAD, SPIN, or a journal) were
> **omitted and documented below**. It is deliberately a short, verified list (few verified >
> many guessed).
>
> **Sibling-confusion guard:** TACAS is **not** CAV, **not** VMCAI, **not** FMCAD, and **not** SPIN.
> Several canonical verification tools were introduced at those venues instead; a famous author or a
> familiar tool name does **not** prove TACAS. Each row was checked to be a TACAS edition
> specifically (see omissions), because CAV is TACAS's closest sibling and the easiest misattribution.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent results, benchmark numbers, or DOIs — confirm the LNCS volume and DOI on
> Springer before citing anything. For TACAS-specific policy, categories, and the artifact/badge
> model, see [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

TACAS has **four paper categories** (research, case-study, regular tool, tool-demonstration), so
pick the row whose **category × contribution** is closest to yours, then study how that paper
states a **construction-or-analysis problem for systems**, delivers a **sound algorithm or a
runnable tool**, and backs it with **honest, reproducible evidence** — the TACAS bar (see
[`../../skills/tacas-writing-style/SKILL.md`](../../skills/tacas-writing-style/SKILL.md),
[`../../skills/tacas-topic-selection/SKILL.md`](../../skills/tacas-topic-selection/SKILL.md), and
[`../../skills/tacas-experiments/SKILL.md`](../../skills/tacas-experiments/SKILL.md)). For each, ask
the self-check question before claiming your paper is "TACAS-shaped."

---

## By category × contribution

### Foundational research paper — algorithm that redefined a field

- **Biere, Cimatti, Clarke & Zhu, "Symbolic Model Checking without BDDs," TACAS 1999** (LNCS 1579).
  Verified: dblp `db/conf/tacas/tacas1999.html`. Introduced **Bounded Model Checking (BMC)** —
  reducing model checking to propositional satisfiability so that SAT solvers, not BDDs, carry the
  search.
  - **Why it is an exemplar:** it is a **research** contribution — a new algorithmic reduction with
    a correctness argument — that reshaped how the community verifies systems, and it is legible to
    any tool builder. Its influence a decade-plus later is exactly what a foundational TACAS paper
    aspires to.
  - **Self-check:** is your core an *algorithm or reduction* with a soundness argument that others
    will build tools on, rather than an engineering datapoint on one system?

### Regular tool paper — a verifier others point at their own code

- **Clarke, Kroening & Lerda, "A Tool for Checking ANSI-C Programs" (CBMC), TACAS 2004** (LNCS 2988).
  Verified: dblp / Springer LNCS. Presented **CBMC**, a bounded model checker for C that became a
  reference implementation for the technique.
  - **Why it is an exemplar:** it is the archetypal TACAS **regular tool** paper — a named,
    downloadable tool that realizes an algorithm on **real C programs**, described so a third party
    can run it. This is the "tool + artifact" identity that distinguishes TACAS from purely
    theoretical verification venues.
  - **Self-check:** could a reviewer install your tool from the (now mandatory) artifact and run it
    on their own inputs, and does the paper describe the tool, not just the idea behind it?

### Regular tool paper — infrastructure the whole field reuses

- **de Moura & Bjørner, "Z3: An Efficient SMT Solver," TACAS 2008** (LNCS 4963). Verified: dblp /
  Springer LNCS. Presented **Z3**, an SMT solver that became core infrastructure across verification.
  - **Why it is an exemplar:** a **tool** whose contribution is measured by adoption — its value is
    that other tools stand on it. It models the TACAS virtue that a solid, reusable tool with an
    honest evaluation is a first-class contribution, not a second-class one.
  - **Self-check:** does your tool give the community a component it will reuse, with an evaluation
    that compares fairly against the strongest existing solvers/checkers on standard benchmarks?

### Regular tool paper — a model-checking platform with a benchmark story

- **Kant, Laarman, Blom, van de Pol, van Dijk & Meijer, "LTSmin: High-Performance,
  Language-Independent Model Checking," TACAS 2015** (LNCS 9035). Verified via dblp / Springer LNCS
  (confirm the DOI before citing).
  - **Why it is an exemplar:** it presents a **tool** as a language-independent platform and backs
    it with performance evidence on shared benchmarks — the kind of measured, reproducible tool
    contribution the TACAS artifact process is built to reward.
  - **Self-check:** is your tool evaluated on **community benchmarks** with runtime/scalability
    reported honestly, so the comparison would survive an SV-COMP-style scrutiny?

---

## Category ↔ exemplar (verified rows)

| Category | Verified TACAS exemplar | Edition | Contribution |
| --- | --- | --- | --- |
| Research (foundational) | Biere, Cimatti, Clarke & Zhu, "Symbolic Model Checking without BDDs" | TACAS 1999 | Bounded Model Checking |
| Regular tool | Clarke, Kroening & Lerda, "A Tool for Checking ANSI-C Programs" (CBMC) | TACAS 2004 | Bounded model checker for C |
| Regular tool | de Moura & Bjørner, "Z3: An Efficient SMT Solver" | TACAS 2008 | SMT solver / reusable infrastructure |
| Regular tool | Kant et al., "LTSmin: ...Language-Independent Model Checking" | TACAS 2015 | Model-checking platform |

> **Case-study and tool-demonstration exemplars:** these categories are prized at TACAS but their
> canonical instances are edition-specific rather than field-defining single names. Draw a
> case-study or tool-demo exemplar from the **current TACAS proceedings on Springer LNCS** and
> verify it on dblp before using it, rather than attributing one from memory (**待核实**).

---

## Omitted for lack of clean TACAS verification (do not attribute to TACAS without re-checking)

To keep the list zero-hallucination, the following were **excluded** after checking — several are
exactly the CAV/sibling confusions the header warns about:

- **NuSMV ("NuSMV 2: An OpenSource Tool for Symbolic Model Checking," Cimatti et al.)** — a **CAV
  2002** tool paper, *not* TACAS. A direct sibling-venue trap given the shared authors and topic.
- **CPAchecker ("A Tool for Configurable Software Verification," Beyer & Keremoglu)** — **CAV 2011**,
  not TACAS, despite being central to software verification and SV-COMP. Omitted.
- **SLAM / BLAST software model checkers** — their founding tool papers are **CAV**-lineage, not
  TACAS placements; omitted to avoid venue misattribution.
- **Storm probabilistic model checker ("A Storm is Coming")** — **CAV 2017**, not TACAS. Omitted.
- **KLEE symbolic execution engine** — **OSDI 2008**, a systems venue, not TACAS. Omitted.

Before adding any paper, confirm it on **dblp** and **Springer LNCS** by matching the venue string
to a **TACAS** edition (not CAV, VMCAI, FMCAD, SPIN, or a journal), then record authors, year, and
the LNCS volume/DOI, and update the access-date header. When in doubt, omit. If web search is
unavailable, add the row as **待核实 / TO VERIFY** with **no attribution**.
