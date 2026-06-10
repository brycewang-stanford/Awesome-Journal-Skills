---
name: jape-contribution-framing
description: Use when framing the headline contribution of a Journal of Applied Econometrics (JAE) manuscript — as an empirical application on real data whose results are replicable, rather than a pure-theory advance. Calibrates claims to what the data and design support and compresses into the 100-word summary.
---

# Contribution Framing for JAE (jape-contribution-framing)

## When to trigger

- Writing or sharpening the contribution paragraph and the 100-word summary
- Deciding how strongly to claim, given the design and the real data
- Aligning the framing with JAE's applied, replicable identity

## Frame the contribution the JAE way

JAE rewards a contribution that is an **application on real data** with **replicable** results: here is a substantive question, here is a credible empirical strategy applied to real data, here is what we find, and every number can be regenerated from the data and code we deposit. Acceptable types:

- A **new empirical finding** on an economic question via a credible design;
- A **methodological application** — adapting or stress-testing a technique on real data, with the application (not the theorem) as the contribution;
- A **replication** that confirms, qualifies, or overturns published results (Replication Article track).

Pure theoretical novelty ("we prove a new asymptotic result") is **not** the JAE contribution; if you have method development, frame the *real-data demonstration* as the payoff.

## Calibrate the claim

Applied-econometrics referees punish over-claiming. The contribution must not exceed what the design and data support — distinguish association from causal effect, note external-validity limits, and let **replicability** carry weight: a modest reproducible finding beats an overclaimed fragile one.

## Fit the 100-word summary

The contribution must compress into a **summary of ≤ 100 words containing no citations**, understandable on its own (see `jape-writing-style`). Draft the one-sentence contribution first, expand into the summary, then back-check against the results.

## Desk-level signals the JAE editor screens for

Before any referee sees the paper, the editorial screen looks for the venue's identity markers. Put them where they are found fast:

| Signal | Where it must appear | Risk if missing |
| --- | --- | --- |
| Real data named (source, span, frequency, N) | First two pages | Read as a theory paper mis-sent to an applied journal |
| Econometric lesson (when/why the method matters *here*) | Contribution paragraph | "Estimator demo without an applied payoff" |
| Replication commitment (deposit to the JAE Data Archive) | Intro or data section | Doubt about reproducibility — fatal at this venue |
| Claim calibrated to design (causal vs. associational) | Contribution paragraph | Over-claiming flag from applied-econometrics referees |

## Worked vignette: framing an exchange-rate pass-through paper

Illustrative numbers only. Draft claim: "We show import prices respond incompletely to exchange rates." Too thin for JAE. Reframed: "Using monthly import-price micro data on 1,900 product lines (2002–2023), we estimate 12-month pass-through of 0.31 (HAC s.e. 0.06) — roughly half the aggregate consensus — and show the gap closes once invoicing-currency composition is held fixed; all series and programs will be deposited in the JAE Data Archive." This names the data, the inference, the quantitative finding, the econometric lesson (aggregation bias in pass-through regressions), and the replication hook — the elements a JAE contribution paragraph carries.

## Referee pushback on claims — venue-grade fixes

- "This is just estimator X applied to dataset Y." → State what the application *teaches*: a conclusion that flips, an inference pitfall exposed, a method stress-tested where its assumptions actually bind, and why the lesson travels beyond this one dataset.
- "Causal language outruns the design." → Downgrade the verbs or add the design-based test; never argue rhetoric at JAE — add a reproducible diagnostic instead.
- "Why JAE and not a field journal?" → If deleting the methods section would leave the paper readable, the econometric lesson is missing; sharpen it before resubmitting anywhere.

## Calibration: accepted-paper contribution texture

Hedged from public JAE issues rather than internal data: accepted papers tend to state the contribution within the first two pages, quantify the headline estimate with its standard error early, and spend a sentence on portability — why the approach generalizes past this application. Confirm current scope wording against the journal's author guidelines.

## Output format

```
【Type】new finding / method application / replication
【Claim】associational / causal — matches design? [Y/N]
【Replicable hook】stated? [Y/N]
【Summary fit】≤100 words, no citations, self-contained? [Y/N]
【Lesson】econometric takeaway travels beyond this dataset? [Y/N]
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — summary cap and scope sources
