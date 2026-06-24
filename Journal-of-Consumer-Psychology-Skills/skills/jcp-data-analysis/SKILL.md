---
name: jcp-data-analysis
description: Use when analyzing experimental data for a Journal of Consumer Psychology (JCP) manuscript — ANOVA/regression on the effect, measured and experimental mediation, moderation and moderated mediation, measurement of the process, and the rigor-era reporting standards. Analyzes the studies; it does not design them (jcp-methods).
---

# Data Analysis (jcp-data-analysis)

## When to trigger

- Your effect is significant but the **process evidence** does not yet hold up
- You ran mediation but a reviewer calls it correlational or under-powered
- A moderation is predicted but the interaction is messy or the simple effects are not probed
- You need to report results to JCP's post-rigor-reform standards (effect sizes, CIs, exclusions)
- The measure of your psychological process is noisy or its validity is in question

## Analyze the process, not just the p-value

JCP's contribution is a mechanism, so the analysis must make the **process** visible and defensible. The headline test of the effect (typically ANOVA or regression with the manipulated IV) is necessary but not sufficient; the paper lives or dies on whether the **mediation/moderation** evidence supports the proposed psychological process and rules out rivals. Report estimates with **effect sizes and confidence intervals**, exact statistics, and full Ns before and after pre-specified exclusions. APA reporting style is the house norm.

## The analysis toolkit by link in the chain

| Link | Standard analysis | What reviewers look for |
|------|-------------------|-------------------------|
| Existence of effect | t-test / ANOVA / OLS with the manipulated IV | clean cells, effect size (d, η²), CI, no covariate fishing |
| Measured mediation | bootstrapped indirect effect (e.g., PROCESS / lavaan), bias-corrected CI | indirect effect with CI excluding 0; honesty that this is **correlational** evidence on the mediator |
| Experimental mediation | causal-chain design or manipulated-mediator analysis | the manipulation of M moves Y as the theory predicts |
| Moderation | regression interaction; ANOVA factorial | interaction term + **probed simple effects** (spotlight/floodlight), not just a significant interaction |
| Moderated mediation | conditional indirect effects (index of moderated mediation) | the index, with CI, and conditional indirect effects by moderator level |

Prefer **experimental/causal-chain mediation and moderation-of-process** over measured-mediator-only inference: JCP reviewers now treat a bootstrapped indirect effect on a self-reported mediator as suggestive, not dispositive, because it cannot establish the causal direction of M → Y.

## Measuring the psychological process

- **Validate the mediator measure**: report reliability (α/ω) for multi-item scales; show the measure captures the intended construct and discriminates from confounds (mood, arousal, difficulty).
- **Rule out alternative mediators** statistically: include rival process measures and show the focal mediator carries the effect when they are modeled together.
- **Avoid mediator-as-manipulation-check confusion**: a manipulation check is not a mediator; the mediator is the downstream mental state.

## Rigor-era reporting (post-2010s consumer-psych reforms)

- Report **exact test statistics, p-values, effect sizes, and CIs** — not just "p < .05."
- Disclose **all conditions and measures** collected; do not hide arms (the disclosure norm).
- Report **sample size determination** and adherence to (or deviation from) the pre-registration.
- State **exclusions and their rule** transparently, with Ns before/after.
- Avoid asterisk-only tables; report the numbers a reader needs to assess the process.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JCP is experimental consumer psychology; randomization inference, mediation done right (`mediate`, not naive controlling-away), and family-wise corrections matter most.

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

- [ ] Effect reported with exact stats, effect size, and CI; cells and Ns clear
- [ ] Mediation uses bootstrapped/bias-corrected CIs; measured-only mediation is labeled correlational
- [ ] At least one stronger-than-Baron-Kenny process test where the claim is causal
- [ ] Moderation: interaction reported **and** simple effects probed (spotlight/floodlight)
- [ ] Moderated mediation: index of moderated mediation + conditional indirect effects
- [ ] Mediator measure reliability reported; rival mediators modeled and ruled out
- [ ] Exclusions pre-specified; all conditions/measures disclosed; preregistration deviations noted

## Anti-patterns

- **Indirect-effect worship**: a significant bootstrapped indirect effect treated as proof of causal process
- **Interaction without simple effects**: a significant interaction with no spotlight/floodlight probing
- **Covariate fishing**: adding controls until the effect appears, undisclosed
- **Hidden arms**: dropping conditions or DVs that didn't work without reporting them
- **p-only reporting**: asterisks instead of effect sizes and CIs
- **Mediator confound**: a "mediator" that is just mood/difficulty the manipulation also moved

## Output format

```text
【Effect】test, stat, effect size, CI, cell Ns
【Mediation】measured / experimental; indirect effect + CI; correlational caveat if measured-only
【Moderation】interaction + probed simple effects (spotlight/floodlight)
【Moderated mediation】index + conditional indirect effects (if applicable)
【Process measure】reliability + rival mediators ruled out
【Rigor disclosures】exclusions, all conditions/measures, preregistration deviations
【Next skill】jcp-contribution-framing
```
