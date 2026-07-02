---
name: cc-figures-tables
description: Use when building or auditing multi-panel mechanistic figures and tables for a Cancer Cell (Cell Press) manuscript — quantification of images, panel logic, image integrity, and legends. It shapes display items; it does not choose statistical tests or write the abstract.
---

# Figures & Tables (cc-figures-tables)

## When to trigger

- Representative images (blots, IHC, micrographs) shown without quantification
- A multi-panel figure has no clear narrative logic
- Worried about image-integrity standards (splicing, over-processing)
- Building a graphical abstract or supplemental display items

## Cancer Cell figure logic

Each main figure should advance **one step of the mechanistic argument** and be readable on its own:

- Panels flow left-to-right / top-to-bottom as a mini-narrative (perturbation → readout → mechanism → consequence).
- Mechanistic figures typically combine schematic + functional data + in vivo and/or human validation.
- A figure usually carries discovery, validation, and a control panel together.
- Keep one main message per figure; push orthogonal corroboration to supplement.

## Quantify everything representative

The signature Cancer Cell requirement: **a representative image must be paired with quantification across biological replicates.**

| Representative image | Required quantification |
|----------------------|--------------------------|
| Western blot | Densitometry across `n` independent blots (normalized to loading) |
| IHC / IF micrograph | Scored / counted across multiple fields and tumors (e.g., QuPath) |
| Flow plot | Summary bar/dot plot of % or MFI across replicates |
| Tumor photo | Tumor volume/weight curves with `n`, stats |
| Migration/invasion image | Quantified across fields/replicates |
| Single-cell UMAP | Proportions / DE stats, not just a colored embedding |

Show data points (superplots) for small `n`; never imply quantity from one picture.

## Image integrity (Cell Press enforces)

- Keep **uncropped, unprocessed** raw blots/gels; include full-length blots in supplement with MW markers.
- No splicing of lanes without a clear dividing line and disclosure.
- Adjustments (brightness/contrast) must be **linear and applied to the entire image**, including controls.
- Do not duplicate, mirror, or reuse panels across figures.
- Disclose any grouping of images from different parts of the same gel.

## Tables and the Key Resources Table

- The **Key Resources Table** (STAR Methods) is mandatory — see `cc-reporting-standards`.
- Data tables (cohorts, mutation lists, screen hits) go to supplement; keep main tables minimal.
- Define every abbreviation and unit in legends.

## Legends

- State `n`, what one replicate is, the statistical test, the error-bar definition, and scale bars.
- Each panel letter referenced; magnification/scale bar on all micrographs.
- Antibodies / markers / treatments named in the legend.

## Worked micro-example: fixing a "representative blot" panel

**Before:** Figure 2C is a single Western blot showing MARK7 down and cleaved-PARP up after treatment,
captioned "representative of independent experiments."

**Why a Cancer Cell reviewer rejects it as evidence:** one image cannot support a quantitative claim; the
reader cannot see variance, `n`, or whether the effect is consistent.

**After:** Figure 2C keeps the representative blot but adds 2C′ — densitometry normalized to loading
control across four independent lysates, plotted as a superplot (individual points + mean), with the
test and exact p in the legend. The uncropped full-length blot with MW markers moves to Figure S2. Now
the panel carries a claim, not an anecdote.

## Panel-order sanity check (per main figure)

Read each figure left-to-right and ask whether it narrates one mechanistic step:

1. **Perturbation** — what was changed (knockdown/knockout/inhibitor), with the validation of that perturbation.
2. **Readout** — the phenotype or molecular consequence, quantified across replicates.
3. **Mechanism** — the intermediate that connects perturbation to readout (binding, flux, signaling).
4. **Orthogonal confirmation** — in vivo and/or human panel that the claim in the figure title needs.

If a panel does not serve the figure's one-sentence title, move it to the supplement.

## Cancer Cell figure failure modes reviewers cite

- A migration/invasion or IHC figure with beautiful images but no per-field, per-tumor quantification.
- Tumor-growth curves without `n` per arm, without the test, or truncated before humane endpoints.
- Flow plots shown as gated dot-plots only, with no summary statistic across mice/donors.
- A graphical abstract that asserts an axis (arrows implying causality) the main figures never establish.
- Kaplan-Meier survival curves with no numbers-at-risk and no censoring shown.
- Contrast/brightness pushed non-linearly, or a loading-control band reused across panels.

## Checklist

- [ ] Every figure advances one mechanistic step; panel order tells a story
- [ ] Each representative image is paired with replicate-level quantification
- [ ] Data points shown for small-n panels (superplots)
- [ ] Blots uncropped in supplement, MW markers visible, no undisclosed splicing
- [ ] Image adjustments linear and whole-image; no duplicated panels
- [ ] Scale bars on all micrographs; channels/markers labeled
- [ ] Legends give `n`, test, error-bar definition
- [ ] In vivo / human validation panels present where claims need them
- [ ] Graphical abstract (if used) conveys the mechanism at a glance

## Anti-patterns

- One representative blot/image as the entire evidence (no quantification)
- Bar charts hiding tiny `n`; undefined error bars
- Spliced or over-contrasted blots; reused/duplicated panels
- Overcrowded figures mixing several unrelated messages
- Missing scale bars or unlabeled axes
- Beautiful schematic with no supporting data

## Output format

```
【Per-figure message】Fig1: ... Fig2: ...
【Representative-without-quantification】flagged panels: [...]
【Image integrity】raw blots? linear adj? duplication check
【Legends】n / test / error bar / scale bar present? Y/N
【Validation panels】in vivo / human present where needed?
【Next step】cc-structured-abstract
```
