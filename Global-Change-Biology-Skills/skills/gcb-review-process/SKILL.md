---
name: gcb-review-process
description: Use to understand how a Global Change Biology (GCB) manuscript is judged — high desk-rejection screening for scope and significance, expert single-anonymous peer review with 2–3 reviewers, and the decision categories. Sets expectations and informs preparation; it does not contact editors or predict outcomes.
---

# Review Process (gcb-review-process)

GCB is selective and desk-rejects a large share of submissions before review. Knowing **how** it is
judged — what triggers desk rejection, who reviews, and what decisions look like — lets you prepare a
manuscript that survives screening and convinces reviewers. Verify volatile specifics on the official
page (see 待核实 in the source map).

## When to trigger

- Setting expectations before submitting
- Diagnosing why a paper might be desk-rejected
- Anticipating reviewer concerns to pre-empt in the manuscript
- Interpreting a decision letter (then route to `gcb-revision-and-rebuttal`)

## How GCB judges a paper

1. **Editorial / desk screening (high bar).** Editors screen first for **scope fit** (a mechanistic
   global-change → biological-response advance), **significance / broad relevance**, and basic
   soundness. A large fraction is **desk-rejected** quickly; a poor scope/significance fit is the most
   common cause.
2. **Expert peer review.** Typically **2–3 reviewers** with matched expertise assess mechanism,
   design, inference, uncertainty, and reproducibility; the model is generally **single-anonymous**
   (author identities visible to reviewers) — confirm current model on the live page (待核实).
3. **Reviewer access to data.** Reviewers may request access to data during evaluation — have the
   archive/availability ready.
4. **Decision categories.** Accept (rare on first pass), **minor / major revision**, or **reject**;
   editors weigh reviewer assessments and fit.

## Prepare for the way it is judged

- Make the **scope fit and significance unmistakable** in the title, abstract, and cover letter.
- Pre-empt the predictable reviewer concerns: scale/extrapolation, confounding/pseudoreplication,
  uncertainty, and reproducibility.
- Have **data and code archived (or staged)** so a reviewer request is trivial to satisfy.

## Anti-patterns

- Submitting a local/conservation-framed paper that fails the global-change scope screen
- Assuming review fixes a significance problem (desk screening catches it first)
- Ignoring uncertainty/reproducibility that expert reviewers will flag
- Being unprepared for a reviewer's request to access the data

## Output format

```
【Desk-screen risk】scope + significance unmistakable? [Y/N → why]
【Reviewer concerns】scale / confounding / uncertainty / reproducibility pre-empted?
【Review model】single-anonymous; 2–3 reviewers (待核实)
【Data ready for reviewers】[Y/N]
【Decision likely】revision categories anticipated
【Next】gcb-submission (pre-decision) or gcb-revision-and-rebuttal (post-decision)
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — peer-review model and editorial screening
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reproducibility/data tooling reviewers may probe
