---
name: jcr-methods
description: Use when choosing or stress-testing the research design for a Journal of Consumer Research (JCR) manuscript — multi-study behavioral experiments, interpretive Consumer Culture Theory (CCT) fieldwork, mixed designs, or a Registered Report — so the evidence matches the conceptual claim. Designs the studies; it does not analyze them (jcr-data-analysis).
---

# Methods & Design (jcr-methods)

## When to trigger

- You have a mechanism but are unsure how to test it
- Deciding between a behavioral-experiments paper and a CCT fieldwork paper
- A reviewer asks whether your design can actually support the process claim
- You are weighing a Registered Report for a confirmatory question

## JCR is methodologically pluralistic by mandate

JCR states **no single preferred method**; the bar is a clear conceptual contribution supported by *appropriate* empirical evidence. In practice two flagship traditions coexist under one masthead, and you should commit to one design logic (or a principled mix):

- **Theory-driven behavioral experimentation** (the dominant tradition): multiple lab and online experiments that isolate a **psychological process** and its boundary conditions.
- **Interpretive / Consumer Culture Theory (CCT)**: ethnography, depth interviews, phenomenology, or netnography that theorizes the sociocultural meanings of consumption.

The journal also publishes quantitative/modeling and methodological work. Choose the design the **conceptual claim** demands, not the one you find convenient.

## Designing the multi-study experimental package

- **Process evidence:** plan studies that establish the effect, then **mediation** (measured or, more convincingly, **moderation-of-process** / manipulated mediator), then **boundary conditions** that the theory predicts.
- **Internal validity:** random assignment; manipulation checks and attention checks; pretested stimuli; counterbalancing; rule out demand and confounds by design.
- **Robustness across studies:** vary populations, stimuli, and operationalizations so the effect is not stimulus-bound; a convergent multi-study package is the JCR norm.
- **Power & samples:** a priori power analysis; specify and justify sample sizes and exclusion rules in advance. Overflow stimuli, full instruments, and additional replication studies belong in the **web appendix** (max 40 MB, excluded from the 60-page cap).

## Designing interpretive / CCT work

- Justify **site, informant selection, and immersion**; show the data are rich enough to support conceptual claims.
- Plan for **trustworthiness**: triangulation, prolonged engagement, member checks, and an audit trail rather than p-values.
- Theorize as you go: the design should enable moving from thick description to second-order constructs.

## Transparency is a design decision, not an afterthought

JCR's transparency regime shapes the design from the start: a **Data Collection Statement** is required for **all** submissions (Step 6), data/materials posting is **required at invited revision** unless exempt, and replication code must be provided. Build clean materials, preregistration where appropriate, and a repository plan (OSF / Harvard Dataverse / Qualitative Data Repository / ResearchBox) into the design. For confirmatory questions, consider a **Registered Report** (full review before final data collection; must be JCR-worthy regardless of outcome).

## Execution bridge (StatsPAI / Stata MCP)

For the **empirical / causal lane**, estimate and audit rather than only specify. Full
map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JCR is predominantly lab experiments; randomization-based inference and the many-outcome family-wise correction (`romano_wolf`) are the decisive tools.

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

- [ ] Design logic (experiments / CCT / mixed) matches the conceptual claim
- [ ] Experiments: effect → process → boundary mapped to specific studies
- [ ] Manipulation/attention checks, random assignment, pretested stimuli
- [ ] A priori power, sample sizes, and exclusion rules pre-specified
- [ ] CCT: site/informant justification and a trustworthiness plan
- [ ] Materials, code, and a repository plan prepared for transparency requirements

## Anti-patterns

- A single study asked to carry a process claim.
- "Mediation" inferred from a measured mediator without manipulating the process.
- Stimulus-bound effects (one scenario, one product) generalized broadly.
- CCT design with too little immersion to support conceptual claims.
- Treating data/materials posting as a post-acceptance chore.

## Output format

```
【Design logic】experiments / CCT / mixed / Registered Report
【Study chain】effect → process → boundary (or CCT framework)
【Validity safeguards】randomization / checks / pretests / trustworthiness
【Power & samples】a priori N, exclusions
【Transparency plan】repository + code + Data Collection Statement
【Web appendix】overflow stimuli / extra studies (≤40 MB)
【Next step】jcr-data-analysis
```
