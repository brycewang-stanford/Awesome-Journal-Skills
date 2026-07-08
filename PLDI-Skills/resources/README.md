# PLDI Resources

Working materials behind the PLDI skill pack. The `skills/` directory carries the
advice; this directory carries what the advice points at — verified sources, real
exemplar papers, a worked first-page rewrite, and an artifact-packaging scaffold
tuned to PLDI's badge culture.

## Contents

| Resource | Use it to... |
| --- | --- |
| [`official-source-map.md`](official-source-map.md) | Trace every venue fact in this pack to a dated official URL, see the access-method caveat, and find the 待核实 list before giving deadline-sensitive advice. |
| [`exemplars/library.md`](exemplars/library.md) | Position a draft against venue-verified PLDI papers, from classic proceedings (DART, Valgrind, Csmith, Halide) to the PACMPL Issue PLDI era, with sibling-venue traps documented. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | Watch a fictional compiler paper's abstract and introduction get rewritten from product-announcement style to PLDI's design-insight-plus-benchmark-rigor arc. |
| [`external_tools.md`](external_tools.md) | Jump to HotCRP, PACMPL, dblp, Zenodo, acmart, and the SIGPLAN Empirical Evaluation Guidelines with author-side checks attached. |
| [`code/README.md`](code/README.md) | Adapt the shared conference methods kit into a badge-ready PLDI artifact: pinned toolchains, scripted benchmark protocols, Zenodo archiving. |

## Scope note

This pack is about a systems-flavored PL conference that publishes through a
journal (PACMPL). Two boundaries follow. First, nothing here belongs to the
economics packs — no regression kits, no journal cover letters. Second, PACMPL's
journal format does not make PLDI a journal venue: submission is an annual
conference cycle with a hard cap and double-blind review, and the skills treat it
that way.

## Suggested route through the pack

1. Decide the venue with [`../skills/pldi-topic-selection`](../skills/pldi-topic-selection/SKILL.md),
   using [`exemplars/library.md`](exemplars/library.md) to calibrate against
   POPL/OOPSLA/ASPLOS neighbors.
2. Shape the paper with [`../skills/pldi-writing-style`](../skills/pldi-writing-style/SKILL.md)
   and the worked example, then harden the evaluation with
   [`../skills/pldi-experiments`](../skills/pldi-experiments/SKILL.md).
3. Package evidence via [`../skills/pldi-reproducibility`](../skills/pldi-reproducibility/SKILL.md)
   and [`code/README.md`](code/README.md), aiming at the badge ladder early.
4. Before any date or rule leaves your mouth, reopen
   [`official-source-map.md`](official-source-map.md) and the live track pages in
   [`external_tools.md`](external_tools.md).
