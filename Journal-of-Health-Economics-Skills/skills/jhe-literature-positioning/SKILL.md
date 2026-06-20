---
name: jhe-literature-positioning
description: Use when the contribution of a Journal of Health Economics (JHE) manuscript relative to the health-economics frontier is fuzzy or undersold. Stakes the marginal contribution against the right health-econ literatures; it does not run the analysis or invent citations.
---

# Literature Positioning (jhe-literature-positioning)

## When to trigger

- A referee or coauthor cannot state in one sentence what this paper adds beyond known health-econ results
- The literature review reads like a list, not an argument about the frontier
- The paper cites general applied-micro work but misses the canonical health-econ findings it must engage
- The contribution is framed against a generic economics literature instead of the health-economics one

## Positioning at JHE

JHE referees are health economists; they hold the field's landmark results in their head and will reject a paper that re-derives a known coverage or moral-hazard effect with a new dataset. The contribution must be staked against the **health-economics frontier specifically** — the insurance-design, provider-incentive, behavior, or human-capital literature your result speaks to — and the marginal contribution must survive the question "a health economist already knows X; what is new?" Position on **one of**: a new mechanism, a new margin (e.g., intensive vs. extensive care use), a credibly-identified magnitude where prior estimates were confounded, a new setting that changes external validity, or a policy counterfactual prior work could not run.

## How to build the positioning argument

1. **Name the two or three literatures you sit between.** A coverage-and-utilization paper sits between the insurance-moral-hazard literature and the access/health-outcomes literature; say which gap you close.
2. **State the closest prior paper and the one-sentence delta.** Not "we extend the literature" but "Prior work estimated take-up; we identify the downstream health-production effect that take-up alone cannot reveal."
3. **Engage the canonical health-econ findings, not just recent arXiv.** A demand paper must engage the moral-hazard/selection canon; a provider paper the payment-response canon; a behavior paper the sin-tax/internality literature. Referees will name the paper you skipped.
4. **Separate the empirical delta from the policy delta.** JHE values both: a better-identified number *and* a health-policy lesson a regulator could act on.
5. **Pre-empt the "this is AJHE/JPubE" reroute** by showing the contribution is to *health economics*, not to public finance with a health label.

## Contribution-type map

| Contribution type | What the positioning must show | Failure mode |
|-------------------|--------------------------------|--------------|
| New mechanism | the channel is novel and the data can isolate it | relabeling a known channel |
| New margin | the margin (intensive/extensive, ex ante/ex post) was unmeasured before | a margin already studied, uncited |
| Credible magnitude | prior estimates were confounded; yours is identified | a cleaner estimate of a settled number |
| New setting / external validity | the setting changes the policy lesson, not just the sample | "same result, new country" with no stakes |
| Policy counterfactual | you can answer a question prior work structurally cannot | counterfactual not tied to a real policy |

## Which canon you must engage, by core

The fastest way to a desk reject is skipping the landmark a referee in your subfield holds. Engage the canon of the *specific* core, not just generic applied micro:

- **Insurance & moral hazard** — the demand-and-selection / welfare-of-insurance tradition (the cost-curve framing of selection and the value-vs-distortion split of utilization). Show you know the difference between behavioral hazard and selection.
- **Provider incentives** — the payment-response literature: how prospective vs. fee-for-service vs. capitation reshape intensity, coding, and patient mix. Engage the supplier-induced-demand debate where relevant.
- **Health behaviors** — the sin-tax / internality / addiction literature; engage the rational-vs-behavioral-addiction framing and the externality-vs-internality basis for policy.
- **Health & human capital** — the fetal-origins / early-life-shocks and health-to-earnings literature; show your shock maps to a known production channel.
- **Markets & competition** — the hospital/insurer competition and consolidation literature, including the regulated-market caveats that change standard IO predictions.

## Worked vignette (illustrative)

A draft on a soda tax positions itself against "the public-finance literature on commodity taxation" and reports a consumption drop. A health economist asks: what is new for *health* economics, and did you engage the internality literature? The JHE rewrite repositions between the sin-tax/internality canon and the obesity-outcomes literature, states the delta ("prior work estimated the consumption response; we identify the downstream caloric-intake and weight margin the consumption response cannot reveal"), and frames the policy lesson as internality-correction, not revenue. The contribution is now to health economics, and the JPubE reroute risk is gone.

## Checklist

- [ ] The marginal contribution is one sentence a health economist would accept
- [ ] The two or three relevant health-econ literatures are named and the gap between them stated
- [ ] The closest prior paper is cited and the delta is explicit
- [ ] The canonical findings of the relevant health-econ subfield are engaged, not skipped
- [ ] Empirical delta and policy delta are both stated
- [ ] The boundary vs. AJHE / JPubE / Health Economics is reinforced by the positioning
- [ ] The contribution survives the one-paragraph test without jargon-driven novelty
- [ ] Citations are real; none invented or marked when unverifiable

## The one-paragraph contribution test

Before the literature section is "done," write the contribution as a single paragraph a busy health economist could read and accept: the question, the two literatures it bridges, the closest prior result, the one-sentence delta, and the policy lesson. If that paragraph needs jargon to sound novel, the contribution is not yet distinct. This paragraph later seeds the introduction (`jhe-writing-style`), so getting it right here pays twice. If you cannot write it without overclaiming, the honest move is to sharpen the empirical or policy delta, or reconsider the venue (`jhe-topic-selection`).

## Anti-patterns

- A literature "review" that lists papers without an argument about the frontier
- "First to study X in country Y" as the whole contribution
- Citing general applied-micro work while skipping the canonical health-econ result a referee will name
- Overclaiming novelty for a known moral-hazard / coverage / take-up effect
- Positioning against public finance when the audience is health economists

## Output format

```text
【Journal】Journal of Health Economics
【Skill】jhe-literature-positioning
【Verdict】contribution clear / undersold / not yet distinct
【Literatures bridged】[lit A] × [lit B] — gap closed
【Closest prior + delta】one sentence
【Contribution type】mechanism / margin / magnitude / setting / counterfactual
【Empirical delta + policy delta】[...]
【Source status】citations verified / 待核实
【Next skill】jhe-identification
```

## Handoff boundary

Positioning sets the bar the design must clear; it does not run the design. Once the contribution paragraph is accepted, hand to `jhe-identification` so the empirical claim is credible enough to support the stated delta. If positioning keeps failing because the question is not really health economics, route back to `jhe-topic-selection` rather than forcing a frame the audience will reject.
