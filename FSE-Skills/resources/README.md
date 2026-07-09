# ESEC/FSE Resources

Action-oriented resources for the FSE skill pack. The `skills/` give advice; this directory lets
an agent model an FSE-shaped paper, benchmark against verified exemplars, and prepare an
open-science replication package for the double-anonymous, journal-style PACMSE process.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before-to-after abstract/introduction rewrite for an empirical software-engineering paper. Illustrative fictional paper; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against real, verified ESEC/FSE papers across contribution shapes, and avoid sibling-venue confusion with ICSE, ASE, and ISSTA. |
| [`official-source-map.md`](official-source-map.md) | Confirm the current-cycle FSE deadline, page budget, review model, PACMSE publication, and artifact policy before giving submission-ready advice. |
| [`external_tools.md`](external_tools.md) | Open the official FSE, PACMSE, HotCRP, and ACM artifact surfaces, plus the cross-check sources for when the gateway blocks a direct fetch. |
| [`code/README.md`](code/README.md) | Use the shared SE replication-package tooling: an evidence-to-claim matrix, an ACM-badge checklist, and a dependency-free smoke checker for anonymized artifacts. |

## Scope Note

This is a software-engineering conference pack whose papers publish in a **journal** (PACMSE),
not an ML-conference or economics pack. Do not import the OpenReview/PMLR machinery or the
Stata/DiD/IV/RDD econometrics kit. FSE evidence is empirical-SE evidence: real subject systems,
credible baselines, threats-to-validity reasoning, and an inspectable artifact carried through a
double-anonymous, Major-Revision-capable review.

## Suggested Workflow

1. Route and frame with
   [`../skills/fse-topic-selection`](../skills/fse-topic-selection/SKILL.md) and
   [`../skills/fse-writing-style`](../skills/fse-writing-style/SKILL.md) — deciding FSE vs.
   ICSE/ASE/ISSTA before writing is the highest-leverage move.
2. Build evidence with [`../skills/fse-experiments`](../skills/fse-experiments/SKILL.md),
   [`../skills/fse-reproducibility`](../skills/fse-reproducibility/SKILL.md), and
   [`code/README.md`](code/README.md).
3. Benchmark against [`exemplars/library.md`](exemplars/library.md), then confirm the live cycle
   in [`official-source-map.md`](official-source-map.md) and
   [`external_tools.md`](external_tools.md) before the HotCRP audit in
   [`../skills/fse-submission`](../skills/fse-submission/SKILL.md).
