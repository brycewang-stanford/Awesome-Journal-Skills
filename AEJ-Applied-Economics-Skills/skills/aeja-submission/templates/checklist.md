# AEJ: Applied Pre-Submission Self-Check (8 sections)

A last-pass checklist for an *American Economic Journal: Applied Economics*
(AEJ: Applied) manuscript before submitting via the AEA online submission system.
Verify volatile specifics (fee, editors, policy details) on the official AEA pages
(检索于 2026-06；以官网为准).

## 1. Venue fit & scope
- [ ] Empirical applied-micro question with a credible causal design (not an AER agenda swing, not a policy-ROI framing for AEJ: Economic Policy, not field-internal)
- [ ] Two subfields beyond your own that will plausibly cite it, named
- [ ] Headline result expressible as a magnitude with units and a standard error

## 2. Anonymization (double-blind)
- [ ] Manuscript fully anonymized: no author names, affiliations, acknowledgments
- [ ] Identifying self-citations removed or neutralized
- [ ] Separate non-anonymized title page prepared (authors, affiliations, contact, acknowledgments)

## 3. Identification & robustness
- [ ] Estimand stated (ITT / LATE / ATT / local-at-cutoff) and matched to the design
- [ ] Design-appropriate diagnostics in the paper (balance+attrition / pre-trends+Bacon / density+bandwidth / first-stage+exclusion)
- [ ] Modern estimator where TWFE / 2SLS would bias; inference clustered at the assignment level
- [ ] Robustness shows the point estimate is stable; design-specific sensitivity (honest-DID / RD bandwidth / weak-IV set) included

## 4. Front matter
- [ ] JEL codes assigned; keywords listed
- [ ] Abstract within AEA norms, stating question + design + headline estimate + lesson

## 5. Exhibits (AEA house presentation)
- [ ] Main causal estimate readable in one table: coefficient, SE in parentheses, N, dep-var mean
- [ ] Standard errors reported everywhere; clustering level in notes; stars (if used) defined
- [ ] Identification figure present (event-study with CIs / RD with density / balance with joint test)
- [ ] Notes self-contained; online appendix prepared separately

## 6. Experimental / own-data
- [ ] Survey instruments / experiment instructions ready
- [ ] Pre-registration (AEA RCT Registry / AsPredicted / OSF) cited; deviations reported

## 7. Reproducibility readiness (AEA Data Editor checks before publication)
- [ ] Paper is buildable into an openICPSR package: one master script regenerates all exhibits from raw data
- [ ] Data Availability Statement drafted for every dataset, with access terms
- [ ] Software/package versions pinned; seeds set/reported; no absolute paths
- [ ] Restricted-data / exemption requests flagged early

## 8. Fees, declarations & policy
- [ ] Submission fee ready (member vs nonmember confirmed; waiver if eligible)
- [ ] Disclosure statement (funding, interested-party relationships) per AEA policy
- [ ] Confirmed not under review elsewhere; AI not listed as an author
