---
name: worlddev-replication-package
description: Use when preparing the data/code or qualitative-transparency materials for a World Development (WD) manuscript under Elsevier's research-data policy and double-anonymized review. Assembles the package; it does not invent evidence or citations.
---

# Replication & Transparency Package (worlddev-replication-package)

## When to trigger

- The paper is empirical and there is no data-availability statement or no organized code
- Sensitive development data (household surveys, conflict locations, vulnerable informants) cannot be posted as-is
- A qualitative paper has no plan for transparency — readers cannot see how evidence became claims
- The data-availability statement risks **de-anonymizing** the authors during double-anonymized review
- Reviewers or the editor request materials and the project is not reproducible end to end

## WD's transparency posture

WD follows **Elsevier's research-data policy**: authors are asked to state data availability and are encouraged to share data and code, with deposit in a recognized repository as best practice (检索于 2026-06；以官网为准). WD is not a journal with a mandatory pre-acceptance reproducibility audit on the model of the AEA or the Econometric Society — but the expectation of transparency is real and rising, and referees increasingly ask for it. Two features make WD distinctive:

1. **Double-anonymized review** creates a real tension: a data-availability statement, a repository link, or an acknowledgments line can reveal author identity. Prepare a **review-safe version** (anonymized statement: "data and code will be deposited in a public repository upon acceptance"; no identifying URLs, no self-citation that unmasks) and a **camera-ready version** with the live deposit. Keep these separate so the wrong one is never uploaded.
2. **Ethical and access constraints are the norm, not the exception** in development research. Restricted survey data, geocoded conflict data, and human-subjects protections often bar open posting. WD accepts this — what it does not accept is silence. State *why* data cannot be shared and *how* a reader could obtain or reconstruct access.

## Quantitative package

- **Data-availability statement** matched to reality: open / restricted-with-access-route / proprietary-with-justification.
- **Code** that runs top to bottom from raw (or de-identified) inputs to every number, table, and figure, with a master script and a README listing software, packages/versions, and runtime.
- **De-identification** of human-subjects data; document the procedure; never post direct identifiers or precise locations of vulnerable populations.
- **Provenance**: cite the original data source and any survey instrument; for secondary data (DHS, LSMS, Afrobarometer), give the version/round.

## Qualitative transparency package

Transparency for qualitative WD work is **not** raw-transcript dumping — that can violate informant confidentiality. It means making the inference auditable:

- **Methods appendix:** sampling/case-selection logic, data-generation process, coding scheme, and analysis approach.
- **Evidence-to-claim trail:** how themes were built; how rival explanations were tested.
- **Anonymized, ethically cleared excerpts** sufficient to let a reader judge the interpretation, with confidentiality protected.
- **Reflexivity and ethics note:** consent, IRB/ethics approval, and the researcher's positionality.

## Mixed-methods

Document **both** strands and, critically, the **integration procedure** — how the qual and quant were brought together — so the joint inference is reproducible in logic even where raw data are restricted.

## Checklist

- [ ] Data-availability statement is accurate (open / restricted / proprietary) with a route to access where closed
- [ ] Quant code runs end-to-end from inputs to all exhibits; README lists software + versions
- [ ] Human-subjects data de-identified; no precise locations of vulnerable groups
- [ ] Secondary data cited with version/round; instruments provided where relevant
- [ ] Qual: methods appendix + evidence trail + ethics/consent documented
- [ ] **Review-safe (anonymized) version** prepared separately from the camera-ready deposit
- [ ] Mixed: integration procedure documented

## Anti-patterns

- A repository link or identifying acknowledgments in the **review** version — breaks double-anonymization
- "Data available on request" with no real intention or route to honor it
- Posting geocoded conflict data or identifiable informant material — an ethics failure WD takes seriously
- Treating qualitative transparency as raw-transcript dumping rather than an auditable inference trail
- Code that reproduces some but not all reported numbers

## Output format

```text
【Journal】World Development (WD)
【Skill】worlddev-replication-package
【Verdict】deposit-ready / gaps remain
【Data status】open / restricted+route / proprietary+justification
【Code】end-to-end reproducible + README? [Y/N]
【Ethics】de-identification / consent / IRB documented? [Y/N]
【Qual transparency】methods appendix + evidence trail? [Y/N / n/a]
【Anonymization】review-safe version separated from camera-ready? [Y/N]
【Source status】verified URL / 待核实 / not asserted
【Next skill】worlddev-referee-strategy
```
