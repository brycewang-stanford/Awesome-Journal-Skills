---
name: lancet-ethics
description: Use to satisfy The Lancet's clinical-ethics and research-integrity requirements — ethics-committee approval and informed consent under the Declaration of Helsinki, the Declaration of interests, ICMJE author contributions, the role-of-the-funding-source statement, the data-sharing statement, patient and public involvement, and SAGER sex/gender plus equity reporting.
---

# Ethics & Research Integrity (lancet-ethics)

## When to trigger

- Preparing the ethics, contributions, conflicts, funding, and data-sharing statements.
- The manuscript lacks a Declaration of interests or a role-of-the-funding-source statement.
- Sex/gender or race/ethnicity reporting is missing where the study warrants it.
- A reviewer or editor flags consent, integrity, or funder-influence concerns.

## Ethics approval and consent

- [ ] Named **ethics committee / institutional review board** approval(s), with the approving body and (where available) reference number, for **every** participating site/country.
- [ ] **Informed consent** obtained (or a documented waiver with justification); consent for publication where identifiable.
- [ ] Conduct stated to follow the **Declaration of Helsinki** (and Good Clinical Practice for trials).
- [ ] For multi-country studies, confirm local approvals and any community/ethics considerations in LMIC settings.

## Declaration of interests (The Lancet's term for COI)

- [ ] A **Declaration of interests** for **all** authors (financial and non-financial), following the **ICMJE disclosure** form; "[Author] declares no competing interests" is explicit, not assumed.
- [ ] Covers grants, consultancies, honoraria, patents, advisory roles, and relevant personal relationships, within the relevant disclosure window.

## Authorship — ICMJE criteria

- [ ] Each author meets all **four ICMJE criteria** (substantial contribution; drafting/revising; final approval; accountability).
- [ ] **Author contributions** described (who did what — design, data, analysis, writing); note who **verified the underlying data**.
- [ ] Contributors who do not meet authorship criteria are acknowledged; any medical writers disclosed.

## Role of the funding source (Lancet-specific, required)

The Lancet requires an explicit **role of the funding source** statement that addresses:

- [ ] What the funder **did and did not do** (e.g., role in design, data collection, analysis, interpretation, writing).
- [ ] **Who had full access to the data** (often "all authors had access to the data," or named authors).
- [ ] **Who had final responsibility for the decision to submit** for publication.
- A typical sentence: *"The funder had no role in study design, data collection, analysis, interpretation, or writing of the report. [Named authors] had full access to all the data and had final responsibility for the decision to submit for publication."*

## Data sharing statement

- [ ] A **data sharing statement** specifying what data will be shared (e.g., de-identified individual participant data), with what (data dictionary, protocol, SAP), to whom, when, by what mechanism, and under what conditions. Follows ICMJE data-sharing requirements (mandatory for clinical trials).

## Patient and public involvement (PPI)

- [ ] State whether and how patients/the public were involved in design, conduct, or dissemination — or that they were not, with reasons.

## Sex, gender, and equity reporting

- [ ] Apply the **SAGER guidelines**: report participants by **sex and/or gender**, justify any single-sex study, and analyse/report sex/gender differences where relevant.
- [ ] Report participants' **race/ethnicity** where relevant, with the classification rationale, and use the **PROGRESS-Plus** equity lens for who was (and was not) represented.
- [ ] Address generalisability across the populations the result is meant to serve, especially for global-health work.

## What Lancet editors check among the declarations

The Lancet treats the declarations block as load-bearing. Editors verify the journal-specific **role of the funding source** statement, an ICMJE-compliant **data-sharing statement** (a blank one is non-compliant for a trial), ethics approval for every site, and SAGER sex/gender reporting.

## Worked micro-example (illustrative — not a real statement)

A hypothetical multi-country trial, public funder.

```
Role of funding source (illustrative): "The funder had no role in design, analysis, or
  writing. AB and CD had full data access and final responsibility for submitting."
Data sharing: de-identified IPD + protocol + SAP on request after 9 months.
```

## Reviewer / editor-pushback patterns and the venue-specific fix

- *"The role-of-the-funding-source statement is missing."* → Add the explicit statement covering funder role, data access, and final responsibility to submit.
- *"The data-sharing statement is blank."* → State what will be shared, with whom, when, and how — or justify "none"; ICMJE makes this mandatory for trials. Confirm any current consent-documentation requirement in the journal's author guidelines.

## Output format

```
【Ethics approval + consent】 committee(s) + Helsinki + consent (all sites)? → gaps
【Declaration of interests】 all authors, ICMJE form, explicit "none" where applicable? yes/no
【Authorship】 ICMJE 4 criteria + contributions + data verifier? yes/no
【Role of funding source】 funder role + data access + final responsibility to submit? yes/no
【Data sharing statement】 present + ICMJE-compliant? yes/no
【PPI】 stated? yes/no
【SAGER + equity】 sex/gender reported; race/ethnicity where relevant; PROGRESS-Plus? yes/no
【Next】 lancet-submission
```

## Anti-patterns

- **Do not** omit the role-of-the-funding-source statement — The Lancet requires it explicitly.
- **Do not** leave the data sharing statement blank for a clinical trial; "no data shared" must be stated and justified.
- **Do not** report a mixed-sex study without sex/gender-disaggregated reporting (SAGER).
- **Do not** assume "no competing interests" — each author must declare explicitly.
