---
name: stoc-submission
description: Use when auditing a STOC (ACM Symposium on Theory of Computing) submission for HotCRP readiness — the abstract + table-of-contents + first-12-pages reading rule, single-column 11-point format, double-blind hygiene, the SIGACT prior/simultaneous-publication policy, and deadline-week sequencing before the November cutoff.
---

# STOC Submission

Run this audit before uploading to the STOC HotCRP site. Anchor cycle: STOC 2026
(58th ACM Symposium on Theory of Computing), whose CFP set the paper deadline at
Tuesday, November 4, 2025, 4:59pm EST, with no separate abstract-registration step
(checked 2026-07-08 at `acm-stoc.org/stoc2026/stoc2026-cfp.html`). Reopen the live
CFP for the cycle you are actually targeting before trusting any number below.

## The reading contract, not a page limit

STOC does not cap submission length. Instead, the 2026 CFP guaranteed committee
attention only to the **abstract, the table of contents, and the first twelve
pages**; everything after that is read at the committee's discretion. That is a
contract about where your persuasion must happen, and it has three consequences:

- Every theorem you want credit for must be *stated* inside the first twelve pages,
  even if its proof lives at page 40.
- The table of contents is a reviewed object. A submission without one, or with one
  that does not reveal the proof architecture, wastes a guaranteed-read surface.
- Proofs beyond page twelve are a courtesy to the diligent reviewer, not a
  substitute for a convincing overview inside the guaranteed pages.

## Format floor (2026 wording)

Typeset in 11-point or larger font, single-column, single-spaced with generous
spacing, 1-inch margins on letter-size paper. There is no mandatory class file in
the STOC submission stage — this is looser than ACM camera-ready format, and
authors coming from two-column ML venues routinely misjudge how few words twelve
single-column pages hold. A minimal compliant preamble:

```latex
\documentclass[11pt,letterpaper]{article}
\usepackage[margin=1in]{geometry}
\usepackage{amsmath,amsthm,amssymb}
\usepackage[numbers]{natbib}
% Double-blind: no \author block, no acknowledgements, no grant numbers.
\title{Your Title}
\author{}
\date{}
```

## Anonymity, new to the house tradition

STOC 2026 used **double-blind reviewing**: the submission must not reveal author
identity in any way. Because the venue only recently moved away from
non-anonymous submissions (the exact first double-blind edition: 待核实), older
lab templates and habits are the main leak source. Sweep for:

- self-citations phrased as "our earlier paper" instead of third person;
- the full version already on arXiv under your names — posting is generally
  compatible with theory double-blind norms, but confirm the current CFP's stance
  before citing your own preprint in a de-anonymizing way (待核实 per cycle);
- PDF metadata (`pdfinfo paper.pdf`), acknowledgements, and grant lines.

## SIGACT prior/simultaneous-publication policy

The 2026 CFP applied SIGACT's standing rule: work already published, or scheduled
to appear before the conference (for STOC 2026: prior to July 2026), in another
conference proceedings or a journal is ineligible, and simultaneous submission to
such venues is barred. The stated exception is publication in **Science or
Nature**. arXiv and ECCC preprints do not count as prior publication.

## Desk-risk and damage triage

| Finding at upload time | Consequence at STOC | Can it be repaired after the deadline? |
|---|---|---|
| Main theorem stated only after page 12 | Committee may never register the result | No — the guaranteed-read window is fixed |
| Author-identifying text or metadata | Violates the double-blind instruction; chair action | No |
| Simultaneous submission to SODA/FOCS/a journal | Policy violation; rejection at both ends | No |
| Missing table of contents | Loses a guaranteed-read surface; sloppy signal | No |
| Font/margin shrinking to fake density | Read as circumventing the reading contract | No |
| Overloaded notation, no overview section | Survives, but converts reviewers to skeptics | Only before the deadline |

## Deadline-week sequence

1. Freeze all theorem statements and check each appears within pages 1–12.
2. Rebuild the table of contents so section titles narrate the proof strategy.
3. Run the anonymity sweep: names, acknowledgements, self-references, metadata.
4. Verify the abstract in HotCRP matches the PDF abstract exactly.
5. If the cycle offers the opt-in automated pre-submission feedback experiment
   (STOC 2026 ran a Gemini-based rigor check, full paper due November 1, 5pm EST,
   output visible to authors only), decide deliberately — it needs the paper
   essentially done three days early.
6. Upload a day ahead; the deadline is a US-Eastern clock time, not AoE.

## What the portal itself will ask

Beyond the PDF, the HotCRP form has its own fields, and mismatches between form
and PDF are chair-visible:

- Title and abstract entered on the form must match the PDF; the form abstract
  is what PC members read while bidding, so it does the first-impression work.
- Topic selections drive assignment — choose the sub-areas whose reviewers you
  actually want, not every box that vaguely applies.
- Conflicts of interest against PC members must be complete and honest;
  under-declaring is an integrity problem, over-declaring shrinks your
  qualified-reviewer pool.
- Author list and order are entered even though reviewers cannot see them;
  fix them now, since changing authorship post-acceptance needs chair approval.

## Habits from other venues that break here

| Imported habit | Why it fails at STOC |
|---|---|
| Two-column conference template | Wrong format; the submission stage wants loose single-column 11-point |
| Deferring all proofs to a "supplementary file" | No such channel exists; one PDF carries everything |
| Waiting for the rebuttal to clarify | There is no rebuttal (`stoc-author-response`) |
| AoE mental arithmetic | The deadline is US-Eastern wall-clock time |
| "Abstract deadline first, paper later" | 2026 had a single deadline; no placeholder week |

## Output format

```text
[STOC readiness] Ready / Needs fixes / Not ready
[Guaranteed-read audit] <theorems or claims currently outside abstract/ToC/first 12 pages>
[Anonymity findings] <leaks discovered>
[Policy findings] <prior/simultaneous-publication conflicts>
[Fix order] <ordered actions before the November deadline>
```
