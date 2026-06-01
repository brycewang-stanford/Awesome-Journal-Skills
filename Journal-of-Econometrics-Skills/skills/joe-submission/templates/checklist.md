# Journal of Econometrics — Pre-Submission Self-Check

Work top to bottom before pressing submit on Editorial Express (database `je`).
Re-verify volatile items (fee, abstract/page limits, portal routing, review model) on the
official pages — several Elsevier pages return HTTP 403 to automated fetches (待核实).

## 1. Scope & contribution
- [ ] The paper makes a **substantive methodological contribution** (estimator / test / identification result / asymptotic theory), not a purely applied result
- [ ] The contribution is stated as a **general property** in the abstract and introduction
- [ ] The nearest competing method is named and the delta is explicit

## 2. Formal core
- [ ] Estimand and model stated precisely; **identification proved** (point vs. partial)
- [ ] Assumptions **labeled**, and primitive/verifiable (or high-level ones justified for a leading case)
- [ ] **Asymptotics** derived: rate + limiting distribution + consistent variance estimator
- [ ] Generality stated; known cases shown to be nested; proof roadmap clear

## 3. Monte Carlo & illustration
- [ ] **Size at nominal 5%/10%** reported in its own panel
- [ ] **Size-adjusted power** reported; compared to nearest method on identical DGPs
- [ ] DGPs stress error distribution, dependence, tuning, and boundary cases
- [ ] **Seeds + replication counts + MC standard errors** reported
- [ ] Empirical **illustration** demonstrates the method without over-claiming an applied finding

## 4. Exhibits
- [ ] Tables/figures numbered, called out in order, with self-contained notes (DGP, $n$, reps, tuning)
- [ ] Size and power kept in separate panels
- [ ] Figures are vector, grayscale-safe, and legible within the single PDF

## 5. Format & style
- [ ] **Single PDF**, ~**40 pages**, **≥1.5 spacing, 11pt** (norm — 待核实)
- [ ] **Abstract ≤ 250 words**; cited references spelled out in full
- [ ] **elsarticle** LaTeX class; **Elsevier** reference style; dataset citations tagged **`[dataset]`** (author/title/repository/version/year/DOI)

## 6. Fee & portal
- [ ] **USD $75 fee paid** (VAT for EU authors); **proof-of-payment file ready to upload** (待核实)
- [ ] Confirmed new submission vs. resubmission > 1 year (fee trigger)
- [ ] Submitting via **Editorial Express** (db `je`), not Editorial Manager (待核实)
- [ ] **Track chosen**: Regular / Annals / Themed (Guest AE if Themed)

## 7. Review readiness & files
- [ ] Review is **single-anonymized** — authors visible to referees; confirm no referee-only content exposed (待核实)
- [ ] Files staged: main **PDF**, **proof of payment**, cover letter, suggested/excluded referees
- [ ] Reproducible artifact: estimator command/function + `run_all` pipeline staged

## 8. Declarations
- [ ] Conflict-of-interest / funding disclosures prepared
- [ ] Confirmed the paper is not under review elsewhere
- [ ] Data availability statement prepared for any real data in the illustration
