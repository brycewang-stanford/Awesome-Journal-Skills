---
name: jme-replication-and-data-policy
description: Use when assembling the supplementary-materials / replication deposit for a Journal of Monetary Economics (JME) manuscript — depositing data, code (Dynare/MATLAB/Stata/R), and appendices on ScienceDirect / Mendeley Data per JME's supplemental-materials policy, plus the Elsevier generative-AI declaration.
---

# Replication & Data Policy (jme-replication-and-data-policy)

## When to trigger

- The paper is empirical/quantitative and you must prepare a deposit
- An editor has asked for supplemental materials as a condition of publication
- You want to pre-empt referee replication concerns
- You need to know exactly what JME's data policy does and does not require

## What JME's policy actually is

JME maintains a **supplementary-materials / replication policy** rather than a one-size mandatory verification gate. Precisely:

- An **editor may require provision of supplemental materials — proofs, data sets, and computational programs — as a condition of publication.**
- Authors are **strongly advised to deposit appendices, computer programs, and data files on ScienceDirect** (and **Mendeley Data** is supported) to **enhance replication of and citation to the research.**
- Authors must include the **declaration of any use of generative AI** in manuscript preparation, per Elsevier policy.

Note what is **待核实**: a separately *enforced*, AEA/Econometrica-style **mandatory pre-publication data-and-code-availability verification** workflow could **not** be confirmed from an official JME page. The confirmed expectation is a **strong deposit recommendation plus editor discretion** to require materials. Treat any claim of a formal verified-reproducibility check as unverified, and build the package as if it will be required — because the editor can require it.

## What to deposit

- **Data**: raw and constructed data sets (or, for proprietary/licensed series, the construction code plus access instructions).
- **Code**: estimation and model code — **Dynare `.mod` files**, MATLAB/Julia DSGE solvers, Stata/R scripts for VAR/LP — with recorded software and package versions.
- **A master script** (`run_all`) that regenerates every table, figure, and IRF from raw inputs.
- **Appendices**: the online supplementary appendix (exempt from the 40-page cap) and a README documenting steps, seeds, and runtime.

## Checklist

- [ ] Data and/or construction code deposited (proprietary series handled with access notes)
- [ ] Estimation/model code included (Dynare/MATLAB/Julia/Stata/R) with versions pinned
- [ ] `run_all` master script reproduces all exhibits, including IRFs and FEVDs
- [ ] Seeds for MCMC / bootstrap / simulation set and reported
- [ ] README documents inputs, steps, runtime, and software versions
- [ ] Materials staged for **ScienceDirect / Mendeley Data** deposit
- [ ] **Generative-AI declaration** included per Elsevier policy

## Anti-patterns

- Assuming no deposit is needed because there is no AEA-style mandatory verifier (the editor can still require it)
- Submitting final-revised data only, with no code to reconstruct real-time series
- A Dynare/MATLAB package that does not run end-to-end on a clean machine
- Omitting the generative-AI declaration


## Reproducibility pass for Journal of Monetary Economics

Use this as a second-pass capability check. First lock the main macro object, the identifying variation, and the policy-relevant counterfactual; then test whether the manuscript addresses macro and monetary economists who expect the shock, mechanism, and policy margin to be visible early.

- **Primary move:** Name data, code, environment, disclosure limits, and archive/deposit route; unresolved proprietary or ethics barriers must be explicit.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against JIE for open-economy trade/finance emphasis, RED for dynamic macro theory, AEJ Macro for broader field positioning; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Deposit target】ScienceDirect / Mendeley Data
【Data】raw + constructed (or access notes for proprietary)? Y/N
【Code】Dynare/MATLAB/Julia/Stata/R, versions pinned? Y/N
【run_all】regenerates all exhibits incl. IRFs/FEVDs? Y/N
【Seeds + README】present? Y/N
【AI declaration】present? Y/N
【Next step】jme-review-process
```
