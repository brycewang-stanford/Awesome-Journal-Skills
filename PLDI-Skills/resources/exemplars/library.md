# PLDI Exemplars Library (contribution type x era)

> **Verified via web search, access date 2026-07-08.** Every row below was checked
> against dblp conference records and the ACM Digital Library to confirm the paper
> really appeared at **PLDI** (or, for the PACMPL era, in **PACMPL Issue PLDI**),
> with author list, year, and pages/article number matching. Anything that could not
> be pinned to PLDI specifically was omitted and documented at the bottom. Five
> verified rows beat fifteen plausible guesses.
>
> **Sibling-confusion guard:** the SIGPLAN family shares people, topics, and — since
> 2023 — even a journal (PACMPL). POPL, OOPSLA, ICFP, ASPLOS, CGO, and OSDI papers
> are routinely misremembered as "PLDI papers." A PACMPL citation alone does **not**
> prove PLDI: PACMPL Vol 7 contains POPL, PLDI, ICFP, *and* OOPSLA issues — the
> issue name is the discriminator. Check `Issue PLDI` explicitly.
>
> **Zero-hallucination rule:** this file records positioning only. Speedups, bug
> counts, and benchmark figures live in the original papers — reread them on the
> ACM DL before quoting any number. Policy facts live in
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Find the row whose contribution type matches your draft, then study how that paper
earns the PLDI bar: a language, compiler, analysis, or runtime idea made concrete in
a working implementation, evaluated on benchmarks a skeptical implementor would
accept (see [`../../skills/pldi-writing-style/SKILL.md`](../../skills/pldi-writing-style/SKILL.md),
[`../../skills/pldi-experiments/SKILL.md`](../../skills/pldi-experiments/SKILL.md), and
[`../../skills/pldi-topic-selection/SKILL.md`](../../skills/pldi-topic-selection/SKILL.md)).
Each row ends with the self-check question to ask of your own paper.

## Verified exemplars

### Dynamic test generation (testing / symbolic execution)

- **Godefroid, Klarlund & Sen, "DART: Directed Automated Random Testing," PLDI 2005,
  pp. 213-223.** Verified: dblp `conf/pldi/pldi2005` (Chicago, IL).
  - **Why it is an exemplar:** takes an idea with deep semantic roots (concolic
    execution) and delivers it as an automated tool applied to real C interfaces —
    the classic PLDI move of turning a semantics insight into a testing engine.
  - **Self-check:** does your technique run on programs you did not write, without
    per-program manual setup?

### Dynamic binary instrumentation (runtimes / tooling)

- **Nethercote & Seward, "Valgrind: A Framework for Heavyweight Dynamic Binary
  Instrumentation," PLDI 2007, pp. 89-100.** Verified: dblp
  `conf/pldi/pldi2007` (San Diego, CA); DOI 10.1145/1250734.1250746; later won the
  Most Influential PLDI Paper award (2017).
  - **Why it is an exemplar:** explains the *design space* (shadow values,
    heavyweight instrumentation) rather than just the tool, so the paper outlived
    its own implementation details — infrastructure framed as research.
  - **Self-check:** if someone rebuilt your system from scratch, does your paper
    tell them which design decisions matter and why?

### Compiler testing at scale (empirical / tools)

- **Yang, Chen, Eide & Regehr, "Finding and Understanding Bugs in C Compilers,"
  PLDI 2011, pp. 283-294.** Verified: dblp `conf/pldi/YangCER11`; ACM DL DOI
  10.1145/1993498.1993532.
  - **Why it is an exemplar:** pairs a generator (Csmith) with a multi-year
    empirical campaign against production compilers, and spends real page count on
    *understanding* the bugs found — evidence depth PLDI reviewers reward over a
    raw bug tally.
  - **Self-check:** does your evaluation explain *why* the technique works, not
    only that counters went up?

### Domain-specific language + optimizing compiler (design / performance)

- **Ragan-Kelley, Barnes, Adams, Paris, Durand & Amarasinghe, "Halide: A Language
  and Compiler for Optimizing Parallelism, Locality, and Recomputation in Image
  Processing Pipelines," PLDI 2013, pp. 519-530.** Verified: dblp
  `conf/pldi/Ragan-KelleyBAPDA13` (Seattle, WA). Note: the related "Decoupling
  algorithms from schedules" paper is ACM TOG 2012, a different publication.
  - **Why it is an exemplar:** names a trade-off space (parallelism, locality,
    recomputation), gives it a language-level representation (schedules), and
    proves the design with cross-architecture performance — design insight and
    benchmark rigor in one arc.
  - **Self-check:** can you state the trade-off space your language or IR exposes,
    independent of your benchmark numbers?

### Proof engineering in the PACMPL era (verification / synthesis)

- **Gopinathan, Keoliya & Sergey, "Mostly Automated Proof Repair for Verified
  Libraries," PACMPL Vol 7, Issue PLDI, Article 107 (2023), DOI 10.1145/3591221.**
  Verified: ACM DL; SIGPLAN Distinguished Paper at PLDI 2023; artifact (Sisyphus)
  archived on Zenodo.
  - **Why it is an exemplar:** shows the modern full package — a journal-formatted
    PACMPL article, a distinguished-paper-level contribution, and a Zenodo-archived
    artifact — i.e., what "PLDI accepted" means structurally since 2023.
  - **Self-check:** is your artifact planned as a citable, DOI-stamped object
    rather than a repository link that may rot?

---

## Quick index (era x contribution type)

| Era | Paper | Where verified | Contribution type |
| --- | --- | --- | --- |
| Classic proceedings | DART (2005, pp. 213-223) | dblp pldi2005 | Automated testing technique |
| Classic proceedings | Valgrind (2007, pp. 89-100) | dblp pldi2007 + ACM DL | Instrumentation framework |
| Classic proceedings | Csmith (2011, pp. 283-294) | dblp + ACM DL | Empirical compiler testing |
| Classic proceedings | Halide (2013, pp. 519-530) | dblp pldi2013 | DSL + optimizing compiler |
| PACMPL Issue PLDI | Proof Repair / Sisyphus (2023, Art. 107) | ACM DL 10.1145/3591221 | Verification tooling |

The pre-2023 rows cite conference proceedings pages; the 2023 row cites a PACMPL
article number. Cite each era in its own native form — mixing them is the most
common PLDI bibliography error since the PACMPL switch.

---

## Omitted after checking (do not attribute to PLDI without re-verification)

- **Leroy, "Formal Certification of a Compiler Back-end" (CompCert)** — POPL 2006,
  not PLDI. The CompCert line is largely POPL/CACM/JAR territory.
- **Lattner & Adve, "LLVM: A Compilation Framework..."** — CGO 2004, not PLDI.
  Frequently misfiled because LLVM dominates PLDI evaluations.
- **Jung et al., "RustBelt: Securing the Foundations of the Rust Programming
  Language"** — PACMPL Vol 2, **Issue POPL** (2018). A PACMPL citation that is not
  PLDI — exactly the issue-name trap described in the header.
- **Solar-Lezama et al., "Combinatorial Sketching for Finite Programs"** — ASPLOS
  2006, not PLDI, despite program synthesis being a PLDI staple today.

Before adding a row, confirm the venue on dblp **and** the ACM DL; for 2023 and
later, confirm the PACMPL volume *and* that the issue field reads `PLDI`; then
record authors, year, pages or article number, and refresh the access date. When a
check is inconclusive, add the row as 待核实 with no attribution, or leave it out.
