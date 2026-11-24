# RFS Manuscript Skeleton

A structural template for a *Review of Financial Studies* submission (OUP for the SFS; SFS
Editorial Express portal; double-blind). RFS norms: abstract **≤ 100 words**, **Chicago
Manual of Style author-date** references, double-spaced (≤ 28 lines/page, font ≥ 11), fee
(high-income) $400 member / $460 non-member, middle-income $260 / $320 (confirm on
sfs.org/review-of-financial-studies/submit-a-paper). RFS requires **public release of all
code** — and, under the Code and Data Sharing Policy, a verified data-and-code package — as a
condition of publication, and offers two routes JF/JFE do not:
**Registered Reports** (Stage 1 design review) and **SFS Cavalcade dual submission**. This is
a structure guide, not a style manual.

## Title page (separate, non-anonymized file)

> [Title]
> [Author 1], [affiliation]; [Author 2], [affiliation]; ...
> Corresponding author: [name, email, ORCID]
> Acknowledgments, grant numbers, presentations — **here only**, not in the blinded file.

## Anonymized manuscript

### Abstract
- One short paragraph, **≤ 100 words** (RFS returns longer abstracts).
- Lead with the **question** and the **headline finding (with magnitude)**.
- State the design and data in a clause; end with the contribution/implication.
- No undefined acronyms; do not open with "The literature has long debated...".

### Keywords / JEL
- Keywords: xxx; xxx; xxx
- JEL: G__, G__, ...

### 1. Introduction
- (a) Hook: the first-order question and why it matters now.
- (b) What we do: design + data; name the source of variation.
- (c) What we find: headline result with magnitude; key robustness in a clause.
- (d) Why it is new: explicit delta vs. the closest 2–3 papers.
- (e) Mechanism / interpretation: what it means for theory or practice.
- (f) Brief roadmap.

### 2. Related literature / theoretical framework
- Organize by question, not chronology. Anchor literatures + frontier + the wedge.
- If theory-driven: state the model and the testable prediction here.

### 3. Data and empirical design
- (a) Sample: universe, period, every filter, final N (attrition table).
- (b) Variable measurement table:

| Role                | Variable | Definition / construction | Source |
|---------------------|----------|---------------------------|--------|
| Dependent           |          |                           |        |
| Key independent     |          |                           |        |
| Controls            |          |                           |        |

- (c) Identification strategy: the source of exogenous variation, in one sentence.
- (d) Estimator and standard-error structure (clustering / adjustment).

### 4. Main results
- (a) Baseline result with economic magnitude.
- (b) Identification diagnostics (parallel trends / density / first-stage F / GRS, as applicable).
- (c) The single most convincing robustness check (full battery → Internet Appendix).
- (d) Mechanism / heterogeneity evidence.

### 5. Robustness (summary; full set in Internet Appendix)
- Alternative specs, measures, subsamples; multiple-testing / out-of-sample for predictability claims.

### 6. Conclusion
- What we learned, the contribution, limitations, and what it implies — not a repeat of the abstract.

### References
- Every in-text citation appears here and vice versa.
- Cite recent RFS/JF/JFE work and canonical theory; use **Chicago Manual of Style author-date** references.

## Internet Appendix (at the end of the manuscript PDF — not a separate upload; no author names)
- IA.A Proofs / full derivations
- IA.B Data construction and variable definitions
- IA.C Full robustness battery (cross-referenced from the main text by IA number)
- IA.D Additional figures and extended tables
- Data-and-code availability statement + structure of the public code release (RFS condition of publication)

## Cover letter (separate)
- The question, the contribution, and why it fits RFS (novelty + rigor).
- The closest RFS/JF/JFE papers and the delta vs. each.
- Prior presentations / working-paper version / any SFS Cavalcade submission.
- Conflict disclosures; no concurrent submission elsewhere (RFS–Cavalcade dual submission is the permitted exception).
- If code cannot be publicly released, the reason (per RFS policy).
- Suggested and opposed referees (no current RFS editor among suggested).
