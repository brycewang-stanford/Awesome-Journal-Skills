---
name: anmath-submission
description: Use when running the final pre-submission preflight for an Annals of Mathematics manuscript — AMS-LaTeX compile, theorem environments, abstract and MSC, references, arXiv, figures, and portal logistics. Checks readiness; does not assess significance (anmath-scope-fit) or correctness (anmath-referee-strategy).
---

# Pre-Submission Preflight (anmath-submission)

## When to trigger

- "I'm submitting tomorrow"
- Final check before clicking submit on the portal
- Unsure what files and metadata the submission system needs

> Verify all volatile specifics (portal URL, accepted formats, length expectations, whether
> a cover letter is collected) on the journal's official submission page first — these change.

## Preflight checklist

### TeX and format

- [ ] Source compiles cleanly with a standard distribution; no errors, no missing refs
- [ ] AMS environments used (`amsthm` for theorem/lemma/proposition/definition/remark/proof)
- [ ] A single, consistent theorem-numbering scheme throughout
- [ ] All cross-references (`\cref`/`\eqref`) resolve; no "??" in the PDF
- [ ] Submitted PDF is the version produced by the source you will provide on acceptance

### Front matter

- [ ] Title, author(s), affiliations, and contact consistent with portal entries
- [ ] Abstract present, self-contained, states the Main Theorem in plain terms
- [ ] MSC subject classification: primary + secondary, matching the headline result
- [ ] Keywords (if requested) chosen to match the area
- [ ] Acknowledgments and funding stated as the journal requires

### Mathematical content

- [ ] Main Theorem stated precisely and early (see anmath-results-framing)
- [ ] Proof complete and gap-free; no unresolved "clearly"/"it is easy to see"
- [ ] Every external result invoked is published and precisely cited
- [ ] No essential step rests on an unpublished/unverifiable claim
- [ ] Computer-assisted steps (if any) documented with archived code/data

### Proof-risk pass

- [ ] Each "standard" argument points to an exact theorem, lemma, or appendix proof
- [ ] Boundary cases, degenerate cases, and parameter exclusions are either proved or explicitly ruled out
- [ ] Notation introduced for one local proof is not reused with a conflicting meaning later
- [ ] Any computer-assisted verification has a human-readable statement of what was certified

### References

- [ ] Bibliography uses consistent style (BibTeX, MathSciNet abbreviations / `\MR`)
- [ ] Every citation in text appears in the bibliography and vice versa
- [ ] Preprints labeled as such; replace with version-of-record where available
- [ ] Closest prior results cited with correct authors and statements

### Figures / diagrams (if any)

- [ ] Vector format (PDF/EPS); labeled; referenced in text; genuinely necessary
- [ ] Commutative diagrams typeset with `tikz-cd`/`amscd`, arrows consistent

### Logistics

- [ ] arXiv preprint id ready to declare (if you posted one)
- [ ] Cover letter prepared if the portal requests it (see anmath-cover-letter)
- [ ] File size / format within portal limits
- [ ] Coauthors have approved the final version

## Submission system notes (verify currency)

- Submission is electronic; check the official page for the current portal and the exact
  upload format (compiled PDF for review; TeX source typically requested on acceptance).
- Be prepared for a long review — detailed proof verification can take a year or more.
- Keep the exact submitted source under version control for later `latexdiff` revisions.

## Anti-patterns

- Submitting a PDF that does not match the source you will later provide
- Broken cross-references ("Theorem ??") left in the compiled file
- Missing or mismatched MSC classification
- Bibliography in a default reference-manager style, inconsistent abbreviations
- Citing a preprint for an essential step that has since been superseded or withdrawn
- Discovering the portal wanted a cover letter only at the upload step

## Output format

```
【Compiles cleanly】yes / no
【Abstract + MSC】present / missing: ...
【Proof gaps】none / BLOCKER: ...
【References】in-text↔bib reconciled; preprints labeled
【Figures/diagrams】none / vector & referenced
【arXiv id】... / none
【Cover letter】prepared / not required
【Next step】anmath-referee-strategy (stress-test) → submit; then await report → anmath-revision
```

## Associated resources

- [`templates/manuscript_template.md`](templates/manuscript_template.md) — AMS-style manuscript skeleton (front matter, theorem environments, sectioning, references)
- [`templates/checklist.md`](templates/checklist.md) — 8-section pre-submission self-check
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — TeX/AMS packages, MathSciNet/zbMATH, proof assistants, diagram tools
