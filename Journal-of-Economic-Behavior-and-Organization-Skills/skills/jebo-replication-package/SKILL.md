---
name: jebo-replication-package
description: Use when assembling the data, code, and experimental-materials deposit for a Journal of Economic Behavior & Organization (JEBO) manuscript — z-Tree/oTree code, instructions, raw and analysis data, and an Elsevier Research Data / Mendeley Data statement. Builds a reproducible package; it does not run the analysis.
---

# Replication & Materials Package (jebo-replication-package)

## When to trigger

- The analysis is settled and you must assemble what others need to reproduce it
- An experiment is done but the **instructions and z-Tree/oTree code** are not yet packaged
- A referee or editor asks where the data and code are
- You are writing the Elsevier "data availability" / Research Data statement
- An agent-based model's runnable code and seeds are not yet organized for sharing

## JEBO's reproducibility posture

JEBO follows the **Elsevier Research Data** policy: data and code sharing is **strongly encouraged** (via Mendeley Data or a linked repository) but **not currently a hard pre-acceptance gate** the way the AEA Data Editor or the Econometric Society's pre-acceptance check are (检索于 2026-06；以官网为准). In practice, for an experimental journal, referees increasingly *expect* the full materials, and a credible deposit strengthens acceptance. Treat the package as part of the contribution, not an afterthought.

The distinctive JEBO requirement is **experimental reproducibility**: a reader must be able to *re-run your experiment*, not just your regressions. That means the instructions, the screen-by-screen protocol, and the experiment software are first-class deposit items.

## What the package must contain

| Item | Detail JEBO referees look for |
|------|-------------------------------|
| Experiment instructions | full participant-facing text (translated to English if run in another language), including comprehension questions |
| Experiment software | z-Tree `.ztt` / oTree app code, or the platform code, runnable with setup notes |
| Screenshots / protocol | session protocol, screen flow, randomization procedure, payment scheme |
| Raw data | subject-level raw output (anonymized), with a codebook |
| Analysis code | scripts that go from raw data to every table/figure, with a master `run` file |
| Software environment | versions (Stata/R/Python, z-Tree/oTree), packages, seeds for any simulation |
| README | one-command (or clearly-ordered) reproduction path; maps each script to each exhibit |
| Pre-registration link | registry URL + a note on deviations, if pre-registered |
| Ethics / consent | IRB/ethics approval reference; consent procedure |

For **agent-based / simulation** papers, the deposit is the model code, parameter files, seeds, and the sweep scripts that regenerate the reported figures.

## Privacy and anonymization

Strip direct identifiers from raw subject data; for field data, follow consent and data-protection constraints and document any access restrictions. State clearly if data cannot be shared and why (Elsevier allows a justified restricted-access statement).

## The data-availability statement

Write the Elsevier "Data availability" statement to match reality: a Mendeley Data DOI / repository link, or a justified statement of restriction. Vague statements ("data available on request") are weak and increasingly disfavored; deposit where possible.

## Checklist

- [ ] Experiment instructions (English) + comprehension questions included
- [ ] z-Tree/oTree or platform code included and runnable, with setup notes
- [ ] Session protocol, screen flow, randomization, and payment scheme documented
- [ ] Raw subject-level data (anonymized) + codebook
- [ ] Analysis scripts reproduce every table/figure from raw data via a master file
- [ ] Software versions, packages, and seeds recorded
- [ ] README maps each script to each exhibit; reproduction path is explicit
- [ ] Pre-registration link + deviations noted (if applicable); IRB/consent referenced
- [ ] Data-availability statement points to a real deposit (Mendeley Data) or a justified restriction

## Anti-patterns

- Sharing analysis code but not the experiment software/instructions (cannot re-run the experiment)
- "Data available on request" with no deposit
- Raw data with direct identifiers left in
- A README that lists files but never gives the reproduction order
- Simulation results with no seeds or sweep scripts
- Claiming pre-registration without linking the registry or disclosing deviations

## Output format

```text
【Deposit location】Mendeley Data DOI / repository link / justified restriction
【Experiment materials】instructions + z-Tree/oTree code + protocol [Y/N]
【Data】raw (anonymized) + codebook [Y/N]
【Code】master run file → every exhibit; versions + seeds recorded [Y/N]
【README】explicit reproduction path mapping script→exhibit [Y/N]
【Pre-reg + ethics】registry link + deviations; IRB/consent [Y/N / n.a.]
【Next step】jebo-referee-strategy
```
