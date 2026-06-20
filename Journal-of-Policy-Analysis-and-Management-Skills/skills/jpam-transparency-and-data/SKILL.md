---
name: jpam-transparency-and-data
description: Use when preparing the replication / transparency materials for a Journal of Policy Analysis and Management (JPAM) manuscript — depositing data and code in a public repository so the reported results can be reproduced, with an honest exemption path for restricted administrative data. Prepares the package; it does not waive requirements.
---

# Transparency & Replication Data (jpam-transparency-and-data)

JPAM publishes program evaluations that often inform real spending decisions, so the evidence must be
**reproducible**. The journal expects authors to **archive the data and code** behind the reported
results in a suitable public repository, with a clear data-availability statement. Build the package as
you go so it does not stall acceptance — and plan early for the **restricted administrative data**
common in policy work. Verify the current wording in Wiley Authors / Research Exchange before upload
(检索于 2026-06-20；以官网为准).

## When to trigger

- Building the replication package (data + code + documentation)
- A manuscript is heading toward acceptance and materials are requested
- Data are restricted (administrative, IRB-protected, provider-licensed) and you need the exemption path
- Writing the data-availability statement

## What to prepare

1. **Public deposit.** Place the replication materials in a recognized repository (e.g., the project's
   ICPSR/openICPSR archive, Harvard Dataverse, OSF, or a journal-designated repository) with a
   persistent identifier — not a personal website or transient cloud link. Recent JPAM data-availability
   statements often use a JPAM/Harvard Dataverse repository, while Research Exchange controls the exact
   repository prompt.
2. **Reproduce every reported number.** A master script regenerates every table and figure from the
   raw/constructed data. Exhibit numbers in the manuscript match the package output exactly.
3. **Documentation.** A README covering data provenance, construction steps, software/package versions,
   seeds for stochastic steps, and the exact command to reproduce each exhibit.
4. **Data-availability statement.** State what is shared, where, and under what license; if data are
   restricted, state precisely why and how a replicator can obtain access.

## Restricted administrative data (the policy-research case)

Policy evaluation often runs on linked administrative or survey microdata that **cannot** be posted.
JPAM's transparency expectation is met honestly by:

- **Explaining the restriction** (legal, IRB, data-provider license) in the data-availability statement.
- **Providing access instructions** — the application process, provider contact, and approximate timeline
  so an independent replicator could obtain the same data.
- **Posting all code** plus any shareable derived/aggregated files and, where feasible, **synthetic or
  simulated data** that let the code run end-to-end.

## Build-as-you-go checklist

- [ ] One master script regenerates **every** table and figure
- [ ] README: provenance, construction, versions, seeds, per-exhibit reproduction steps
- [ ] Software/package versions pinned (`renv.lock` / `requirements.txt` / recorded installs)
- [ ] Manuscript exhibit numbers match the package output exactly
- [ ] Public repository with a persistent identifier chosen (journal-designated where specified)
- [ ] Data-availability statement drafted
- [ ] Restricted data: restriction explained + access path + synthetic data where feasible

## Anti-patterns

- Treating the package as a post-acceptance afterthought (it can gate publication)
- Depositing code that does not actually reproduce the printed tables/figures
- A personal URL or expiring cloud link instead of a persistent repository
- Claiming data are restricted with no access path or synthetic substitute
- Undocumented, un-seeded, unpinned code that only "works on my machine"

## Calibration anchors (hedged)

- Policy evaluations lean heavily on **restricted administrative data**; an honest restriction note plus
  a real access path and runnable code on synthetic/derived data is the expected, accepted route — not a
  loophole to skip transparency.
- The exact deposit requirement, repository prompt, and reproduction-check workflow can change; confirm
  the current data-policy wording in Wiley Authors / Research Exchange.
- Build the package alongside the analysis: retrofitting reproducibility after acceptance is where
  policy papers stall.

## Worked micro-example (illustrative)

A welfare-reform evaluation uses linked state UI and TANF records that cannot be posted. The package
still meets the bar: a **data-availability statement** explains the licensing restriction and names the
state agency's data-request process and timeline; **all code** is deposited with a master script; a
**synthetic dataset** matching the variable structure lets a replicator run the full pipeline; and
shareable **aggregated tables** are included. An independent researcher could obtain the real data and
reproduce every number. (Illustrative.)

## Output format

```
【Repository】public archive + persistent ID — chosen? [Y/N]
【Reproduces results?】master script verified locally? [Y/N]
【Documentation】README + provenance + seeds + pinned versions? [Y/N]
【Restricted data?】restriction explained + access path + synthetic data?
【Data-availability statement】drafted? [Y/N]
【Next】jpam-review-process
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — JPAM data/replication policy evidence and repository guardrails
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — repositories and reproducibility tooling for restricted-data projects
