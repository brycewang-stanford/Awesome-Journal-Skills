---
name: jpart-transparency-and-data
description: Use when preparing the data and replication materials for a Journal of Public Administration Research and Theory (JPART) manuscript. JPART requires authors, where ethically possible, to publicly release all data and software code as a condition of publication, with a mandatory Data Availability Statement. Prepares the package; it does not waive requirements.
---

# Transparency & Data Policy (jpart-transparency-and-data)

JPART does not merely encourage sharing — it **requires** authors, *where ethically possible*, to
**publicly release all data and software code underlying the published paper as a condition of
publication**, and every paper must carry a **Data Availability Statement**. Build the package as you go
so acceptance does not stall on materials.

## When to trigger

- Building the reproducibility/replication package and the Data Availability Statement
- A manuscript is heading toward acceptance and you need materials in shareable form
- Data cannot be fully shared (privacy, ethics, legal/provider restrictions) and you need the exemption path
- Preparing or linking a **preregistration / pre-analysis plan** (JPART accepts blinded pre-reg reports)

## What JPART requires (verify current wording on the policy page)

1. **Public release of data and code.** As a condition of publication, release the data and the software
   code that produced the results — in a trusted, citable public repository with a persistent identifier
   (e.g., a Dataverse or OSF deposit), not a personal website or transient cloud link.
2. **Data Availability Statement.** A mandatory statement in the manuscript describing what is available,
   where, and under what access terms.
3. **Reproducible materials.** Data, code, and documentation sufficient to regenerate every reported
   result: a master script + README + pinned versions + seeds.
4. **Preregistration where applicable.** For experiments, link the (blinded) pre-analysis plan and mark
   confirmatory vs. exploratory analyses; the journal accepts blinded pre-reg reports for review.

## When data cannot be shared (exemption path)

- **Explain why** in the Data Availability Statement (ethical/privacy concerns or provider restrictions).
- Provide **README instructions on exactly how others can obtain the data** (access process, contact).
- Where possible, **provide synthetic data** resembling the restricted data so the code can be run.
- Exemptions typically require **explicit editor approval** — do not assume a quiet opt-out.

## Build-as-you-go checklist

- [ ] One **master script** regenerates **every** table and figure from raw/constructed data
- [ ] **README** documents data provenance, construction steps, and how to reproduce each exhibit
- [ ] **Seeds** set and reported for every stochastic step
- [ ] Software/package **versions pinned** (`renv.lock` / `requirements.txt` / recorded installs)
- [ ] Exhibit numbers in the manuscript **match** the package output exactly
- [ ] **Data Availability Statement** drafted (what / where / access terms)
- [ ] Public deposit prepared in a citable repository with a persistent identifier
- [ ] Restricted data: exemption note + access instructions + synthetic data + editor approval where needed
- [ ] Preregistration / pre-analysis plan linked (blinded) where applicable

## Anti-patterns

- Treating the deposit as a post-publication afterthought (release is a condition of publication)
- Depositing code that does not actually reproduce the printed tables/figures
- A personal URL instead of a trusted citable repository
- Claiming data are restricted without an access path, synthetic substitute, or editor approval
- Undocumented, un-seeded, unpinned code that "works on my machine"

## Output format

```
【Data + code release】public, citable repository staged? [Y/N]
【Reproduces tables/figures?】master script verified locally? [Y/N]
【Data Availability Statement】drafted? [Y/N]
【Documentation】README + provenance + seeds + pinned versions? [Y/N]
【Restricted data?】exemption note + access path + synthetic data + editor approval?
【Preregistration】linked (blinded) where applicable? [Y/N/NA]
【Next】jpart-review-process
```

## Supplementary resources

- [`../../resources/code/`](../../resources/code/) — master-script + reproducible skeleton to adapt
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — repositories, preregistration, reproducibility tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — data-and-code release policy + Data Availability Statement
