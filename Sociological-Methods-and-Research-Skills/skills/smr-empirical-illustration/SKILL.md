---
name: smr-empirical-illustration
description: Use when building the real-data empirical illustration for a Sociological Methods & Research (SMR) paper — a demonstration that the method changes a substantive conclusion, not a decorative example. Designs the illustration; does not derive properties or design the Monte Carlo.
---

# SMR Empirical Illustration

Use this to make the real-data section earn its place. SMR expects a methods paper to show that the
method *matters substantively* — that using it instead of the incumbent leads to a different,
better-justified conclusion about the social world. A throwaway "we also applied it to some data"
section is a reviewer flag.

## The "it changes the answer" standard

The illustration's job is to demonstrate consequence:

- **Run the incumbent and the new method on the same data**, and show where they diverge. The payoff
  sentence is "the standard approach would have concluded X; our method shows Y, and Y is the
  defensible answer because [reason tied to the method's properties]."
- **Tie the divergence to the mechanism** established in `smr-derivation-and-properties` and the regime
  identified in `smr-simulation-studies`: the data should sit in the regime where the incumbent is
  known to fail.
- **State the substantive stake**: who would have made a wrong inference, and about what, if they had
  used the old method? The stake makes the method consequential, not just correct.

## Choosing the dataset

- Pick data that **lives in the failure regime** (e.g., few clusters, non-invariance across groups,
  informative missingness, network dependence) so the method has something to do.
- Prefer **public or depositable data** — SMR's availability policy expects the data and code behind
  the illustration to be accessible (see `smr-software-and-reproducibility`). If data are restricted,
  plan the availability statement now.
- A **familiar, recognizable dataset** lets readers judge the result against intuition; an exotic one
  forces them to trust you on both the data and the method.

## What to report

| Element | Purpose |
|---|---|
| Side-by-side incumbent vs. new method | Show the divergence concretely |
| The substantive conclusion under each | Make the stake visible |
| A diagnostic that the data are in the failure regime | Justify why the new method is needed here |
| Uncertainty for both methods | Avoid replacing one overconfident answer with another |
| Link to released code/data | Satisfy reproducibility expectations |

## Keep it an illustration, not a substantive paper

The danger runs both ways. Too thin and it is decorative; too thick and the paper becomes a
substantive study that belongs in ASR/AJS (the failure flagged in `smr-topic-selection`). Calibrate:
the illustration should be deep enough to show the method changes the answer, and no deeper. The unit
of analysis is the *method's behavior on real data*, not a full substantive argument with its own
literature.

## Checklist

- [ ] Incumbent and new method are run on the same data with results side by side.
- [ ] The divergence is tied to the method's mechanism and the simulated failure regime.
- [ ] The substantive stake (who would be wrong, about what) is stated.
- [ ] A diagnostic shows the data are actually in the regime where the method is needed.
- [ ] Uncertainty is reported for both methods.
- [ ] Data are public/depositable, or a restricted-data availability plan exists.
- [ ] The section stays an illustration, not a full substantive study.

## Anti-patterns

- **Decorative application**: the method is run, but it would not change any conclusion.
- **Regime mismatch**: data where the incumbent is fine, so the new method has nothing to prove.
- **Substantive creep**: the illustration grows into an ASR/AJS-style paper and loses methods focus.
- **One-method reporting**: showing only the new method's result, hiding what the incumbent would say.
- **Inaccessible data with no plan**: an illustration readers can never reproduce.

## Output format

```text
[Illustration status] consequential / decorative / not ready
[Dataset + regime] <data : why it sits in the failure regime>
[Divergence] <incumbent conclusion vs. new-method conclusion>
[Substantive stake] <who would have been wrong, about what>
[Reproducibility] data/code accessible? restricted-data plan?
[Next SMR skill] smr-tables-figures
```
