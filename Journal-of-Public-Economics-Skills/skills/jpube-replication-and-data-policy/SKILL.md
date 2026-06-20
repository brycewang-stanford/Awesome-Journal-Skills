---
name: jpube-replication-and-data-policy
description: Use when assembling data and code for a Journal of Public Economics (JPubE) manuscript under Elsevier's Option C research-data framework — data-availability statements, repository deposit/citation/linking, restricted administrative data, and a reproducible package. It does not run the analysis.
---

# Replication & Data Policy (jpube-replication-and-data-policy)

## When to trigger

- You are preparing a data-availability statement or research-data declaration
- Your results rest on restricted tax/health/register data and you must document access
- You want a reproducible package that pre-empts referee replication requests
- You need to choose between repository deposit and a restricted-data access statement

## JPubE / Elsevier requirement

JPubE's Guide for Authors applies Elsevier **Option C** research-data instructions: deposit research
data in a relevant repository, cite and link the dataset in the article, or provide a statement
explaining why research data cannot be shared. For public-economics work using restricted tax, health,
or register microdata, the practical route is usually a data statement plus a code package and exact
access path rather than public release of protected rows.

## Build the package around Option C

Public-economics referees frequently ask to see the elasticity/bunching/RD pipeline, so build a clean
package around the data route:

- **Data-availability statement** matching reality: open data -> link the repository; restricted
  tax/health/register data -> state the access path, the agency, and why microdata cannot be shared.
- **Dataset citation/linking.** Cite open datasets in the reference list with repository, version, year,
  persistent identifier, and the `[dataset]` marker where applicable.
- **Programs even when microdata are proprietary.** Supply all cleaning and estimation code so the
  workflow is auditable even if IRS/SSA/CMS or register microdata cannot leave the enclave.
- **Disclosure compliance.** Document cell-size suppression and output-clearance for restricted data;
  never embed suppressed cells in shared outputs.
- **One master script** (`run_all`) regenerating every table and figure from inputs; pin
  software/package versions (`renv.lock`, `requirements.txt`, recorded `ssc` versions); set and report
  seeds for bootstrap / randomization inference.
- **README** mapping each exhibit to the script that produces it.

## Checklist

- [ ] Data-availability statement drafted and consistent with the data used
- [ ] Open data deposited, cited, and linked; restricted data explained with access path
- [ ] Restricted-data access path, agency, and sharing limits documented
- [ ] All cleaning + estimation programs supplied (even if microdata are restricted)
- [ ] Disclosure / cell-suppression compliance documented for shared outputs
- [ ] `run_all` master script regenerates all exhibits; versions and seeds pinned
- [ ] README maps exhibits -> scripts
- [ ] Current JPubE/Elsevier data fields checked in Editorial Manager before upload

## Anti-patterns

- Treating Option C as optional boilerplate rather than a repository link or a concrete reason data
  cannot be shared
- A data-availability statement that does not match what was actually used
- Sharing restricted-data outputs without documented disclosure clearance
- A package with no master script, unpinned versions, or unreported seeds

## Data-availability routing by source

Public-finance papers lean on restricted microdata more than most fields, so the availability statement
is rarely "open repository." Route by what you actually used.

| Data source | Availability statement says | What you still ship |
|-------------|------------------------------|----------------------|
| Public tax/SOI tabulations, survey extracts | Link repository (Mendeley/openICPSR/Zenodo) and cite dataset | Data + all code |
| IRS/SSA/CMS enclave microdata | Access path + agency + why microdata cannot leave | All cleaning + estimation code |
| European whole-population registers | Application route, custodian, approval ID | Code + non-disclosive aggregates |
| Mixed (public + restricted) | Split the statement by component | Repository for the open part, access note otherwise |

## Worked vignette: a register-DID package referees can trust

A social-insurance reform evaluated on a national register cannot share person-level rows. The package
still makes the DID pipeline auditable: `run_all` regenerates every exhibit from cleared aggregates; the
README maps Table 3 (the moral-hazard wedge) and Figure 2 (the event study) to their scripts;
`renv.lock` pins versions; the bootstrap seed is fixed so the SEs on the **MVPF = 1.4** statistic
(illustrative) replicate. The availability statement names the custodian, the approval ID, and the
cell-suppression rule (min count 10), so a referee sees the workflow without touching protected
microdata.

## Calibration anchors

- The reproducibility bar a JPubE referee imagines: could a second analyst, given the same authorized
  access, rebuild every elasticity/MVPF/bunching number? Code completeness and exact access
  documentation are what you control.
- Option C is about deposit/citation/linking or a sharing explanation; it is not the same as promising a
  named AEA-style data-editor code run.

## Output format

```
【Data type】open / restricted-administrative / register / mixed
【Availability statement】drafted + consistent? [Y/N]
【Restricted access】path + agency + limits documented? [Y/N]
【Programs supplied】all cleaning + estimation code? [Y/N]
【Reproducibility】run_all + pinned versions + seeds? [Y/N]
【Policy check】Option C route and Editorial Manager data fields checked? [Y/N]
【Next step】jpube-review-process
```
