---
name: expecon-robustness
description: Use when an Experimental Economics (ExpEcon) result may be a power artifact, multiple-comparisons artifact, or sensitive to the inference unit, exclusions, or design choices. Hardens the statistical case; it does not design the experiment or draft prose.
---

# Robustness & Inference (expecon-robustness)

## When to trigger

- A referee asks "is the study adequately powered?" and there is no sample-size justification
- You ran several treatments / outcomes and report many p-values without correction
- Inference treats individual decisions as independent when subjects interact in groups
- Results move when you change the exclusion rule, the outcome measure, or pool/unpool sessions

## The ExpEcon inference stack

Experimental control buys clean identification; it does not buy clean *inference*. Five things separate a robust ExpEcon paper from a fragile one.

### 1. Power / sample-size justification (do this before data, defend it after)

- Pre-specify the **minimum detectable effect (MDE)** that is economically meaningful and the power to detect it, at the **correct unit** (session or matching group, not individual decision). A study powered on individual n but analyzed at the group level is overstated.
- Use pilot or prior-literature variances; for interactive games, simulate at the group level. Report the realized power for the primary comparison, not just a post-hoc "we found p<0.05."
- A clean, well-powered **null** is publishable here — especially as a Registered Report. Do not p-hack a null into significance; defend it with power.

### 2. The unit-of-observation problem

- Within a matching group, decisions are correlated; the **independent unit is the group/session**, often giving far fewer effective observations than the raw decision count suggests.
- Use group-level summaries, **cluster-robust SEs at the session/matching-group level**, mixed models with group random effects, or non-parametric tests on group means (Mann–Whitney / permutation). With few clusters, prefer randomization-inference / permutation tests over asymptotic clustering.

### 3. Multiple treatments & multiple hypotheses

- If you test several outcomes or several pairwise treatment contrasts, **correct for multiplicity** (Holm, Romano–Wolf, List–Shaikh–Xu for experiments, or pre-registered families). Distinguish the **primary** pre-registered comparison (no correction needed if it is the single confirmatory test) from **secondary/exploratory** ones (correct, and label exploratory).
- Report the pre-registered analysis first, exactly as specified; report deviations and additional analyses separately and labeled.

### 4. Non-parametric vs. parametric

- Experimental outcomes are often bounded, censored (contributions in [0,20]), or non-normal. Lead with **non-parametric tests** on the primary comparison; use regression for covariate adjustment and heterogeneity, not to rescue a fragile mean difference.

### 5. Robustness to design and analysis choices

- Show the effect survives: alternative exclusion rules (comprehension failers in/out), first-half vs. second-half rounds (learning), partner vs. stranger if both run, and a permutation test of the treatment label.
- Report **attrition** and, in field/online studies, differential attrition (Lee bounds if it threatens balance).

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Experimental Economics is lab/field experiments; randomization inference, `romano_wolf` for many treatments/outcomes, and power are decisive — observational tools secondary.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or `benjamini_hochberg`.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists missing checks + the exact
  `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Decisive checks in the body, exhaustive battery in the appendix.
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Sample size justified via MDE + power **at the group/session unit**; realized power reported
- [ ] Inference uses the correct independent unit (cluster-robust / group-means / RI), not raw decision n
- [ ] Few-cluster inference handled (permutation / randomization inference) when sessions are few
- [ ] Multiplicity corrected across outcomes/contrasts; primary vs. exploratory clearly separated
- [ ] Primary analysis matches the pre-analysis plan exactly; deviations flagged
- [ ] Non-parametric test leads for the bounded/non-normal primary outcome
- [ ] Robustness to exclusions, learning (round halves), and order shown; attrition reported

## Anti-patterns

- "We found a significant effect" with no power analysis and a tiny number of independent groups
- Per-decision n inflating significance when subjects are in repeated, interacting groups
- A cherry-picked significant contrast among many, uncorrected and unlabeled as exploratory
- Switching the primary outcome or exclusion rule after seeing results, without disclosure
- Parametric t-tests on heavily censored contribution data as the only evidence
- Declaring a null "no effect" when the design never had power to detect a meaningful effect

## Worked vignette (illustrative)

A public-goods paper runs 4 treatments × 3 outcomes and reports 7 significant tests. The fix: declare the single pre-registered primary contrast (cooperation under punishment vs. no-punishment) tested at the matching-group level via a permutation test on group means (say 12 groups/arm), then apply Romano–Wolf across the remaining family and label the rest exploratory. The headline survives correction (illustrative p=0.004); two secondary "effects" do not and are reported honestly as exploratory.

## Referee pushback mapped to the fix

- *"How many independent observations do you actually have?"* → Count **groups/sessions**, not decisions; report inference at that unit and the realized power for it.
- *"You ran a fishing expedition."* → Declare the single pre-registered primary test; correct the rest (Romano–Wolf/Holm) and label them exploratory.
- *"Few clusters — your SEs are unreliable."* → Use randomization inference / permutation tests on group means rather than asymptotic clustering.
- *"The null is uninformative."* → Report the MDE; show the design had power to detect a meaningful effect, so the null is evidence of absence, not absence of evidence.
- *"Results depend on dropping subjects."* → Show the effect with and without comprehension failers and state the pre-specified rule.

## A minimal robustness panel to pre-build

1. Primary test at the group/session unit (non-parametric lead).
2. Same test with comprehension failers included vs. excluded.
3. First-half vs. second-half rounds (learning).
4. Permutation/randomization-inference p-value on the treatment label.
5. Multiplicity-corrected family of secondary contrasts, labeled exploratory.
6. Attrition table (and differential attrition / Lee bounds in field-online designs).

If all six point the same way, the result is robust in the sense ExpEcon referees mean; if (3) or (4) flips it, the headline is fragile and you learned that before a referee did.

## Output format

```text
【Journal】Experimental Economics (ESA method flagship)
【Skill】expecon-robustness
【Verdict】robust / fragile / underpowered
【Power】MDE + power at group/session unit; realized power
【Inference unit】group-means / cluster-robust / randomization inference
【Multiplicity】correction used; primary vs. exploratory split
【Design robustness】exclusions / learning halves / order / attrition
【Next skill】expecon-tables-figures
```
