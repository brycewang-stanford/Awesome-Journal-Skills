---
name: finman-robustness
description: Use when deciding which robustness checks a Financial Management (FM) paper actually needs — FM explicitly puts "less weight on trivial robustness tests," so the craft is selecting threat-targeted checks and demoting busywork. Curates the robustness layer; it does not establish identification (finman-identification) or format exhibits (finman-tables-figures).
---

# Robustness Strategy (finman-robustness)

## When to trigger

- The paper has a wall of robustness tables and you cannot say which threat each one answers
- A coauthor wants to add "a few more specifications to be safe" before submission
- A referee asked whether the result survives an *alternative explanation*, not just an alternative specification
- You are unsure which checks belong in the main text vs. the internet appendix

## The FM robustness philosophy (this is the distinctive part)

Most journals reward more robustness tables; **FM explicitly does not.** The editors state they put **less weight on trivial robustness tests** and more on **new ideas** and **whether the result is interesting and credible.** This inverts the usual instinct: at FM, a robustness section that mechanically re-runs the regression with five winsorization thresholds and three control sets signals *weak ideas hiding behind volume*. The skill here is **subtraction, then precision** — cut the busywork, then run the small number of checks that each defuse a *named alternative explanation* a smart referee would actually raise. One check that kills the leading confounder is worth more than ten that vary nothing important.

## Threat-targeted robustness, not specification spraying

Build the robustness set by listing the alternative explanations a referee could offer, then pairing each with the *one* check that addresses it. Everything not on that list is a candidate for the appendix or the cut.

| Alternative explanation a referee raises | The targeted check (not a generic one) |
|------------------------------------------|----------------------------------------|
| "It's an omitted firm characteristic" | Oster-style coefficient-stability / sensitivity to selection on unobservables |
| "It's reverse causality" | lead-lag / pre-trend / a design that fixes timing |
| "It's driven by one industry or period" | drop-the-suspect-subsample; show stability, not 12 random subsamples |
| "It's a measurement artifact of variable X" | re-do with the one credible alternative measure of X |
| "It's a mechanical accounting identity" | re-specify to break the identity; show the result is not tautological |
| "The inference is overstated" | the *right* SE (two-way / wild-cluster), not five SE flavors |
| "It won't survive transaction costs" (asset pricing) | net-of-cost returns, realistic implementation |

## Curation sequence

1. **List the alternative explanations** explicitly — these are the only legitimate drivers of robustness work.
2. **Map one check per threat.** If two checks address the same threat, keep the stronger one.
3. **Demote or delete the rest.** Winsorization sweeps, control-set permutations that change nothing, and SE-flavor tables go to the internet appendix or out.
4. **Lead with the most threatening alternative.** The first robustness exhibit should answer the objection most likely to sink the paper.
5. **Report stability, not a starred wall.** Show the point estimate barely moves across the threat-targeted checks; that is the persuasive object, not significance stars.

## What "less weight on trivial robustness" does NOT mean

Under-weighting trivial robustness is not a license to skip the checks that matter. FM still expects:

- **Correct inference** — the right clustering / standard errors are non-negotiable, not optional robustness.
- **A defused leading alternative** — the single most plausible confound must be addressed; this is identification, not busywork.
- **Honest sensitivity** — an Oster-style bound or a pre-trend plot is *cheap and decisive*, the opposite of trivial.
The distinction FM draws is between checks that **change what a reader believes** (keep, lead with) and checks that **only signal diligence** (winsorization sweeps, SE menus, control churn — cut or appendix). When in doubt, ask: "If this check came out differently, would my conclusion change?" If no, it is trivial.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Financial Management is empirical corporate finance + asset pricing; corporate-causal chain (DiD/IV/RDD) plus the factor-zoo haircut for cross-sectional pricing.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or `benjamini_hochberg`.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists missing checks + the exact
  `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Decisive checks in the body, exhaustive battery in the appendix.
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Each robustness check is tied to a named alternative explanation, not a generic permutation
- [ ] No redundant checks that vary something immaterial (winsorization sweeps, control churn)
- [ ] The leading alternative explanation is addressed first and convincingly
- [ ] Inference robustness is the *correct* SE, not a menu of SE flavors
- [ ] Asset-pricing results shown net of realistic transaction costs where relevant
- [ ] Main text carries only threat-defusing checks; the rest is in the internet appendix
- [ ] Every retained check would change the conclusion if it came out differently
- [ ] Stability of the point estimate is the headline, not a wall of asterisks

## Anti-patterns

- A 15-row robustness table where no row corresponds to a real alternative explanation
- Adding checks "to be safe" — at FM this reads as padding, not rigor
- Five winsorization thresholds and three control sets presented as serious robustness
- Reporting four standard-error flavors instead of justifying the one correct clustering
- Letting robustness volume substitute for a missing identification argument
- Burying the one check that actually matters among nine that do not

## Worked vignette (illustrative)

A draft has eleven robustness tables; a referee says "this is thorough but I still don't know if it's real." The FM fix: list the three live alternatives — omitted governance quality, reverse causality, and a single-industry driver — and replace eleven tables with three: an Oster sensitivity bound, a lead-lag timing test, and a drop-financials subsample. Each defuses one named threat; the coefficient moves from 3.2 to 3.0 to 3.1 across them (illustrative), so stability is the story. The other eight tables move to the internet appendix. The paper now reads as confident, not defensive — exactly FM's taste.

## Subfield-specific robustness that is never trivial

Some checks look like robustness but are actually identification, and FM expects them even under its lean philosophy:

- **Corporate finance:** event-window sensitivity around a shock; placebo timing; a Goodman-Bacon decomposition for staggered designs.
- **Asset pricing:** out-of-sample / sub-period stability, factor-model choice, and net-of-cost returns — a "significant" gross alpha that vanishes after costs is not robust, it is refuted.
- **Banking / microstructure:** alternative measures of the latent construct (liquidity, information asymmetry) where the proxy is contestable.
- **Governance / payout:** sensitivity to the omitted-quality story (Oster bounds), since selection on unobservables is the standing objection.
These are threat-targeted by construction; they belong in the keep column, not the cut column.

## Output format

```
【Alternative explanations】[named list a referee would raise]
【Threat → check map】[one targeted check per threat]
【Demoted / cut】[trivial checks moved to appendix or removed]
【Leading threat addressed first】[Y/N]
【Inference】correct SE chosen (not a flavor menu)? [Y/N]
【Headline】point-estimate stability shown, not a starred wall? [Y/N]
【Next skill】finman-tables-figures
```
