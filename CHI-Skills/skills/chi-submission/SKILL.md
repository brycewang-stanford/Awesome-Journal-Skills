---
name: chi-submission
description: Use when auditing an ACM CHI Papers submission for PCS readiness, covering the September full-paper deadline, the anonymized single-column template, word-count norms instead of page limits, subcommittee designation, supplementary and video upload, anonymization of external links, and CHI's desk-reject triage before upload.
---

# CHI Submission

Run this audit before uploading to PCS (Precision Conference Solutions) — CHI does not
use OpenReview or CMT. Every date and cap below was read from the CHI 2027 Papers pages
on 2026-07-08 through search-engine renderings (direct fetches of `chi2027.acm.org`
were blocked in the verification environment); reopen the live pages before acting on
any number.

## What the CHI 2027 cycle posted

- Full Papers deadline: **Thursday, September 10, 2026**, on PCS, *including videos and
  supplementary materials* — CHI collects everything on one date, unlike venues with a
  later supplement window. No separate abstract-registration deadline was found for
  2027; confirm on the live page rather than assuming (待核实).
- Review format: the **single-column** ACM submission template (CHI has used
  single-column reviewing since 2021). The two-column look happens later, in TAPS.
- Length is governed by words, not pages. The posted norm: roughly **5,000–8,000 words**
  for a typical paper (excluding references), submissions at or above **12,000 words**
  face extra scrutiny and desk rejection when the length is not justified, and papers of
  about 5,000 words or fewer are welcomed as short papers reviewed with expectations
  commensurate with their size. CHI's standing phrase is that a paper should be the
  length appropriate to its contribution.
- The submission form requires you to designate a reviewing **subcommittee** (up to two
  choices) — a strategic decision, not paperwork; see `chi-topic-selection`.
- Anonymization is mandatory and extends beyond the PDF: supplemental materials and
  **external links to datasets or code repositories** that reveal identity are posted
  desk-reject grounds.

## The anonymization trap specific to CHI

CHI's policy is anonymized review of an HCI paper, which creates leak channels that ML
venues rarely have: consent-form headers naming the lab, screenshots of a deployed
system showing a university logo, video figures with a narrator saying "at our
institution," OSF or GitHub links registered to a named account, and app-store pages
for the studied prototype. Cite your own prior studies in the third person and keep
the citation; scrub everything else.

```bash
# Mechanical pre-upload sweep on the PCS package
pdfinfo paper.pdf | grep -Ei 'author|creator|producer'      # PDF metadata identity
pdftotext paper.pdf - | grep -nEi 'github|osf\.io|our (lab|university|institution)' | head
texcount -inc -sum main.tex | tail -3                        # word count vs the norms
ffprobe -v error -show_entries format=duration,size video-figure.mp4   # video sanity
unzip -l supplement.zip | grep -Ei 'consent|irb|ethics|\.git/' | head  # named forms
```

Treat consent forms and ethics-approval letters as the highest-risk files: they carry
institution names by design, so upload templated, de-identified versions.

## Desk-reject triage, CHI edition

CHI 2026 formalized an *assisted desk reject* step run jointly by subcommittee chairs
and ACs, with expanded criteria — desk screening is now a real stage, not a formality.

| Finding at audit time | CHI severity | Realistic fix |
|---|---|---|
| Wrong template or altered format | Desk reject | Recompile on the current ACM single-column class |
| Identity leak in PDF, supplement, or link | Desk reject | De-identify; replace links with anonymized archives |
| ~12,000+ words without justification | Desk reject risk | Cut or explicitly justify length in the submission |
| No plausible HCI contribution for any subcommittee | Desk reject at SC/PC screening | Re-frame or re-route before the deadline |
| Video figure missing captions | Review-stage damage | Add a .srt/.sbv file (see `chi-supplementary`) |
| Weak subcommittee match | Quiet mis-review | Change the designation, not the paper, if the work is sound |

## Deadline-week order of operations

1. Lock the subcommittee pair first; it determines who reads everything else.
2. Freeze the manuscript at a defensible word count and record the `texcount` output.
3. Render and caption the video figure early — encoding and captioning always take
   longer than the writing team budgets.
4. Assemble supplements from a clean export, then run the mechanical sweep above on the
   exact files going into PCS.
5. Fill every PCS field (title, abstract, authors, subcommittees, contribution
   statement fields if asked) a day before; PCS has no post-deadline mercy.
6. Re-download the submitted package and open it cold, the way a 1AC will.

## Length is an argument, not a quota

Because CHI reviews words against contribution, padding is a visible defect: a 9,500
word paper whose study supports 7,000 words of claims reads as inflated, and reviewers
say so. Cut the third restatement of the findings, move instrument details to the
supplement, and keep the method section exactly as long as replication requires — no
longer.

## Cycle-volatile items — reverify every year

- The September date, the no-abstract-deadline reading, and all word-count wording.
- Subcommittee list and count for the live cycle (the 2026 list is posted on
  chi2026.acm.org; the 2027 list was not yet published at check time — 待核实).
- Desk-reject criteria wording, which changed as recently as August 2025.
- Whether PCS asks new form questions (AI-use disclosure, data-availability fields).

## Output format

```text
[CHI submission status] ready / blocked / needs work
[Word count] <n> words vs posted norms; justification needed? yes/no
[Subcommittees] first: <name> / second: <name or none>
[Anonymity sweep] clean / leaks: <pdf | supplement | links | video | forms>
[Desk-reject exposure] <highest-risk item>
[Fix queue] <ordered actions before September upload>
```
