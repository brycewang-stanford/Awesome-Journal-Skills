---
name: jf-robustness
description: Use when planning or auditing the robustness, sensitivity, and multiple-testing battery for a The Journal of Finance (JF) manuscript. Decides which checks are load-bearing; it does not design the main test.
---

# Robustness & Sensitivity (jf-robustness)

## When to trigger

- The main result is in but the robustness section is thin or scattershot
- A factor / anomaly result flips when you change the sample, weighting, or factor model
- A referee will ask "does this survive [alternative measure / subperiod / specification]?"
- You have many candidate checks and need to know which are decisive vs. filler

## Principle: robustness defends the claim, it does not pad it

JF wants a focused battery that targets the **specific threats** to *your* claim, not a wall of 30 regressions. Each check should answer a question a sophisticated referee would actually raise. Secondary checks belong in the Internet Appendix (see `jf-internet-appendix`); the main text shows the few that matter.

## Robustness map by paper type

### Corporate / empirical (causal claim)
- Alternative measures of the outcome and treatment
- Alternative control sets and fixed-effects structures (does the effect survive saturated FE?)
- Sample-composition checks (drop crisis years, drop the largest sector, balanced vs. unbalanced panel)
- Alternative clustering / standard-error assumptions
- Sensitivity to unobservables (Oster δ; Rosenbaum bounds for matched designs)
- Placebo outcomes that should NOT move

### Asset pricing (cross-section / predictability)
- Equal- vs. value-weighting; NYSE breakpoints; exclude microcaps / penny stocks
- Subperiods (pre/post a structural break; first vs. second half)
- Alternative factor models as controls (FF3 → FF5 → q-factor → +MOM)
- Transaction-cost / implementability haircut on the long-short return
- Out-of-sample and post-publication-period performance
- Multiple-testing adjustment when the signal was selected from many

## The multiple-testing red line

If the headline result was chosen from a search over many signals, specifications, or cuts, a naive t > 2 is **not** evidence. Report an adjusted hurdle (FDR / Bonferroni / the elevated thresholds in Harvey–Liu–Zhu) and disclose the size of the search. JF referees treat undisclosed specification search as a fatal flaw, not a minor one.

## Checklist

- [ ] Each robustness check maps to a named threat to the main claim
- [ ] The result survives the most adversarial reasonable specification, not just friendly ones
- [ ] Alternative measures / samples / weighting are shown (asset pricing: value-weighting + breakpoints)
- [ ] Sensitivity to unobservables (corporate) or multiple testing (asset pricing) is addressed
- [ ] Out-of-sample / subperiod evidence is present where the claim is predictive
- [ ] Magnitudes (not just significance) are stable across checks; instability is disclosed, not hidden
- [ ] The main text keeps only decisive checks; the rest are flagged for the Internet Appendix

## Anti-patterns

- A "kitchen-sink" robustness table where every cell is significant and none is explained
- Reporting only the specifications that work and omitting the search
- Treating value-weighted failure of an equal-weighted result as a footnote
- Adding controls until significance appears, then reporting that as "robust"
- Claiming robustness while the economic magnitude swings by an order of magnitude across cuts

## Output format

```
【Paper type】corporate-empirical / asset-pricing
【Decisive checks (main text)】[...]
【Appendix checks】[...]
【Multiple-testing / unobservables addressed?】yes / no
【Most adversarial spec survived?】yes / no — [detail]
【Magnitude stability】stable / disclosed instability
【Next step】jf-tables-figures
```
