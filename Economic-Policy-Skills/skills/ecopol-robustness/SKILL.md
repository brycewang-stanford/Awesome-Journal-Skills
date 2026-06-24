---
name: ecopol-robustness
description: Use when an Economic Policy (EP) manuscript's results may be specification-, sample-, or inference-fragile, especially ahead of the two-discussant panel. Organizes robustness by the threat a discussant will raise; it does not invent evidence or citations.
---

# Robustness Strategy (ecopol-robustness)

## When to trigger

- The headline policy magnitude moves under plausible alternative specifications
- A discussant could attribute the result to one sample, period, or country
- Inference rests on few clusters / few treated units (common in policy evaluations)
- The result is statistically significant but the **magnitude** — the part a policymaker uses — is imprecise
- You are pre-empting the academic discussant's "have you tried…" before the conference

## Robustness is discussant-proofing, not a checklist dump

At EP, robustness has a specific purpose: the paper will be debated live by **two invited discussants** who act as the referees, and the academic one will arrive with a list of fragility tests. So organize robustness **by the threat each test neutralizes**, not as a mechanical appendix of "alternative specifications." A reader (and the policy discussant) should see, for each test, *which way of being wrong it rules out*. Because EP papers carry a recommendation, the central object to defend is the **magnitude and its confidence interval**, not just the sign.

## The threat-to-test map (build the robustness section from this)

| Threat a discussant will raise | The test that answers it |
|--------------------------------|--------------------------|
| "It's driven by one period/sample" | leave-one-out by year/region; pre/post-crisis split |
| "Functional form is doing the work" | alternative specifications; semi/non-parametric check |
| "Parallel trends / pre-trends fail" | event-study leads; honest-DID / pre-trends sensitivity bounds |
| "Confounders you didn't control for" | coefficient-stability / Oster δ bounds; placebo on unaffected groups |
| "Inference is too optimistic with few clusters" | wild-cluster bootstrap; randomization inference |
| "Measurement error in the policy variable" | alternative coding; instrument or bound the error |
| "It won't generalize beyond this case" | replicate on a second jurisdiction/episode if data allow |

## Craft moves

- **Put a robustness summary in the main text**, not buried 40 pages deep: a compact figure or sentence showing the headline number is stable across the threats that matter. The policy discussant will not read the appendix.
- **Distinguish robustness from heterogeneity.** Stable-everywhere = robust; differs-by-group = a finding to report, not a failure to hide.
- **Report the range, not just a star.** "The effect lies between X and Y across all specifications" is the EP-useful statement.
- **Pre-register the discussant's likely objections** (use `ecopol-referee-strategy`) and answer the top three in the main text proactively — you cannot reply live as easily as in a referee letter, so anticipate.
- **Honesty about fragility.** If one test moves the number, say what it implies for the policy conclusion rather than hiding it — discussants will find it.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Economic Policy is policy-facing applied economics; foreground a credible design and a policy-relevant magnitude.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or `benjamini_hochberg`.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists missing checks + the exact
  `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Decisive checks in the body, exhaustive battery in the appendix.
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Robustness section organized by threat, each test labeled with the threat it neutralizes
- [ ] A main-text robustness summary (figure or sentence) — not appendix-only
- [ ] Headline **magnitude + CI** shown to be stable (or its instability honestly bounded)
- [ ] Few-cluster / few-treated inference addressed (wild bootstrap / randomization inference)
- [ ] Pre-trends / parallel-trends sensitivity reported where the design needs it
- [ ] Coefficient-stability or placebo evidence against unobserved confounders
- [ ] Heterogeneity reported as a finding, not disguised as robustness
- [ ] Top three likely discussant objections answered proactively in the main text

## Anti-patterns

- A 20-table appendix of "alternative specifications" with no map to the threats they address
- Defending only significance while the policy-relevant magnitude swings across specifications
- Standard clustered SEs with five treated jurisdictions and no few-cluster correction
- Burying every robustness result in the appendix where the policy discussant never sees it
- Quietly dropping a specification that breaks the result instead of reporting and interpreting it

## Output format

```text
【Journal】Economic Policy (EP)
【Skill】ecopol-robustness
【Headline magnitude】X (CI: [.,.]) — stable across threats? Y/N
【Threats neutralized】[sample / functional form / pre-trends / confounders / inference / measurement / external]
【Main-text summary】figure/sentence present? Y/N
【Few-cluster inference】method used
【Honest fragility note】what moves the number and the policy implication
【Next skill】ecopol-tables-figures
```
