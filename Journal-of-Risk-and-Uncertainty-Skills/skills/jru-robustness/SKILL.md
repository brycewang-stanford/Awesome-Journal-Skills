---
name: jru-robustness
description: Use when a Journal of Risk and Uncertainty (JRU) result may be sensitive to specification, incentive frame, sample, or inference. Organizes robustness by the threat to the risk/uncertainty parameter; it does not invent evidence or citations.
---

# Robustness Strategy (jru-robustness)

## When to trigger

- The headline risk/ambiguity parameter shifts under a different functional form (CRRA vs. CARA vs. expo-power) and you are unsure which to report
- An experimental result might be an artifact of stakes, order, the random-incentive system, or a particular elicitation device
- A referee will ask whether the finding survives EU vs. non-EU specifications, or pooled vs. heterogeneous-type estimation
- Multiple hypotheses are tested across many lottery menus or treatments and no correction is in place

## Organize robustness by threat, not by appendix

A JRU robustness section earns its place when every check is tied to a **specific threat to the parameter's interpretation**. List the threats first, then the check that answers each.

| Threat to the result | The check that addresses it |
|----------------------|-----------------------------|
| Functional-form dependence of the risk parameter | Re-estimate under CRRA, CARA, expo-power; report whether the *qualitative* claim is stable |
| Utility–weighting confound | Show the result holds under a model that separates u from w (e.g., RDU/CPT, not just EU) |
| Elicitation-device artifact | Replicate the pattern with a second device (price list vs. BDM vs. matching probabilities) |
| Random-incentive / isolation failure | Compare one-shot-paid vs. all-paid; test for portfolio/house-money effects |
| Stake / hypothetical-bias sensitivity | Vary real stakes; compare to hypothetical where relevant |
| Subject heterogeneity masked by pooling | Estimate a mixture / finite-type model or random coefficients, not just a representative agent |
| Multiple comparisons across menus/treatments | Adjust (e.g., Holm / Romano–Wolf) and report which results survive |
| Inference too optimistic | Cluster at the subject level; report with few-cluster corrections where needed |

For VSL / insurance empirics, add: alternative risk measures, sample-selection probes, and sensitivity to the publication-selection / meta-analytic benchmark.

## Sequencing

1. Rank threats by how badly each would damage the headline claim if true.
2. Run the check that kills the most dangerous threat first; if the result dies there, stop and rethink before polishing anything.
3. Report robustness as "the *sign and rough magnitude* of [parameter] is stable across [family]," not "Table A12 shows similar results."
4. Distinguish checks that the **design** demands (incentive-frame tests for experiments) from generic ones (alternate clustering).
5. Hand off to `jru-tables-figures` once the parameter is stable across the threats that matter.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JRU spans decision experiments and applied risk; randomization inference for experiments, DiD/IV for observational claims.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or `benjamini_hochberg`.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists missing checks + the exact
  `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Decisive checks in the body, exhaustive battery in the appendix.
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Every robustness exhibit names the threat it addresses
- [ ] The risk parameter is shown stable across at least two functional forms
- [ ] A model that separates utility from probability weighting is among the specifications
- [ ] Experiments: incentive-frame, stake, and order effects probed; second elicitation device where feasible
- [ ] Heterogeneity addressed (mixture / random coefficients) rather than masked by a representative agent
- [ ] Multiple-comparison adjustment applied when many menus/treatments are tested
- [ ] Inference clusters at the subject (or assignment) level; few-cluster issue handled

## Anti-patterns

- A robustness appendix that is a pile of tables with no map from threat to check
- Reporting only the functional form that gives the cleanest number
- Treating an EU-only robustness suite as sufficient when the claim is about non-EU behavior
- Pooling across heterogeneous subjects and presenting the average as if it were a type
- Mining many lottery menus and reporting the significant ones without correction

## Distinguish robustness from a specification search

JRU referees draw a sharp line between *probing a result* and *searching for one*. Stay on the right side of it:

- **Pre-commit the headline specification** and present alternatives as deviations from it, not as a menu you chose among.
- **Report all the forms you ran**, including the ones where the estimate weakened — selective reporting reads as a fishing expedition to a specialist.
- **State the decision rule** for when the result "survives": e.g., the sign holds and the magnitude stays within a stated band across forms and devices.
- For experiments, distinguish **pre-registered** confirmatory checks from exploratory ones, and label them as such.

## Robustness the experiment specifically demands

Lab and field elicitation papers carry threats that generic econometric robustness misses:

- **Comprehension and noise:** show the result is not driven by subjects who failed comprehension checks; consider a trembling-hand / Fechner noise term rather than dropping "irrational" subjects.
- **Incentive realism:** compare real vs. hypothetical, and high vs. low stakes, where the claim depends on it.
- **Within-subject consistency:** report test-retest or internal consistency for the elicited parameter.

## Worked vignette (illustrative)

A paper reports loss aversion λ ≈ 2.1 from a choice-list experiment. The most dangerous threat is that λ is an artifact of the **list format** (multiple switching, framing). The first check replicates the estimate with a second device (matching probabilities); the second re-estimates under CPT vs. a reference-dependent EU baseline; the third splits by a mixture model to confirm λ is not driven by a confused minority. Only after λ survives all three — with the across-device range reported in full — does the paper present it as the headline in `jru-tables-figures`.

## Output format

```text
【Journal】Journal of Risk and Uncertainty
【Skill】jru-robustness
【Verdict】robust / patch / result fragile
【Top threat】<the check that would most damage the claim>
【Threat→check map】<list>
【Parameter stability】sign+magnitude across <families/devices>
【Heterogeneity】mixture / random coefficients / not addressed
【Source status】verified / 待核实 / not asserted
【Next skill】jru-tables-figures
```
