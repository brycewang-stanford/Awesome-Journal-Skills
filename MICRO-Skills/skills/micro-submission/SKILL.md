---
name: micro-submission
description: Use when auditing a MICRO submission before HotCRP upload — the 11-page-plus-references limit with no appendix allowed, EDT (not AoE) deadline arithmetic, the abstract-registration gate a week before the paper, minimum 9pt fonts, mandatory page numbers, all-author reference entries, and MICRO's visual-plus-automated format inspection.
---

# MICRO Submission

Run this audit against the exact PDF headed to HotCRP. Anchors below are the MICRO
2026 (59th) cycle — CFP and submission guidelines at `microarch.org/micro59/submit/`,
checked 2026-07-08. Every number is a snapshot; reopen the current cycle's pages.

## Three traps that are specifically MICRO's

1. **Deadlines run on US Eastern time.** MICRO 2026 closed abstracts on March 31 and
   papers on April 7, each at 11:59 PM **EDT**. Authors trained on AoE venues lose up
   to a working day by assuming AoE. Convert to every co-author's timezone in writing
   during deadline week.
2. **The abstract deadline is a registration gate, one week early.** No abstract in
   HotCRP by the first date means no paper submission at all. Register placeholders
   for every plausible paper; withdrawing is free, adding late is impossible.
3. **No appendix. At all.** The 2026 guidelines allow at most 11 pages of content
   plus unlimited references — and explicitly permit **no appendix**. Anything you
   planned to park after the references must be cut, absorbed into the 11 pages, or
   moved to an anonymized artifact repository (see `micro-supplementary`).

## Format gate table (2026 guidelines)

| Rule | 2026 setting | Enforcement |
|---|---|---|
| Content length | ≤ 11 pages, everything except references | Inspected; overlength rejected |
| References | Unlimited pages | Must name **all authors — no "et al."** per entry |
| Appendix | Forbidden | No parking space exists |
| Fonts | Minimum 9pt everywhere, figures included | Checked visually, not just by tool |
| Page numbers | **Required** on the submission | Unusual — most venues strip them |
| Template | MICRO 2026 LaTeX template strongly encouraged | Geometry edits and `\vspace` squeezing barred |
| Inspection | Visual **and** automated | Passing the HotCRP format checker is *not* clearance |

The last row deserves emphasis: the guidelines state submissions can be rejected for
format violations *even if* the HotCRP check passed. Treat the checker as a smoke
test, then eyeball a printed copy — tiny axis labels on plots are the classic kill.

## Anonymity, MICRO flavor

- Double-blind review, maintained through the rebuttal/revision window.
- Artifact links (e.g., a GitHub repository) must be **fully anonymized, or
  removed** if they cannot be — the 2026 guidelines say both halves explicitly.
- No acknowledgments section in the submission: no people, no funding agencies.
- Self-citations in third person; scrub PDF metadata, embedded paths, and simulator
  config files inside any linked artifact that carry usernames or lab hostnames.

## Mechanical pre-flight

```bash
# page count and font floor
pdfinfo paper.pdf | grep Pages
pdffonts paper.pdf | awk 'NR>2 {print $1}' | sort -u        # spot rasterized/tiny fonts manually
# page numbers present? (render page 2 footer and look)
pdftotext -f 2 -l 2 paper.pdf - | tail -3
# reference hygiene: no "et al." allowed inside entries
grep -n "et al" references.bib && echo "FIX: expand all author lists"
# identity leakage
pdftotext paper.pdf - | grep -inE "(our (prior|previous) work|anonymous|acknowledg)"
exiftool paper.pdf | grep -iE "author|creator"
```

## HotCRP sequencing for deadline week

1. **T-8 days (abstract deadline):** register title, abstract, authors, topics,
   conflicts. Topic checkboxes drive reviewer assignment — pick for the mechanism,
   not the application domain.
2. **T-3:** freeze the evaluation; regenerate all figures from the run archive so
   the artifact and the PDF cannot disagree later at AE time.
3. **T-1:** full format pass (table above) on the final PDF; print pages with the
   densest figures and check 9pt compliance by eye.
4. **T-0, hours early in EDT terms:** upload, confirm HotCRP shows the final PDF
   (re-download it and diff checksums), and have a second author log in
   independently to verify the submission state.

## What the abstract registration should actually contain

The T-8 abstract is not a formality — reviewers bid on it and topic-matching runs
from it. Three failure modes to avoid at the registration gate:

- **Placeholder prose** ("we study caches") attracts mismatched bidders whose
  eventual reviews read the paper against the wrong literature.
- **Overclaiming the final numbers** before the sweep finishes — the PDF must
  deliver the abstract's promise, and the HotCRP abstract should be updated to
  match the final PDF before the paper deadline.
- **Wrong topic checkboxes.** Pick the mechanism area (memory hierarchy, branch
  prediction, accelerators, security) over the application domain (ML, graphs) —
  the mechanism community is who you want reviewing.

Conflicts deserve the same care at registration: advisors, recent co-authors, and
institutional conflicts declared per the form's definitions. A conflict discovered
after assignment is an integrity incident, not a paperwork fix.

## Also decide: main track or Industry Track

MICRO 2026 opened an inaugural **Industry Track** with its own CFP and a review
process tailored to production constraints (`micro59/submit/industrial.php`). If the
paper's value is deployment evidence rather than a new general mechanism, route it
there deliberately — do not let a production paper be judged by main-track novelty
rules. Track-specific deadlines and rules: 待核实 against the live page.

## If something goes wrong at the wire

- **HotCRP shows "draft" at T-minus-minutes:** an unfinished required field is
  the usual cause — the form, not the PDF. Fill, save, re-check the state label.
- **The format checker rejects a compliant PDF:** rebuild with the untouched
  template class file; embedded Type-3 fonts from a figure pipeline are the
  common trigger. Do not "fix" it by altering template geometry.
- **A co-author spots an identity leak post-deadline:** do not silently update
  anything; email the program chairs immediately — self-reporting a leak is
  survivable, discovery is not.
- **Missed the abstract gate entirely:** there is no paper this cycle. Move
  straight to the lattice in `micro-workflow` and book the next venue's window.

## Output format

```text
[Upload verdict] go / no-go (blocking items listed)
[Clock] deadline in EDT: <local equivalents per author>
[Abstract gate] registered by T-7: yes / no
[Pages] content: N/11 · references: N (unlimited) · appendix present: must be "no"
[Format] 9pt floor / page numbers / template intact / no vspace hacks: pass-fail each
[References] entries with "et al.": N (must be 0)
[Anonymity] artifact links anonymized-or-removed / metadata clean / no acks: pass-fail
[Track] main / industry — one-line justification
```
