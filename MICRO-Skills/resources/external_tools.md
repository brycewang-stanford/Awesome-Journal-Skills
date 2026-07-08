# External Tools - MICRO

Access date: 2026-07-08. Reopen every URL for the current cycle before acting on
it; MICRO rules are re-set each edition. If a page 403s from your environment, use
a search-engine rendering of the exact URL and cross-check ACM DL / IEEE Xplore /
dblp, as documented in [`official-source-map.md`](official-source-map.md).

## Official cycle surfaces

- MICRO 2026 hub: https://www.microarch.org/micro59/
- Call for Papers: https://www.microarch.org/micro59/submit/papers.php
- Submission guidelines (format, anonymity, conduct): https://www.microarch.org/micro59/submit/guidelines.php
- Sample-paper PDF (format reference): https://www.microarch.org/micro59/submit/micro59-sample-paper.pdf
- Industry Track CFP: https://www.microarch.org/micro59/submit/industrial.php
- HotCRP submission site: https://micro2026.hotcrp.com/ (deadlines page: `/deadlines`)
- Past symposia index (ordinal/lineage checks): https://microarch.org/past.html
- AE pattern anchor (2025; check for a micro59 equivalent): https://www.microarch.org/micro58/submit/artifacts.php

## Community and award surfaces

- ACM SIGMICRO: https://www.sigmicro.org/
- MICRO Test of Time Award: https://www.sigmicro.org/awards/tot/
- MICRO Hall of Fame: https://www.sigmicro.org/micro-hall-of-fame/
- SIGARCH calls-for-contributions mirror: https://www.sigarch.org/call-contributions/micro-2026/
- IEEE TCCA CFP mirror: https://ieeetcca.org/2026/02/16/micro-2026-call-for-papers/

## Bibliographic authorities (venue-attribution checks)

- dblp MICRO series: https://dblp.org/db/conf/micro/index.html
- ACM DL proceedings (recent editions), e.g. 58th: https://dl.acm.org/doi/proceedings/10.1145/3725843
- IEEE Xplore conference record: https://ieeexplore.ieee.org/xpl/conhome/1000440/all-proceedings

## Sibling-venue calendars (for the lattice in `micro-workflow`)

- ASPLOS: https://www.asplos-conference.org/
- ISCA: https://iscaconf.org/
- HPCA: current-cycle page via https://conf.researchr.org/ (e.g., hpca-2027 track)

## Five author-side verification passes

1. **Clock pass** — deadlines re-read from the live CFP *and* the HotCRP deadlines
   page, timezone noted (2026 used EDT, not AoE), converted per co-author.
2. **Geometry pass** — page count vs the current limit, no-appendix rule honored,
   9pt floor eyeballed on print, page numbers present, template untouched.
3. **Bibliography pass** — zero "et al." entries, all authors named, venue
   attribution of key citations confirmed on dblp/ACM DL/Xplore.
4. **Anonymity pass** — PDF metadata, artifact links anonymized-or-removed, no
   acknowledgments, third-person self-citations, config files inside linked repos
   scrubbed of hostnames/paths.
5. **Portal pass** — abstract registered before the early gate, all HotCRP fields
   (topics, conflicts, authors) complete, final PDF re-downloaded and checksummed,
   second author confirms the submission state.

## Do not infer

- Do not project 2026 dates, page limits, or the EDT convention onto 2027.
- Do not assume the Industry Track, the AE badge set, or the rebuttal/revision
  mechanics repeat next cycle.
- Do not treat a passing HotCRP format check as format compliance — the 2026
  guidelines reserve rejection after visual inspection.
- On conflict between pages, the newest official CFP/guidelines text or direct
  chair communication wins; record the conflict in the source map.
