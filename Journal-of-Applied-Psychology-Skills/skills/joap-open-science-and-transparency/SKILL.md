---
name: joap-open-science-and-transparency
description: Use when meeting the Journal of Applied Psychology (JAP) open-science requirements. JAP holds empirical work (including meta-analyses) to the TOP framework — data, materials, and code availability with persistent identifiers, a data-transparency / data-availability statement, and preregistration weighed in evaluation. Prepares compliance; it does not waive requirements.
---

# Open Science & Transparency (joap-open-science-and-transparency)

JAP is a TOP-aligned APA journal. Empirical submissions (including meta-analyses) are held to the
**Transparency and Openness Promotion (TOP)** standards: share **data, materials, and analysis code**
with **persistent identifiers**, provide a **data-availability / transparency statement**, and report
**preregistration** where applicable — with transparency weighed in evaluation. Prepare this early, not
at acceptance. Verify the **current TOP level and exact statement wording** on the official APA page
(待核实).

## When to trigger

- Building the data/materials/code deposits and the data-availability statement
- Deciding whether (and how) to claim an exemption from sharing
- Linking a preregistration and reporting its status
- A reviewer or editor flagged transparency, data access, or reproducibility

## What is expected (verify current wording on the official page)

1. **Data, materials, and code availability.** Make the dataset, study materials (scales, manipulations,
   instructions), and analysis scripts available, or state precisely why not. Sensitive personnel /
   organizational data often need a documented exemption with an access path.
2. **Data-transparency / data-availability statement.** A statement describing what data exist, where
   they live, how they can be accessed, and whether any portion has appeared in other papers (a
   **prior-use / overlapping-data disclosure** is expected when datasets are reused across articles).
3. **Persistent identifiers (DOIs).** Provide DOIs for shared data/materials/code (OSF, ICPSR,
   Dataverse, Zenodo) — not transient personal links.
4. **Preregistration.** Report preregistration honestly and link it (anonymized for masked review); its
   presence and quality are weighed, and Registered Reports may be available (confirm on the official
   page; 待核实).

## Build-it-right checklist

- [ ] **Data** deposited with a **DOI**; a **codebook/data dictionary** included (or a justified exemption)
- [ ] **Analysis code** deposited; results regenerate in a fresh session
- [ ] **Materials** (scales, manipulations, instructions) deposited with a DOI
- [ ] **Data-availability / transparency statement** drafted per current TOP requirements
- [ ] **Prior-use disclosure**: any overlap of this dataset with other papers stated explicitly
- [ ] **Preregistration** linked (anonymized for review); confirmatory vs. exploratory consistent with it
- [ ] Shared links **anonymized** for masked submission (no author-identifying repository info)

## Exemptions (do them honestly)

- Personnel and organizational data are often legally or contractually constrained. State exactly
  **what** is withheld, **why** (confidentiality, proprietary, IRB), and **how** others can access or
  approximate it (synthetic/aggregated data, application path, full code release). Unjustified opacity
  counts against the paper.

## Data-availability statement — worked draft (illustrative)

A model statement for the servant-leadership package; confirm the exact required headings against the
journal's current TOP/author requirements.

```
Data availability: Team- and individual-level data for the field study and
  trial-level data for the experiment are available at OSF
  (DOI 10.XXXX/osf.io/abcde), with a codebook.
Materials: All scales, the leadership manipulation, and instructions are
  deposited (DOI 10.XXXX/osf.io/fghij).
Code: Mplus/R scripts reproduce all reported values in a fresh session; a run
  log is included (DOI 10.XXXX/osf.io/klmno).
Preregistration: The experiment was preregistered (osf.io/pqrst) before data
  collection; one field-study serial-mediation analysis is reported as exploratory.
Prior use: The field dataset has not been used in any other manuscript.
  (If applicable, list overlapping papers and the constructs each uses.)
Exemptions: None. (If applicable: what is withheld, why, and the access path.)
```

## Transparency-readiness decision table

| Situation | Editorial read | What to deposit / state |
|-----------|----------------|-------------------------|
| Fully shareable data + materials + code | expected baseline | DOIs for data, materials, code + run log |
| Proprietary organizational data | exemption considered if justified | synthetic/aggregated data + access path + full code |
| Archival / third-party dataset | acceptable with provenance | link source, share derivation scripts, document version |
| Dataset reused across papers | requires disclosure | state overlap, which constructs each paper uses |
| "Available on request" | reads as non-compliant | replace with a persistent DOI before submission |

## Reviewer / editor pushback and the venue fix

- "No DOI, just a personal link" → swap every transient link for a persistent identifier before the
  masked submission goes out.
- "Statement says open but the repo is empty" → deposit first; draft the statement from the live DOIs.
- "Is this the same data as your other paper?" → add a prior-use/overlap disclosure; JAP expects it.
- "Preregistration deviates from the analysis" → add a deviations note; relabel post hoc work exploratory.
- "OSF page reveals author identity" → use the anonymized view link for masked review.

## Anti-patterns

- Treating data/materials/code sharing as optional or "available on request"
- Omitting the data-availability/transparency statement or a required prior-use disclosure
- Personal/transient links instead of DOIs
- Claiming an exemption without a justification or access path
- Identifying author info in repository links during masked review

## Output format

```
【Data】deposited + DOI + codebook (or justified exemption)? [Y/N]
【Materials】deposited + DOI? [Y/N]
【Code】deposited + fresh-session reproducible? [Y/N]
【Transparency statement】drafted per current TOP wording (待核实)? [Y/N]
【Prior-use disclosure】dataset overlap stated? [Y/N/NA]
【Preregistration】linked (anonymized) + consistent with reporting? [Y/N/NA]
【Next】joap-review-process
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — OSF, ICPSR, Dataverse, Zenodo, preregistration templates, DOIs
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — TOP requirements, data-availability statement, preregistration policy
