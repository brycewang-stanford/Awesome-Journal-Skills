---
name: chi-experiments
description: Use when designing or auditing the studies behind an ACM CHI paper — matching evidence shape to contribution type, powering quantitative experiments, making qualitative work rigorous and auditable, reporting participants and ethics properly, and avoiding the ADR-Data and ADR-Method screening grounds.
---

# CHI Experiments and Studies

"Experiments" at CHI means human evidence: controlled lab studies, field deployments,
interview and diary studies, surveys, log analyses, and mixtures of these. Two of the
four assisted desk-reject rubric grounds CHI now screens with — **ADR-Data** (grossly
insufficient data for the claims) and **ADR-Method** (grossly insufficient
methodological detail or transparency) — are study-design judgments made *before full
review*. Evidence design is therefore survival, not polish.

## Match the evidence to the claim, not to habit

| Claim shape | Evidence that convinces CHI reviewers | Chronic mismatch seen in reviews |
|---|---|---|
| "Technique X outperforms Y" | Controlled comparison, counterbalanced, powered, effect sizes | Underpowered n=12 with p-values only |
| "Users experience/need Z" | Interviews or diary study to saturation, systematic analysis | Cherry-picked quotes, no analysis method stated |
| "System S is usable/useful in practice" | Field deployment with real tasks over time | One-hour lab walkthrough of a demo |
| "Population P interacts differently" | Sampling strategy that can reach P, comparative design | Convenience sample of students standing in for P |
| "Design guideline G holds" | Multiple probes/instantiations, triangulated methods | Single prototype, single context, universal claim |
| "Measure M captures construct C" | Validation study: reliability, convergent validity | New questionnaire used, never validated |

Mixed methods are a CHI signature: a quantitative result explains *that*, the paired
qualitative strand explains *why*. If you run both, integrate them in the analysis —
a qualitative section bolted after the ANOVA reads as decoration.

## Quantitative discipline

- **Power before running.** Decide the smallest effect worth detecting, then size the
  study; report the analysis. Post-hoc power excuses convince nobody.

```python
# a priori sample size for a within-subjects comparison (paired t-test)
from statsmodels.stats.power import TTestPower
n = TTestPower().solve_power(effect_size=0.5, alpha=0.05, power=0.8,
                             alternative="two-sided")
print(round(n))   # ≈ 34 participants for d=0.5 — n=12 detects only d≈0.88
```

- Report **effect sizes with confidence intervals** alongside test statistics; CHI's
  methods community has campaigned against naked p-values for a decade.
- State the analysis plan's provenance: preregistered, planned-but-unregistered, or
  exploratory. Label exploratory findings as such instead of promoting them.
- Check assumptions (normality, sphericity) and name the corrections used; Likert
  and time data routinely need non-parametric or transformed treatment.
- Counterbalance and report order effects for within-subjects interaction studies.

## Qualitative discipline

Qualitative work at CHI is judged on rigor, not sample size. What reviewers audit:

- The **named analysis method** actually followed — reflexive thematic analysis,
  grounded-theory procedures, interaction analysis — with its own reporting
  conventions honored (e.g., do not report inter-rater reliability for reflexive TA
  while claiming a codebook emerged from consensus; pick a coherent paradigm).
- **Recruitment, who the participants are, and what they were paid**, in a table.
- Enough **quote evidence per theme** to show the theme is in the data, attributed
  with participant IDs (P1–Pn), balanced across participants.
- **Researcher positionality** where the topic makes the researcher's standpoint
  analytically relevant (common in accessibility, health, and marginalized-community
  work) — a norm in parts of CHI, not a universal requirement.

## Participants and ethics are results-page material

CHI reviewers read the participants section as evidence, and screening cites it:

1. Recruitment channel and criteria; compensation and its local adequacy.
2. Ethics approval (IRB or equivalent) named, or the honest statement of why the
   jurisdiction requires none — plus consent procedure for data, recordings, and
   any footage reused in the video figure (`chi-supplementary`).
3. Demographics reported to the level the claims need: an accessibility claim needs
   disability descriptions; a cross-cultural claim needs more than "US and EU".
4. Risks and mitigations for sensitive topics; deception disclosed and debriefed.
5. Data handling: anonymization, storage, deletion timeline.

## Deployment and AI-system studies

For field deployments, report duration, retention, and usage telemetry honestly —
attrition is data. For AI-infused interfaces, evaluate both the model and the human
experience: state model version, prompts/configurations, and failure behavior during
the study window, because "users trusted the system" is uninterpretable without
knowing how often the system was wrong. Pin model versions; a study run on a moving
API is unreplicable by construction (`chi-reproducibility`).

## Pre-submission evidence audit

Walk each headline claim backwards: which figure/table/theme supports it, from which
data, collected from whom, analyzed how? Any claim that dead-ends is either cut,
scoped down ("in our lab task, for our participants..."), or flagged as future work.
This single pass defuses most ADR-Data exposure.

## Output format

```text
[Contribution type] <from chi-topic-selection>
[Evidence inventory] <study 1: design, n, analysis> · <study 2: ...>
[Claim-evidence dead ends] <claims without support, or none>
[Quant status] power: <basis> / effect sizes+CIs: yes/no / plan provenance: prereg|planned|exploratory
[Qual status] method named+followed: yes/no / quotes balanced: yes/no
[Ethics] approval: <body or n/a+reason> / compensation: <amount> / consent for footage: yes/no
[ADR exposure] Data: low/med/high · Method: low/med/high — <weakest point>
```
