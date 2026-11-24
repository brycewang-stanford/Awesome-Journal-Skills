---
name: nsdi-submission
description: Use when running the final pre-upload audit of an NSDI submission — the abstract-then-paper week on the per-deadline HotCRP site, 11:59 pm US Eastern cutoffs, the 12-page cap with references and appendices outside it, track-dependent anonymization, the eight-paper author cap, and the resubmission-ban check.
---

# NSDI Submission

The audit below is ordered by irreversibility: calendar errors first, then format,
then blindness, then policy. Numbers are the NSDI '27 cycle as re-verified on
2026-11-24. Both '27 gates are now closed and the NSDI '28 CFP was not yet published on
that date, so for the next gate the new CFP and its HotCRP `/deadlines` page outrank
everything here.

## Gate 0: the right site, the right clock

NSDI runs a **separate HotCRP instance per deadline**
(`nsdi27spring.usenix.hotcrp.com`, `nsdi27fall...`). Uploading to a stale spring site
bookmarked in March is a real failure mode. The '27 fall gate (now closed) ran:

- Abstracts (title, author list, track, conflicts): **September 10, 2026**.
- Full papers: **September 17, 2026**.
- Both **11:59 pm US EDT** — an Eastern-US midnight (HotCRP showed 8:59 PM PDT), not
  AoE and not the Pacific cutoff NSDI '26 used. Same-named deadlines moved time zones
  between editions; compute each coauthor's local equivalent from the HotCRP page, not
  from memory.

The abstract gate is a prerequisite: no registered abstract, no paper upload a week
later. Register even if 60% sure — withdrawing is free, materializing an unregistered
paper is impossible.

## Gate 1: format

| Item | '27 rule | Audit action |
|---|---|---|
| Body | ≤ 12 pages incl. footnotes, figures, tables | Count on the compiled PDF |
| References | extra pages allowed | Nothing else hiding among them |
| Appendices | extra pages allowed after references | Nothing load-bearing inside (`nsdi-supplementary`) |
| Template/fonts | two-column, 10-pt Times-Roman on 12-pt leading, 7" x 9" text block, 8.5" x 11" paper, numbered pages | Non-conforming papers are rejected without review — diff against the USENIX template |
| Track | research / operational / frontiers, stated on the title page and the form | Matches the evidence actually in the paper; no track changes after submission |
| Introduction | no more than 3 pages (the prescreen reads only this) | Scope, generalist readability, and track-conforming claims all visible here |

The '27 **prescreen** reads the Introduction alone and checks (a) scope against the
topic list, (b) that an NSDI PC member outside your subfield can follow it, and (c) that
it states the contribution the track expects — a novel idea plus some evaluation evidence
(research), a novel idea a PhD student could not fully evaluate (frontiers), or the
deployment setting, scale and lessons (operational).

Page-cap pressure at NSDI is figure pressure — figures count. The fix is content
triage, never `\vspace` surgery or font tricks; production chairs and reviewers both
notice geometry games.

## Gate 2: blindness, per track

Baseline sweep for all tracks — no author names, affiliations, acknowledgments, or
funding numbers; self-citations in third person; references never omitted for
anonymity; concurrent NSDI submissions cited with the CFP's fixed sentence ("Under
submission. Details omitted for double-blind reviewing.").

Then the fork:

- **Research/frontiers:** omit links to your own online content (use the form's
  auxiliary material instead); deployment context must not identify the institution by
  implication. A trace "from our global CDN" plus a author-count and a topology
  detail can triangulate to one company; neutralize to scale-descriptive terms.
- **Operational systems:** the CFP *relaxes* object anonymity — real system names,
  company names, and links may stay because judging real-world use requires them —
  while author names stay hidden. Do not import this exception into a research-track
  paper.

```bash
# Mechanical pass on the exact upload candidate
pdftotext final.pdf - | grep -nEi '(acknowledg|funded by|grant|@[a-z]+\.(com|edu))' | head
pdfinfo final.pdf | grep -Ei 'author|creator'          # PDF metadata identity
grep -rnEi '(github\.com/[a-z0-9-]+|/home/|/Users/)' *.tex figures/ | head
# research track only: search for your institution's giveaway nouns
pdftotext final.pdf - | grep -niE 'ourcorp|internal-codename' | head
```

Mechanical passes catch strings; only a human pass catches implication. Have a
non-author read the PDF asking one question: *who wrote this?*

## Gate 3: policy

- **Dual submission / prior publication / plagiarism:** prohibited by USENIX;
  concurrent review anywhere else is disqualifying, and the ban survives
  notification-date arithmetic ("they'd decide before NSDI" does not help).
- **Resubmission ban:** if this work was rejected (without a revision option) from
  the immediately preceding NSDI deadline, it cannot enter this one. Check the
  paper's own decision history — spring '27 reject means no fall '27 entry
  (`nsdi-review-process`).
- **One-shot revisions** enter with their auxiliary packet complete
  (`nsdi-author-response`); an ordinary-looking resubmission that ignores its issue
  list is terminally rejected.
- **Author cap:** at most **eight submissions per author across all '27 deadlines**
  — reconcile the group's ledger, counting spring entries.
- **AI use:** papers produced entirely or substantively by generative AI are barred —
  an AI-written section (related work and conclusion included) is a violation — and the
  HotCRP form requires an **attestation that all text is primarily human written**;
  grammar-and-clarity assistance on human-written text is encouraged.
- **Preprints:** a concurrent arXiv/technical report is allowed only if the submission
  uses a **different title and system name**.
- **Authorship:** from the '27 fall gate the USENIX Authorship Policy applies.
- **Ethics:** authors **attest at submission** that the work complies with their
  institutions' ethical standards; papers with user data (traffic, passwords, social
  data) should include a subsection on the ethical issues, and the PC may examine
  ethics as it examines technical soundness.

## HotCRP form fields deserve the same audit as the PDF

Reviewers meet the form before the paper: title and abstract must match the PDF
verbatim (drift reads as sloppiness and can confuse bidding); topic selections route
the paper toward the sub-community you want reviewing it — choose for the reviewer
profile, not maximal coverage; the full author list is entered at abstract time for
conflict computation even though the PDF hides it, and late author additions after
review assignment are a co-chairs-level incident. Declare conflicts by the site's
definitions, completely and no wider.

## Final sequence

1. T-8 days: fall HotCRP account, abstract fields drafted, conflicts entered.
2. T-7 (Sept 10): abstract registered; track locked deliberately.
3. T-2: content freeze; Gates 1-2 executed on the near-final PDF.
4. T-1: coauthor sign-off; HotCRP title/abstract verbatim-match the PDF.
5. T-0 (Sept 17): upload, status **complete**, then download the receipt copy and
   read it — the uploaded bytes, not the local file, are the submission.

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue nsdi-skills   # from a clone of the AJS repository
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
[Clock] site URL + local-time cutoffs confirmed from /deadlines
[Gate 1] pages / template / track — pass or blocker
[Gate 2] mechanical findings + human-pass verdict (track-appropriate)
[Gate 3] dual-sub / ban / cap / AI / ethics — each cleared or flagged
[Receipt] uploaded PDF re-read? fields match?
[Blockers] ordered, with owner and time cost
```
