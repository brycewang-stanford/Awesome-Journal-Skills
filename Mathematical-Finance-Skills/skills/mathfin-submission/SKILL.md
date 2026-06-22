---
name: mathfin-submission
description: Use when running the final Mathematical Finance submission preflight through Wiley Research Exchange, including LaTeX source, compiled PDF, supplementary files, classifications, data availability statement, and single-blind review considerations.
---

# Submission Preflight (mathfin-submission)

## When to trigger

- The paper is ready to submit through Wiley Research Exchange
- You need to check LaTeX files, classifications, appendices, and policy statements
- You are unsure what a theory-first Wiley submission needs before upload

## Preflight checklist

### Scientific readiness

- [ ] Main theorem(s) stated with complete hypotheses and conclusions
- [ ] Full proofs included or placed in appendices
- [ ] Detailed mathematical analysis moved to appendix where appropriate
- [ ] Numerical experiments, if any, tied to rigorous analysis
- [ ] Contribution to financial modelling explicit in abstract and introduction

### Files

- [ ] Main Document - LaTeX `.tex` file
- [ ] Main Document - compiled PDF
- [ ] LaTeX supplementary/supporting files as needed
- [ ] Figures and tables prepared as separate files if required at revision
- [ ] Bibliography file and custom macros included

### Metadata and declarations

- [ ] Title, abstract, keywords
- [ ] JEL and AMS/MSC classifications where requested
- [ ] Data Availability Statement
- [ ] Funding, conflicts, acknowledgements
- [ ] Open Access choice and APC implications checked if relevant — *Mathematical Finance* is a hybrid Wiley journal with **no submission fee**; optional OA APC was **USD 3,840 / GBP 2,590 / EUR 3,190** as of 2026-06-22 (re-verify on Wiley's APC page; may be covered by an institutional agreement). Editor as of 2026-06-22: **Rama Cont**.

## LaTeX hygiene

- Keep custom macros minimal and defined in one place.
- Confirm the PDF compiles from a clean checkout.
- Avoid fragile local paths.
- Ensure theorem, lemma, proposition, assumption, and equation labels are stable.

## Preamble conventions that ease refereeing

```latex
\usepackage{amsmath,amssymb,amsthm}
\usepackage[capitalise]{cleveref}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{definition}
\newtheorem{assumption}{Assumption}[section]
\newtheorem{definition}[theorem]{Definition}
\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}
% one shared counter => "Lemma 3.4" is unambiguous across text and appendix
```

Number within sections, share one counter across theorem-like environments, and never renumber
assumptions between revisions without flagging it — referees cross-reference their earlier
reports against your labels.

## Cover letter for a theorem-first venue

Three short paragraphs suffice: (1) the financial-modelling problem and the main theorem in
plain words; (2) the methodological novelty — which hypothesis is weakened or which object is
new — naming the one or two closest papers; (3) declarations: not under review elsewhere, any
overlap with a thesis chapter or proceedings version disclosed, and suggested non-conflicted
referees who command the relevant stochastic-analysis toolkit. Do not retell every section.

## Classification and keyword picks

Choose MSC codes that match the proof toolkit (e.g., 60G44 martingales, 60H30 applications of
stochastic analysis, 91G20 derivative pricing, 93E20 optimal stochastic control) alongside the
JEL codes common for pricing and control work (e.g., G12, G13, C61). Keywords should name both
the mathematical objects (BSDE, free boundary, martingale optimal transport) and the financial
problem — referee matching at a theory journal runs on both vocabularies.

## Length and structure calibration

Accepted papers commonly run on the order of 25–45 journal pages with appendices carrying a
substantial share of the proofs; treat these as soft anchors, not rules, and confirm any formal
limits against the journal's current author guidelines. A longer manuscript is not
automatically penalized, but it must earn its length with genuinely distinct results, and the
main text should stay readable end-to-end without the appendix.

## Upload-readiness order

Check the paper in this order:

1. Compile from a clean checkout and compare the generated PDF with the intended submission PDF.
2. Read theorem statements without proofs; every hypothesis and conclusion should be self-contained.
3. Check appendix references from the main text and from the appendix back to the main theorem.
4. Confirm numerical files, if any, regenerate figures/tables named in the PDF.
5. Reopen live Wiley pages for editor, fee, open-access, and policy details before final upload.

This order catches scientific blockers before metadata work. Do not spend time polishing upload forms while
a theorem, appendix pointer, or data statement remains unstable.

## Output format

```text
[Scientific readiness] pass / gaps
[Files ready] tex / pdf / bib / figures / supplement
[Policy statements] data / conflicts / funding / OA
[Live checks needed] editor / APC / submission-flow fee screen / reference style
[Next step] submit or fix listed gaps
```
