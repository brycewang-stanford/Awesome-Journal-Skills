---
name: jf-referee-strategy
description: Use when anticipating referee objections and selecting suggested/opposed reviewers before or during a The Journal of Finance (JF) submission. Plans for review; it does not write the rebuttal (use jf-rebuttal).
---

# Referee Strategy (jf-referee-strategy)

## When to trigger

- Before submission: pre-empt the objections a JF referee will raise
- The portal asks for suggested / opposed reviewers and you need a principled list
- You want to red-team your own paper against the JF review culture
- After a desk pass, before you get reports, to prepare your defenses

## The JF review culture you are writing for

JF review is **demanding and multi-round**, run by an Editor and Associate Editors who pick referees from the broad finance community. Referees reward general interest, clean identification or a well-motivated test, economic significance, and honest robustness. They punish data mining, unaddressed endogeneity, fragile factor results, and over-long papers that bury the result. Write the paper as if the toughest referee in your subfield — and one generalist outside it — will both read it.

## Anticipate the predictable objections

| Paper type        | The objection that will come                                         | Pre-empt by…                                              |
|-------------------|----------------------------------------------------------------------|-----------------------------------------------------------|
| Corporate/empirical | "The treatment is endogenous / pre-trends drive this"              | Event-study plot, placebo, modern staggered-DID estimator |
| Corporate/empirical | "Your instrument is not excludable"                                | Three-leg exclusion argument + reduced form               |
| Asset pricing     | "This is data mining / multiple testing"                             | Disclose the search; adjusted hurdle; out-of-sample        |
| Asset pricing     | "It only works in equal-weighted microcaps"                          | Value-weighting, NYSE breakpoints, exclude penny stocks    |
| Asset pricing     | "Your factor is spanned by existing factors"                         | Spanning regressions vs. FF5 / q-factor / momentum         |
| Any               | "Too long; the contribution is buried"                               | Tighten intro; move depth to the Internet Appendix         |
| Any               | "Effect is statistically but not economically significant"           | Lead with magnitude in interpretable units                 |

## Selecting reviewers (when the portal allows)

- **Suggest** scholars who know the literature and can evaluate the method, are not collaborators / co-authors / advisees, and have no conflict. Spread across the relevant subfields so a generalist editor sees balanced expertise.
- **Oppose** (sparingly, with brief neutral reasons) only direct competitors with a clear conflict — over-long oppose lists look defensive.
- Do not suggest only friendly names; JF editors recognize and discount a stacked list.

## Checklist

- [ ] The two or three most likely objections are written down and each has a pre-emptive response in the paper
- [ ] Endogeneity (corporate) or multiple-testing (asset pricing) is addressed before a referee raises it
- [ ] The economic magnitude is front and center, not just significance
- [ ] The paper length and structure will not draw a "buries the result" complaint
- [ ] Suggested reviewers are qualified, conflict-free, and span the relevant subfields
- [ ] Opposed reviewers (if any) are few and justified neutrally

## Anti-patterns

- Hoping a known weakness goes unnoticed instead of addressing it in the paper
- A suggested-reviewer list of only co-authors and friends
- A long opposed list that signals the authors expect a hostile reception
- Ignoring the generalist reader — writing only for three subfield experts
- Treating the cover letter as the place to make arguments that belong in the paper

## Output format

```
【Top objections】[1] ... [2] ... [3] ...
【Pre-emptive response in paper?】yes / no per objection
【Endogeneity / multiple-testing pre-empted?】yes / no
【Suggested reviewers】[names + 1-line rationale, conflict-free]
【Opposed reviewers】[few, neutral reason] / none
【Next step】jf-submission (if pre-submission) or jf-rebuttal (after decision)
```
