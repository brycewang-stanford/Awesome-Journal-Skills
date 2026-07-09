# TACAS Resources

Action-oriented resources for the TACAS skill pack. The `skills/` give advice; this directory lets
an agent decide which of TACAS's four paper categories a project fits, benchmark against verified
exemplar tools and foundational papers, and prepare a badge-ready artifact for the ETAPS Artifact
Evaluation Committee.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before-to-after rewrite of a TACAS **tool-paper** introduction — leading with what the tool does, its availability, and reproducible benchmark evidence. Illustrative fictional tool; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against real, dblp-verified TACAS papers across categories (foundational research and canonical tool papers), and avoid sibling-venue confusion with CAV, VMCAI, FMCAD, and SPIN. |
| [`official-source-map.md`](official-source-map.md) | Confirm the current-cycle TACAS deadline, category page limits, blind model, mandatory-artifact rule, badge set, LNCS open-access model, and SV-COMP hosting before giving submission-ready advice. |
| [`external_tools.md`](external_tools.md) | Open the official ETAPS, TACAS, EasyChair, Springer LNCS, `tacas.info` artifact, and SV-COMP surfaces, plus the cross-check sources for when the gateway blocks a direct fetch. |
| [`code/README.md`](code/README.md) | Use the shared replication-package tooling: an evidence-to-claim matrix and a dependency-free smoke checker, plus the TACAS-specific checks (badge readiness, the clean-VM run) the generic kit cannot make. |

## Scope Note

This is a **formal-methods / verification-tools** conference pack, not an ML-conference or
economics pack. Do not import OpenReview/PMLR machinery or the Stata/DiD/IV/RDD econometrics kit.
TACAS evidence is verification evidence: sound algorithms, correct tools, honest benchmark
comparisons (often against SV-COMP-style task sets), and an artifact an ETAPS evaluator can run on
a clean VM to earn Available / Functional / Reusable badges.

## Suggested Workflow

1. Route and frame with
   [`../skills/tacas-topic-selection`](../skills/tacas-topic-selection/SKILL.md) — decide the
   **category** (research / case-study / regular tool / tool-demonstration) and TACAS-vs-CAV/VMCAI
   before writing, because the category fixes the page limit, the blind mode, and the artifact
   obligation.
2. Build evidence and tooling with
   [`../skills/tacas-experiments`](../skills/tacas-experiments/SKILL.md),
   [`../skills/tacas-reproducibility`](../skills/tacas-reproducibility/SKILL.md), and
   [`code/README.md`](code/README.md).
3. Benchmark against [`exemplars/library.md`](exemplars/library.md), then confirm the live cycle in
   [`official-source-map.md`](official-source-map.md) and
   [`external_tools.md`](external_tools.md) before the EasyChair audit in
   [`../skills/tacas-submission`](../skills/tacas-submission/SKILL.md).
