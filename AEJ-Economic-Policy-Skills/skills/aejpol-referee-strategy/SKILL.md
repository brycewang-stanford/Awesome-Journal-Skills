---
name: aejpol-referee-strategy
description: Use when anticipating how AEJ: Economic Policy referees and editors will read a manuscript, before submission or before an R&R, to pre-empt the objections that sink policy-evaluation papers. Maps likely pushback to fixes and calibrates expectations; it does not write the response letter (see aejpol-rebuttal) or fix the identification.
---

# Referee Strategy — Reading the Manuscript as an AEJ: Policy Referee (aejpol-referee-strategy)

## When to trigger

- Before submitting: you want to find the objections a referee will raise first
- Deciding whether the paper is ready or needs another round of work
- Calibrating expectations about the AEA single-blind process and timeline
- Triaging which weaknesses to fix vs. disclose before submission

## How AEJ: Policy referees read

AEJ: Policy reviews are **single-blind** through the AEA system (referees see the authors; authors do not see referees), refereed by economists who expect both **credible causal evidence** and a **policy-relevant welfare reading**. A referee typically tests four things in order; a paper dies at the first one it fails:

1. **Is it a policy paper of broad interest?** (the `aejpol-topic-selection` test) — a clean estimate with no policy lever or welfare reading invites a "better suited to a field journal / AEJ: Applied" rejection.
2. **Is the causal claim credible?** (the `aejpol-identification` test) — staggered TWFE, asserted parallel trends, a weak instrument, or an over-generalized RDD are the usual kill shots.
3. **Does the welfare/policy reading follow?** (the `aejpol-theory-model` test) — a hand-waved "this is welfare-improving" or a sufficient-statistic formula whose assumptions are violated.
4. **Is it robust and reproducible?** (the `aejpol-robustness` / `aejpol-replication-package` tests).

### Pre-empting the predictable objections

| Likely referee objection | Pre-emption to build before submitting |
|---|---|
| "This isn't a policy paper / not broad-interest" | Lead with the policy question + welfare stake; state the cost-benefit reading in the abstract |
| "Staggered TWFE is biased here" | Heterogeneity-robust DID + Bacon decomposition + flat leads, in the main paper |
| "Parallel trends is assumed, not shown" | Event-study leads + honest-DID bounds |
| "Exclusion restriction is not credible" | Institutional + theoretical defense + falsification |
| "The welfare claim is hand-waved" | Explicit sufficient-statistic / MVPF / cost-benefit derivation |
| "External validity is unclear" | Heterogeneity by setting; explicit scope of the policy lesson |
| "Effect is significant but tiny / not policy-relevant" | Benchmark the magnitude against budget / status quo |
| "Not reproducible / data unavailable" | AEA-compliant package + restricted-data access path ready |

### Calibrating expectations
- AEA review is thorough; expect a small number of detailed referee reports and an editor letter. Plan for an R&R rather than a clean accept.
- Decide in advance which objections you will *fix* (identification, robustness) vs. *bound and disclose* (external validity, a calibrated welfare parameter). Disclosing a limitation precisely is stronger than hiding it.

## Checklist

- [ ] The "is this a policy paper?" objection is pre-empted on page one
- [ ] The single most likely identification objection has a main-text answer (not relegated to the appendix)
- [ ] The welfare reading is derived, not asserted
- [ ] Each predictable objection is mapped to an exhibit or paragraph that answers it
- [ ] Limitations you cannot fix are bounded and disclosed precisely
- [ ] Reproducibility is ready before the editor asks

## Anti-patterns

- Submitting hoping referees will not notice the staggered-TWFE / pre-trends problem
- Hiding a known limitation instead of bounding and disclosing it
- A welfare claim with no derivation, trusting the referee to grant it
- Putting the decisive robustness check only in an online appendix the referee may skip
- Mis-calibrating to a generic-journal process and ignoring AEA single-blind norms

## Worked vignette (illustrative)

An education-policy paper using a funding-formula RDD anticipates three objections: (1) "local estimate only" → states the estimand and argues the threshold population is the marginal policy population; (2) "manipulation at the cutoff" → CJM density test + donut RDD; (3) "no welfare reading" → translates the test-score effect into a cost-per-standard-deviation and compares to class-size policies. All three answers are in the main text, so no referee can raise them as fatal.

## Output format

```
【Broad-interest verdict】would a referee call this a policy paper? [Y/N + fix]
【Top identification objection】+ main-text pre-emption
【Welfare-reading objection】derived or hand-waved? + fix
【Objection→answer map】[objection → exhibit/paragraph]
【Fix vs. disclose list】what to fix now / what to bound and disclose
【Next step】aejpol-submission (if ready) or back to the named skill
```
