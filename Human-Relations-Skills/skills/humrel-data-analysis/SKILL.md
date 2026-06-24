---
name: humrel-data-analysis
description: Use when executing and reporting the analysis for a Human Relations (HR) manuscript — qualitative coding and data-to-theory construction, critical interpretation, or quantitative estimation and robustness. Makes the evidence-to-theory link transparent; it does not design the study (see humrel-methods).
---

# Data Analysis & Evidence (humrel-data-analysis)

## When to trigger

- You have data but the path from data to theory is opaque
- Qualitative: quotes are decorative, not evidentiary; coding is undocumented
- Critical: the interpretation reads as assertion rather than disciplined reading of the material
- Quantitative: main results exist but theorizing stops at the coefficient
- A reviewer asks "how did you get from your data to these constructs?"

## The HR bar: make the inference auditable, then theorize beyond it

HR judges each tradition on its own terms, but every branch must satisfy the same demand: a reader should be able to *see how the evidence became theory*, and the analysis must yield the "unique and substantive theoretical contribution" the journal screens for. The relational, social nature of work should remain visible in the analysis — not abstracted away into variables or quotations stripped of context.

## Branch A — Qualitative analysis (the data-to-theory ladder)

- **Transparent coding.** Document first-order codes (informant terms), second-order themes (your constructs), and aggregate dimensions — a Gioia-style data structure — or an equivalent (Eisenhardt cross-case, Langley process bracketing). State who coded, how disagreements were resolved, and how iteration proceeded.
- **Data-to-theory table.** Link representative raw evidence → codes → constructs so the inference is auditable (build with `humrel-tables-figures`).
- **Power quotes vs. proof quotes.** A few vivid quotes in the body; corroborating quotes in tables/appendix. Quotes must *carry* the claim, not illustrate it after the fact.
- **Patterned evidence + negative cases.** Back each construct with evidence across informants; report disconfirming instances and how they refined the theory.
- **Process display.** For process theory, show the temporal/event structure (timeline, phase model, visual map).

## Branch B — Critical analysis

- Make the **interpretive procedure** explicit (how texts/talk/practices were read; which discursive or material features mattered) so the reading is disciplined, not just asserted.
- Keep **reflexivity** active: how your standpoint shaped the interpretation.
- Tie the critique to a **constructive theoretical claim** — the analysis should leave readers with a new way to understand, not only a debunking.

## Branch C — Quantitative analysis

- **Main models** match the design (multilevel/mixed, panel FE, SEM, event-history) with standard errors clustered at the right level.
- **Construct validity in the analysis:** report reliabilities, factor structure, and discriminant validity; address common-method concerns with design or statistical remedies where same-source.
- **Robustness that targets the theory's threats:** alternative measures, samples, specifications, and endogeneity checks — not a table farm.
- **Interpret magnitudes** in substantive, relational terms, not significance stars alone; HR house style for exhibits avoids decorating tables with asterisks as the "result."
- **Probe the mechanism** (mediation/moderation or supplementary tests), don't stop at X→Y.

## Either branch — the "so what" of the evidence

- Tie every result back to the mechanism and the theoretical surprise.
- Distinguish what the data *can* and *cannot* establish — overclaiming is a fast route to rejection.
- Mind the **data transparency matrix:** if several papers draw on the same dataset, you must declare them and provide a matrix of which variables/quotations each uses; failure is grounds for rejection (检索于 2026-06；以官网为准).

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Human Relations blends critical/qualitative and quantitative work; apply the chain below to its survey / experimental quantitative papers.

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

- [ ] Qual: data structure (first-order → second-order → dimensions) documented
- [ ] Qual: a data-to-theory table built; quotes carry (not decorate) claims; negative cases reported
- [ ] Critical: interpretive procedure explicit; reflexivity active; claim is constructive
- [ ] Quant: reliabilities/validity reported; SEs clustered correctly; magnitudes interpreted
- [ ] Mechanism probed, not just the headline relationship
- [ ] Claims matched to what the evidence can support; limits stated
- [ ] Same-dataset papers declared with a transparency matrix if applicable

## Anti-patterns

- "Anecdotal" qualitative work: cherry-picked quotes, no coding transparency
- Quotes that illustrate a pre-set conclusion rather than supporting it
- Critical readings asserted with no statement of how the material was analyzed
- Robustness theater that never addresses the real threat
- Reporting significance with no substantive magnitude or relational meaning
- Concealing other papers built on the same dataset

## Output format

```text
【Journal】Human Relations
【Skill】humrel-data-analysis
【Branch】qualitative / critical / quantitative
【Data-to-theory link】data structure / interpretive procedure / mechanism tests
【Key evidence】power quotes or main estimates (with magnitude)
【Robustness/trustworthiness】checks done + gaps
【Transparency】same-dataset matrix needed? (yes/no/NA)
【Next skill】humrel-contribution-framing
```
