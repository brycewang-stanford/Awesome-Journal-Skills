---
name: sf-data-and-transparency
description: Use when preparing the data, code, and transparency materials for a Social Forces (SF) manuscript. SF requires a data availability statement on every published paper and encourages deposit in a public repository where ethically feasible. Covers quantitative and qualitative transparency and restricted-data paths; it does not waive requirements.
---

# Data & Transparency (sf-data-and-transparency)

Social Forces makes one transparency requirement explicit: **"The inclusion of a data availability
statement is a requirement for papers published in the Journal."** Unlike journals that run an
editor-verified pre-publication replication, SF asks for a clear **statement** plus deposit **where
ethically feasible**. Treat the statement as a real deliverable and build the materials as you go so it
is honest and complete.

## When to trigger

- Drafting the **data availability statement** (required for publication)
- Deciding where and how to deposit data and code
- Data cannot be fully shared (privacy, ethics, legal/provider restrictions) and you need the right wording
- Documenting qualitative or restricted sources to support the claims

## What SF requires (verify current wording on the policy page)

1. **Data availability statement.** Every published paper carries one. It should describe whether and
   how the data underlying the results are available — repository name, persistent identifier or
   accession number, or the access process for restricted data.
2. **Deposit where ethically feasible.** Authors are encouraged to deposit data (and ideally analysis
   code) in a **public repository** with persistent identifiers — e.g., openICPSR, Harvard Dataverse,
   OSF, Zenodo. This is encouraged, not a journal-run verification step (待核实 on any evolving policy).
3. **Documentation that supports reproducibility.** A master script + README + pinned versions + seeds,
   so the reported tables and figures can in principle be regenerated.

## When data cannot be shared (restricted-data path)

- **Explain why** in the statement (ethical/privacy concerns or legal restrictions by the provider).
- Give **access instructions**: the application/enclave process and provider contact, so a reader could
  in principle obtain the same data.
- Where possible, provide **synthetic or simulated data** so the code can be run end to end.

## Qualitative / restricted transparency

- Document interviews, fieldnotes, and archival sources in a form that supports the claims (evidence
  tables, annotated sources), with access controls where confidentiality requires them.
- Consent should cover **publication of the data**, and identifying details should be anonymized.

## Build-as-you-go checklist

- [ ] **Data availability statement** drafted (availability + identifier/accession or access process)
- [ ] One **master script** regenerates **every** table and figure from raw/constructed data
- [ ] **README** documents provenance, construction steps, and how to reproduce each exhibit
- [ ] **Seeds** set and reported; software/package **versions pinned**
- [ ] Restricted data: reason + access path + synthetic substitute where feasible
- [ ] Exhibit numbers in the manuscript **match** the deposited/declared materials

## Anti-patterns

- Writing the data availability statement as a one-line afterthought at proofs
- Saying "data available on request" with no repository, identifier, or real process
- Claiming data are restricted without giving an access path or synthetic substitute
- Depositing code that does not actually reproduce the reported tables/figures
- Over-stating SF's policy as an editor-run replication mandate when it is a statement + encouraged deposit

## Choosing the right data-availability path

Social Forces spans survey, administrative, demographic, qualitative, and restricted-access data, so the
statement has to match the data type honestly. A routing table:

| Data situation | Statement should say | Repository / mechanism |
|----------------|----------------------|------------------------|
| Public survey (GSS/PSID style) | Where to download + wave | Cite source; deposit construction code |
| Author-collected, shareable | Deposited with persistent ID | openICPSR, Dataverse, OSF, Zenodo |
| Restricted administrative | Why restricted + enclave path | Provider process; synthetic substitute |
| Qualitative / interviews | What is documented + consent limits | Evidence tables; access controls |

Calibration (hedged): SF requires a data availability statement and encourages deposit where ethically
feasible — not an editor-run pre-publication replication. Confirm wording against current guidelines.

## Worked vignette (illustrative)

A panel study of educational stratification links restricted administrative records to a public survey.
The honest statement names the public survey and wave (downloadable), notes the linked records are
reachable only through the provider's secure enclave with the application contact, and points to a
synthetic analytic file plus master script on OSF so a reader can run the pipeline end to end — public
where possible, a documented access path where not, a runnable substitute throughout.

Referee fixes: "'available on request' is not enough" → name a repository or access process;
"code does not reproduce Table 3" → ship a master script that regenerates every declared exhibit.

## Output format

```
【Data availability statement】drafted? availability + identifier/access path? [Y/N]
【Deposit】public repository + persistent ID (where feasible)? [Y/N/NA]
【Reproduces tables/figures?】master script verified locally? [Y/N]
【Documentation】README + provenance + seeds + pinned versions? [Y/N]
【Restricted data?】reason + access path + synthetic data?
【Next】sf-review-process
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — repositories, reproducibility tooling, qualitative-transparency options
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — data availability statement requirement and deposit encouragement
