---
name: wacv-writing-style
description: Use when revising a WACV paper's prose and first page, covering how to write for the chosen Applications or Algorithms track, leading with the real-world constraint or the method, self-contained figure captions inside the 8-page-including-figures budget, scoped claims, and a first page that pre-empts the Revise-and-Resubmit question.
---

# WACV Writing Style

Use this to make a WACV paper read the way its reviewers judge it. The governing fact is
the two-round model: a first page that answers the reviewer's obvious question earns
*Accept*; one that leaves it open earns *Revise and Resubmit*. Facts are the WACV 2026/2027
cycles as read on 2026-07-09.

## Write for your track

The two tracks reward different first pages, and writing to the wrong one draws the wrong
review:

| If your track is… | Lead the first page with… | The reviewer is asking… |
|---|---|---|
| **Applications** | The real-world constraint and why existing methods break under it | Does this system actually work under the deployment constraint you name? |
| **Algorithms** | The method/mechanism and the matched-baseline comparison | Is the algorithmic idea new, and does the gain survive fair comparison? |

An Applications paper that opens with "a novel attention module" and an Algorithms paper
that opens with "an important real-world problem" have each buried their contribution under
the other track's framing.

## The first-page arc

Put the contribution in the first page: **problem/constraint → why prior methods are
insufficient (each named) → method or system → evidence → why it fits the track**. Every
major claim on that page should point to a figure, a table, or a section — not to a promise.
Because WACV reviewers see three reviews reconciled by an AC, a page that a busy reader can
summarize in two sentences travels further than a dense one.

## Figures are page budget

The cap is **8 pages including figures and tables**. A teaser, two qualitative grids, and
three result tables can eat half the paper, so design figures as line items:

- One teaser that states the contribution visually, with a **self-contained caption** a
  reviewer can read without the body.
- Qualitative results that a reviewer will judge by eye — check they render at print zoom.
- Tables that report the comparison *under the stated condition*, with uncertainty.

```text
Caption test (apply to every figure):
  Can a reviewer who reads ONLY this caption state (a) what is shown and
  (b) what it demonstrates about the claim? If not, rewrite the caption, not the body.
```

## Scope every claim

WACV's applications framing punishes overclaiming quickly, because a reviewer can often
name the deployment case you did not test. Scope claims to the domain, constraint, and
hardware you actually demonstrated ("row-crop segmentation at 2 W in sub-10-lux light"), and
disclaim what you did not show. A scoped claim that holds beats a broad claim a reviewer can
break in one sentence — and broken claims are what turn into revision requests.

## Compress for eight pages

- Move protocol detail, extra qualitative results, and derivations to the anonymized
  supplement (see `wacv-supplementary`), keeping the body's argument intact.
- Cut roadmap sentences that restate the table of contents; spend the space on the gap
  paragraph, where reviewers form their opinion.
- Keep notation and baselines consistent between body and supplement so a Round 2 reviewer
  re-reading a revised paper is never confused by a moved number.

## Reverify each cycle

- The 8-page-including-figures rule and the references-only overflow.
- The two-track review criteria and any track-specific formatting.
- The author-kit style version.

## Output format

```text
[Track fit] first page leads with the right thing for <Applications|Algorithms>: yes/no
[First-page arc] constraint/method → gap → evidence present: yes/no
[Figure budget] pages spent on figures/tables: <n of 8> · captions self-contained: yes/no
[Overclaim risk] <claim a reviewer could break> → scoped: yes/no
[Compression] what moves to supplement: <list>
```
