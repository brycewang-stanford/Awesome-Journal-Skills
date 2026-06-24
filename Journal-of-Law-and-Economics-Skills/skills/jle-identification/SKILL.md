---
name: jle-identification
description: Use when the causal identification argument is the bottleneck for a The Journal of Law and Economics (JLE) manuscript — a law change (DiD/event study), a court/judge/case-assignment design, a regulatory threshold (RD), or an antitrust/enforcement event. Stress-tests the law-to-outcome mapping to the JLE credibility bar before exhibits are finalized; it does not write the prose or build the deposit.
---

# Identification Strategy (jle-identification)

## When to trigger

- A causal claim about a legal rule rests on OLS + controls, or TWFE on staggered statute adoption
- A court/judge design's random-assignment defense, monotonicity, or exclusion is not pinned down
- A regulatory threshold's density, bandwidth, or bunching response is unaddressed
- An antitrust/enforcement event study has contaminated windows or no clean control market
- You are unsure the design clears JLE's law-and-economics credibility bar

## The JLE identification bar

JLE judges identification through a **law-and-economics lens**: the **mapping from a legal/regulatory source of variation to the causal estimand must be explicit, defended, and consistent with how the rule actually operates**. Referees here are economists who also know the institution — they will ask whether the statute really bound when you say, whether enforcement varied, whether the "control" jurisdiction had its own contemporaneous reform. State the estimand, name the identifying assumption, show the diagnostic that could have failed, and keep the claim inside what the legal design supports. Inference must match the design (cluster at the level of legal variation — usually the jurisdiction; correct for few jurisdictions).

## Design paths

### Path A: Law change / staggered statute adoption (DiD / event study)
- With staggered adoption across jurisdictions, **move beyond TWFE** — Callaway–Sant'Anna, Sun–Abraham, de Chaisemartin–D'Haultfœuille, or Borusyak–Jaravel–Spiess imputation; a Goodman-Bacon decomposition to show which 2×2s drive the estimate.
- **Clean event-study leads** for pre-trends; date treatment to **when the rule binds** (effective date, not signing date), and handle anticipation and phase-ins.
- Rule out **contemporaneous legal change** in treated jurisdictions (other reforms riding the same bill); defend parallel trends across jurisdictions, ideally with Rambachan–Roth honest-DID.

### Path B: Court / judge / case-assignment design (IV or as-good-as-random)
- Establish **random (or as-good-as-random) assignment** of cases to judges/panels; test for balance on case characteristics; document the assignment rule and exceptions (recusal, specialization).
- Judge leniency/stringency as an **instrument**: report first-stage strength, defend **exclusion** (the judge affects the outcome only through the ruling), and **monotonicity** (no defiers).
- State the **LATE** (compliers near the assignment margin); resist reading it as the population effect.

### Path C: Regulatory threshold / eligibility cutoff (RD / bunching)
- **Density test** (McCrary / Cattaneo–Jansson–Ma) for manipulation around the regulatory cutoff; covariate smoothness; **local-linear with data-driven bandwidth** and bias-corrected robust CIs (rdrobust); donut and bandwidth sensitivity.
- Where firms/agents sort to avoid a rule, treat **bunching** as evidence, not noise (size-based regulation, tax/penalty kinks); estimate the response from the missing mass.
- State whether the estimand is the local effect at the threshold and resist extrapolation.

### Path D: Antitrust / enforcement event (merger, decree, entry, ruling)
- Define the **event window** tightly and rule out confounding announcements; for prices/output, use **clean control markets** unaffected by the action.
- Get **market definition** right (the antitrust object); show the treated and control markets were comparable pre-event.
- For merger price effects, consider difference-in-differences across affected vs. unaffected products/regions; for enforcement deterrence, distinguish the targeted firm from spillover deterrence on others.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JLE is empirical law-and-economics — DiD around legal/regulatory change is central.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference + `romano_wolf` for many-outcome control.
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the magnitude in interpretable units; route the full battery to the appendix. A
run end-to-end (synthetic data, real returns) is in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Design chosen; the legal-variation-to-estimand mapping stated in one sentence
- [ ] Estimand named (ATT / LATE / local-at-threshold / event effect) and matched to the design
- [ ] Treatment dated to when the rule **binds**; anticipation/phase-in handled
- [ ] Design-appropriate diagnostic shown (event-study leads + Bacon / assignment balance + first-stage / density + bandwidth / clean control market)
- [ ] Modern estimator where TWFE or 2SLS would bias; contemporaneous legal change ruled out
- [ ] Inference clustered at the jurisdiction/assignment level; few-cluster correction (wild-cluster bootstrap)
- [ ] The claim never exceeds what the legal design identifies (no extrapolation past the local/LATE object)

## Anti-patterns

- TWFE on staggered law changes with no heterogeneity-bias discussion
- Dating treatment to the statute's signing rather than its effective/binding date
- A judge-IV design with no balance test, or with exclusion asserted (the judge surely affects only via the ruling) rather than argued
- An RD at a regulatory cutoff with no density test, or ignoring bunching that signals manipulation
- An enforcement event study with a contaminated window or a "control" market that shared the shock
- Clustering at the firm level when the legal variation is at the state level (over-stated precision)

## Getting the legal timing and bindingness right (the JLE-specific failure)

The single most common identification flaw a law-and-economics referee catches is **mis-specifying when and on whom the rule operates** — a problem generic econometrics training does not flag. Before estimating, pin down:

- **Signing vs. effective vs. enforcement date.** A statute may be signed in one year, take effect the next, and be enforced only once an agency issues rules. Date treatment to when behavior could actually respond; show the others as robustness.
- **Who is bound and who is exempt.** Grandfather clauses, small-firm carve-outs, and phase-ins mean the "treated" group is narrower than the jurisdiction; mis-coding exemptions attenuates the estimate.
- **Anticipation.** If agents knew the rule was coming, pre-period behavior is contaminated; allow for anticipation windows.
- **Court vs. statute.** A judicial decision can change the law mid-period within a jurisdiction; treat a controlling appellate ruling as a treatment date too.

## Worked vignette (illustrative)

A paper studies whether a staggered state damages-cap reform reduced malpractice litigation. The first draft uses TWFE; a referee flags that early-reform states contaminate the comparison. The JLE fix: re-estimate with Callaway–Sant'Anna by adoption cohort, date treatment to the cap's effective date, and show flat event-study leads. A Goodman-Bacon decomposition reveals 22% of the TWFE estimate came from forbidden already-treated comparisons (illustrative). The heterogeneity-robust ATT settles at an 8% fall in claims (s.e. 3), an honest-DID bound shows it survives a plausible pre-trend violation, and a placebo on non-malpractice torts (uncapped) is null — isolating the legal channel.

## Referee pushback mapped to the identification fix

- *"Staggered TWFE here is biased."* → Re-estimate with Callaway–Sant'Anna / Sun–Abraham; show flat leads and a Bacon decomposition.
- *"Your control jurisdictions had their own reforms."* → Document the legal landscape; drop contaminated controls; add a placebo on an unaffected legal area.
- *"Judge assignment isn't really random / the exclusion fails."* → Show assignment balance, the assignment rule, and argue exclusion institutionally with a falsification on never-binding cases.

## Output format

```
【Design】law change / court-assignment / RD-threshold / enforcement event
【Legal-variation-to-estimand mapping】one sentence
【Estimand】ATT / LATE / local-at-threshold / event effect
【Treatment timing】rule binds when: ___ (effective date, not signing)
【Identification evidence】event-leads+Bacon / assignment balance+first-stage / density+bandwidth / clean control market
【Estimator + inference】modern estimator; clustering at jurisdiction; few-cluster/honest-DID if any
【What it does NOT identify】[...]
【Next step】jle-theory-model (if a model is needed) or jle-robustness
```
