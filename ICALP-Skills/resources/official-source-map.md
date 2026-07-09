# Official Source Map - ICALP (EATCS)

Access date: 2026-07-09

This map records the official and cross-check sources used for ICALP-specific facts in this
pack. ICALP is the main annual conference of the **European Association for Theoretical Computer
Science (EATCS)**; its proceedings appear open-access in **LIPIcs** (Leibniz International
Proceedings in Informatics, Schloss Dagstuhl). ICALP runs on a **single annual deadline** and a
**two-track** structure — Track A (Algorithms, Complexity and Games) and Track B (Automata, Logic,
Semantics and Theory of Programming). Reopen the current-cycle call, the Important Dates page, and
the LIPIcs author instructions before giving submission-ready advice.

## Access method note

Direct fetches of `conf.researchr.org`-style hosts were not needed here, but the ICALP 2026 site
(`icalppodcspaa2026.cs.rhul.ac.uk`), the CFP PDF host (`callforpaper.org`), the mailing-list
archives (`lists.seas.upenn.edu`, `mail-archive.com`), `wikicfp.com`, and `dmatheorynet.blogspot.com`
each returned **HTTP 403** to a direct fetch from the verification gateway on 2026-07-09. Official
text was therefore read through **search-engine renderings of the exact CFP URLs** (the TYPES-announce
and DMANET postings of the ICALP 2026 Call for Papers, the Royal Holloway ICALP 2026 site, and the
Track A/Track B HotCRP pages) and cross-checked against **dblp** (`dblp.org/db/conf/icalp/`), the
**LIPIcs/DROPS** volume at Dagstuhl (`drops.dagstuhl.de`, `LIPIcs.ICALP.2026`), and **eatcs.org**.
Facts that could not be pinned to two independent surfaces are labeled **待核实**.

Naming note: ICALP is *not* a US theory venue. It is EATCS's European flagship; do not conflate its
calendar, format, or review model with STOC, FOCS, or SODA (ACM/SIAM venues with their own rules).

## Primary official sources

| # | Source URL | What it verifies | Access date |
|---|---|---|---|
| 1 | https://icalppodcspaa2026.cs.rhul.ac.uk/icalp/ | ICALP 2026 identity: 53rd EATCS ICALP, Royal Holloway (Egham, UK), co-located with PODC and SPAA; Track A / Track B; LIPIcs proceedings | 2026-07-09 |
| 2 | https://lists.seas.upenn.edu/pipermail/types-announce/2025/012199.html | ICALP 2026 Call for Papers (TYPES-announce rendering): dates, 15-page extended-abstract + appendix/full-version rule, anonymity, no-simultaneous-submission, awards | 2026-07-09 |
| 3 | http://dmatheorynet.blogspot.com/2025/12/dmanet-icalp-2025-12-icalp-2026-call.html (DMANET ICALP 2026 CFP posting) | Cross-rendering of the same CFP: Track A/B scope, lightweight double-blind, Track B rebuttal 21-24 Mar 2026 | 2026-07-09 |
| 4 | https://icalp2026-a.hotcrp.com/ | ICALP 2026 **Track A** HotCRP submission site and deadlines | 2026-07-09 |
| 5 | https://icalp2026-b.hotcrp.com/ | ICALP 2026 **Track B** HotCRP submission site (rebuttal-enabled) | 2026-07-09 |
| 6 | https://drops.dagstuhl.de/entities/series/LIPICs | LIPIcs series home: open-access Dagstuhl proceedings; the `lipics-v2021` document class and 20-page (e.g. 15+5) style recommendation | 2026-07-09 |
| 7 | https://dblp.org/db/conf/icalp/icalp2026.html | dblp ICALP 2026 record; LIPIcs ICALP 2026 volume, proceedings editors | 2026-07-09 |
| 8 | https://www.eatcs.org/index.php/international-colloquium | EATCS ICALP series page: ICALP as EATCS's main conference; Track A/B tradition | 2026-07-09 |
| 9 | https://www.sigact.org/prizes/g%C3%B6del.html + https://eatcs.org/index.php/godel-prize | Gödel Prize (jointly EATCS/ACM SIGACT), presented at ICALP in even years; EATCS Award, Presburger Award, EATCS Distinguished Dissertation Award | 2026-07-09 |
| 10 | https://conferences.au.dk/icalp2025/submission-guidelines | ICALP 2025 submission guidelines (immediate prior cycle): the ≤15-page-excluding-references-and-appendix norm and the omitted-proofs-or-full-version appendix rule, used to corroborate the 2026 format | 2026-07-09 |

## Verified 2026 facts used in skills

- **ICALP 2026 is the 53rd EATCS International Colloquium on Automata, Languages, and Programming**,
  held at **Royal Holloway, University of London** (Egham, UK), with the main colloquium on
  **July 7-10, 2026** and workshops on **July 6, 2026**, co-located with **PODC 2026** and **SPAA
  2026** (sources 1, 7).
- **Two tracks:** **Track A — Algorithms, Complexity and Games**; **Track B — Automata, Logic,
  Semantics and Theory of Programming** (sources 1, 2, 8).
- **ICALP 2026 calendar (AoE):** abstract registration **3 February 2026**, full submission
  **6 February 2026**; **Track B rebuttal 21-24 March 2026**; author notification **20 April 2026**;
  conference July 7-10 (sources 2, 3, 4, 5).
- **Submission format:** an **extended abstract of at most 15 pages**, *excluding* references and a
  *clearly labelled appendix*; the appendix may be either omitted proofs or a **full version**, read
  at the program committee's discretion. Use of the **LIPIcs document class (`lipics-v2021`)** is an
  option but not required at submission; accepted papers must comply with the LIPIcs style
  (sources 2, 10, 6).
- **Review is lightweight double-blind:** submissions are anonymous and self-references must be in
  the third person. **Track B has a rebuttal**; **Track A** authors are contacted only if there are
  correctness issues (no general rebuttal) (sources 2, 3).
- **No prior publication and no simultaneous submission** to another conference or journal is
  allowed (source 2).
- **Publication venue is LIPIcs** — the open-access Leibniz International Proceedings in Informatics
  at Schloss Dagstuhl; volumes are free to read and there is no author-facing APC in the LIPIcs model
  (sources 6, 7).
- **Awards:** best paper and best student paper for **each** track (student-only papers must be
  marked at submission). The colloquium also hosts the **EATCS Award**, the **Presburger Award**
  (young scientist), the **EATCS Distinguished Dissertation Award**, and the **Gödel Prize**
  (jointly EATCS/ACM SIGACT, presented at ICALP in even years) (sources 2, 9).
- **Program Committee chairs (reported):** Track A co-chairs **Sayan Bhattacharya** (University of
  Warwick) and **Danupon Nanongkai** (MPI-INF); Track B chaired by **Michael Benedikt** (University
  of Oxford), with **Gabriele Puppis** listed among the LIPIcs ICALP 2026 proceedings editors
  (sources 3, 7).

## The pure-theory model (why there is no artifact evaluation)

ICALP is a **pure theoretical-computer-science venue**. There is **no artifact-evaluation track and
no ACM/IEEE-style badge scheme** — the paper *is* its proofs. The analogue of an artifact here is the
**full version**: complete, checkable proofs in a clearly labelled appendix and/or an arXiv/ECCC/HAL
posting the reviewers can consult. This pack therefore adapts the usual "artifact" and
"reproducibility" skills to **proof rigor and full-version norms** rather than runnable code. A paper
whose central contribution *is* an implementation or an experiment is usually mis-routed and belongs
at an experimental-algorithms or systems venue (see `icalp-topic-selection`).

## No editor-in-chief; the LIPIcs open-access model

Like every conference in this collection, ICALP has **no standing editor-in-chief**; the rotating
analogue is the per-edition **Program Committee chairs** for Track A and Track B and the local
Organizing Committee, under the **EATCS** and the ICALP steering committee. LIPIcs is **open access**
with no reader paywall; the cost model is conference registration plus Dagstuhl's publication charge,
and at least one author presents each accepted paper.

## Still cycle-volatile (verify every year)

- All dates and AoE cutoffs, and whether both tracks share a single submission deadline.
- The exact page limit and whether the LIPIcs class is mandatory *at submission* (the ≤15-page +
  appendix norm is verified for 2025/2026, but re-read the current call). **待核实** for any future
  cycle's exact number.
- Whether Track A also gains a rebuttal, and the Track B rebuttal window.
- **ICALP 2026 acceptance rate and number of accepted papers** (**待核实** — not confirmed to two
  surfaces at access time).
- **Camera-ready deadline and LIPIcs production timeline** for 2026 (**待核实** — exact date not
  pinned).
- **ICALP 2027 host and location** (**待核实** — not confirmed at access time).
- The exact 2026 PC-chair rosters beyond the names above, and Gabriele Puppis's precise Track B role
  (**待核实** — Puppis is confirmed only as a proceedings editor).
- Any generative-AI use / disclosure policy (**待核实**).
