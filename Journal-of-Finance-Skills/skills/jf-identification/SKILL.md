---
name: jf-identification
description: Use when the causal-identification strategy is the bottleneck for a corporate / empirical The Journal of Finance (JF) manuscript — natural experiments, IV, DID, RDD. Stress-tests the design; for asset-pricing tests use jf-empirical-design.
---

# Causal Identification (jf-identification)

## When to trigger

- The paper makes a causal claim ("X causes Y") resting on a research design
- You rely on an instrument, a shock, a discontinuity, or a diff-in-diff and a referee will attack the exclusion/parallel-trends assumption
- Endogeneity (reverse causality, omitted variables, selection) threatens the headline result

> Scope: corporate / empirical causal effects. For cross-sectional asset-pricing tests use `jf-empirical-design`.

## JF's bar for identification

JF is the AFA flagship, general-interest, with a ~5% acceptance rate and ~33–45% desk rejection (afajof.org editor reports, accessed 2026-05-30). For a corporate/empirical paper, **credible identification is usually the binding constraint** — a clever question with a weak design is a classic JF desk reject. The design must convince a broad AFA readership, not just specialists.

## Design audit

| Design                 | Core assumption to defend                     | Standard JF attack to pre-empt                 |
|------------------------|-----------------------------------------------|------------------------------------------------|
| Natural experiment     | Shock is plausibly exogenous & well-timed     | Anticipation; confounding co-occurring events  |
| Instrumental variables | Relevance + exclusion                         | "Why does the instrument affect Y only via X?" |
| Diff-in-diff           | Parallel trends; no differential shocks       | Pre-trends; staggered-adoption bias            |
| RDD                    | No manipulation; continuity at the cutoff     | Bunching; bandwidth sensitivity                |

- State the **source of variation** in one sentence in the introduction (JF rewards a clearly named shock or instrument).
- Show the **identifying assumption** is testable where possible (pre-trends, first-stage F, McCrary test) and put the full battery in the **Internet Appendix** (bundled in the same PDF; see `jf-internet-appendix`).
- Report **economic magnitude**, since JF writes for a general-interest reader.

## Worked vignette — a staggered-regulation natural experiment

*Illustrative numbers.* A paper claims a disclosure regulation, rolled out across states in 2011–2016, causes treated firms to cut leverage; the DID shows book leverage falling 4.2 pp (t = 3.4). Walk it through JF's bar:

1. **Name the variation in one sentence**: "Staggered state-level adoption of Rule X gives treated firms a plausibly exogenous shock to disclosure costs" — the introduction's credibility hook for a broad-readership editor.
2. **Defend the assumption**: an event-study plot shows flat pre-trends before adoption; the full coefficient panel goes to the Internet Appendix.
3. **Fix the staggered-adoption bias**: a naive two-way fixed-effects estimate (4.2 pp) is contaminated by already-treated controls. Re-estimate with a modern estimator (Callaway–Sant'Anna or Sun–Abraham); the clean estimate lands at ~3.1 pp — report it and flag the TWFE bias.
4. **Pre-empt anticipation**: show no effect in the year before the law as a placebo.
5. **Report magnitude**: 3.1 pp on a ~30% mean is a ~10% relative move — say so, since JF prizes economically large effects over bare significance.

The editor sees a named shock, a defended assumption, the right estimator, and a magnitude that matters to the AFA readership.

### Referee-pushback patterns and the JF-specific fix
| Pushback you will hear                              | JF-specific fix                                                  |
|----------------------------------------------------|------------------------------------------------------------------|
| "Your TWFE DID is biased under staggered adoption" | Re-estimate with Callaway–Sant'Anna / Sun–Abraham; show both     |
| "The instrument could affect Y through other channels" | Spell out the one channel; falsification on the alternative paths |
| "Treated and control firms differ at baseline"     | Balance table + covariate-trend plot in the Internet Appendix    |
| "The shock coincides with the 2014–16 oil bust"    | Excluded-period re-estimation; industry × year fixed effects     |
| "Is 3 points economically meaningful?"             | Express as % of the sample mean and tie to a dollar magnitude    |

## Calibration anchors for JF identification
- For a corporate/empirical paper, identification is typically the **binding constraint**: a first-order question with a fragile design is a classic flagship desk reject, while a less novel question with airtight identification can survive.
- JF expects the **identification battery visible but not bloating the body** — pre-trends, first-stage F, McCrary density, balance tables go to the Internet Appendix, with one or two decisive plots in the main text.
- Weak-instrument and modern-DID standards evolve; confirm the expected diagnostics against recent issues and current author guidelines.

## Execution bridge (StatsPAI / Stata MCP)

Do not stop at advising the right estimator — **run it and report the number.** Full
map: [`shared-resources/empirical-methods/execution-with-mcp.md`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JF-specific instantiation:

1. `detect_design` → `preflight` → `recommend` on the data; fit with `as_handle=true`.
2. **Staggered DiD:** estimate with `callaway_santanna` / `sun_abraham` (not bare TWFE);
   run `bacon_decomposition` to expose the bad-comparison weight you are correcting —
   this *is* the "TWFE is biased" pre-emption, executed. Put the clean estimate in the
   body; the event-study/pre-trend panel goes to the **Internet Appendix**.
3. **IV:** report `effective_f_test` and an `anderson_rubin_ci` (weak-IV-robust), not a
   2SLS t-stat alone.
4. **RDD:** `rdrobust` for the bias-corrected estimate; `rddensity`/`mccrary_test` and
   bandwidth sweep (`rdbwselect`) → Internet Appendix; one density/RD plot in the body.
5. `audit_result(result_id)` to enumerate what the design still owes; then
   `honest_did_from_result` to bound a pre-trend violation. Cite methods only via
   `bibtex`.

The JF body shows one or two decisive exhibits with the **economic magnitude**; the
full diagnostic battery lives in the bundled Internet Appendix (see `jf-internet-appendix`).
If StatsPAI/Stata are not connected, adapt the vendored `resources/code/` skeleton and
say which number is unverified.

See this run end-to-end on synthetic data — every number an actual tool return — in
[`resources/worked-examples/02-execution-walkthrough.md`](../../resources/worked-examples/02-execution-walkthrough.md)
(TWFE −0.0227 vs clean CS −0.0272, pre-trends p = 0.155, honest-DiD breakdown point).

## Checklist

- [ ] Source of identifying variation named in one sentence
- [ ] Exclusion / parallel-trends / continuity assumption explicitly defended
- [ ] First-stage strength (IV) or pre-trend evidence (DID) shown
- [ ] Modern estimators used where staggered adoption applies
- [ ] Confounders and anticipation effects addressed
- [ ] Magnitude interpreted, not just significance

## Anti-patterns

- A causal verb ("increases", "causes") with only conditional correlations behind it
- An instrument with a hand-waved exclusion restriction
- Two-way fixed-effects DID on staggered adoption with no modern correction
- A clever question whose design no broad-readership editor would send out

## Output format

```
【Design】NE / IV / DID / RDD
【Source of variation (1 sentence)】...
【Key assumption + how defended】...
【Main threat pre-empted?】yes / no
【Magnitude】...
【Next step】jf-robustness
```
