---
name: jpam-topic-selection
description: Use when judging whether a research idea fits the Journal of Policy Analysis and Management (JPAM) — a credibly evaluable policy or program question with a decision-relevant takeaway that reaches across economics, political science, and public management. Tests fit and sharpens the question; it does not design the study or run analysis.
---

# Topic Selection & Fit (jpam-topic-selection)

JPAM publishes work that **evaluates real policies and programs** and **informs a real decision**. The
fit bar is two-sided: the question must be **causally answerable** with a credible design *and*
**policy-relevant** in a way an APPAM audience (economists, political scientists, public-management
scholars, and practitioners) recognizes. A clever identification with no policy stake is off-fit;
so is an urgent policy question with no path to a credible estimate.

## When to trigger

- Choosing among ideas for a JPAM submission
- A reviewer or colleague said the paper is "interesting but not really policy"
- Deciding whether the work is a Feature Article or a shorter type (Policy Insights / Retrospective)
- Unsure whether JPAM or a field journal (economics / political science / public administration) is the home

## The JPAM fit test

1. **Name the policy or program.** What concrete intervention, rule, or reform is being evaluated?
   "The effect of X policy on Y outcome" — not "the determinants of Y."
2. **Name the decision.** Who acts differently if the finding is true — a legislator, agency, program
   designer, funder? State the counterfactual policy choice.
3. **Name the credible design.** Is there real exogenous variation (random assignment, an eligibility
   threshold, a staggered rollout, a policy discontinuity, a plausible instrument)? If not, the idea
   may not clear JPAM's identification bar.
4. **Name the cross-field stake.** Why would a reader outside the home subfield (e.g., a political
   scientist if you are an economist) care? JPAM rewards questions that bridge disciplines.
5. **Name the magnitude that matters.** What effect size would change the decision? This anchors power
   and later the cost-benefit framing.

## Field coverage (any of these is in scope)

Education, health, labor & welfare, housing, crime & justice, environment & energy, immigration, social
policy, public finance, program administration. Domestic **and** international policy are both in scope.

## Article-type fit

| If the work is… | Type | Note |
|-----------------|------|------|
| A full, credibly identified evaluation | Feature Research Article | the core of the journal |
| A short, timely, decision-relevant take | Policy Insights (≤ 3,000 words, not peer-reviewed) | confirm invitation/rules (检索于 2026-06) |
| A methods advance for policy analysts | Methods for Policy Analysis | route to `jpam-research-design` |
| A reflective look back at a policy/literature | Policy Retrospective | route to `jpam-theory-building` |

## Checklist

- [ ] A specific policy/program named, not a vague correlate
- [ ] A concrete decision the evidence informs, with the policy counterfactual stated
- [ ] A credible source of identifying variation exists (not just controls)
- [ ] A cross-disciplinary stake an APPAM reader recognizes
- [ ] A decision-relevant magnitude defined up front
- [ ] Correct article type chosen; home-journal check vs. econ/PS/PA siblings done

## Anti-patterns

- "Determinants of" descriptive work with no policy lever (off-fit for a Feature Article)
- A pure methods or pure theory paper with no policy application (likely a field-journal fit)
- Policy relevance asserted in the abstract but never tied to an actual decision or counterfactual
- Choosing JPAM because the econ field journals rejected it, with no policy reframing
- Treating "topical" as "policy-relevant" — timeliness is not the same as decision relevance

## Worked micro-example (illustrative)

"The determinants of college enrollment" is off-fit — descriptive, no lever. Reframed as *"Does a
state's automatic-FAFSA-completion mandate raise enrollment among low-income students, and at what cost
per additional enrollee?"* it names a **policy** (the mandate), a **decision** (whether other states
should adopt it), **identifying variation** (staggered state adoption → heterogeneity-robust DiD), a
**cross-field stake** (mobility for economists, administrative-burden for public-management readers), and
a **magnitude that matters** (an effect large enough to justify the administrative cost). That is a JPAM
Feature Article. (Policy/numbers illustrative.)

## Calibration anchors (hedged)

- "Timely" is not "decision-relevant" — a topic in the news still needs a concrete decision and a
  credible design to fit a Feature Article.
- If the only path is selection-on-observables, the idea may not clear JPAM's identification bar; look
  for exogenous variation before committing.
- When in doubt between JPAM and a field journal, ask which referee pool the contribution needs: if it
  needs a policy reader as much as a method reader, it is a JPAM paper.

## Output format

```
【Policy / program】the intervention being evaluated
【Decision informed】who acts differently, and the counterfactual
【Identifying variation】RCT / DiD / RD / IV / synthetic control / none-yet
【Cross-field stake】why a reader outside the subfield cares
【Article type】Feature / Policy Insights / Methods / Retrospective
【Next】jpam-literature-positioning
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — policy data sources by field (education, health, labor, crime, housing)
- [`../../resources/exemplars/library.md`](../../resources/exemplars/library.md) — real JPAM papers by field × method to calibrate fit
