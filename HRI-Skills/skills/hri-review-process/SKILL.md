---
name: hri-review-process
description: Use to understand and navigate the ACM/IEEE HRI full-paper review pipeline — the initial desk check and track assignment, the 1AC/2AC plus three external reviewers, the double-blind two-phase model, the author rebuttal, the online reviewer discussion, the program-committee meeting, and the per-track subcommittees — and to see where author leverage exists.
---

# HRI Review Process

Understanding HRI's pipeline tells you where your effort actually moves the outcome. HRI runs a
**double-blind, two-phase** review with a real **rebuttal** and a **program-committee meeting** —
closer to a rigorous conference model than to a journal R&R, but with a discussion culture that
gives the rebuttal genuine weight. Contribution-typed **subcommittees** mean your paper is judged by
reviewers matched to its track. This skill models the pipeline; `hri-author-response` covers writing
the rebuttal. Mechanics below are the HRI 2026 cycle (see `resources/official-source-map.md`).

## The pipeline, stage by stage

1. **Initial check (desk stage).** Program-Committee Chairs, Track Chairs, and Area Chairs screen
   submissions for **desk rejections** (over length, anonymity violations, out of scope) and
   **track changes** (moving a paper to a better-fitting subcommittee). Clearing this stage is
   entirely in your control — see `hri-submission`.
2. **Assignment.** Each paper is assigned within its **track/subcommittee** to a **1AC (primary area
   chair)** and a **2AC (secondary)**. The 1AC recruits **three external reviewers** — experts in the
   topic who are not on the program committee.
3. **Reviewing.** The three externals write reviews; the ACs read the paper and the reviews. So a
   typical paper has **three external reviews plus two AC perspectives**.
4. **Rebuttal (phase two for authors).** Authors receive the reviews and submit **one rebuttal**
   (HRI 2026: due ~12 Nov 2025), addressing misunderstandings, factual errors, and specific concerns.
5. **Discussion.** After the rebuttal, the 1AC leads an **online discussion** among the reviewers,
   who may revise scores in light of the rebuttal and each other's points.
6. **Program-committee meeting.** The PC meets to make final decisions, with the ACs championing or
   critiquing papers based on reviews, rebuttal, and discussion.
7. **Decision** (HRI 2026: December). Some editions may use light shepherding/conditional acceptance
   (**待核实** per cycle). There is **no in-cycle major-revision round** — a reject is a reject for
   that edition.

## What reviewers are told to value

HRI reviewer guidance steers toward **impact over polish**: reviewers are asked to favor
**slightly flawed but impactful** work over **perfectly executed but low-impact** work, and to judge
the paper **as the contribution type of its track** (a Design paper by design criteria, a User
Studies paper by study rigor, and so on). The reviewer form asks reviewers to identify the paper's
**key findings** and **claimed contribution** and to assess how well the evidence supports them.
Write so those are effortless to state — an ambiguous contribution is a reviewing risk.

## Where author leverage actually is

- **Before submission (highest leverage):** clear the desk check, pick the right **track**, make the
  contribution and its evidence unmistakable, and include an anonymized **video**. Most outcomes are
  set here.
- **The rebuttal (real, bounded leverage):** because reviewers discuss and can move scores *after*
  the rebuttal, a focused rebuttal that corrects a genuine misreading or a factual error routinely
  changes decisions. It is not a formality. See `hri-author-response`.
- **You cannot influence:** AC/reviewer assignment, the discussion you do not see, or the PC-meeting
  debate. Do not waste the rebuttal arguing with tone; fix what a reviewer can act on.

## Calibrating your expectations

- HRI is **highly selective** — recent editions accepted roughly a quarter of full-paper submissions
  (HRI 2025 reported ~100/400 ≈ 25%; HRI 2024 ~24.7%; treat exact figures as reported, **待核实** to
  the official program). A strong paper still faces a hard bar.
- **Three externals + two ACs** means disagreement is normal; a split (e.g., two positive, one
  negative) is common and is exactly where the rebuttal and discussion decide the paper.
- **Best-paper awards are given per track**, so excellence is judged within your contribution type,
  not across the whole conference.

## Reading your reviews

- Separate **fatal** concerns (a design confound, an unsupported central claim, an ethics gap) from
  **fixable** ones (a missing citation, a clarification, an added analysis you can describe).
- Identify each reviewer's **decisive objection** — the one thing that, if resolved, flips them — and
  aim the rebuttal there.
- Note where reviewers **disagree**; the rebuttal can help the discussion resolve the split in your
  favor by giving the sympathetic reviewer ammunition.

## Reverify each cycle

- Reviewer/AC counts (3 externals + 1AC/2AC is the recent norm) and the desk-check ownership.
- Whether the edition uses shepherding/conditional acceptance.
- Rebuttal timing, length, and whether referencing new results is allowed (**待核实**).

## Output format

```text
[Stage] where the paper is: desk-check / reviewing / rebuttal / discussion / PC-meeting / decided
[Reviewer picture] 3 externals + 1AC/2AC · scores/split summarized
[Decisive objections] per reviewer, the one thing that flips them
[Leverage] what the rebuttal can realistically move here
[Track] judged as which contribution type · award eligibility per track
[Next action] <ordered>
```
