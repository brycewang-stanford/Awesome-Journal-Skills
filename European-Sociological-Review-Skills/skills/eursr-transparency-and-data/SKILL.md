---
name: eursr-transparency-and-data
description: Use when preparing the Data Availability Statement and the replication package for a European Sociological Review (ESR) manuscript. ESR requires a Data Availability Statement for every manuscript and (for submissions from 1 January 2025) a replication package for statistical/computational work upon conditional acceptance; qualitative work is exempt. Prepares documentation; it does not over-state or under-state the policy.
---

# Transparency & Data (eursr-transparency-and-data)

ESR's transparency expectations are **stricter than a sharing norm**: a **Data Availability Statement
(DAS) is required for every manuscript**, and for **submissions received on or after 1 January 2025**,
authors using **statistical or computational methods must deposit a replication package as a condition
of publication** (assembled by acceptance, typically required at conditional acceptance). **Qualitative-
data work is exempt** from the package requirement. **Confirm the current wording and effective dates on
the live OUP/ESR page** — this skill states the policy as verified in 2026-06; treat specifics as
volatile.

## When to trigger

- Writing the **Data Availability Statement** (needed at submission)
- Assembling the **replication package** ahead of conditional acceptance
- Deciding what can be shared given confidentiality, DUA, or proprietary constraints (register data)
- A reviewer or editor asked how the analysis can be reproduced

## What the ESR policy requires (verify current wording)

- **Data Availability Statement** in every article — describing how the data can be accessed and the
  conditions for access (open, controlled/enclave, on-request, or restricted).
- **Replication package** for statistical/computational papers, due at conditional acceptance: the code,
  the constructed/analysis data (or a documented access path when redistribution is barred), and
  documentation sufficient to regenerate every reported result.
- **Exemption**: research using qualitative data (interviews, participant observation) is not required
  to submit a replication package.
- **Restricted data path**: where register/administrative data (e.g., national statistical offices,
  SOEP, EU-SILC scientific-use files) cannot be redistributed, share **all code** plus a precise access
  route (provider, file version, DUA), so a qualified researcher could reproduce the results.

## Build a package that reproduces (do this from the start)

- **One master script** regenerates every table/figure from the (constructed) data, in order.
- **Set and report seeds** for imputation, bootstrap, and MCMC; pin versions (`renv.lock`,
  `requirements.txt`, recorded `ssc`/`net` installs).
- **Archive the harmonization/recoding code** (ISCED/CASMIN, ISCO/ISEI/EGP) — it is part of the result.
- **README** documenting data sources and versions, run order, expected outputs, runtime, and any
  access restrictions.
- Deposit in a citable repository (e.g., OSF, Zenodo, GESIS) and reference it in the DAS.

## Transparency posture by data type (ESR)

| Data type | In the package | Restricted | DAS framing |
|-----------|----------------|------------|-------------|
| Public comparative survey (ESS, EVS) | data + code | none | "openly available from [archive], version X" |
| EU-SILC / SOEP scientific-use file | code + constructed-vars script | raw microdata | "available from [provider] under its access terms" |
| National register / administrative | all code + access route | raw records | "accessible via [NSO/enclave] under DUA; code provided" |
| Qualitative (exempt) | analytic documentation (optional) | identifiable transcripts | state the exemption + confidentiality basis |

## Worked micro-example (illustrative)

A comparative scarring paper uses public ESS plus a restricted national register linkage.

```
DAS: "ESS Round data are openly available from the ESS Data Archive (edition cited). The linked
  register data are accessible to qualified researchers via [national statistical office] under a data-
  use agreement; all analysis and harmonization code is provided in the replication package."
Package (for conditional acceptance): master.R + harmonization scripts + constructed analysis file for
  the ESS portion; full code for the register portion with a documented access path; seed = 2026;
  renv.lock pinned; README with run order and runtime; deposited on Zenodo with a DOI.
Statistical method → not exempt → package required.
```

The posture shares what supports the claims, documents provenance, and is explicit about what cannot be
redistributed and how to obtain it — exactly what ESR's mandate expects.

## Referee / editor pushback → ESR-specific fix

- *"Your register data can't be shared, so this isn't reproducible."* → Provide **all code** plus a
  precise access route (provider, version, DUA); the policy accommodates restricted data via an access
  path, not an exemption from code.
- *"The DAS is vague."* → Name the archive/provider, the data version/edition, and the exact access
  condition; a generic "data available on request" is weak.
- *"Numbers don't match your code."* → Re-run the master script end-to-end before depositing; mismatches
  read as a credibility failure under the mandate.

## Calibration anchors

- **A replication package is a condition of publication, not a courtesy.** For statistical/computational
  work submitted from 1 Jan 2025, plan it from day one — it is not an afterthought at acceptance.
- **Restricted data still requires shareable code.** ESR's mandate is satisfied by code + a documented
  access path, not by declaring the data private.
- **The DAS is required for everyone.** Even exempt qualitative work needs a Data Availability Statement;
  confirm the current wording and effective dates on the live page.

## Anti-patterns

- Treating the replication package as optional or leaving it to the last minute
- A vague "data available on request" DAS with no provider, version, or access condition
- Claiming a qualitative exemption for a statistical/computational paper
- Omitting the harmonization/recoding code from the package (the result is not reproducible without it)
- Depositing code whose output does not match the manuscript's tables

## Output format

```
【DAS】drafted, names archive/provider + version + access condition? [Y/N]
【Package required?】statistical/computational (yes) vs. qualitative (exempt)
【Package contents】master script + data/access path + harmonization code + seeds + README? [Y/N]
【Restricted data handled】code shared + documented access route? [Y/N]
【Policy check】current ESR DAS + replication wording/dates confirmed? [Y/N/待核实]
【Next】eursr-review-process
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — repositories (OSF / Zenodo / GESIS), reproducibility tooling
- [`../../resources/code/`](../../resources/code/) — master-script + pinned-version skeleton to base the package on
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — ESR Data Availability + replication policy and effective dates
