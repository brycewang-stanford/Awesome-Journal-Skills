---
name: jhe-replication-package
description: Use when assembling the data, code, and access documentation for a Journal of Health Economics (JHE) manuscript — where much health data is restricted (claims, administrative, EHR) and the journal's policy encourages rather than mandates deposit. Packages reproducibility and a credible restricted-data access path; it does not run the analysis.
---

# Replication Package (jhe-replication-package)

## When to trigger

- The analysis uses restricted health data (Medicare/Medicaid claims, hospital discharge, EHR, registry, survey-linked admin) and you must document an access path
- A Data Availability Statement and code package need assembling for submission
- A referee or editor asks whether the results are reproducible despite data being non-public
- You are deciding what can be deposited publicly versus what stays behind a Data Use Agreement / IRB

## What JHE actually requires (and what it does not)

JHE follows the Elsevier **Research Data** policy: authors are **encouraged** to deposit data in a repository and to **state data availability at submission** — this is *not* the AEA's mandatory pre-publication openICPSR build-and-verify gate (检索于 2026-06；以官网为准). That softer baseline is precisely why credibility here rests on **how well you document the path to reproduction**, not on a public dataset that often cannot exist. The health-economics reality is that most rich data is restricted by privacy law (HIPAA), Data Use Agreements, and IRB. The professional standard JHE referees increasingly expect: **code is shareable even when data is not**, the Data Availability Statement is honest and specific, and another researcher could in principle obtain the same data and re-run the code.

## Build the package around the data's access tier

| Data tier | What to deposit | What to document |
|-----------|-----------------|------------------|
| Public (NHANES, BRFSS, MEPS public-use) | data + code + README; aim for a one-command rebuild | exact extract/version, vintage, derivation code |
| Restricted but obtainable (CMS VRDC, state HCUP/SID, claims via DUA) | **code + full DAS**; synthetic or simulated extract if licensing allows | the application process, DUA terms, cost, approximate wait, contact |
| IRB / enclave-only (EHR, linked admin, secure enclave) | code + access protocol; results-only outputs | IRB approval, enclave rules, what can leave the enclave |

## Documentation that earns trust

1. **Data Availability Statement, honest and specific.** Name the data, the holder, the access mechanism, and the realistic path/cost/wait — not "available on request" with no detail.
2. **Share the code regardless of data access.** Cleaning, construction, and analysis scripts in run order, with a master script and a manifest mapping each exhibit to the code that makes it.
3. **Pin the environment.** Software versions, packages, seeds; for skewed-spending estimators (two-part, GLM) state the exact implementation so results are reproducible.
4. **Separate construction from analysis** so a reader with the same DUA can rebuild the analysis sample.
5. **Respect privacy in the package itself.** No re-identifiable cells, small-cell suppression honored, no PHI in logs or example outputs.
6. **Map every table and figure to its script** so the reproduction is auditable exhibit by exhibit.

## Checklist

- [ ] Data Availability Statement names the data, holder, access mechanism, and realistic path/cost/wait
- [ ] Code shared even though data is restricted; master script + exhibit-to-code manifest present
- [ ] Environment pinned (versions, packages, seeds); skew/zero estimators reproducible
- [ ] Construction code separated from analysis code; sample-build documented
- [ ] Privacy honored: small-cell suppression, no PHI in code/logs/outputs
- [ ] Public-data portions are genuinely one-command reproducible
- [ ] DUA / IRB constraints stated so a referee understands what cannot be posted

## Why this matters more at JHE than at the AEA journals

Because JHE only *encourages* deposit rather than running a mandatory pre-publication build-and-verify, the burden of credibility shifts onto the author. There is no Data Editor who will catch a broken pipeline before publication, which cuts both ways: less friction at acceptance, but a higher reputational cost if a reader later cannot reproduce your work from the materials you provided. Treat the package as your own quality control — a colleague should be able to run the public portions today and, with the documented access path, rebuild the restricted portions later. That standard, not the letter of the policy, is what protects the paper.

## Anti-patterns

- "Data available on request" with no holder, mechanism, cost, or wait time
- Refusing to share code because the data is restricted (code is almost always shareable)
- A package that silently leaks small cells or PHI into logs or example outputs
- Unpinned environment so the skewed-spending estimator cannot be reproduced
- No mapping from exhibits to scripts, so reproduction is unauditable
- Treating the encouraged Elsevier policy as "nothing required" and shipping no DAS

## Common restricted health-data sources and their access reality

Name the holder and mechanism precisely; "available on request" is not a path. Typical JHE data and how to describe access:

- **CMS Medicare/Medicaid claims (VRDC / ResDAC)** — application + DUA, fees, multi-month wait, virtual enclave with output review.
- **HCUP / state inpatient & ED databases (SID/SEDD)** — purchase + DUA per state; describe the state and vintage.
- **EHR / hospital-system data** — institutional DUA + IRB; often enclave-only; state what can leave.
- **Linked administrative / register data (e.g., Scandinavian registers)** — national-statistics-agency application; remote-access servers; long lead times.
- **Public-use surveys (NHANES, MEPS, BRFSS, NHIS)** — public; here a one-command rebuild from the cited extract *is* expected, so do it.

The DAS should let a reader estimate the cost, time, and eligibility to obtain the same data — that is what substitutes for a public deposit at JHE.

## Worked vignette (illustrative)

A paper uses 100% Medicare claims through the CMS VRDC enclave; the data cannot be deposited. A weak package says "data available from CMS." The JHE-credible package: a DAS naming the VRDC, the DUA application path, the approximate fee and multi-month wait, and the enclave's output-review rules; the full cleaning/construction/analysis code with a master script and a manifest mapping Tables 1–5 and Figures 1–3 to scripts; a pinned software environment with seeds; and a small simulated extract (structure only, no real records) so a reader can dry-run the code before obtaining access. Reproduction is now a documented, auditable path despite zero public data.

## Output format

```text
【Journal】Journal of Health Economics
【Skill】jhe-replication-package
【Data tier】public / restricted-obtainable / IRB-enclave
【DAS】names data, holder, mechanism, cost/wait? [Y/N]
【Code】shared + master script + exhibit-to-code manifest? [Y/N]
【Environment】versions/packages/seeds pinned? [Y/N]
【Privacy】small-cell suppression, no PHI in package? [Y/N]
【Policy note】Elsevier "encouraged" deposit (检索于 2026-06；以官网为准)
【Next skill】jhe-referee-strategy
```

## Handoff boundary

This skill assembles and documents the data/code package and the Data Availability Statement; it does not run or re-run the analysis. Build it once the exhibits are stable (after `jhe-tables-figures` / `jhe-robustness`) so the exhibit-to-code manifest does not drift. When the package is honest and auditable, hand off to `jhe-referee-strategy` to pre-empt the reproducibility objection before submission.
