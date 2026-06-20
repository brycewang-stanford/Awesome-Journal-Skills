---
name: jimf-internet-appendix
description: Use when organizing the online/supplementary appendix and the data-and-code deposit for a Journal of International Money and Finance (JIMF) manuscript. Structures supplementary material and the replication package; it does not establish the main result or write the main text.
---

# Online Appendix & Replication (jimf-internet-appendix)

## When to trigger

- Robustness, derivations, and extra country results are crowding the main text and need a home
- The appendix is sprawling with no map from each table back to a main claim
- You must prepare the Elsevier data-and-code deposit (Mendeley Data / linked repository) and a Data Availability Statement
- Restricted data (central-bank, BIS, supervisory, EPFR, Bloomberg/Datastream-licensed) cannot be posted and you need a compliant access path
- A referee asked for a check that belongs in supplementary material, not the published exhibits

## What goes in the JIMF online appendix (and what must not)

The appendix is for material that *supports but does not carry* a main claim. JIMF referees do read it, so it must be navigable and every item must trace to a main-text statement. The main paper must remain self-contained: the headline result, identification, and the lead robustness checks live in the body, not the appendix.

| Belongs in the online appendix | Stays in the main text |
|--------------------------------|------------------------|
| Full control sweeps; alternative-measure tables | The preferred specification and headline coefficient |
| By-country / by-region detail behind a pooled estimate | The identification argument and lead robustness |
| Variable definitions, sources, vintages, splicing notes | The one-line data-to-object mapping |
| Model derivations, additional proofs | The mechanism stated for the reader |
| Placebo and falsification full tables | The headline placebo result |
| Sensitivity to bandwidth/window/lag choices | The chosen window and why |

## Why JIMF referees actually open the appendix

Unlike some journals where the appendix is a courtesy, JIMF referees use it to verify the claims the main text makes economically: the full country-by-country results behind a pooled coefficient, the alternative-measure tables that show the headline is not an artifact, and the variable definitions that confirm you measured what you say. Build it for that reader. The single most common appendix failure is the orphan table — an exhibit with no main-text sentence it supports — which signals the analysis was run but never integrated into the argument. The index at the top is the cure: it forces every appendix item to declare its main-text home.

## Replication & data policy (Elsevier; verify on the live Guide for Authors)

JIMF follows **Elsevier's research-data policy**: authors are expected to share data and code, typically via **Mendeley Data** or a linked repository, and to include a **Data Availability Statement** describing how the data can be accessed (检索于 2026-06；以官网为准 — exact wording and whether deposit is mandatory at acceptance is 待核实). Build the package as if it will be checked.

1. **Code that runs top-to-bottom** from raw (or documented-access) inputs to every table and figure, with a master script and a README mapping each script to each exhibit number.
2. **Data Availability Statement** that is honest about restricted sources: state which series are public (IMF IFS/BoP, BIS, World Bank, Lane–Milesi-Ferretti, Chinn–Ito, AREAER) and which are licensed/restricted (Bloomberg, Datastream, EPFR, supervisory/central-bank data), and give the access path for the latter (vendor, application route, or contact) rather than posting them.
3. **Series-level documentation**: every variable's source, vintage, units, and any splicing/seasonal adjustment, so a replicator can reconstruct the panel.
4. **Seeds and software versions** for any bootstrap, simulation, or estimation, so results are exactly reproducible.
5. **A table-to-script-to-data map** so a referee or the Elsevier process can trace any number.

## Handling restricted international data (the JIMF-specific problem)

International-finance papers lean on data that often cannot be redistributed, and the Data Availability Statement must be honest about it. A practical taxonomy:

| Data type | Typical examples | Deposit approach |
|-----------|------------------|------------------|
| Fully public | IMF IFS/BoP, BIS statistics, World Bank WDI, Lane–Milesi-Ferretti, Chinn–Ito, AREAER | Post the cleaned panel + code |
| Public but licensed redistribution | some central-bank series, Reinhart–Rogoff classifications | Post code + access instructions, not the raw file if the license forbids |
| Vendor-licensed | Bloomberg, Refinitiv/Datastream, EPFR | Post code with the exact pull/query; do NOT post the data; name the vendor and field |
| Restricted/confidential | supervisory bank data, confidential central-bank transaction data | Describe the access route (application, data-room, contact); provide synthetic or aggregated extracts if permitted |

The test a referee applies: could someone with the same data licenses reproduce every number from your code? If the answer requires an undocumented manual step or a vendor pull you never specified, the package fails.

## Worked vignette (illustrative)

A paper's online appendix is 70 pages of regression dumps with no index, and the replication code needs a manual Datastream download the README never mentions. The JIMF fix: add a one-page index at the top mapping each appendix table to the main-text claim it supports (A1–A4 → Section 4 robustness, A5–A8 → by-country heterogeneity behind Table 3, etc.); write a master script with a documented `data/` step that lists the exact Datastream/Bloomberg fields and the EPFR query, posts the public series (IMF, BIS, Lane–Milesi-Ferretti) directly, and states in the Data Availability Statement which series are licensed and how to obtain them. The appendix is now navigable and the package is reproducible by anyone with the same licenses.

## Checklist

- [ ] Every appendix table maps to a specific main-text claim (a one-line index at the top)
- [ ] The main paper is self-contained without the appendix (headline + identification + lead robustness in the body)
- [ ] Master script reproduces every table and figure from documented inputs
- [ ] Data Availability Statement drafted; public vs. restricted series clearly separated
- [ ] Restricted data (Bloomberg/Datastream/EPFR/supervisory) given an access path, not posted
- [ ] Variable definitions, sources, vintages, and splicing documented at the series level
- [ ] Seeds and software/package versions recorded for bootstraps and simulations
- [ ] A replicator with the same data licenses could reproduce every number from the code
- [ ] No licensed vendor data (Datastream/Bloomberg/EPFR) posted in violation of its license

## Anti-patterns

- An appendix that is a 60-page data dump with no index from tables to claims
- A main result that is only fully shown in the appendix (the body is not self-contained)
- A Data Availability Statement that claims "data available on request" while the code silently needs licensed Bloomberg pulls
- Posting licensed vendor data (Datastream/Bloomberg/EPFR) in violation of the license
- Code that hard-codes one machine's paths or omits the seed, so the bootstrap cannot be reproduced
- Treating the deposit as a post-acceptance afterthought rather than building it alongside the exhibits

## Output format

```text
【Journal】Journal of International Money and Finance
【Skill】jimf-internet-appendix
【Body self-contained】headline + identification + lead robustness in main text? [Y/N]
【Appendix index】each appendix item → main-text claim? [Y/N]
【Replication】master script reproduces all exhibits from documented inputs? [Y/N]
【Data statement】public vs. restricted separated; access path for restricted? [Y/N]
【Restricted data】Bloomberg/Datastream/EPFR/supervisory handled per license? [Y/N]
【Source status】Elsevier data policy verified / 待核实
【Next skill】jimf-writing-style
```
