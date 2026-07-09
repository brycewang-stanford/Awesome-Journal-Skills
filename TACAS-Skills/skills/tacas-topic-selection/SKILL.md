---
name: tacas-topic-selection
description: Use when deciding whether a formal-methods / verification project belongs at TACAS (ETAPS) or a sibling like CAV, VMCAI, FMCAD, SPIN, or a journal, AND — distinctively — which of TACAS's four categories (research, case-study, regular tool, tool-demonstration) it fits, plus whether the work is a SV-COMP competition contribution rather than a paper.
---

# TACAS Topic Selection

Decide two things before drafting: **is this TACAS**, and **which TACAS category**. TACAS — Tools
and Algorithms for the Construction and Analysis of Systems — is the ETAPS conference at the
**tool-and-algorithm end of verification**: model checking, program analysis, SMT and decision
procedures, testing and synthesis, and the systems that implement them. Its defining feature versus
its siblings is that a **usable, evaluated tool is a first-class contribution**, backed by a
mandatory artifact. A brilliant idea with no tool and no experiment can still be a research paper,
but a paper that is really a benchmark ranking is a **SV-COMP** contribution, not a TACAS paper.

## First cut: is this TACAS, or a sibling?

TACAS overlaps heavily with the other verification venues, so decide by **emphasis and calendar**,
not by topic alone.

| Signal in your project | Better home | Why |
|---|---|---|
| A tool or algorithm for constructing/analysing systems, with real experiments, ETAPS timing fits | **TACAS** | Tools-and-algorithms core; mandatory-artifact culture; LNCS open access |
| Deep new verification *theory/algorithm*, breadth of formal methods, larger page room | **CAV** | Closest sibling; broader FM flagship, different calendar and process |
| Principled study of verification/abstract-interpretation *foundations* | **VMCAI** | Verification, model checking, and abstract interpretation focus |
| Hardware / SAT-centric formal methods, industrial hardware verification | **FMCAD** | Its named center |
| Explicit-state / software model checking around the SPIN lineage | **SPIN** | Community and tooling match |
| A full journal-length treatment with proofs and extended evaluation | **STTT / FMSD / a journal** | No conference page ceiling; STTT is the TACAS-adjacent journal |
| A verifier to be run on the common task set and ranked | **SV-COMP** (at TACAS) | It is a competition entry, not a stand-alone tool paper |

**CAV is the trap.** Many canonical tools (NuSMV, CPAchecker, Storm) debuted at CAV, not TACAS.
Differentiate by TACAS's ETAPS context, its tool/tool-demo/case-study categories, its per-category
page limits, and its artifact-as-first-class model — and check dblp before assuming a lineage.

## Second cut: which of the four categories?

| Your contribution | Category | Page limit | Note |
|---|---|---|---|
| A new algorithm, encoding, decision procedure, or theory with a correctness argument | **Regular research** | ≤16 | Double-blind; artifact voluntary |
| Applying existing methods/tools to a substantial real system, with lessons | **Case-study** | ≤16 | Single-blind; artifact voluntary |
| A usable tool realizing a technique, with an evaluation | **Regular tool** | ≤16 | Single-blind; **mandatory artifact** |
| A mature tool shown in operation, focused on usage/UI/workflow | **Tool-demonstration** | ≤6 | Single-blind; **mandatory artifact** |

The category is a commitment: a research paper is judged on the idea and its soundness; a tool paper
is judged on the tool *and its runnable artifact*; a case-study paper is judged on the realism of
the system and the honesty of the lessons; a tool-demo is judged on a working demonstration in six
pages. Pick the one whose bar your evidence actually clears.

## Contribution shapes TACAS rewards

- **Algorithm / reduction** — a new way to construct or analyse systems with a soundness (and often
  completeness/complexity) argument (the BMC lineage).
- **Tool** — a downloadable, evaluated implementation others can point at their own inputs (the
  CBMC / Z3 lineage), now inseparable from a working artifact.
- **Case study** — a substantial application of verification to a real system that teaches the
  community what works and what breaks at scale.
- **Competition-driven** — participation in SV-COMP / VerifyThis that advances shared benchmarks and
  reproducible comparison.

## The tool-vs-research and re-label tests

- **Tool-vs-research test:** if the paper's core would survive with the tool removed (an algorithm
  and a proof), it is a **research** paper; if the core *is* the working tool and its evaluation,
  it is a **tool** paper — and then the artifact is mandatory.
- **Re-label test:** could this be submitted to CAV/VMCAI/FMCAD unchanged and read as native there?
  If its heart is FM breadth or new theory depth, weigh those venues; TACAS rewards the
  tool-and-algorithm framing with reproducible experiments.

## Cheap reconnaissance before committing

```text
[Scope]   scan the last two TACAS proceedings (dblp, Springer LNCS) for your subarea
          -> several recent papers = a reviewer pool exists; none = mismatch or a CAV/FMCAD topic
[Category] find 2-3 recent papers in the category you plan to use; match their evidence depth
[Artifact] if tool/tool-demo, can you package a clean-VM artifact by the post-paper deadline? if
          not, the category is wrong for this cycle
[Calendar] compare the next ETAPS/TACAS deadline with CAV/VMCAI/FMCAD dates -> route to the
          nearest honest fit rather than idling a year
```

## Decision procedure

```text
[Is it TACAS?] tool/algorithm to construct/analyse systems + experiments? -> yes; else CAV/VMCAI/FMCAD/journal
[Competition?] a verifier to be ranked on common tasks -> SV-COMP, not a tool paper
[Category] algorithm+proof -> research; usable tool+eval -> regular tool; mature tool in use -> tool-demo;
          real-system application -> case-study
[Blind + artifact] research -> double-blind, voluntary artifact; tool/tool-demo -> single-blind, mandatory artifact
[Verdict] TACAS <category> / sibling venue / SV-COMP / journal, with a one-line reason
```

Run this before the writing skills; a wrong venue-or-category decision wastes every later step. When
the verdict is TACAS, continue with `tacas-workflow` for the calendar and `tacas-writing-style` for
the paper shape.
