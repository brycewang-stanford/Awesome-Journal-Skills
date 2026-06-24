---
name: worlddev-identification
description: Use when the inference logic is the bottleneck for a World Development (WD) manuscript — credible causal design for quantitative work, or a transparent inferential logic for qualitative and mixed-methods work. Stress-tests the strategy to WD's pluralist bar before exhibits are finalized.
---

# Identification & Inference Strategy (worlddev-identification)

## When to trigger

- A causal claim rests on OLS + controls, or TWFE on staggered timing
- An RCT or quasi-experiment exists but the estimand and external relevance are unstated
- A **qualitative** paper makes causal-sounding claims with no explicit inferential logic
- A **mixed-methods** paper runs strands in parallel without saying how they jointly warrant the claim
- You are unsure whether the evidence clears WD's bar for the *kind* of claim being made

## WD's pluralist standard

WD does not impose a single identification template. It imposes a single demand: **the route from evidence to claim must be explicit, defended, and matched to the claim's strength.** A paper that says "is associated with" needs descriptive credibility; a paper that says "causes" needs a design that earns it; a paper that says "this mechanism explains why" needs a logic — quantitative or interpretive — that traces the mechanism. The cardinal sin at WD is a **claim that outruns its warrant**, in either direction (over-claiming causality from correlation, or burying a genuine causal design under hedging). Pick the branch that fits your claim and make the warrant transparent.

### Branch A — Quantitative causal design

- **DID / event study:** with staggered adoption, move past TWFE (Callaway–Sant'Anna, Sun–Abraham, de Chaisemartin–D'Haultfœuille); show clean pre-trends; report a Goodman-Bacon decomposition where relevant.
- **IV:** strong first stage; with weak instruments use Anderson–Rubin / weak-IV-robust sets; defend exclusion in institutions and theory, not just algebra — WD referees probe whether the instrument is plausible *in that development context*.
- **RDD:** density (McCrary / Cattaneo–Jansson–Ma) test; optimal bandwidth + robustness; covariate smoothness; bias-corrected CIs.
- **RCT:** explicit estimand; randomization balance; attrition (Lee bounds if differential); multiple-hypothesis adjustment; and — distinctively for WD — **external relevance**: why this site/sample teaches something beyond itself.
- Inference clustered at the assignment/treatment level; address few-cluster issues (wild-cluster bootstrap). Spatial correlation matters in development data — consider Conley SEs.

### Branch B — Qualitative inference

Qualitative is **not** second-class at WD. The bar is transparency of inference, not sample size.

- **Name the logic:** process tracing, comparative case logic (most-similar / most-different), congruence testing, or interpretive thematic analysis — say which.
- **Case selection justified by the logic**, not by convenience; explain why these cases can bear the claim.
- **Evidence trail:** how data were generated (interviews, archives, observation), coding approach, and how rival explanations were tested and rejected (not merely mentioned).
- **Trustworthiness:** triangulation across sources, attention to negative cases, reflexivity about the researcher's position.

### Branch C — Mixed-methods integration

The contribution of a mixed-methods paper is the **integration**, not the coexistence of two strands. State the design (sequential explanatory, sequential exploratory, convergent) and what each strand does that the other cannot: e.g., the quant estimates *how much*, the qual explains *why* and *for whom*. A paper where the qualitative section is decorative will be read as a quantitative paper with an unexamined appendix.

## Referee pushback mapped to the fix

- *"OLS with controls is not identification."* → Find a design (DID/IV/RDD) or downgrade the claim to descriptive and own it.
- *"Staggered TWFE is biased here."* → Re-estimate with Callaway–Sant'Anna / Sun–Abraham; show flat leads.
- *"Why these three cases?"* → Justify selection by the inferential logic and show how rivals were ruled out.
- *"The RCT is clean but local."* → Argue external relevance: mechanism, scope conditions, transferable lessons.
- *"The qual and quant don't talk to each other."* → Make the integration explicit; show the joint inference.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). World Development is multidisciplinary development studies; the chain serves its quantitative-causal lane, mixed-methods work uses its own standards.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference + `romano_wolf` for many-outcome control.
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the magnitude in interpretable units; route the full battery to the appendix. A
run end-to-end (synthetic data, real returns) is in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Branch chosen; the evidence-to-claim route stated in one sentence
- [ ] Quant: design-appropriate diagnostics (pre-trends / density / first-stage / balance); modern estimator where TWFE would bias; clustering correct
- [ ] Qual: inferential logic named; case selection justified; rivals tested, not just listed
- [ ] Mixed: integration design stated; each strand's distinct job is explicit
- [ ] External relevance argued for single-site/single-case work
- [ ] Inference reported with SEs / coverage (no significance asterisks); the claim never exceeds the warrant

## Anti-patterns

- "Causes" from OLS + controls with no design
- Treating a qualitative paper as needing "more N" rather than a clearer inferential logic
- A mixed-methods paper that runs strands in parallel and never integrates them
- An RCT presented with no discussion of who is left out or whether it travels
- Significance asterisks instead of standard errors / confidence intervals

## Output format

```text
【Journal】World Development (WD)
【Skill】worlddev-identification
【Branch】quant-causal / qualitative / mixed
【Evidence→claim route】one sentence
【Warrant evidence】design diagnostics / inferential logic + rival tests / integration design
【External relevance】why it travels beyond the site/case
【What it does NOT warrant】the claim it cannot support
【Source status】verified URL / 待核实 / not asserted
【Next skill】worlddev-theory-model
```
