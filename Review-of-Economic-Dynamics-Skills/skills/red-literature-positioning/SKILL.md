---
name: red-literature-positioning
description: Use when positioning a Review of Economic Dynamics (RED) manuscript within the dynamic-economics and SED literature — mapping the quantitative-macro lineage a paper builds on, citing in author-year style, and making the marginal advance legible to the Society for Economic Dynamics readership rather than a generalist audience.
---

# Literature Positioning for RED (red-literature-positioning)

## When to trigger

- Writing the introduction and related-work sections for a RED submission
- Unsure which strand of the dynamic-economics literature the paper extends
- Pitching the contribution to the SED community versus a generalist top-5 framing

## How to position for RED

RED's readers are the **SED community** working on dynamic models. Position the paper inside the
**method lineage**, not just the topic:

- Name the **modeling tradition** you extend (e.g., RBC/DSGE, Aiyagari/Bewley–Huggett heterogeneous
  agents, Krusell–Smith aggregate-uncertainty methods, search/matching, endogenous growth, HANK).
- State the **quantitative gap** precisely: which moment the prior models miss, which mechanism is
  absent, which policy environment is unmodeled, or which computational barrier you remove.
- Distinguish your **contribution type** — a new mechanism, a new solution/estimation method, a new
  quantitative finding, or a new empirical regularity that disciplines the model.
- Use **author-year (Harvard-style)** citations throughout, consistent with RED's reference system.

Because RED's scope is method-defined, the literature you cite should be **dynamic-model** literature.
A paper that mostly cites reduced-form empirical work without a dynamic-modeling anchor reads as a
poor fit; tie empirical references back to what they discipline in the model.

## Checklist

- [ ] The modeling lineage is named and the paper's place in it is explicit
- [ ] The marginal advance is stated as a quantitative/mechanistic delta, not "we also study X"
- [ ] Closely related SED-community papers are cited and differentiated, not ignored
- [ ] Citations are clean author-year; reference list complete and consistent

## Anti-patterns

- A generalist "big literature" sweep that never locates the paper in a dynamic-model tradition
- Burying the closest competitor instead of confronting it head-on
- Mixed or inconsistent citation styles instead of clean author-year

## SED-reader positioning move

For each cited strand, name the **state variable, shock, friction, or numerical method** that connects it
to your paper. A RED reader should be able to see the dynamic lineage without translating from a
general-interest pitch.

Use this sequence:

1. Closest model/method and its missing mechanism.
2. Closest quantitative result and the moment it cannot match.
3. Closest computation/estimation approach and the constraint it imposes.
4. Your paper's delta in one sentence.

Do not spend equal space on literatures that supply motivation but do not discipline the dynamic model.

## Lineage map template

Write the positioning as a lineage map before drafting prose:

```text
LINEAGE MAP — [paper title]
  Tradition:       [e.g., incomplete-markets / Aiyagari–Bewley–Huggett]
  State variables: [what the tradition tracks: wealth distribution, beliefs, match capital]
  Closest model:   [author-year] — misses [mechanism]
  Closest moment:  [author-year] — cannot match [moment + magnitude]
  Closest method:  [author-year] — constrained by [computational or estimation limit]
  This paper:      adds [delta] and shows [quantitative consequence]
```

Every line should name something dynamic — a state variable, a shock process, a friction, or a solution
method. If a line can only be filled with a topic word ("inequality", "housing"), the positioning is
still generalist and not yet RED-shaped.

## Positioning vignette: a firm-dynamics draft

A draft embeds collateral constraints in a Hopenhayn-style entry/exit model. Illustrative map: tradition
= heterogeneous-firm dynamics; closest model = a frictionless benchmark whose firm-size distribution is
too thin at entry; closest moment = an exit hazard by age that prior calibrations overshoot by roughly a
third (illustrative figure); delta = a borrowing constraint that bends the hazard while preserving the
aggregate-TFP discipline of the benchmark. The introduction's first four sentences fall straight out of
this map, each anchored by one author-year citation.

## Strand-weighting rule

Allocate related-work space by what disciplines the model: strands that supply calibration targets,
solution methods, or competing mechanisms earn paragraphs; strands that only motivate the topic earn one
sentence with a representative citation. SED readers forgive a short motivation; they do not forgive a
missing comparison to the nearest quantitative experiment in their own tradition.

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — author-year style and scope sources
