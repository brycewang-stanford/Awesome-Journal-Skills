---
name: aeja-robustness
description: Use when an American Economic Journal: Applied Economics (AEJ: Applied) manuscript's headline estimate must be shown to survive specification, sample, and inference choices before submission or in an R&R. Builds the robustness suite a sophisticated referee expects; it does not establish the primary identification (aeja-identification) or format the exhibits (aeja-tables-figures).
---

# Robustness Suite (aeja-robustness)

## When to trigger

- The main estimate is in hand and you need to show it is not an artifact of one specification
- A referee asks "is this robust to [alternative controls / sample / functional form / inference]?"
- The result depends on a bandwidth, a clustering choice, or a sample-selection rule that could be questioned
- You suspect specification-search concerns and want to pre-empt them

## The AEJ: Applied robustness bar

AEJ: Applied referees probe whether the headline number is **stable, honestly inferred, and not the product of researcher degrees of freedom**. Robustness here is not a wall of regressions — it is a **targeted set of checks each tied to a specific threat to the design**. Map every plausible objection to the one check that answers it, and report the checks so the reader sees the estimate barely moves.

| Threat to the result | The check that answers it |
|----------------------|---------------------------|
| Omitted confounders | Oster δ / coefficient-stability bounds; added controls in steps |
| Specification search | a specification curve / multiverse; pre-registered primary spec |
| Functional form | levels vs logs, alternative outcome definitions, nonparametric version |
| Sample selection | drop influential units, alternative inclusion rules, balanced vs unbalanced panel |
| Inference too narrow | clustered SEs at the right level, wild-cluster bootstrap (few clusters), randomization inference |
| Design-specific fragility | DID: honest-DID bounds; RD: bandwidth/donut; IV: weak-IV-robust set |
| Multiple outcomes/subgroups | Romano–Wolf / List–Shaikh–Wooldridge MHT adjustment |

## Robustness craft

1. **Lock the primary specification first.** Everything else is a perturbation around it; do not present five co-equal specs and let the reader guess which is preferred.
2. **One threat → one check.** A robustness table should read as "here is the worry, here is the evidence it is not a problem."
3. **Show stability, not just significance.** The persuasive object is that the *point estimate* barely moves, not that it stays starred.
4. **Be honest about where it weakens.** A check that shifts the estimate is information; report it and bound the implication rather than hiding it.
5. **Match inference to the data structure** (clustering, spatial dependence, few clusters) — wrong SEs are the most common AEJ: Applied robustness failure.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). AEJ: Applied is applied microeconomics — labor, health, education, and development field settings where a clean research design is the entry ticket.

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

- [ ] Primary specification declared (ideally pre-registered) before perturbations
- [ ] Each robustness check mapped to a specific threat, not added for volume
- [ ] Coefficient-stability evidence (Oster δ or stepwise controls) for selection-on-unobservables
- [ ] Inference stress-tested: correct clustering level + wild-cluster/randomization inference where relevant
- [ ] Design-specific sensitivity included (honest-DID / RD bandwidth / weak-IV set)
- [ ] Multiple-hypothesis adjustment if many outcomes/subgroups
- [ ] Stability of the *point estimate* shown, and any check that moves it reported honestly

## Anti-patterns

- A 20-column robustness table with no map from check to threat ("kitchen-sink robustness")
- Reporting only that significance survives while the point estimate wanders
- Hiding the specification that breaks the result
- Clustering at the wrong level or ignoring few-cluster bias, then claiming robustness
- Treating "added more controls and it survived" as sufficient for selection on unobservables
- Subgroup p-hacking with no MHT correction

## Worked vignette (illustrative)

An IV estimate of the return to a training program is 0.11 (s.e. 0.04). The robustness suite: (i) effective F of 23 rules out weak instruments; (ii) the Anderson–Rubin 95% set is [0.04, 0.19], so inference is not weak-IV-fragile; (iii) Oster δ implies selection on unobservables would need to be 1.8× selection on observables to nullify it; (iv) wild-cluster bootstrap with 14 clusters keeps the CI away from zero; (v) dropping the largest region moves the estimate to 0.10. The point estimate barely moves — the AEJ: Applied target.

## Referee pushback mapped to the robustness fix

- *"This looks like specification search."* → Declare the pre-registered or primary spec; show a
  specification curve in which the point estimate barely moves.
- *"Did you cluster correctly?"* → Cluster at the assignment level; with few clusters report a wild-cluster
  bootstrap or randomization-inference p-value.
- *"Could selection on unobservables explain this?"* → Report Oster δ; state how strong selection on
  unobservables would have to be (relative to observables) to nullify the result.

## Output format

```
【Primary spec】declared / pre-registered? [Y/N] — estimate: ___ (s.e. ___)
【Threat → check map】selection: ___ | spec-search: ___ | form: ___ | sample: ___ | inference: ___ | design: ___
【Inference】clustering level: ___; few-cluster/randomization: ___
【Design sensitivity】honest-DID / RD bandwidth / weak-IV set: ___
【Estimate stability】range across checks: [___, ___]; checks that move it: ___
【Next step】aeja-tables-figures
```
