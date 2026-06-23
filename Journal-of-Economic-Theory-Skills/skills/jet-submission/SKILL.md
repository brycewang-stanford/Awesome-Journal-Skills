---
name: jet-submission
description: Use when running the final pre-submission preflight for the Journal of Economic Theory (JET) via Elsevier Editorial Manager — editable Word/LaTeX source (no PDF source), 250-word abstract, 1-7 keywords, optional Highlights, author-year proof-stage references, Option C data statement, generative-AI disclosure, and the APC-vs-submission-fee distinction. Final checks; it does not draft content.
---

# Submission Preflight (jet-submission)

## When to trigger

- About to press submit on Editorial Manager and want a last pass
- Unsure which files JET expects at initial submission
- Confirming elsarticle formatting, abstract references, and the AI declaration are compliant

## Process facts (verified 2026-06-20; re-confirm on the official page)

- JET is published by **Elsevier (Academic Press / Elsevier Science)**, **print ISSN 0022-0531**,
  electronic **1095-7235**. Submission is via **Elsevier Editorial Manager** through the journal's
  portal (attach-files page).
- **Source must be editable**: `.doc/.docx` for Word or `.tex` for LaTeX. **PDF is not accepted as a
  source file.** For LaTeX submissions, use Elsevier `elsarticle` and upload every file needed for the
  system-built peer-review PDF.
- **Reference formatting is flexible at first submission** if references are complete and consistent.
  JET's proof-stage style is **name-year / author-year**; abstract references must be written in full.
- **References cited in the abstract must be given in full.** Keep **unpublished results / personal
  communications out of the reference list.**
- **Authors must disclose generative-AI use at submission.**
- **Research data policy**: Elsevier **Option C** applies. If the paper has research data, deposit it
  in a relevant repository and cite/link it, or explain why sharing is not possible. Pure theorem
  papers should still make any numerical or computer-assisted artifact reproducible.
- **Submission fee vs APC**: the official pages inspected do not list a JET submission fee. Do **not**
  confuse that with the separate **open-access APC, last verified at USD 3,130** excl. tax (hybrid
  journal; APC applies only if you choose OA after acceptance). A 2026-06-23 re-audit could not
  independently re-confirm the exact figure (Elsevier now serves APCs through its personalized
  submission flow, not a static public number), so treat USD 3,130 as the last-verified value and
  confirm the live amount in the submission system before relying on it.
- **Abstract / keywords / Highlights**: abstract must not exceed **250 words**; provide **1-7 English
  keywords**. Highlights are encouraged as a separate editable file with **3-5 bullets**, each no more
  than **85 characters**.

## Preflight checklist

### Format & source
- [ ] Compiled from **editable `.tex`** in `elsarticle`; no PDF-as-source
- [ ] **Full references inside the abstract**; reference list excludes personal communications
- [ ] Abstract is **250 words or fewer**; **1-7 English keywords** supplied
- [ ] Highlights file prepared if used: **3-5 bullets**, each **85 characters or fewer**
- [ ] References complete and consistent; ready for JET's author-year proof-stage style
- [ ] Definition/assumption/proposition/theorem/proof structure renders cleanly; cross-refs resolve

### Declarations
- [ ] **Generative-AI use disclosed** (or explicit "none")
- [ ] Conflict-of-interest / funding statements prepared
- [ ] Option C data statement prepared: repository citation/link, or no-data / cannot-share explanation
- [ ] Confirmed not under review elsewhere

### Files for Editorial Manager
- [ ] Main `.tex` + `.bib` + figure sources; cover letter (scope-fit pitch to the matching editor)
- [ ] Suggested / excluded referees (expert, conflict-free)

## elsarticle theorem preamble that compiles cleanly

```latex
\documentclass[preprint,12pt]{elsarticle}
\usepackage{amsmath,amssymb,amsthm}
\newtheorem{theorem}{Theorem}
\newtheorem{proposition}{Proposition}
\newtheorem{lemma}{Lemma}
\newtheorem{corollary}{Corollary}
\theoremstyle{definition}
\newtheorem{definition}{Definition}
\newtheorem{assumption}{Assumption}
\newtheorem{example}{Example}
\theoremstyle{remark}
\newtheorem{remark}{Remark}
% Appendix proofs: restate main results (thmtools' restatable, or manual theorem* copies
% keeping the body's numbering) so referees never page-flip mid-proof.
\bibliographystyle{elsarticle-harv} % JET proof-stage style is name-year / author-year
```

Compile this skeleton with your environments **before** pasting in the paper; theorem-numbering
clashes between `elsarticle` options and `amsthm` are easier to fix on an empty file.

## Cover letter for editor routing

- One paragraph: the **theorem sentence** plus the named subfield (mechanism design, decision
  theory, matching, information design, …) so the field-matching editor claims the paper.
- One paragraph: the **closest published theorem** and your delta in one clause each.
- Declarations recap: generative-AI disclosure, not under review elsewhere, any conflicts.
- Suggested referees: experts on the closest theorems, conflict-free; an excluded-referee request
  needs a neutral, factual reason.
- No marketing language — the desk screen reads for scope fit and seriousness, not enthusiasm.

## Common Editorial Manager bounces for theory papers

- Source rejected because only a compiled PDF was uploaded — Editorial Manager needs the `.tex`.
- The system-built PDF breaks theorem environments because a custom `.sty` file was not uploaded
  alongside the source.
- Bibliography file missing, so abstract references and the reference list fail to render.

## Final compile-and-cross-reference sweep

- [ ] Every `\ref`/`\eqref` resolves — zero "??" in the compiled PDF
- [ ] Theorem numbering is continuous; appendix restatements carry the body's numbers
- [ ] Abstract is 250 words or fewer; abstract citations written out in full; no `\citet` abbreviations there
- [ ] 1-7 English keywords supplied; Highlights file meets 3-5 / 85-character limits if included
- [ ] Figures embedded as vector PDF with fonts embedded
- [ ] Supplementary appendix uploaded as its own file if proofs were offloaded (confirm the
      expected file split against the journal's current author guidelines)

## Output format

```
【Source】editable .tex (elsarticle), no PDF source? [Y/N]
【Abstract/keywords】≤250 words; 1-7 keywords; abstract refs in full? [Y/N]
【AI disclosure】declared? [Y/N]
【Data】Option C statement ready: repository/link or explain? [Y/N]
【Fee】APC ≠ submission fee acknowledged? [Y/N]
【Next】await editor desk screen → jet-review-process
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — elsarticle/LaTeX toolchain
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official JET URLs behind every fact
