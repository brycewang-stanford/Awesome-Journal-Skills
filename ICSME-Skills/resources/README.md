# IEEE ICSME Resources

Action-oriented resources for the ICSME skill pack. The `skills/` give advice; this directory lets
an agent model an ICSME-shaped maintenance/evolution paper, benchmark against verified exemplars,
and prepare an open-science replication package for the single-round, double-anonymous IEEE process
and its ROSE-Festival artifact track.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before-to-after abstract/introduction rewrite for a maintenance/evolution paper. Illustrative fictional paper; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against real, verified ICSM/ICSME papers across contribution shapes, and avoid sibling-venue confusion with ICSE, FSE, MSR, and SCAM. |
| [`official-source-map.md`](official-source-map.md) | Confirm the current-cycle ICSME deadlines, page budget, single-round review model, track list, and ROSE-Festival badges before giving submission-ready advice. |
| [`external_tools.md`](external_tools.md) | Open the official ICSME, EasyChair, IEEE, and ROSE surfaces, plus the cross-check sources for when the gateway blocks a direct fetch. |
| [`code/README.md`](code/README.md) | Use the shared SE replication-package tooling: an evidence-to-claim matrix, a ROSE-badge checklist, and a dependency-free smoke checker for anonymized artifacts. |

## Scope Note

This is a **maintenance/evolution** conference pack: an **IEEE** venue (IEEEtran two-column, IEEE
Xplore, IEEE research-object badges), single-round double-anonymous review, and a strong open-science
and replication culture. Do not import the ACM `acmart` template, ACM's four-badge scheme, the
OpenReview/PMLR machinery, or the Stata/DiD/IV/RDD econometrics kit. ICSME evidence is
maintenance-empirical evidence: real evolving subject systems, mined change history with pinned
provenance, credible baselines, threats-to-validity reasoning, and an inspectable artifact carried
through a single-round review that offers **no Major Revision** safety net.

## Suggested Workflow

1. Route and frame with
   [`../skills/icsme-topic-selection`](../skills/icsme-topic-selection/SKILL.md) and
   [`../skills/icsme-writing-style`](../skills/icsme-writing-style/SKILL.md) — deciding ICSME (and
   which ICSME track) vs. ICSE/FSE/SANER/MSR before writing is the highest-leverage move.
2. Build evidence with [`../skills/icsme-experiments`](../skills/icsme-experiments/SKILL.md),
   [`../skills/icsme-reproducibility`](../skills/icsme-reproducibility/SKILL.md), and
   [`code/README.md`](code/README.md) — mining provenance pinned at collection time cannot be
   retrofitted, and there is no revision round to add it in.
3. Benchmark against [`exemplars/library.md`](exemplars/library.md), then confirm the live cycle in
   [`official-source-map.md`](official-source-map.md) and
   [`external_tools.md`](external_tools.md) before the EasyChair audit in
   [`../skills/icsme-submission`](../skills/icsme-submission/SKILL.md).
