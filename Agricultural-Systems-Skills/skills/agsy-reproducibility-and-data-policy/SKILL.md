---
name: agsy-reproducibility-and-data-policy
description: Use when preparing the data, code, and model materials for an Agricultural Systems (AgSy) manuscript. AgSy applies Elsevier's research-data policy, which treats software, code, and models as research data — deposit them in a repository and cite/link them, or state why they cannot be shared. Covers model-description standards and exemptions. Prepares the materials; it does not waive requirements.
---

# Reproducibility & Data Policy (agsy-reproducibility-and-data-policy)

AgSy is a modelling journal, so reproducibility is not just about data — it is about whether someone
else could **re-run or re-implement your model**. Elsevier's research-data policy explicitly counts
**software, code, models, algorithms, protocols, and methods** as research data. Build the package as
you go so submission and revision do not stall. The 2026-06-20 Guide for Authors refresh says
Agricultural Systems applies **Option C**: deposit research data, cite and link it, or state why
sharing is not possible.

## When to trigger

- Building the data + code + model materials for submission
- Writing the data-availability statement
- Data, code, or the model cannot be fully shared (licence, privacy, proprietary model) and you need
  the exemption path
- Preparing model documentation so reviewers can assess reproducibility

## What AgSy / Elsevier expects

1. **Deposit research data in a repository.** Use a recognized repository (Mendeley Data, Zenodo, OSF,
   or a domain repository), **cite and link** the dataset in the article. Not a personal website.
2. **Code and models count as data.** Deposit run scripts, parameter files, and — where licensing
   allows — the model code or a pointer to the exact model version. A black-box model with no access
   path weakens the paper.
3. **Data-availability statement.** State the availability of data at submission. If data, code, or the
   model cannot be shared, **explain why** (third-party licence, privacy, proprietary model) and how
   others could obtain equivalent access.
4. **Model description.** Document model version, structure/equations, parameter sources, calibration
   vs. evaluation data, and driving inputs. For agent-based models, follow the **ODD protocol** so the
   model can be re-implemented.

## When data/code/model cannot be shared (exemption path)

- **Explain why** (proprietary model, licensed input data, privacy/legal restrictions).
- Give a **README** describing exactly how others can obtain access (provider, licence, version).
- Where possible, share **synthetic inputs** or a reduced example so the workflow can be exercised.

## Build-as-you-go checklist

- [ ] One **master workflow** regenerates every table/figure from inputs + model runs
- [ ] **Data + code + model/run scripts** deposited in a repository with a DOI/permanent link
- [ ] **README** documents data provenance, model version, calibration/evaluation split, and how to reproduce each exhibit
- [ ] **Seeds** set and reported for every stochastic step (Monte Carlo, ABM, weather/price generators)
- [ ] Software/model **versions pinned** (`renv.lock` / `requirements.txt` / environment file)
- [ ] Exhibit numbers in the manuscript **match** the package output exactly
- [ ] Restricted materials: exemption note + access instructions + synthetic example where feasible
- [ ] **Data-availability statement** drafted for the manuscript

## Anti-patterns

- Treating the package as a post-acceptance afterthought
- Depositing data but not the **code or model** (Elsevier counts them as research data)
- A black-box model with no version, parameters, or access path
- A personal URL instead of a citable repository with a permanent identifier
- Undocumented, un-seeded, unpinned runs that "work on my machine"

## Worked micro-example (illustrative)

An agent-based crop–livestock model with a licensed weather input is packaged. Elsevier treats more than
tabular data as "research data," so each artifact maps to a sharing path:

- **Model code** is open → deposited on Zenodo with a tagged version and DOI; the commit is cited.
- **Weather data** is licensed → cannot be redeposited. The README names the provider, license, and
  version, and ships a synthetic series so a reader can exercise the workflow end-to-end.
- **ABM documentation** follows the ODD protocol so the model can be re-implemented, not just re-run;
  **seeds** are fixed and `renv.lock` pins the toolchain.

Outcome: a reviewer can reproduce every exhibit except the licensed input, for which a documented,
exercisable substitute exists.

## Referee pushback → the AgSy-specific fix

- *"The model is a black box."* → Deposit code (or pin the version) and document structure, parameters,
  and the calibration/evaluation split; add the ODD protocol for an ABM.
- *"Data are on a personal website."* → Move to a citable repository with a permanent identifier.
- *"Only the data is shared."* → Add run scripts, parameter files, and the model/version — Elsevier
  counts them as research data.

## Calibration anchors

- Agricultural Systems currently uses Elsevier **Option C** research-data instructions: deposit, cite,
  and link research data, or explain why sharing is not possible.
- The ODD protocol is a community standard for agent-based models, not a journal format.

## Output format

```
【Repository】data + code + model deposited with DOI/link? [Y/N]
【Reproduces tables/figures?】master workflow verified locally? [Y/N]
【Model documented】version + parameters + calibration/eval split (+ODD if ABM)? [Y/N]
【Restricted?】exemption note + access path + synthetic example?
【Data-availability statement】drafted? [Y/N]
【Next】agsy-review-process
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — repositories, version-pinning, and model-description standards (ODD)
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — Elsevier research-data policy (data, code, models)
