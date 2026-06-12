---
name: jpube-replication-and-data-policy
description: Use when assembling data and code for a Journal of Public Economics (JPubE) manuscript under Elsevier's research-data framework — data-availability statements, repository options, restricted administrative data, and a reproducible package. Reflects what is verified and flags what is 待核实; it does not run the analysis.
---

# Replication & Data Policy (jpube-replication-and-data-policy)

## When to trigger

- You are preparing a data-availability statement or research-data declaration
- Your results rest on restricted tax/health/register data and you must document access
- You want a reproducible package that pre-empts referee replication requests
- You are unsure exactly what JPubE requires versus what Elsevier requires

## What is verified vs. 待核实

**Verified:** JPubE is an Elsevier journal and follows **Elsevier's general research-data sharing framework** — manuscripts ordinarily include a **data-availability / research-data statement**, with options to link a repository (e.g., Mendeley Data, ICPSR/openICPSR, Zenodo) or to explain why data cannot be shared.

**待核实:** A binding, JPubE-*specific* mandatory data-and-code **deposit-and-verification** policy (analogous to the AEA Data Editor's reproducibility check, with a named data editor and a pre-publication code run) was **not confirmed** — the official Guide for Authors on ScienceDirect returned HTTP 403 to direct fetching at access time (2026-06-01). Treat any claim of a mandatory JPubE deposit/verification step as **待核实** and confirm the current requirement on the official Guide for Authors before relying on it. Do not assert a deposit mandate this pack could not verify.

## Build the package regardless

Public-economics referees frequently ask to see the elasticity/bunching/RD pipeline, so build a clean package whether or not a deposit is mandatory:

- **Data-availability statement** matching reality: open data → link the repository; restricted tax/health/register data → state the access path, the agency, and why microdata cannot be shared.
- **Programs even when microdata are proprietary.** Supply all cleaning and estimation code so the workflow is auditable even if IRS/SSA/CMS or register microdata cannot leave the enclave.
- **Disclosure compliance.** Document cell-size suppression and output-clearance for restricted data; never embed suppressed cells in shared outputs.
- **One master script** (`run_all`) regenerating every table and figure from inputs; pin software/package versions (`renv.lock`, `requirements.txt`, recorded `ssc` versions); set and report seeds for bootstrap / randomization inference.
- **README** mapping each exhibit to the script that produces it.

## Checklist

- [ ] Data-availability statement drafted and consistent with the data used
- [ ] Restricted-data access path, agency, and sharing limits documented
- [ ] All cleaning + estimation programs supplied (even if microdata are restricted)
- [ ] Disclosure / cell-suppression compliance documented for shared outputs
- [ ] `run_all` master script regenerates all exhibits; versions and seeds pinned
- [ ] README maps exhibits → scripts
- [ ] Current JPubE/Elsevier data requirement re-checked on the official page (待核实 items)

## Anti-patterns

- Asserting a specific JPubE deposit mandate this pack could not verify (it is 待核实)
- A data-availability statement that does not match what was actually used
- Sharing restricted-data outputs without documented disclosure clearance
- A package with no master script, unpinned versions, or unreported seeds

## Data-availability routing by source (decision grid)

Public-finance papers lean on restricted microdata more than most fields, so the availability statement is rarely "open repository." Route by what you actually used.

| Data source | Availability statement says | What you still ship |
|-------------|------------------------------|----------------------|
| Public tax/SOI tabulations, survey extracts | Link repository (Mendeley/openICPSR/Zenodo) | Data + all code |
| IRS/SSA/CMS enclave microdata | Access path + agency + why microdata cannot leave | All cleaning + estimation code |
| European whole-population registers | Application route, custodian, approval ID | Code + non-disclosive aggregates |
| Mixed (public + restricted) | Split the statement by component | Repository for the open part, access note otherwise |

## Worked vignette: a register-DID package referees can trust (illustrative)

A social-insurance reform evaluated on a national register cannot share person-level rows. The package still makes the DID pipeline auditable: `run_all` regenerates every exhibit from cleared aggregates; the README maps Table 3 (the moral-hazard wedge) and Figure 2 (the event study) to their scripts; `renv.lock` pins versions; the bootstrap seed is fixed so the SEs on the **MVPF = 1.4** statistic (illustrative) replicate. The availability statement names the custodian, the approval ID, and the cell-suppression rule (min count 10), so a referee sees the workflow without touching protected microdata.

## Calibration anchors

- The reproducibility bar a JPubE referee imagines: could a second analyst, given the enclave access, rebuild every elasticity/MVPF/bunching number? Code completeness — not data shipment — is what you control.
- Hedge: whether JPubE runs a named-data-editor verification step (AEA-style) is **待核实**; do not promise or assume one — confirm the current Elsevier/JPubE requirement on the official Guide for Authors before relying on it.

## Output format

```
【Data type】open / restricted-administrative / register / mixed
【Availability statement】drafted + consistent? [Y/N]
【Restricted access】path + agency + limits documented? [Y/N]
【Programs supplied】all cleaning + estimation code? [Y/N]
【Reproducibility】run_all + pinned versions + seeds? [Y/N]
【Policy check】JPubE/Elsevier requirement re-verified (待核实)? [Y/N]
【Next step】jpube-review-process
```
