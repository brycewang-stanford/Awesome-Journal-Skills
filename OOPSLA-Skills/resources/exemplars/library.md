# OOPSLA Exemplars Library (contribution shape × era)

> **Verification protocol, access date 2026-07-08.** Each entry was confirmed against a dblp
> conference/journal record or an ACM Digital Library DOI landing page (read via search
> renderings — see the access-method note in
> [`../official-source-map.md`](../official-source-map.md)) to be either (a) an entry in an
> ACM SIGPLAN OOPSLA proceedings volume (pre-2018 era) or (b) an article in a **PACMPL Issue
> OOPSLA** (journal era). Anything that could not be pinned to OOPSLA specifically was cut
> and logged in the rejection list at the bottom. Six confirmed entries beat a long guessed
> list.
>
> **The trap this library guards against:** the SIGPLAN family shares authors, topics, and
> even paper series across PLDI, POPL, ICFP, ECOOP, and Onward!, and famous "OOPSLA-sounding"
> results often live elsewhere. A citation claiming OOPSLA is wrong until the dblp key says
> `conf/oopsla/...` or the DOI resolves to a PACMPL OOPSLA issue.
>
> **What these entries are for:** studying how a strong OOPSLA paper *shapes* its
> contribution and evidence. Do not quote their numbers, speedups, or study sizes from this
> file — reread the originals. Policy questions go to
> [`../official-source-map.md`](../official-source-map.md), never to an exemplar.

---

## Reading the library

OOPSLA's published scope runs "from design to implementation and from mathematical
formalisms to empirical studies" (PACMPL scope statement, source 6 in the source map). The
six entries below are chosen to span that spread — a benchmark suite, a measurement
methodology, a soundness counterexample, a language-design experience paper, a formal
semantics for a deployed feature, and a large-scale socio-technical study — because the most
common OOPSLA planning mistake is assuming only one of these shapes is "a real OOPSLA
paper." Pair each with the skill named in its row.

## The six verified exemplars

| Paper | Where verified | Contribution shape | Study with |
| --- | --- | --- | --- |
| Blackburn et al., *The DaCapo Benchmarks: Java Benchmarking Development and Analysis*, OOPSLA 2006 | DOI 10.1145/1167473.1167488 | Community infrastructure: a benchmark suite plus the methodology argument for why the old one misled | `oopsla-experiments` |
| Georges, Buytaert & Eeckhout, *Statistically Rigorous Java Performance Evaluation*, OOPSLA 2007, pp. 57-76 | dblp `conf/oopsla/GeorgesBE07`; DOI 10.1145/1297027.1297033 | Methodology critique: shows prevailing measurement practice can invert conclusions, then prescribes statistics | `oopsla-reproducibility` |
| Meyerovich & Rabkin, *Empirical Analysis of Programming Language Adoption*, OOPSLA 2013 | DOI 10.1145/2509136.2509515 | Socio-technical empirical study: hundreds of thousands of repositories plus programmer surveys | `oopsla-topic-selection` |
| Amin & Tate, *Java and Scala's Type Systems are Unsound*, OOPSLA 2016, pp. 838-848 | dblp `conf/oopsla/AminT16`; DOI 10.1145/2983990.2984004 | Counterexample paper: short programs breaking two industrial type systems, with the design post-mortem | `oopsla-writing-style` |
| Bezanson et al., *Julia: Dynamism and Performance Reconciled by Design*, PACMPL 2(OOPSLA):120, 2018 | DOI 10.1145/3276490 | Language-design experience report: how a shipped language's choices interact, argued with evidence | `oopsla-related-work` |
| Belyakova et al., *World Age in Julia: Optimizing Method Dispatch in the Presence of Eval*, PACMPL 4(OOPSLA):207, 2020 | DOI 10.1145/3428275 | Formalization of a deployed mechanism: a core calculus plus the optimizations the semantics licenses | `oopsla-supplementary` |

## What each one teaches an author

- **DaCapo (2006).** The claim is not "our suite is bigger" but "the incumbent suite makes
  JVM research draw wrong conclusions, and here is the replacement plus the analysis
  discipline to use it." Infrastructure earns an OOPSLA slot when it carries an argument.
- **Georges et al. (2007).** The paper's engine is an error demonstration: identical systems
  compared under common practice yield contradictory verdicts, so confidence intervals are
  not optional. This is the ancestor of the evidence bar `oopsla-experiments` enforces.
- **Meyerovich & Rabkin (2013).** Proof that OOPSLA accepts questions whose subject is
  *programmers*, not compilers — provided the corpus scale and survey design would survive a
  social-science referee. The human-aspects lane is real but has its own methodology bar.
- **Amin & Tate (2016).** A handful of small programs, decades of consequence. Note how the
  writing spends its pages on *why* the unsoundness arises from feature interaction, turning
  a bug report into a design lesson — the OOPSLA move.
- **Julia (2018).** The journal-era experience paper: retrospective, honest about trade-offs,
  and valuable precisely because the language shipped. Use it to calibrate whether an
  industrial-experience draft has enough analysis to be research.
- **World Age (2020).** Formal work in the OOPSLA register: the calculus (juliette) exists to
  explain and optimize a mechanism running in a real implementation, and the paper keeps
  that motivation in front of the math throughout.

## Cut during verification (and why)

- *Design Patterns* (Gamma, Helm, Johnson, Vlissides) — a 1994 **book**, not an OOPSLA
  paper, despite its deep association with the OOPSLA community. Do not cite it as one.
- *Bringing the Web up to Speed with WebAssembly* — verified to be **PLDI 2017**; kept out
  as the canonical SIGPLAN-sibling misattribution risk for this pack.
- *Is Sound Gradual Typing Dead?* — **POPL 2016**. Gradual-typing performance work spreads
  across POPL/PLDI/OOPSLA; check each paper's dblp key individually.
- *Understanding TypeScript* — **ECOOP 2014** (AITO's European OO conference, not a SIGPLAN
  PACMPL track). ECOOP proximity makes this family of mix-ups common.
- Any candidate whose only evidence was a PDF hosted on an author page with no dblp or DOI
  confirmation reachable at the access date — logged as unusable rather than guessed.

## Maintenance rule

To add an entry: locate the dblp key (`conf/oopsla/...` or `journals/pacmpl/...` with an
OOPSLA issue) **and** the ACM DOI, record both plus pages/article number, and date the check.
If either lookup fails, the paper goes in the cut list, not the table. Entries older than
two SPLASH cycles should be re-spot-checked when touched, since DOIs occasionally remap.
