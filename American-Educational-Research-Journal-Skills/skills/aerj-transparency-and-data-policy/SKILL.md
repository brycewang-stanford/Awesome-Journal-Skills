---
name: aerj-transparency-and-data-policy
description: Use when preparing the transparency, reporting, and data-availability materials for an American Educational Research Journal (AERJ) manuscript. AERJ expects work to meet the AERA Standards for Reporting on Empirical Social Science Research (quantitative + qualitative) and the AERA Code of Ethics expectations on making data available. Prepares the materials; it does not waive requirements.
---

# Transparency & Data Policy (aerj-transparency-and-data-policy)

AERJ is an AERA journal: it expects reporting that is **warranted** and **transparent**, per the **AERA
reporting standards**, and adherence to the **AERA Code of Ethics**, which expects authors to make data
available for reanalysis after publication (within confidentiality and legal limits). Build
transparency in as you write, not after acceptance.

## When to trigger

- Aligning the manuscript with the AERA reporting standards
- Planning data/code availability and documentation
- Human-subjects data that cannot be fully shared (privacy, IRB, provider restrictions)
- A qualitative or mixed-methods study where transparency means more than a dataset

## What to satisfy (verify current wording on the official pages)

1. **Reporting standards.** Meet the **AERA Standards for Reporting on Empirical Social Science
   Research** — adequate evidence (warrant) and explicit logic of inquiry (transparency), for **both
   quantitative and qualitative** work. Humanities-oriented work follows the companion 2009 standards.
2. **Data availability.** Per the AERA Code of Ethics, be prepared to **share data and the basis of
   interpretations** for reanalysis after results are published, subject to participant confidentiality
   and legal/IRB limits. Document provenance and construction.
3. **Quantitative materials.** Data (or access path), code, and documentation sufficient to regenerate
   reported results: master script + README + pinned versions + seeds.
4. **Qualitative transparency.** Make the analytic process inspectable — coding scheme, exemplar
   evidence, audit trail, reflexivity — rather than dumping raw transcripts. QDR supports controlled
   access where raw data are sensitive.

## When data cannot be shared

- **Explain why** (human-subjects confidentiality, IRB constraints, or data-provider restrictions such
  as state SLDS / district agreements).
- Give **access instructions** (application process, provider contact, restricted-use license).
- Where feasible, provide **synthetic or de-identified data** so analysis code can be exercised.

## Build-as-you-go checklist

- [ ] Reporting matches the AERA standard appropriate to the method (quant / qual)
- [ ] **Master script** regenerates every table/figure (quant) or analytic process documented (qual)
- [ ] **README**: provenance, construction, how to reproduce/inspect each exhibit
- [ ] **Seeds** set; software/package **versions pinned**
- [ ] Restricted data: rationale + access path + synthetic/de-identified substitute where feasible
- [ ] IRB/consent and confidentiality protections documented
- [ ] Preregistration / pre-analysis plan linked (anonymized) where applicable

## Anti-patterns

- Treating transparency as a post-acceptance afterthought
- "Data available on request" with no documented process or scope
- Dumping raw qualitative data instead of an inspectable analytic trail
- Claiming restriction without an access path or de-identified substitute
- Undocumented, un-seeded, unpinned code that "works on my machine"

## Transparency obligations by data type (AERJ referees)

AERA reporting standards and the Code of Ethics apply across traditions, but what "available for
reanalysis" means depends on the data. Match your obligation to the row below.

| Data type | What sharing/transparency means here | Common shortfall |
|-----------|--------------------------------------|------------------|
| Public-use survey (e.g., national longitudinal) | Code + documentation regenerating results | "Available on request" with no script |
| Restricted administrative (state/district) | Access path + license + synthetic substitute | Restriction claimed, no path given |
| Original qualitative | Coding scheme, exemplars, audit trail, reflexivity | Raw transcripts dumped or nothing shown |
| Mixed | Both quant materials and qual analytic trail | One strand documented, the other opaque |

## Worked transparency vignette (illustrative)

An AERJ policy/institutional study links a **state longitudinal data system** to a district intervention. The data
cannot be shared, so the transparency package states the reason (SLDS confidentiality and a data-use
agreement), gives the application path to the state agency, and ships **synthetic** data with the same
schema so the master script runs end to end. The README documents construction of every derived
variable and pins package versions; seeds are set so the illustrative **0.13 SD** estimate regenerates
exactly. A weak version would write "data restricted" and stop — leaving no way to inspect the logic
of inquiry the AERA standard requires.

## Referee pushback and the venue fix

- *"I can't verify the qualitative claims."* → Provide an inspectable analytic trail (coding scheme,
  exemplar evidence, reflexivity), not raw data.
- *"'Available on request' is not a plan."* → Replace with a documented access process and scope.
- *"Code won't run on my machine."* → Ship a master script, README, seeds, and pinned versions;
  confirm any policy wording against the journal's current submission guidelines.

## Output format

```
【Reporting standard met】empirical-social-science (quant/qual)? [Y/N]
【Data availability】shareable / access-path / synthetic? [which]
【Documentation】README + provenance + seeds + pinned versions? [Y/N]
【Qualitative transparency】coding + evidence + audit trail + reflexivity? [Y/N/NA]
【Restricted data】rationale + access + substitute?
【Next】aerj-review-process
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reproducibility tooling, QDR, preregistration registries
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — AERA reporting standards + Code of Ethics
