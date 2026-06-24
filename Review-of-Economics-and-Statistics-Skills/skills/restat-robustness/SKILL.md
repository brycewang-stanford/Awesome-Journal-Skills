---
name: restat-robustness
description: Use when the headline estimate of a The Review of Economics and Statistics (REStat) manuscript needs to survive specification, sample, measurement, and inference choices before submission. Builds the robustness suite that REStat referees expect; it does not establish the primary identification.
---

# Robustness Suite (restat-robustness)

## When to trigger

- The main estimate exists but its stability under reasonable alternatives is untested
- A referee could ask "does this survive [specification / sample / inference] choice?"
- Inference rests on conventional SEs without checking clustering / few-cluster / multiple-testing
- The result might be an artifact of how a variable was measured

## The REStat robustness bar

REStat referees ask whether the headline number is **a fact about the world or an artifact of choices**. The persuasive paper shows the estimate is **stable across the specifications a skeptic would try**, and is honest where it is fragile. Because REStat weights **measurement**, robustness here includes a dimension siblings sometimes skip: **robustness to measurement choices** (alternative measures, error corrections, construct definitions). Robustness is not a kitchen sink — it is a **targeted defense** of the specific threats this design invites (route the threat menu via `restat-referee-strategy`).

## The five robustness dimensions

| Dimension | What to vary | Pass condition |
|-----------|--------------|----------------|
| **Specification** | Controls, fixed effects, functional form, sample restrictions | Headline stable in sign and rough magnitude |
| **Sample** | Subperiods, leave-one-group-out, trimming outliers, alt. universe | No single group/period drives the result |
| **Measurement** | Alternative measures of outcome/regressor, error corrections, construct defs | Conclusion not an artifact of one measure |
| **Identification** | Alternative estimators (het-robust DID, alt bandwidth/IV), placebo/falsification | Design-appropriate estimators agree; placebos null |
| **Inference** | Clustering level, wild-cluster bootstrap (few clusters), randomization inference, multiple-testing correction | SEs valid under the data's dependence; key results survive MHT |

## Building the suite

1. **Start from the threats, not the menu.** List the 4–6 objections this exact design invites; each gets a robustness exhibit. (`restat-referee-strategy`)
2. **One headline, many checks.** Keep a single main estimate; show alternatives orbit it in a robustness table or a coefficient-stability plot.
3. **Report, don't bury, fragility.** If an estimate weakens under a defensible alternative, say so and bound it — referees trust honest authors.
4. **Specification curve where appropriate.** For results sensitive to many small choices, a specification curve shows the full distribution rather than cherry-picked rows.
5. **Inference last and seriously.** Cluster at the assignment level; with few clusters use wild-cluster bootstrap; adjust for multiple outcomes (Romano–Wolf / sharpened q-values).

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). REStat is applied econometrics/empirical micro — the home of careful identification; DiD/IV/RDD with weak-IV-robust CIs.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or `benjamini_hochberg`.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists missing checks + the exact
  `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Decisive checks in the body, exhaustive battery in the appendix.
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Headline estimate stable across the controls/FE/functional-form a skeptic would try
- [ ] Sample robustness: leave-one-out / subperiod / trimming shown; no single group drives it
- [ ] Measurement robustness: alternative measure(s) and/or error correction reported
- [ ] Alternative design-appropriate estimators agree; placebo/falsification tests null
- [ ] Inference: clustering justified; few-cluster fix applied; multiple-testing handled
- [ ] Fragility, where it exists, is reported and bounded — not hidden
- [ ] Robustness exhibits map to the specific threats this design invites

## Anti-patterns

- A robustness "kitchen sink" unconnected to the design's actual threats
- Reporting only the specifications that work; omitting the obvious skeptical one
- Conventional SEs with a handful of clusters (mechanical over-rejection)
- Many outcomes, no multiple-testing correction (referees will recompute)
- Ignoring measurement-robustness — a REStat-specific gap referees catch
- A specification curve presented as decoration without reading off what it implies

## Worked vignette: the measurement-robustness check a referee demanded (illustrative)

A health paper estimates the effect of a clinic-opening on infant mortality, using a registry-based mortality
rate. The headline is robust to controls, sample, and clustering — but a REStat referee notes the registry
under-counts deaths in remote areas, and under-counting is correlated with clinic access (where clinics
opened, reporting also improved). This is non-classical measurement error that could create the result. The
robustness answer is not another control set: it is an **alternative outcome** (survey-based mortality from an
independent source) plus a **bounding exercise** under plausible mis-reporting rates. The effect survives the
survey measure and the bounds exclude zero — a measurement-robustness defense siblings often skip but REStat
expects. This is the dimension that most often separates a REStat accept from a revise.

## Output format

```
【Headline estimate】[point + SE], identified by [design]
【Specification】stable across: [controls/FE/form] → [Y/N + range]
【Sample】leave-one-out / subperiod / trimming → [Y/N]
【Measurement】alt measure / error correction → [result]
【Identification】alt estimators agree? placebos null? [Y/N]
【Inference】clustering: [level]; few-cluster: [wild bootstrap?]; MHT: [method]
【Honest fragility】[where it weakens + bound] — or "robust throughout"
【Next step】restat-tables-figures
```
