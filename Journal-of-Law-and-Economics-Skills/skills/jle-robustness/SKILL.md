---
name: jle-robustness
description: Use when a The Journal of Law and Economics (JLE) manuscript's headline estimate must be shown to survive specification, sample, jurisdiction, and inference choices before submission or in an R&R. Builds the robustness suite a law-and-economics referee expects; it does not establish the primary identification (jle-identification) or format the exhibits (jle-tables-figures).
---

# Robustness Suite (jle-robustness)

## When to trigger

- The main estimate of a legal/regulatory effect is in hand and you must show it is not an artifact of one specification
- A referee asks "is this robust to alternative controls / sample / which jurisdictions / how you date the rule?"
- The result depends on a bandwidth, a clustering choice, a treatment date, or a sample of included jurisdictions that could be questioned
- You suspect specification-search concerns and want to pre-empt them

## The JLE robustness bar

JLE referees — economists who know the institution — probe whether the estimated effect of the rule is **stable, honestly inferred, and not the product of researcher degrees of freedom**, with special attention to **legal-design choices**: how you dated the rule, which jurisdictions you treated as controls, whether enforcement was uniform. Robustness here is not a wall of regressions; it is a **targeted set of checks each tied to a specific threat to the legal identification**. Map every plausible objection to the one check that answers it, and show the point estimate barely moves.

| Threat to the result | The check that answers it |
|----------------------|---------------------------|
| Omitted confounders | Oster δ / coefficient-stability bounds; controls added in steps |
| Wrong treatment date | re-date to signing vs. effective vs. enforcement onset; donut around the date |
| Contaminated control jurisdictions | drop jurisdictions with contemporaneous reforms; alternative donor pools; placebo on uncovered legal areas |
| Specification search | a specification curve; declare the primary spec up front |
| Functional form | levels vs. logs, alternative outcome/penalty definitions, nonparametric version |
| Sample / jurisdiction selection | leave-one-state-out, balanced vs. unbalanced panel, drop the largest jurisdiction |
| Inference too narrow (few jurisdictions) | cluster at the legal-variation level; wild-cluster bootstrap; randomization/permutation inference |
| Design-specific fragility | DiD: honest-DID bounds; RD: bandwidth/donut; IV: weak-IV-robust set |

## Robustness craft

1. **Lock the primary specification first.** Everything else perturbs around it; do not present five co-equal specs and let the reader guess the preferred one.
2. **One threat → one check.** A robustness table should read "here is the worry, here is the evidence it is not a problem."
3. **Stress the legal-design choices specifically.** Re-dating the rule, swapping the control jurisdictions, and varying enforcement assumptions are the JLE-characteristic checks a referee who knows the institution will demand.
4. **Show stability of the point estimate**, not just surviving significance.
5. **Match inference to the data structure.** With few states/jurisdictions, asymptotic clustered SEs over-reject; report a wild-cluster bootstrap or randomization inference — the single most common JLE robustness failure.
6. **Be honest about where it weakens.** A check that moves the estimate is information; report it and bound the implication.
7. **Use placebos on uncovered legal areas.** A distinctive and persuasive JLE robustness move is a placebo on an outcome the rule should *not* affect (an uncapped tort alongside a capped one, an unregulated adjacent market) — a null there isolates the legal channel far more credibly than another control regression.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JLE is empirical law-and-economics — DiD around legal/regulatory change is central.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or `benjamini_hochberg`.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists missing checks + the exact
  `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Decisive checks in the body, exhaustive battery in the appendix.
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Primary specification declared before perturbations
- [ ] Each robustness check mapped to a specific threat, not added for volume
- [ ] Treatment-date sensitivity shown (signing vs. effective vs. enforcement)
- [ ] Control-jurisdiction sensitivity shown (drop contaminated, leave-one-out, placebo legal area)
- [ ] Coefficient-stability evidence (Oster δ or stepwise) for selection on unobservables
- [ ] Inference at the legal-variation level + wild-cluster/randomization where jurisdictions are few
- [ ] Design-specific sensitivity (honest-DID / RD bandwidth / weak-IV set)
- [ ] Stability of the point estimate shown; any check that moves it reported honestly

## Separating identification robustness from policy interpretation

Keep the robustness section about whether the *estimate of the legal effect* is stable, and do not let it drift into re-arguing the rule's normative merits. A referee wants to know the number survives re-dating, control swaps, and correct inference — not your view on whether the rule is good policy. Park the welfare and policy discussion in its own section (see `jle-theory-model`) so the robustness evidence reads as clean, mechanical stress-testing of the identified effect.

## Anti-patterns

- A 20-column robustness table with no map from check to threat ("kitchen-sink robustness")
- Clustering at the firm or case level when the legal variation is at the state level, then claiming robust precision
- Ignoring few-cluster bias with a dozen states and reporting naive clustered SEs
- Hiding the treatment-date choice or the control-jurisdiction choice that breaks the result
- Reporting only that significance survives while the point estimate wanders
- Treating "added more controls and it survived" as sufficient for selection on unobservables

## Worked vignette (illustrative)

A DiD estimate that an entry-licensing law raised consumer prices is 6% (s.e. 2). The robustness suite: (i) re-dating from the statute's signing to its effective date shifts the estimate trivially (6.1%); (ii) dropping the three states with simultaneous occupational-licensing reforms leaves it at 5.7%; (iii) a leave-one-state-out sweep stays within [5.2%, 6.4%]; (iv) Oster δ implies selection on unobservables would need to be 2.1× selection on observables to nullify it; (v) with 11 treated states a wild-cluster bootstrap keeps the 95% interval away from zero, whereas naive clustering over-rejects; (vi) a placebo on an unlicensed adjacent service is null. The point estimate barely moves — the JLE target.

## The few-clusters problem is the JLE default, not the exception

Most JLE empirical designs exploit variation across a small number of legal units — 50 states, a dozen circuits, a handful of countries, one agency's enforcement regions. With few clusters, conventional clustered standard errors **over-reject**, so a result that looks significant may not survive correct inference. Treat this as the baseline expectation, not a corner case:

- Report a **wild-cluster bootstrap** (Cameron–Gelbach–Miller) or **randomization/permutation inference** as the primary inference when clusters are few, with naive clustered SEs shown only for comparison.
- For a single treated unit or a few, consider **synthetic control** with placebo-based inference instead of DiD.
- Do not "solve" few clusters by clustering at a finer level (case, firm) that the legal variation does not justify — that manufactures precision the design cannot support.

## Referee pushback mapped to the robustness fix

- *"You only have 11 states — your standard errors are too small."* → Cluster at the state level and report a wild-cluster bootstrap or randomization-inference p-value.
- *"Your result depends on when you say the law took effect."* → Show estimates under signing, effective, and enforcement dates with a donut around each.
- *"Could the control states' own reforms drive this?"* → Drop contaminated controls, run leave-one-out, and add a placebo on an unaffected legal area.
- *"One treated state can't give you valid inference."* → Switch to synthetic control with placebo (in-space) inference rather than asymptotic clustering.

## Output format

```
【Primary spec】declared? [Y/N] — estimate: ___ (s.e. ___)
【Threat → check map】confounders: ___ | date: ___ | controls: ___ | form: ___ | sample: ___ | inference: ___ | design: ___
【Inference】clustering level: ___; few-cluster method: ___
【Design sensitivity】honest-DID / RD bandwidth / weak-IV set: ___
【Estimate stability】range across checks: [___, ___]; checks that move it: ___
【Next step】jle-tables-figures
```
