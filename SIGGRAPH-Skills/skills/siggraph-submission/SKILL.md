---
name: siggraph-submission
description: Use when auditing an ACM SIGGRAPH / SIGGRAPH Asia Technical Papers submission for Linklings readiness, covering the two-step form-then-upload deadline, the acmart (>=2.16) format and the 7-page conference-track budget, the dual-track vs Journal-only choice, the mandatory representative image and supplemental video, and desk-risk triage before the UTC cutoff.
---

# SIGGRAPH Submission

Run this audit before you finalize on the SIGGRAPH **Linklings** site. A SIGGRAPH Technical
Paper is a **journal article in ACM Transactions on Graphics (TOG)** that also earns a
conference presentation slot, so the package is judged to a journal bar while moving on a
conference clock. Every number below was read from the SIGGRAPH 2026 technical-papers call and
submissions FAQ on 2026-07-09 via search renderings (see
`resources/official-source-map.md`); treat them as a one-cycle snapshot and reopen the live call
first. Note SIGGRAPH runs **two cycles a year** — SIGGRAPH North America (deadline ~January) and
SIGGRAPH Asia (deadline ~May) — so confirm which one you are targeting.

## The two-step deadline

SIGGRAPH separates the **submission form** from the **paper upload**, and both are hard UTC
cutoffs, not AoE:

- **Submission form** locks title, abstract, topic areas, and the *complete* co-author list
  (SIGGRAPH 2026: **15 January 2026, 22:00 UTC/GMT**). After this the author list can no longer be
  edited and no new submissions can be created — a missed form deadline means no paper exists.
- **Complete submission** uploads the paper PDF (or an MD5 checksum of it) plus all supplemental
  materials and resolves conflicts (SIGGRAPH 2026: **23 January 2026, 22:00 UTC/GMT**). SIGGRAPH
  Asia uses a two-stage variant (abstract/registration, then full paper — 2026 Stage-2 paper
  deadline 12 May, upload 13 May).

The MD5-checksum option lets you freeze the PDF at the form deadline and upload the exact bytes by
the later deadline; the checksum you register must match the file you upload.

## Format and page budget

- **ACM `acmart` class, version 2.16 or higher** — earlier template versions produce an *invalid*
  submission and are a mechanical reject. This is the `acmtog` journal format lineage; it is not
  IEEEtran and not the two-column conference `sigconf` you may know from other ACM venues.
- **Conference-track / dual-track page budget:** **<= 7 pages excluding references and figures-only
  pages**, with **at most two figures-only pages** placed *after* the references (graphical
  material and captions only — no tables or body text smuggled in). The reference list itself has
  **no length limit**. Journal-track papers are held to TOG's completeness bar rather than a hard
  page cap — confirm the current-cycle wording.
- Number every page and stamp your paper ID (obtained from the submission form) on each page.

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
  not in the 7-page body.

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
- Whether review is single-blind (historically yes) or anonymized this cycle — **待核实**.
- Supplemental size limits, video codec/length rules, and any generative-AI disclosure policy.

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
