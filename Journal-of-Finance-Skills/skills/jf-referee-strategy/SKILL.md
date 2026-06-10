---
name: jf-referee-strategy
description: Use when anticipating referee objections and selecting suggested/opposed reviewers before or during a The Journal of Finance (JF) submission. Plans for review; it does not write the rebuttal (use jf-rebuttal).
---

# Referee Strategy (jf-referee-strategy)

## When to trigger

- Before submitting: anticipating the objections a JF referee will raise
- The portal asks for suggested / opposed reviewers
- A conflict of interest among editors, AEs, or referees needs flagging

## How JF review works (plan around it)

JF, the AFA flagship, runs a demanding multi-round process: a handling **editor** (currently **Antoinette Schoar (MIT)**, with co-editors and 50+ Associate Editors — verify the masthead) screens first, then assigns typically **2–3 referees**. The reality is severe — **~33–45% desk-rejected, ~5% accepted** (afajof.org editor reports, accessed 2026-05-30). Most papers die at desk review, so the first job is surviving the editor, not the referees.

### JF-specific channels
- A **cover letter is normally unnecessary** at JF — use one **only** to flag a conflict of interest (referees/AEs/editors who should be excluded) or to request a code-sharing exemption. Do not pad it (see `jf-submission`).
- Suggested/opposed reviewers, if the portal asks, should be specific and justified.

## Anticipating objections (pre-empt in the paper)

| Likely referee objection            | Where to neutralize it                          |
|-------------------------------------|-------------------------------------------------|
| "This is already in [paper]"        | Contribution paragraph (`jf-literature-positioning`) |
| "Identification is not credible"    | Design section + IA tests (`jf-identification`) |
| "Just data mining / multiple testing" | Disclosed search + adjusted thresholds (`jf-robustness`) |
| "Not general-interest enough"       | Reframe for the broad AFA reader (`jf-topic-selection`) |

## Reading the AFA screening funnel

Two gates sit in series. The **handling editor** reads the abstract, introduction, and identification before spending referees' time; you only reach the **referee panel** once the editor judges the paper plausibly flagship-publishable. Because the editor screens for general interest and first-order importance, the highest-leverage pre-submission work is making the first three pages survive an editor who is not a specialist in your niche. Treat the editor as the audience for the introduction, the referee for the design and Internet Appendix.

### Desk-reject patterns at a top-3 finance journal
Recurring shapes that draw a fast editorial "no" at JF (and JFE/RFS); pre-empt them before the portal, not in the rebuttal:

| Desk-reject pattern                         | What the editor sees                                  | Pre-submission fix                                  |
|---------------------------------------------|-------------------------------------------------------|-----------------------------------------------------|
| Narrow / single-subfield question           | "Interesting to microstructure people only"           | Reframe the first-order stake (`jf-topic-selection`) |
| Causal verb, correlational design           | No named shock/instrument in the intro                | Lead with the source of variation (`jf-identification`) |
| Anomaly with naive t > 1.96 only            | Smells of the factor zoo                              | Multiple-testing-adjusted threshold (`jf-robustness`) |
| Statistically significant, economically tiny | A 2-bp effect dressed as a discovery                  | Report Sharpe gain / % of market cap up front        |
| Wrong-journal fit (reads like a JFE paper)  | Specialized, results-driven, no broad hook            | Re-center on the general-interest reader             |

Confirm the current desk-reject rate language against the journal's editor reports rather than quoting a fixed number.

## Worked vignette — pre-empting the panel on an anomaly paper

*Illustrative figures.* A new "supplier-concentration" return predictor shows a 55 bps/month long-short spread, raw t = 3.1. War-game the panel before submitting:

- **AE / asset-pricing referee**: does 55 bps survive Fama–French five-factor + momentum alphas, and is t = 3.1 above the factor-zoo bar (~3.0, illustratively)? Pre-empt with the post-adjustment alpha (say 38 bps, t = 2.7) in the body and the full factor grid in the IA.
- **"Is it real" referee**: microcap artifact? Pre-empt with a NYSE-breakpoint, value-weighted version (say 31 bps).
- **General-interest editor**: why would a corporate reader care? Tie the signal to a mechanism (supply-chain risk pricing) that reaches beyond the anomaly catalog.

The deliverable is a one-page objection map — each likely reviewer, their attack, the table or IA section answering it — written before submission.

### Referee-pushback patterns and the JF-specific fix
| Pushback you will hear                          | JF-specific fix                                                |
|-------------------------------------------------|----------------------------------------------------------------|
| "Run it value-weighted with NYSE breakpoints"   | Pre-build the VW result; IA holds EW and alternative breakpoints |
| "The effect is economically trivial"            | Lead with Sharpe gain / bps, not the t-stat                     |
| "Your shock coincides with the 2008 crisis"     | Excluded-period and placebo windows in the IA                   |

## Checklist

- [ ] Top 3 likely referee objections listed and pre-empted in the manuscript
- [ ] Desk-reject risk assessed (general interest, identification, fit)
- [ ] Opposed reviewers (genuine COI) noted only if the portal asks
- [ ] Cover letter used only for COI or code-exemption — otherwise omitted
- [ ] Suggested reviewers are specific and defensible

## Anti-patterns

- Writing a long cover letter JF did not ask for
- Listing opposed reviewers without a real conflict (reads as gaming)
- Ignoring desk-reject risk and over-optimizing for referees
- Leaving the obvious "already known" objection unaddressed

## Output format

```
【Top objections + where pre-empted】...
【Desk-reject risk】low / med / high — why
【COI to flag in cover letter?】yes / no
【Suggested/opposed reviewers (if asked)】...
【Next step】jf-submission → (after decision) jf-rebuttal
```
