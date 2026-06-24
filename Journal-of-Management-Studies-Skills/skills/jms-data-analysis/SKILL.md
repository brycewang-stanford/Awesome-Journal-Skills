---
name: jms-data-analysis
description: Use when the execution and credibility of the analysis is the bottleneck for a Journal of Management Studies (JMS) manuscript — regression/SEM and robustness for quantitative work, OR coding, abduction, and trustworthiness for qualitative work. Runs and defends the analysis; it does not design the study (jms-methods) or build exhibits (jms-tables-figures).
---

# Data Analysis (jms-data-analysis)

## When to trigger

- Estimates are in but reviewers question endogeneity, robustness, or the indirect-effect claim
- A qualitative analysis reaches findings but the path from data to constructs is not auditable
- Effects hinge on a single specification with no robustness
- A mediation/moderation result is reported without the analysis JMS expects
- A reviewer says "the analysis does not support the claim" or "I can't see how you got here"

## The JMS analysis bar — two idioms, one standard

JMS judges analysis by whether it **credibly supports the theoretical claim**, in whichever idiom the study uses. Quantitative work is held to identification and robustness standards; qualitative work is held to **trustworthiness and transparency** standards. Use the path that matches your design; do not import quant criteria (p-values, effect sizes) to judge a qualitative paper, or qualitative looseness into a quantitative one.

## Quantitative path

- **Specification & estimator**: match the estimator to the data structure (OLS/GLM, fixed effects for panels, SEM for latent constructs and full mediation models, multilevel models for nested data). State why.
- **Mediation done right**: test indirect effects with bootstrapped confidence intervals (not Baron–Kenny steps alone); but remember an indirect effect is *evidence for* a theorised mechanism, not a substitute for theorising it.
- **Moderation**: plot the interaction; report simple slopes and the region of significance; do not over-read a marginal interaction.
- **Endogeneity & robustness**: run the identification strategy planned in `jms-methods` (FE, IV/2SLS, DiD, matching) and a robustness battery — alternative measures, alternative samples, controls in/out — each tied to a *named threat*, not a fishing expedition.
- **Measurement evidence**: report reliability (alpha/CR), convergent/discriminant validity (AVE), and CFA fit; address CMB with a designed test, not only Harman.

## Qualitative path

- **Coding transparency**: show the move from first-order codes → second-order themes → aggregate dimensions; a reader should be able to trace a quote to a construct.
- **Abductive logic**: make the iteration between data and theory explicit — surprising observations, the candidate explanations considered, why the retained one fits best. JMS rewards visible abduction, not a tidy after-the-fact story.
- **Evidentiary support**: a representative-quotes table tying each theme to data; report disconfirming/negative cases and how they refined the model.
- **Trustworthiness**: state the procedures used (audit trail, member checking, inter-coder reliability where appropriate, prolonged engagement) so credibility is demonstrable.
- **From narrative to mechanism**: for process work, show *what drives the transitions* across phases, not just the sequence.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JMS mixes qualitative and quantitative management research; the chain below is for the quantitative-empirical lane.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or
  `benjamini_hochberg` — report the adjusted threshold.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`;
  multilevel data → cluster at the right level.
- **Re-fit off one handle:** `audit_result(result_id)` lists the missing checks and the
  exact `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Keep the decisive checks in the body and the exhaustive battery in the appendix. See the
executed chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Path chosen (quantitative / qualitative) and matched to the design
- [ ] Quant: estimator fits the data; mediation via bootstrapped CIs; interactions plotted with simple slopes
- [ ] Quant: each robustness check tied to a named threat; CMB addressed by design; CFA/validity reported
- [ ] Qual: first-order → second-order → aggregate-dimension chain is auditable
- [ ] Qual: abductive reasoning visible; representative quotes table; negative cases reported
- [ ] Qual: trustworthiness procedures stated
- [ ] The claim never exceeds what the analysis supports

## Anti-patterns

- **Mechanism by mediation**: claiming a process exists only because the indirect effect is significant
- **Robustness theatre**: a wall of checks that never names the threat each one rules out
- **p-hacking / specification mining**: the one significant model among many, presented as the model
- **Quote-mining**: cherry-picked quotes with no systematic coding behind them
- **Tidy abduction**: a too-clean narrative that hides the messy data-theory iteration reviewers want to see
- **Idiom confusion**: judging a qualitative paper by sample size and significance, or a quant paper by "richness"

## Output format

```text
【Path】quantitative / qualitative
【Quant】estimator + why; mediation (bootstrap CI); moderation (simple slopes); robustness→threats; CMB/CFA
【Qual】coding chain (1st→2nd→dimensions); abduction made visible; quotes table; negative cases; trustworthiness
【Claim support】does the analysis carry the theoretical claim? gaps …
【Next step】jms-tables-figures
```
