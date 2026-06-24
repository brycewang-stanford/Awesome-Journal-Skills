---
name: jleo-robustness
description: Use when organizing robustness and sensitivity checks for a Journal of Law, Economics, and Organization (JLEO) manuscript — structuring checks by the institutional/organizational threat each one defuses (selection into governance, reform endogeneity, measurement of institutional constructs, alternative mechanisms). Organizes the robustness program; it does not establish primary identification (jleo-identification).
---

# Robustness Strategy (jleo-robustness)

## When to trigger

- The main result holds but a referee will ask "is this an artifact of the sample / specification / measurement?"
- The robustness section is a mechanical appendix list ("Table A1–A8") with no threat each addresses
- The institutional measure (asset specificity, governance form, judicial independence) is a proxy whose validity is questionable
- An alternative mechanism could produce the same pattern and is not yet ruled out
- The estimate is sensitive to clustering, controls, or the treatment-timing window

## Robustness as threat-defusal at JLEO

JLEO referees — institutional and organizational economists — do not reward a wall of robustness tables. They reward a robustness program **organized by the specific threats to the institutional claim**. For each headline result, name the threats, then show the check that defuses each. The institution-specific threats cluster as follows:

| Threat to the institutional claim | The check that defuses it |
|-----------------------------------|---------------------------|
| Selection into the governance form / institution | IV / selection model / matching robustness; bound the selection (Oster δ) |
| Endogenous reform timing or anticipation | event-study leads; placebo timing; controls for pre-trends; alternative timing windows |
| The institutional construct is mismeasured | alternative proxies for the construct; measurement-error bounds; cross-validate the measure |
| An alternative mechanism explains the pattern | a test that separates your mechanism from the rival (heterogeneity prediction, falsification) |
| Inference is fragile (few clusters, serial correlation) | wild-cluster bootstrap; alternative clustering levels; randomization inference |
| Functional form / spec mining | a small, principled spec curve; pre-specified controls; not 40 arbitrary specs |

## Sequencing the program

1. **List threats before checks.** For each main result write the two or three threats that, if true, would overturn the institutional interpretation. Robustness exists to kill those, not to fill pages.
2. **Construct validity first.** Because JLEO results hinge on measuring institutional constructs (specificity, governance form, judicial independence, committee power), validate the measure early — alternative operationalizations should not move the conclusion.
3. **Mechanism vs. rival.** The most persuasive JLEO robustness is a test that *only your mechanism* predicts (e.g., the effect is concentrated where transaction-cost theory says it should be, absent where it should not). This doubles as evidence, not just defense.
4. **Inference robustness.** Institutional treatments often have few clusters (states, courts, reforms). Use wild-cluster bootstrap or randomization inference and report it.
5. **Bound the unobservable.** Where selection cannot be fully ruled out, use Oster-style bounds or sensitivity analysis to show how strong unobserved selection would have to be to overturn the result.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JLEO is law-and-economics/organizations; institutional designs with endogeneity — foreground identification.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or `benjamini_hochberg`.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists missing checks + the exact
  `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Decisive checks in the body, exhaustive battery in the appendix.
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Each headline result has a named list of two or three threats to its institutional interpretation
- [ ] Every robustness exhibit maps to one named threat (not a generic "additional specifications" dump)
- [ ] The institutional construct is validated with at least one alternative measure
- [ ] A test that separates the proposed mechanism from the leading rival is included
- [ ] Inference robustness shown for few-cluster / serial-correlation concerns
- [ ] Selection sensitivity (Oster δ or equivalent) reported where selection is the live threat

## Anti-patterns

- A robustness appendix organized by table number rather than by threat
- Reporting twenty specifications without saying which threat each one rules out (reads as fishing)
- Ignoring measurement of the institutional construct while piling controls on the regression
- Leaving the leading alternative mechanism un-tested because the main result is "significant"
- Default one-way clustering with a handful of institutional clusters and no bootstrap

## Worked vignette (illustrative)

A paper claims judicial independence reduces expropriation of firms. Threats: (1) independence is endogenous to economic conditions; (2) the independence index is noisy; (3) general rule-of-law improvement, not independence specifically, drives the result. The threat-organized program: an event study around a constitutional reform isolating timing (threat 1); two alternative independence indices that agree (threat 2); and a placebo on a rule-of-law dimension that the mechanism says should not matter for *this* outcome (threat 3). Each table is captioned by the threat it kills, not by its position in the appendix.

## Output format

```text
【Headline result】[...]
【Threats to the institutional interpretation】1) ___ 2) ___ 3) ___
【Check per threat】threat 1 → ___ ; threat 2 → ___ ; threat 3 → ___
【Construct validity】alternative measure(s): ___
【Mechanism vs. rival test】[...]
【Inference robustness】wild-cluster / randomization / alt-clustering: ___
【Selection bound】Oster δ or sensitivity: ___
【Next skill】jleo-tables-figures
```
