# CAV Resources

Action-oriented resources for the CAV skill pack. The `skills/` give advice; this directory lets
an agent model a CAV-shaped paper, benchmark against verified exemplars, and prepare a
verification-tool artifact for the LNCS, two-stage-review, AEC-badged CAV process.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before-to-after abstract/introduction rewrite for a formal-verification paper. Illustrative fictional paper; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against real, verified CAV papers across contribution shapes (technique, algorithm, SMT-solver tool paper, new application domain), and avoid sibling-venue confusion with TACAS, FMCAD, and VMCAI. |
| [`official-source-map.md`](official-source-map.md) | Confirm the current-cycle CAV categories, page limits, anonymization matrix, two-stage review, LNCS publication, and AEC badges before giving submission-ready advice. |
| [`external_tools.md`](external_tools.md) | Open the official CAV, FLoC, Springer LNCS, and artifact surfaces, plus the SV-COMP/SMT-COMP/SMT-LIB benchmark references and the cross-check sources for when the gateway blocks a direct fetch. |
| [`code/README.md`](code/README.md) | Use the shared replication-package tooling, plus the CAV-specific checks the generic kit cannot make (benchmark provenance, solver seeds, resource limits, proof witnesses). |

## Scope Note

This is a **formal-methods / verification** conference pack whose papers publish as **Springer
LNCS open-access chapters**, not an ACM-journal, IEEE, or ML-conference pack. Do not import the
PACMPL/OpenReview machinery, the IEEEtran double-column habit, or the empirical-social-science
statistics kit. CAV evidence is verification evidence: soundness and completeness arguments,
standard benchmarks (SV-COMP, SMT-COMP, HWMCC, VNN-COMP), fair solver comparisons with pinned
versions and resource limits, and — where the claim is correctness — checkable proof
witnesses/certificates, all carried through a two-stage review and an optional AEC artifact
badge.

## Suggested Workflow

1. Route and frame with
   [`../skills/cav-topic-selection`](../skills/cav-topic-selection/SKILL.md) and
   [`../skills/cav-writing-style`](../skills/cav-writing-style/SKILL.md) — deciding CAV vs.
   TACAS/FMCAD/VMCAI/POPL and picking the right category (Regular vs. Tool vs. Application) before
   writing is the highest-leverage move.
2. Build evidence with [`../skills/cav-experiments`](../skills/cav-experiments/SKILL.md),
   [`../skills/cav-reproducibility`](../skills/cav-reproducibility/SKILL.md), and
   [`code/README.md`](code/README.md).
3. Benchmark against [`exemplars/library.md`](exemplars/library.md), then confirm the live cycle
   in [`official-source-map.md`](official-source-map.md) and
   [`external_tools.md`](external_tools.md) before the portal audit in
   [`../skills/cav-submission`](../skills/cav-submission/SKILL.md).
