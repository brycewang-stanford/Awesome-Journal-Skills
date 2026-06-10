---
name: jeg-submission
description: Use when running the final Journal of Economic Growth submission preflight through Springer Nature, including abstract length, title-page metadata, LaTeX or Word source files, declarations, data availability, and Open Choice fee checks.
---

# Submission Preflight (jeg-submission)

## When to trigger

- Submitting to JEG this week
- Checking Springer Nature file and metadata requirements
- Confirming no submission fee, optional APC, declarations, and source files

## Preflight checklist

- [ ] Submission portal: Springer Nature "Submit manuscript" path for journal 10887
- [ ] Abstract is 150-250 words
- [ ] Title page includes author details, ORCID, corresponding-author email,
      abstract, 4-6 keywords, JEL codes, and Statements/Declarations
- [ ] Editable source files provided: LaTeX preferred, Word accepted
- [ ] Data Availability Statement included
- [ ] Author Contribution and Competing Interest information ready
- [ ] LLM use disclosed if applicable; LLM not listed as author
- [ ] Subscription route chosen unless Open Choice APC is intentionally selected
- [ ] APC amount and editor facts re-verified on live Springer pages

## JEG-specific final read

Before upload, read only the title, abstract, introduction, and first results/model section and check:

- The paper is visibly about long-run growth, development, or dynamic macroeconomics.
- The contribution is framed as a growth mechanism, not a generic method or adjacent-field estimate.
- Theory/empirics classification is clear, with the right appendix and data/code expectations.
- Declarations and Data Availability Statement match the actual empirical, simulation, or calibration files.

If these fail, fix framing before formatting details. A polished Springer file will not save a weak JEG fit.

## Exhibit and appendix calibration

Hedged anchors drawn from what accepted JEG articles typically look like (treat as priors, verified against recent issues, never as hard limits):

- The main text usually carries a focused exhibit set — roughly 6-10 tables and figures — with the robustness mass pushed to an online appendix that can hold several times the main text's exhibit count.
- Common appendix blocks: data construction and sources, proofs, additional robustness (alternative samples, Conley cutoffs, alternative instruments), and calibration detail with untargeted moments.
- Persistence and comparative-development papers usually include at least one map exhibit; theory papers a transition-path or phase-diagram figure.

## Worked vignette — a submission-day audit

Illustrative final pass on a deep-determinants manuscript:

- Abstract at 241 words (inside the 150-250 window); 5 keywords; JEL codes O11, O33, N10 plus a mechanism-specific code.
- 8 main exhibits and 23 appendix exhibits; every table note states sample, units, clustering, and Conley cutoffs where outcomes are geocoded.
- The Data Availability Statement names the digitized historical-census deposit and the restricted survey's access path — matching the replication package line for line.
- Title page carries ORCID, declarations, and the LLM-use disclosure; the cover letter's one-paragraph pitch leads with the growth mechanism, never the estimator.
- The replication README is cross-checked against the jeg-replication-and-data-policy output, and the calibration folder regenerates both transition-path figures on a clean machine.
- Two gaps caught: a map exported as a low-resolution bitmap (replaced with vector) and a missing JEL code for the historical content — both fixed before upload.

## Fit-mismatch triggers to clear before upload

- The abstract's first sentence names a policy or program rather than a question about why economies grow or diverge.
- No introduction sentence states what the paper changes in our understanding of long-run growth or comparative development.
- The headline estimand is short-run and partial-equilibrium with no long-run translation anywhere in the text.
- Keywords and JEL codes signal an adjacent field (labor, public finance, IO) rather than growth, development, demography, or technological change — re-pick them to match the mechanism.

Any one of these is worth delaying submission to repair; portal mechanics and current file-format rules should be re-confirmed against the journal's current author guidelines on submission day.

## Output format

```text
[Files] tex/docx + pdf + figures + bib
[Metadata] abstract / keywords / JEL / ORCID
[Declarations] DAS / contributions / competing interests / LLM
[Fees] no submission fee; OA APC only if chosen
[Next step] submit or fix listed gaps
```
