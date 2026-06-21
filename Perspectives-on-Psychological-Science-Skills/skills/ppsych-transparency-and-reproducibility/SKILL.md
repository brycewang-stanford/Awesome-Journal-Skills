---
name: ppsych-transparency-and-reproducibility
description: Use when meeting open-science and reproducibility obligations for a Perspectives on Psychological Science (PoPS) piece — repository deposit for any original data, a documented and ideally preregistered systematic protocol for meta-science, and exemplary disclosure (PoPS is an open-science leader). Builds the transparency layer; it does not draft the synthesis (ppsych-organizing-framework) or run the submission preflight (ppsych-submission).
---

# Transparency & Reproducibility (ppsych-transparency-and-reproducibility)

## When to trigger

- The piece reports or reuses any original data and you must make it available
- The piece is **meta-science** and its systematic coverage/coding must be reproducible
- You are deciding what to preregister, deposit, and disclose for a field-shaping reform piece
- You want the open-science layer to be drafted from live identifiers, not promised at acceptance

## Why this matters more at PoPS than almost anywhere

PoPS is a **leading venue for the open-science and replication movement** — much of the meta-science that reshaped psychology's methods appeared here. The journal's readers and reviewers hold reform-adjacent work to its own standard: a piece arguing for transparency that is itself opaque loses all authority. The bar is **exemplary practice**, especially for the reform/meta-science pieces that are PoPS's signature. Build the transparency layer early so the statements are written from real DOIs and OSF links, not aspirations.

## What the obligation bites on (by piece type)

| Piece type | Where transparency applies |
|------------|---------------------------|
| **Integrative review / theoretical statement** | the **systematic coverage account** (search strategy, inclusion/exclusion from `ppsych-literature-synthesis`); no new data of its own |
| **Meta-science / methodology** | the **systematic protocol** — sampling frame, coding scheme, double-coding/reliability, and the **data + code** behind every prevalence figure or statistic |
| **Meta-analysis with a superordinate message** | full meta-analytic dataset, effect-size extraction, and analysis code, reproducibly deposited |
| **Any piece including original data** | the data must be in a **repository**; the cover letter confirms ethical data collection (检索于 2026-06；以官网为准) |

## PoPS / SAGE policy facts (检索于 2026-06；以官网为准 — re-confirm on the author pages)

- **Original data → repository.** When original data are included, they must be available in a repository; deposit and cite the dataset (检索于 2026-06；以官网为准).
- **Ethical-collection confirmation.** Authors confirm in the **cover letter** that data collection followed ethical guidelines (检索于 2026-06；以官网为准).
- **Open-practice norms.** APS has historically pioneered **Open Practice badges** (Open Data, Open Materials, Preregistration) at its journals; confirm current badge availability and criteria for PoPS on the author pages, since policy evolves (检索于 2026-06；以官网为准 · 待核实 for the exact current PoPS badge set).
- **TOP-style sharing.** Treat the Transparency and Openness Promotion (TOP) guidelines as the baseline expectation for data/code/materials sharing; map your deposits to it (检索于 2026-06；以官网为准).

## Building the reproducible meta-science protocol

For a reform/meta-science piece, the protocol *is* the design — make it auditable:

1. **Preregister** the sampling frame, inclusion/exclusion rules, and the coding scheme (OSF/AsPredicted) **before** coding, and report the registration link. Mark any deviation as a deviation.
2. **Deposit** the coded dataset, the coding manual, and the analysis scripts (R/Python) in a public repository (OSF, GitHub + Zenodo DOI).
3. **Report reliability** for subjective coding (two coders, inter-rater agreement) so the prevalence claims are not one reader's judgment.
4. **Make figures reproducible** — every prevalence/forest exhibit regenerates from the deposited data and script.

## Checklist

- [ ] Piece type identified; the right transparency obligation selected (coverage account vs. data+code)
- [ ] Any original data deposited in a repository and cited; ethical-collection confirmation in the cover letter
- [ ] Meta-science: protocol preregistered (frame + inclusion + coding); registration link reported
- [ ] Meta-science / meta-analysis: dataset, coding manual, and analysis code deposited (OSF/Zenodo DOI)
- [ ] Inter-rater reliability reported for subjective coding
- [ ] Every prevalence/forest figure regenerates from deposited data + script
- [ ] Deposits mapped to TOP-level expectations; Open-Practice badge eligibility checked (待核实 current set)
- [ ] Transparency statements drafted from live identifiers, not promises
- [ ] AI-use and conflict-of-interest disclosures prepared per current policy

## Anti-patterns

- A reform/transparency argument that is itself unreproducible (fatal credibility loss at PoPS)
- "Data available upon request" instead of a repository deposit when original data are included
- A meta-science prevalence figure with an undisclosed, unpreregistered sampling frame
- One-coder subjective extraction presented as fact, with no reliability statistic
- Promising open data/code at acceptance instead of depositing and citing it at submission
- Asserting the current badge set, TOP level, or data policy from memory rather than the live SAGE/APS pages

## Output format

```text
【Piece type】review/theory / meta-science / meta-analysis / includes-original-data
【Coverage account】search + inclusion/exclusion documented (review/theory)? Y/N · N/A
【Data deposit】original data in repository + cited; ethical-collection confirmed in cover letter? Y/N · N/A
【Preregistration】meta-science protocol preregistered; link reported? Y/N · N/A
【Code/materials】coding manual + analysis scripts deposited (DOI)? Y/N · N/A
【Reliability】inter-rater agreement reported for subjective coding? Y/N · N/A
【Reproducible figures】prevalence/forest exhibits regenerate from deposit? Y/N · N/A
【Policy re-confirm】badges / TOP level / data policy checked on SAGE/APS pages? Y/N · 待核实
【Next step】→ ppsych-editor-strategy → ppsych-submission
```
