---
name: ase-topic-selection
description: Use when deciding whether a software-engineering project belongs at ASE (IEEE/ACM Automated Software Engineering) or should be routed to ICSE, ESEC/FSE, ISSTA, a PL venue, or an SE journal, and when distinguishing ASE by its automation-centric contribution shape, its tool/technique emphasis, and its AI4SE/SE4AI scope.
---

# ASE Topic Selection

Decide the venue before drafting. ASE — the **IEEE/ACM International Conference on Automated
Software Engineering** — is the home for research that **automates** software-engineering tasks:
the analysis, design, implementation, testing, comprehension, and maintenance of software, and
increasingly the two-way street of AI for SE and SE for AI. Its reviewers read for a **technique or
tool that automates something**, evaluated on real subjects. A paper whose real center is a broad
empirical observation, a testing-theory result, or a pure ML advance is respected and then rejected
as off-center.

## The routing question that matters most

The decisive ASE question is not "is this SE?" but **"is the contribution an *automation* — a
technique or tool that does an SE task a human or a weaker tool did before?"** If the beating heart
of the paper is a new automated mechanism (an analysis, a generator, a synthesizer, a repair
technique, a learned model applied to an SE task), ASE is a natural home. If the heart is a finding,
a theory, or a measurement study, a sibling fits better — even when the topic overlaps.

## Sibling-venue routing table

| Signal in your project | Better home | Why |
|---|---|---|
| Core is a technique/tool that **automates** an SE task, evaluated on real systems | **ASE** | Automated software engineering is its named center; dual IEEE/ACM, IEEE-Xplore+ACM-DL proceedings |
| Broad empirical or foundational SE contribution; the lesson is a finding, not a tool | **ESEC/FSE** | The general-SE flagship; PACMSE journal model, empirical breadth |
| Equally broad SE technique, but ICSE's cycle/stage fits and you want its reach | **ICSE** | The other general-SE flagship; different calendar and (IEEE-side) format |
| Depth in testing theory, program analysis foundations, or fault detection | **ISSTA** | Deeper testing/analysis expertise, round-based reviewing |
| The automated mechanism *is* a program-language/compiler advance | **PLDI / OOPSLA / POPL** | PL venues own the language-mechanism contribution |
| The contribution is a new model/architecture; the SE task is a benchmark | **an ML venue** | Model-as-contribution routes out of SE |
| Study too long or too nuanced for the page budget | **TSE / TOSEM / EMSE** | Journals with no page ceiling; some feed ASE's Journal-First track |

## Contribution shapes ASE rewards

- **Technique + tool + evaluation on real subjects** — a new analysis, test-generation, synthesis,
  repair, or comprehension technique, embodied in a tool and run on real systems against credible
  *tool* baselines (the TestEra / runtime-monitoring lineage in the exemplars library).
- **Automated technique with a disciplined empirical evaluation** — pairing an automatic method with
  an honest comparison and effectiveness metric (the Tarantula fault-localization lineage).
- **Learning-based automation with the SE task as the point** — learned code representations or
  models applied to a real SE task, where the *task* result, not the architecture, is the
  contribution (the code-clone-detection lineage).
- **AI4SE / SE4AI** — using AI to automate SE tasks, or applying SE automation to build, test, and
  maintain AI/ML systems; a growing ASE center of gravity.
- **Tooling infrastructure and datasets** — often routed to the co-located **Tools and Datasets**
  track when the contribution is a usable artifact more than a research claim.

## The model-swap and re-label tests

Two quick tests sharpen a borderline verdict:

- **Model-swap test:** if your paper leans on an LLM or learner, ask whether the automation still
  stands as a contribution when the model is swapped. If the design (the analysis, the coupling, the
  oracle) survives, it is ASE-shaped; if only the model result remains, route to an ML venue.
- **Re-label test:** could this be submitted to FSE unchanged and read as a broad empirical SE
  paper, or to ISSTA as a testing-depth paper? If its heart is *automation machinery*, ASE fits; if
  its heart is a finding or testing theory, route accordingly.

## Which co-located track fits

- **Research Papers** — a full technique/tool contribution with real-subject evaluation.
- **NIER (New Ideas and Emerging Results)** — a bold new direction not yet backed by a full
  evaluation (4 pages): groundbreaking, reflection, or late-breaking-advances.
- **Tools and Datasets** — a usable tool or dataset as the contribution (short, demo-oriented).
- **Journal-First** — work already accepted at TSE/TOSEM/EMSE (after 1 Jan 2025) presented at ASE.
- **Industry Showcase / Doctoral Symposium** — practitioner results and PhD-stage work.

## Cheap reconnaissance before committing

```text
[Scope]   scan the last two ASE programs (dblp conf/kbse, conf.researchr.org) for your subarea
          -> 3+ recent papers = a reviewer pool exists; 0 = opening or mismatch
[Shape]   is your contribution a runnable automation, or a finding/theory? -> automation => ASE
[Citations] majority SE-automation venues (ASE/ICSE/FSE/ISSTA)? -> majority non-SE => naturalize first
[Calendar] compare the next ASE deadline with ICSE/FSE/ISSTA/journal dates -> nearest honest fit
```

## Decision procedure

```text
[Audience] who runs your automation if the claim holds? -> SE developers/testers/maintainers/tool-builders?
[Claim type] technique+tool / automated-technique+evaluation / learning-based automation / AI4SE-SE4AI
[Automation test] is a runnable mechanism the contribution? -> yes => ASE; no => FSE/ISSTA/PL/ML
[Track check] full technique -> Research; bold early idea -> NIER; usable tool -> Tools & Datasets
[Verdict] ASE research track / co-located track / sibling venue / journal, with a one-line reason
```

Run this before the writing skills; a wrong venue decision wastes every later step. When the
verdict is ASE, continue with `ase-workflow` for the calendar and `ase-writing-style` for the paper
shape.
