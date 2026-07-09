# ACM CoNEXT Resources

Action-oriented resources for the CoNEXT skill pack. The `skills/` give advice; this directory
lets an agent model a CoNEXT-shaped networking paper, benchmark against verified exemplars, choose
between the two annual cycles, and prepare a reproducible artifact for the double-anonymous,
journal-style PACMNET process.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before-to-after abstract/introduction rewrite for a systems-networking paper. Illustrative fictional paper; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against real, verified ACM CoNEXT papers across contribution shapes, and avoid sibling-venue confusion with SIGCOMM, NSDI, and IMC. |
| [`official-source-map.md`](official-source-map.md) | Confirm the current-cycle CoNEXT deadlines (December and June), page budget, review model, PACMNET publication, and reproducibility badging before giving submission-ready advice. |
| [`external_tools.md`](external_tools.md) | Open the official CoNEXT, PACMNET, HotCRP, and ACM reproducibility surfaces, plus the cross-check sources for when the gateway blocks a direct fetch. |
| [`code/README.md`](code/README.md) | Use the shared replication-package tooling: an evidence-to-claim matrix, an ACM-badge checklist, and a dependency-free smoke checker for anonymized artifacts. |

## Scope Note

This is a **systems-networking** conference pack whose papers publish in a **journal** (PACMNET),
not an ML-conference or economics pack. Do not import the OpenReview/PMLR machinery or the
Stata/DiD/IV/RDD econometrics kit. CoNEXT evidence is networking evidence: real testbeds and
deployments, honest baselines, reproducible measurements from pinned traces and configs, and an
inspectable artifact carried through a double-anonymous, one-shot-major-revision review that lands
in a PACMNET issue.

## Suggested Workflow

1. Route and frame with
   [`../skills/conext-topic-selection`](../skills/conext-topic-selection/SKILL.md) and
   [`../skills/conext-writing-style`](../skills/conext-writing-style/SKILL.md) — deciding CoNEXT vs.
   SIGCOMM/NSDI/IMC, and December vs. June, before writing is the highest-leverage move.
2. Build evidence with [`../skills/conext-experiments`](../skills/conext-experiments/SKILL.md),
   [`../skills/conext-reproducibility`](../skills/conext-reproducibility/SKILL.md), and
   [`code/README.md`](code/README.md) — and remember badge **opt-in is due at submission**.
3. Benchmark against [`exemplars/library.md`](exemplars/library.md), then confirm the live cycle in
   [`official-source-map.md`](official-source-map.md) and
   [`external_tools.md`](external_tools.md) before the HotCRP audit in
   [`../skills/conext-submission`](../skills/conext-submission/SKILL.md).
