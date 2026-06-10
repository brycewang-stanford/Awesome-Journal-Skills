---
name: jhr-topic-selection
description: Use when checking whether a research question fits the Journal of Human Resources (JHR) — empirical microeconomics with a policy-relevant, causal emphasis — and to filter out off-scope "HR management" framings before paying the nonrefundable fee. A fit gate, not an idea generator.
---

# Topic Selection & Scope Fit (jhr-topic-selection)

## When to trigger

- You are choosing a target journal and JHR is a candidate
- The paper's title or framing uses "human resources / HR" language
- You want to confirm a policy-relevant micro question is in scope before submitting
- Deciding whether a descriptive paper is JHR-worthy

## The single most important gate: scope

JHR's **name is misleading.** It is a **leading empirical-microeconomics journal**, founded 1965 at the UW-Madison Institute for Research on Poverty, and it **does NOT consider management or personnel ("HR management") research.** The nonrefundable **$175 fee is not refunded** for out-of-scope papers — so this check has real money attached. If your paper is about firm HR practices, recruitment systems, or organizational behavior, JHR is the wrong venue.

## What JHR actually wants

Empirical microeconomics with a **public-policy** orientation, in one of its core fields:

- **Labor economics** — employment, wages, labor supply, minimum wage, unions
- **Economics of education** — attainment, returns to schooling, school/teacher effects
- **Health economics** — insurance, health behaviors, birth/mortality outcomes
- **Development economics** — household welfare, schooling and health in low-income settings
- **Discrimination** — labor-market and other gaps (audit studies, decompositions)
- **Retirement** — Social Security, claiming, saving, aging

A JHR paper typically pairs a **policy-relevant question** with a **credible empirical design** on real microdata, and draws a lesson a policymaker or applied economist would care about.

## Fit checklist

- [ ] The question is **economics**, not HR-management/organizational behavior
- [ ] It sits in a core JHR field (labor / education / health / development / discrimination / retirement)
- [ ] There is a clear **policy relevance** or first-order applied-micro lesson
- [ ] A **causal design** is available (or the descriptive facts are genuinely new and disciplined)
- [ ] The data can ultimately be deposited (or waivered) under JHR's CC0 policy

## Anti-patterns

- Submitting a "human resource management" paper because the name seems to match
- A narrow within-subfield estimate with no policy lesson
- Theory with no empirical content (JHR is empirical)
- A descriptive paper whose facts are neither new nor policy-relevant

## Borderline calls and how to make them

| Borderline paper | Call | Reasoning |
|---|---|---|
| Personnel economics with firm payroll data, wage-setting question | In scope | Economics question about labor markets, even though the data are firm-side |
| "HR analytics" predicting attrition with ML | Out | Prediction for managers, no economic estimand or policy lever |
| Evaluation of a public workforce-training program | In scope | Classic JHR territory: human-capital policy with a design |
| Survey study of employee engagement and culture | Out | Organizational behavior; redirect to a management journal |
| Structural labor model, no credible variation, no policy counterfactual | Weak fit | JHR's center of gravity is design-based; consider a field journal in structural work |
| New descriptive facts on intergenerational mobility from linked tax data | Plausible | Disciplined, novel description of a first-order policy object can clear the bar |

## Two-paper vignette

- Paper A: county-staggered childcare-subsidy expansion, linked mother-child
  administrative records, event-study evidence on maternal employment and
  child outcomes. Fits JHR on all three axes: field (labor/education), design
  (rollout DID), policy lever (subsidy generosity). Proceed.
- Paper B: "How our talent-acquisition platform reduced time-to-hire" with
  internal firm metrics. The word "human resources" in the title is exactly
  the trap the scope rule exists for — redirect before spending the fee.

## Pre-commitment questions

Before locking JHR as the target, answer in writing:

1. Which JHR field claims this paper, and which recent work in that field is
   the natural shelf neighbor? (Scope lists can shift; confirm against the
   journal's current author guidelines.)
2. What variation will referees test: rollout timing, a cutoff, a lottery, or
   an instrument?
3. Can the data eventually satisfy the CC0 deposit or a defensible waiver?
4. Is the policy lesson statable in one sentence a state legislator's analyst
   could act on?

## Output format

```
【In scope?】empirical micro + policy, not HR-mgmt? [Y/N]
【Field】labor / education / health / development / discrimination / retirement
【Policy lesson】one sentence
【Design available】RCT / RDD / DID / IV / decomposition / descriptive
【Verdict】proceed to jhr-literature-positioning, or redirect venue
```
