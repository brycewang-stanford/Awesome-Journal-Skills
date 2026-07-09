---
name: imc-reproducibility
description: Use when strengthening ACM IMC reproducibility and availability evidence, covering the artifact-availability declaration, measurement provenance (vantage points, dates, tool versions), dataset release with schema, honest reproducibility for a moving Internet, the Replicability Track, and consistency between what the paper claims and what the released data contains.
---

# IMC Reproducibility

Use this before submission and again before camera-ready. IMC treats availability and
reproducibility as scored dimensions, not courtesies: the submission carries an
**artifact-availability declaration**, accepted papers are shepherded to deliver it, and IMC runs a
dedicated **Replicability Track**. The goal is that a competent reader could rebuild your analysis
from the released data — and re-run your *method* to gather comparable new data — and reach your
conclusions.

## The moving-Internet reality

Measurement differs from lab science: **you cannot re-collect the same data**, because the network
changes between runs. So reproducibility at IMC splits in two:

- **Analysis reproducibility:** the released dataset + scripts regenerate every figure and number
  in the paper. This you can and must make turnkey.
- **Method reproducibility:** the tooling and documented vantage-point setup let someone re-run the
  measurement to obtain *comparable* (not identical) data. This is what enables replication.

Say which you provide, and never present method reproducibility as if it reproduced your exact
numbers.

## Evidence map

- Map each finding, claim, and reported number to a **verifiable location** — a paper section, a
  figure generated from released data, or a script in the artifact.
- For the measurement, document **vantage points** (locations, ASes, probe types), **timing**
  (dates, durations, cadence), **targets** (lists with capture dates), **tools** (versions,
  configs), and **sampling/rate limits**.
- Keep the **availability declaration** truthful and specific: what is shared, where, and — if
  something cannot be shared — exactly why (privacy, proprietary, legal).
- Keep the paper and the released data **consistent**: a number in the PDF that no script produces
  from the released data is read as carelessness.

## Availability declaration audit

| Claim in the paper | Weak answer | IMC-ready answer |
|---|---|---|
| "We scan N hosts" | "Data available on request" | Released dataset (or privacy-safe derivative) + scan metadata + scripts |
| "Measured from many vantage points" | Vantage points unnamed | Documented vantage-point table: locations, ASes, probe types, dates |
| "We observe behavior X over time" | Single-snapshot data | Time-stamped longitudinal data + the analysis window stated |
| "Our tool detects Y" | "Code will be released" | Released, runnable tooling with a README and a small example |
| "We used user/traffic data" | Nothing (privacy cited vaguely) | Aggregated/anonymized release + documented privacy method + ethics link |

## Provenance pinning

```text
[Vantage points] record every location/AS/probe-type, and quantify coverage bias
[Timing]         measurement dates, durations, cadence; state the analysis window
[Targets]        target/seed lists with capture dates; how they were sourced (and their stability)
[Tools]          exact tool versions and configs; rate limits and opt-out/blocklist handling
[Sampling]       inclusion/exclusion criteria and resulting sample sizes; how you handle churn
[Privacy]        the anonymization/aggregation applied before release, matching the Ethics section
```

## Degrees of reproducibility (state the one you achieved)

- **Turnkey analysis:** one documented command regenerates each figure/table from released data.
- **Scripted analysis:** scripts exist but need documented manual steps or restricted-data access.
- **Method-only:** the tooling and setup are released, but the data cannot be shared (privacy/legal)
  — a stranger can re-measure, not reproduce your exact numbers.

Aim turnkey for the analysis of any releasable dataset; when data is sensitive, provide a
privacy-safe derivative plus method-only reproducibility, and say so plainly.

## The Replicability Track

IMC runs a dedicated **Replicability Track** for work that reproduces or replicates prior
measurement results, entered via an **Expression of Interest** screened by a small committee, then
a full submission judged like the main track (priority to replicability over reproducibility). If
your contribution *is* re-measuring a prior study on today's Internet, this is the track — design
for a fair, documented re-run and an honest account of what changed and why.

## Consistency and camera-ready pass

- Before submission: every scored number traces to the (anonymized) artifact; the availability
  declaration matches reality; infrastructure is anonymized (no owner strings, AS/probe IDs, lab
  domains).
- Before camera-ready: swap anonymized links for permanent, DOI-issuing archives; finalize the
  documented schema and license; align with any Community Contribution Award intent
  (`imc-artifact-evaluation`).

## Output format

```text
[Claim inventory] <claim -> evidence location>
[Availability] full / partial / none, stated honestly (+ reason)
[Provenance gaps] <vantage points / timing / targets / tool versions / privacy>
[Reproducibility level] turnkey-analysis / scripted / method-only, stated honestly
[Paper fixes] <must appear in the PDF>
[Release fixes] <additions before upload / camera-ready>
```
