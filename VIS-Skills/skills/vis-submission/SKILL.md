---
name: vis-submission
description: Use when auditing an IEEE VIS full-paper submission for PCS readiness, covering the abstract-then-paper two-deadline structure under the VGTC society, the IEEE VGTC/TVCG 9+2 page budget, author-optional double-blind anonymization, the supplemental-material one-week window, and desk-reject triage before the AoE cutoff for a paper that will publish in IEEE TVCG.
---

# VIS Submission

Run this audit before uploading to the **Precision Conference System (PCS)**. IEEE VIS full papers
are published as **journal articles in IEEE TVCG**, so the submission is judged at a journal bar
even though it also earns a conference slot. Every number below was read from the IEEE VIS 2026
Call for Full Papers and Paper Submission Guidelines on 2026-07-09 via search renderings of the
`ieeevis.org` URLs (see `resources/official-source-map.md`); treat them as a one-cycle snapshot and
reopen the live call first.

## The two-deadline structure (abstract, then paper)

VIS separates the **abstract** deadline from the **full-paper** deadline, and both are AoE:

- **Abstract (VIS 2026: 21 March 2026)** locks title, abstract, authors, and area/keyword choices.
  The **author list must be final at this point** — you cannot add authors after it. The abstract
  also drives area routing and reviewer bidding.
- **Full paper (VIS 2026: 31 March 2026)** uploads the PDF. After this, **title, abstract, and the
  main PDF are frozen**.
- **Supplemental material (VIS 2026: 7 April 2026)** has its own later window — a one-week
  extension introduced so authors can finish and properly anonymize videos, data, and code after
  the paper is in. Do not treat it as extra time for the paper itself.

Register the abstract with the *real* title and area, not a placeholder — misrouting to the wrong
of the six areas puts your paper in front of the wrong Area Paper Chair and reviewer pool.

## PCS mechanics

In PCS, at the top of the Submissions tab select society **VGTC**, conference **VIS 2026**, track
**VIS 2026 Full Papers**. Getting the society/track wrong files your paper against a sibling VGTC
venue (VR, ISMAR) or the wrong track. Fill conflicts, the primary area, and keywords carefully —
they determine your reviewers.

## Format and page budget

- **IEEE VGTC / TVCG-conference template**, unmodified. This is the VGTC document class (LaTeX
  template at `github.com/ieee-vgtc/vis-latex-submission-template`; a Typst port exists) — not
  `acmart`, and not a generic two-column IEEEtran habit carried from another IEEE venue.
- **Page budget (verify per cycle):** **up to 9 pages of content** plus **up to 2 pages that
  contain only references and acknowledgements** — the "9+2" budget. Figures, tables, and text all
  count toward the 9; nothing decision-critical can hide in the reference pages.
- Margins, font, and columns are fixed by the template; recover space by editorial compression, not
  by shrinking the template.

## Author-optional double-blind sweep

VIS runs **author-optional double-blind** review: anonymizing is not strictly required, but for
most paper types it is good scientific practice and **strongly recommended** — and once you opt in,
the anonymization must be clean. Because visualization papers lean on systems, demos, videos, and
open-source releases, the leak surface is wide:

```bash
# Mechanical pass on the submission PDF and any supplemental archive
pdfinfo paper.pdf | grep -Ei 'author|creator|producer'
pdftotext paper.pdf - | grep -nEi 'github\.com/[a-z0-9-]+|osf\.io|youtu|acknowledg|grant|our (tool|system|lab)' | head
grep -rniE 'university|@[a-z0-9.]+\.edu|lab name|project url' supplemental/ | head
```

The VIS-specific leaks: a system named after your lab, a demo screenshot showing a username or an
institutional URL, a supplemental video with a spoken affiliation or a visible desktop, a live
GitHub/OSF link that discloses authorship, and a teaser figure watermarked with a project site.
Re-host code, data, and video behind an anonymizing location before upload if you are submitting
double-blind.

## Open practices at submission time

- If your contribution is a technique, system, study, or dataset, prepare the **open materials**
  now (anonymized for review): code, data, stimuli, analysis scripts, and a supplemental video.
- Preregistration, if your study used it, should be cited (anonymously) — it strengthens an
  empirical claim and is surfaced again in the Open Practices form at camera-ready.
- Cache anything you cannot regenerate (model outputs, crowd-study responses) before the deadline.

## Desk-risk triage

| Finding at audit time | Severity | Real fix |
|---|---|---|
| Content over 9 pages | Desk-reject-grade | Cut or move to supplemental; the 2 reference pages do not absorb body text |
| Template altered (margins, shrunk font, wrong class) | Named desk-reject ground | Recompile with the clean VGTC template; recover space editorially |
| Author added after the abstract deadline | Not permitted | Nothing fixes this post-abstract; finalize authorship before 21 March-equivalent |
| Identity leak in a double-blind PDF, video, or repo link | Anonymity violation | Re-anonymize and re-host; scrub PDF and video metadata |
| Supplemental video unplayable / wrong codec | Reviewers cannot assess it | Re-encode to the required format before the supplemental deadline |
| Same work under review at another venue | Dual-submission exposure | Withdraw one; verify the current concurrent-submission wording |

## Final-week order of operations

1. Freeze the paper's argument early; the abstract you register must match the final paper.
2. Submit the abstract with final authors, primary area, and keywords before the abstract cutoff.
3. Build and anonymize the supplemental package (video, code, data) for its own later deadline.
4. Run the mechanical anonymity checks on the *final* PDF and *final* supplemental archive.
5. Confirm PCS society/conference/track selection and every conflict a day early.
6. Re-download the uploaded PDF and view it cold to confirm it is the file you meant.

## Reverify each cycle

- The abstract/paper/supplemental dates and the second-round timeline.
- The page budget and which VGTC/TVCG template revision is required.
- Whether double-blind is optional or mandatory this year, and the anonymization guidance.
- Dual-submission wording and any generative-AI disclosure rule — all cycle-volatile.

## Output format

```text
[VIS submission status] ready / blocked / needs work
[Abstract] title/authors/area/keywords locked by the abstract deadline? yes/no
[PCS] society VGTC / VIS 2026 / Full Papers track selected? conflicts complete?
[Format] pages used (content/refs), VGTC template compliance
[Anonymity] double-blind? clean / leaks: <where, incl. video/repo>
[Open materials] code/data/video prepared and anonymized? yes/no
[Fix queue] <ordered, with owners and dates before the AoE cutoff>
```
