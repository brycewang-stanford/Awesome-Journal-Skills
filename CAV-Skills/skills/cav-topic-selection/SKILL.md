---
name: cav-topic-selection
description: Use when deciding whether a formal-methods project belongs at CAV (Computer Aided Verification) or should be routed to TACAS, FMCAD, VMCAI, LPAR/IJCAR, POPL/PLDI/OOPSLA, or a journal (FMSD/JAR/TOCL), and when choosing the right CAV category — Regular, Short Tool, Short Application, or Industrial Experience & Case Study.
---

# CAV Topic Selection

Decide the venue and the category before drafting. CAV — the International Conference on Computer
Aided Verification — is the **flagship** venue for computer-aided formal analysis of hardware and
software systems: model checking, SMT and theorem proving, program analysis and synthesis, and
their tools. Its papers are Springer LNCS chapters read by verification researchers, so reviewers
reward a **durable verification contribution with a stated guarantee**, not a systems demo or an ML
result with a verification label attached.

## Two decisions, not one

At CAV you choose both a **venue** (CAV vs. its siblings) and a **category** (Regular vs. Tool vs.
Application vs. Industrial). Get the venue right first, then the category — a strong tool filed as a
Regular Paper, or a technique squeezed into a 10-page tool paper, wastes the fit.

## Sibling-venue routing table

| Signal in your project | Better home | Why |
|---|---|---|
| A general verification technique/algorithm with a soundness/completeness result, mature enough for the flagship | **CAV** | Flagship scope; the Regular-Paper archetype |
| Emphasis on tools, algorithms, and their construction/analysis, or you want the ETAPS calendar | **TACAS** | Tools and Algorithms for the Construction and Analysis of Systems; overlaps heavily but is a distinct venue |
| Hardware-oriented or applied model checking, or a formal-methods-in-design focus | **FMCAD** | Formal Methods in Computer-Aided Design |
| Verification, model checking, and abstract interpretation with a foundations flavor, often earlier-stage | **VMCAI** | Verification, Model Checking, and Abstract Interpretation |
| Automated/interactive theorem proving or logic-focused | **IJCAR / LPAR / ITP / CADE** | Reasoning and proof communities |
| The core is a programming-language semantics, type system, or PL analysis | **POPL / PLDI / OOPSLA** | PL venues; verification is a means, not the contribution |
| The study is too long or too deep for the page limit | **FMSD / JAR / TOCL / STTT** | Journals with no conference page ceiling |

CAV and TACAS overlap the most; the honest tie-breakers are the **calendar** (CAV is annual in
mid-year, often under FLoC or standalone; TACAS runs at ETAPS in spring) and **community pull** for
your subarea. A strong paper is publishable at either — route to the nearer honest fit.

## Contribution shapes CAV rewards

- **Technique / algorithm with a guarantee** — a new decision procedure, model-checking algorithm,
  abstraction, invariant-synthesis method, or proof technique, with a stated soundness/completeness
  property and evidence it scales past prior methods (the CEGAR / interpolation lineage).
- **Tool paper** — a usable, downloadable verification tool (solver, model checker, prover, analyzer)
  evaluated on standard benchmarks, with the engineering foregrounded (the CVC4 / Marabou lineage).
- **New application domain** — bringing a hard real problem into verification's scope with a real
  technique (the neural-network-verification lineage).
- **Application / case study / industrial experience** — applying verification to a concrete system
  and reporting what worked, what did not, and what generalizes.

## The re-label and swap tests

Two quick tests sharpen a borderline verdict:

- **Guarantee test:** does your contribution come with a formal property (soundness, completeness,
  an equisatisfiability or refinement claim)? If the "result" is only a benchmark score with no
  guarantee, it may be a tool note (TACAS) or a heuristic paper, not a CAV Regular Paper.
- **Re-label test:** could this paper be submitted to FMCAD or VMCAI unchanged and read as native
  there? If its heart is hardware-design methodology or early-stage abstract interpretation, route
  accordingly; CAV rewards the general, flagship framing.

## Category-selection cues (once CAV is chosen)

```text
[Regular]      a technique/algorithm + proof + benchmark evaluation           -> 18 pages, anonymized
[Short Tool]   a downloadable tool; the contribution is the usable system     -> 10 pages, NOT anonymized
[Short App]    verification applied to a specific problem, technique-light     -> 10 pages, anonymized
[Industrial]   a real/industrial deployment experience or case study          -> 10 pages, NOT anonymized
```

If you have both a technique and a tool, the usual move is a Regular Paper that describes the
technique with the tool as its evaluation vehicle — reserve the Tool Paper for when the *system
itself* is the contribution.

## Cheap reconnaissance before committing

```text
[Scope]     scan the last two CAV programs (dblp, i-cav.org) for your subarea
            -> 3+ recent papers = a reviewer pool exists; 0 = opening or mismatch
[Benchmarks] is there a standard benchmark set (SV-COMP, SMT-COMP, HWMCC, VNN-COMP) reviewers expect?
            -> yes and you did not use it => reframe or add it before submitting
[Calendar]  compare the next CAV deadline with TACAS/FMCAD/VMCAI dates -> route to the nearest
            honest fit rather than idling a cycle
```

## Decision procedure

```text
[Audience]   who acts differently if the claim holds? -> verification-tool builders/users/theorists?
[Claim type] technique-with-guarantee / tool / application / industrial experience
[CAV vs sibling] both fit? -> choose by calendar, community pull, and hardware/PL/logic tilt
[Category]   technique+proof -> Regular; usable system -> Tool; applied -> Application/Industrial
[Verdict]    CAV <category> / sibling venue / journal, with a one-line reason
```

Run this before the writing skills; a wrong venue or category decision wastes every later step.
When the verdict is CAV, continue with `cav-workflow` for the calendar and `cav-writing-style` for
the paper shape.
