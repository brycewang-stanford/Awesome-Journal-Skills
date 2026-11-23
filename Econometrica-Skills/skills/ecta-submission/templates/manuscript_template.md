# Econometrica Manuscript Template (Theory / Methods)

A skeleton for a theorem-driven Econometrica manuscript. Adapt for a structural / empirical
paper by expanding the application section and the identification discussion. Use LaTeX with
`amsthm` theorem environments in the actual paper; this template shows the logical structure.

> Econometrica constraints to keep in view while drafting: the main text must fit
> **≤45 pages including references and appendices** (font ≥12pt, line spacing ≥1.5, margins
> ≥1.25in); the **Supplemental Appendix is ≤25 pages** and further **Supplemental Material**
> (full proofs, Monte Carlo detail) is unrestricted; the abstract is **≤150 words**.

---

## Title

> [Title]

## Authors

> [Author names and full affiliations on the title page — Econometrica is single-anonymous; no de-identification]

## Abstract

> A few sentences (≤150 words): the setting, the central result (in words), what assumption
> it relaxes or what object it delivers, and the payoff. State the result, not just the topic.

**Keywords:** ... (required)
**JEL Classification:** ... (optional at Econometrica)

---

## 1. Introduction

- The problem and why it is hard.
- **Informal statement of the main theorem** (reach it within the first ~2 pages).
- Relation to the closest prior result (one sentence of formal difference per key neighbor).
- Roadmap.

## 2. Setup

### 2.1 Definitions

> Define every object the results use: spaces, parameter set, operators, solution concept.

### 2.2 Assumptions

> Numbered, displayed assumptions. Group standing assumptions separately from those invoked
> only for specific results. Each assumption must be used somewhere.

- **Assumption 1.** ...
- **Assumption 2.** ...
- **Assumption 3.** ...

> Optional: a short "Discussion of Assumptions" paragraph — what each buys, what relaxing it costs.

## 3. Main Results

### 3.1 Identification / Existence

- **Theorem 1.** *Under Assumptions 1–2, [precise conclusion: identification / existence].*

  *Proof sketch.* [Architecture + the hard step. Full proof in Supplemental Material §A.] ∎

> Interpretation paragraph: what the result means, what is surprising, which assumption does the work.

### 3.2 Asymptotic Distribution / Uniqueness / Representation

- **Theorem 2.** *Under Assumptions 1–3, [limiting distribution / uniqueness / representation],
  with [asymptotic variance / functional form pinned up to ...].*

  *Proof sketch.* [...] ∎

> Interpretation paragraph.

### 3.3 Inference / Comparative Statics (as applicable)

- **Proposition 1.** *[Consistent variance estimator / comparative-static / corollary].*

## 4. Monte Carlo Evidence

- DGPs: favorable design(s) and boundary / adverse design(s).
- Sample sizes (several), number of replications, nominal level.
- Comparison against the natural competitor method(s).
- Report bias / RMSE, empirical size, size-adjusted power, coverage, length, tuning sensitivity.
- Behavior under weak / near-boundary identification if the theory has that regime.

> Table 1: [size / coverage]. Table 2: [power / RMSE]. Each fully self-contained.

## 5. Empirical Application (if applicable)

- Data, sample, and how the variation maps to the identifying restrictions.
- Estimates with the inference procedure justified by Section 3.
- Counterfactual / comparative-static delivered by the identification argument.

## 6. Conclusion

> Brief. Restate the contribution and its limits; do not re-derive.

---

## Appendix A. Proof of Theorem 1
## Appendix B. Proof of Theorem 2

> Full, complete proofs. In the submitted paper these (if long) live in the **Supplemental
> Material** (Supplemental Appendix ≤25 pages, plus unrestricted online Supplemental
> Material), cross-referenced from the body — they do not count toward the 45-page limit.

## Supplemental Material

- Full proofs of all results not fully proven in the body.
- Complete Monte Carlo design and additional simulations.
- Additional theorems / extensions.
- Data and Code Availability (Econometric Society policy): provenance, environment,
  exhibit↔script map, PDF README; Data Editor reproducibility check at conditional
  acceptance; Zenodo deposit (verify current policy).

---

## References

> Cite theorem-level results precisely where a proof depends on them. Match the journal's
> current reference style. Ensure in-text and list agree both ways. References count toward
> the 45-page limit, so keep the list tight and load-bearing.
