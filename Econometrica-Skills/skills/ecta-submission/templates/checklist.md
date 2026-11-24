# Econometrica Pre-Submission Checklist

> Verify all volatile specifics (portal URL, submission fee, editorial board, the current
> Data and Code Availability Policy, formatting and blinding rules) on the official journal
> site before relying on them. Figures below were current as of 2026-05-30.
> https://www.econometricsociety.org/publications/econometrica
>
> Econometrica-specific essentials: at least one author must be an **Econometric Society**
> member; submission fee **US$125 regular / US$50 student** (from 2025); main text
> **≤45 pages incl. references and appendices**; Supplemental Appendix **≤25 pages**;
> abstract **≤150 words**; portal **Editorial Express**; replication under the ES Data and
> Code Availability Policy (**Data Editor** check; **Zenodo** deposit).

## 1. Contribution and fit

- [ ] Contribution stated as a theorem or estimator-plus-asymptotics, not as an application
- [ ] Result holds on the most general natural class, not just a parametric example
- [ ] Clear economic / behavioral / inferential payoff stated
- [ ] Honest placement: this is Econometrica-deep (method/theorem), not general-interest-applied (AER/QJE/JPE/REStud)
- [ ] Not an off-the-shelf applied paper (eligibility/co-editor screen returns those)

## 2. Manuscript structure

- [ ] Introduction reaches the (informal) main result quickly
- [ ] Main text **≤45 pages** incl. references and appendices; font ≥12pt / spacing ≥1.5 / margins ≥1.25in
- [ ] Definitions, assumptions numbered and displayed
- [ ] Theorems / Propositions / Lemmas numbered consistently
- [ ] Each main result followed by a short interpretation paragraph
- [ ] Cross-references by number, not "above / below"
- [ ] Conclusion is brief

## 3. Proofs

- [ ] Every proof complete — no "easy to see," no skipped step
- [ ] Proof sketches in the body; full proofs in the Supplemental Material if long
- [ ] Every regularity condition used in a proof appears as a numbered assumption
- [ ] No CLT / fixed-point / limit theorem invoked whose hypotheses are unverified
- [ ] Existence and uniqueness (or set characterization) both addressed
- [ ] The novel / hard step is given in full

## 4. Identification and asymptotics (methods papers)

- [ ] Parameter defined as a population functional, separate from the estimator
- [ ] Identification conditions numbered; point vs. partial identification stated
- [ ] Rate of convergence derived; limiting distribution derived
- [ ] Asymptotic variance + a consistent estimator provided
- [ ] Pointwise vs. uniform asymptotics addressed; weak-identification robustness considered

## 5. Finite-sample / Monte Carlo evidence

- [ ] At least one favorable and one boundary / adverse design
- [ ] Multiple sample sizes showing the asymptotics engage
- [ ] Comparison against the natural competitor method(s)
- [ ] Number of replications stated; Monte Carlo error small / reported
- [ ] Size, power (size-adjusted), coverage, length reported as relevant
- [ ] Tuning-parameter sensitivity examined

## 6. Tables and figures

- [ ] Each exhibit self-contained (design, n, replications, nominal level, per-column meaning)
- [ ] Three-line / booktabs style; no vertical rules or shading
- [ ] Figures fully labeled; vector format; readable in grayscale
- [ ] Every number in the text matches the tables exactly

## 7. References

- [ ] Every in-text citation in the reference list and vice versa
- [ ] Theorem-level results cited precisely where a proof depends on them
- [ ] Foundational and contemporaneous work cited fairly
- [ ] Reference style matches the journal's current requirement

## 8. Title page and author identity (single-anonymous — no de-identification)

- [ ] Title page carries abstract, keywords, and full author affiliations (official instructions, re-checked 2026-11-23)
- [ ] Self-citation in the third person (style, not a blinding rule)
- [ ] Current policy re-confirmed on the Instructions / Editorial Procedures pages

## 9. Supplemental Material

- [ ] Full proofs of all results not fully proven in the body
- [ ] Complete Monte Carlo design and additional simulations
- [ ] Supplemental Appendix **≤25 pages**; further material in unrestricted Supplemental Material
- [ ] Additional theorems / extensions referenced from the body
- [ ] Self-contained and cross-referenced from the main text

## 10. Data and Code Availability Policy (Econometric Society)

- [ ] Replication package reproduces from a clean checkout
- [ ] Monte Carlo / simulation tables reproduce bit-for-bit (seeds recorded) — simulations in-scope
- [ ] Single master script (`run_all`) regenerates every exhibit
- [ ] Environment pinned (software versions + dependencies)
- [ ] README in **PDF** (Social Science Data Editors' template)
- [ ] Data provenance / access documented; restricted data handled per agreement
- [ ] Deposit at ES Journals' Community on **Zenodo** (DOI reserved); Data Editor check at conditional acceptance
- [ ] If pure theory (no empirical/experimental/simulation results): exemption requested **at initial submission**
- [ ] Verified against the current ES Data Editor policy and deposit location

## 11. Submission portal (Editorial Express)

- [ ] Account ready; correct portal URL (editorialexpress.com, `dbase=econometrica`; verify on site)
- [ ] At least one author is a current **Econometric Society** member
- [ ] Main manuscript + Supplemental Material uploaded as specified
- [ ] Abstract (≤150 words), keywords, JEL codes (optional) entered accurately
- [ ] Correct field / classification chosen for co-editor routing
- [ ] Qualified, conflict-free referee suggestions provided
- [ ] Submission fee handled — **US$125 regular / US$50 student** member (non-refundable; invited resubmissions need only membership; exempt if all authors reside in World Bank low-income countries)
