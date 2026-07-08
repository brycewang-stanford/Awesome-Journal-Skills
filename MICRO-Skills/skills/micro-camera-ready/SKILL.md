---
name: micro-camera-ready
description: Use when a MICRO paper is accepted and the camera-ready is due — the nine-week July-to-September window in the 2026 cycle, de-anonymization and acknowledgments restoration, keeping the all-author reference rule, integrating rebuttal promises, the optional post-AE artifact appendix, and IEEE/ACM publication logistics.
---

# MICRO Camera-Ready

For the 2026 cycle: notification July 7, camera-ready **September 11, 2026** — nine
weeks, with artifact evaluation (see `micro-artifact-evaluation`) running inside
the same span and the symposium following in Athens, Oct 31 – Nov 4. This skill
turns the acceptance email into a correct published record.

## The nine-week plan

| Weeks | Work |
|---|---|
| 1 | Re-read reviews cold; extract every fix promised in the rebuttal into a tracked worklist |
| 2–4 | Execute the worklist: new runs promised, clarified methodology text, corrected figures |
| 3–6 | Artifact evaluation submission and evaluator support (parallel track) |
| 7 | De-anonymization pass + acknowledgments + final reference audit |
| 8 | Publisher formatting, copyright/rights forms, metadata |
| 9 | Buffer; upload early — September 11 is also the AE endgame in recent cycles |

## De-anonymization is an additive diff, not a rewrite

Produce the camera-ready as a reviewed diff against the accepted PDF:

- Author block, affiliations, ORCIDs in.
- **Acknowledgments restored** — people, funding agencies, grant numbers were
  *required to be absent* at submission (2026 guidelines), so they are easy to
  forget permanently. Check the grant-numbers list with every PI.
- Self-citations rewritten from third person where it now reads awkwardly.
- Artifact links swapped from anonymized mirrors to the permanent public home —
  coordinated with AE badge requirements (archival repository for the Available
  badge; a GitHub URL alone does not qualify).
- Nothing else moves without a reason traceable to a review or the rebuttal log.
  Silent post-acceptance content changes are how camera-readies grow claims the PC
  never reviewed.

```bash
# guardrails on the final build
latexdiff accepted.tex camera.tex > diff.tex && pdflatex diff.tex   # human-review the delta
grep -n "et al" references.bib && echo "STILL banned at camera-ready: expand authors"
grep -inE "anonym|under review|blind" camera.tex                    # stale scaffolding
pdftotext camera.pdf - | grep -iE "acknowledg" || echo "MISSING acknowledgments?"
```

Note the second line: MICRO's all-authors-no-"et al." reference rule is a
formatting requirement of the venue, not an anonymity artifact — it survives into
the final version. New references added at camera-ready must follow it too.

## Page arithmetic changes

Camera-ready page allowances (and whether the artifact appendix rides free) are set
by the publisher instructions that arrive with acceptance — the 2025 cycle granted
a **two-page artifact appendix at no charge** for papers passing AE; assume the
same shape for 2026 but treat exact numbers as 待核实 until the author kit lands.
Budget the appendix content early from the AE package README rather than writing
it fresh in week 8.

## Publication and indexing facts worth knowing

- MICRO proceedings appear in **both** the ACM Digital Library and IEEE Xplore
  (the symposium is IEEE/ACM; e.g., the 58th's proceedings are in the ACM DL, the
  40th's in Xplore). Your DOI will be the citable anchor — put it in the artifact
  README when the publisher assigns it.
- AE badges (Available / Functional / Reproducible, per the 2025 AE pages) are
  printed on the paper and attached as ACM DL metadata — the camera-ready and the
  AE outcome must land together.
- Attendance/registration obligations for publication (who must register, whether
  presentation is in-person-only for Athens): 待核实 on `micro59/attend/` — verify
  before booking nothing or everything.

## Presentation pipeline (the deadline after the deadline)

Athens follows seven weeks after camera-ready. Start the talk while the paper is
still warm:

- **The talk is the four-beat argument at 4x compression** (see
  `micro-writing-style`): one characterization slide, one insight slide, the
  block diagram, the headline bar chart with the cost line on the same slide.
  Everything else is backup slides for Q&A.
- **Q&A at MICRO is methodology Q&A.** Prepare backup slides for: baseline
  config table, sensitivity sweep edges, the worst-regressing workload, and the
  iso-storage comparison. These four cover most questions actually asked.
- Whether lightning sessions, poster obligations, or speaker-registration
  deadlines apply for the 2026 program: 待核实 on the program pages when they
  post — assign an owner to watch for them.

## Post-camera-ready checklist

- [ ] arXiv posting updated to the final text (respecting the publisher's policy).
- [ ] Artifact repository tagged `micro26-camera-ready`, badge requirements met.
- [ ] Talk and poster pipeline started — the Athens slot arrives fast after the
      September deadline.
- [ ] Consider IEEE Micro **Top Picks** submission when the call opens: it selects
      from the year's architecture conference papers, and MICRO papers are core
      candidates.

## Metadata that outlives the conference

The camera-ready fixes the paper's permanent search surface — worth ten deliberate
minutes:

- Title and abstract as submitted to the publisher become the ACM DL / IEEE
  Xplore record; typos here are forever.
- Author name forms and ORCIDs consistent with each author's prior record, or
  the bibliometric graph splits.
- Index terms/keywords chosen for the mechanism community's search habits
  (structure names, not application buzzwords).
- The artifact DOI and the paper DOI should cross-reference: paper's artifact
  statement cites the Zenodo DOI; the Zenodo record cites the paper DOI once
  assigned.

## Output format

```text
[Worklist] rebuttal promises: N total, N done, N dropped-with-reason
[Diff audit] camera vs accepted: additive-only confirmed / flagged changes listed
[Restored] authors / acks+grants / self-citations / permanent links: done each
[References] et-al scan clean incl. new entries: yes / no
[AE coupling] badge target · archival deposit done · appendix drafted: status
[Publisher] rights form / metadata / page allowance: done each (待核实 items named)
[Logistics] registration & presentation rules verified on live page: yes / pending
```
