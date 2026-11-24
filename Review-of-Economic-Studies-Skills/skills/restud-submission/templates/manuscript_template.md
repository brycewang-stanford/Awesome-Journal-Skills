# REStud Manuscript Template

A structural skeleton for a Review of Economic Studies submission. REStud publishes
both theory and applied work; use the empirical or theory spine below (or both for a
theory-with-empirics paper). Verify current length/abstract limits and the reference
style on the journal's official author guidelines page.

---

## Title page

> [Title]
> [Authors: first name, initial(s), surname, each followed by department and institution]
> [Corresponding author contact; acknowledgements / funding]

## Abstract

> One short paragraph (no more than 150 words). Lead with the **result**, not
> the motivation: question → contribution (new model / design / fact) → headline
> finding (with magnitude) → why it matters.

> JEL: [codes]    Keywords: [required]

## 1. Introduction (no separate "motivation" preamble — start with the question)

1. **Hook & question** — the broad economic question, stated for a non-specialist.
2. **What we do** — the contribution in 1–2 sentences (the new model / design / fact).
3. **How** — the method/design and the key idea ("why now / why not before").
4. **What we find** — the headline result, with magnitude.
5. **Related work** — located against the closest 3–5 papers (confront, do not list).

## 2. (Theory spine) Model

### 2.1 Environment / setup
> Minimal — only objects the result needs. Notation defined once.

### 2.2 Main results
> Proposition 1 (formal statement). Verbal gloss: the economic force, the comparative
> static, what it rules out.
> Proposition 2 ...
> *Proof sketches in text; full proofs in the Online Appendix.*

### 2.3 Discussion / extensions
> Which assumptions are relaxable; what the special case already delivers.

## 3. (Empirical spine) Data and research design

### 3.1 Data and sample
> Source, period, unit of observation, selection criteria.

### 3.2 Identification strategy
> State the identifying assumption in one sentence. Name the design (DiD / IV / RDD /
> SCM / RCT / structural) and the modern estimator. Map model assumptions to the
> empirics if the paper has both.

| Variable type        | Name | Definition |
|----------------------|------|------------|
| Outcome              |      |            |
| Treatment / regressor|      |            |
| Instrument / running var |  |            |
| Controls             |      |            |

## 4. Results

### 4.1 Main result
> Each exhibit carries one result; report magnitude, not just stars.

### 4.2 Diagnostics
> Pre-trends / density / balance / weak-IV / placebo as the design requires.

### 4.3 Robustness
> Specification stability, alternative inference, the most fragile assumption confronted.

### 4.4 Mechanism / heterogeneity
> Evidence for the channel; pre-specified heterogeneity cuts.

## 5. Conclusion

> Restate the contribution, its scope, and its limits. No new results.

## References

> Author-date (Harvard) style. Example:
> Card, D. and A. Krueger (1994), "Minimum Wages and Employment", *American Economic
> Review*, 84(4), 772–793.

## Online Appendix

- **A. Proofs** — full proofs of all propositions, numbered to match the main text.
- **B. Additional robustness** — specifications and falsification tests held out of the main text.
- **C. Data appendix** — construction details, sources, summary statistics.
- **D. (Structural)** — estimation details, solver settings, convergence, counterfactuals.
