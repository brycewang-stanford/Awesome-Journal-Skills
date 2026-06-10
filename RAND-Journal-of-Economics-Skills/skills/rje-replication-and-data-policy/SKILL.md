---
name: rje-replication-and-data-policy
description: Use to assemble a reproducible replication package for a RAND Journal of Economics (RJE) industrial-organization manuscript and to handle RJE's supporting-information rules correctly — the journal discourages supplementary material and does not host data/code itself. Reflects what is and is NOT confirmed in RJE policy.
---

# Replication & Data Policy (rje-replication-and-data-policy)

## When to trigger

- Preparing data and code for an RJE submission or revision
- Deciding what (if anything) to attach as supporting information
- Confirming what RJE's data/code policy actually requires

## What RJE policy actually says (verified 2026-06-01)

Be precise, because RJE's posture differs from data-mandate journals:

- **No formal data/code-deposit (replication-package) requirement was located on any official RJE page.** The supplementary-material page (rje.org/sup-mat.html) addresses only **author-hosted supporting files**, not a mandated replication archive or Data Availability Statement. Treat a formal mandate as **unspecified — 待核实**; re-check the Wiley author guidelines and rje.org before relying on either presence or absence.
- **Supporting information is discouraged "as a general rule."** When provided, it is **hosted via author-maintained links (1999–2007) or through Wiley (2007–present)** — the journal **does not host materials directly** — is **posted online without editing or typesetting**, may be **assessed critically by reviewers**, and **may be declined**.

So: there is no openICPSR-style deposit step to plan for here (unlike AEA journals or the QJE Dataverse), but reproducibility still matters to referees, and anything you do attach is governed by the discouraging supporting-information rule.

## What to do anyway (IO reproducibility norms)

Build a clean package even absent a mandate — IO referees probe replicability of structural estimates:

- **One master script** (`run_all`) regenerating every table, figure, and counterfactual from the analysis data. Structural estimation is slow — cache intermediate objects, document expected runtime, and store converged parameter estimates.
- **Pin the environment:** record Stata `ssc`/`net` package versions, `requirements.txt` (`pyblp`, `linearmodels`), or `renv.lock`; report solver/optimizer settings and **random seeds / starting values** for non-convex objectives.
- **Document restricted data** (Nielsen/Kilts, FSRDC Census, CMS, proprietary firm data): describe access, provide construction code, and note what cannot be shared.
- **README** mapping each exhibit to the script and inputs that produce it.

## Handling supporting information (RJE-specific)

- Keep core results in the **article and appendix** (within the <=10-page appendix+references budget); do **not** park decisive results in supporting information the journal discourages and may decline.
- If you must include supporting files, **justify them**, expect they appear unedited/untypeset, and host per current Wiley practice.

## Restricted-data disclosure grid (common IO sources)

IO empirics lean on restricted data. For each, document the access path and the construction code sharable when the raw data cannot move.

| Data source | Typical IO use | What to document (sharable even if data are not) |
|---|---|---|
| Nielsen / Kilts (NielsenIQ) | Retail scanner demand | Kilts Center license; cleaning/aggregation code |
| FSRDC / Census microdata | Plant-level entry/exit, production | RDC approval, disclosure review, construction scripts |
| CMS / claims data | Health-insurance, provider markets | Data-use-agreement terms; variable derivations |
| Proprietary firm data | Auction bids, transaction prices | NDA scope; a synthetic stand-in for the demo run |

## Worked vignette: packaging a structural estimation

Suppose your article estimates a dynamic entry model on FSRDC data and demand on Nielsen data, with a slow GMM step:

- **`run_all`**: one master script runs demand, supply recovery, the dynamic step, and counterfactuals in order, with a flag to load cached results.
- **Caching with provenance**: store converged vectors, the objective value, and the seed/starting-value grid, so a referee verifies the optimum without re-solving.
- **Restricted data**: FSRDC data cannot leave the enclave — ship construction code plus a synthetic micro-extract so the pipeline runs.
- **Exhibit map**: a README mapping each exhibit to its script and input.

## Referee-pushback patterns and the venue fix

- **"I cannot tell whether GMM reached a global optimum."** Fix: report the objective at every start and ship the seed; cache the converged vector.
- **"The counterfactual is not reproducible from the code."** Fix: ensure `run_all` regenerates every counterfactual, not just estimation tables.
- **"You promise data you may use but not redistribute."** Fix: state the access path and provide construction code plus a synthetic stand-in; never imply you can release restricted data.
- **"Hosting is unclear given RJE hosts nothing."** Fix: plan author-maintained or Wiley-hosted links; confirm against the journal's current author guidelines.

## Anti-patterns

- Assuming an AER/QJE-style mandatory deposit exists at RJE (none confirmed — 待核实)
- Dumping core estimates into discouraged, possibly-declined supporting information
- An unreproducible structural pipeline with unrecorded seeds/starting values
- Promising to share restricted data you are not licensed to release

## Output format

```
【RJE mandate】formal deposit required? NOT confirmed (待核实) — verify on rje.org/Wiley
【Master script】run_all regenerates all exhibits + counterfactuals? [Y/N]
【Environment pinned】versions + seeds + starting values recorded? [Y/N]
【Restricted data】access + construction documented? [Y/N]
【Supporting info】minimal + justified (discouraged by RJE)? [Y/N]
【Next step】rje-submission
```
