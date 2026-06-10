---
name: jet-submission
description: Use when running the final pre-submission preflight for the Journal of Economic Theory (JET) via Elsevier Editorial Manager — editable .tex source (no PDF source), elsarticle formatting, full references in the abstract, generative-AI disclosure, JEL codes and keywords, and the fee-vs-APC distinction. Final checks; it does not draft content.
---

# Submission Preflight (jet-submission)

## When to trigger

- About to press submit on Editorial Manager and want a last pass
- Unsure which files JET expects at initial submission
- Confirming elsarticle formatting, abstract references, and the AI declaration are compliant

## Process facts (verified where reachable; re-confirm on the official page)

- JET is published by **Elsevier (Academic Press / Elsevier Science)**, **print ISSN 0022-0531**,
  electronic **1095-7235**. Submission is via **Elsevier Editorial Manager** through the journal's
  portal (attach-files page).
- **Source must be editable `.tex`** (Elsevier `elsarticle` class). **PDF is not accepted as a
  source file.** Reference styles per template sources are `elsarticle-harv` (name-year) and
  `elsarticle-num` (numbered) — the single required style is **待核实**; confirm in the live guide.
- **References cited in the abstract must be given in full.** Keep **unpublished results / personal
  communications out of the reference list.**
- **Authors must disclose generative-AI use at submission.**
- **Submission fee**: no fee is indicated (third-party tracker lists JET "Free") — but the official
  guide was unreachable (403), so this is **待核实**. Do **not** confuse it with the separate
  **open-access APC of USD 3,130** (hybrid journal; APC applies only if you choose OA after acceptance).
- **Length / abstract caps**: no official limit found — **待核实**.

## Preflight checklist

### Format & source
- [ ] Compiled from **editable `.tex`** in `elsarticle`; no PDF-as-source
- [ ] **Full references inside the abstract**; reference list excludes personal communications
- [ ] JEL classification codes + keywords included (standard Elsevier practice — **待核实** as verbatim rule)
- [ ] Definition/assumption/proposition/theorem/proof structure renders cleanly; cross-refs resolve

### Declarations
- [ ] **Generative-AI use disclosed** (or explicit "none")
- [ ] Conflict-of-interest / funding statements prepared
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
\bibliographystyle{elsarticle-harv} % or elsarticle-num — confirm the required style in the live guide
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
- [ ] Abstract citations written out in full; no `\citet` abbreviations there
- [ ] Figures embedded as vector PDF with fonts embedded
- [ ] Supplementary appendix uploaded as its own file if proofs were offloaded (confirm the
      expected file split against the journal's current author guidelines)

## Output format

```
【Source】editable .tex (elsarticle), no PDF source? [Y/N]
【Abstract refs】cited in full? [Y/N]
【AI disclosure】declared? [Y/N]
【Fee】no submission fee assumed (待核实); APC ≠ fee acknowledged? [Y/N]
【Next】await editor desk screen → jet-review-process
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — elsarticle/LaTeX toolchain
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official JET URLs behind every fact
