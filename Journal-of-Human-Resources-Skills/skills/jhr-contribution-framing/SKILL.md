---
name: jhr-contribution-framing
description: Use when sharpening the Journal of Human Resources (JHR) contribution claim around applied microeconomics, credible design-based evidence, public-policy relevance, magnitudes translated into natural human-capital units, and explicit reconciliation with prior published estimates.
---

# Contribution Framing (jhr-contribution-framing)

## When to trigger

- The paper has credible estimates but the JHR contribution is not obvious
- The policy lesson is buried
- The manuscript does not explain how it reconciles with prior work

## Contribution formula

```text
We study [policy-relevant empirical-micro question] using [data/design]. Relative
to [closest prior work], we [new variation/data/population/reconciliation] and
show [result with magnitude]. The findings matter for [policy or human-resource
outcome in the economics sense] because [mechanism].
```

## Must include

- Field: labor, education, health, development, discrimination, retirement, or
  adjacent empirical micro.
- Credible design or disciplined descriptive contribution.
- Magnitude and policy relevance.
- Relationship to prior estimates.
- Boundary conditions: population, time, institution, and external validity.

## Reconciliation paragraph

JHR framing is strongest when the contribution paragraph does not merely say "we add evidence." Add a
reconciliation sentence:

```text
Our estimate differs from [prior estimate] because [sample/design/institution/period], and when we
re-estimate the prior specification on [shared sample or comparable sample], the gap narrows/widens in
the predicted direction.
```

If the paper cannot explain why its magnitude differs from prior work, the contribution is vulnerable
even when the design is credible. Route to `jhr-data-analysis` for comparative estimation.

## JHR claim stress test

Before finalizing the introduction, test the claim against four reviewer questions:

- **What is learned about human resources?** Name the labor, education, health, family, retirement,
  inequality, discrimination, or development margin in economics terms.
- **Why is the estimate credible?** State the design feature in one sentence without jargon.
- **Why is the magnitude meaningful?** Translate the coefficient into dollars, months, percentile points,
  employment probability, schooling units, or another natural policy unit.
- **Why does it differ from prior work?** Identify whether the difference is design, sample, institution,
  period, outcome construction, or policy context.

If the answer to any question requires an appendix table to be intelligible, the main contribution
paragraph is not yet ready for JHR.

## Magnitude translation menu

JHR contribution claims land when the coefficient is restated in the natural
unit of the field, paired with a benchmark such as the control mean, cost per
treated unit, or the closest prior estimate:

- **Labor**: percentage-point employment changes, log wages converted to annual
  dollars, weeks of unemployment duration.
- **Education**: test-score standard deviations, completion or enrollment
  percentage points, years of attainment.
- **Health**: per-1,000 birth outcomes, coverage points, utilization counts.
- **Retirement**: months of claiming delay, replacement-rate points.
- **Development**: schooling years, height-for-age, household consumption.

A claim like "enrollment rose 4.2 percentage points off a 31 percent base,
comparable to halving posted tuition" is doing the venue's work for the reader.

## Worked vignette: tuition-waiver framing

Illustrative paper: staggered adoption of community-college tuition waivers
across 23 states, 2014-2019, linked administrative enrollment and earnings
records, Callaway-Sant'Anna ATT. All numbers are placeholders for the pattern.

- Draft claim: "We study the effect of tuition waivers on enrollment." Too thin
  for JHR — no magnitude, no policy unit, no reconciliation.
- Reframed claim: "Waivers raise first-time enrollment by 4.2 percentage points
  (13 percent of base), concentrated in the bottom family-income quartile; prior
  cross-state OLS estimates near 1 point understate the effect because
  non-adopting states were already trending upward."
- Boundary sentence: identified for adopting states' public two-year systems;
  spillovers to four-year colleges are bounded, not estimated.

## Desk-screen contribution risks

| Draft symptom | Why JHR balks | Repair |
|---|---|---|
| "First to study X in setting Y" | Setting novelty alone is not a contribution | Say what the new variation identifies that prior settings could not |
| Sign-and-significance summary | JHR wants magnitudes a policymaker can use | Translate to natural units with a benchmark |
| No prior-estimate sentence | Misses the reconciliation expectation | Add the bridge sentence and cite the comparative table |
| Policy claim broader than the estimand | External-validity overreach flagged by referees | Scope to compliers or adopters and state what does not travel |

## Output format

```text
[One-sentence contribution] ...
[Policy relevance] ...
[Prior-work reconciliation] ...
[Magnitude] ...
[Boundary] ...
[Next step] jhr-tables-figures
```
