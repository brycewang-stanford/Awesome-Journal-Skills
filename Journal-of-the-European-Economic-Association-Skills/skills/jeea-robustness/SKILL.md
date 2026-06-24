---
name: jeea-robustness
description: Use when the headline result of a Journal of the European Economic Association (JEEA) manuscript needs to be shown stable to specification, sample, inference, and (for theory) assumption perturbations. Organizes robustness around the actual threats a general-interest referee will raise; it does not design the main result.
---

# Robustness (jeea-robustness)

## When to trigger

- The main estimate moves when a referee imagines a different specification
- Inference rests on assumptions (homoskedasticity, few clusters) you have not stressed
- A theory result might hinge on one functional form or parameter range
- You have a pile of "robustness tables" but no organizing logic

## The JEEA robustness bar

A general-interest referee does not want a wall of extra columns — they want to know the **headline result survives the threats that matter**. Organize robustness by **threat to the claim**, not by "more specifications." Each robustness exhibit should answer a specific objection a JEEA referee would raise, and the headline magnitude should be **stable in sign and roughly in size** across the credible perturbations. Report everything as **standard errors / confidence sets, never significance asterisks**, and ensure every robustness check is reproducible for the **JEEA Data Editor** check.

## Robustness organized by threat

| Threat to the claim | Robustness response |
|---------------------|---------------------|
| Omitted variables / selection | Oster (2019) δ and bounded bias; alternative controls; coefficient-stability discipline |
| Estimator bias (staggered DID) | heterogeneity-robust estimators (CS / SA / BJS / dCDH) as the main result, not an aside |
| Weak / invalid instrument | first-stage strength; Anderson–Rubin / weak-IV-robust sets; over-ID where available |
| Wrong inference | clustering at the right level; wild-cluster bootstrap with few clusters; randomization inference |
| Sample / outliers | winsorize / trim; alternative samples and time windows; influential-observation checks |
| Functional form | alternative specifications; semiparametric or flexible controls |
| Multiple hypotheses | Romano–Wolf / FDR adjustment when many outcomes/subgroups |
| Theory: assumption fragility | relax the driving assumption; show the result degrades smoothly, not knife-edge |

## Principles

- **One threat, one exhibit, one sentence.** Each robustness check maps to a named objection and a one-line conclusion.
- **Main result = the credible estimator.** Do not bury the heterogeneity-robust DID in an appendix while TWFE leads.
- **Stability, not significance-chasing.** The point is the magnitude holds, not that it stays starred (and there are no stars at JEEA).
- **Pre-empt, don't pad.** Cut robustness checks no referee would ask for; add the ones `jeea-referee-strategy` flags.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JEEA is a general-interest European economics flagship; credible identification across applied fields.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or `benjamini_hochberg`.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists missing checks + the exact
  `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Decisive checks in the body, exhaustive battery in the appendix.
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Robustness organized by threat, each tied to a specific referee objection
- [ ] Heterogeneity-robust estimator is the main result where staggered timing applies
- [ ] Inference stressed: clustering level justified; wild-cluster bootstrap if few clusters
- [ ] Selection/OVB addressed (Oster δ or design-based defense)
- [ ] Multiple-testing handled when many outcomes/subgroups
- [ ] Theory: driving assumption relaxed; result shown not knife-edge
- [ ] Every check reproducible; no significance asterisks anywhere

## Worked vignette (illustrative)

A draft has fifteen robustness columns and a referee still calls the result fragile. The problem is that none of the fifteen addresses the actual threat — selection into treatment. The JEEA-grade fix cuts the padding and adds the three checks the threat demands: an Oster δ showing the bias needed to overturn the result exceeds 1, a placebo on a group the mechanism predicts should show no effect, and wild-cluster inference because there are only twelve treated units. One paragraph, three exhibits, threat neutralized — far more persuasive than fifteen columns of "add another control."

## Main-text vs. online-appendix split

JEEA papers carry an online appendix, so use it to keep the main text focused: the **headline robustness** (the credible estimator, the key placebo, the inference fix) belongs in the main text; the **exhaustive grid** (every control set, every sample window) belongs in the appendix, referenced in one sentence. Do not bury the result-deciding check in the appendix, and do not pad the main text with checks no referee asked for.

## Anti-patterns

- A dozen robustness columns with no statement of which threat each addresses
- TWFE as the headline with the modern estimator hidden in the online appendix
- "Robust to controls" while the real threat (selection, weak IV) is untouched
- Reporting that results "remain significant" instead of that the magnitude is stable
- Robustness checks that quietly change the sample or estimand without flagging it
- The result-deciding robustness check buried in the online appendix

## Output format

```
【Threats addressed】[OVB / estimator / weak-IV / inference / sample / form / MHT / assumption]
【Main result estimator】[the credible one, not TWFE-only]
【Stability verdict】[sign + magnitude hold? Y/N, with the range]
【Inference】[clustering level; wild-cluster/RI if needed]
【Residual fragility】[what still moves the result]
【Next step】jeea-tables-figures
```
