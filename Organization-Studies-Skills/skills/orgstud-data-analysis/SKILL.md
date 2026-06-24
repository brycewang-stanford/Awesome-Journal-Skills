---
name: orgstud-data-analysis
description: Use when executing and reporting the analysis for an Organization Studies (OS) manuscript — qualitative coding and the data-to-theory ladder, process analysis, or quantitative estimation and robustness. Makes the evidence-to-theory link transparent; it does not design the study (see orgstud-methods).
---

# Data Analysis & Evidence (orgstud-data-analysis)

## When to trigger

- You have data but the path from raw material to theory is opaque
- Qualitative: your quotes are decorative, not evidentiary; the coding is undocumented
- Process: you have events but no visible analytic structure turning them into a model
- Quantitative: main results exist but robustness and alternative explanations are thin
- A reviewer asks "how did you get from your data to these constructs?"

## OS expects readers to *see* how data became theory

OS's interpretive, European tradition makes **analytic transparency** a first-class criterion — qualitative rigor is judged on its own terms, not against a quantitative yardstick. The reader must be able to *audit the inference* from raw data to theoretical claim. Make the analytic ladder visible.

## Branch A — Qualitative analysis (the data-to-theory ladder)

- **Transparent coding.** Show first-order codes (informant terms), second-order themes (researcher constructs), and aggregate dimensions — the **Gioia data structure** — or an equivalent (Eisenhardt cross-case tables, Langley process bracketing). State who coded, how disagreements were resolved, and how iteration with theory proceeded.
- **Data-to-theory table.** A table linking representative raw evidence → codes → constructs, so the inference is auditable (build it with `orgstud-tables-figures`).
- **Power quotes vs. proof quotes.** A few vivid "power quotes" in the body carry the argument; corroborating "proof quotes" sit in tables/appendix. Quotes must *carry* the claim, not illustrate a conclusion reached elsewhere.
- **Evidence for each construct.** Every construct backed by patterned evidence across informants/cases, with prevalence where appropriate.
- **Negative cases.** Report disconfirming instances and how they refined the theory — central to trustworthiness at OS.
- **Process display.** For process theory, show the temporal/event structure (timeline, phase model, visual mapping); make the transitions between phases analytically explicit, not just narrated.

## Branch B — Process analysis (when the contribution is a process model)

- Choose a **process strategy** explicitly: narrative, temporal bracketing, visual mapping, grounded theory, or alternate templates (Langley). Say why it fits.
- Identify **events, sequences, and turning points**; show what triggers each transition and what each phase accomplishes that the prior could not.
- Distinguish **real-time** from **retrospective** data and address the recall/hindsight risks of each.
- The output is a **process model figure** plus the analytic account that earns it.

## Branch C — Quantitative analysis

- **Main models** match the design (FE/RE, event-history, multilevel, network); standard errors clustered at the right level.
- **Robustness that targets the theory's threats** — alternative measures, samples, specifications, endogeneity checks, modern staggered-DiD diagnostics if relevant — not a wall of tables that never address the real threat.
- **Mechanism evidence.** Don't stop at the reduced-form relationship; probe *why* (mediation/moderation or supplementary tests).
- **Effect interpretation in organizational terms** — magnitudes, not just significance.

## Either branch — the "so what" of the evidence

- Tie every analytic result back to the mechanism and the theoretical puzzle.
- Distinguish what the data *can* and *cannot* establish — overclaiming is a fast OS rejection.
- Prepare exhibits jointly with `orgstud-tables-figures`.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Organization Studies is largely qualitative/theoretical; use the chain below only for its quantitative-empirical papers, and say so when a study is interpretive.

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
- [ ] Qual: a data-to-theory / evidence table built; quotes carry (not decorate) claims
- [ ] Qual: negative cases reported and used to refine the theory
- [ ] Process: process strategy named; turning points and transitions made explicit
- [ ] Quant: SEs clustered appropriately; robustness targets the theory's threats; magnitudes interpreted
- [ ] Mechanism is probed, not just the headline relationship
- [ ] Claims are matched to what the evidence can actually support

## Anti-patterns

- "Anecdotal" qualitative work: cherry-picked quotes with no coding transparency
- Quotes that illustrate a pre-set conclusion rather than generating/supporting it
- A process "model" that is really a narrative with no analytic structure or transition logic
- Robustness theater: many tables that never address the real identification threat
- Reporting significance with no interpretation of organizational magnitude
- Overclaiming causality or generalizability beyond what the design supports

## Output format

```text
【Branch】qualitative / process / quantitative
【Data-to-theory link】data structure / process strategy / mechanism tests done
【Key evidence】power quotes, the process model, or main estimates
【Trustworthiness/robustness】checks completed + gaps (negative cases, clustering, alt explanations)
【What evidence cannot show】explicit limits
【Next skill】orgstud-contribution-framing
```
