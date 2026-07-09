# ISSTA Exemplars Library (contribution shape × technique)

> **Verified via web search, access date 2026-07-09.** Every paper below was checked against the
> **ACM SIGSOFT / ISSTA Impact Paper Award** record and the **ACM Digital Library / dblp** ISSTA
> proceedings to confirm it actually appeared at the **International Symposium on Software Testing
> and Analysis** — matching the ISSTA edition year, author list, and title. Papers that could not
> be cleanly confirmed as ISSTA (as opposed to a sibling venue) were **omitted and documented
> below**. This is deliberately a short, verified list (5 verified > 20 guessed).
>
> **Sibling-confusion guard:** ISSTA is **not** ICSE, FSE/ESEC-FSE, ASE, ICST, OSDI, or PLDI.
> Several famous testing and analysis papers live at those venues, not at ISSTA — a paper being
> about symbolic execution or test generation does **not** make it an ISSTA paper (see omissions).
> Each row below was checked to be an ISSTA edition specifically.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent results, tool numbers, or table figures — read the original in the ACM DL
> before citing anything. For ISSTA-specific policy and the do-not-misattribute list, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **contribution shape × technique** is closest to yours, then study how that
paper puts a **testing-or-analysis contribution the community could reuse** on its first page,
with an **evaluation on real subjects** and **claims tied to measurable evidence** — the ISSTA
bar (see
[`../../skills/issta-writing-style/SKILL.md`](../../skills/issta-writing-style/SKILL.md),
[`../../skills/issta-topic-selection/SKILL.md`](../../skills/issta-topic-selection/SKILL.md), and
[`../../skills/issta-experiments/SKILL.md`](../../skills/issta-experiments/SKILL.md)). For each,
ask the self-check question before claiming your paper is "ISSTA-shaped." Every paper here is an
**ISSTA Impact Paper Award** honoree, so each is also evidence of what the community judges to
have lasted.

---

## By contribution shape

### Reusable benchmark / testing infrastructure

- **Just, Jalali & Ernst, "Defects4J: A Database of Existing Faults to Enable Controlled Testing
  Studies for Java Programs," ISSTA 2014.** (ISSTA Impact Paper Award 2024.)
  - **Why it is an exemplar:** the contribution is a **curated, reproducible fault database** that
    turned "evaluate on some bugs" into "evaluate on *these* bugs, the same way I did" — an
    infrastructure paper that became the shared substrate for a decade of fault-localization and
    program-repair evaluation. The model of an ISSTA contribution whose value is *reuse*.
  - **Self-check:** if your artifact is infrastructure, does it give the community a controlled,
    versioned subject set others can run against without rebuilding it?

### Analysis technique with a new semantic quantity

- **Geldenhuys, Dwyer & Visser, "Probabilistic Symbolic Execution," ISSTA 2012.** (ISSTA Impact
  Paper Award 2022.)
  - **Why it is an exemplar:** extends symbolic execution from "which paths are feasible" to **how
    probable each path is**, adding model-counting over path conditions — a technique contribution
    that opens a new question (quantitative program behaviour) rather than tuning an existing one.
  - **Self-check:** does your analysis compute a genuinely new quantity about program behaviour, or
    a faster version of a quantity the field already had?

### Empirical study that reframes a research area

- **Parnin & Orso, "Are Automated Debugging Techniques Actually Helping Programmers?" ISSTA 2011.**
  (ISSTA Impact Paper Award 2021.)
  - **Why it is an exemplar:** a **human study** that measured whether fault-localization rankings
    help real developers, and reset the field's evaluation assumptions — an ISSTA paper whose
    contribution is *evidence about a methodology*, not a new tool. Pairs with
    `issta-experiments`'s "match evidence to the claim you are actually making."
  - **Self-check:** is your empirical claim about *whether a class of techniques works* backed by a
    study designed to answer that, not by re-running the techniques on more benchmarks?

### Rigorous evaluation of a technique class (program repair)

- **Qi, Long, Achour & Rinard, "An Analysis of Patch Plausibility and Correctness for
  Generate-and-Validate Patch Generation Systems," ISSTA 2015.** (ISSTA Impact Paper Award 2025.)
  - **Why it is an exemplar:** dissects **why generate-and-validate repair produces plausible but
    incorrect patches**, separating passing-the-tests from being-correct — an analysis that made
    "patch correctness" a first-class evaluation concern for the whole repair subfield.
  - **Self-check:** does your evaluation distinguish the metric that is easy to satisfy from the
    property you actually care about, and report the gap?

### Dynamic analysis for a new measurable property

- **Li, Hao, Halfond & Govindan, "Calculating Source Line Level Energy Information for Android
  Applications," ISSTA 2013.** (ISSTA Impact Paper Award 2023.)
  - **Why it is an exemplar:** attributes **energy consumption to source lines** via dynamic
    analysis, bringing a previously coarse, whole-app measurement down to a granularity developers
    can act on — a technique whose worth is in the actionable evidence it produces.
  - **Self-check:** does your analysis report its property at a granularity a developer can use, and
    validate that attribution against ground truth?

---

## By contribution shape (index)

| Contribution shape | Verified ISSTA exemplar | Edition | Technique |
| --- | --- | --- | --- |
| Reusable benchmark / infrastructure | Just, Jalali & Ernst, "Defects4J" | ISSTA 2014 | Curated Java fault database |
| Analysis with a new semantic quantity | Geldenhuys, Dwyer & Visser, "Probabilistic Symbolic Execution" | ISSTA 2012 | Symbolic execution + model counting |
| Empirical study reframing an area | Parnin & Orso, "Are Automated Debugging Techniques Actually Helping Programmers?" | ISSTA 2011 | Controlled human study |
| Rigorous evaluation of a technique class | Qi, Long, Achour & Rinard, "Patch Plausibility and Correctness" | ISSTA 2015 | Program-repair analysis |
| Dynamic analysis for a new property | Li, Hao, Halfond & Govindan, "Source Line Level Energy" | ISSTA 2013 | Dynamic energy attribution |

> Five verified ISSTA Impact-Paper-Award papers across five contribution shapes. Note that two of
> them (Parnin & Orso; Qi et al.) are *evaluation/analysis* papers, not tool papers — a reminder
> that ISSTA rewards evidence about testing and analysis, not only new testing tools.

---

## Omitted for lack of clean ISSTA verification (do not attribute to ISSTA without re-checking)

To keep the list zero-hallucination, the following were **excluded** after checking — several are
exactly the sibling-venue confusions the header warns about. Verify the venue before citing any of
them as ISSTA:

- **Cadar, Dunbar & Engler, "KLEE: Unassisted and Automatic Generation of High-Coverage Tests..."**
  — a landmark symbolic-execution paper, but published at **OSDI 2008** (a systems venue), **not
  ISSTA**. A direct topic trap: symbolic execution does not imply ISSTA.
- **Fraser & Arcuri, "EvoSuite: Automatic Test Suite Generation for Object-Oriented Software"** —
  the canonical EvoSuite paper is at **ESEC/FSE 2011**, **not ISSTA**. Omitted.
- **Pacheco, Lahiri, Ernst & Ball, "Feedback-Directed Random Test Generation" (Randoop)** — a
  foundational test-generation paper, but at **ICSE 2007**, **not ISSTA**. Omitted.
- **AFL / libFuzzer** — hugely influential fuzzers, but tools/technical reports rather than ISSTA
  research-track papers. Omitted.

Before adding any new paper, confirm it on the ACM Digital Library or dblp by matching the **ISSTA
edition and year** (the proceedings volume names "ACM SIGSOFT International Symposium on Software
Testing and Analysis"), then record authors, year, and DOI, and update the access-date header.
When in doubt, omit. If web search is unavailable, add the row as **待核实 / TO VERIFY** with **no
attribution**.
