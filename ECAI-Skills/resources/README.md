# ECAI Resources

Action-oriented resources for the ECAI skill pack. The `skills/` give advice; this directory lets
an agent model an ECAI-shaped paper, benchmark against verified exemplars, and prepare an
open-science package for the double-blind, summary-reject-and-rebuttal process — while keeping
straight which regime the target edition is in (standalone IOS Press **FAIA** vs the joint
**IJCAI-ECAI 2026** IJCAI proceedings).

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before-to-after abstract/introduction rewrite for a broad-AI ECAI paper that must land its contribution inside a 7-page body. Illustrative fictional paper; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against real, verified ECAI/PAIS papers across contribution shapes (KR, planning, multi-agent, ML, applied AI), and avoid sibling-venue confusion with IJCAI, AAAI, AAMAS, and NeurIPS. |
| [`official-source-map.md`](official-source-map.md) | Confirm the current-cycle ECAI deadline, page budget, review model, publisher/template regime, and PAIS status before giving submission-ready advice. |
| [`external_tools.md`](external_tools.md) | Open the official IJCAI-ECAI 2026, ECAI 2024, IOS Press FAIA, EurAI, and dblp surfaces, plus cross-check sources for when the gateway blocks a direct fetch. |
| [`code/README.md`](code/README.md) | Use the shared reproducibility tooling: a claim-to-evidence matrix and a dependency-free smoke checker for an anonymized supplementary package. |

## Scope Note

This is a **general-AI** conference pack (symbolic + applied AI: KR, planning, argumentation,
search, multi-agent, ML) with a **book-series open-access** publication model (IOS Press FAIA)
whose current edition is **merged with IJCAI**. It is not an ML-benchmark pack, not an economics
pack, and not an ACM/IEEE software-engineering pack. Do not import `acmart`/`IEEEtran` templates,
an ACM artifact-badging workflow, or a Stata/DiD econometrics kit. ECAI evidence is broad-AI
evidence — a well-posed problem, a sound method (formal or empirical), and enough experiments or
proofs to back the claim inside a tight 7-page body.

## Suggested Workflow

1. Route and frame with
   [`../skills/ecai-topic-selection`](../skills/ecai-topic-selection/SKILL.md) and
   [`../skills/ecai-writing-style`](../skills/ecai-writing-style/SKILL.md) — decide ECAI vs.
   IJCAI/AAAI/AAMAS (and main track vs. PAIS) **before** writing, because the 2026 joint edition
   and the FAIA page budget shape the paper.
2. Build evidence with [`../skills/ecai-experiments`](../skills/ecai-experiments/SKILL.md),
   [`../skills/ecai-reproducibility`](../skills/ecai-reproducibility/SKILL.md), and
   [`code/README.md`](code/README.md).
3. Benchmark against [`exemplars/library.md`](exemplars/library.md), then confirm the live cycle
   and the **publisher/template regime** in [`official-source-map.md`](official-source-map.md)
   and [`external_tools.md`](external_tools.md) before the submission audit in
   [`../skills/ecai-submission`](../skills/ecai-submission/SKILL.md).
