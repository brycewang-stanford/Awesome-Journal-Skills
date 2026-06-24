---
name: jfe-robustness
description: Use when a Journal of Financial Economics (JFE) result needs the exhaustive robustness battery the journal is known for — alternative measures, subsamples, specifications, and falsification. Builds the stress-test plan; it does not choose the core estimator (jfe-empirical-design) or the identification design (jfe-identification).
---

# Robustness Battery (jfe-robustness)

## When to trigger

- The result holds in the baseline but you have not tried obvious alternatives
- A referee could ask "does this survive a different measure / sample / specification?"
- You are unsure which robustness tests belong in the main text vs. the Internet Appendix
- You suspect a result might be fragile and want to find out before a referee does

## Why robustness is JFE's signature

JFE's referee culture rewards thoroughness: a result is credible only after it survives a wide battery of sensible alternatives, and reviewers expect *every* alternative explanation to be addressed, not merely the convenient ones. A fragile result that breaks under a routine variation is a classic JFE rejection. The headline tests live in the main text; the rest go to the Internet Appendix, which JFE asks you to append to the end of the main manuscript file (see `jfe-internet-appendix`).

Because JFE mandates a **code + non-proprietary-data deposit** (Mendeley Data) at acceptance for post-2021 submissions, your robustness battery must be *runnable*, not just described — referees increasingly probe reproducibility after the field-wide concerns about non-replicable factors (the Fama-French factor lineage is the benchmark) and fragile staggered-DID results.

## The robustness dimensions

Work through each; for each, decide main-text vs. appendix.

### 1. Alternative measures
- Re-measure the dependent and key independent variables (different proxies, data sources, definitions).
- Show the result is not an artifact of one operationalization.

### 2. Alternative specifications
- Add/remove fixed effects; vary the control set; show coefficient stability (a coefficient-stability / Oster bounds argument for omitted-variable bias where relevant).
- Functional form: levels vs. logs, linear vs. nonparametric.

### 3. Alternative samples
- Drop influential years (e.g., the financial crisis), industries, or large firms.
- Subperiod stability; exclude the most/least-treated units.

### 4. Alternative inference
- Re-cluster at a different level; wild-cluster bootstrap when clusters are few.
- Permutation/randomization inference where appropriate.

### 5. Falsification & placebos
- Outcomes that should *not* respond if your story is right.
- Placebo timing or placebo treatment groups.

### 6. Ruling out alternative explanations
- For each rival story a referee could tell, design a test that distinguishes it from yours.
- This is the single most important block for JFE — list the alternatives explicitly and kill them one by one.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JFE is finance top-3 (with JF, RFS) — corporate-causal chain for corporate papers, factor-zoo haircut for asset pricing; attribute canon to the correct top-3 journal.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or `benjamini_hochberg`.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists missing checks + the exact
  `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Decisive checks in the body, exhaustive battery in the appendix.
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Key variables re-measured with at least one alternative proxy
- [ ] Specification varied (FE set, controls, functional form) with stable coefficients
- [ ] Subsample / subperiod stability shown; crisis or outlier periods isolated
- [ ] Inference re-done at an alternative cluster level (or wild bootstrap)
- [ ] Falsification / placebo tests run and reported
- [ ] Each named alternative explanation has a distinguishing test
- [ ] Main-text vs. Internet-Appendix split decided for every test

## Anti-patterns

- Reporting only the robustness checks that pass ("cherry-picked specifications")
- A "robustness" section that re-runs the same model with one extra control and calls it done
- Leaving an obvious rival explanation untested and hoping no referee notices
- A result that flips sign or loses significance under a routine variation, reported without comment
- Dumping every check into the main text so the paper becomes unreadable

## Output format

```
【Headline result】...
【Robustness done】measures[...] specs[...] samples[...] inference[...] placebos[...]
【Alternatives ruled out】[story -> test] pairs
【Fragile under】[...] (if any — fix before submission)
【Main-text vs. appendix】split decided: yes/no
【Next】jfe-tables-figures
```
