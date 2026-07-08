# External Tools - NSDI

Access date: 2026-07-08

Open these surfaces at the start of every NSDI engagement. The venue reissues its rules
per edition and runs two deadlines per edition, so a link that answered a spring
question can be superseded by the fall update of the same page.

## Live official surfaces

- NSDI '27 conference page: https://www.usenix.org/conference/nsdi27
- NSDI '27 Call for Papers: https://www.usenix.org/conference/nsdi27/call-for-papers
- NSDI '26 multiple-deadlines process (model for the revise/resubmit rules):
  https://www.usenix.org/conference/nsdi26/additional-info
- NSDI '26 Call for Artifacts (model for badge mechanics):
  https://www.usenix.org/conference/nsdi26/call-for-artifacts
- Per-deadline HotCRP sites: `https://nsdi<yy>spring.usenix.hotcrp.com/` and
  `https://nsdi<yy>fall.usenix.hotcrp.com/` — the `/deadlines` page on each is the
  authoritative clock.
- NSDI symposium index (all editions, open-access proceedings):
  https://www.usenix.org/conferences/byname/178
- USENIX Test of Time awards: https://www.usenix.org/conferences/test-of-time-awards
- dblp NSDI stream (venue verification for citations): https://dblp.org/db/conf/nsdi/

If `usenix.org` or `dblp.org` refuses direct fetches (both returned HTTP 403 during
this pack's verification), read the exact URLs through search-engine renderings and
cross-check at least two independent renderings before trusting a date.

## Author-side verification passes

Run each pass against the exact files you will upload, not the working draft.

1. **Clock pass.** Confirm the abstract and full-paper cutoffs and their time zone on
   the HotCRP `/deadlines` page — NSDI '27 listed 11:59 pm US EDT where NSDI '26 used
   PDT, so never reuse last cycle's conversion table. Write the local-time equivalent
   for every coauthor.
2. **Budget pass.** 12 pages including footnotes, figures, and tables; references and
   appendices ride beyond the cap. Verify with a page-by-page scan of the final PDF,
   and confirm nothing decision-critical sits past page 12.
3. **Blindness pass.** Mechanical sweep for names, affiliations, funding,
   acknowledgments, repository owners, and PDF metadata — then re-check the
   operational-track exception if applicable (system and company names may stay; author
   names never do).

```bash
pdftotext submission.pdf - | grep -nEi 'university|corp|inc\.|acknowledg|grant no|github\.com' | head
pdfinfo submission.pdf | grep -Ei 'author|creator|producer'
grep -rnEi '/Users/|/home/|@(gmail|edu)' figures/ *.tex | head   # paths and emails inside sources
```

4. **Status pass.** In HotCRP, "complete" is the only state that counts; abstract
   registered a week earlier, all authors and conflicts entered, track selected, and
   the eight-submissions-per-author ledger reconciled across the group.
5. **Revision pass** (one-shot resubmissions only). Auxiliary material contains the
   change-highlighted PDF and the high-level change summary, and every item on the
   reviewers' required-issues list maps to a visible change.

## Do not infer

- Do not project the '27 deadline pair onto a future edition; each CFP resets dates,
  time zones, tracks, and revision rules.
- Do not assume the fall deadline mirrors the spring one within an edition — read the
  fall HotCRP page itself.
- Do not treat artifact badges, Community Award terms, or presenter obligations as
  stable; they live on per-edition pages.
- When two official pages disagree, the newer CFP or a direct note from the program
  co-chairs controls; record the conflict in your submission log.
