# EJ Manuscript Skeleton

A structural template for a The Economic Journal manuscript. EJ publishes the full breadth of
economics for a broad international readership, values clear exposition, and uses **author-date**
references. Adapt section order so theory leads when the model is the contribution. For a **short
paper** (AER:Insights style), compress to <6,000 words / 5 exhibits. The accepted-author guide
uses author-date references, a <=100-word abstract, a <=40-character short title, and keywords of
<=20 characters each; re-check the live portal for any submission-form field limits.

---

## Title
> [Concise, economics-forward title — name the question or the mechanism, not the dataset; legible to a generalist]

## Abstract
> State the economic question, the mechanism, what you do (model and/or identification), the main
> finding with a magnitude, and the **broad economic implication**. Lead with the economics, not
> the method. Keep it within 100 words for accepted-author production.

**JEL Classification:** [≥2 codes — required at submission]
**Keywords:** [concise terms, each <=20 characters for accepted-author production]

---

## 1. Introduction
- The economic question and why a **generalist economist** should care (broad relevance argued, not assumed)
- What is established, and the framing **theory** (author-date)
- The precise gap / tension: a conflated channel, an untested prediction, a missing force
- What this paper does (mechanism first, then method), in 2–3 sentences
- Main findings, their economic interpretation, and the **portable lesson**
- (Optional) short related-literature paragraph naming the 1–2 literatures you contribute to

## 2. Model / Theoretical Framework
- Primitives: agents, objective, constraints, what is optimized
- Economic intuition stated **in words before the algebra** (EJ exposition bar)
- Equilibrium concept; existence/uniqueness where relevant
- The key comparative static — stated as the prediction the data will test
- For empirics-led papers: the *smallest* model that delivers the testable prediction
- (Structural) the parameters to be estimated and what will identify each

## 3. Data and Institutional Setting
- Sources and sample construction (time span, selection criteria)
- Institutional background that motivates the identifying variation
- Variable definitions

| Role                 | Variable | Definition |
|----------------------|----------|------------|
| Outcome              |          |            |
| Treatment / key RHS  |          |            |
| Controls             |          |            |
| Instruments (if any) |          |            |

## 4. Empirical Strategy
- The estimating equation, derived from or connected to Section 2
- The identifying assumption, stated in one plain sentence and defended economically
- Estimator and inference (clustering level + justification)
- Diagnostics planned (pre-trends / first-stage F / manipulation / parameter identification)

## 5. Results
- Baseline result expressed as an **economic magnitude**, not stars alone
- Headline figure (event study / dose-response / model fit / counterfactual) with confidence bands
- Mechanism evidence: the test that discriminates your channel from rivals

## 6. Mechanisms and Robustness
- Specification stability; selection-on-unobservables bound (e.g., Oster δ)
- Rival mechanisms named and tested against
- Triangulation (second data source / design / structural cross-check)
- External validity / generalizability argued or bounded (EJ broad-interest bar)
- (Structural) sensitivity of estimates and counterfactuals; untargeted-moment fit
- Punchline in main text; full battery in the online appendix

## 7. (Optional) Counterfactuals / Welfare
- Counterfactual experiments from the estimated model
- Welfare: who gains, who loses, against an efficiency benchmark

## 8. Conclusion
- What economics learned and the **portable lesson** (not a table-by-table recap)
- Honest limitations, bounded

---

## Acknowledgments
- All sources of research funding acknowledged (EJ requirement)

## References (author-date style)

Author, A. B., and C. D. Author. Year. "Title." *The Economic Journal* Volume (Issue): pages.

Order references alphabetically, then chronologically for each author; cite datasets and replication
packages where relevant.

---

## Online Appendix / Replication (RES / EJ Data Editor)
- A. Proofs and derivations
- B. Full robustness battery
- C. Additional descriptive statistics and data construction details
- D. Data and code availability statement (DCAS); replication package destined for **Zenodo**;
  restricted-data exemption requested **at first submission** if applicable
