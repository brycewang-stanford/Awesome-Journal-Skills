---
name: aejpol-robustness
description: Use when an AEJ: Economic Policy manuscript's headline policy estimate needs to be shown stable and credible against specification, sample, inference, and identification threats. Organizes the robustness program by threat-to-the-policy-conclusion; it does not design the primary identification or write exhibits.
---

# Robustness — Defending the Policy Estimate (aejpol-robustness)

## When to trigger

- The headline causal estimate moves across specifications, or you do not yet know if it does
- A referee will ask "is this robust?" and you have no organized answer
- Inference (clustering, few clusters, multiple outcomes) is not yet airtight
- You need to show the **policy conclusion**, not just a coefficient, survives stress

## Principle: robustness defends the policy conclusion, not the coefficient

At AEJ: Policy, robustness is judged by whether the **policy takeaway** is stable — if the headline estimate is the cost-per-job or the MVPF, show *that* number is stable, with its uncertainty, not merely that a regression coefficient stays significant. Organize the robustness program around the **threats that would change the policy conclusion**, and report enough that a skeptical referee can see each threat addressed.

### Robustness by threat (each maps to a concrete check)

| Threat to the policy conclusion | Check |
|---|---|
| Functional form / controls drive the result | Specification ladder; show the estimate across a coherent set, not a single lucky spec |
| Pre-trends / parallel-trends violation | Honest-DID (Rambachan–Roth) sensitivity bounds; placebo pre-period "effects" |
| Estimator bias under staggered timing | Re-estimate with ≥1 heterogeneity-robust DID estimator (CS / SA / BJS / dCDH) |
| Bandwidth / kernel (RDD) | Bandwidth sweep + bias-corrected CIs; donut-RDD if heaping at the cutoff |
| Weak / invalid instrument | Effective F; AR-robust CI; over-ID test if available |
| Wrong inference / few clusters | Wild-cluster bootstrap; report clustering level sensitivity |
| Multiple outcomes / specifications | Romano–Wolf / sharpened q-values; a specification curve where many specs are run |
| Confounding by an omitted policy/shock | Controls for co-timed policies; event-study around the focal reform only |
| Selection on unobservables | Oster (2019) δ / bounds; argue the implied selection is implausible |
| Sample composition / outliers | Drop influential jurisdictions; winsorize; alternative sample windows |

### Sensitivity that is policy-specific
- If the policy lesson depends on a welfare parameter you calibrate (discount rate, value of a statistic, recycling rule), report the lesson across a plausible range of that parameter, not one value.
- If external validity is the policy worry, show heterogeneity by jurisdiction characteristics and discuss which settings the estimate travels to.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). AEJ: Policy evaluates programs and reforms; the design must carry a policy-relevant magnitude, not just statistical significance.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER, accounts for
  cross-test correlation) or `benjamini_hochberg` — report the adjusted threshold.
- **OVB sensitivity:** `oster_delta` / `sensemakr` — the confounder strength that would
  overturn the headline.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists the missing checks and the
  exact `suggest_function` for each — no guessing the battery.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Keep the decisive checks in the body and the exhaustive (now actually-run) battery in
the appendix. See the executed chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] The headline *policy* number (not just a coefficient) is shown stable across specs
- [ ] The single most likely referee threat is pre-empted with a dedicated exhibit
- [ ] At least one heterogeneity-robust estimator shown where staggered timing applies
- [ ] Inference stress-tested (wild-cluster / AR / multiple-testing as relevant)
- [ ] Selection-on-unobservables addressed (Oster bounds or equivalent)
- [ ] Calibrated welfare parameters varied across a defended range
- [ ] No "kitchen-sink" robustness with no narrative — each check answers a named threat

## Anti-patterns

- A robustness section that is a wall of tables with no statement of which threat each rebuts
- Showing the coefficient is stable while the welfare/policy number is never re-derived
- A specification curve run but only the favorable region discussed
- Treating "still significant" as robustness while ignoring magnitude stability
- Calibrating one welfare parameter value and never probing it

## Sequencing the robustness section for a referee

Order the section so a referee meets the answer before the doubt: (1) the **main heterogeneity-robust
estimate** and its event-study; (2) the **single most likely fatal threat** with its dedicated check;
(3) the **inference** stress-tests; (4) a compact **specification curve or table** of remaining variants;
(5) the **calibrated-parameter sensitivity** for the welfare number. Each subsection ends with one
sentence stating that the *policy conclusion* is unchanged, with its band — not merely that the
coefficient stays signed.

## Worked vignette (illustrative)

A staggered-DID estimate of a minimum-wage change on employment is the basis for a "small disemployment cost" policy claim. A referee will doubt staggered TWFE and pre-trends. The robustness program: CS and SA estimators (estimate within 10% of TWFE, illustrative), flat pre-period leads, an honest-DID bound showing the sign survives a pre-trend twice the largest observed lead, and wild-cluster inference across 30 states. The policy claim — disemployment cost per dollar of raised earnings — is re-derived under each and reported with its band.

## Output format

```
【Headline policy number】the quantity whose stability you defend
【Top 3 threats】ranked by how badly each would change the conclusion
【Checks per threat】[threat → check → result]
【Inference】clustering / few-cluster / multiple-testing handling
【Calibrated-parameter sensitivity】range probed + conclusion stability
【Next step】aejpol-tables-figures
```
