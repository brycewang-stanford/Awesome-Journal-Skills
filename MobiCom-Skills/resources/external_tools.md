# External Tools - MobiCom

Access date: 2026-07-09

Open these surfaces at the start of every MobiCom engagement. The venue reissues its rules
per edition and runs two deadlines per year, so a link that answered a winter-round
question can be superseded by the summer-round update of the same page — and the two rounds
feed different editions.

## Live official surfaces

- MobiCom current-edition site: https://www.sigmobile.org/mobicom/ (navigate to the year)
- MobiCom 2026 conference page: https://www.sigmobile.org/mobicom/2026/
- MobiCom 2026 Call for Papers: https://www.sigmobile.org/mobicom/2026/cfp.html
- Per-edition HotCRP site: `https://mobicom<yy>.hotcrp.com/` — the `/deadlines` page on it
  is the authoritative clock (e.g., https://mobicom26.hotcrp.com/deadlines).
- MobiCom artifact evaluation (model page): https://www.sigmobile.org/mobicom/2025/artifact_cfp.html
- SIGMOBILE Test-of-Time Paper Award: https://www.sigmobile.org/grav/awards/test-of-time-paper
- dblp MobiCom stream (venue verification for citations): https://dblp.org/db/conf/mobicom/
- ACM Digital Library MobiCom proceedings: https://dl.acm.org/conference/mobicom

If `sigmobile.org`, `hotcrp.com`, or `dblp.org` refuses direct fetches (all three returned
HTTP 403 during this pack's verification), read the exact URLs through search-engine
renderings and cross-check at least two independent renderings before trusting a date.

## Author-side verification passes

Run each pass against the exact files you will upload, not the working draft.

1. **Clock pass.** Confirm on the HotCRP `/deadlines` page which **round** is open, its
   **abstract-registration** date, its **paper** date, and that the cutoff is **AoE** — the
   page may print a US-Eastern clock time (the March 14, 2026 winter round showed 7:59 am
   EDT for an 11:59 pm AoE deadline). Confirm which **edition** the round feeds. Write each
   coauthor's local-time equivalent from the page, not from memory.
2. **Budget pass.** 12 single-spaced numbered pages **including figures and tables**, in
   the double-column geometry (columns 9.25in x 3.33in, 0.33in gutter, ≤55 lines/column,
   ≥10pt, US letter); references and appendices ride outside the cap. Verify with a
   page-by-page scan of the compiled PDF and confirm nothing decision-critical sits past
   page 12.
3. **Blindness pass.** Mechanical sweep for names, affiliations, funding, acknowledgments,
   repository owners, and PDF metadata — then the wireless-specific sweep for identity
   leaks that generic checks miss: testbed/building names, IRB or deployment-site
   identifiers, and dataset URLs.

```bash
pdftotext submission.pdf - | grep -nEi 'university|corp|inc\.|acknowledg|grant|@[a-z]+\.(com|edu)' | head
pdfinfo submission.pdf | grep -Ei 'author|creator|producer'
grep -rnEi '/Users/|/home/|github\.com/[a-z0-9-]+|testbed-[a-z]+' *.tex figures/ | head  # paths, repos, testbed names
```

4. **Status pass.** In HotCRP, "complete" is the only state that counts; the abstract must
   be registered at the earlier deadline, all authors and conflicts entered, topic
   selections set for the reviewer profile you want, and title/abstract matching the PDF.
5. **Revision/rebuttal pass.** For a **rebuttal**, confirm the length limit and that every
   response maps to a specific reviewer point. For a **one-shot revision**, confirm the
   change-highlighted PDF and change summary are attached and that every item on the
   reviewers' required-changes list maps to a visible edit.

## Do not infer

- Do not project one round's dates or which edition it feeds onto another round; each CFP
  and each `/deadlines` page resets them.
- Do not assume the summer round mirrors the winter round of the same year — read the
  round's own HotCRP page.
- Do not treat artifact badges, the rebuttal length, presenter obligations, or the AoE
  convention as stable; they live on per-edition pages.
- When two official pages disagree, the newer CFP or a direct note from the program chairs
  controls; record the conflict in your submission log.
