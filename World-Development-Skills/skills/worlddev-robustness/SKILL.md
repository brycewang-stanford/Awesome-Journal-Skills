---
name: worlddev-robustness
description: Use when results may be sensitive — to specification, sample, measurement, or inference for quantitative work, or to interpretation and triangulation for qualitative work — in a World Development (WD) manuscript. Organizes checks by threat; it does not invent evidence or citations.
---

# Robustness & Trustworthiness (worlddev-robustness)

## When to trigger

- The headline result moves under plausible alternative specifications
- A referee suspects the finding is driven by one region, one wave, or one measurement choice
- Development data are messy (recall error, measurement in informal economies, attrition) and this is unaddressed
- A qualitative finding rests on a few vivid quotes with no account of disconfirming evidence
- The robustness section is a mechanical dump of appendix tables organized by table, not by threat

## Organize by threat, not by table

The single biggest WD robustness failure is a wall of appendix tables with no logic. A WD referee — often from a different discipline than the author — wants to see that you **identified the threats to your specific claim and addressed each one**. Structure the robustness work as a short list of named threats, each with the check that retires it and a one-line verdict. For each threat: *what would break the claim, what test isolates it, what the test shows.*

### Quantitative threat map

| Threat | Check |
|--------|-------|
| Specification dependence | Add/drop controls in a disciplined sequence (Oster-style δ/bounds); specification curve if the literature is unsettled |
| Sample / outlier dependence | Drop influential units, regions, or waves; leave-one-out; trim |
| Measurement error (acute in development data) | Alternative measures; validation against an independent source; bounds |
| Inference fragility | Cluster at the right level; few-cluster wild bootstrap; spatial (Conley) SEs; randomization inference for RCTs |
| Selection / attrition | Lee bounds; selection models; characterize who exits |
| Multiple hypotheses | Romano–Wolf or sharpened q-values across the family of outcomes |
| Mechanism vs. confound | Show the proposed mechanism's footprint; rule out the leading alternative explicitly |

Run the checks the threat justifies — not the full menu. A paper that reports forty robustness tables but never addresses the obvious confound has gold-plated the wrong corner.

### Qualitative trustworthiness map

Robustness for qualitative WD work is **trustworthiness**, and it is judged, not waived:

- **Triangulation:** corroborate key claims across data sources or informant types.
- **Negative-case analysis:** actively present and account for evidence that cuts against the argument — its absence is a red flag.
- **Member checking / saturation:** where appropriate, evidence that interpretations were checked and categories stabilized.
- **Audit trail:** enough on coding and analysis that another researcher could follow the inference.
- **Reflexivity:** acknowledge how the researcher's position shaped access and interpretation.

### Mixed-methods

Show the strands **converge or that divergence is informative**. When quant and qual disagree, that tension is data — explain it rather than hiding the weaker strand.

## Development-specific traps WD referees catch

- Treating survey measures from informal/subsistence settings as if measured with the precision of administrative data
- Ignoring spatial autocorrelation in geographically clustered development data
- Pooling heterogeneous countries/regions and reporting one average that masks the policy-relevant variation
- Generalizing from one program/site without scope conditions
- Reporting the robust result but not the *fragile* one a skeptic would run

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). World Development is multidisciplinary development studies; the chain serves its quantitative-causal lane, mixed-methods work uses its own standards.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or `benjamini_hochberg`.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists missing checks + the exact
  `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Decisive checks in the body, exhaustive battery in the appendix.
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Robustness organized by named threat, each with check + one-line verdict
- [ ] Inference matched to the design (clustering level, few-cluster, spatial, randomization)
- [ ] Measurement error addressed where development data warrant it
- [ ] The leading alternative explanation is ruled out, not merely mentioned
- [ ] Qual: triangulation + negative cases + audit trail present
- [ ] Heterogeneity that matters for policy is shown, not averaged away
- [ ] No significance asterisks; effect sizes and uncertainty reported in real units

## Anti-patterns

- A robustness appendix sorted by table number with no threat logic
- Forty checks for a non-threat, zero for the obvious confound
- Burying a fragile headline result and reporting only the survivor specifications
- Qualitative work that quotes only confirming voices and never the disconfirming ones
- Hiding quant/qual divergence in a mixed paper instead of explaining it

## Output format

```text
【Journal】World Development (WD)
【Skill】worlddev-robustness
【Verdict】robust / fragile / mixed
【Threats addressed】[threat → check → verdict] for each
【Leading alternative】how it is ruled out
【Qual trustworthiness】triangulation / negative cases / audit trail (if applicable)
【Policy-relevant heterogeneity】shown / hidden
【Source status】verified URL / 待核实 / not asserted
【Next skill】worlddev-tables-figures
```
