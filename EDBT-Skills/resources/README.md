# EDBT Resources

Action-oriented resources for the EDBT skill pack. The `skills/` give advice; this directory lets
an agent model an EDBT-shaped paper, benchmark against verified exemplars, and prepare a
reproducible package for the multiple-cycle, revise-and-resubmit, open-access OpenProceedings
process.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before-to-after abstract/introduction rewrite for a database-systems paper. Illustrative fictional paper; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against real, verified EDBT papers across contribution shapes, and avoid sibling-venue confusion with SIGMOD, VLDB, ICDE, and the co-located ICDT. |
| [`official-source-map.md`](official-source-map.md) | Confirm the current cycle deadlines, page budgets, paper shapes, review model, the OpenProceedings publication terms, and the resubmission ban before giving submission-ready advice. |
| [`external_tools.md`](external_tools.md) | Open the official EDBT/ICDT host site, EDBT Association, Microsoft CMT, and OpenProceedings surfaces, plus the cross-check sources for when the gateway blocks a direct fetch. |
| [`code/README.md`](code/README.md) | Use the shared replication-package tooling: a claim-to-evidence matrix, a reproducibility checklist, and a dependency-free smoke checker for a database-systems artifact. |

## Scope Note

This is a **database-systems** conference pack whose papers are published **open access on
OpenProceedings.org** under CC-BY-NC-ND, not in the ACM/IEEE paywalled DLs and not as an ML or
economics pack. Do not import the OpenReview/PMLR machinery or the Stata/DiD/IV/RDD econometrics
kit. EDBT evidence is database-systems evidence: real workloads and datasets, credible baselines,
honest measurement across realistic scales, and an inspectable artifact carried through a
multiple-cycle process with a genuine in-cycle revise-and-resubmit.

## Suggested Workflow

1. Route and frame with
   [`../skills/edbt-topic-selection`](../skills/edbt-topic-selection/SKILL.md) and
   [`../skills/edbt-writing-style`](../skills/edbt-writing-style/SKILL.md) — deciding EDBT vs.
   SIGMOD/VLDB/ICDE/ICDT, and picking the paper shape and cycle, before writing is the
   highest-leverage move.
2. Build evidence with [`../skills/edbt-experiments`](../skills/edbt-experiments/SKILL.md),
   [`../skills/edbt-reproducibility`](../skills/edbt-reproducibility/SKILL.md), and
   [`code/README.md`](code/README.md).
3. Benchmark against [`exemplars/library.md`](exemplars/library.md), then confirm the live cycle in
   [`official-source-map.md`](official-source-map.md) and
   [`external_tools.md`](external_tools.md) before the CMT audit in
   [`../skills/edbt-submission`](../skills/edbt-submission/SKILL.md).
