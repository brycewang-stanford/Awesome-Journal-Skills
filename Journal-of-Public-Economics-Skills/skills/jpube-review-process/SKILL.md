---
name: jpube-review-process
description: Use when you need to understand or plan around the Journal of Public Economics (JPubE / JPubEc) editorial process — single anonymized review with a minimum of two reviewers, the Editorial Manager workflow, the Hendren–Kopczuk editorial leadership, SSRN preprint option, and the one-appeal policy. Explains the process; for the final file check use jpube-submission.
---

# Review Process (jpube-review-process)

## When to trigger

- You want to know what happens after you press submit at JPubE
- You are deciding whether to post an SSRN preprint at submission
- You need to plan timelines and expectations around the review model
- A decision arrived and you are weighing whether to appeal

## How JPubE review works (verified facts)

- **Single anonymized review.** Reviewers' identities are hidden from authors, but **authors' identities are known to reviewers and editors**. This is *not* double-anonymized — do not strip your name from the manuscript expecting blind review; write knowing referees see who you are. (Contrast: some venues use double-anonymized review.)
- **Minimum of two reviewers.** Suitable submissions are typically sent to at least two reviewers; expect substantive, specialist public-finance reports.
- **Editorial leadership.** The current ScienceDirect masthead lists **Editors Nathaniel Hendren (MIT)** and **Wojciech Kopczuk (Columbia)**, supported by co-editors and advisory editors. A handling editor manages your manuscript and synthesizes the reports into the decision.
- **Editorial Manager workflow.** Submission and all correspondence run through Elsevier's **Editorial Manager** system; decisions (desk reject / reject / major or minor revision / accept) and revision uploads happen there.
- **SSRN preprint option.** At submission you may opt to have the manuscript posted publicly on **SSRN** after initial quality checks; this choice has **no effect on the editorial process or outcome**, so it is a free dissemination option, not a strategic lever.
- **Generative-AI disclosure** is required at submission and is part of the editorial-integrity screen.

## Appeals (verified)

- Formal **appeals are permitted** under Elsevier's Appeal Policy, but **only one appeal per submission** is considered. Treat the appeal as a scarce, one-shot instrument: use it only for a clear factual or procedural error in the handling of the paper, with a calm, evidence-based case — not to relitigate taste. (See `jpube-rebuttal` for crafting the substance.)

## Planning implications

- Write for **named, specialist referees** who can see your identity — frame contribution and self-citations accordingly.
- Do not over-invest in anonymization; invest in a transparent design two specialist reviewers can endorse.
- Decide the SSRN option deliberately (visibility vs. preferring to wait), knowing it does not change your odds.

## Checklist

- [ ] Manuscript written for single-anonymized (identity-visible) specialist review
- [ ] Expect ≥ 2 reviewers; address the obvious public-finance objections pre-emptively
- [ ] Editorial Manager account and metadata ready
- [ ] SSRN preprint decision made deliberately
- [ ] AI-use disclosure prepared
- [ ] Appeal reserved for a clear error, used at most once

## Anti-patterns

- Stripping author identity expecting double-blind review (JPubE is single anonymized)
- Treating the SSRN option as if it improved acceptance odds
- Burning the single appeal on a taste disagreement instead of a factual/procedural error
- Ignoring AI disclosure requirements during submission

## Decision pathways after submit

What lands in your inbox, and what each outcome implies for a public-finance paper.

| Outcome | What it means | Your move |
|---------|---------------|-----------|
| Desk reject | Editor judged fit/contribution below bar before review | Re-route (jpube-topic-selection) or strengthen welfare framing |
| Reject after review | Specialists found a design or welfare gap | Appeal only on a clear error; else resubmit elsewhere |
| Major revision | Contribution viable; identification/welfare needs work | Route fundamentals to identification/data skills, then rebuttal |
| Minor revision | Close; clarifications and exhibits | Tighten, document, return promptly |
| Accept | — | Confirm data-availability and final source files |

## Worked vignette: deciding whether to appeal (illustrative)

A bunching paper is rejected; two specialist reports agree the excess-mass counterfactual is the weak point, while one aside claims "the elasticity (**e = 0.4**, illustrative) is implausibly high." The author wants to appeal the second remark. The review-process read: the binding objection is the counterfactual, which is a substantive design judgment, not a factual or procedural error — so it is **not** appeal-eligible. The single appeal is reserved; the better path is to rebuild the counterfactual and resubmit (or send elsewhere), not to spend the one-shot appeal contesting taste.

## Calibration anchors

- Plan for named, specialist referees who see your identity: pre-empt the obvious public-finance objection (counterfactual, pre-trends, sufficient-statistic assumption) in the manuscript itself.
- Calibration: short-paper-track targets are published separately from the standard track; do not infer a fixed turnaround time for ordinary submissions from the short-paper 4-6 week target.

## Output format

```
【Review model】single anonymized (identity visible), ≥2 reviewers — understood? [Y/N]
【Editorial Manager】account + metadata ready? [Y/N]
【SSRN preprint】opt-in decision: [yes/no]
【AI disclosure】prepared? [Y/N]
【Appeal status】reserved for clear error, ≤1 use — noted? [Y/N]
【Next step】jpube-submission
```
