---
name: imc-experiments
description: Use when designing or auditing ACM IMC measurements, covering representative vantage points, honest ground truth, longitudinal design for a moving Internet, safe and ethical active measurement, coverage-bias quantification, provenance pinning, and matching the measurement to the shape of each claim about the real Internet.
---

# IMC Measurements

Use this before submission when the measurement design is not yet locked. IMC reviewers are
measurement empiricists; the study is where a good question is won or lost. The organizing
principle is **evidence proportional to a claim about the real Internet** — the measurement must
observe the thing the paper asserts, from vantage points and over a period a skeptic would accept,
and it must be collected safely and ethically.

## Design audit

- **Match the measurement to the claim shape.** A claim about *reachability in the wild* needs many
  real vantage points; a claim about *deployment* needs coverage of the population; a claim about
  *behavior over time* needs a dated longitudinal window; a claim about *security* needs validated
  ground truth. A snapshot from two hosts cannot support a wild-Internet claim.
- **Choose vantage points for representativeness, not convenience.** Name locations, ASes, and
  probe types; argue why they support the claim; and **quantify the coverage bias** you cannot
  remove (e.g., volunteer probes over-representing certain regions).
- **Get ground truth right.** For detection/labeling claims, state where the labels come from and
  validate a subsample against an independent source; report the residual error.
- **Design for a moving Internet.** Instrument for churn, diurnal effects, load-balancing, CDN and
  anycast behavior, and path changes. Decide before collecting what a change over time would mean.
- **Make active measurement safe and ethical** (see the safety block) — this is inseparable from
  the design at IMC, not a compliance afterthought.
- **Pin provenance** so the measurement can be re-run as a *method* and its data reproduced as an
  *analysis* (`imc-reproducibility`).

## Claim-to-evidence design table

| Claim about the Internet | Matching evidence | Reject pattern avoided |
|---|---|---|
| "Reachable/blocked in the wild" | Many real vantage points across networks/regions, dated | "Two hosts stood in for the Internet" |
| "Widely deployed" | Population-scale coverage with stated sampling | "Convenience sample, claimed universal" |
| "Behavior changes over time" | Dated longitudinal window with stability analysis | "Single snapshot presented as a trend" |
| "We detect/measure X accurately" | Validated ground-truth subsample + error bounds | "No ground truth; labels unvalidated" |
| "This vantage point is representative" | Coverage-bias quantified vs. the target population | "Bias assumed away" |

## Ethical and safe active measurement

At IMC this is design, and it is a review gate (`imc-submission`):

```text
[Do no harm]   rate-limit probes; avoid overloading targets or intermediary networks
[Opt-out]      honor blocklists and abuse contacts; provide a clear opt-out and project page
[Human data]   for traffic/DNS/user data, obtain IRB approval/exemption; minimize and anonymize
[Belmont]      argue respect for persons (consent where owed), beneficence (risk vs. benefit),
               justice (who bears risk vs. benefits)
[Disclosure]   for vulnerability/exposure findings, plan responsible disclosure and a timeline
[Consent]      for volunteer vantage points, obtain informed consent and protect participants
```

## Provenance floor for measurement studies

- Record every **vantage point** (location, AS, probe type) and quantify coverage.
- Record **timing**: measurement dates, durations, cadence, and the analysis window.
- Record **targets**: seed/target lists with capture dates and how they were sourced.
- Record **tools**: exact versions, configs, rate limits, and opt-out handling.
- Archive the **captured data**, not just the query — the Internet will have changed by re-run.

## Vignette: measuring protocol deployment

Suppose the paper claims a protocol is widely deployed. The matching plan: scan (or query a
platform for) a population-scale target set with stated inclusion criteria; run from vantage points
whose coverage you quantify; date every scan and repeat over a window to show stability; validate a
subsample of "deployed" classifications against an independent signal; handle churn and duplicates
explicitly; and document the probing safety design in the Ethics section — every number traceable
to a dated, provenanced capture in the released dataset.

## Reporting floor

- Confidence intervals for rate/proportion estimates; say what they represent and the sample size.
- Coverage and its bias, stated quantitatively, for every vantage-point-based claim.
- Measurement dates and windows for every temporal claim.
- The compute/probe budget and any rate limits actually used.

## Output format

```text
[Measurement readiness] strong / adequate / weak
[Claim -> evidence map] <claim: vantage points / window / ground truth / statistic>
[Representativeness] <vantage points named? coverage bias quantified?>
[Ethics/safety] <active-measurement safety + IRB + disclosure handled? yes/no>
[Provenance] <vantage points / timing / targets / tool versions pinned? yes/no>
[Decision-critical next run] <one measurement to add or extend>
```
