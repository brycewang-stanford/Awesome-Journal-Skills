# POPL Resources

Working materials that back the POPL skill pack. The `skills/` directory advises; this
directory lets an agent check facts against dated official sources, benchmark a draft
against venue-verified POPL landmarks, and stand up a proof-artifact package without
dragging in kits built for empirical fields.

## Contents

| Resource | Use it to... |
| --- | --- |
| [`official-source-map.md`](official-source-map.md) | Confirm POPL 2027/2026 mechanics — deadline, format cap, full double-blind, conditional acceptance, artifact badges — with URLs, access dates, and the 待核实 register. |
| [`exemplars/library.md`](exemplars/library.md) | Position a draft against dblp/ACM-DL-verified POPL landmarks from 1977 to the PACMPL era, and dodge the LICS/JCSS/FPCA misattribution traps. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | Study a before/after rewrite of a fictional type-systems paper's first page into the POPL informal-to-formal ramp. |
| [`external_tools.md`](external_tools.md) | Jump to HotCRP, the PACMPL journal pages, dblp, Zenodo, and proof-assistant toolchain references, with author-side checks. |
| [`code/README.md`](code/README.md) | Adapt the shared ML-conference artifact kit to a mechanized-proof artifact — and see exactly where its assumptions stop applying. |

## Scope note

This is a programming-languages *theory* conference pack. Do not import the
econometrics kits from the journal packs, and be careful even with the shared ML
kit: POPL's central artifact is usually a proof development whose "reproduction" is
type-checking, not a training run whose reproduction is seeds and GPUs. The
adaptations in [`code/README.md`](code/README.md) spell out the mapping.

## Suggested order of use

1. Route the project with [`../skills/popl-topic-selection`](../skills/popl-topic-selection/SKILL.md);
   if it stays, shape the first page with
   [`../skills/popl-writing-style`](../skills/popl-writing-style/SKILL.md) against the
   worked example.
2. Build the evidence spine with
   [`../skills/popl-reproducibility`](../skills/popl-reproducibility/SKILL.md) and
   [`../skills/popl-experiments`](../skills/popl-experiments/SKILL.md), benchmarking
   ambition against [`exemplars/library.md`](exemplars/library.md).
3. Before anything deadline-facing, reopen the live pages listed in
   [`official-source-map.md`](official-source-map.md) — POPL's July cutoff makes stale
   date advice uniquely expensive — then run
   [`../skills/popl-submission`](../skills/popl-submission/SKILL.md).
