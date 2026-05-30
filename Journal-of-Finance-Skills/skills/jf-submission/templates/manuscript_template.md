# The Journal of Finance — Manuscript Skeleton

> A JF-oriented structure: general-interest framing, accessible exposition, decisive results in the main text, and technical depth in the Internet Appendix. Confirm current formatting against the official author guidelines.

## Title page

> [Title — concrete and general-interest]
>
> Abstract (≈100 words): one sentence on the question, one on the design/data, one or two on the headline result **with its economic magnitude**, one on the contribution.
>
> JEL classification: [e.g., G12, G14, G32]
> Keywords: [3–5]

## 1. Introduction (the first ~3 pages do the work)

1. The question and why a broad finance audience should care
2. What we do (design / data / test, in plain terms)
3. What we find — headline result in **interpretable economic units**
4. Why it is credible (source of identifying variation, or the test design)
5. Contribution relative to the closest 3–5 papers (named, with the specific delta)
6. Brief roadmap (optional)

## 2. Data and sample

- Sources (name the databases, e.g., CRSP, Compustat, TAQ, Refinitiv; via WRDS)
- Sample period and filters (brief here; full construction in the Internet Appendix)
- Summary statistics (Table I)

### Variable definitions (Table I or appendix)

| Type                | Variable | Definition (formula) | Source |
|---------------------|----------|----------------------|--------|
| Dependent           |          |                      |        |
| Key independent     |          |                      |        |
| Controls            |          |                      |        |
| Instrument (if any) |          |                      |        |

## 3. Research design

### Corporate / empirical branch
- Identification strategy: [natural experiment / DID / RDD / IV]
- Source of variation and exogeneity argument
- Estimating equation; fixed-effects structure; clustering level

### Asset-pricing branch
- Test assets and portfolio construction (sorts; weighting; breakpoints)
- Estimator: Fama–MacBeth / time-series alphas / spanning / predictive
- Standard-error correction: Shanken / Newey–West / two-way clustering
- Benchmark factor model: CAPM / FF3 / FF5 / +MOM / q-factor

## 4. Main results

- Headline table (Table II/III) with economic-magnitude interpretation in the text
- Event-study / sorted-portfolio figure where applicable

## 5. Robustness (decisive checks only)

- Each check tied to a named threat to the claim
- Multiple-testing adjustment (asset pricing) or sensitivity to unobservables (corporate)
- Out-of-sample / subperiod evidence where the claim is predictive
- (Exhaustive checks → Internet Appendix)

## 6. Mechanism / interpretation (if applicable)

- Evidence on *why* the effect arises; cross-sectional predictions consistent with the channel

## 7. Conclusion

- Restate the answer and its economic significance for the broad audience; honest scope and limitations

## References

- Journal style; foundational + recent JF/JFE/RFS work on the topic; in-text ↔ list consistent

## Internet Appendix (separate file)

- Section IA.A: full data construction and filters
- Section IA.B: proofs / derivations
- Section IA.C: secondary and exhaustive robustness (Tables IA.I, IA.II, …)
- Section IA.D: additional figures and simulations
- Every IA item is referenced from the main text.

## Statements (separate, non-blinded as required)

- Conflict-of-interest / disclosure statement
- Data-availability / replication statement
- Funding and acknowledgments
