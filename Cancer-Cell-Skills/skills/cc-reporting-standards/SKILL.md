---
name: cc-reporting-standards
description: Use when assembling STAR Methods and the Key Resources Table for a Cancer Cell (Cell Press) manuscript, and when ensuring rigor / reproducibility (cell-line authentication, mycoplasma, antibody validation, ARRIVE animal reporting, data/code deposition). It governs reporting; it does not design experiments.
---

# Rigor, Reproducibility & STAR Methods (cc-reporting-standards)

## When to trigger

- Drafting or auditing the Methods section for a Cell Press submission
- Reviewers may flag unauthenticated cell lines, undefined reagents, or missing deposition
- Need to build the Key Resources Table (KRT) and assign RRIDs
- Animal or sequencing work needs structured rigor reporting

## STAR Methods structure

Cell Press uses **STAR Methods** (Structured, Transparent, Accessible Reporting). Organize methods under standardized headings:

1. **Key Resources Table (KRT)** — at the top; tabulates every critical reagent/resource with source, identifier, and RRID.
2. **Resource availability** — Lead contact; Materials availability (plasmids, cell lines, mouse strains); Data and code availability.
3. **Experimental model and study participant details** — cell lines, animals, human subjects, organoids/PDX provenance.
4. **Method details** — full protocols, reproducible by an expert.
5. **Quantification and statistical analysis** — what test, what `n`, what software (links to `cc-statistics`).

## Key Resources Table — what must carry an RRID / identifier

| Category | Required detail |
|----------|-----------------|
| Antibodies | Host, clone, vendor, catalog #, RRID, dilution/application |
| Cell lines | Name, sex/origin, source, authentication status, RRID (Cellosaurus) |
| Chemicals / inhibitors | Vendor, catalog #, identifier |
| Critical kits | Vendor, catalog # |
| Deposited data | Repository + accession (GEO/SRA/PRIDE/PDB) |
| Oligos / sgRNAs / primers | Full sequences |
| Recombinant DNA / plasmids | Source, Addgene # / RRID |
| Organisms / strains | Strain, source, RRID (e.g., MGI/JAX) |
| Software / algorithms | Name, version, URL, RRID |

## Cell-line rigor (frequent reviewer target)

- **Authenticate** human cell lines (STR profiling); reference Cellosaurus; state the source.
- **Mycoplasma testing** — state that lines were tested negative; give frequency.
- Flag any misidentified/commonly contaminated lines (ICLAC register) and justify use.
- Report passage range and culture conditions enough to reproduce.

## Antibody validation

- Give clone, catalog, RRID, and **application-specific** validation (KO/KD control, single band of expected MW, IHC titration with positive/negative tissue).
- For new/critical antibodies, show validation in the supplement.

## Animal reporting (ARRIVE 2.0 essentials)

- Species, strain, sex, age, source; housing and husbandry.
- **Sample size** rationale; **randomization**; **blinding** of outcome assessment.
- Inclusion/exclusion criteria; humane endpoints; number used and analyzed.
- IACUC protocol number and approving institution (statement routed via `cc-ethics-registration`).

## Data and code availability

- Deposit and cite accessions in the KRT and availability statement:
  - Sequencing / arrays → **GEO/SRA**; controlled human genomics → **dbGaP/EGA**
  - Proteomics → **PRIDE**; metabolomics → MetaboLights/Workbench
  - Structures → **PDB** (+ **EMDB** for cryo-EM maps)
- Custom code → versioned public repo with a citable DOI (e.g., Zenodo).
- "Available on request" is unacceptable for these data types.

## Worked micro-example: a KRT antibody row before → after

**Before (desk-reject-grade entry):**

> Anti-MARK7 — Abcam — for Western blot

**After (STAR-compliant entry):**

> Rabbit monoclonal anti-MARK7, clone EPR-xxxx, Abcam, Cat# ab000000, RRID:AB_0000000; WB 1:1000,
> validated against MARK7-KO lysate (single band at expected MW, Figure S1).

The "after" carries host, clonality, clone ID, vendor, catalog, RRID, application, dilution, and the
validation evidence — every column a Cancer Cell editor scans the KRT for. A reviewer who cannot find
the RRID or the KO/KD validation treats the reagent as unverified.

## STAR Methods pre-submission self-check

Walk the Methods in the order an in-house editor will:

1. Is the **KRT at the top**, with a row for every antibody, line, organism, plasmid, oligo, dataset, and software?
2. Does **Resource availability** name the lead contact and state materials + data + code availability explicitly?
3. Are **cell lines** authenticated (STR), mycoplasma-negative, and cross-checked against the ICLAC misidentified-lines register?
4. Do **animal** subsections give species/strain/sex/age, sample-size rationale, randomization, and blinded outcome scoring?
5. Are **all** newly generated large datasets deposited with accessions echoed in both the KRT and the availability statement?
6. Is the **statistics** subsection specific — exact test, `n` as biological replicates, multiplicity correction?

## Rigor failure modes that draw reviewer or editor flags

- A KRT that lists reagents but omits RRIDs or authentication status.
- Human lines with no STR profile, or a commonly contaminated line used without justification.
- Antibodies validated "by the manufacturer" only, with no in-house KO/KD or titration control.
- Animal work reporting "n mice" with no allocation, blinding, or exclusion criteria.
- Sequencing/proteomics described in Results but with no GEO/PRIDE accession by submission.
- Code described as "custom scripts" with no repository or DOI.

## Checklist

- [ ] STAR Methods headings used; KRT at top
- [ ] Every antibody, cell line, organism, plasmid, software has source + RRID
- [ ] Human cell lines STR-authenticated; mycoplasma-negative stated
- [ ] Antibody validation described (and shown for critical ones)
- [ ] Animal section reports sample size, randomization, blinding, exclusions
- [ ] All large datasets deposited; accessions in KRT + availability statement
- [ ] Custom code deposited with DOI
- [ ] Lead contact and materials-availability statements present

## Anti-patterns

- Cell lines with no authentication or mycoplasma statement
- Antibodies listed as "anti-X (Abcam)" with no catalog/RRID/validation
- Animal methods with no randomization/blinding/sample-size basis
- Sequencing data "available upon request" with no accession
- Methods too thin to reproduce the experiment

## Output format

```
【STAR Methods】headings complete? KRT present?
【KRT gaps】reagents missing source/RRID: [...]
【Cell-line rigor】authenticated? mycoplasma? contaminated-line flags?
【Antibody validation】adequate / show in supplement: [...]
【Animal rigor】ARRIVE elements present? [...]
【Deposition】GEO/SRA/PRIDE/PDB accessions + code DOI status
【Next step】cc-statistics or cc-ethics-registration
```
