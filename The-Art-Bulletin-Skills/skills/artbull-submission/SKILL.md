---
name: artbull-submission
description: Use when running the final pre-submission preflight for The Art Bulletin — double-blind anonymization, the required Word files (manuscript, abstract, illustrations, captions, cover sheet), word/abstract/illustration caps, Chicago formatting, and the permissions status. Final checks; it does not draft content.
---

# Submission Preflight (artbull-submission)

The last check before e-mailing the submission to **the.art.bulletin@collegeart.org** (or via a
large-file transfer service). The Art Bulletin is **double-blind** and accepts **Microsoft Word
only** — no PDFs, because PDFs cannot be anonymized for review. The most common avoidable failures are
broken anonymity, a PDF submission, and an over-length manuscript. Verify volatile specifics on the
official page first.

## When to trigger

- "Submitting this week" — last pass before sending the files
- Confirming the file set, caps, and anonymization
- Checking that permissions are at least underway (see `artbull-images-and-permissions`)

## Process facts (verify volatile items on the official page)

- **Owner / publisher:** College Art Association (CAA) / Taylor & Francis (Routledge).
- **Submission:** electronic only — **e-mail** (`the.art.bulletin@collegeart.org`) or **large-file
  transfer**; **Microsoft Word, not PDF**.
- **Review model:** **double-blind** — strip all author-identifying information from text and notes.
- **Article length:** **up to 16,000 words including endnotes** (待核实; confirm current cap).
- **Abstract:** **no more than 100 words**; **biographical statement ≤ 50 words** on the cover sheet.
- **Illustrations:** **maximum 20 images** with captions in a **single Word file ≤ 10 MB** at
  submission; **high-resolution files supplied promptly on acceptance**.
- **Style:** **The Chicago Manual of Style**, **endnotes** (CMOS ch. 14); 12-pt, double-spaced.
- **Permissions:** the **author** secures and pays for reproduction rights and photography (fair use
  per the CAA code).
- **Fee:** no submission fee stated; optional open-access **APC** under T&F Open Select after
  acceptance (confirmed as the model 2026-06-22; the APC amount is set by Taylor & Francis — check the
  live T&F page if choosing open access).

## Preflight checklist

### Files (separate Word files)
- [ ] Manuscript (Word, 12-pt, double-spaced, **endnotes**)
- [ ] Abstract (**≤ 100 words**)
- [ ] Illustrations file (single Word file **≤ 10 MB**, **≤ 20 images** with captions)
- [ ] Separate captions/list-of-illustrations file
- [ ] Cover sheet (author, **≤ 50-word bio**, contact, **word count**)

### Anonymity (double-blind)
- [ ] No author name/affiliation/acknowledgments in manuscript or notes
- [ ] Self-citations neutralized (no "as I argued in…")
- [ ] **Submitted as Word, not PDF** (so the office can anonymize)
- [ ] Identifying **file metadata stripped** (document properties)

### Length, style & images
- [ ] Article ≤ ~16,000 words **including endnotes**
- [ ] Chicago notes/endnotes; "Figure n" references consistent; full credit-line captions
- [ ] Permissions secured or clearly underway; high-res image plan ready for acceptance

## Anti-patterns

- Submitting a **PDF** (cannot be anonymized — breaks the process)
- Leaving author identifiers in text, notes, or file metadata
- Over 16,000 words once endnotes are counted; abstract over 100 words
- More than 20 illustrations or an illustration file over 10 MB
- Treating permissions as a post-acceptance problem only

## Desk-reject and return-without-review triggers at this venue

The College Art Association's quarterly can return a manuscript before review when the form makes
review impossible or the fit is wrong.

| Trigger | Why it stops the paper here | Preflight fix |
|---|---|---|
| Submitted as PDF | A PDF cannot be anonymized for double-blind review | Submit Microsoft Word only |
| Author identifiers / metadata | Names, "as I argued in…," or document properties reveal the author | Strip from text, notes, and properties pane |
| Over length | Endnotes counted push the manuscript past the cap | Trim apparatus; recount with endnotes included |

## Worked vignette: the preflight that caught three silent failures

Suppose an author is ready to e-mail an article on a Baroque ceiling program. The preflight finds three
problems invisible in a casual read. The **document properties** still carry the author's name from a
re-save — a metadata leak that would breach the double-blind process. The word count "passed" only
because the author forgot the **endnotes**, whose dense apparatus pushes the total over the long-form
cap. And the illustrations were spread across two Word files, not the single file the office expects,
with one over the size limit. None of these touches the argument, yet all three could trigger a return
without review; the author clears the metadata, recounts and trims the notes, and consolidates the
plates into one file.

## Calibration anchor (hedge where uncertain)

- The most common avoidable failures here are a PDF submission, broken anonymity (text, notes, or
  metadata), and an over-length manuscript once endnotes are counted — verify every volatile cap on the
  journal's current submission guidelines, and stage the author-funded high-resolution images for
  acceptance.

## Output format

```
【Files】manuscript · abstract · illustrations · captions · cover sheet — all Word? [Y/N]
【Anonymized】text + notes + metadata clean; Word not PDF? [Y/N]
【Length】words incl. endnotes ≤ 16,000? abstract ≤ 100? bio ≤ 50? [Y/N]
【Illustrations】≤ 20 images, file ≤ 10 MB? [Y/N]
【Style】Chicago endnotes + captions/credit lines? [Y/N]
【Permissions】secured/underway + high-res plan? [Y/N]
【Next】await decision → artbull-revision-and-response on R&R
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — anonymization, Chicago, and image-prep tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official Art Bulletin / CAA submission facts and 待核实 markers
