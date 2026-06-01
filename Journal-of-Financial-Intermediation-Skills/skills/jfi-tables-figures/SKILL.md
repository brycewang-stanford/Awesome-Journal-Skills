---
name: jfi-tables-figures
description: Use to design the exhibits for a Journal of Financial Intermediation paper — banking-literate tables and figures with explicit sample construction, institution definitions, event timing, and self-contained notes. It designs exhibits; it does not run the estimation.
---

# Tables & Figures (jfi-tables-figures)

## When to trigger

- Building or revising the table/figure set for a JFI submission
- A referee found the exhibits hard to read or under-documented

## What JFI exhibits must do

JFI exhibits are read by **banking and intermediation specialists**, so they must be self-contained and
institution-aware:

- **Summary / sample table first:** the bank/loan/firm universe, the data source (Call Reports, DealScan,
  HMDA, etc.), every filter, and units — readers must reconstruct the sample from the notes alone.
- **Define institutions and variables in the notes:** what counts as a "bank," how credit/balance-sheet
  quantities are measured, the treatment and its timing.
- **Main result table:** the headline specification with the FE structure visible, standard errors and the
  clustering level stated, and the mechanism estimate foregrounded.
- **Event-study / dynamics figure:** for DID designs, a pre-trend-and-effect plot is often the single most
  persuasive exhibit; show confidence bands and the reference period.
- **Robustness exhibits:** alternative samples, windows, and specifications, compactly tabulated.
- **Theory papers:** a clean figure of the mechanism or comparative statics, with parameters in the note.

## House conventions

Number exhibits and call them out in order; **numbered manuscript sections** (1, 1.1) host them. Notes
should name the estimator, sample, clustering, and significance markers. There is **no stated exhibit or
length cap** (待核实).

## Anti-patterns

- A results table a reader cannot map to a sample or a clustering choice
- Star-soup with no economic-magnitude discussion
- A DID paper with no event-study/pre-trend figure
- Figures whose axes, units, or parameters are undefined

## Output format

```
【Sample table】source + filters + units documented? [Y/N]
【Main table】FE structure + clustering visible? [Y/N]
【Dynamics figure】event-study/comparative-statics present? [Y/N]
【Notes】self-contained (estimator, sample, SE)? [Y/N]
【Next skill】jfi-writing-style
```
