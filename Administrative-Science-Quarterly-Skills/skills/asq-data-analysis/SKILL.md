---
name: asq-data-analysis
description: Use when executing and reporting the analysis for an Administrative Science Quarterly (ASQ) manuscript — qualitative coding and data-to-theory construction, or quantitative estimation and robustness. Makes the evidence-to-theory link transparent; it does not design the study (see asq-methods).
---

# Data Analysis & Evidence (asq-data-analysis)

## When to trigger

- You have data but the path from data to theory is opaque
- Qualitative: your quotes are decorative, not evidentiary; coding is undocumented
- Quantitative: main results exist but robustness/alternative explanations are thin
- Reviewers ask "how did you get from your data to these constructs?"

## Branch A — Qualitative analysis (the data-to-theory link)

ASQ expects readers to *see how raw data became theory* — its guidelines stress that helping readers understand *how the research was performed* and ensuring the *trustworthiness* of published work are explicit aims (verify at journals.sagepub.com/author-instructions/asq). Qualitative rigor is judged on its own terms here, not held to a quantitative yardstick. Make the analytic ladder visible.

- **Transparent coding.** Describe first-order codes (informant terms), second-order themes (researcher constructs), and aggregate dimensions — the Gioia-style data structure — or an equivalent (Eisenhardt cross-case, Langley process bracketing). State who coded, how disagreements were resolved, and how iteration proceeded.
- **Data-to-theory table.** Provide a table linking representative raw evidence → codes → constructs, so the inference is auditable (see `asq-tables-figures`).
- **Power quotes vs. proof quotes.** Use a few vivid "power quotes" in the body; place corroborating "proof quotes" in tables/appendix. Quotes must *carry* the claim, not illustrate it after the fact.
- **Evidence for each construct.** Every theoretical construct should be backed by patterned evidence across informants/cases, with counts or prevalence where appropriate.
- **Negative cases.** Report disconfirming instances and how they refined the theory.
- **Process display.** For process theory, show the temporal/event structure (timeline, phase model, visual mapping) — as Barley (1986, ASQ) did in tracing how CT scanners restructured radiology departments over time.

## Branch B — Quantitative analysis

- **Main models** match the design (FE/RE, event-history, multilevel, network models); report clearly with appropriate standard errors (clustering at the right level).
- **Robustness** that targets the *theory's* threats: alternative measures, alternative samples, alternative specifications, endogeneity checks, and modern staggered-DiD diagnostics if relevant.
- **Mechanism evidence.** Don't stop at the reduced-form relationship — provide mediation/moderation or supplementary tests that probe *why*.
- **Effect interpretation.** Report and interpret *magnitudes* in organizational terms, not just significance stars.
- **Alternative explanations** are tested, not waved away.

## Either branch — the "so what" of the evidence

- Tie every analytic result back to the mechanism and the surprise.
- Distinguish what the data *can* and *cannot* establish — overclaiming is a fast path to rejection.
- Prepare the exhibits jointly with `asq-tables-figures`.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). ASQ wants a clean causal or well-identified observational design behind an organizational-theory contribution; reduced-form estimation fits the chain below, interpretive work does not.

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

- [ ] Qual: data structure (first-order → second-order → dimensions) is documented
- [ ] Qual: a data-to-theory / evidence table is built; quotes carry (not decorate) claims
- [ ] Qual: negative cases reported and used to refine theory
- [ ] Quant: standard errors clustered at the appropriate level
- [ ] Quant: robustness targets the theory's threats; effect *magnitudes* interpreted
- [ ] Mechanism is probed, not just the headline relationship
- [ ] Claims are matched to what the evidence can actually support

## Anti-patterns

- "Anecdotal" qualitative work: a few cherry-picked quotes with no coding transparency
- Quotes that illustrate a pre-set conclusion rather than generating/supporting it
- Quantitative robustness theater: many tables that never address the real threat
- Reporting significance with no interpretation of organizational magnitude
- Stopping at the X→Y relationship without evidence on the mechanism
- Overclaiming causality or generalizability beyond the design

## Output format

```
【Branch】qualitative / quantitative
【Data-to-theory link】data structure / mechanism tests done
【Key evidence】power quotes or main estimates
【Robustness/trustworthiness】checks completed + gaps
【What evidence cannot show】explicit limits
【Next step】asq-contribution-framing
```
