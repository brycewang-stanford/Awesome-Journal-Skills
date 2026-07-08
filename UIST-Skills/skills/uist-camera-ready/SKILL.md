---
name: uist-camera-ready
description: Use when converting a conditional UIST acceptance into a published paper — delivering the rebuttal-promised changes by the July deadline, working the ACM TAPS pipeline with alt text for every figure and table, de-anonymizing correctly, finalizing the video figure, and preparing the Detroit talk and demo.
---

# UIST Camera-Ready

A UIST acceptance is conditional: the June 27 notification (2026 cycle, verified
2026-07-08) accepts the paper *as amended by your rebuttal*, and the July 24
camera-ready is where those amendments come due. This phase has three workstreams —
the contractual edits, the ACM production pipeline with its accessibility
requirements, and conference logistics — and they share four weeks.

## Workstream 1: deliver the contract

Reconstruct the promise ledger from your rebuttal (see `uist-author-response`) and
the meta-review or condition list in the notification:

- Make each promised change where you said you would make it, and keep a diff-notes
  file mapping promise → location — useful if the process asks anyone to verify
  conditions, and essential when six co-authors edit in parallel.
- The growth budget is +10%: one extra page for standard papers, half a page for
  short papers (2026 numbers). Promised additions get the space first; new
  camera-ready ambitions get what remains.
- Do not silently make substantive changes nobody asked for; a camera-ready is a
  fulfillment step, not a second revision cycle.

## Workstream 2: production and accessibility

Camera-ready flows through **ACM TAPS** (source upload, not just a PDF), and the
2026 guide adds accessible-PDF tagging via APTARA. The author-side accessibility
obligations are concrete:

| Item | 2026 requirement |
|---|---|
| Alt text | Required for **every figure, subfigure, and table** |
| Tables | Real table markup, not images of tables |
| Math | Source-level math, not equation screenshots |
| Video | Final video figure with captions |
| PDF tagging | Applied in the TAPS/APTARA workflow from your source |

Writing alt text for an interface-systems paper is its own small craft: describe
the interaction state the figure evidences, not the pixels. "Annotated sequence:
a finger drags on the forearm and the cursor traces the same path on the watch,
0.3 s later" beats "screenshot of the system."

```text
Alt-text pass over the figure inventory:
  [ ] every \includegraphics has \Description{...}
  [ ] every subfigure has its own description
  [ ] tables described (what varies across rows/columns, the takeaway)
  [ ] teaser figure description states the core interaction
  [ ] no description says "image of" / "figure showing" boilerplate
```

## Workstream 3: de-anonymize and finalize assets

- Restore authors, affiliations, acknowledgements, and grant numbers; flip the
  `acmart` options from the review/anonymous configuration to the final one per the
  current guide.
- Reverse the third-person self-citation contortions where they now read oddly —
  but only where the meaning improves.
- Restore real repository and project-page URLs, and make them live before the
  proceedings do (see `uist-artifact-evaluation` for what should be at the other
  end).
- Produce the final video figure: captioned, de-anonymized, credits added; check
  the current guide for any preview-video obligation (待核实 for 2026).
- Complete ACM e-rights before TAPS will process; the open-access terms applying to
  UIST 2026 authors were not verifiable at check time (待核实) — read the e-rights
  form, not folklore.

## TAPS realities

TAPS consumes source (LaTeX or Word), not a hand-tuned PDF, which surprises teams
whose submission compiled through local hacks:

- Custom macros, non-standard packages, and manual float surgery that survived
  review can fail TAPS validation; budget one full rebuild-from-clean-template
  day.
- Figures need production-quality originals (vector where possible); the
  screenshot that looked fine at review DPI may not at publication.
- The `\Description{}` commands are part of the source, so the alt-text pass
  happens in LaTeX, not in a PDF editor afterward.
- Validate early: upload a candidate build the week the system opens rather than
  on the deadline, because TAPS error messages arrive on production timelines,
  not chat timelines.
- Keep the review PDF and the camera-ready in the same repository with a tagged
  divergence point; the "which version did we promise that in" question recurs
  for years.

## Four-week schedule (notification June 27 → deadline July 24, 2026)

| Week | Deliverable |
|---|---|
| 1 | Promise ledger reconstructed; edits assigned; e-rights initiated; registration/visa checks started |
| 2 | All contractual edits merged; +10% budget reconciled; figure originals collected |
| 3 | Alt-text pass; TAPS candidate upload; validation errors cleared |
| 4 | Final video captioned and uploaded; last TAPS build verified; buffer only |

## Conference logistics start now

- Registration and the presenting author: confirm the current in-person requirement
  wording (待核实 for 2026) as soon as notification lands — visas for a US venue
  (Detroit, November 2-5, 2026) can take longer than the camera-ready window.
- UIST talks are short and demo-culture shaped: build the talk around the live or
  recorded demonstration, not around related-work slides.
- Plan the hallway demo: papers whose systems can be demonstrated at the conference
  compound their impact; shipping hardware to a venue takes lead time (and consider
  a Demos-track submission for the same system where the rules allow).

## Output format

```text
[Contract status] promises delivered <k>/<n>; open items with owners
[Page budget] final length vs +10% allowance
[TAPS status] source uploaded / validation errors / complete
[Accessibility] alt-text pass done? tables/math as markup? video captioned?
[Logistics] e-rights · registration · visa · demo shipping — each with a date
```
