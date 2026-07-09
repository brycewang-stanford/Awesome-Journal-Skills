# ICDE Resources

The twelve `skills/` tell an agent what to do; this folder gives it the raw material to do it
well — a modeled ICDE opening to draft against, award-verified papers to benchmark positioning,
a runnable-artifact reference for the CMT supplement, and the dated fact ledger that keeps every
claim honest. Everything here is oriented around one ICDE reality that separates this pack from
its double-blind siblings: **the review is single-blind, so author identity stays on the paper
and the supplement.**

## Map of the folder

- **[`official-source-map.md`](official-source-map.md)** — the factual backbone. Read it first
  when a date or policy is load-bearing: it records what was verified, from which URL, on
  2026-07-09, the access-method caveat, and the 待核实 items that were deliberately not guessed.
- **[`external_tools.md`](external_tools.md)** — the live surfaces (research call, important
  dates, submission guidelines, CMT, IEEE Xplore, TKDE) plus the author-side verification loop
  and the do-not-infer rules. Open these before any deadline-sensitive advice.
- **[`exemplars/library.md`](exemplars/library.md)** — three award-anchored real ICDE papers
  (the 10-Year Influential Paper lineage plus an industry best paper) as positioning references,
  with a guarded list of famous papers that are *not* ICDE papers.
- **[`worked-examples/01-introduction.md`](worked-examples/01-introduction.md)** — a fictional
  write-optimized-index paper whose first page is rewritten before → after, showing the ICDE
  first-page contract in action.
- **[`code/README.md`](code/README.md)** — a pointer into the shared artifact smoke-check kit,
  read with data-systems eyes for the CMT supplemental package.

## What this folder is not

It is a data-engineering conference pack, not an empirical-economics one: there is no
Stata/DiD/IV/RDD kit here, and the ML-conference smoke checker in `code/` is a packaging aid,
never a substitute for the workload-and-baseline discipline that
[`../skills/icde-experiments/SKILL.md`](../skills/icde-experiments/SKILL.md) and
[`../skills/icde-reproducibility/SKILL.md`](../skills/icde-reproducibility/SKILL.md) enforce. It
also serves the **research track** primarily; the industry and applications track appears only as
a routing option inside
[`../skills/icde-topic-selection/SKILL.md`](../skills/icde-topic-selection/SKILL.md).

## How the pieces chain together

Route the project before touching format:
[`../skills/icde-topic-selection`](../skills/icde-topic-selection/SKILL.md) settles research vs.
industry and ICDE vs. SIGMOD/PVLDB. Then shape the paper with
[`../skills/icde-writing-style`](../skills/icde-writing-style/SKILL.md), the worked example open
beside the draft and positioning checked against the exemplars. Harden the evidence through
[`../skills/icde-experiments`](../skills/icde-experiments/SKILL.md) and the reproducibility skill,
using the smoke check as a last gate. Finally execute the chosen round with
[`../skills/icde-workflow`](../skills/icde-workflow/SKILL.md) and
[`../skills/icde-submission`](../skills/icde-submission/SKILL.md) — re-confirming every date
against the source map and external-tools pages, never against a past edition's memory.
