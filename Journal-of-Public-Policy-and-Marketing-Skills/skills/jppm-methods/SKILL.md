---
name: jppm-methods
description: Use when choosing and designing the evidence for a Journal of Public Policy & Marketing (JPP&M) manuscript — experiments with policy-realistic stimuli, quasi-experimental policy evaluation (DiD, RDD, synthetic control), surveys, field data, or meta-analysis. Designs the studies; it does not estimate them (jppm-data-analysis).
---

# Methods & Evaluation Design (jppm-methods)

## When to trigger

- Deciding whether the question needs an experiment, a policy evaluation, a survey, or a synthesis
- A policy rolled out and you must find a credible counterfactual before claiming impact
- Your label/disclosure experiment uses stimuli no agency could ever mandate
- The sample excludes the very population the policy is meant to protect
- You are combining lab and field evidence and need the pieces to carry distinct weight

## Methodological pluralism, disciplined by the policy question

JPP&M accepts a wider methods palette than most marketing journals — randomized experiments, quasi-experimental evaluation, surveys, field and archival data, meta-analysis, qualitative work — but the choice must follow from the **policy inference** required. Two questions dominate: *Would the proposed instrument work?* (prospective — usually experiments with realistic stimuli) and *Did the enacted instrument work?* (retrospective — evaluation designs with explicit counterfactuals). A submission that answers the retrospective question with before/after trends, or the prospective one with fantasy stimuli, fails regardless of statistical polish. Missing counterfactual reasoning in an evaluation design is one of this journal's known desk-reject patterns.

## Prospective designs: policy-realistic experiments

- **Mandatable stimuli.** Test warning/label/disclosure formats an agency could actually require — real estate on a package, formats from the live rulemaking (e.g., FDA front-of-package proposals), not a full-screen banner no rule would compel.
- **Treatment contrasts = decision options.** Conditions should map to the regulator's choice set (status quo vs. proposed rule vs. stricter alternative), so each pairwise contrast answers a decision.
- **Consequential outcomes.** Choice with real stakes, purchases, incentivized behavior — self-reported intentions alone are weak currency for a claim that a rule will change behavior.
- **Policy-relevant samples.** Recruit the protected population (smokers for tobacco warnings, low-income households for financial disclosures, parents for children's marketing). A student panel cannot carry a vulnerability claim; when using Prolific/CloudResearch, screen and quota accordingly.
- **Marketplace noise.** Add realistic competing information (cluttered shelf, competing claims); effects that survive noise are the ones that survive markets.

## Retrospective designs: evaluation with a counterfactual

| Design | Use when | JPP&M-specific cautions |
|--------|----------|-------------------------|
| Difference-in-differences | policy adopted in some states/markets/categories, not others | staggered adoption needs heterogeneity-robust estimators; argue parallel trends behaviorally, not just visually |
| Regression discontinuity | eligibility threshold or size cutoff assigns exposure | check manipulation at the cutoff (firms sort!); effects are local to the threshold |
| Synthetic control | one large unit treated (a city soda tax, a national ban) | pre-period fit and placebo runs are the argument |
| Event study | timing of enforcement/announcement is sharp | anticipation by firms and media coverage blur the event date |
| Interrupted time series | no untreated comparison exists at all | weakest option; state so and bound the claims |

Firms' strategic responses are both a threat and a finding: reformulation, pre-emptive compliance, or channel-shifting can contaminate the comparison group — design to detect it (untreated outcomes, supply-side data) rather than assume it away.

## Surveys, qualitative work, and synthesis

- **Surveys** earn their place for constructs no archive holds (perceived deception, privacy concern, financial anxiety) — use validated scales and probability or well-quota'd samples when claims are population-level.
- **Qualitative designs** are welcome for vulnerable populations whose experience frames the policy problem; document access, consent, and IRB care to a higher standard, and avoid designs that further burden participants.
- **Meta-analysis** suits mature streams (warning-label effects, disclosure formats); code moderators the regulator controls (format, placement, dose).

## Checklist

- [ ] The design answers the paper's policy question (prospective vs. retrospective) directly
- [ ] Experimental stimuli are mandatable and conditions map to the regulator's choice set
- [ ] The sample includes the population the policy targets; vulnerable groups are powered, not token
- [ ] Evaluations name the counterfactual and the assignment mechanism explicitly
- [ ] Firm strategic response is measured or ruled out, not assumed absent
- [ ] Ethics/IRB treatment matches the sensitivity of the population studied
- [ ] Pre-registration or a pre-analysis plan is in place for confirmatory studies

## Anti-patterns

- **Before/after theater**: a pre/post trend presented as policy impact with no comparison group
- **Fantasy stimuli**: disclosure formats no agency could mandate, generalized to regulation
- **Convenience-sample vulnerability claims**: conclusions about protected groups from panels that exclude them
- **Intentions-only evidence** for behavior-change claims
- **One-method dogma**: forcing an experiment onto a question that demands field variation, or vice versa
- **Sorted cutoffs**: an RDD where firms demonstrably manipulate the threshold, unexamined

## Output format

```text
【Policy question type】prospective (would it work) / retrospective (did it work)
【Design】experiment / DiD / RDD / synthetic control / survey / meta-analysis / qualitative
【Counterfactual】comparison group + assignment logic (retrospective) or control condition logic (prospective)
【Stimuli & sample】mandatable formats; policy-target population included
【Firm response plan】how strategic reactions are detected or bounded
【Next skill】jppm-data-analysis
```
