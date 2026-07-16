# Accounting, Organizations and Society — Resources

Capability layer for the **Accounting, Organizations and Society (AOS)** skill pack.
Runnable code is vendored for self-containment; cross-cutting quantitative-method
guidance lives once in the shared empirical-methods hub and is linked below. Because
AOS is mixed-methods, note the division of labor: the shared hub serves the pack's
**quantitative strand** (experiments, surveys, archival-with-theory); the qualitative
strand's rigor apparatus (case logic, coding discipline, evidence registers) lives in
this pack's skills themselves.

## Contents

| Resource | What it gives an agent |
|---|---|
| [`code/`](code/) | Reproducible Stata + Python causal-inference skeleton (clean → descriptive → DiD/IV/RDD/DML → mechanism → robustness → tables). Vendored from the verified Economic-Research-Journal-Skills library (Stata 18 MP, 2026-06). Relevant to AOS's archival-with-theory and experimental strands only; copy-and-adapt, change no command blindly. |
| [reviewer-objection-checklist](../../shared-resources/empirical-methods/reviewer-objection-checklist.md) | Referee objections by identification strategy, each with its preemption — for the pack's quantitative strand. |
| [reporting-standards](../../shared-resources/empirical-methods/reporting-standards.md) | Modern inference and reporting table stakes (clustering, multiple testing, DiD/RDD reporting, reproducibility). |
| [`official-source-map.md`](official-source-map.md) | Official Elsevier/ScienceDirect URLs behind every verified AOS fact in this pack (checked 2026-07-16), with re-check flags for volatile items. |
| [`external_tools.md`](external_tools.md) | Tradition-by-tradition toolkit: qualitative coding software and evidence registers; experiment platforms and pools; survey psychometrics; archival stacks. |
| [`worked-examples/`](worked-examples/) | Before → after rewrite in AOS house style. `01-introduction.md` shows the theory-first, conversation-entering introduction of a qualitative field paper. Fictional teaching paper; invents no journal policy. |
| [`exemplars/library.md`](exemplars/library.md) | Canonical AOS papers by tradition × topic (foundational statements, field studies, governmentality/ANT, experiments), each with a self-check question. Positioning guidance only — no reproduced findings. |

## How to use

1. **Before committing to AOS** — run the draft against `exemplars/library.md` and the
   scope gate in `aos-topic-selection`; the capital-markets-without-theory genre fails
   at triage, not at review.
2. **While analyzing** — qualitative strand: build the claim → evidence register the
   skills describe; quantitative strand: adapt `code/` and walk the shared
   reviewer-objection checklist.
3. **Before submitting** — reconcile every volatile fact (portal, article types,
   OA pricing, declarations) against `official-source-map.md` and the live Guide for
   Authors.

> Shared-hub guidance is venue-neutral; defer to this pack's skills and
> `official-source-map.md` for what *AOS specifically* expects.
