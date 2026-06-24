---
name: restud-robustness
description: Use when the main results of a The Review of Economic Studies (REStud) manuscript exist but referee-anticipating checks — robustness, heterogeneity, mechanism, placebo, alternative specifications — are missing or fragile. Hardens the result against demanding referees; does not redesign identification.
---

# REStud Robustness (restud-robustness)

## When to trigger

- The main result rests on a single specification
- No placebo / falsification evidence exists
- A referee will say "the effect is driven by X" and you have no pre-empting check
- The result is statistically marginal and sensitivity is undocumented
- Heterogeneity or mechanism evidence is absent and the channel is asserted, not shown

## The REStud standard

REStud referees are demanding and the journal is known for *developing strong papers across rounds*. A robust REStud result is one that **does not hinge on one fragile specification**. The goal of this stage is to find the weak point before a referee does, and either fix it or report it honestly. Robustness is not a wall of extra tables — it is targeted evidence against the most plausible alternative explanations. Two REStud-specific facts shape how you stage it: (1) bulk robustness belongs in the **online appendix / supplementary file**, with only the decisive checks in the main text; (2) for an *accepted* empirical paper, every robustness number must be reproducible, because the **Data Editor (Miklós Koren) reruns your code before publication** under the AEA DCAS standard (see `restud-replication-package`) — a check you cannot regenerate from the deposit is a liability, not a defense.

## Priority of checks

Run, in roughly this order of referee salience:

1. **Specification robustness.** Vary fixed effects, controls, functional form, and sample windows. The headline magnitude should be *stable*, not just same-signed. Report a coefficient-stability / sensitivity table or a `specchart`-style plot.
2. **Placebo / falsification.** A test where the effect should be absent (placebo outcome, placebo timing, placebo population). A clean placebo is worth more than ten near-identical specifications.
3. **Inference robustness.** Re-cluster at alternative levels; wild-cluster bootstrap if clusters are few; randomization inference for designs that admit it.
4. **Mechanism.** Show evidence consistent with the proposed channel — auxiliary outcomes, subgroup patterns the theory predicts. Mechanism evidence must not weaken the identification of the main effect.
5. **Heterogeneity.** Effects where theory predicts them to be larger/smaller. Pre-specify the cuts; do not data-mine subgroups and report the significant one.
6. **Selection / attrition / measurement.** For panels and experiments: differential attrition, measurement-error bounds, sample-selection corrections where relevant.

## Calibrating effort

- A **new empirical fact** paper lives or dies on robustness — over-invest in (1) and (2).
- A **new design** paper must show the design's diagnostics are not knife-edge — over-invest in (3) and design-specific placebos.
- A **theory-with-empirics** paper needs (4) tightest — the empirics must confirm the model's specific predictions, not just a correlation.

## Reporting discipline

- Put the **decisive** robustness evidence in the main text, not the appendix. A referee reading only the body should see the result survive its hardest test.
- Move the bulk of additional specifications and falsification exercises to the **online appendix**, cross-referenced from the body.
- Report robustness as a *coefficient-stability table or specification plot*, so the reader sees the distribution of estimates at a glance rather than reading ten columns.
- If a reasonable specification weakens the result, **say so and explain why** (power, a known confounder, a sample boundary) rather than hiding it — a demanding REStud referee will run the check themselves.

## The honest-fragility test

Before submission, ask: "What single change would a hostile referee make to break this result?" Then make that change yourself and report the outcome. If the result breaks under a reasonable alternative, the paper is not ready — return to `restud-identification` (empirical) or `restud-theory-model` (theory) rather than papering over it with more tables.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). REStud is top-5 general-interest economics; credible identification with modern estimators is the bar across applied fields.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or `benjamini_hochberg`.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists missing checks + the exact
  `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Decisive checks in the body, exhaustive battery in the appendix.
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Headline magnitude stable across alternative specifications, not merely same-signed
- [ ] At least one genuine placebo / falsification test
- [ ] Inference re-examined at alternative clustering / with few-cluster correction
- [ ] Mechanism evidence consistent with the asserted channel
- [ ] Heterogeneity cuts pre-specified, not mined
- [ ] Attrition / selection / measurement addressed where relevant
- [ ] The single most fragile assumption is identified and stress-tested

## Anti-patterns

- "Robustness theater" — ten near-identical columns that vary nothing a referee cares about
- A result that flips sign or loses significance under a reasonable alternative spec, reported only in the appendix
- Mechanism claims with no supporting evidence ("we interpret this as ...")
- Data-mined heterogeneity: testing 20 subgroups and headlining the one that is significant
- Hiding the fragile specification instead of confronting it
- Under-powered / fragile empirics presented as definitive

## Output format

```
【MAIN RESULT】<one line>
【SPEC ROBUSTNESS】stable / fragile — details
【PLACEBO】present / absent — what it tests
【INFERENCE】clustering level + few-cluster correction used
【MECHANISM EVIDENCE】[...]
【HETEROGENEITY】pre-specified cuts: [...]
【MOST FRAGILE ASSUMPTION】<identified + how stress-tested>
【NEXT SKILL】restud-tables-figures
```
