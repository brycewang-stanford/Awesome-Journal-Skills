# QJE Manuscript Skeleton

A structural skeleton for a *Quarterly Journal of Economics* (QJE) empirical-micro
submission. QJE favors a big question + credible identification + a broad lesson,
with an extensive online appendix and author-date references. Adapt to your project;
verify current author guidelines on the official page.

## Title & authors

> [Title — concrete and informative; the question or the finding, not the method]
>
> [Author names centered; corresponding author's address + email; total word count — QJE's first page must give these (affiliations go after the last line of text)]

## Abstract (state the finding)

> One or two sentences: the question and the source of variation. Then the headline
> result **with a number and units**. Close with the broad lesson. No "this paper
> studies the important question of"; a general-interest reader should know what you
> found from the abstract alone.

**JEL codes:** [required; place at the end of the abstract] · **Keywords:** [optional — not required by QJE]

## 1. Introduction (the top-5 arc)

1. **The question** — plain language, stakes clear, in one or two sentences.
2. **Why it is hard** — the identification problem that blocked a clean answer.
3. **The setting & variation** — the natural experiment / novel data that solves it.
4. **The headline result** — the number, early and memorable, with units.
5. **Interpretation & mechanism** — what it means; conceptual frame in a sentence.
6. **Contribution & broad lesson** — placement vs. the 3–6 frontier papers + "beyond this setting."
7. **Roadmap** — brief.

> QJE intros weave the literature into the introduction; do not write a standalone
> "Section 2: Literature Review."

## 2. Setting / Conceptual framework

- Institutional background needed to understand the source of variation.
- A light conceptual frame or model: define the object being estimated; state the
  testable prediction. Match theory weight to the question.

## 3. Data

- Sources (with provenance and vintage), sample construction, key variables and units.
- Summary statistics; balance/representativeness as relevant.

## 4. Empirical strategy

- The identifying variation in one sentence; the estimating equation.
- The identifying assumption stated plainly and defended (exogeneity / exclusion / continuity).
- Estimator (for staggered DID: Callaway–Sant'Anna / Sun–Abraham / dCDH, not plain TWFE).
- Inference: clustering level; few-cluster handling.

## 5. Results

### 5.1 Headline result

- Lead with the **headline figure** (event-study plot / RDD discontinuity / first stage).
- Main estimates table: readable, units stated, self-contained note.

### 5.2 Identification diagnostics

- Pre-trends / density / first-stage / balance; placebo and falsification evidence.

### 5.3 Robustness (summary; full battery in the online appendix)

- One line per threat category, pointing to the appendix.

### 5.4 Mechanism

- The prediction from §2 tested; the channel shown, not merely asserted.

### 5.5 Heterogeneity (where it teaches something)

- Cuts that sharpen the mechanism or the external-validity story.

## 6. Interpretation / Magnitudes

- Benchmark the effect size against the literature; map to a welfare/policy quantity
  where feasible; bound what the estimate does and does not extend to.

## 7. Conclusion

- Restate the question, the answer, and the broad lesson. No new claims.

## References (author-date)

> Surname, First. Year. "Title." *Journal* Volume (Issue): pages.
>
> Akerlof, George A. 1970. "The Market for 'Lemons': Quality Uncertainty and the Market Mechanism." *Quarterly Journal of Economics* 84 (3): 488–500.
>
> Chetty, Raj, and Nathaniel Hendren. 2018. "The Impacts of Neighborhoods on Intergenerational Mobility I: Childhood Exposure Effects." *Quarterly Journal of Economics* 133 (3): 1107–1162.

## Online appendix (extensive — expected at QJE)

- A. Data construction and variable definitions
- B. Full robustness battery, organized by threat category
- C. Additional figures / tables referenced in the body
- D. Proofs / derivations for any formal results
- E. Replication note (see qje-replication-package): run order, environment, exhibit map
