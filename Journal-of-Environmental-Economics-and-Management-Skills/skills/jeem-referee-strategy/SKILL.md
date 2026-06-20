---
name: jeem-referee-strategy
description: Use when pre-empting the objections a Journal of Environmental Economics and Management (JEEM) referee will raise — the environmental-economist's reflexes on sorting, spatial SEs, leakage, hypothetical bias, and scope — before submission or in an R&R. Anticipates and defuses pushback; it does not replace the rebuttal letter (jeem-rebuttal).
---

# Referee Strategy (jeem-referee-strategy)

## When to trigger

- The paper is near submission and you want to find the holes a field referee will hit first
- A coauthor asks "what will the referees attack?" on a hedonic, DiD, or valuation paper
- You need to decide which robustness checks to put in the main text vs. appendix to pre-empt referees
- An R&R is coming and you want to model the two-referee-plus-editor dynamic before drafting responses

## The self-review pass before submission

Before submitting, read your own paper as a hostile field referee for one hour and write the report you fear. The exercise surfaces the objections the writing has trained you to skip: the buffer radius you never justified, the spatial SEs you computed but buried, the welfare claim that quietly became "total" when the design only identifies "marginal," the recent JAERE paper you half-remember and never cited. Every objection you can pre-answer in the submitted draft is one the actual referee cannot use to send the paper back. This self-review is the cheapest revision round you will ever run.

## Who referees at JEEM

JEEM referees are **environmental and resource economists** — they have run the hedonic, fought the spatial-SE battle, and read the valuation-bias literature. They are reflexively skeptical of (a) causal claims that ignore sorting or spatial confounding, (b) valuation estimates that ignore known biases, (c) welfare numbers that overreach the design, and (d) papers where the environment is decoration. Anticipate the field reflex, not the generic applied-micro reflex.

## The objections to pre-empt by branch

| Branch | The reflexive objection | Pre-empt it by |
|--------|--------------------------|----------------|
| Hedonic / RP valuation | "This is sorting / omitted amenities, not WTP" | quasi-experimental amenity shock, boundary FE, parallel pre-trends in price |
| Stated-preference | "Hypothetical bias / no scope test / protest responses" | incentive-compatible design, explicit scope test, bias calibration, protest handling |
| Regulation DiD | "Staggered TWFE is biased; pre-trends?" | heterogeneity-robust estimator + event-study leads up front |
| Permit market / cap-and-trade | "Leakage and reshuffling flip the welfare sign" | bound leakage; show coverage; address uncovered-source response |
| Weather / climate IV | "This is weather, not climate; adaptation?" | separate short-run shock from long-run expectation; model adaptation margin |
| Any spatial result | "Your standard errors ignore spatial correlation" | Conley SEs with a reported cutoff, in the main text |
| Any welfare claim | "You estimate a reduced form but claim a welfare number" | the model/assumptions that license the welfare mapping (jeem-theory-model) |

## Strategy craft

1. **Put the field's favorite robustness check in the main text, not the appendix.** Spatial SEs and the event-study plot are not optional extras at JEEM — burying them invites the referee to assume you are hiding something.
2. **Concede the design's true limits in the paper.** Naming the boundary of your welfare claim (marginal not total, PE not GE, local not external) disarms the referee who would otherwise score the point.
3. **Anticipate the second referee.** Reviews often pit a methods-focused referee against a policy-focused one; serve both — design credibility *and* a usable policy number.
4. **Map likely cites you missed.** A JEEM referee will know the recent JEEM/JAERE paper on your exact question; engage it before they force you to.
5. **Decide the editor's risk.** Editors desk-screen for scope and style; an environmental mechanism that is not load-bearing is the fastest path to a desk reject — fix that before worrying about referee minutiae.

## Worked vignette (illustrative)

A hedonic paper on Superfund cleanup is going out. Modeling the referees: a field referee will reflexively say "this is sorting, not capitalization" and "your SEs ignore spatial correlation"; a policy referee will ask "what is the implied benefit-cost ratio of cleanup?" The pre-emptive strategy: put the boundary-discontinuity specification and the parallel pre-cleanup price trends in the *main text* (answering R1's sorting reflex), report Conley SEs at two cutoffs in the headline table (answering the spatial reflex before it is raised), and add a benefit-cost paragraph translating the capitalization estimate into cleanup welfare (serving R2). The editor's scope screen is satisfied because the air/soil-quality externality is unmistakably the engine. Each likely objection is answered before it is voiced.

## Reading the editor vs. the referees

At JEEM the editor desk-screens for scope and style, then weighs the referees. Two implications for strategy: first, the **scope screen is the highest-probability rejection**, so a non-load-bearing environmental mechanism must be fixed before any referee subtlety. Second, when referees conflict, the editor's summary letter — not the longer of the two reports — sets the priority; design the paper (and later the rebuttal) around the threat to the *core welfare claim*, which is what the editor protects.

## Checklist

- [ ] Each branch-specific reflexive objection (table above) has a named answer in the paper
- [ ] Spatial SEs and the event-study/RD plot are in the main text, not buried
- [ ] The welfare claim's true limits are stated, not left for a referee to expose
- [ ] The closest recent JEEM/JAERE paper is engaged before a referee names it
- [ ] The paper serves both a methods referee and a policy referee
- [ ] The environmental mechanism is unmistakably load-bearing (desk-reject insurance)
- [ ] Robustness placement (main vs. appendix) chosen to pre-empt, not to hide

## Anti-patterns

- Hiding spatial SEs or the event-study plot in an appendix, inviting suspicion
- Overclaiming welfare (total when only marginal is identified) and waiting to be caught
- Ignoring the obvious recent field paper a referee will know cold
- Answering the generic applied-micro objection while missing the field reflex (sorting, leakage, scope)
- Treating the editor's scope screen as a formality when the environment is decoration

## Suggesting and excluding reviewers

JEEM (via Editorial Manager) typically lets authors suggest and exclude reviewers; use it strategically and honestly. Suggest field economists who work in your specific lineage (hedonics, valuation, regulation, resource dynamics) and would engage the substance — not friends, and not people so close they would be conflicted out. Exclude only with a defensible reason (a direct competitor on the identical question, a known prior rejection). The editor reads these lists as a signal: a thoughtful suggestion list shows you know who the relevant referees are, which itself reinforces that the paper is genuinely in JEEM's field.

## The "so what for policy" referee

Beyond the methods reflex, JEEM referees increasingly ask the policy-relevance question: even a perfectly identified estimate can draw a lukewarm report if the welfare or policy payoff is thin. Pre-empt this by making the regulator-usable number (the efficient tax, the benefit-cost ratio, the optimal quota) explicit and bounded. A paper that nails identification but never says what a policymaker should do differently leaves a referee with nothing to champion.

## Output format

```text
【Journal】Journal of Environmental Economics and Management
【Skill】jeem-referee-strategy
【Branch reflex】top objection for this paper's branch
【Pre-empt】where/how it is answered in the paper (main text?)
【Spatial SEs】in main text? [Y/N]
【Welfare limits】stated honestly? [Y/N]
【Closest field paper】engaged? [Y/N]
【Desk-reject risk】mechanism load-bearing + scope/style compliant? [Y/N]
【Source status】verified URL / 待核实 / not asserted
【Next skill】jeem-submission
```
