---
name: aaai-topic-selection
description: Use when deciding whether a project is a strong AAAI submission across its broad AI scope, should be reframed or routed to a dedicated track such as AI for Social Impact or AI Alignment, or should instead go to IJCAI, NeurIPS, ICML, ICLR, AISTATS, UAI, ACL, CVPR, KDD, CHI, ICRA, or another specialist venue.
---

# AAAI Topic Selection

Use this while the project is still movable. AAAI is broad across artificial intelligence, so a
strong submission should make an AI contribution that is intelligible beyond a narrow subfield.

## Strong AAAI signals

- Clear AI problem and contribution: method, theory, system, benchmark, dataset, evaluation, social
  impact, alignment, human-AI interaction, planning, reasoning, learning, NLP, vision, robotics, or
  knowledge representation.
- Evidence that supports a general AI claim, not only a local application result.
- Responsible treatment of ethics, safety, privacy, fairness, social impact, or misuse when the
  paper touches those areas.
- Reproducibility path strong enough for checklist scrutiny.
- Narrative clear enough for Phase 1 reviewers from adjacent AI areas.

## Weak AAAI signals

- Pure application deployment with little AI insight.
- Benchmark bump without mechanism, analysis, or robust comparison.
- Closed system with no reviewable evidence.
- Paper better framed as statistics, NLP, vision, HCI, robotics, or systems for a specialist venue.
- Policy-sensitive claims with thin ethics or stakeholder analysis.

## Routing logic

- Prefer IJCAI for broad AI work with an international AI community emphasis.
- Prefer NeurIPS, ICML, or ICLR for stronger ML method/theory or representation-learning framing.
- Prefer AISTATS or UAI for statistics, uncertainty, causal, or probabilistic emphasis.
- Prefer ACL, CVPR, KDD, CHI, ICRA, or systems venues when the contribution is domain-specific.
- Prefer a workshop if evidence is preliminary but the idea is timely.

## Fit-versus-route table

AAAI's breadth is an asset only when the contribution reads as general AI, not a narrow benchmark
result. Use the dominant signal to decide between AAAI and a specialist venue.

| Project shape | AAAI fit | Better route if not |
| --- | --- | --- |
| New planning or KR mechanism | strong, core AAAI turf | UAI for pure uncertainty |
| ML method with broad insight | plausible | NeurIPS/ICML for deep theory |
| Domain deployment, thin AI | weak | KDD, CHI, or ICRA |
| Stakeholder-facing impact work | strong via AI for Social Impact | domain policy venue |

## Broad-AI contribution stress test

Before routing to AAAI, rewrite the project in three forms. If any form collapses into a dataset name
or a leaderboard delta, the submission needs reframing or a specialist venue.

| Stress-test form | Strong answer | Weak answer |
| --- | --- | --- |
| One-sentence AI problem | names a general reasoning, learning, planning, representation, evaluation, alignment, or human-AI problem | names only an application domain |
| Contribution type | method, theory, benchmark, dataset, evaluation, system, social-impact analysis, or alignment intervention | "we apply model X to task Y" |
| Transfer argument | explains why the insight should matter across tasks, models, settings, or stakeholders | only says one benchmark improves |
| Evidence shape | mechanism, ablation, comparison, human/stakeholder evidence, or formal result tied to the claim | one table with no diagnostic support |
| Limitation | states where the approach should not be expected to work | hides the narrowness until the appendix |

If the strong answer is hard to write, do not force AAAI fit. Route the paper to the community whose
reviewers naturally value the main evidence: ML method/theory, uncertainty/statistics, NLP, vision,
robotics, HCI, systems, or the application domain.

## Route decision ledger

Keep a short ledger for borderline projects. It should contain:

- **Dominant contribution:** the one contribution type the paper wants to be judged on.
- **Primary reviewer:** the AAAI-adjacent reviewer who can fairly evaluate it.
- **Secondary reviewer:** the cross-area reviewer who must still understand the first page.
- **Must-have evidence:** the result, theorem, ablation, artifact, user/stakeholder evidence, or
  benchmark analysis without which AAAI fit fails.
- **Better venue if missing:** the specialist venue that becomes stronger if the must-have evidence
  cannot be added before submission.

Use the ledger to prevent ambiguous framing such as "AAAI because it is broad" or "specialist venue
because reviewers will know the dataset." Broad scope is useful only when the claim is stated at the
right abstraction level.

## Worked vignette

A team has a fairness-aware allocation system for a city service. The AI insight is a constraint
formulation, and the stakes are social. Walking the signals: the contribution generalizes beyond the
one city (strong signal) and is policy-sensitive (needs stakeholder evidence). Verdict: AAAI fit is
strong, routed to AI for Social Impact rather than the Main Track, with harm and stakeholder analysis
treated as required evidence, not an afterthought.

## Output format

```text
[AAAI fit] strong / plausible / weak / no
[Track route] Main / AI for Social Impact / AI Alignment / other
[Core AI contribution] <one sentence>
[Evidence required] <experiment, theory, artifact, stakeholder analysis>
[Best venue route] AAAI / IJCAI / NeurIPS / ICML / ICLR / AISTATS / UAI / domain venue
```
