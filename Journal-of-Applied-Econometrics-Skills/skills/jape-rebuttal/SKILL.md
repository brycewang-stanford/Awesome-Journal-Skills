---
name: jape-rebuttal
description: Use when drafting the response letter for a Journal of Applied Econometrics (JAE) revise-and-resubmit — replying to single-blind anonymous referees and the Editor-in-Chief on applied-econometrics objections (identification on real data, inference, robustness) while keeping the JAE Data Archive package in sync with every revised result.
---

# Rebuttal for JAE (jape-rebuttal)

## When to trigger

- You have a JAE decision letter inviting a revision and are drafting the response
- Referees raise objections about identification, inference, or reproducibility
- You need to keep your archive-bound data/code consistent with the revised paper

## How to respond at JAE

JAE review is **single-blind**: referees are anonymous, you are not, and the **Editor-in-Chief** makes the final call. Address the Editor and each referee separately. Reproduce every comment verbatim, then reply with the **exact manuscript change** and, where the point is decision-critical, **new diagnostic evidence** (a robustness table, an alternative estimator, a placebo test). Do not thank the anonymous reviewers inside the manuscript acknowledgments (review is single-blind).

## Group the comments

- **Identification / estimand** — defend assumptions on real data, add tests rather than assert.
- **Inference** — if challenged on standard errors, show HAC/clustered/weak-IV-robust alternatives.
- **Robustness** — push expanded grids into the unlimited **online appendix** (the main text stays within 35 pages).
- **Reproducibility** — if a referee cannot regenerate a number, fix the code and say so.

## Keep the archive in sync

Because every reported result must be regeneratable from the eventual **JAE Data Archive** deposit (plain ASCII/CSV + readme + programs), update the master script and exported text outputs alongside the revised tables. A response that changes numbers but not the underlying code creates an archive mismatch that surfaces at acceptance.

## Anti-patterns

- Arguing identification verbally instead of adding a test
- Letting revised tables and the replication package drift apart
- Bloating the 35-page main text with new robustness instead of using the appendix
- Treating a reject as a resubmission opportunity without an Editor's invitation

## Objection triage for the JAE response letter

Sort every referee point into one of four lanes before writing a word; each lane has a fixed deliverable:

| Lane | Typical JAE phrasing | Deliverable | Lands in |
| --- | --- | --- | --- |
| Identification | "Parallel trends are assumed, not tested" | New diagnostic + heterogeneity-robust re-estimate | Main text or appendix + archive script |
| Inference | "With 13 clusters these SEs are unreliable" | Wild cluster bootstrap p-values beside CRVE | Table note + appendix grid + seeded code |
| Robustness | "Does this survive sample X / spec Y?" | The requested grid, run fully | Online appendix (35-page text untouched) |
| Reproducibility | "Equation (7) and Table 4 disagree" | Code fix, regenerated exhibits, explicit erratum line | Archive package + response letter |

## Worked response excerpt (illustrative)

```text
Referee 2, Comment 3: "The 2SLS results may reflect a weak instrument;
the first-stage F of 9.4 is not reassuring."

Response: We agree this needed weak-IV-robust treatment. Revised Table 5
now reports the effective first-stage F (9.4) in each column and adds
Anderson–Rubin 95% intervals; the headline estimate 0.31 has AR interval
[0.05, 0.63], so the qualitative conclusion stands at conventional levels.
Appendix D repeats the analysis on the stronger-instrument subsample
(F = 18.7). Programs iv_ar.do and appendixD.do in the replication
package regenerate every new number (seeds logged in README.txt).
```

The anatomy: concede what is correct, add the test rather than the argument, quantify, and name the archive script — the last step is the JAE-specific move that ends the thread.

## Tone for a single-blind venue

Referees know who you are; you do not know them. Avoid guessing identities, avoid flattery, and avoid relitigating fit — the Editor-in-Chief already judged scope by sending it out. Where two referees conflict (one wants more macro context, one wants it cut), propose the resolution explicitly and flag it for the Editor's adjudication rather than silently picking a side. If a requested analysis is infeasible (confidential data, computational cost), say so, quantify the obstacle, and offer the nearest feasible substitute plus a readme note describing how a reader with data access could run the original.

## Output format

```
【Per-referee】each comment quoted + concrete change? [Y/N]
【Lanes】every comment triaged (ident/inference/robustness/repro)? [Y/N]
【New evidence】decision-critical tests added (not asserted)? [Y/N]
【Appendix】expanded robustness to online appendix? [Y/N]
【Archive sync】code/data updated to match revised results? [Y/N]
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — single-blind / EiC and Data Archive sources
