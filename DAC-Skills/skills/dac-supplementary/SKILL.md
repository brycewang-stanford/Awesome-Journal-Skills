---
name: dac-supplementary
description: Use when deciding what belongs inside the six reviewed pages of an ACM/IEEE Design Automation Conference (DAC) Research Manuscript versus in an external repository, given DAC's tight 6+1 budget, its references-only seventh page, the double-blind constraint on any linked material, and the absence of a formal reviewed-appendix or artifact-badging track.
---

# DAC Supplementary Material

Use this to split content between the reviewed pages and anything external. DAC's constraint is
severe and specific: the manuscript is **6 pages of body plus one references-only page**, and unlike
some venues DAC does **not** provide an unlimited reviewed appendix or a formal artifact-evaluation
track (**待核实** per cycle). The governing rule follows directly: **anything that decides
acceptance must fit inside the six body pages**, because a reviewer is neither obligated to nor
guaranteed to open external material.

## The decision-criticality test

For each piece of content, ask: *would a reviewer need this to be convinced the contribution is real
and the QoR claim is fair?* If yes, it belongs in the body. If it merely lets a motivated reader
reproduce or extend the work, it can live externally.

| Content | Where it goes | Why |
|---|---|---|
| The headline QoR results and the mechanism | Body (6 pages) | Decision-critical; reviewers judge on these |
| Per-benchmark result table for the main claim | Body | The fairness of the comparison is the paper |
| The key ablation | Body | Attribution of the gain is decision-critical |
| Full hyperparameter grids, extra corners, exhaustive per-instance logs | External repo | Supports reproduction, does not decide acceptance |
| Source code, scripts, generated datasets | External repo | Reproducibility, not a reviewed deliverable |
| Extra proofs/derivations too long for six pages | External repo, with the result stated in-body | The claim must stand in-body; detail can be external |

## The seventh page is references only

DAC's most mechanical rule: the one extra page holds **references and nothing else**. Do not treat
it as an appendix — an extra figure, a paragraph, or a table there is grounds for **desk rejection**
(`../dac-submission`). Plan the technical argument to end cleanly at page six.

## External material under double-blind

If you link a repository, dataset, or artifact at review time, it must be **anonymized** exactly
like the PDF:

- No author names, institution names, or lab-named tools in the repo, README, or commit metadata.
- Host on an anonymizing service or a fresh anonymous mirror; a personal GitHub URL de-anonymizes.
- Strip cluster paths, internal server names, and vendor-flow fingerprints from any logs or scripts
  you include.
- Remember reviewers may **not** open it — so external material can only *strengthen* a paper that
  already stands on its six pages, never *rescue* one that does not.

## What DAC does not have (plan accordingly)

- **No formal reviewed appendix** — do not write "see the appendix" for anything decision-critical;
  there is no guaranteed extra reviewed space beyond the six pages.
- **No standing ACM artifact-badging track** for research manuscripts (**待核实**) — so an artifact
  earns you credibility and citations, not a badge; build it for reproducibility and community use,
  not for a review score (`../dac-artifact-evaluation`, `../dac-reproducibility`).

## Compression before relegation

Before moving something out, try to *earn* its space in the body: convert a prose result to a
compact table, merge two figures, cut standard EDA background the reviewers already know. Six dense
double-column pages hold more than first drafts assume.

## Output format

```text
[Split audit]    each item -> body (decision-critical) / external (reproduction) / cut
[Seventh page]   references only, no body content? yes/no
[External anon]  linked repo/dataset/artifact anonymized? reviewer-optional acknowledged? yes/no
[Stands alone]   does the paper convince on its six pages without external material? yes/no
[Compression]    space reclaimed before relegating anything? yes/no
```
