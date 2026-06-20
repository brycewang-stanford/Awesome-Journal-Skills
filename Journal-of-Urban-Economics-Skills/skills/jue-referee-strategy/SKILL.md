---
name: jue-referee-strategy
description: Use when anticipating the objections a Journal of Urban Economics (JUE) referee will raise before submission, so the manuscript pre-empts them. Maps the recurring JUE spatial pushbacks to where each is answered in the paper; it does not run the analysis or draft the response letter (jue-rebuttal).
---

# Referee Strategy (jue-referee-strategy)

## When to trigger

- The paper is close to submission and you want to pre-empt the predictable JUE objections
- You suspect a referee will say "this is sorting, not the treatment" and the paper does not answer it
- The control geography or spatial scale could be attacked and no pre-emptive check exists
- You need to decide which referee concerns to answer in the paper vs. flag for the editor
- A coauthor is over-confident that the design is bulletproof against spatial critiques

## The JUE referee reads for spatial credibility first

A JUE referee is an urban economist who has seen every spatial confound. Before submission, walk the paper through the objections they reliably raise and confirm each is *already answered in the text*, not deferred to a hoped-for revision.

| Predictable JUE referee objection | Where the paper must already answer it |
|-----------------------------------|----------------------------------------|
| "This is spatial **sorting/selection**, not the treatment." | `jue-identification` balance/composition + a placebo pre-trend; the prose says so |
| "Your control areas are **contaminated by spillovers**." | spillover-ring estimate; controls outside the ring; SUTVA addressed |
| "Standard errors ignore **spatial autocorrelation**." | Conley/spatial-cluster SEs with a defended cutoff, vs naive |
| "The result is an artifact of your **spatial scale** (MAUP)." | estimates at multiple scales; scale-stability shown |
| "The **boundary/buffer** is arbitrary." | radius/donut sensitivity; covariate smoothness at the boundary |
| "What does this mean **in equilibrium** once agents re-sort?" | `jue-theory-model`: short-run vs long-run, incidence located |
| "Why **JUE** and not RSUE/JEG/JPubE?" | `jue-literature-positioning`: the strand and delta are explicit |
| "The **magnitude** is uninterpretable / not policy-relevant." | result in % or elasticity; welfare/policy reading threaded in |
| "Shift-share **exogeneity** is asserted." | Rotemberg weights or BHJ diagnostics reported |

## Strategy craft

1. **Map every likely objection to a specific exhibit or paragraph.** If an objection has no home in the paper, you have found the gap to close before submission, not after.
2. **Distinguish fatal from cosmetic.** A sorting or SUTVA objection can sink the paper; a "add one more control" objection cannot. Invest defense effort accordingly.
3. **Pre-empt in the text, not the appendix alone.** The first reader is the editor deciding desk-reject; the main text must show the design survives the obvious spatial attacks.
4. **Use the cover letter for what referees cannot infer** — a confidential-data exemption, a deliberate scope choice, why a sibling journal is wrong.
5. **Seed the rebuttal.** Note, for each anticipated objection, the check you would run if asked, so `jue-rebuttal` is fast.

## Two referee personas to write for

JUE papers are typically read by at least two reviewers with different priors; design the paper to satisfy both:

- **The design referee** wants the spatial identification airtight — sorting, SUTVA, spatial SEs, boundary/scale sensitivity. They will not be moved by policy relevance if the design leaks. Your identification and robustness sections are written for this reader.
- **The urban-economics referee** wants the mechanism and the magnitude to matter for cities — is the elasticity new, does it discipline theory, does it speak to housing/transport/place-based policy? A perfectly identified but uninteresting result loses this reader. Your framing, theory, and conclusion are written for them.

A paper that pleases only one persona stalls. The introduction must signal *both* a credible spatial design and a contribution an urban economist cares about.

## Checklist

- [ ] Every recurring spatial objection (sorting / spillover / spatial SE / MAUP / boundary) has a home in the text
- [ ] Sorting and SUTVA — the fatal ones — are answered in the main text, not only the appendix
- [ ] The sibling-fit objection is pre-empted in the introduction
- [ ] The magnitude is interpretable and tied to policy/welfare
- [ ] Cover letter flags what referees cannot infer (exemptions, scope, venue choice)
- [ ] For each anticipated objection, a fallback check is ready for the rebuttal
- [ ] Page one satisfies both the design referee and the urban-economics referee
- [ ] Suggested reviewers are spatial-design-fluent; opposed reviewers have a defensible reason

## Anti-patterns

- Assuming the design is obvious and leaving sorting/spillover objections unanswered
- Burying the answer to a fatal objection in an appendix the editor may not reach
- Treating all referee comments as equally important and over-investing in cosmetic ones
- No cover-letter framing, so the editor must guess scope and venue fit
- Entering the R&R with no pre-planned checks for the objections you could see coming

## Suggesting and excluding reviewers

Editorial Manager often asks for suggested and opposed reviewers; use it strategically. Suggest urban economists who know the *spatial* design you use and the strand you contribute to — a referee fluent in boundary discontinuities or shift-share will engage your evidence rather than fault its absence. Oppose only with a defensible reason (direct competition, conflict). A thoughtful suggestion list signals to the editor that you know the field's reviewers, which is itself a small fit signal; a list of distant or non-spatial names suggests the paper may not belong at JUE.

## Worked vignette (illustrative)

Before submitting the light-rail capitalization paper, the team lists the JUE referee's likely fire: sorting into the corridor, displaced demand contaminating controls, non-spatial SEs, and "why not RSUE." Each gets a pre-emptive home: a pre-period demographic balance table (sorting), a spillover-ring estimate (SUTVA), Conley SEs at a 5km cutoff (spatial dependence), and an intro paragraph staking the agglomeration-vs-transport strand (venue). The remaining anticipated ask — robustness to the ring radius — is pre-run and parked for the rebuttal. The paper now answers its referees before they write.

## The desk-reject gate is the first referee

At a high-volume field flagship the editor's triage *is* the first review, and it is unforgiving. Before submission, read your own first page as the handling editor: in two minutes can they see (1) it is genuinely spatial, (2) the identification is credible against the obvious confounds, (3) the magnitude matters for cities, and (4) why JUE and not a sibling? If any of these is not visible on page one, the paper risks a desk-reject before a referee ever weighs in. The cover letter is your one chance to supply what the first page cannot — frame it for the editor, not the eventual referee.

## Output format

```text
【Objection → home】sorting: ___ | spillover: ___ | spatial-SE: ___ | MAUP: ___ | boundary: ___ | venue: ___ | magnitude: ___
【Fatal vs cosmetic】fatal objections answered in main text? [Y/N]
【Cover-letter framing】exemptions/scope/venue stated? [Y/N]
【Rebuttal seeds】fallback checks pre-planned for each objection? [Y/N]
【Open gap】objection with no home in the paper: ___
【Next skill】jue-submission
```

> If a likely objection has no home in the paper and you cannot build one before the deadline, that is a signal to delay submission rather than gamble on the referee not noticing — at a field flagship, they will.
