---
name: jimf-robustness
description: Use when a Journal of International Money and Finance (JIMF) result must be shown stable across samples, regimes, measures, and inference choices. Designs the robustness layer mapped to international-finance threats; it does not establish the design (jimf-identification / jimf-empirical-design).
---

# Robustness Strategy (jimf-robustness)

## When to trigger

- The main coefficient is in hand but a referee will ask whether it survives sample, period, and measurement choices
- The result might be driven by one crisis episode, one dominant country (the US), or one regime
- Inference is OLS-clustered-one-way and the panel has serial and cross-sectional correlation
- You are assembling a robustness section and want it to answer *threats*, not pad column count

## The JIMF robustness logic: every check answers a named threat

A JIMF robustness section is persuasive when each exhibit is tied to an *international-finance threat to inference*, not when it is a wall of specifications. Build the section as a threat → check map. The threats that JIMF referees raise most are: a single global episode driving everything; US-centrism; regime dependence; a fragile measurement choice; and inference that ignores cross-country dependence.

| Threat (JIMF-specific) | Check that answers it |
|------------------------|------------------------|
| One global episode drives the result (GFC, taper tantrum, COVID) | Drop the episode / window; rolling samples; show stability |
| US-centrism — the result is the dollar / the Fed, not "international" | Drop the US; use NEER not USD; replicate with ECB/other-center shocks |
| Regime dependence (peg vs. float; capital-account open vs. closed) | Split by Ilzetzki–Reinhart–Rogoff regime; interact with openness (Chinn–Ito / AREAER) |
| Fragile measurement | Swap CDS↔spread, gross↔net flows, VIX↔GFCy factor, policy rate↔shadow rate |
| Cross-country / serial dependence in inference | Two-way clustering; Driscoll–Kraay; wild-cluster bootstrap with few countries |
| Reverse causality / anticipation | Lead-lag tests; placebo windows; controls for ex-ante exposure |
| Outliers / influential country-quarters | Winsorize; jackknife by country; influence diagnostics |
| Omitted global factor | Add time fixed effects (absorbs common shocks) and show within-time variation still identifies |

## How to sequence and present it

1. **Lead with the threat the referee will raise first** — usually "this is just the GFC" or "this is just the dollar." Answer it in the main text, not the appendix.
2. **Show point-estimate stability, not just significance.** A coefficient that wanders from 0.6 to 0.1 across measures is fragile even if each stays "significant." Plot the estimate across specifications (a specification curve or coefficient-stability figure reads well at JIMF).
3. **Use time fixed effects as both a control and a diagnostic.** Adding time FE that absorb all common global shocks and seeing the within-time (cross-country) coefficient survive is the cleanest answer to "it's the global cycle."
4. **Match inference to the panel.** With ~20–60 countries and serially correlated errors, one-way clustering understates SEs; report Driscoll–Kraay or two-way clustering, and wild-cluster bootstrap when the cluster count is small.
5. **Demote the rest to the online appendix** with a map (see `jimf-internet-appendix`).

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JIMF is international macro-finance; cross-country panels + asset pricing — identification plus factor/Newey-West inference.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or `benjamini_hochberg`.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists missing checks + the exact
  `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Decisive checks in the body, exhaustive battery in the appendix.
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Each robustness exhibit names the threat it answers
- [ ] "It's just the GFC/COVID" answered by dropping the episode and by rolling samples
- [ ] "It's just the dollar/Fed" answered by dropping the US, using NEER, or a non-US center
- [ ] Regime/openness dependence tested (IRR classification; Chinn–Ito / AREAER openness)
- [ ] Headline measure swapped for the leading alternative; point estimate stable, not just significant
- [ ] Inference accounts for cross-country and serial dependence (Driscoll–Kraay / two-way / wild bootstrap)
- [ ] Influential single country ruled out (jackknife by country)
- [ ] The two reflex checks (drop-US, drop-episode) are in the main text, not buried in the appendix
- [ ] Time fixed effects shown to leave within-time identification intact (or absence justified)

## Anti-patterns

- A robustness section that is 15 specifications with no statement of which threat each addresses
- Reporting only that significance survives while the point estimate halves across measures
- Never dropping the US or the GFC episode — the two checks every JIMF referee wants
- One-way clustering on a 30-country panel with obvious serial and cross-sectional correlation
- Treating "we added more controls" as robustness when the threat is a global confounder (which time FE, not controls, address)
- Burying the most important robustness (regime split, drop-US) in the appendix where the editor won't see it

## Robustness vs. identification (do not confuse them)

A robustness section cannot rescue a non-identified estimate; it can only show an identified estimate is stable. If a referee's concern is that the result is *not causal* (a global confounder, endogenous policy), that is an identification problem owned by `jimf-identification` — adding twenty more specifications does not address it. Robustness here means: holding the identification fixed, does the magnitude survive reasonable choices of sample, period, regime, measure, and inference? Keep the two sections distinct, and do not pad robustness to compensate for a weak design.

## Worked vignette (illustrative)

A draft's headline is that capital-account openness amplifies spillovers. The referee suspects it is mechanically the 2008 crisis and the dollar. The JIMF fix: (1) drop 2008Q3–2009Q2 and show the interaction holds; (2) re-estimate with time fixed effects so only cross-country differences in openness identify the coefficient; (3) split by IRR regime and show the amplification is in floats; (4) re-run with two-way (country and quarter) clustering, where the openness interaction stays at ~0.4 (s.e. 0.15, illustrative). Each check is captioned with the threat it kills.

## Referee pushback mapped to the robustness fix

- *"This is just the 2008 crisis."* → Drop the crisis window and show the coefficient holds; add rolling-sample estimates so the reader sees stability over time.
- *"This is just the dollar / the US."* → Drop the US from the panel; re-run in NEER terms; replicate with a non-US monetary center (ECB) where feasible.
- *"It only works for floats / open economies."* → Either own the regime dependence as a finding (split by IRR / openness) or show it holds across regimes.
- *"Your standard errors are too small."* → Move from one-way to two-way or Driscoll–Kraay; wild-cluster bootstrap with few countries; report how inference changes.
- *"One country drives this."* → Jackknife by country; show the estimate is not an artifact of a single influential country-quarter.

## Sequencing the robustness section against page limits

Lead the main-text robustness with the two checks every JIMF referee runs in their head — drop the obvious episode and drop the US — plus the time-FE diagnostic for the global confounder. Put measurement swaps and the full regime/openness grid in the online appendix with an index (see `jimf-internet-appendix`). The goal is that the editor, reading only the body, already sees the result is not the crisis, not the dollar, and not the global cycle; everything else is there for the referee who wants it.

## Output format

```text
【Journal】Journal of International Money and Finance
【Skill】jimf-robustness
【Top threat answered in main text】GFC-only / dollar-only / regime / measurement / inference
【Stability shown】point estimate across specs (not just significance)? [Y/N]
【Regime + openness split】IRR / Chinn–Ito / AREAER tested? [Y/N]
【Inference】Driscoll–Kraay / two-way / wild bootstrap as warranted
【Demoted to appendix】list → jimf-internet-appendix
【Next skill】jimf-tables-figures
```
