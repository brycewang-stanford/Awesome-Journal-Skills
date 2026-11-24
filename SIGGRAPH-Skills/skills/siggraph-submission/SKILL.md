---
name: siggraph-submission
description: Use when auditing an ACM SIGGRAPH / SIGGRAPH Asia Technical Papers submission for Linklings readiness, covering the two-step form-then-upload deadline, the acmart (>=2.16) format and the 7-page conference-track budget, the dual-track vs Journal-only choice, the mandatory representative image and supplemental video, and desk-risk triage before the UTC cutoff.
---

# SIGGRAPH Submission

Run this audit before you finalize on the SIGGRAPH **Linklings** site. A SIGGRAPH Technical
Paper is a **journal article in ACM Transactions on Graphics (TOG)** that also earns a
conference presentation slot, so the package is judged to a journal bar while moving on a
conference clock. Every number below was read from the SIGGRAPH 2026 technical-papers call,
anonymity policy and submissions FAQ (first on 2026-07-09, re-verified directly on 2026-11-24; see
`resources/official-source-map.md`); treat them as a one-cycle snapshot and reopen the live call
first. As of 2026-11-24 SIGGRAPH 2027 has posted only its deadlines (form 21 Jan, paper 28 Jan,
upload 29 Jan 2027, 22:00 UTC), not its full call. Note SIGGRAPH runs **two cycles a year** — SIGGRAPH North America (deadline ~January) and
SIGGRAPH Asia (deadline ~May) — so confirm which one you are targeting.

## The two-step deadline

SIGGRAPH separates the **submission form** from the **paper upload**, and both are hard UTC
cutoffs, not AoE:

- **Submission form** locks title, abstract, topic areas, and the *complete* co-author list
  (SIGGRAPH 2026: **15 January 2026, 22:00 UTC/GMT**). After this the author list can no longer be
  edited and no new submissions can be created — a missed form deadline means no paper exists.
- **Paper deadline** takes the paper PDF (or an MD5 checksum of it), the representative image and
  all supplemental materials (SIGGRAPH 2026: **22 January 2026, 22:00 UTC/GMT**).
- **Upload and conflicts deadline** one day later accepts only files matching the registered MD5
  checksums, and every co-author must have entered conflicts and expertise keywords — a paper with
  no conflicts is automatically rejected (SIGGRAPH 2026: **23 January 2026, 22:00 UTC/GMT**).
  SIGGRAPH Asia uses the same stages (2026: form 5 May, paper 12 May, upload 13 May, 23:59 AoE).

The MD5-checksum option lets you freeze the PDF at the paper deadline and upload the exact bytes by
the upload deadline; the checksum you register must match the file you upload.

## Format and page budget

- **ACM `acmart` class, version 2.16 or higher** — earlier template versions produce an *invalid*
  submission and are a mechanical reject. This is the `acmtog` double-column journal format; it is
  not IEEEtran and not the `sigconf` format you may know from other ACM venues. Submit with
  `\documentclass[acmtog,anonymous,review]{acmart}` and `\acmSubmissionID{<paper ID>}`; the paper
  itself must be Adobe PDF, and LaTeX packages must be on the TAPS accepted list.
- **Conference-track / dual-track page budget:** **<= 7 pages excluding references and figures-only
  pages**, with **at most two figures-only pages** placed *after* the references (graphical
  material and captions only — no tables or body text smuggled in). The reference list itself has
  **no length limit**. **Journal-only** submissions have **no maximum (or minimum) length**
  (typical 8-12 pages without references) and are held to TOG's completeness bar.
- Number every page and stamp your paper ID (obtained from the submission form) on each page.

## Anonymity — SIGGRAPH Technical Papers are double-blind

The 2026 call states that "the SIGGRAPH review process is double-blind". Concretely: no names or
affiliations, **no acknowledgements** (add them back at camera-ready), clean PDF metadata, no
recognisable author voice narrating the video, and anonymous supplemental and code. Cite your own
published work in the third person; cite overlapping work under review elsewhere anonymously and
upload it as anonymous review-only supplemental; do **not** cite a public arXiv version of this
same paper — list it in the form's hidden "Prepublication" field. The anonymity policy also bans
project pages, PR and social-media publicity from two weeks before the deadline until the decision;
posting to arXiv is allowed if it does not mention SIGGRAPH or use the ACM TOG format. Direct
anonymity breaks are desk-rejected.

## Generative AI disclosure

The ACM Policy on Authorship applies: disclose any use of generative-AI tools that generated new
content (beyond grammar correction). Citations to non-existent material get a paper rejected,
possibly without review — verify every reference.

## Dual-track vs Journal-only — decide before you write the last section

Every submission is either **dual-track** (eligible to be published as a Journal/TOG paper *or* a
Conference paper) or **Journal only**. Dual-track is the default for most authors: it keeps the
lighter-validation Conference outcome available for earlier-stage or riskier work rather than
forcing an all-or-nothing Journal verdict. Choose Journal-only only when a Conference-track
publication would not serve the work. The committee, not you, assigns the final track at accept
time (see `siggraph-review-process`).

## Supplemental materials — the video is not optional

SIGGRAPH evaluates *results*, and results in graphics are temporal and visual. Plan the
supplemental package as a first-class deliverable, not an afterthought:

- **Representative image** — a single still that will front the paper in the program; required.
- **Supplemental video** — the reviewers' primary evidence for animation, simulation, rendering,
  and interaction claims. You must hold **permissions for every image in the paper and every frame
  of the video at submission time**.
- **Code, data, and additional results** — uploaded as supplemental material; appendices go here,
  not in the 7-page body. Keep the companion video to **five minutes or less**, use MP4 / JPG / PNG,
  and stay under about **500 MB** in total (beyond that, reviewers are not guaranteed to look).
  Supplemental comes in two parts: (A) material that will be published in the ACM DL and (B)
  review-only material such as anonymized overlapping papers and an anonymous cover letter.

```bash
# Mechanical pre-upload pass on the PDF and the supplemental bundle
pdfinfo paper.pdf | grep -Ei 'title|pages'
pdffonts paper.pdf | grep -i 'no'          # catch un-embedded fonts (Type3/no-embed) -> production reject
ffprobe -hide_banner supplemental.mp4 2>&1 | grep -Ei 'codec|duration|resolution'
du -h supplemental/*                        # confirm each file is under the portal size cap
```

## Desk-risk triage

| Finding at audit time | Severity | Real fix |
|---|---|---|
| `acmart` older than v2.16 | Mechanical reject | Recompile against the current class; do not patch the .cls |
| Conference-track body over 7 pages (refs/figure-pages excluded) | Over-length reject | Cut, or move figures to the two figures-only pages; refs do not absorb body text |
| A third figures-only page, or tables/text on a figures page | Format violation | Restructure into <=2 figures-only pages, graphical content only |
| No supplemental video for a temporal/visual result | Scored against you | Produce the results video; static frames cannot show motion/interaction |
| Missing permissions for a video frame or figure | Ethics/production block | Re-shoot, replace, or clear rights before upload |
| Author list wrong after the form deadline | Uneditable | Nothing fixes this post-form-deadline — lock authors before it |
| Paper ID not on every page | Handling error | Regenerate the PDF with the ID stamped |
| Names, acknowledgements, identifying repo URL or PDF metadata | Desk reject (anonymity) | Use the `anonymous,review` options, strip metadata, anonymize repos |
| No conflicts entered by a co-author at the upload deadline | Automatic reject | Have every co-author enter conflicts and expertise keywords in Linklings |

## Final-week order of operations

1. Freeze the body early; the argument and the results figures cannot churn in the last 48 hours.
2. Complete the **submission form** (title/abstract/topics/all co-authors) well before its earlier
   deadline; register the MD5 checksum if you plan to freeze bytes.
3. Render the final results video and the representative image; verify permissions on every asset.
4. Run the mechanical PDF/video checks on the *final* files, not drafts.
5. Fill every Linklings field — topic areas that match your evidence, conflicts for every
   co-author's institution and recent collaborators — a day early.
6. Re-download the uploaded PDF and video and inspect them cold to confirm they are the files you
   meant.

## Reverify each cycle

- Which cycle you are in (SIGGRAPH vs SIGGRAPH Asia) and its exact UTC cutoffs.
- The required acmart revision and the current Conference-track page budget.
- The anonymity policy and embargo window (2026: double-blind; embargo from two weeks before the
  deadline).
- Supplemental size guidance (2026: about 500 MB), video length (2026: five minutes or less), and
  the generative-AI disclosure wording.

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue siggraph-skills   # from a clone of the AJS repository
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

## Output format

```text
[SIGGRAPH submission status] ready / blocked / needs work
[Cycle] SIGGRAPH 20XX (Jan) / SIGGRAPH Asia 20XX (May)
[Form] title/abstract/topics/all authors locked by the earlier deadline? yes/no
[Format] acmart >=2.16? body pages (conf-track <=7)? figures-only pages <=2?
[Track] dual-track / journal-only
[Supplemental] representative image? results video? permissions cleared?
[Fix queue] <ordered, with owners and dates before the UTC cutoff>
```
