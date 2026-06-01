---
name: jpube-tables-figures
description: Use when designing the exhibits for a Journal of Public Economics (JPubE) manuscript — bunching density plots, event-study and RD/RKD graphs, incidence and distributional figures, and self-contained tables. Makes the public-finance design visible; it does not run the analysis (use jpube-data-analysis).
---

# Tables & Figures (jpube-tables-figures)

## When to trigger

- The identifying variation is buried in a regression table instead of shown in a graph
- A bunching, RD, or event-study result has no picture
- Tables are dense, under-noted, or not callable in order
- You need exhibits that make a policy elasticity legible to a referee

## Why figure-forward at JPubE

JPubE's identification often *is* a picture — a spike of excess mass at a tax kink, a jump at an eligibility cutoff, a clean break at a reform date. Because referees are public-finance specialists assessing design credibility, **the headline of a JPubE empirical paper is frequently one transparent graph** that lets the reader see the response before any regression. Build exhibits so the design is self-evident.

## Exhibit norms

- **Lead with the design figure.** Bunching: observed density vs. smooth counterfactual around the kink/notch, with the excluded region marked. RD/RKD: binned scatter with the fitted discontinuity/kink and CIs. DID: event-study plot with leads and zero-line.
- **Show, then estimate.** A figure that makes the response visible earns more trust than a coefficient; the table quantifies what the figure shows.
- **Distributional / incidence plots** where the contribution is about who bears a tax or gains from a transfer.
- **Self-contained notes.** Each table/figure note states the sample, data source (and restricted-access caveat), the estimator, the inference (clustering level), and the units — readable without the text.
- **Clean tables.** Report the policy parameter (elasticity, MVPF, take-up) prominently; avoid 10-column kitchen-sink tables; put diagnostics in clearly labeled panels.
- **Print quality.** Vector output (PDF/EPS); legible at print size; minimal chartjunk (no 3D, restrained color); confidence bands shown.

## Checklist

- [ ] A design figure leads the empirical section (bunching / RD / event-study)
- [ ] The policy parameter (elasticity / MVPF / take-up) is prominent in the main table
- [ ] Every exhibit is callable in order and self-contained via its note
- [ ] Notes state sample, source + access caveat, estimator, clustering, units
- [ ] Distributional / incidence exhibit included where the contribution warrants
- [ ] Vector graphics, confidence bands shown, chartjunk removed

## Anti-patterns

- Hiding a bunching or RD result inside a regression table with no plot
- Figures with no confidence bands or no marked counterfactual / excluded region
- Notes that omit the data source or the restricted-access caveat
- A 10-column main table where the key elasticity is one buried row

## Output format

```
【Lead figure】bunching / RD / RKD / event-study — present? [Y/N]
【Key parameter visible】elasticity / MVPF / take-up in main table? [Y/N]
【Notes self-contained】sample/source/estimator/clustering/units? [Y/N]
【Distributional exhibit】[present / not needed]
【Print quality】vector + bands + low chartjunk? [Y/N]
【Next step】jpube-writing-style
```
