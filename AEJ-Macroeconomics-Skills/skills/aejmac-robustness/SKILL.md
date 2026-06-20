---
name: aejmac-robustness
description: Use when the headline result of an American Economic Journal: Macroeconomics (AEJ: Macro) manuscript must be shown stable across specification, sample, identification, and tuning choices. Builds the robustness program a macro referee will demand; it does not establish the primary identification or model (use aejmac-identification / aejmac-theory-model first).
---

# Robustness Program (aejmac-robustness)

## When to trigger

- The headline number rests on one specification, one sample, one lag length, or one grid
- A referee could ask "is this an artifact of [choice]?" and you have no panel of alternatives
- The empirical IRF and the model-implied response are compared but only at the baseline
- A structural/calibrated result has never been re-run under alternative targets

## The AEJ: Macro robustness bar

Macro inference is fragile in characteristic ways: **short effective samples**, **structural breaks** (Great Moderation, ZLB, COVID), **specification forks** (lag length, detrending, prior, calibration target), and **method dependence** (SVAR vs. LP; perturbation vs. global). The AEJ: Macro robustness bar is to show the **headline quantity survives the choices a skeptical macro referee would flip**, and to be honest where it does not. Robustness is not a graveyard of extra tables — it is a targeted defense of the specific number the paper claims.

## A macro robustness program (build the panel)

### Empirical (SVAR / LP / narrative)
- **Sample splits**: pre/post-1984 (Great Moderation), exclude/keep the ZLB period, exclude COVID; report whether the response is stable.
- **Specification**: lag length, detrending/filtering choice (HP vs. one-sided vs. none), control set, levels vs. differences.
- **Method cross-check**: if SVAR is baseline, corroborate with LP (and vice versa); agreement is strong evidence.
- **Inference**: alternative HAC bandwidths / clustering; weak-instrument-robust bands for proxy-VAR/LP-IV.
- **Identification variants**: alternative orderings / sign sets / instrument constructions.

### Quantitative (DSGE / HANK / structural)
- **Alternative calibration targets** and parameter ranges; show how the headline quantity moves.
- **Alternative solution method / accuracy** (higher perturbation order, finer grid) where nonlinearity matters.
- **Alternative model elements** (Taylor-rule coefficients, adjustment costs, market structure) the referee will name.
- **Estimation**: alternative moments / priors; re-estimate on a subsample.

### Cross-cutting
- **External validity**: another country / dataset / period where the mechanism should also hold.
- **Placebo / falsification**: a response that should be zero (pre-shock leads; a non-targeted series).

## Reporting discipline

- Lead with a **one-paragraph summary** of what is robust and what is not, then a compact robustness table/figure.
- Keep the **baseline number visible** in every robustness exhibit so the reader sees the movement.
- Put the bulk in the **online appendix**; main text carries the decisive checks only.
- A spec-curve / multiverse plot is powerful for empirical macro when many forks exist.

## Checklist

- [ ] The specific choices a referee would flip are enumerated
- [ ] Sample splits across the relevant macro breaks (Great Moderation / ZLB / COVID)
- [ ] Specification forks (lags, filtering, controls) tested with baseline shown alongside
- [ ] Method cross-check (SVAR↔LP, or perturbation↔global) where both are plausible
- [ ] Quantitative: alternative targets/parameters move the headline within a stated range
- [ ] Placebo/falsification and at least one external-validity check
- [ ] Honest statement of where the result weakens, not just where it holds

## Anti-patterns

- A wall of robustness tables that never restate the baseline, so movement is invisible
- Testing only the choices that confirm the result; omitting the obvious adversarial fork
- Ignoring the ZLB/COVID break in a sample that spans it
- Claiming robustness from one alternative specification
- Hiding a fragile headline behind a forest of irrelevant checks
- "Available upon request" instead of an online-appendix robustness section

## Worked vignette: is the fiscal multiplier a Great-Moderation artifact? (illustrative)

A paper reports a fiscal multiplier of 1.2 from a proxy-VAR on 1960–2019. A referee suspects it is driven by the volatile pre-1984 period. The robustness program: re-estimate on 1984–2019, exclude the ZLB years, and corroborate with local projections using the same narrative instrument. Suppose the multiplier is 1.2 full sample, 1.0 post-1984, 1.4 at the ZLB, all with overlapping bands, and the LP cross-check agrees within 0.1 — the paper then claims a multiplier "around 1.0–1.4 depending on the monetary regime," which is more credible and more interesting than the single number (illustrative).

## Output format

```
【Headline quantity defended】... (baseline value)
【Empirical robustness】sample splits / specs / method cross-check / inference variants
【Quantitative robustness】alt targets / parameters / solution accuracy
【Placebo + external validity】...
【Where it weakens (honest)】...
【Next step】aejmac-tables-figures
```
