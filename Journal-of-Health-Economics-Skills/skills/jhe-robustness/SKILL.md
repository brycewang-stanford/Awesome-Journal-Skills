---
name: jhe-robustness
description: Use when a Journal of Health Economics (JHE) result must be shown stable to specification, sample, inference, and mechanism threats before submission or in response to referees. Organizes robustness by identifying threat; it does not establish the design (jhe-identification) or build exhibits.
---

# Robustness Strategy (jhe-robustness)

## When to trigger

- The headline estimate may be sensitive to specification, sample window, or functional form
- Inference is suspect: few clusters (states), serial correlation, or multiple outcomes/subgroups
- A referee will ask whether the result is a coverage/take-up artifact rather than the claimed effect
- The mechanism story is asserted but not separated from competing explanations

## Robustness the JHE way: organize by threat, not by appendix

A wall of starred alternative specifications persuades no one. JHE referees want each robustness check **mapped to a specific threat to the health-economics claim**, with the point estimate's *stability* — not its significance — as the object. Build the robustness section as a threat-response ledger: name the threat a health economist would raise, run the check that addresses it, and report whether the magnitude moves. The threats that recur at JHE are selection, concurrent policy, measurement of health/utilization, and inference with few policy clusters.

## Threat-to-check ledger

| Threat to the claim | Check that addresses it |
|---------------------|-------------------------|
| Residual selection into insurance/treatment | bounds (Lee/Manski/Oster); selection-on-observables-to-unobservables (Oster δ) |
| Concurrent reform contaminates the policy variation | placebo on ineligible group/period; leave-one-reform-out; pre-period falsification |
| Staggered-timing bias | heterogeneity-robust estimator (CS / SA / dCDH); honest-DID sensitivity |
| Health/utilization mismeasurement (claims coding, self-report) | alternative outcome definitions; administrative vs. survey cross-check; coding-change robustness |
| Functional form / sample window | log vs. level, trimming outliers (skewed health spending!), alternative bandwidths, donut RD |
| Few-cluster inference (states) | wild-cluster bootstrap; randomization inference; correct clustering level |
| Multiple outcomes/subgroups | MHT adjustment (Romano–Wolf / sharpened q-values); pre-specify the primary outcome |
| Mechanism is one of several | horse-race the channels; show the competing story predicts a pattern you do not see |

## Sequencing

1. **Lead with the threat the editor/referee will raise first** — usually selection or concurrent policy at JHE.
2. **Report stability, not stars.** Show the point estimate across checks in one figure or compact table; if it moves, say so and explain.
3. **Right-size the spending/skew problem.** Health expenditure is heavily right-skewed and zero-inflated; defend the estimator (two-part, GLM, IHS) rather than defaulting to OLS on a log.
4. **Treat inference as a first-class robustness item**, not a footnote — few-state clustering is a classic JHE referee catch.
5. **Pre-register the primary outcome** where multiple health outcomes invite cherry-picking.
6. **Show, do not assert, stability.** A single figure plotting the point estimate and CI across every check is worth more than a paragraph claiming robustness; a referee can read it in seconds.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JHE is health economics — insurance/program reforms and selection; foreground DiD/IV/RDD and selection corrections.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or `benjamini_hochberg`.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists missing checks + the exact
  `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Decisive checks in the body, exhaustive battery in the appendix.
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Every robustness check is mapped to a named threat to the health-econ claim
- [ ] Point-estimate stability is the reported object (not just significance)
- [ ] Selection and concurrent-policy threats are addressed head-on
- [ ] Skewed/zero-inflated health spending handled with a defended estimator
- [ ] Inference matches the design: correct clustering level + few-cluster correction
- [ ] Multiple outcomes/subgroups get MHT adjustment; primary outcome pre-specified
- [ ] The mechanism is distinguished from at least one competing explanation

## Anti-patterns

- A leave-out or alternative-sample check run but never reconciled when the estimate moves
- An appendix of starred specifications with no map from check to threat
- OLS on log spending with no handling of zeros or skew
- Clustering below the policy level, then claiming significance
- Running every subgroup and reporting the significant ones with no MHT adjustment
- "Results are robust" with no figure showing the point estimate holding
- Dodging the selection threat with more controls instead of a bound or design fix

## The skewed-spending decision, made explicitly

Health spending and utilization are the journal's signature dependent variables, and they are right-skewed, zero-inflated, and heavy-tailed — the estimator choice is itself a robustness question a referee will press. Make it a deliberate, defended choice rather than a default:

- **Many zeros + continuous positive part** → two-part model (probit/logit for any use × GLM for the positive amount); report both parts.
- **Skew without excess zeros** → GLM with a log link (often gamma), which avoids retransformation bias that plagues OLS-on-log.
- **Want to keep zeros and interpret in levels** → IHS or Poisson/PPML, stating the elasticity interpretation honestly.
- Whatever you pick, **show the result is not an artifact of the functional form** by reporting at least one alternative, and never present OLS-on-log as if retransformation were free.

## Worked vignette (illustrative)

A provider-payment paper shows intensity rises after a fee change; a referee suspects it is patient selection, not a true behavioral response. The JHE fix: hold the threat ledger explicit — (a) an Oster δ shows selection on unobservables would need to be 2× the observables to overturn the result; (b) a placebo on a fee-unaffected service shows no jump; (c) the spending outcome is re-run with a two-part model given 30% zeros; (d) inference is wild-cluster bootstrapped over 41 providers. The point estimate holds across all four (say 6.2%, stable within ±0.8pp, illustrative). The mechanism — behavioral response, not selection — now survives.

## Output format

```text
【Journal】Journal of Health Economics
【Skill】jhe-robustness
【Primary threat】selection / concurrent-policy / staggered-bias / measurement / inference
【Threat→check ledger】[threat: check → estimate movement]
【Spending estimator】OLS / two-part / GLM / IHS — defended? [Y/N]
【Inference】clustering level + few-cluster correction
【MHT】adjusted across outcomes/subgroups? [Y/N]
【Verdict】estimate stable / moves (explained) / fragile
【Next skill】jhe-tables-figures
```

## Handoff boundary

This skill stress-tests an already-identified estimate; it does not fix a broken design (that is `jhe-identification`) or present the results (that is `jhe-tables-figures`). If a robustness check reveals the estimate is not actually identified — it swings with the selection bound or fails the placebo — route back to `jhe-identification` rather than papering over it with more specifications. When the point estimate holds across the threat ledger, hand off to `jhe-tables-figures` to make the stability legible.
