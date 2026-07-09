# ICDT Resources

Action-oriented resources for the ICDT skill pack. The `skills/` give advice; this directory lets an
agent model an ICDT-shaped paper, benchmark against verified exemplars, and prepare a
complete-proofs, anonymous, LIPIcs-formatted submission for the two-cycle International Conference on
Database Theory.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before-to-after abstract/introduction rewrite for a database-theory paper — model fixed first, theorem stated early, matching bounds. Illustrative fictional result; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against real, verified ICDT Test-of-Time papers across contribution shapes, and avoid the PODS/STOC/journal misattributions. |
| [`official-source-map.md`](official-source-map.md) | Confirm the current cycle's deadlines, the revision option, the anonymity rule, the 15-page LIPIcs format, and the LIPIcs/CC-BY publication model before giving submission-ready advice. |
| [`external_tools.md`](external_tools.md) | Open the official ICDT, EDBT/ICDT, CMT, and DROPS/LIPIcs surfaces, plus the cross-check sources for when the gateway blocks a direct fetch. |
| [`code/README.md`](code/README.md) | Understand why ICDT has no code-artifact track, and use the proof-artifact checklist (complete proofs, matching bounds, self-contained PDF, consistent full version). |

## Scope Note

This is a **pure database-theory** conference pack. Its papers are **theorems**, published **open
access in LIPIcs** (Schloss Dagstuhl) — not ACM/IEEE proceedings, not a journal, and not a systems
track. Do **not** import the ML-conference reproducibility/Docker machinery, the econometrics kit, or
an ACM artifact-badging workflow. ICDT evidence is a **complete, checkable proof**; ICDT
"reproducibility" is **verifiability of theorems**; the "artifact" is the marked appendix plus the
arXiv full version.

## Suggested Workflow

1. Route and frame with [`../skills/icdt-topic-selection`](../skills/icdt-topic-selection/SKILL.md)
   and [`../skills/icdt-writing-style`](../skills/icdt-writing-style/SKILL.md) — deciding ICDT vs. PODS
   (and vs. EDBT/a pure-TCS venue) before writing is the highest-leverage move.
2. Build the argument with [`../skills/icdt-experiments`](../skills/icdt-experiments/SKILL.md) and
   [`../skills/icdt-reproducibility`](../skills/icdt-reproducibility/SKILL.md) — matching bounds and
   self-contained proofs cannot be retrofitted.
3. Benchmark against [`exemplars/library.md`](exemplars/library.md), then confirm the live cycle in
   [`official-source-map.md`](official-source-map.md) and [`external_tools.md`](external_tools.md)
   before the CMT audit in [`../skills/icdt-submission`](../skills/icdt-submission/SKILL.md).
