---
name: chi-submission
description: Use when auditing an ACM CHI Papers submission for PCS readiness, covering the September full-paper deadline, the anonymized single-column template, word-count norms instead of page limits, the 150-word abstract cap, reviewer-matching descriptors and Review Responsibility slots, supplementary and video upload, anonymization of external links, and CHI's desk-reject triage before upload.
---

# CHI Submission

Run this audit before uploading to PCS (Precision Conference Solutions) — CHI does not
use OpenReview or CMT. Every date and cap below was re-read directly from the CHI 2027
Papers pages on 2026-11-24; reopen the live pages before acting on any number.

## What the CHI 2027 cycle posted

- Full Papers deadline: **Thursday, September 10, 2026**, on PCS, *including videos and
  supplementary materials* — CHI collects everything on one date, unlike venues with a
  later supplement window. The submission site opened **August 13, 2026**, and the
  call states there is **no abstract deadline**. All deadlines are AoE and carry a
  24-hour grace period that is contingency only, not an extension.
- Review format: the **single-column** ACM submission template (CHI has used
  single-column reviewing since 2021). The two-column look happens later, in TAPS.
- Length is governed by words, not pages. The posted norm: **5,000–8,000 words**
  encouraged (the average CHI paper is about 7,000–8,000 words excluding references,
  captions and appendices), submissions above **12,000 words** are desk-rejected unless
  strongly justified, and papers under 5,000 words are short papers reviewed with
  expectations commensurate with their size. CHI's standing phrase is that a paper
  should be the length appropriate to its contribution.
- **Abstract: 150 words or fewer** on every submission.
- **No more subcommittees.** For CHI 2027 authors no longer submit to a topical
  subcommittee; the form instead asks for **descriptors** of the expertise needed to
  review the paper (domain, method or approach, users/participants/communities,
  primary contribution), which drive reviewer matching — a strategic decision, not
  paperwork; see `chi-topic-selection`.
- **Review Responsibility Policy:** by submitting, all authors agree to the RRP; each
  submission must name authors in review-responsibility slots covering **four**
  completed reviews, and a declared reviewer who fails to deliver gets their
  submissions desk-rejected. Every author needs an **ORCID**, and the DBLP field in
  PCS must hold a profile URL or "n/a".
- The author list is frozen at the paper deadline (no additions during R&R or at
  publication-ready); PCS affiliations are final.
- Closely related concurrent submissions (same study, artifact or dataset) must be
  uploaded, anonymized, in the concurrent-submissions field, or the paper is
  desk-rejected.
- Human-subjects research: include a short note to reviewers giving the ethics-review
  context of your research environment.
- Generative AI: the call defers to the ACM Policy on Authorship, and papers violating
  that policy are listed desk-reject examples. The policy (updated May 14, 2026; read
  via the Internet Archive because acm.org refuses automated fetches) requires AI use
  *in the conduct of the research* — study design, data generation or collection,
  coding, analysis, AI-built artifacts relied on for conclusions — to be described in
  detail in the methods section, and no longer requires disclosure of AI used only to
  assist with writing. CHI 2027 posts no separate AI-disclosure form.
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

CHI 2026 formalized an *assisted desk reject* step; CHI 2027 keeps it, now seeded by an
automated rubric report that the AC reads and an SC and Papers Chair confirm — desk
screening is a real stage, not a formality (`chi-review-process`).

| Finding at audit time | CHI severity | Realistic fix |
|---|---|---|
| Wrong template or altered format | Desk reject | Recompile on the current ACM single-column class |
| Identity leak in PDF, supplement, or link | Desk reject | De-identify; replace links with anonymized archives |
| ~12,000+ words without justification | Desk reject risk | Cut or explicitly justify length in the submission |
| No plausible HCI contribution / no HCI literature context | Desk reject or ADR | Re-frame or re-route before the deadline |
| Abstract over 150 words | Compliance failure | Cut before upload |
| RRP slots missing, invalid ORCID, thin descriptors | Flagged in completeness report | Fix in the post-deadline window, better before |
| Video figure missing captions | Review-stage damage | Add a .srt/.sbv file (see `chi-supplementary`) |
| Vague or scattershot descriptors | Quiet mis-review | Choose fewer, more specific descriptors, not the paper |

## Deadline-week order of operations

1. Lock the descriptors and RRP reviewer slots first; they determine who reads
   everything else.
2. Freeze the manuscript at a defensible word count and record the `texcount` output.
3. Render and caption the video figure early — encoding and captioning always take
   longer than the writing team budgets.
4. Assemble supplements from a clean export, then run the mechanical sweep above on the
   exact files going into PCS.
5. Fill every PCS field (title, abstract, authors with ORCID/DBLP, descriptors, RRP
   slots, concurrent submissions) a day before; PCS has no post-deadline mercy.
6. Re-download the submitted package and open it cold, the way the AC will.

## Length is an argument, not a quota

Because CHI reviews words against contribution, padding is a visible defect: a 9,500
word paper whose study supports 7,000 words of claims reads as inflated, and reviewers
say so. Cut the third restatement of the findings, move instrument details to the
supplement, and keep the method section exactly as long as replication requires — no
longer.

## Cycle-volatile items — reverify every year

- The September date, the no-abstract-deadline reading, and all word-count wording.
- The reviewer-matching descriptor vocabulary (new for CHI 2027, replacing the
  subcommittee list) and the Subcommunity Chair roster on the Program Committee page.
- Desk-reject criteria wording, which changed for CHI 2026 and again for CHI 2027.
- Whether PCS asks new form questions (AI-use disclosure, data-availability fields).

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue chi-skills   # from a clone of the AJS repository
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
[CHI submission status] ready / blocked / needs work
[Word count] <n> words vs posted norms; justification needed? yes/no
[Abstract] <n> words vs 150 cap
[Descriptors] domain: <..> · method: <..> · participants: <..> · contribution: <..>
[RRP] <names in four review slots; ORCID + DBLP present? yes/no>
[Anonymity sweep] clean / leaks: <pdf | supplement | links | video | forms>
[Desk-reject exposure] <highest-risk item>
[Fix queue] <ordered actions before September upload>
```
