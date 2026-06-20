---
name: popdevr-transparency-and-data
description: Use when preparing the data-availability statement and reproducibility materials for a Population and Development Review (PDR, Wiley / Population Council) manuscript. PDR follows Wiley's data-sharing and research-integrity expectations — a data availability statement, ORCID, and reproducible, well-documented materials deposited in a FAIR repository (verify current policy). Covers restricted-data exemptions. Prepares the materials; it does not waive requirements.
---

# Transparency & Data (popdevr-transparency-and-data)

PDR sits within **Wiley's** author and research-integrity framework: a **data availability statement** is
expected, ORCID is encouraged/required for submitting authors, and authors are expected to make data and
materials available where ethics and licensing permit. PDR hosts no repository of its own — *you* choose
a **FAIR** repository and provide persistent identifiers. Build the materials as you go so revision and
acceptance do not stall. Verify current wording on the Wiley author page and the data-policy page. 待核实.

## When to trigger

- Building the reproducibility materials and the data availability statement
- A manuscript reached revision/acceptance and you must finalize the statement and deposit
- Data cannot be fully shared (privacy, confidentiality, DHS/census licensing, provider restrictions) and
  you need the exemption language
- Choosing a repository and persistent identifier; setting up ORCID

## What PDR / Wiley expect (verify current policy on the author page)

1. **Data availability statement.** Include a statement describing **whether and how** the data underlying
   the results can be accessed. For public data, give the access method with a **persistent identifier**
   (DOI or accession number); for restricted data, state the access conditions.
2. **FAIR repository + persistent identifiers.** Because PDR hosts no repository, deposit data and
   materials in a **FAIR-aligned repository** (ICPSR/openICPSR, Harvard Dataverse, Zenodo, OSF) and cite
   it with a permanent link — not a personal website or generic cloud folder. Find one via
   FAIRsharing.org or re3data.org.
3. **Reproducible, documented code.** Provide code that regenerates the results, with **software versions
   recorded** and **informative comments**. For a quantitative population-and-development paper, treat
   this as expected, not optional.
4. **Restricted data (common in this field).** DHS, census microdata, and linked administrative records
   are frequently licensed or confidential — **describe the conditions limiting access** and how others
   may obtain the data, provide the **extract specification and code** rather than the raw microdata, and
   align with FAIR principles as far as possible.
5. **ORCID and integrity.** Provide ORCID for the submitting author; declare funding, conflicts, and
   ethics/consent where human subjects are involved.

## Build-as-you-go checklist

- [ ] **Data availability statement** drafted (public / restricted / on request) with persistent IDs
- [ ] Data + materials deposited in a **FAIR repository** with a DOI/accession number
- [ ] One **master script** regenerates every table, figure, life table, decomposition, and projection
- [ ] **README** documents data provenance/vintage, construction of rates/exposure, and how to reproduce each exhibit
- [ ] **Code commented** and **software/package versions recorded** (`renv.lock` / `requirements.txt` / installs)
- [ ] **Seeds** set and reported for bootstrap and simulation
- [ ] Exhibit numbers in the manuscript **match** the deposited output exactly
- [ ] Restricted data: exemption note + access conditions + extract spec + synthetic data where feasible
- [ ] **ORCID** registered for the submitting author; funding/conflicts/ethics declared

## Anti-patterns

- Treating the data statement as a last-minute formality at acceptance
- A personal URL or generic cloud link instead of a persistent identifier in a FAIR repository
- Posting licensed DHS/census microdata you are not permitted to redistribute (share the extract code instead)
- Undocumented, un-seeded, uncommented code that "works on my machine"
- Claiming data are restricted without describing the access conditions

## What a reproducibility reviewer expects at PDR

PDR draws referees who re-derive a denominator or re-run a decomposition, and who care that licensed data
were handled correctly. Calibrate the package against the data class you actually used.

| Data class | Typical source | Deposit obligation |
|------------|----------------|--------------------|
| Fully public | HMD, HFD, WPP, published vital statistics, World Bank/WDI | Extract code + constructed analytic file (where license permits) + persistent ID |
| Public-but-licensed | IPUMS, **DHS**, redistribution-restricted census | Extract specification + code, **not** raw microdata; cite the provider's persistent access path |
| Restricted/confidential | Linked administrative records, RDC-only census, linked registers | Code + synthetic stand-in file + exact access-conditions note |

## Referee-pushback patterns and the PDR-specific fix

- *"I cannot tell which WPP/HMD vintage or DHS round produced these numbers."* -> Record the release label
  and download date in the README and a code comment; vintages and rounds revise the figures.
- *"You posted DHS microdata — that violates the license."* -> Remove raw microdata; ship the DHS extract
  request specification and the cleaning code, and cite DHS as the persistent access path.
- *"Your bootstrap/projection intervals are not reproducible."* -> Set and report a seed for every
  resampling and simulation step.
- *"You say data are restricted but give no way to obtain them."* -> Name the data enclave or application
  pathway and the access conditions; a bare "restricted" reads as evasion.

## Output format

```
【Data statement】public / restricted / on request — drafted with persistent ID? [Y/N]
【Repository】FAIR repo + DOI/accession (not personal URL)? [Y/N]
【Licensed data handled】extract code, not raw microdata, for DHS/census? [Y/N/NA]
【Reproducible code】master script + comments + recorded versions + seeds? [Y/N]
【Exhibits match deposit?】[Y/N]
【ORCID + declarations】submitting-author ORCID + funding/conflicts/ethics? [Y/N]
【Next】popdevr-review-process
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — FAIR repositories and reproducibility tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — PDR / Wiley data-availability and integrity policy
