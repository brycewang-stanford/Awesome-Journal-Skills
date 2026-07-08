# OSDI Resources

Action-oriented resources for the OSDI skill pack. The `skills/` directory gives advice;
this directory lets an agent verify current OSDI policy, benchmark a draft against real
accepted OSDI papers, study the systems narrative in worked form, and smoke-check an
artifact package before sysartifacts evaluation.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`official-source-map.md`](official-source-map.md) | Trace every 2026-cycle fact to an official USENIX/HotCRP source, see the 403/search-rendering access note, and read the explicit 待核实 list before giving deadline-sensitive advice. |
| [`external_tools.md`](external_tools.md) | Open the live official surfaces (USENIX pages, HotCRP, sysartifacts, dblp) and run the five author-side verification passes. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against five verified OSDI papers spanning 2004–2022, and avoid the OSDI/SOSP/NSDI/ATC misattribution traps. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before → after rewrite of a fictional storage-system abstract and introduction into the OSDI design-narrative arc. |
| [`code/README.md`](code/README.md) | Run the shared ML-conference reproducibility kit as a smoke check on an artifact package, plus OSDI-specific checks the generic kit cannot make. |

## Scope note

This is a systems-conference pack for a USENIX venue. Its center of gravity is a built,
measured system — not statistical estimators, not econometrics. Do not import the
economics code kit; the shared ML-conference kit is referenced only for artifact-package
hygiene, and OSDI-specific policy always comes from the source map and the live CFP.

## Suggested workflow

1. Route and frame with
   [`../skills/osdi-topic-selection`](../skills/osdi-topic-selection/SKILL.md) and
   [`../skills/osdi-writing-style`](../skills/osdi-writing-style/SKILL.md), using
   [`exemplars/library.md`](exemplars/library.md) as the accepted-paper baseline.
2. Build evidence with [`../skills/osdi-experiments`](../skills/osdi-experiments/SKILL.md)
   and [`../skills/osdi-reproducibility`](../skills/osdi-reproducibility/SKILL.md);
   smoke-check the artifact with [`code/README.md`](code/README.md).
3. Before upload, reconfirm every rule in
   [`official-source-map.md`](official-source-map.md) and
   [`external_tools.md`](external_tools.md), then run
   [`../skills/osdi-submission`](../skills/osdi-submission/SKILL.md) end to end.
