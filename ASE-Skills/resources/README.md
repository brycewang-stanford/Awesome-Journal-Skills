# ASE Resources

Action-oriented resources for the ASE skill pack. The `skills/` give advice; this directory lets
an agent model an ASE-shaped paper, benchmark against verified exemplars, and prepare an
open-science replication package for the double-anonymous, revision-capable ASE research track
whose proceedings appear in both IEEE Xplore and the ACM Digital Library.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before-to-after abstract/introduction rewrite for an automated-software-engineering paper (a new technique embodied in a tool, evaluated on real subjects). Illustrative fictional paper; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against real, verified ASE papers across contribution shapes, and avoid sibling-venue confusion with ICSE, FSE, ISSTA, and PLDI. |
| [`official-source-map.md`](official-source-map.md) | Confirm the current-cycle ASE deadline, page budget, required template, Accept/Revision/Reject model, dual IEEE/ACM proceedings, and artifact policy before giving submission-ready advice. |
| [`external_tools.md`](external_tools.md) | Open the official ASE, HotCRP, IEEE Xplore, ACM DL, and dblp surfaces, plus the cross-check sources for when the gateway blocks a direct fetch. |
| [`code/README.md`](code/README.md) | Use the shared SE replication-package tooling: an evidence-to-claim matrix, an artifact-badge checklist, and a dependency-free smoke checker for anonymized artifacts. |

## Scope note

This is an **automated-software-engineering** conference pack: the center of gravity is
*automating* software tasks — analysis, testing, synthesis, repair, comprehension, and increasingly
AI4SE / SE4AI. Do not import the OpenReview/PMLR machinery of an ML-conference pack or the
econometrics kit of a journal pack. ASE evidence is automated-SE evidence: real subject systems,
credible tool baselines, sound program-analysis or empirical method, and an inspectable artifact
carried through a double-anonymous, early-rejection-gated, Revision-capable review that publishes
in both IEEE Xplore and the ACM Digital Library.

## Suggested workflow

1. Route and frame with
   [`../skills/ase-topic-selection`](../skills/ase-topic-selection/SKILL.md) and
   [`../skills/ase-writing-style`](../skills/ase-writing-style/SKILL.md) — deciding ASE vs.
   ICSE/FSE/ISSTA before writing is the highest-leverage move.
2. Build evidence with [`../skills/ase-experiments`](../skills/ase-experiments/SKILL.md),
   [`../skills/ase-reproducibility`](../skills/ase-reproducibility/SKILL.md), and
   [`code/README.md`](code/README.md).
3. Benchmark against [`exemplars/library.md`](exemplars/library.md), then confirm the live cycle
   in [`official-source-map.md`](official-source-map.md) and
   [`external_tools.md`](external_tools.md) before the HotCRP audit in
   [`../skills/ase-submission`](../skills/ase-submission/SKILL.md).
