---
name: aej-economic-policy
description: Use when targeting American Economic Journal: Economic Policy or deciding whether a policy-relevant applied economics manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# American Economic Journal: Economic Policy (aej-economic-policy)

## Journal positioning

AEJ: Economic Policy is the American Economic Association's field home for policy-relevant applied economics one tier below AER's general-interest bar. It publishes credible evaluations of public, health, education, environmental, and tax/transfer policy — work where the identification is sound and the magnitudes speak directly to a policy question. The contribution is the policy lesson backed by clean causal evidence; this is the home for excellent policy-evaluation papers that are narrower than an AER general-interest swing.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the AEA site and the editorial-manager submission system.

## When to trigger

- The author names AEJ: Policy as the target, or is stepping down from an AER policy submission.
- A paper credibly evaluates a policy — tax, transfer, regulation, public program, health, education, environment — with policy-relevant magnitudes.
- A strong applied paper has a clear policy reading and needs a venue that prizes policy relevance plus identification.
- The author needs AEJ: Policy's desk-reject risks and a credible AER / public-economics alternative list.

## Scope & topic fit

- Public economics and the design/evaluation of taxes, transfers, social insurance, and public programs.
- Health, education, and environmental/energy policy evaluation with credible identification.
- Regulation, market design in the public interest, and the distributional and welfare consequences of policy.
- Applied work where the policy question and its quantitative answer are the contribution, not a methodological novelty.

## Method & evidence bar

- Identification plus policy relevance is the joint filter: the design (RCT, DiD, IV, RDD, bunching) must be credible and the estimated effects must map onto a real policy parameter.
- Modern estimators and inference are baseline — proper DiD under staggered policy adoption, valid instruments, RDD diagnostics, correct standard errors.
- Magnitudes must be interpreted in policy terms (cost-effectiveness, welfare, incidence, behavioral responses), not left as significant coefficients.
- Data and code transparency is mandatory; the AEA data and code availability and verification policy applies, with deposit checked before acceptance.

## Structure & house style

- The introduction states the policy question, the identification, the headline effect and its policy-relevant magnitude, and the lesson for policy design.
- Lead with the design and the policy-relevant estimate; develop welfare/distributional implications and mechanisms as support, with secondary analyses in an online appendix.
- AEJ uses an unstructured abstract and JEL codes; robustness and supplementary tables belong in the appendix.
- Exhibits should report magnitudes in interpretable units and connect estimates to the policy counterfactual.

## Official-submission checklist

- Search the live site for "AEJ: Economic Policy submission guidelines" and the AEA "Data and Code Availability Policy," and follow the current versions.
- Re-check the submission fee, formatting, abstract/JEL, anonymization, and figure/table standards on the editorial-manager system.
- Re-check the current data/code deposit and verification workflow (openICPSR / AEA Data Editor), and for experiments any pre-registration / pre-analysis-plan expectations — enforced before acceptance.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the policy question and why the answer matters for policy design.
- [ ] The contribution is stated as identification + policy-relevant magnitude, not as statistical significance.
- [ ] The introduction positions the paper against the recent policy-evaluation frontier on this question.
- [ ] Identification threats are addressed by design; magnitudes are interpreted in welfare/incidence/cost terms.
- [ ] Data and code are ready for the AEA availability + verification workflow.

## Common desk-reject triggers

- A policy "evaluation" with weak or correlational identification.
- Naive TWFE on staggered policy adoption, weak IV, or RDD without density/covariate diagnostics.
- Significant effects with no policy-relevant magnitude, welfare reading, or design lesson.
- A descriptive policy commentary with no credible causal evidence.

## Re-routing decision

- General-interest policy importance → `american-economic-review`; one crisp policy result → `aer-insights`.
- Core public-economics field-leading → `journal-of-public-economics`; European policy-debate framing → `economic-policy`.
- Applied micro where design (not policy) is the headline → `aej-applied-economics`; careful measurement / shorter → `review-of-economics-and-statistics`.
- Field-specific policy → the relevant top field journal (`journal-of-health-economics`, `journal-of-environmental-economics-and-management`, `journal-of-labor-economics`).

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] American Economic Journal: Economic Policy
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the identification + policy-relevant magnitude clear the bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission system / fee / JEL / data-code policy / pre-registration>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
