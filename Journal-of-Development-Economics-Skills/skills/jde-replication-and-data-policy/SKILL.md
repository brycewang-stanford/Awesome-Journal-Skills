---
name: jde-replication-and-data-policy
description: Use when assembling the data and code deposit for a Journal of Development Economics (JDE) submission or accepted paper — JDE's mandatory replication policy, Mendeley Data hosting, and the fact that data/code can be requested at the review stage. Builds the package; it does not run the analysis.
---

# Replication & Data Policy (jde-replication-and-data-policy)

## When to trigger

- A paper is heading toward submission or acceptance and the replication package is not built
- You are unsure what JDE requires and when
- Some data are proprietary/restricted (government microdata, partner-NGO data) and you need a compliant path
- You want to pre-empt a referee asking for data and code during review

## JDE's policy (what it actually requires)

JDE operates a **mandatory replication policy**. The journal will, in general, publish a paper **only if the data used are clearly and precisely documented and readily available to any researcher for replication**. Authors of accepted papers containing **empirical, simulation, or experimental** work must provide, **prior to publication**, the data, programs, and other computational details sufficient to permit replication; these are posted on the JDE website **alongside the article**. JDE partners with **Mendeley Data** to host research data, displayed next to the article on ScienceDirect.

Crucially, this is not only an acceptance-stage formality: **editors or referees may request the data, programs, and computational details at the review stage**. So the package must be submission-ready, not assembled after acceptance.

## Build the package as you go

- **One master script** (`run_all`) that regenerates every table and figure from raw or constructed data, in order.
- **A README** documenting data provenance, every construction/cleaning step, software and package versions, run time, and which script produces which exhibit.
- **Pinned environment**: record Stata `ssc`/`net` versions, `renv.lock`, or `requirements.txt`; set and report all random **seeds** (bootstrap, randomization inference, simulation).
- **Self-contained**: relative paths, no machine-specific dependencies, no orphaned hand edits to outputs.

## Restricted or proprietary data

JDE's standard is that data be available for replication, but development work often uses **restricted government surveys or partner-collected data** that cannot be redistributed. In that case:

- Provide **all programs** and a precise, documented **access path** so another researcher could obtain the data and rerun the code.
- Disclose the restriction clearly (cover letter and README) rather than silently omitting data.
- Where possible, deposit a de-identified extract or simulated data that exercises the code.

## Pre-results review note

For **pre-results-reviewed** papers, the pre-specified research plan (hypotheses, statistical analysis plan, power analysis) is included in the **supplementary online appendix**, and the published article carries a footnote noting the pre-results submission — the analysis plan is itself part of the replication record.

## Anti-patterns

- Treating replication as an acceptance-stage chore — JDE can request it during review
- A code dump with no README and no master script
- Hand-edited tables that the code does not reproduce
- Claiming proprietary data as a reason to share neither programs nor an access path

## Output format

```
【Master script regenerates all exhibits?】[Y/N]
【README】provenance + steps + versions + seeds? [Y/N]
【Environment pinned】[Stata/R/Python versions]
【Data status】public / restricted (+ access path)
【Mendeley Data deposit prepared?】[Y/N]
【Pre-results plan in appendix?】[Y/N/NA]
【Next step】jde-review-process
```
