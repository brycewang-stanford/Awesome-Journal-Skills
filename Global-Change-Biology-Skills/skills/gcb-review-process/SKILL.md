---
name: gcb-review-process
description: Use to understand how a Global Change Biology (GCB) manuscript is judged — high desk-rejection screening for scope and significance, expert single-anonymous peer review with 2–3 reviewers, and the decision categories. Sets expectations and informs preparation; it does not contact editors or predict outcomes.
---

# Review Process (gcb-review-process)

GCB is selective and desk-rejects a large share of submissions before review. Knowing **how** it is
judged — what triggers desk rejection, who reviews, and what decisions look like — lets you prepare a
manuscript that survives screening and convinces reviewers. Verify volatile specifics on the official
page before submission.

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
2. **Expert peer review.** Matched experts assess mechanism, design, inference, uncertainty, and
   reproducibility; live-check current anonymity / transparent-review options on the official page.
3. **Reviewer access to data.** Reviewers may request access to data during evaluation — have the
   archive/availability ready.
4. **Decision categories.** Accept (rare on first pass), **minor / major revision**, or **reject**;
   editors weigh reviewer assessments and fit.

## Prepare for the way it is judged

- Make the **scope fit and significance unmistakable** in the title, abstract, and cover letter.
- Pre-empt the predictable reviewer concerns: scale/extrapolation, confounding/pseudoreplication,
  uncertainty, and reproducibility.
- Have **data and code archived (or staged)** so a reviewer request is trivial to satisfy.

## Desk-reject triggers and how to neutralize them

The editorial screen is where most submissions end. Map the common trigger to the pre-submission move
that removes it, before the manuscript ever reaches a reviewer.

| Desk-reject trigger | Why it fires | Neutralizing move |
|---------------------|--------------|-------------------|
| Scope mismatch | Reads as regional/conservation, not global-change | Lead title/abstract with driver → response mechanism |
| Thin significance | Increment too small for a broad-readership venue | State magnitude and cross-system relevance up front |
| Scale overreach | Plot result framed as global | Match the claim to the evidence; flag extrapolation |
| Missing required element | No graphical abstract or data statement | Complete both before submitting |
| Reproducibility gap | No archiving plan visible | Stage the DOI deposit and say so |

## Worked micro-example (illustrative)

A range-shift modelling paper is screened. The editor checks three things in order: does it test a
global-change driver (yes — warming), is the advance broad (the mechanism generalizes across montane
floras), and is it sound enough to review (design and uncertainty look defensible). It passes to two
reviewers with matched expertise (illustrative), one a biogeographer and one a modeller. The modeller
asks for the projection ensemble; because the code is already staged for archiving, the request is
trivial to satisfy. Had the paper led with "a new record for our region," it would likely have stopped
at the desk. Reviewer counts and roles are illustrative; confirm the current model on the official page.

## What expert reviewers reliably probe

- Whether a correlative pattern is being presented as a mechanism.
- Whether plot-to-biome scaling carries propagated uncertainty.
- Whether confounding or pseudoreplication undermines the causal claim.
- Whether the archived data and code actually reproduce the headline result.

## Anti-patterns

- Submitting a local/conservation-framed paper that fails the global-change scope screen
- Assuming review fixes a significance problem (desk screening catches it first)
- Ignoring uncertainty/reproducibility that expert reviewers will flag
- Being unprepared for a reviewer's request to access the data

## Output format

```
【Desk-screen risk】scope + significance unmistakable? [Y/N → why]
【Reviewer concerns】scale / confounding / uncertainty / reproducibility pre-empted?
【Review model】expert review; anonymity / transparent-review option live-checked? [Y/N]
【Data ready for reviewers】[Y/N]
【Decision likely】revision categories anticipated
【Next】gcb-submission (pre-decision) or gcb-revision-and-rebuttal (post-decision)
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — peer-review model and editorial screening
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reproducibility/data tooling reviewers may probe
