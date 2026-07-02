---
name: jacs-submission
description: Use when running the final pre-submission preflight for a Journal of the American Chemical Society (JACS) manuscript via ACS Paragon Plus — files, TOC graphic, SI, CIFs/CCDC, disclosures, and format. Runs the submission checklist — it does not improve the science or prose.
---

# Pre-Submission Preflight (jacs-submission)

## When to trigger

- "We're submitting today" — last check before the Paragon Plus upload
- You are unsure which files Paragon Plus expects
- You need a final, mechanical gate on format, SI, and disclosures

## Pre-submission checklist

### Files and system

- [ ] Manuscript in ACS Word or LaTeX template format
- [ ] Separate **Supporting Information** PDF
- [ ] **CIF** files for all crystal structures; CCDC numbers obtained and cited
- [ ] **TOC / abstract graphic** prepared per ACS size/content rules
- [ ] Figures at ACS-specified resolution/format; embedded or uploaded as required
- [ ] Submitting via **ACS Paragon Plus** with a registered account

### Format

- [ ] Title, author list, affiliations, corresponding author(s) correct
- [ ] ORCID linked for authors as required
- [ ] Abstract within format norms; TOC graphic matches the abstract's message
- [ ] Citations in **ACS numbered style**, in order, with abbreviated journal titles
- [ ] Compound numbering consistent across text, schemes, and SI
- [ ] Article type (Article / Communication) selected to match the manuscript

### Characterization and data (rigor gate)

- [ ] Every new compound: full characterization + purity evidence in SI
- [ ] Copies of key spectra (¹H, ¹³C, diagnostic others) in SI, legible
- [ ] Chiral/HPLC traces for stereochemistry/purity claims
- [ ] checkCIF/PLATON addressed; CCDC numbers correct
- [ ] Mechanism/catalysis claims supported by controls/kinetics/labeling as stated
- [ ] Computational coordinates and details in SI if computation is used

### Disclosures and integrity

- [ ] Cover letter included (advance + fit)
- [ ] Conflict-of-interest statement per ACS policy
- [ ] Funding/acknowledgments handled (kept out of double-blind text if applicable)
- [ ] Data availability statement present
- [ ] Preprint / prior / companion-paper disclosure if applicable
- [ ] Safety hazards disclosed for dangerous reagents/procedures
- [ ] No image manipulation beyond uniform, disclosed adjustments

### Reviewers

- [ ] Suggested reviewers entered (independent, no conflicts)
- [ ] Excluded reviewers entered with brief justification, if any

> Confirm the **current** required files, limits, and policies on the JACS author
> page in Paragon Plus before submitting; specifics change over time.

## Paragon Plus operation notes

- Upload main text, SI, CIFs, and graphics in the slots Paragon Plus designates.
- Verify the assembled proof PDF renders all figures, schemes, and Greek/math correctly.
- Enter ORCID, conflicts, funders, and reviewer suggestions in the system fields.
- Keep file sizes within the portal limits; check the generated PDF before approving.

## Assembled-proof audit (the last human read)

The merged PDF that Paragon Plus builds is what the editor first sees. Read it
end-to-end once, hunting only for assembly damage:

- [ ] Superscripts/subscripts survived conversion (¹³C, m/z, R1/wR2, °C, Å, δ)
- [ ] ChemDraw schemes rasterized sharply; wedge/hash bonds still distinguishable
- [ ] Bold compound numbers stayed bold in captions and tables
- [ ] Cross-references resolve — no "Scheme ??", no SI pointer to a section that moved
- [ ] TOC graphic sits in its slot, uncropped, text legible at printed size
- [ ] SI page numbering continuous; SI table of contents matches actual sections
- [ ] CCDC numbers in text match the deposited CIF filenames one-to-one

## Timeline discipline (avoid same-day chaos)

- **Days before:** deposit CIFs with the CCDC and obtain numbers; run checkCIF;
  collect every co-author's ORCID and conflict statement; confirm the reviewer
  list with the corresponding author.
- **Day before:** freeze compound numbering; regenerate the SI PDF from the
  frozen text so spectra order matches; verify HRMS calcd/found pairs against
  the final structures one last time.
- **Submission day:** only mechanical steps remain — uploads, metadata, proof
  audit, approve. If a chemistry-content edit surfaces on submission day, stop
  and loop back to `jacs-methods` or `jacs-writing-style`; do not patch in the portal.

## What triggers a bounce-back before review

- Abstract/TOC graphic mismatch — the graphic shows chemistry the abstract never claims
- A CIF that fails checkCIF with unexplained A-level alerts
- SI referenced in the text ("see Figure S12") but the figure absent from the uploaded SI
- Corresponding-author email that differs between the manuscript and the portal record

## Anti-patterns

- Submitting with CIFs undeposited or CCDC numbers as placeholders
- SI missing spectra copies for some compounds
- "Data available on request" instead of a real availability statement
- TOC graphic that violates ACS size rules or doesn't show the chemistry
- Non-ACS reference formatting left from a reference manager
- Forgetting the cover letter or the conflict/funding disclosures

## Output format

```
【Files】manuscript / SI / CIFs / TOC graphic — present? [...]
【Format】ACS template, citations, numbering — OK / fix: [...]
【Rigor gate】characterization + CCDC + mechanism support — OK / gaps: [...]
【Disclosures】COI / funding / data / preprint / safety — OK / missing: [...]
【Reviewers】suggested / excluded — entered? Y/N
【Verdict】ready to submit / blockers: [...]
【Next】await decision → jacs-revision
```

## Related resources

- [`templates/checklist.md`](templates/checklist.md) — full pre-submission self-check by section
- [`templates/manuscript_template.md`](templates/manuscript_template.md) — JACS-style manuscript skeleton (Article/Communication, SI structure)
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — Paragon Plus, CCDC deposition, ACS templates and styles
