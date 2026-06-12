---
name: demog-data-and-reproducibility
description: Use when preparing the data-availability statement and reproducibility materials for a Demography (PAA / Duke University Press) manuscript. Demography requires a data availability statement at acceptance with persistent identifiers and encourages reproducible, commented code; it hosts no repository, so authors deposit in a FAIR repository. Covers restricted-data exemptions. Prepares the materials; it does not waive requirements.
---

# Data & Reproducibility (demog-data-and-reproducibility)

Demography asks every **accepted** manuscript for a **data availability statement** and **encourages
reproducible code**. The journal **does not maintain its own repository** — *you* choose a FAIR
repository and provide persistent identifiers. Build the materials as you go so acceptance does not
stall.

## When to trigger

- Building the reproducibility/replication materials and the data availability statement
- A manuscript reached acceptance and you must finalize the statement and deposit
- Data cannot be fully shared (privacy, confidentiality, proprietary/provider restrictions) and you
  need the exemption language
- Choosing a repository and persistent identifier

## What Demography requires (verify current wording on the ethics/disclosures page)

1. **Data availability statement.** Accepted manuscripts must include a statement confirming **whether
   and how** the data have been shared. For publicly available data, describe the access method with
   a **persistent identifier** (DOI or accession number).
2. **Persistent identifiers + FAIR repository.** Because Demography hosts no repository, deposit data
   and materials in a **FAIR-aligned repository** (e.g., ICPSR/openICPSR, Harvard Dataverse, Zenodo,
   OSF) and cite it with a permanent link — not a personal website or generic cloud folder. Find one
   via FAIRsharing.org or re3data.org.
3. **Reproducible code (encouraged).** Provide code that regenerates the results, with **software
   versions recorded** and **informative comments** explaining each step. Treat this as expected, not
   optional, for a quantitative demographic paper.
4. **Restricted data.** Where access is limited to protect confidential or proprietary information,
   **describe the conditions limiting access** and how others may obtain the data, while still aligning
   with FAIR principles as far as possible.

## Build-as-you-go checklist

- [ ] **Data availability statement** drafted (public / restricted / on request) with persistent IDs
- [ ] Data + materials deposited in a **FAIR repository** with a DOI/accession number
- [ ] One **master script** regenerates every table, figure, life table, and decomposition
- [ ] **README** documents data provenance/vintage, construction of rates/exposure, and how to reproduce each exhibit
- [ ] **Code commented** and **software/package versions recorded** (`renv.lock` / `requirements.txt` / installs)
- [ ] **Seeds** set and reported for bootstrap, simulation, microsimulation
- [ ] Exhibit numbers in the manuscript **match** the deposited output exactly
- [ ] Restricted data: exemption note + access conditions + synthetic data where feasible

## Anti-patterns

- Treating the data statement as a last-minute formality at acceptance
- A personal URL or generic cloud link instead of a persistent identifier in a FAIR repository
- Undocumented, un-seeded, uncommented code that "works on my machine"
- Claiming data are restricted without describing the access conditions
- Calling the $1,000 editorial-management fee an "open-access" or "data" charge (it is neither)

## What a reproducibility reviewer expects at Demography

Demography, the Population Association of America flagship published open access by Duke University
Press, draws referees who routinely re-derive a denominator or re-run a Kitagawa split by hand. The
deposit must let them do so. Calibrate the package against the data class you actually used.

| Data class | Typical source | Deposit obligation |
|------------|----------------|--------------------|
| Fully public | HMD, HFD, IPUMS, WPP, published vital statistics | Extract code + constructed analytic file (where license permits) + persistent ID |
| Public-but-licensed | IPUMS, DHS, redistribution-restricted census | Extract specification + code, not raw microdata; cite the provider's persistent access path |
| Restricted/confidential | Linked administrative records, RDC-only census, linked mortality files | Code + synthetic stand-in file + exact access-conditions note |

## Referee-pushback patterns and the Demography-specific fix

- *"I cannot tell which HMD/HFD vintage produced these rates."* -> Record the release label and download
  date in the README and a code comment; vintages revise historical rates.
- *"The decomposition components in the deposit do not sum to the headline number."* -> Add an assertion
  that components reconcile to the total e0 (or TFR) change before you deposit; ship the check passing.
- *"Your bootstrap intervals are not reproducible."* -> Set and report a seed for every resampling,
  microsimulation, and graduation step; an un-seeded interval reads as un-reproducible.
- *"You say data are restricted but give no way to obtain them."* -> Name the data enclave or
  application pathway and the access conditions; a bare "restricted" reads as evasion.

## Output format

```
【Data statement】public / restricted / on request — drafted with persistent ID? [Y/N]
【Repository】FAIR repo + DOI/accession (not personal URL)? [Y/N]
【Reproducible code】master script + comments + recorded versions + seeds? [Y/N]
【Exhibits match deposit?】[Y/N]
【Restricted data?】access conditions described + synthetic data where feasible?
【Next】demog-review-process
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — FAIR repositories and reproducibility tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — Demography data-availability and reproducible-code policy
