---
name: ngeo-methods
description: Use when building the online Methods section of a Nature Geoscience manuscript so every quantitative Earth-science claim is grounded in data, model diagnostics, and quantified uncertainty. Structures Methods and the reproducibility layer; does not design figures or frame the headline result.
---

# Nature Geoscience Methods (ngeo-methods)

## When to trigger

- Your main text is carrying instrument, sampling, or model-configuration detail that belongs online
- You cannot tell what a reader *needs in the main text* versus what belongs in online Methods
- Referees of a prior draft asked how a number was derived or how uncertainty was propagated
- The Article is over length and Methods-type material is a prime relocation target
- You are unsure how to state data and code availability

## The Nature Methods architecture

Nature Geoscience separates the main text from an **online Methods** section (placed after the main text, divided by topical subheadings; verify current length allowances). The division of labor:

- **Main text** carries only what a broad reader needs to *believe and interpret* the headline advance: the essential approach, the decisive observational or model constraint, and the headline uncertainty.
- **Online Methods** carries the full, reproducible account: instruments and platforms, sampling and site selection, proxy calibration, model setup and forcing, statistical procedures, and the **complete uncertainty budget**.

The online Methods is not an appendix of leftovers — it is peer-reviewed in full and is where a specialist referee decides whether to trust the result.

## What every Nature Geoscience Methods must ground

| Claim type                          | Must appear in Methods                                          |
|-------------------------------------|-----------------------------------------------------------------|
| Field / lab measurement             | instrument, precision, sampling design, replication            |
| Remote-sensing / satellite product  | sensor, product version, retrieval, resolution, bias handling  |
| Proxy reconstruction                | calibration dataset, transfer function, age model, error       |
| Model result                        | model + version, resolution, forcing/boundary conditions, spin-up, ensemble |
| Any statistical inference           | test, assumptions, significance definition, multiple-comparison handling |
| Every headline number               | how uncertainty was estimated and propagated                   |

## Grounding without over-claiming (a Nat. Geosci. distinctive)

Nature Geoscience referees are sharp about the gap between what data show and what is inferred. Pre-empt the two signature objections **explicitly**:

- **"The model is not anchored to observations."** → State the observational validation in the main text and the full comparison in Methods. A model result with no data anchor is a classic desk-reject.
- **"The uncertainty is not quantified / not propagated."** → Give every headline number a stated uncertainty and describe the propagation in Methods. Separate measurement error, model spread, and structural uncertainty where they differ in kind.

## Data, code, and reproducibility statements

Nature Portfolio requires explicit statements — plan them here, not at submission:

- **Data availability**: deposit in a **community repository** where one exists (e.g. PANGAEA for Earth-system data, NCEI, IRIS/SAGE for seismology, GenBank for sequences), otherwise a general repository (Figshare, Dryad, Zenodo). State accession/DOI. "Available on request" alone is not sufficient for the underlying data.
- **Code availability**: custom code that generates the central results must be made available (repository + DOI, or at minimum to editors/referees); state it explicitly.
- **Reporting Summary**: the Nature Portfolio Reporting Summary accompanies submission (see `ngeo-submission`); its content must be consistent with Methods.

## Sentence patterns that buy referee trust

- **Validation clause (main text):** "Simulated surface fluxes reproduce the observed seasonal cycle to within X% (Methods, Fig. Sn)."
- **Split uncertainty:** "We estimate a rate of value ± (measurement) ± (model spread), the latter dominated by [source]."
- **Age-model flag (paleo):** "Ages are on the [framework] timescale; the reconstruction is robust to alternative age models (Methods)."
- **Ensemble one-liner:** "Results are consistent across all N ensemble members (Methods)."

## Checklist

- [ ] Main text keeps only what a broad reader needs to trust and interpret the advance
- [ ] Online Methods is divided by topical subheadings and is fully reproducible
- [ ] Every quantitative claim is grounded in data or a data-validated model
- [ ] Model results are explicitly anchored to observations
- [ ] The headline number carries a stated, propagated uncertainty
- [ ] Data availability names a repository + accession/DOI (community repo preferred)
- [ ] Code availability is stated for custom analysis code
- [ ] Methods are consistent with the Reporting Summary

## Anti-patterns

- Treating online Methods as a dumping ground rather than a reproducible protocol
- A model-only claim with no observational validation
- Headline numbers with no uncertainty, or measurement and model spread merged silently
- "Data available on request" as the only data statement
- Undefined proxy calibrations or unstated age models in paleoclimate work
- Methods that contradict the Reporting Summary or the availability statements

## Output format

```
【Main-text trust minimum】approach / decisive constraint / headline uncertainty
【Online Methods subheadings】list
【Model anchored to observations】yes / fix
【Headline uncertainty propagated】yes / fix
【Data availability】repository + DOI?  yes / fix
【Code availability】stated?  yes / fix
【Next】ngeo-figures (lead figure) or ngeo-supplementary (SI partition)
```

> Methods length allowances, repository lists, and reporting-summary requirements evolve — verify current Nature Geoscience / Nature Portfolio policy on the official author pages (Checked: 2026-07-16).
