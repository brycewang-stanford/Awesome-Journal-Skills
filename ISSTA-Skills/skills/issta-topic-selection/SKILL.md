---
name: issta-topic-selection
description: Use when deciding whether a project is a strong ISSTA fit versus ICSE, FSE, ASE, ICST, PLDI/CAV, or an SE journal, identifying whether the contribution is a testing/analysis technique, characterizing its evaluation shape, and sharpening the framing before writing begins.
---

# ISSTA Topic Selection

Use this before writing. ISSTA is the venue for techniques that **test or analyze software** — that
find, characterize, or reason about program behaviour and defects — evaluated on real subjects. The
routing decision is mostly about whether that is the *core* of the contribution, or an ingredient in
something broader.

## Fit test

- Prefer ISSTA when the contribution is a testing or analysis technique: test generation, fuzzing,
  symbolic or concolic execution, static/dynamic analysis, fault localization, program-repair
  evaluation, sanitizers, or an empirical study *about* testing and analysis.
- Route to **ICSE or FSE** when the contribution is broader software engineering: requirements,
  design, process, developer studies, or a technique whose testing angle is secondary. These are
  the general SE flagships; ISSTA is the testing/analysis specialist.
- Route to **ASE** when the core is automation of an SE task and the testing/analysis content is a
  means rather than the end.
- Route to **ICST** when the work is testing-focused but a better fit for a testing-specific
  audience, or is more applied/industrial than ISSTA's research-track bar.
- Route to **PLDI, POPL, or CAV/TACAS** when the contribution is primarily a language/analysis
  *foundation* or a *verification* result, and the empirical bug-finding evaluation is secondary.
- Route to an **SE journal** (TSE, TOSEM, EMSE) when the work needs journal-length exposition or is
  an extended empirical study beyond a conference's scope.

## Fit signal table

| Signal in the project | ISSTA reading |
|---|---|
| A technique that finds bugs / analyzes behaviour, evaluated on real subjects | Core fit — the house genre |
| A shared benchmark or testing infrastructure others will reuse | Core fit (see Defects4J lineage) |
| A rigorous empirical study of a testing/analysis technique class | Core fit — evaluation is a contribution |
| A broad SE process, requirements, or human-factors result | Better at ICSE or FSE |
| A formal analysis/verification result with a thin empirical side | Better at PLDI/POPL or CAV |
| A tool-automation contribution where testing is incidental | Better at ASE |

## Vignette: where a repair project goes

A project produces an automated program-repair technique with a new patch-ranking method and an
evaluation on Defects4J. ISSTA reading: strong fit — a testing/analysis technique with a real
benchmark and a bug-finding-adjacent evaluation. Reframe it as a *study of why existing repair tools
produce incorrect patches* and it is still ISSTA (an evaluation contribution). Turn it into a formal
soundness result about the repair calculus with little empirical evaluation, and PLDI or CAV becomes
the better home; grow it into a broad process for integrating repair into developer workflows, and
ICSE fits better.

## Sharpening moves before committing

- Name the technique and the property it targets. If the core is not a testing/analysis technique or
  a study of one, the ISSTA framing does not exist.
- Confirm an established benchmark exists or can be built; an evaluation a reviewer cannot compare to
  prior work is a quiet fit failure here.
- Check the evaluation can be run at a fair, equal budget against the nearest tool — ISSTA's
  comparison bar is high.
- Topic emphasis drifts between editions; scan the current call's topics of interest before final
  routing.

```text
Is the core a technique that tests or analyzes software,
evaluated on real subjects against a fair baseline?
  yes -> ISSTA is a strong candidate
  broader SE / process / human factors -> ICSE / FSE
  automation-first -> ASE ; testing-applied -> ICST
  formal / verification-first -> PLDI / POPL / CAV
```

## Output format

```text
[Fit] strong ISSTA / possible ISSTA / better elsewhere
[Best venue] ISSTA / ICSE / FSE / ASE / ICST / PLDI / CAV / journal
[Contribution sentence] <one sentence naming technique + property>
[Top rejection risk] <originality / evaluation / comparison / scope>
[Next action] <technique work, benchmark choice, framing, or venue switch>
```
