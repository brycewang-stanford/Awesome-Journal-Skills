---
name: psychrev-submission
description: Use when running the final pre-submission preflight for a Psychological Review manuscript — Editorial Manager portal, APA format and length, abstract, masking, references, ethics, and (for computational models) sharing the author's own model code. Theory journal; there is no empirical data-availability/replication-package step.
---

# Pre-Submission Preflight (psychrev-submission)

> Psychological Review is a theory journal. There is no experimental dataset or empirical
> replication package to deposit. The preflight centers on the *theory paper's* format,
> the review-mode choice (open by default, masked on request), APA style, and — for computational models — sharing the author's **own model
> code** (not a shared empirical-analysis kit). 检索于 2026-06；以官网为准.

## When to trigger

- "I'm about to submit to Psychological Review"
- Final check before clicking submit in Editorial Manager
- Unsure which files the portal expects for a theory/modeling paper

## Pre-submission checklist

### Scope & fit
- [ ] The paper makes a **theoretical contribution** (new theory / formal model / synthesis), not an empirical report
- [ ] Data appear only to **motivate or constrain** the theory; no new experiment is the contribution
- [ ] It enters and evaluates standing theories ("systematic evaluation of alternative theories")
- [ ] Fit confirmed against the current Psychological Review aims & scope (verify on the official page)

### Format (verify exact current requirements on the APA author page)
- [ ] **APA 7th-edition** formatting: double-spaced, 12-pt (e.g., Times New Roman), 1-inch margins (verify edition)
- [ ] **Title page** with all authors, affiliations, ORCID iDs, contact (if you opt for masked review, these go only in the cover letter)
- [ ] **Abstract ≤ 250 words** on a separate page, followed by **up to five keywords** (APA submission guidelines, re-verified 2026-11-24)
- [ ] No fixed upper length, but texts **> 15,000 words** carry a justification for the length
- [ ] Equations numbered; figures meet APA resolution/format specs; figures are diagrams/simulations, not experiments
- [ ] Manuscript file in **Word / Open Office** format (LaTeX: .tex + .bib/.bbl in a ZIP plus a PDF)
- [ ] If any empirical work or quantitative analysis is reported: a **"Transparency and openness"** subsection in the Method meeting the TOP **disclosure** level (data/code/materials availability; whether any work was preregistered)

### Masking (only if you choose masked review — open review is the default)
- [ ] No author-identifying content in the manuscript body
  - Self-citations phrased neutrally ("prior work (Author, 2020)"), not "in our earlier paper"
  - Acknowledgments/funding identifiers kept out of the body (added after acceptance)
- [ ] Document file properties scrubbed of author name/affiliation; file names carry no author/institution

### References & citations
- [ ] **APA 7th** author–date in-text citations; full reference list (verify edition; see source map)
- [ ] Every in-text citation appears in the reference list and vice versa
- [ ] The current, strongest form of each rival model is cited (not only its original version)
- [ ] All references are real and accurately quoted (no fabricated or mis-cited sources)

### Model code (computational/formal models)
- [ ] The author's **own model code** (simulation/fitting scripts) prepared for sharing per APA/journal policy
- [ ] Code reproduces the simulation figures and reported fits; parameters and seeds documented
- [ ] A README states language/version, how to run, and what each script produces
- [ ] (This is the model's code, NOT a shared empirical-analysis pipeline — there is no dataset to deposit)

### Ethics & originality (APA Ethics Code)
- [ ] Manuscript is original, unpublished, and not under review elsewhere
- [ ] Authorship reflects genuine intellectual contribution; order agreed by all authors
- [ ] Any prior conference/preprint version disclosed as required; generative-AI use in drafting **disclosed in the method section and cited** (AI cannot be an author — APA policy)
- [ ] Similarity/overlap acceptable and self-overlap disclosed

### Portal files (Editorial Manager)
- [ ] Main manuscript (body + figures + references), masked only if you chose masked review
- [ ] Separate title page with author info and corresponding author
- [ ] Model code / supplemental files if applicable; cover letter if requested
- [ ] Any author-agreement or conflict-of-interest forms the system requires

## Desk-reject triggers to preempt

1. **It's an empirical paper** (the data is the contribution) — the defining Psychological Review desk-reject.
2. **A literature survey / methods-and-design paper** — explicitly out of scope.
3. **A "model" that only redescribes data** with free parameters and no falsifiable commitment.
4. **Insufficient theoretical advance** — a relabel, a refit, or an incremental extension.
5. **Formatting failures** (or identity leaks after choosing masked review), or over-length with no justification.

## Editorial Manager operation notes

- Psychological Review submits via **Editorial Manager** (editorialmanager.com/rev — confirm the exact URL; see source map).
- Choose open (default) or masked review; if masked, enter author metadata only in the system and cover letter, never in the manuscript.
- Choose the correct article type (Theoretical article vs. Theoretical Note).
- **Fees**: submitting for peer review is free of charge; an APC applies only if you choose gold open access (APA submission guidelines, re-verified 2026-11-24).

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue psychological-review-skills   # from a clone of the AJS repository
```

It reports, with a location for each finding:

- this venue's machine-readable limits, review mode and required statements, when the venue has a
  rules block (`--list-venues`);
- citations ↔ references;
- table and figure numbering, cross-references and standard-error notes;
- abstract numbers traced to the tables;
- placeholders and tracked changes.

With the Research Toolkit pack installed, `rt-submission-readiness` runs the same check as stage 0
of the full pre-submission pipeline (scorecard → referee panel → polish → cover letter). Anything
it lists as *not checked* still needs the manual items below.

## Anti-patterns

- Submitting a paper whose real contribution is data or method
- Author identity leaking through "our prior study," acknowledgments, or file properties
- Reference list missing the current form of the rival models
- Figures that are experiments (impossible here) or undefined boxes-and-arrows
- For a computational model, withholding the model code reviewers will ask for

## Output format

```
【Scope】theoretical contribution, data only constrains: yes / fix
【Format】APA 7th / abstract ≤ 250 / length justified if > 15k / figures conceptual: pass / fix
【Review mode】open (default) / masked; if masked, body + properties + filenames clean: yes / fix
【References】APA 7th; rivals' current form cited; all real: yes / fix
【Model code】own simulation/fitting code prepared + README (if computational): yes / n-a
【Ethics】original, not under review, authorship correct, AI disclosed: yes / fix
【Portal files】MS (masked if chosen) + title page/cover letter + code/forms: complete / missing [...]
【Next step】await decision → psychrev-review-process; revise → psychrev-rebuttal
```

## Related resources

- [`templates/checklist.md`](templates/checklist.md) — 8-section pre-submission self-check (scope / format / optional masking / abstract / theory / figures-code / references / ethics & portal)
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — Theory/modeling tools (citation mapping, reference managers, modeling environments, diagram software, argument-logic aids)
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — Official APA Psychological Review scope, format, and portal facts (with verification dates)
