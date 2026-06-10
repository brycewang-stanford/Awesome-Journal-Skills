---
name: rof-replication-and-data-policy
description: Use when preparing the Review of Finance (RoF) replication package — code, data, pseudo-datasets for proprietary sources such as Datastream or Bankscope, log files, the Data Availability Statement, dataset citations, cover-letter exception requests at initial submission, and OUP supplementary hosting, since the journal's code-sharing policy can hold publication until programs are received.
---

# Review of Finance Replication And Data Policy

Use this before submission and after acceptance. Reopen the current RoF code-sharing and
data-availability policy before final packaging.

## Package checklist

- Prepare replication programs with comments, software names, versions, package dependencies,
  and execution order.
- Provide actual data when non-proprietary. If data are proprietary, prepare a pseudo-dataset
  plus log files or other evidence required by current policy.
- Draft a Data Availability Statement and formatted dataset citations.
- Request any exception in the cover letter at initial submission when policy requires early
  disclosure.
- Expect publication to wait until code is received when the policy applies.
- Package materials for OUP supplementary hosting rather than inventing a separate archive.

## RoF replication packet

Build the packet around editorial risk:

- `README` states execution order, software, package versions, expected runtime, and output locations.
- `data_manifest` names every raw, intermediate, pseudo, and restricted dataset, with access status.
- `run_all` recreates each table, figure, and appendix exhibit or clearly marks non-runnable restricted
  steps.
- `logs` prove that the submitted outputs were generated from the submitted programs.
- `DAS` and dataset citations match the manuscript, cover letter, and supplementary files.

For proprietary data, the pseudo-dataset is not decoration. It should let the editor see variable names,
file structure, merge keys, and code flow, while logs or other evidence document the confidential run.
Request exceptions at the earliest required stage; late exceptions create publication risk.

## OUP supplementary package blueprint

```text
rof_replication/
  README.md            run order, software + versions, runtime, output map
  data/raw/            non-proprietary inputs only, with dataset citations
  data/pseudo/         simulated rows mirroring restricted files (schema-true)
  code/01_build        cleaning: return screens, merges, winsorizing
  code/02_main         every body table and figure, numbered as in the paper
  code/03_appendix     internet-appendix exhibits
  logs/                full execution logs from the confidential run
  output/              regenerated exhibits, traceable to the submitted PDF
```

## Finance-data shipping reality

| Source | Ships in the package? | What ships instead |
|---|---|---|
| CRSP / Compustat (WRDS) | No — licensed | exact query, extraction date, variable list, pseudo-rows |
| Datastream / Refinitiv | No | request scripts, screen list incl. dead-stock handling, pseudo-data |
| Bankscope / Orbis (BvD) | No; vintages also vanish | vintage date, consolidation filters, ID list if the license allows |
| ECB SDW / Eurostat | Usually yes | series codes plus download date, or the snapshot itself |
| Hand-collected (filings, prospectuses) | Yes — expected | the dataset plus the collection protocol |
| Proprietary (exchange, supervisor, bank) | No | pseudo-dataset, logs, access procedure, exception named in the cover letter |

Confirm the current shipping rules for each source against the journal's current author
guidelines and your own license terms before promising anything in the DAS.

## Vintage and version control

- BvD products overwrite history: pin the Orbis/Bankscope vintage in the README and store
  per-table row counts so the editor's office can audit drift in any re-pull.
- WRDS tables are backfilled; record extraction dates next to every query.
- Pin software environments (Stata version plus ado dates, renv or requirements files);
  the expectation behind RoF's policy is that the editorial side can execute the package,
  not reverse-engineer it.

## Pre-acceptance dry run

- Clone the package to a clean machine or container and run only what the README says —
  no tribal knowledge allowed.
- Trace every number in the submitted PDF to a line in `output/`; anything untraceable is
  either a stale exhibit or a missing script.
- Run the pseudo-data through the full code path: identical merge keys, variable types,
  and column order, so structure errors surface before the editor finds them.
- Reconcile four documents — manuscript DAS, cover letter, README, dataset citations
  (Chicago style, matching the manuscript's reference format) — into one consistent story.

## Worked exception case

Illustrative. A microstructure paper combines proprietary order-book data from a European
exchange with public Datastream prices. The packet ships: complete code; a pseudo
order-book with the true schema and fabricated quantities; logs from the confidential run;
Datastream request scripts; a cover-letter paragraph requesting the exception at initial
submission — the stage RoF requires — citing the exchange's redistribution restriction;
and a DAS routing readers to the exchange's access procedure. Publication then waits only
on packet verification, not a post-acceptance scramble. Verify the exact exception
mechanics against the journal's current author guidelines.

## Output format

```text
[Replication status] ready / needs fixes / exception needed
[Data status] public / proprietary / restricted / simulated
[Code status] complete / missing pieces / undocumented
[DAS] <draft or missing>
[Publication risk] <low/medium/high>
```
