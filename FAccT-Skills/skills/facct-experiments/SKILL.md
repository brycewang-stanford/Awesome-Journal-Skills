---
name: facct-experiments
description: Use when designing or auditing ACM FAccT empirical work — quantitative fairness audits with disaggregated metrics and fair baselines, qualitative and participatory studies with coding and reflexivity, mixed-methods designs, sound handling of protected attributes and proxies, consent and IRB for human-subjects and community-facing work, and matching evidence to the shape of a fairness/accountability/transparency claim.
---

# FAccT Experiments

Use this before submission when the empirical story is not yet locked. FAccT evidence is **not
leaderboard evidence**: the reviewer pool asks whether your study actually shows the *harm,
disparity, accountability gap, or transparency effect* you claim, on the *people* you claim it for,
with methods honest about their limits. The organizing principle is **evidence proportional to the
claim** — and because FAccT is interdisciplinary, "evidence" can be a disaggregated statistical
audit, a coded interview corpus, a participatory study, or a documented case, each held to its own
field's standard of rigor.

## Evaluation audit

- **Match evidence to the claim shape.** A claim about *disparate harm* needs **disaggregated**
  results by subgroup, not aggregate accuracy; a claim about *how affected people experience* a
  system needs qualitative or behavioral data from those people; a claim about *accountability*
  needs the institutional/process evidence, not a metric.
- **Disaggregate, and defend the groups.** Report metrics per protected/affected subgroup with
  uncertainty. State how group membership was defined and measured — proxies for race, gender,
  disability, or income carry construct-validity risk you must name and bound.
- **Choose fair baselines and fair comparisons.** For a fairness method, compare against the
  strongest prior fairness intervention *and* the do-nothing baseline, with an equal, documented
  budget; for an audit, compare against the vendor's own claims or a documented ground truth.
- **Hold qualitative work to method.** Coding schemes, inter-coder agreement where appropriate,
  saturation, an audit trail, and **reflexivity** about the researchers' standpoint — qualitative
  rigor is first-class at FAccT, not a soft option.
- **Treat human subjects and communities with care.** Document consent, IRB/ethics approval or its
  considered absence, compensation, data minimization, and how you avoid re-identifying or
  re-harming the people in your data — this is scored, and it feeds the Ethical Considerations
  statement.
- **Design harms and limits in, not on.** Know before you run which populations you cannot speak
  for and which disparities your instrument might miss, and instrument to surface them.

## Claim-to-evidence design table

| FAccT claim | Matching evidence | Reject pattern avoided |
|---|---|---|
| "System X harms group G more" | Disaggregated error/outcome metrics by G, with CIs, on real data | "Aggregate accuracy hides the subgroup gap" |
| "Our method reduces the disparity" | Gap before/after vs. a tuned fairness baseline + the accuracy cost | "Fairness improved, utility cost never reported" |
| "Affected people cannot contest decisions" | Interviews/observation with those people, coded and reflexive | "Researcher speculation stands in for lived experience" |
| "This documentation improves transparency" | A study of whether real users act differently with it | "Assumed usefulness; never tested with a reader" |
| "The proxy is valid for the protected attribute" | Validation of the proxy against ground truth, error stated | "Proxy treated as truth; construct threat ignored" |

## Handling protected attributes and proxies

```text
[Definition]   state how each group is defined; whose categories are these, and who is erased by them?
[Measurement]  is the attribute observed, self-reported, or inferred? report proxy error and bias
[Intersection] test intersectional subgroups where numbers allow; note where they are too small
[Consent]      do the people classified know and agree? document the ethics basis
[Missingness]  who is absent from the data entirely, and how does that bound the claim?
```

## Mixed-methods and participatory rigor

- Say **why** each method is present and what it does that the other cannot — triangulation, not
  decoration.
- For participatory or community-based work, document how the community shaped the questions, how
  findings return to them, and how power was handled — FAccT reviewers include people who do this
  seriously.
- Report negative and disconfirming evidence; a study that only confirms the authors' prior reads
  as advocacy, not research.

## Vignette: auditing a hiring model

A paper claims a screening model disadvantages a protected group. The matching plan: obtain or
construct a realistic labeled dataset with documented provenance; report selection/error rates
**disaggregated** by group and intersection with confidence intervals; validate the group proxy and
state its error; compare against the vendor's fairness claim; audit a sample of individual cases
qualitatively for face validity; document the consent/ethics basis for using the data; and state
plainly which populations the audit cannot speak to — every number traceable to a logged analysis in
the supplementary material.

## Statistical and methodological floor

- Uncertainty (CIs or equivalent) on every disaggregated comparison; multiple-comparison awareness
  across subgroups.
- For qualitative work: the coding scheme, agreement or a defense of a single-coder design, and the
  interview/observation protocol.
- The compute, data scale, and — for any human-subjects component — the sample and recruitment, not
  vague feasibility language.

## Output format

```text
[Evaluation readiness] strong / adequate / weak
[Claim -> evidence map] <claim: population / metric-or-method / uncertainty>
[Disaggregation] <groups reported? proxy validity stated? intersections where possible?>
[Ethics basis] <consent / IRB / compensation / re-harm avoidance documented? yes/no>
[Qual rigor] <coding / agreement / reflexivity present where relevant? yes/no>
[Decision-critical next run] <one study extension or analysis>
```
