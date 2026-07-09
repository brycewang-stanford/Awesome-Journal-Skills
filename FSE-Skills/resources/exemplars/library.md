# ESEC/FSE Exemplars Library (contribution shape × method)

> **Verified via web search, access date 2026-07-09.** Every paper below was checked against
> **dblp** and the **ACM Digital Library** to confirm it appeared at the **ACM (SIGSOFT)
> International Symposium/Conference on the Foundations of Software Engineering (FSE / ESEC/FSE)**
> — matching title, author list, year, and venue string. Papers that could not be cleanly
> confirmed as FSE (as opposed to ICSE, ASE, ISSTA, PLDI, or a journal) were **omitted and
> documented below**. It is deliberately a short, verified list (5 verified > 15 guessed).
>
> **Sibling-confusion guard:** FSE is **not** ICSE, **not** ASE, **not** ISSTA, and **not** a PL
> venue. Several canonical SE tools were introduced at those venues instead; a famous author or a
> familiar tool name does **not** prove FSE. Each row was checked to be an FSE/ESEC-FSE edition
> specifically (see omissions).
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does
> not reproduce or invent results, effect sizes, or table numbers — read the original on ACM DL
> before citing anything. For FSE-specific policy, scope, and the cycle model, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **contribution shape × method** is closest to yours, then study how that
paper states a **software-engineering problem practitioners recognize**, backs it with
**evidence proportional to the claim**, and names its **threats to validity** — the FSE bar (see
[`../../skills/fse-writing-style/SKILL.md`](../../skills/fse-writing-style/SKILL.md),
[`../../skills/fse-topic-selection/SKILL.md`](../../skills/fse-topic-selection/SKILL.md), and
[`../../skills/fse-experiments/SKILL.md`](../../skills/fse-experiments/SKILL.md)). For each, ask
the self-check question before claiming your paper is "FSE-shaped."

Several rows are ESEC/FSE **Test of Time** or SIGSOFT **Distinguished Paper** honorees, so they
also model what "influence a decade later" looks like at this venue.

---

## By contribution shape

### Technique + empirical method — automated debugging

- **Zeller, "Yesterday, my Program Worked. Today, it Does Not. Why?", ESEC/FSE 1999.**
  Verified: dblp `db/conf/esec/esec99.html`. Introduced **delta debugging** — automatically
  narrowing a large set of changes to a minimal failure-inducing subset.
  - **Why it is an exemplar:** it turns a universal developer experience ("it broke and I don't
    know why") into a **general, automatable algorithm** with a crisp minimality guarantee, then
    demonstrates it on real failures. The problem is instantly legible to practitioners and the
    contribution travels beyond any one program.
  - **Self-check:** does your technique solve a problem a working developer would name unprompted,
    and is the method general rather than tied to one system?

### Technique + tool — automated test generation

- **Sen, Marinov & Agha, "CUTE: A Concolic Unit Testing Engine for C," ESEC/FSE 2005.**
  Verified: dblp `rec/conf/sigsoft/SenMA05.html`. ACM SIGSOFT Distinguished Paper; later an
  ESEC/FSE Impact Paper honoree. Introduced **concolic testing** (concrete + symbolic execution)
  for real C programs with pointers.
  - **Why it is an exemplar:** a named technique delivered as a **usable tool** and evaluated on
    real code — the classic FSE "idea you can run." The contribution is a mechanism others adopt,
    not a one-off result.
  - **Self-check:** is your technique embodied in a tool a third party could point at their own
    programs, and does the evaluation use real subjects rather than toy inputs?

### Empirical study — regression testing / flaky tests

- **Luo, Hariri, Eloussi & Marinov, "An Empirical Analysis of Flaky Tests," FSE 2014,
  pp. 643-653** (DOI 10.1145/2635868.2635920). Verified: ACM DL / dblp. The first extensive study
  of non-deterministic test outcomes.
  - **Why it is an exemplar:** it names and *characterizes* a phenomenon practitioners feel but
    had not measured — building a taxonomy of flakiness causes from real projects. Pure empirical
    insight that reshaped a research area.
  - **Self-check:** does your study change what the community believes about real practice, with a
    dataset and coding methodology a reviewer could scrutinize?

### Empirical methodology — validity of a research instrument

- **Just, Jalali, Inozemtseva, Ernst, Holmes & Fraser, "Are Mutants a Valid Substitute for Real
  Faults in Software Testing?", FSE 2014, pp. 654-665** (DOI 10.1145/2635868.2635929). Verified:
  ACM DL / dblp; SIGSOFT Distinguished Paper.
  - **Why it is an exemplar:** it interrogates a **method the field relies on** (mutation as a
    proxy for real faults) and reports a statistically grounded answer, controlling for coverage.
    The contribution improves how everyone else evaluates, not one tool's score.
  - **Self-check:** does your paper strengthen or question a widely used measurement, with an
    analysis whose statistics and confounds are laid out explicitly?

### Learning-based technique — naturalness of code

- **Allamanis, Barr, Bird & Sutton, "Suggesting Accurate Method and Class Names," ESEC/FSE 2015.**
  Verified: ACM DL / dblp; ESEC/FSE Test of Time honoree.
  - **Why it is an exemplar:** it frames **identifier naming** as a learnable regularity in large
    code corpora and evaluates the suggestions on real projects — an early, disciplined "ML for
    code" contribution with an SE question at its center rather than a model as the point.
  - **Self-check:** if the model were swapped for another, would the software-engineering lesson
    survive — or is the model the whole paper (an `fse-topic-selection` re-route signal)?

---

## Contribution-shape ↔ exemplar (verified rows)

| Contribution shape | Verified FSE exemplar | Edition | Method |
| --- | --- | --- | --- |
| Technique + empirical method | Zeller, "Yesterday, my Program Worked..." | ESEC/FSE 1999 | Delta debugging |
| Technique + tool | Sen, Marinov & Agha, "CUTE" | ESEC/FSE 2005 | Concolic testing |
| Empirical study | Luo, Hariri, Eloussi & Marinov, "Flaky Tests" | FSE 2014 | Mining + taxonomy |
| Empirical methodology | Just et al., "Are Mutants a Valid Substitute...?" | FSE 2014 | Controlled study |
| Learning-based technique | Allamanis, Barr, Bird & Sutton, "...Method and Class Names" | ESEC/FSE 2015 | ML for code |

> Five verified papers across five contribution shapes. The two FSE 2014 rows also show the
> venue's twin empirical modes — *discovering* a phenomenon (flaky tests) and *validating an
> instrument* (mutants) — both prized here.

---

## Omitted for lack of clean FSE verification (do not attribute to FSE without re-checking)

To keep the list zero-hallucination, the following were **excluded** after checking — several are
exactly the sibling-venue confusions the header warns about:

- **"DART: Directed Automated Random Testing" (Godefroid, Klarlund & Sen)** — verified to be
  **PLDI 2005**, *not* FSE, despite being concolic testing's other founding paper and sharing an
  author with CUTE. A direct sibling-venue trap; listed only as a guardrail.
- **"Feedback-directed Random Test Generation" (Randoop; Pacheco et al.)** — **ICSE 2007**, not
  FSE. Omitted.
- **Automated program repair founding paper (GenProg line)** — the field's ICSE/GECCO origins are
  *not* FSE placements; omitted to avoid venue misattribution.
- **Delta-debugging journal version, "Simplifying and Isolating Failure-Inducing Input"** — the
  extended treatment appeared in **IEEE TSE (2002)**, a journal, not FSE; cite the ESEC/FSE 1999
  paper for the FSE attribution and the TSE article separately.

Before adding any paper, confirm it on **dblp** and **ACM DL** by matching the venue string to an
FSE / ESEC/FSE edition (not ICSE, ASE, ISSTA, or a PL venue), then record authors, year, and
DOI/pages, and update the access-date header. When in doubt, omit. If web search is unavailable,
add the row as **待核实 / TO VERIFY** with **no attribution**.
