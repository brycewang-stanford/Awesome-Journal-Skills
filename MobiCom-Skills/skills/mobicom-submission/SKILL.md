---
name: mobicom-submission
description: Use when running the final pre-upload audit of a MobiCom submission — confirming the right per-edition HotCRP site and round, the AoE cutoff printed as an Eastern clock time, the 12-page double-column cap, the abstract-registration prerequisite, and the double-blind sweep including wireless-testbed identity leaks.
---

# MobiCom Submission

Work this list from the mistakes you cannot take back toward the ones you can: pick the
wrong round and the paper is simply gone; a format or blindness slip is recoverable only
before upload. The numbers are the MobiCom 2026 cycle as rendered on 2026-07-09; whatever
the live HotCRP `/deadlines` page says for your round wins over anything printed here.

## Step 1: right site, right round, right clock

MobiCom runs a **per-edition HotCRP site** (`mobicom<yy>.hotcrp.com`) with **two rounds a
year**, and the rounds feed different editions. Before anything, confirm three things on
the `/deadlines` page:

- **Which round** is open (winter/spring or summer/fall) and **which edition it feeds** —
  the summer round after MobiCom 2026 competes for MobiCom 2027, not the 2026 program.
- The **abstract-registration** date, which precedes the paper upload by about a week.
- The **paper** cutoff and that it is **AoE**. MobiCom's winter round printed 7:59 am EDT
  for an 11:59 pm AoE deadline — the clock on the page is not your local midnight. Compute
  each coauthor's local time from the page.

The abstract step gates the paper step: miss the earlier date and HotCRP will not let you
upload a week later. Register the abstract whenever the paper is plausible — a registered
abstract you later withdraw costs nothing, an unregistered one cannot be revived.

## Step 2: format

| Item | Rule | Audit action |
|---|---|---|
| Body | ≤ 12 single-spaced numbered pages incl. figures and tables | Count on the compiled PDF |
| Columns | double column, 9.25in x 3.33in, 0.33in gutter, ≤55 lines/col | Diff the template geometry; do not resize |
| Font | ≥ 10 pt | Check the class option, not the eyeball |
| References | outside the cap | Nothing else hiding among them |
| Appendices | after references, outside the cap | Nothing load-bearing inside (`mobicom-supplementary`) |

Page pressure at MobiCom is figure pressure — plots and system diagrams count against the
12. The fix is content triage, never `\vspace` surgery or shrinking a radio-testbed figure
below legibility; reviewers and production both notice geometry games.

## Step 3: blindness

Double-blind baseline for every submission — no author names, affiliations, funding
numbers, or acknowledgments; self-citations in the third person; references never dropped
for anonymity. Then the wireless-specific sweep that generic checks miss:

```bash
# Mechanical pass on the exact upload candidate
pdftotext final.pdf - | grep -nEi '(acknowledg|funded by|grant|@[a-z]+\.(com|edu))' | head
pdfinfo final.pdf | grep -Ei 'author|creator'                 # PDF metadata identity
grep -rnEi '(github\.com/[a-z0-9-]+|/home/|/Users/)' *.tex figures/ | head
# wireless giveaways: named testbed, building, deployment site, IRB/site IDs
pdftotext final.pdf - | grep -niE '(our (building|campus|testbed)|room [0-9]|IRB #?[0-9])' | head
```

A deployment described as "our campus mesh over N buildings" plus a photo of a recognizable
skyline can triangulate to one lab; neutralize identifying detail to scale-descriptive
terms. Mechanical passes catch strings; only a human pass catches implication. Have a
non-author read the PDF asking one question: *whose testbed is this?*

## Step 4: policy

- **Dual submission / prior publication / plagiarism:** concurrent review elsewhere is
  disqualifying; a same-title workshop or demo needs a delta the paper states.
- **Which edition:** confirm the paper is entering the round you intend and is not a
  disallowed re-entry of a paper still under decision from the prior round.
- **Ethics / measurement:** work that measures real users, spectrum, or third-party
  infrastructure must address handling in the paper; the exact 2027 wording is 待核实 — read
  that CFP section live.
- **AI-use policy:** the current cycle's wording is 待核实; do not assume last year's rule.

## HotCRP form fields deserve the same audit as the PDF

Reviewers meet the form before the paper: title and abstract must match the PDF verbatim;
topic selections route the paper toward the wireless/mobile sub-community you want bidding
on it — choose for the reviewer profile, not maximal coverage; the full author list is
entered at abstract time for conflict computation even though the PDF hides it, and late
author additions after assignment are a chairs-level incident. Declare conflicts by the
site's definitions, completely and no wider.

## Final sequence

1. T-8 days: HotCRP account on the correct round, abstract fields drafted, conflicts entered.
2. T-7 (abstract cutoff): abstract registered; topics chosen deliberately.
3. T-2: content freeze; Steps 2-3 executed on the near-final PDF.
4. T-1: coauthor sign-off; HotCRP title/abstract verbatim-match the PDF.
5. T-0 (paper cutoff, AoE): upload and drive the paper to **complete** status, then
   re-download what HotCRP stored and open it — only the bytes on the server count, and a
   silently truncated or wrong-version upload is caught only by looking.

## Output format

```text
[Round]    site URL + which edition it feeds + AoE cutoff in local time
[Format]   pages / columns / font / template — pass or blocker
[Blind]    mechanical findings + human-pass verdict (wireless giveaways)
[Policy]   dual-sub / ethics / AI-use — each cleared or flagged
[Receipt]  uploaded PDF re-read? HotCRP fields verbatim-match?
[Open]     remaining blockers, most-irreversible first, with owner + hours
```
