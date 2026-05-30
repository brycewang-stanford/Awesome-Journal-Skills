---
name: jf-tables-figures
description: Use when finalizing tables and figures for a The Journal of Finance (JF) manuscript. Enforces accessible, self-contained, publication-grade exhibits; it does not decide which results to run.
---

# Tables & Figures (jf-tables-figures)

## When to trigger

- The main tables have too many columns / too much information density
- Tables show t-statistics inconsistently, or omit the standard-error correction in the note
- Figures are low-resolution, over-plotted, or pasted screenshots of Stata/R output
- A referee or copy editor will say a table "cannot be read without the text"

## JF exhibit norms

JF articles are general-interest and somewhat shorter; main exhibits must be **few, clean, and self-contained**. A reader should understand each table or figure from its title, headers, and note alone. Deep diagnostic tables move to the Internet Appendix (`jf-internet-appendix`).

### Table structure (clean, no vertical rules)

```
Table III. Effect of the Reform on Firm Leverage
-----------------------------------------------------------------
                          (1)        (2)        (3)
                       Leverage   Leverage   Leverage
-----------------------------------------------------------------
Treat x Post           0.041***   0.038***   0.040***
                       (0.012)    (0.011)    (0.013)
  Controls                No         Yes        Yes
  Firm FE                 Yes        Yes        Yes
  Year FE                 Yes        Yes        Yes
  Observations          48,210     48,210     48,210
  Adjusted R^2           0.61       0.64       0.65
-----------------------------------------------------------------
Standard errors clustered by firm in parentheses.
***, **, * denote significance at 1%, 5%, 10%.
```

### Conventions
- Report standard errors in parentheses (not t/z) and state the clustering / correction in the note.
- Significance via `***/**/*`, defined in the note.
- Keep columns to what the reader needs; do not stack a dozen specifications in one main table.
- One reported R²/pseudo-R² is enough — do not pile on AIC/BIC/within-R².
- Table caption above; note below. Number with the journal's running scheme (e.g., Roman numerals as JF uses).
- For asset-pricing tables, label test assets, weighting (EW/VW), breakpoints, and the factor model used as controls.

## Figure norms

- Vector or ≥300 dpi; legible at print size.
- A small, restrained palette; distinguishable in greyscale where feasible.
- Each figure self-contained: axis labels, units, sample, and source/note.
- Common JF figures: event-study coefficient plots with CIs; cumulative long-short returns; sorted-portfolio mean returns; binned scatter / RDD plots.
- Do not over-plot: a few series, clearly labeled, beat ten overlapping lines.

## Checklist

- [ ] Each main table/figure is self-contained (readable from caption + note alone)
- [ ] Standard-error type and clustering/correction stated in every table note
- [ ] No vertical rules; clean horizontal-rule layout; consistent decimals
- [ ] Columns limited to what supports the claim; diagnostics pushed to the Internet Appendix
- [ ] Asset-pricing tables state weighting, breakpoints, test assets, and benchmark factors
- [ ] Figures are vector/≥300 dpi, legible in greyscale, with units and source
- [ ] Table/figure numbering matches in-text references exactly

## Anti-patterns

- A 12-column main table no one can parse
- Reporting t-stats in some tables and SEs in others
- Omitting the clustering level from the note ("a referee cannot tell how you got the SEs")
- Pasting raw Stata/R output as an image
- A figure with five line styles, five colors, and a paragraph-length legend
- Tables whose magnitudes are never interpreted in the text

## Output format

```
【Main exhibits】X tables / Y figures
【Self-contained?】yes / no
【SE note present in all tables?】yes / no
【Greyscale-legible figures?】yes / no
【Diagnostics moved to appendix?】yes / no
【Next step】jf-internet-appendix
```
