---
name: jape-submission
description: Use when running the final pre-submission preflight for the Journal of Applied Econometrics (JAE) via Editorial Express — Free Format PDF submission, the 100-word citation-free summary, the 35-page limit, any-consistent-style references, the no-submission-fee policy, the optional open-access charge, and the three-papers-under-review cap. Final checks; it does not draft content.
---

# Submission Preflight for JAE (jape-submission)

## When to trigger

- About to press submit on Editorial Express for a JAE paper
- Confirming which files and limits JAE expects at first submission
- Checking the fee/open-access situation and the per-author cap

## Process facts (re-confirm volatile items on the official page)

- Published by **John Wiley & Sons**; submitted via **Editorial Express** at `editorialexpress.com/jae`; manuscripts handled in **PDF**.
- **Free Format** first submission: strict formatting is **not** required initially, and references may be in **any consistent style**.
- **No submission fee.** Hybrid open access is **optional** and triggers an Article Publication Charge **only if you choose OA on acceptance** (a Wiley APC; the exact ~USD 4,230 / GBP 2,800 / EUR 3,570 figure is **待核实** — the live funded-access page was bot-blocked). Non-OA publication is free.
- **Cover letter optional.** Categories: Research Articles and the dedicated **Replication Articles** track.
- **Cap:** no more than **three papers** from the same author under review at once.

## Preflight checklist

- [ ] Single **PDF** uploaded to Editorial Express
- [ ] Main article within **35 pages**; extended material in the **online appendix** (no cap)
- [ ] **Summary ≤ 100 words**, self-contained, **no citations**; **≤ six keywords**; title without abbreviations
- [ ] References in **one consistent style** (Free Format)
- [ ] **Conflict-of-interest statement** present; acknowledgments do **not** thank reviewers
- [ ] No more than **three** of your papers under review at once
- [ ] Data exportable to plain **ASCII/CSV** + readme; programs staged for the **JAE Data Archive**

## Editorial Express upload sequence

Stage the materials in the order the form consumes them, so nothing is improvised at the screen (exact fields may evolve — confirm on the live form):

1. **Manuscript PDF** — one file, fonts embedded, line/page numbers helpful for single-blind review (no anonymization needed; authors are known).
2. **Track choice** — Research Article vs. Replication Article; pick deliberately, the framing promises differ.
3. **Summary + keywords** — paste-ready: ≤100 words, citation-free, ≤6 keywords, title without abbreviations.
4. **Online appendix** — separate file(s), clearly labeled; this is where the unlimited robustness material lives.
5. **Declarations** — conflict-of-interest statement; note confidential/proprietary data here and in the paper.
6. **Cover letter (optional)** — only worth writing if it says something the PDF cannot (see skeleton below).

## Last-mile desk-reject sweep

Five minutes before upload, check the failure modes specific to this venue: a summary that quietly cites a paper; a 38-page main text whose author assumed "about 35" was fine; a keywords list of nine; an acknowledgments section thanking anonymous referees from a prior round; data the paper admits can never be deposited *or* described for access; and a fourth paper still under review at JAE from the same author. Each is cheap to fix now and expensive after the editorial office notices.

## Optional cover letter skeleton

```text
Dear Editor,

We submit "[Title]" as a [Research Article / Replication Article].
Using [data: source, span, N], we [one-sentence finding with the
headline estimate]. The econometric lesson is [one sentence].
All data and programs are staged for the JAE Data Archive in
plain-text format; [none are / the following are] confidential,
with access documented in the readme.
This manuscript is not under review elsewhere; [k] ≤ 3 of our
papers are currently under review at JAE.

[Authors]
```

Keep it under a page; at this venue the letter's only real job is fit, track, and the replication commitment.

## Worked preflight (illustrative)

A 41-page draft with 11 main-text exhibits: move three robustness tables and two figures to the appendix (now 34 pp, 6 exhibits), compress a 132-word abstract to 97 words by cutting two citation clauses and one methods sentence, export the final `.dta` files to CSV with a readme stub, and confirm only two other papers are under JAE review. Total cost: an afternoon. Skipping it risks an administrative bounce before any referee reads page one.

## Output format

```
【PDF】single PDF via Editorial Express? [Y/N]
【Track】Research / Replication Article chosen deliberately? [Y/N]
【Limits】≤35pp; summary ≤100w no-cites; ≤6 keywords? [Y/N]
【Refs】one consistent style (Free Format)? [Y/N]
【Fee】no fee; OA optional (APC 待核实)? [Y/N]
【Pipeline】≤3 papers under review? [Y/N]
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — Editorial Express, Free Format, limits, fee/OA sources
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — staging the replication package
