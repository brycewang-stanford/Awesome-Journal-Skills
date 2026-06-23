---
name: pnasnexus-statistics
description: Use to enforce PNAS Nexus's statistics and reproducibility reporting — n and replication, test choice and assumptions, effect sizes with uncertainty, multiple-comparison control, randomization/blinding, sample-size justification, and reproducible code. Also covers whether a Registered Report (Stage 1/2) is the right route for confirmatory work.
---

# Statistics & Reproducibility (pnasnexus-statistics)

## When to trigger

- Results report P values but not effect sizes or n.
- "Three independent experiments" is claimed but replication is unclear.
- Multiple comparisons are run with no correction.
- A reviewer is likely to ask "were analyses pre-specified?" and there's no answer.
- The analysis is not reproducible from the deposited code (`pnasnexus-data`).
- The study is confirmatory and you want reviews **before** collecting data — consider a Registered Report.

## The reporting backbone (every quantitative claim)

Each claim needs: **effect size + uncertainty + n + test + what n means.**

- [ ] **n** stated, with the unit of replication (biological vs technical replicates; cells vs animals vs subjects vs experiments).
- [ ] **Effect size** with **95% CI** (preferred) or SD/SEM clearly labeled — not P alone.
- [ ] **Exact P values** (e.g., P = 0.013), not "P < 0.05", unless extremely small.
- [ ] **Test named and justified** (assumptions checked: normality, variance homogeneity, independence).
- [ ] **Multiple comparisons** corrected (Bonferroni/Holm/FDR) when many tests are run.

## Replication and design

- Distinguish **biological replication** (independent samples) from **technical replication** (re-measurement). The former is what counts.
- State **how the sample size was chosen** (power analysis or explicit rationale), not post-hoc.
- Report **randomization** of subjects/treatments and **blinding** of measurement/analysis where applicable, or state why not.
- Report **inclusion/exclusion criteria** and any excluded data, with reasons, decided in advance.

## Registered Reports: a PNAS Nexus route for confirmatory work

PNAS Nexus offers **Registered Reports**, where the **study design and analysis plan are peer-reviewed before data are collected** (Stage 1, ≤3 pp), and — on **in-principle acceptance** — the completed study (Stage 2) is published largely regardless of whether the hypothesis was supported, provided the pre-registered plan was followed.

Consider a Registered Report when:

- The study is **confirmatory** / hypothesis-testing and you want to guard against p-hacking and publication bias.
- A null or mixed result would still be informative to the field.
- The design benefits from reviewer input **before** the expense of data collection.

In the Stage 2 manuscript, **separate pre-registered (confirmatory) analyses from post-hoc (exploratory) ones** explicitly, and report deviations from the Stage 1 plan.

## Discipline-specific notes across PNAS Nexus divisions

PNAS Nexus spans **biological/health/medical, physical sciences & engineering, and social & political sciences**, so match the rigor conventions of your division:

- **Biological / health / medical:** replication unit, ARRIVE-style animal reporting, antibody/reagent validation, clinical-study reporting standards (CONSORT/STROBE) where applicable.
- **Social / political / behavioral:** pre-registration is increasingly expected; report power, sampling frame, and deviations from the plan.
- **Physical / engineering / computational:** report uncertainties, error propagation, and numerical reproducibility (seeds, solver settings).

## Avoid the classic reviewer kills

- **Pseudoreplication**: treating technical replicates / cells from one animal as independent n.
- **HARKing / p-hacking**: presenting exploratory findings as confirmatory. Label exploratory work as such (or run a Registered Report).
- **"Representative" images** with no quantification across replicates.
- **Bar chart + SEM** masking a tiny, variable n.
- Comparing two effects by their **significance** ("significant here, not there") instead of testing the **difference**.

## Reproducibility package

- Analysis code in a public repository, archived for a DOI (see `pnasnexus-data`), with a README and environment/versions.
- Deterministic where possible; report random seeds for simulations/ML.
- Because PNAS Nexus **mandates** that code and data be available in a public repository upon publication, build the reproducibility package as you go — it is not optional here.

## Output format

```
【Per-claim backbone】 effect+CI / n / unit-of-n / test / assumptions → list gaps
【Replication】 biological vs technical clear? yes/no
【Sample-size rationale】 power/justification present? yes/no
【Randomization & blinding】 reported / N/A-justified / missing
【Multiplicity】 corrected? method
【Registered Report?】 confirmatory work → Stage 1/2 considered? yes/no/N-A
【Division-specific rigor】 (Bio-Health-Medical / Physical-Engineering / Social-Political) conventions met? yes/no
【Reproducibility】 code + versions + seeds in a public repo (mandatory)? yes/no
【Next】 pnasnexus-data
```

## Anti-patterns

- **Do not** report P without effect size and n.
- **Do not** count technical replicates as independent observations.
- **Do not** infer "no effect" from a non-significant test on an underpowered sample.
- **Do not** present post-hoc subgroup findings as if pre-specified — use a Registered Report for true confirmatory tests.
- **Do not** defer the reproducibility package — public data/code is mandatory at PNAS Nexus.
