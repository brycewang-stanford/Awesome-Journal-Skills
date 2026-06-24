---
name: imfer-robustness
description: Use when an IMF Economic Review (IMFER) manuscript's headline cross-country estimate must be shown to survive specification, sample, country-composition, and inference choices before submission or in an R&R. Builds the robustness suite a dual academic/policy referee expects; it does not establish identification (imfer-identification) or format exhibits (imfer-tables-figures).
---

# Robustness Suite (imfer-robustness)

## When to trigger

- The main estimate is in hand and you must show it is not an artifact of one specification
- A referee asks "is this driven by a few countries / a particular crisis episode / the sample window?"
- The result depends on a sample-selection rule, a country grouping, or a deflator/exchange-rate convention
- You suspect a global common shock or one influential economy is doing the work
- You want to pre-empt specification-search and country-cherry-picking concerns

## The IMFER robustness bar

IMFER referees probe whether the headline number is **stable, honestly inferred, and not the product of country-composition or specification search** — and, distinctively, whether it would still *guide policy* under reasonable alternatives. Robustness here is a targeted set of checks, each tied to a specific threat to an *international-macro* design, not a wall of regressions. The persuasive object is that the **point estimate barely moves** when you drop the obvious country, switch the window, or change the inference.

| Threat to the result | The check that answers it |
|----------------------|---------------------------|
| One country / region drives it | leave-one-country-out; drop the dominant economy or region; jackknife |
| A single crisis episode drives it | drop the GFC / euro-crisis / COVID window; alternative event definitions |
| Global common shock confounds it | add the global financial cycle factor / US-shock control; time effects |
| Sample / coverage selection | balanced vs. unbalanced panel; alternative country-inclusion rules; advanced-vs-EM split |
| Specification search | specification curve; pre-registered or primary spec; stepwise controls |
| Measurement convention | alternative deflators, USD vs. local currency, gross vs. net flows |
| Inference too narrow | Driscoll–Kraay (cross-sectional dependence); country clustering; wild-cluster bootstrap (few countries) |
| Omitted confounders | Oster δ / coefficient-stability bounds |

### Inference under cross-country dependence (the common slip)
Standard errors are where IMFER robustness most often fails, because country panels violate the assumptions behind default clustering. Flows, spreads, and prices are **cross-sectionally dependent** (a global shock hits everyone), so country-clustered SEs alone understate uncertainty — use Driscoll–Kraay or a two-way (country and time) cluster. The country dimension is usually **small** (30–60 economies), so cluster-robust asymptotics are unreliable — report a wild-cluster bootstrap. Serial correlation within country is the norm — do not assume i.i.d. errors. State which of these you address and why; a referee who suspects the SEs are too tight will discount the whole result.

## Robustness craft

1. **Lock the primary specification first.** Everything else perturbs it; do not present five co-equal panels and let the referee guess the preferred one.
2. **Lead with the country-composition checks.** Leave-one-country-out and drop-the-dominant-economy are the *first* things an IMFER referee runs in their head — show them in the main paper.
3. **Stress the global common shock.** Demonstrate the effect is not the global financial cycle masquerading as your policy variable.
4. **Match inference to cross-country structure.** Driscoll–Kraay or two-way clustering, and wild-cluster bootstrap when the country count is small — wrong SEs are the most common IMFER robustness failure.
5. **Report stability, not just significance.** Show the *point estimate* range across checks; a check that moves it is information — bound the implication for policy rather than hiding it.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). IMFER is international macro/finance; cross-country panels with confounded policy — emphasize identification and clustering.

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
- [ ] Leave-one-country-out / drop-dominant-economy shown (composition not driving the result)
- [ ] Crisis-episode sensitivity (drop GFC / euro / COVID) reported
- [ ] Global common shock / global financial cycle controlled
- [ ] Sample-selection alternatives (balanced/unbalanced; AE/EM split; coverage rules) tested
- [ ] Measurement conventions (currency, deflator, gross/net) varied
- [ ] Inference correct for cross-sectional dependence and few-country count; SEs not asterisks
- [ ] Point-estimate range across checks reported; any check that moves it explained

## Anti-patterns

- A 20-column robustness table with no map from check to threat ("kitchen-sink robustness")
- Never running leave-one-country-out when one economy obviously dominates the panel
- Ignoring the global financial cycle / US-shock common factor
- Reporting only that significance survives while the point estimate wanders
- Country clustering with very few countries and no wild-cluster bootstrap
- Hiding the window or sample rule that breaks the result

## Worked vignette (illustrative)

A panel estimate of the spillover from US tightening to EM inflows is −0.8% of GDP (s.e. 0.2). The suite: (i) leave-one-country-out keeps it in [−0.9, −0.7] with no single economy decisive; (ii) dropping the GFC window leaves it at −0.7; (iii) adding the global financial cycle factor barely shifts it; (iv) the AE/EM split shows the effect concentrated in EMs as the mechanism predicts; (v) Driscoll–Kraay SEs (cross-country dependence) keep the CI away from zero; (vi) gross vs. net flows give the same sign and magnitude. The point estimate barely moves — the IMFER target — and the one check that softens it (excluding commodity exporters) is reported with its policy reading.

## Referee pushback mapped to the robustness fix

- *"This is driven by a few countries."* → Show leave-one-country-out and drop-the-dominant-economy in the main paper; report the estimate range.
- *"This is the GFC / euro crisis, not your variable."* → Drop the crisis window and add the global-cycle control; show the result holds.
- *"Did you cluster correctly?"* → Use Driscoll–Kraay for cross-country dependence; with few countries report a wild-cluster bootstrap.
- *"Different currency / flow convention would change this."* → Re-run in USD and local currency, gross and net; show the same sign and magnitude.

## The composition check IMFER referees run first

Because IMFER panels are small in the country dimension and dominated by a few large economies, the single most predictable referee move is "drop the obvious country and show me it survives." Build this into the paper, not the appendix: report a leave-one-country-out distribution (or a coefficient plot with each country excluded), and if one economy is decisive, say so and bound the implication. A panel where China, the US, or one euro-area crisis country silently drives the headline is the most common IMFER robustness failure — and the easiest to pre-empt.

## Output format

```text
【Journal】IMF Economic Review
【Skill】imfer-robustness
【Primary spec】declared? [Y/N] — estimate: ___ (s.e. ___)
【Composition】leave-one-country-out / drop-dominant range: [___, ___]
【Episode / window】drop-crisis result: ___
【Common shock】global-financial-cycle control result: ___
【Sample / measurement】AE-EM split, currency, gross/net: ___
【Inference】Driscoll–Kraay / wild-cluster (few countries): ___
【Estimate stability】range across checks: [___, ___]; checks that move it: ___
【Next skill】imfer-tables-figures
```
