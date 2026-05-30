---
name: information-systems-research
description: Use when targeting Information Systems Research (ISR) or deciding whether an information-systems behavioral / economic / design-science manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Information Systems Research (information-systems-research)

## Journal positioning

Information Systems Research (ISR) is INFORMS's flagship IS journal and a member of the AIS Senior Scholars' Basket of eight. It publishes rigorous IS research across behavioral, economic, and design-science traditions, often with a strongly quantitative or economic orientation reflecting its INFORMS lineage. Like MISQ it demands a genuine theoretical contribution to IS, but its center of gravity tilts toward analytical models, econometric identification, and quantitative design-science. The readership is the quantitative IS research community.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the INFORMS / ISR site and the editorial submission system.

## When to trigger

- The author names ISR (or the AIS Senior Scholars' Basket / INFORMS IS flagship) as the venue.
- A quantitative or economic IS paper — econometric, analytical-modeling, or quantitative design-science — needs an IS flagship.
- A behavioral IS paper with strong measurement needs an INFORMS-audience home.
- The author needs ISR's desk-reject risks and a credible Basket / INFORMS alternative list before submitting.

## Scope & topic fit

- Economics of IS: digital platforms, online markets, network effects, IT business value, pricing of digital goods.
- Econometric / quantitative behavioral IS: technology use, digital behavior, social media, and online communities with identification.
- Design science with a quantitative or analytical evaluation; IT artifact design with prescriptive theory.
- Analytical modeling of IS phenomena (information economics, security, privacy, recommendation, platform design).

## Method & evidence bar

- A genuine IS theoretical contribution is required; technical sophistication alone does not suffice.
- Econometric work needs credible identification (DiD/IV/RDD/experiments), proper inference, and robustness; field experiments are valued.
- Analytical models need correct, non-trivial results with proofs and an IS insight.
- Behavioral work needs validated constructs, adequate power, and attention to common-method bias; design-science needs rigorous evaluation.

## Structure & house style

- The introduction frames the IS problem, the contribution, and the identification or model early, for a quantitative readership.
- Models and proofs (or identification arguments) are central; robustness, derivations, and instruments go to an electronic companion / online appendix.
- Results report economic or behavioral magnitudes and interpret them, not only significance.
- The discussion states the IS theoretical contribution and boundary conditions.

## Official-submission checklist

- Search the live site for "Information Systems Research submission guidelines / author instructions" and follow the current INFORMS version, including area/department scope.
- Re-check formatting, abstract length, anonymization/double-blind policy, and reference style.
- Re-check the current data and code availability / reproducibility policy and electronic-companion rules.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the IS theoretical contribution for a quantitative audience.
- [ ] The contribution is stated as identification / model result / mechanism, not predictive accuracy or significance.
- [ ] Identification or proofs are complete; robustness/derivations live in the electronic companion.
- [ ] Constructs (if behavioral) are validated; magnitudes are reported and interpreted.
- [ ] Abstract, anonymization, references, and data/code policy match the current ISR guide.

## Common desk-reject triggers

- An analytics/ML application with no IS theoretical contribution.
- An econometric paper with endogeneity and no credible source of variation.
- An analytical model that is correct but offers no IS insight, or has implausible assumptions.
- A paper that is really economics, CS, or marketing framed as IS.

## Re-routing decision

- IS contribution that is more behavioral/qualitative or design-theory-led → `mis-quarterly`.
- Theory-rich, methodologically broad IS for the AIS flagship → `journal-of-the-association-for-information-systems`.
- Management-of-IS, IT business value, IS strategy → `journal-of-management-information-systems`.
- Broad quantitative management → `management-science` (IS department); computational/ML-for-OR with no IS theory → `informs-journal-on-computing`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Information Systems Research
[Topic tags] <2–3 closest topics + genre: econ/behavioral/DSR>
[Method/evidence] <does the identification or model + IS contribution clear ISR's bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission system / blinding / electronic companion / data-code>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
