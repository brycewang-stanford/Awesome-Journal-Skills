---
name: humrel-methods
description: Use when choosing and justifying the research design for a Human Relations (HR) manuscript — qualitative/ethnographic, critical, quantitative, or mixed — and setting the rigor bar. Designs the study; it does not run the analysis (see humrel-data-analysis).
---

# Methods & Research Design (humrel-methods)

## When to trigger

- You are choosing among a qualitative/ethnographic, critical, quantitative, or mixed-methods design
- The design is chosen but its *rigor and transparency* are not yet defensible
- A qualitative study lacks a sampling logic or trustworthiness safeguards
- A quantitative study lacks construct validity or theorizes only the coefficient
- A mixed-methods study cannot say *why* both strands and what each adds

## Principle: method follows the theoretical question — and HR privileges none

HR treats qualitative, critical, quantitative, and mixed-methods work as **equally first-class**, in the Tavistock human-relations tradition. There is no house preference for an estimator or a paradigm; what is non-negotiable is that the design fits the social-theoretical question (from `humrel-theory-development`) and is executed with rigor, transparency, and reflexivity. A sophisticated method cannot rescue a thin theory, and a single immersive ethnography can carry an HR paper if the insight is deep and the craft is high. Note also the **double-anonymous review**: write methods so they establish credibility without revealing the authors' institution, field site identity, or grant.

## Branch A — Qualitative / ethnographic design

For *how/why* process, meaning, identity, and contested dynamics at work.

- **Theoretical (not convenience) sampling.** Sites/cases/informants chosen to illuminate the mechanism; state the logic (polar types, extreme/critical case, longitudinal, theoretical replication).
- **Access and immersion.** Specify duration, depth, and your role (participant vs. non-participant); for ethnography, time in the field; for historical work, the archive.
- **Triangulated data.** Interviews (count, who, when, guide), observation, documents — and how they corroborate.
- **Trustworthiness.** Credibility, transferability, dependability, confirmability: member checks, prolonged engagement, audit trail, negative-case analysis.
- **Reflexivity.** State your standpoint and how it shaped access, interpretation, and the relations you studied — HR expects this, not as confession but as method.

## Branch B — Critical design

For research interrogating power, ideology, discourse, and taken-for-granted arrangements.

- Make the **critical-theoretical lens** explicit (labour process, Foucauldian, feminist, postcolonial, CDA) and tie analytic choices to it.
- Treat reflexivity and positionality as central, not optional.
- Ensure the critique is **generative**: the design must surface a constructive theoretical claim, not only an unmasking.

## Branch C — Quantitative design

For *whether/how much/under what conditions* across many cases.

- **Sample and unit of analysis** justified relative to the theory (individuals nested in teams/organizations; dyads; events).
- **Construct validity.** Operationalizations defended; multi-item measures with reliability; address common-method bias if same-source/cross-sectional.
- **Multilevel structure.** If theory is cross-level, use HLM/mixed models and justify aggregation.
- **Identification in service of theory.** Where causal claims are made, state the threat and the strategy (panel FE, longitudinal lags, quasi-experiment) — but identification is a means to a *theoretical* end at HR, not the contribution itself.

## Branch D — Mixed methods

- State the **integration logic**: sequential, concurrent, or nested, and *what each strand adds* that the other cannot. Avoid bolting a few interviews onto a survey for decoration.

## Either branch

- The design must let you *see the mechanism*, not just endpoints.
- Pre-empt obvious alternative explanations at the design stage.
- Plan the data-to-theory link now (feeds `humrel-data-analysis` and `humrel-tables-figures`).

## Execution bridge (StatsPAI / Stata MCP)

For the **empirical / causal lane**, estimate and audit rather than only specify. Full
map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Human Relations blends critical/qualitative and quantitative work; apply the chain below to its survey / experimental quantitative papers.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result` to
  enumerate the checks the design owes.
- **Panel / staggered DiD:** `callaway_santanna` / `sun_abraham` + `bacon_decomposition`
  + `honest_did_from_result`. **IV:** `effective_f_test` + `anderson_rubin_ci`. **RDD:**
  `rdrobust` + `mccrary_test`.
- **Experiments:** randomization-based inference and `romano_wolf` for the many-outcome
  family-wise correction reviewers expect.

Match the toolchain to the **reviewer pool**, and report the effect size the venue
wants. A run end-to-end (synthetic data, real returns) is in the
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Design matches the theoretical form (process → qual/critical; variance → quant)
- [ ] Qual: theoretical sampling stated; access/immersion specified; trustworthiness named
- [ ] Critical: lens explicit; reflexivity central; critique is generative
- [ ] Quant: construct validity and (if needed) multilevel structure addressed
- [ ] Mixed: integration logic and the added value of each strand stated
- [ ] Obvious alternatives are designed against, not just discussed later
- [ ] Methods text is anonymized (no institution/site/grant tells)

## Anti-patterns

- Convenience sampling dressed up as theoretical sampling
- Qualitative work with no transparency about coding, sources, or fieldwork depth
- A fancy estimator chosen to signal rigor when the question doesn't need it
- Critical work that is reflexive in tone but methodologically opaque
- "Mixed methods" that is a survey with ornamental quotes
- Methods that reveal author/site identity in a double-anonymous submission

## Output format

```text
【Journal】Human Relations
【Skill】humrel-methods
【Design】qualitative / critical / quantitative / mixed (type)
【Why it fits】link to the social-theoretical question
【Sampling/identification】logic + key threat addressed
【Rigor safeguards】trustworthiness / construct validity / integration logic
【Anonymization】no site/institution/grant tells (yes/no)
【Next skill】humrel-data-analysis
```
