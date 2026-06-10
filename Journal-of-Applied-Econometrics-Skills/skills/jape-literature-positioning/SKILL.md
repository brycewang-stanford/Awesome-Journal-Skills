---
name: jape-literature-positioning
description: Use when positioning a Journal of Applied Econometrics (JAE) manuscript against prior work — applied-econometrics precedent, the methods you apply, and JAE's own corpus and Data Archive of replicable papers. Frames the gap as an application/replication advance under JAE's citation-style-agnostic Free Format.
---

# Literature Positioning for JAE (jape-literature-positioning)

## When to trigger

- Drafting or revising the related-work framing for a JAE paper
- Deciding which methodological and applied precedents to foreground
- Making sure your positioning reflects JAE's emphasis on replicable applied work

## Position on two axes at once

JAE values an **application on real data** that advances or rigorously tests a technique. Position simultaneously on:

1. **Method lineage** — cite the econometric technique(s) you apply or extend, and the canonical references for the estimator/inference you use. Make clear what you adopt unchanged vs. adapt.
2. **Applied / substantive lineage** — cite prior empirical work on the same question or data, and say precisely what your application adds: new data, a new design, more credible inference, a resolved puzzle.

Because JAE runs a **Replication Article** track and a Data Archive of ~1,487 datasets, its culture rewards engagement with **prior replicable evidence**. If your result revisits a published finding, position relative to that paper's archived data/code and state whether you confirm, qualify, or overturn it.

## Free Format and references

JAE accepts references "**in any style or format, as long as it is consistent throughout the manuscript**" and allows **Free Format** first submission. Positioning is about *substance and consistency*, not house style — pick one style, keep it uniform, and do not stall on a template.

## Archive-aware positioning

When a prior JAE or applied-econometrics paper has public data/code, do not cite it only as background.
Use the archive trail to sharpen the contribution:

- If you reuse the design, say which archived sample, variables, or code paths are retained.
- If you update the evidence, state whether new data, corrected coding, or a different inference method
  changes the original conclusion.
- If you extend a method, explain what the old archive could not test and what your new package will let
  readers inspect.
- If replication fails, separate data drift, implementation differences, and substantive disagreement.

This turns literature positioning into an empirical audit trail, which is closer to JAE's culture than a
generic related-work survey.

## Four citation strata a JAE bibliography carries

Audit the reference list against these strata; a JAE submission that is thin in any one reads as mis-positioned:

| Stratum | What it contains | Failure mode if absent |
| --- | --- | --- |
| Estimator/inference canon | The original method papers plus the inference refinements you actually use (HAC, wild bootstrap, weak-IV) | Referees assume you applied the method naively |
| Applied precedent | Prior empirical answers to the same question, with their designs and magnitudes | "What does this add?" is unanswerable |
| JAE-corpus neighbors | Related JAE papers, ideally with archived data/code you can point to | Editor cannot see why this venue |
| Replication target (if any) | The specific published paper revisited, with its archive entry | The Replication Article framing collapses |

## Worked positioning sketch: revisiting an archived result (illustrative)

Suppose a 2015 JAE paper found money-demand elasticity −0.45 using quarterly G7 data through 2012, with data and programs in the archive. A strong positioning paragraph states: which archived series and code paths you reuse unchanged (their sample construction), what you change (extend to 2024; replace HAC with wild bootstrap for the short country panel), and the outcome (elasticity −0.41 on their sample — a confirmation — but −0.22 post-2015, a qualification). That single paragraph does the work of three survey pages — the positioning shape JAE's archive culture exists to enable.

## Pushback: "incremental application" — the JAE counter

When a referee writes that the paper is X-applied-to-new-data, do not pile on citations. Sharpen the audit trail: name the precedent paper whose conclusion your application tests, show where its archived evidence stops (sample end, inference choice, omitted heterogeneity), and state which of confirm / qualify / overturn your result delivers. At JAE, position against *reproducible evidence*, not abstract literatures — a gap defined by what an existing archive package cannot show is the most defensible gap claim here.

## Positioning map block

```text
Method canon: [refs] — adopted unchanged: [...] / adapted: [...]
Applied precedent: [refs] — their finding: [...] — your delta: [...]
JAE neighbors: [refs] — archive entries consulted: [Y/N]
Replication target: [ref or N/A] — verdict: confirm / qualify / overturn
```

## Output format

```
【Method lineage】key technique refs cited? [Y/N]
【Applied lineage】prior empirics engaged? [Y/N]
【Replication tie】revisits a published result? archive acknowledged? [Y/N/NA]
【Strata】all four citation strata covered? [Y/N]
【Gap】application/replication advance in one sentence
【Refs】single consistent style? [Y/N]
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — Free Format and Data Archive sources
