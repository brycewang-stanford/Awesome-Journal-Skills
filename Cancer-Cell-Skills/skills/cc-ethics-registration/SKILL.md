---
name: cc-ethics-registration
description: Use when assembling ethics approvals and availability statements for a Cancer Cell (Cell Press) manuscript — IACUC animal approval, human-sample IRB/consent, biosafety, and data/code deposition statements. It governs compliance declarations; it does not design experiments or write methods detail.
---

# Ethics, Approvals & Data Availability (cc-ethics-registration)

## When to trigger

- The study uses animals, human samples, or hazardous agents
- You need the IACUC / IRB / consent / biosafety statements
- You need the **Data and code availability** statement and accessions
- A clinical-translational component may need trial registration

## Animal work — IACUC

- State that all animal procedures were **approved by the institutional IACUC** (or equivalent), with the **protocol number** and institution.
- Confirm compliance with relevant national/institutional guidelines.
- Pair with ARRIVE-style methods reporting (sample size, randomization, blinding, humane endpoints) handled in `cc-reporting-standards`.

## Human samples — IRB & consent

- State **IRB / ethics committee approval** (institution + protocol).
- State that **informed consent** was obtained (or a documented waiver and its basis).
- Affirm compliance with the **Declaration of Helsinki** for human-subjects research.
- For patient-identifiable genomic data, note controlled-access deposition (dbGaP/EGA) and any data-use limitations.
- If a clinical trial provided samples/outcomes, give the **registration number** (e.g., ClinicalTrials.gov) and registry.

## Biosafety & other compliance

- Note biosafety level / institutional biosafety approval for pathogens, lentivirus/retrovirus, or hazardous reagents where relevant.
- Recombinant DNA / dual-use considerations if applicable.
- Disclose any field-collected or regulated materials (permits).

## Data and code availability (Cell Press standard)

Provide an explicit statement with three components:

1. **Data** — all newly generated datasets deposited and accessions listed (GEO/SRA for sequencing; dbGaP/EGA for controlled human genomics; PRIDE for proteomics; PDB/EMDB for structures; MetaboLights/Workbench for metabolomics). State public availability as of publication date.
2. **Code** — any original/custom code deposited in a citable repository with a DOI (e.g., Zenodo release of a GitHub tag).
3. **Other** — any additional information/reagents available from the lead contact on request.

Accessions must also appear in the **Key Resources Table**. "Available on request" is not acceptable for the data types above.

## Authorship & disclosure (usually adjacent)

- Author contributions (CRediT-style), competing-interests declaration, and funding statement are typically required — confirm current sections on the author page.

## Checklist

- [ ] IACUC approval stated with protocol # and institution (if animals)
- [ ] IRB/ethics approval + informed consent (or waiver) stated (if human samples)
- [ ] Declaration of Helsinki compliance affirmed (human subjects)
- [ ] Controlled-access deposition noted for patient-identifiable genomics
- [ ] Trial registration number given (if a registered trial supplied data)
- [ ] Biosafety / hazardous-agent approvals noted where relevant
- [ ] Data availability: all accessions listed and in the KRT
- [ ] Code deposited with a citable DOI
- [ ] Competing interests, funding, and author contributions drafted

## Anti-patterns

- "Animal experiments followed guidelines" with no IACUC approval/number
- Human samples used with no IRB/consent statement
- Genomic patient data with no controlled-access plan
- "Data available upon request" for sequencing/proteomics/structures
- Missing or vague competing-interests / funding declarations
- Trial-derived data with no registration number


## Ethics pass for Cancer Cell

Use this as a second-pass capability check. First lock the cancer context, mechanism, model system, validation chain, and translational boundary; then test whether the manuscript addresses cancer-biology reviewers who expect mechanistic oncology, translational relevance, and strong multi-modal validation.

- **Primary move:** Check consent/approval, registration, safety, privacy, data sharing, and disclosure statements before claiming compliance.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against Cell for broader biology, Nature Cancer for oncology breadth, Clinical Cancer Research for clinical translation; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Animal】IACUC approval + protocol #? Y/N
【Human】IRB + consent + Helsinki? controlled-access if needed? Y/N
【Biosafety】approvals noted where relevant? Y/N
【Trial registration】number given (if applicable)? Y/N
【Data availability】accessions listed + in KRT? Y/N
【Code】DOI deposited? Y/N
【Disclosures】competing interests / funding / contributions? Y/N
【Next step】cc-writing-style or cc-submission
```
