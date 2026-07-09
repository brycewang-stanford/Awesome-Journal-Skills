# ASE Exemplars Library (contribution shape × automated-SE method)

> **Verified via web search, access date 2026-07-09.** Every paper below was checked against
> **dblp** (the ASE proceedings live under the historical series key `conf/kbse`, from the
> conference's original name *Knowledge-Based Software Engineering*) and the **ACM Digital
> Library / IEEE Xplore** to confirm it appeared at the **IEEE/ACM International Conference on
> Automated Software Engineering (ASE)** — matching title, authors, year, and venue string. Papers
> that could not be cleanly confirmed as ASE (as opposed to ICSE, ESEC/FSE, ISSTA, or PLDI) were
> **omitted and documented below**. It is deliberately a short, verified list (5 verified > 15
> guessed).
>
> **Sibling-confusion guard:** ASE is **not** ICSE, **not** ESEC/FSE, **not** ISSTA, and **not** a
> PL venue. Several canonical SE tools were introduced at those venues instead; a famous author or
> a familiar tool name does **not** prove ASE. Each row was checked to be an ASE edition
> specifically (see omissions). Acronym trap: "ASE" is also the Association for Science Education
> and the Association for Surgical Education — neither is this venue.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent results, effect sizes, or table numbers — read the original on ACM DL / IEEE
> Xplore before citing anything. For ASE-specific policy, scope, and the review model, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **contribution shape × automated-SE method** is closest to yours, then study how
that paper (1) **automates a software-engineering task a practitioner recognizes**, (2) **embodies
the idea in something runnable** (a tool, an analysis, a monitor), and (3) **evaluates it on real
subjects** against a credible baseline — the ASE bar (see
[`../../skills/ase-writing-style/SKILL.md`](../../skills/ase-writing-style/SKILL.md),
[`../../skills/ase-topic-selection/SKILL.md`](../../skills/ase-topic-selection/SKILL.md), and
[`../../skills/ase-experiments/SKILL.md`](../../skills/ase-experiments/SKILL.md)). For each, ask the
self-check question before claiming your paper is "ASE-shaped."

Several rows are ASE **Most Influential Paper** honorees, so they also model what "automation that
still matters a decade-plus later" looks like at this venue.

---

## By contribution shape

### Technique + tool — runtime verification / monitoring

- **Havelund & Roşu, "Monitoring Programs Using Rewriting," ASE 2001, pp. 135-143.**
  Verified: dblp `conf/kbse` (ASE'01, Coronado Island/San Diego, CA). ASE Most Influential Paper;
  widely credited with helping launch the **runtime verification** field.
  - **Why it is an exemplar:** it *automates* the checking of program executions against formal
    specifications by rewriting — a mechanism others could adopt, not a one-off result. The problem
    (does this run satisfy its properties?) is legible to practitioners and the method generalizes.
  - **Self-check:** does your technique automate a checking/analysis task, embodied in a monitor or
    tool a third party could run on their own programs?

### Technique + tool — specification-based test generation

- **Khurshid & Marinov, "TestEra: A Novel Framework for Automated Testing of Java Programs,"
  ASE 2001, pp. 22-31.** Verified: dblp `conf/kbse` (ASE 2001) / ACM DL. ASE Most Influential Paper
  (awarded 2015).
  - **Why it is an exemplar:** a named framework that **automatically generates test inputs** from
    specifications for real Java programs — the classic ASE "automation you can run." The
    contribution is a mechanism others reuse, evaluated on real code rather than toy inputs.
  - **Self-check:** is your technique embodied in a tool that automates a testing/analysis task on
    real subjects, with the automation (not a hand-tuned example) as the contribution?

### Empirical evaluation of a technique — fault localization

- **Jones & Harrold, "Empirical Evaluation of the Tarantula Automatic Fault-Localization
  Technique," ASE 2005, pp. 273-282.** Verified: dblp `conf/kbse` (ASE 2005) / ACM DL. A founding
  study of coverage-based (spectrum) fault localization.
  - **Why it is an exemplar:** it pairs an *automatic* localization technique with a **disciplined
    empirical evaluation** — comparing against alternatives on real faulty programs with a defined
    effectiveness measure. Automation plus honest measurement, the ASE twin virtues.
  - **Self-check:** does your paper evaluate an automated technique against credible alternatives on
    real subjects, with an effectiveness metric a reviewer could scrutinize and reproduce?

### Technique — automated program comprehension / documentation

- **Sridhara, Hill, Muppaneni, Pollock & Vijay-Shanker, "Towards Automatically Generating Summary
  Comments for Java Methods," ASE 2010, pp. 43-52** (DOI 10.1145/1858996.1859006). Verified: ACM DL
  / dblp `conf/kbse`. ASE Most Influential Paper (awarded 2022).
  - **Why it is an exemplar:** it automates a **comprehension/maintenance** task — synthesizing
    natural-language summaries from code structure — and evaluates the output with human judgments.
    An automated-SE contribution centered on a task developers do daily, not a model for its own
    sake.
  - **Self-check:** does your automation target a comprehension/maintenance task, with an evaluation
    that measures whether the *output* helps, not just that a pipeline ran?

### Learning-based technique — deep learning for code

- **White, Tufano, Vendome & Poshyvanyk, "Deep Learning Code Fragments for Code Clone Detection,"
  ASE 2016, pp. 87-98.** Verified: dblp `conf/kbse/WhiteTVP16`. An early, disciplined "deep
  learning for code" contribution (learned lexical + AST representations for clone detection);
  later an ASE Most Influential Paper honoree.
  - **Why it is an exemplar:** it frames an **SE task (clone detection)** as the point and uses
    learned code representations as the means, evaluated on real code — the model-swap test passes
    because the SE lesson (learned representations improve clone detection) survives the specific
    architecture.
  - **Self-check:** if the network were swapped, would the software-engineering lesson survive — or
    is the model the whole paper (an `ase-topic-selection` re-route signal toward an ML venue)?

---

## Contribution-shape ↔ exemplar (verified rows)

| Contribution shape | Verified ASE exemplar | Edition | Automated-SE method |
| --- | --- | --- | --- |
| Technique + tool (monitoring) | Havelund & Roşu, "Monitoring Programs Using Rewriting" | ASE 2001 | Runtime verification by rewriting |
| Technique + tool (testing) | Khurshid & Marinov, "TestEra" | ASE 2001 | Specification-based test generation |
| Empirical evaluation | Jones & Harrold, "...Tarantula..." | ASE 2005 | Spectrum-based fault localization |
| Technique (comprehension) | Sridhara et al., "...Summary Comments for Java Methods" | ASE 2010 | NL summarization from code |
| Learning-based technique | White, Tufano, Vendome & Poshyvanyk, "Deep Learning Code Fragments..." | ASE 2016 | DL code representations |

> Five verified papers across five contribution shapes, all quintessentially *automated* SE:
> monitoring, test generation, fault localization, comprehension, and learned code models. Four are
> ASE Most Influential Paper honorees.

---

## Omitted for lack of clean ASE verification (do not attribute to ASE without re-checking)

To keep the list zero-hallucination, the following were **excluded** after checking — several are
exactly the sibling-venue confusions the header warns about:

- **"CUTE: A Concolic Unit Testing Engine for C" (Sen, Marinov & Agha)** — verified **ESEC/FSE
  2005**, *not* ASE, despite sharing an author (Marinov) with TestEra. A direct sibling trap.
- **"DART: Directed Automated Random Testing" (Godefroid, Klarlund & Sen)** — **PLDI 2005**, a PL
  venue, not ASE. Omitted.
- **"Feedback-directed Random Test Generation" (Randoop; Pacheco et al.)** — **ICSE 2007**, not
  ASE. Omitted.
- **"EvoSuite: Automatic Test Suite Generation for Object-Oriented Software" (Fraser & Arcuri)** —
  **ESEC/FSE 2011**, not ASE. Omitted (its tool-demo and later papers appear at various venues;
  verify each edition string before attributing).
- **Automated program repair founding work (GenProg line)** — its ICSE/GECCO origins are *not* ASE
  placements; omitted to avoid venue misattribution.

Before adding any paper, confirm it on **dblp** (`conf/kbse` for ASE) and **ACM DL / IEEE Xplore**
by matching the venue string to an ASE edition (not ICSE, FSE, ISSTA, or a PL venue), then record
authors, year, and DOI/pages, and update the access-date header. When in doubt, omit. If web search
is unavailable, add the row as **待核实 / TO VERIFY** with **no attribution**.
