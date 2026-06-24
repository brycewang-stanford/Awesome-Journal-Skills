---
name: jmcb-robustness
description: Use when a Journal of Money, Credit and Banking (JMCB) result may be specification-, sample-, or inference-sensitive and you need to plan checks that each kill a specific threat. Builds a threat-mapped robustness suite; it does not re-run the core identification or write the prose.
---

# Robustness Strategy (jmcb-robustness)

## When to trigger

- The headline (an IRF, an elasticity, a counterfactual welfare number) might flip under nearby choices
- A referee will ask "is this the recursion ordering / lag length / sample window talking?"
- Standard errors look too tight for a bank×time panel or for serially correlated macro data
- The result depends on one regime (a crisis, the ZLB) and you have not shown sub-sample stability
- You have a pile of "robustness" tables but cannot say which threat each one rules out

## The JMCB robustness logic

JMCB referees do not reward a wall of additional regressions; they reward checks that are **mapped to a named threat to the specific identification**. A robustness suite is a list of "the result could be wrong because X — here is the check that rules out X." Given the journal's monetary/banking focus, the recurring threats are: shock contamination, specification dependence (lags, ordering, controls), inference understatement on panels and serially correlated series, and regime/sample instability around crises and policy transitions.

## Threat → check map (build yours from this)

| Named threat | Diagnostic / check |
|---|---|
| Shock is contaminated (information effect, anticipation) | Re-identify with info-robust surprises; orthogonalize to forecast revisions; placebo on pre-announcement windows |
| SVAR result is ordering-/restriction-driven | Vary recursive ordering; alternative sign-restriction sets; report the full identified set |
| IRF is lag-length / horizon dependent | Vary VAR lags; local-projection vs. VAR; alternative horizons |
| Panel SEs understated | Two-way (bank and time) clustering; wild-cluster bootstrap with few clusters; Driscoll–Kraay for cross-sectional dependence |
| Result is one-regime (crisis/ZLB) artifact | Split pre/post-2008, exclude crisis, exclude ZLB; state-dependent specification |
| Demand contamination (micro-banking) | Tighter fixed effects (firm×time); single-bank-firm vs. multi-bank-firm subsample |
| Controls are doing the work | Sequentially add controls (Oster-style movement check); show coefficient stability |
| Outliers / measurement | Alternative winsorizing; drop largest institutions; alternative variable definitions |

## How to present it

1. **Lead with the threats a JMCB referee will actually raise**, ordered by how damaging they would be if true.
2. For each, show the headline magnitude **next to** the baseline so the reader sees stability (or honest movement), not just significance survival.
3. Put the **3–4 load-bearing checks in the main text**; relegate the long tail to the online appendix with a pointer (see `jmcb-internet-appendix`).
4. Where a check *does* move the result, say so and interpret it — a transparent boundary is more credible than a uniform table of survivors.

## Inference deserves its own pass

For JMCB's two dominant data shapes, the default standard errors are usually wrong in a predictable direction:

- **Bank/firm panels:** a single dimension of clustering understates uncertainty when shocks are common across units within a period. Cluster on **both** the cross-sectional unit (bank/firm) and time; with few clusters in either dimension, use the **wild-cluster bootstrap** (Cameron–Gelbach–Miller). If cross-sectional dependence is plausible, report **Driscoll–Kraay** as a complement.
- **Macro time series / local projections:** serially correlated errors require **HAR/Newey–West** or lag-augmentation; for VARs, report bootstrap or bias-corrected bands rather than asymptotic ones at short samples.

State the clustering/inference choice once, prominently, and show the headline survives a reasonable alternative — referees treat a casual one-way-clustered SE as a red flag.

## Crisis and regime stability is not optional for long samples

Many JMCB samples straddle the 2008 crisis, the ZLB/QE era, and post-Basel-III regulation. A result that holds only because one of these episodes dominates the variation is fragile. Show the headline in **pre/post sub-samples**, **excluding the crisis window**, and — where the mechanism plausibly changes at the bound — in a **state-dependent** specification (e.g., interacting the shock with a ZLB or high-uncertainty indicator). If the effect genuinely is regime-specific, that is itself a finding; report it as one rather than letting it masquerade as a general result.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JMCB is monetary/banking — macro time series + bank panels; local projections for the macro lane, DiD/IV for the bank lane.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or `benjamini_hochberg`.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists missing checks + the exact
  `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Decisive checks in the body, exhaustive battery in the appendix.
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Each robustness check is tied to a named threat to *this* identification
- [ ] Inference re-examined: clustering dimensions correct; few-cluster and serial-correlation handled
- [ ] Specification dependence shown (ordering/lags/horizon/controls) with magnitudes side by side
- [ ] Sub-sample / regime stability shown (crisis, ZLB, policy transition) if the period spans one
- [ ] Micro-banking: demand-contamination check via tighter fixed effects or single-vs-multi-bank firms
- [ ] Load-bearing checks in main text; long tail in the online appendix with a map
- [ ] Any check that moves the result is reported and interpreted, not hidden

## Anti-patterns

- A robustness section that adds controls and reports "still significant" without showing the magnitude
- Twenty appendix tables with no statement of which threat each addresses
- Reporting only the checks that survive and quietly dropping the ones that did not
- Leaving panel SEs one-way clustered when shocks are common across banks in a period
- Claiming generality from a single regime without a crisis/ZLB sub-sample
- Treating statistical-significance survival as the bar when the question is magnitude stability

## Don't over-test: a focused suite beats an exhaustive one

A robustness section that runs every permutation signals uncertainty, not rigor. Pick the checks that map to the objections a JMCB referee will actually raise (shock cleanliness, demand contamination, inference, regime stability) and present those in the body with magnitudes side by side. Everything else — alternative winsorization thresholds, dozens of control permutations — goes to the online appendix with a one-line summary in text. The goal is to show the headline is stable where it matters, not to bury the reader.

## Worked vignette (illustrative)

An SVAR finds a contractionary monetary shock raises credit spreads. A referee suspects the recursive ordering. The threat-mapped response: re-estimate under three alternative orderings and a sign-restricted scheme, plot the IRFs together, and show the peak spread response stays in a 15–22bp band across all of them (illustrative). One check — using revised instead of real-time data — does shift the peak; the authors report it and argue the real-time version is the policy-relevant one. That honesty reads as strength at JMCB.

## Output format

```text
【Journal】Journal of Money, Credit and Banking
【Skill】jmcb-robustness
【Top threats】ranked list of what could make the headline wrong
【Threat → check】each check mapped to the threat it rules out
【Inference fix】clustering dims / few-cluster / serial-correlation handling
【Regime stability】crisis / ZLB / transition sub-samples
【Main vs appendix】load-bearing checks in text; tail mapped to online appendix
【Honest movement】any check that shifts the result + interpretation
【Next skill】jmcb-tables-figures
```
